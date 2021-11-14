from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import JsonResponse
import multiprocessing
import requests
from django.core.paginator import Paginator

from .models import db
import json
# from celery import shared_task


class UkWebOpr(View):
    """
    This class is to do an operations on UK website
    """
    @staticmethod
    def multiprocess(order, country, parameter):
        """
        This method is to make a multiprocessing.
        """
        collection_name = db['weather_data']
        response = requests.get(f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/{order}/{country}.txt")
        collection_name.insert({"country": country, "data": response.text, "order": order, "parameter": parameter})

    @staticmethod
    def post(request):
        """
        This method is for batch processing which will fetch data from the UK web
        and store in mongoDB.
        """
        orders = ['ranked', 'date']
        country_list = ['UK', 'Northern_Ireland', 'England_and_Wales', 'Wales', 'Scotland', 'England_N',
        'England_S', 'Scotland_N', 'Scotland_E', 'Scotland_W', 'England_E_and_NE', 'England_NW_and_N_Wales',
        'Midlands', 'East_Anglia', 'England_SW_and_S_Wales', 'England_SE_and_Central_S']

        parameters = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall', 'Raindays1mm', 'AirFrost']

        processes = []
        for order in orders:
            for country in country_list:
                for parameter in parameters:
                    process = multiprocessing.Process(
                        target=UkWebOpr.multiprocess,
                        args=(order, country, parameter),
                    )
                    processes.append(process)
                    process.start()
        for process in processes:
            process.join()
        return JsonResponse({"status": "data is stored in DB"}, safe=False)

    @staticmethod
    def pagination_func(pair_wise_list,number_of_elements_per_page, page_number ):
        paginator = Paginator(pair_wise_list, number_of_elements_per_page)
        page_obj = paginator.get_page(page_number)
        return page_obj.object_list

    @staticmethod
    def get(request):
        """
        This method is to get the specific countries data on the basis of year, order and parameter
        """
        collection_name = db['weather_data']
        responses = {}
        number_of_elements_per_page = request.headers.get("Elements-per-page", 10)
        page_number = request.headers.get("Page-number", 1)

        create_query_string = {}
        for params in request.GET:
            if params != "years":
                create_query_string.update({params: request.GET[params]})

        if create_query_string.get("order") == "ranked":
            first_line = ['jan', 'year', 'feb', 'year', 'mar', 'year', 'apr', 'year', 'may', 'year', 'jun', 'year',
                          'jul', 'year',
                          'aug', 'year', 'sep', 'year', 'oct', 'year', 'nov', 'year', 'dec', 'year', 'win', 'year',
                          'spr', 'year',
                          'sum', 'year', 'aut', 'year', 'ann', 'year']
            mongo_res = collection_name.find(create_query_string)
            try:
                for data in mongo_res:
                    with open("resp.txt", "w+") as file2:
                        file2.write(data.get("data"))

                    years_list = []
                    pair_wise_list = []
                    with open("resp.txt", "r+") as file_open:
                        for line in file_open.readlines()[6:]:
                            splitted_lines = line.split()
                            summed = list(zip(first_line, splitted_lines))
                            for i in range(len(summed) - 1):
                                if i % 2 == 0:
                                    list1 = list(summed[i])
                                    list2 = list(summed[i + 1])
                                    year = int(list2[1])
                                    if year not in years_list:
                                        years_list.append(year)
                                        list2[1] = {}
                                        list2[1][first_line[i]] = list1[1]
                                        pair_wise_list.append({year: list2[1]})
                                    else:
                                        for dicts in pair_wise_list:
                                            for _, val in enumerate(dicts):
                                                if val == year:
                                                    dicts[year].update(
                                                        {
                                                            first_line[i]: list1[1]
                                                        }
                                                    )
                    if request.GET.get("years"):
                        for i in pair_wise_list:
                            for _, val in enumerate(i):
                                if request.GET.get("years") not in years_list:
                                    responses.update({data["parameter"]: {
                                        request.GET.get("years"): "No Data Available for this year"}})
                                elif val == int(request.GET.get("years")):
                                    responses.update({data["parameter"]:{request.GET.get("years"): i[val]}})
                    else:
                        responses.update({data["parameter"]: UkWebOpr.pagination_func(pair_wise_list,
                                                                                             number_of_elements_per_page,
                                                                                             page_number)})
                if not responses:
                    responses.update({"error": "Please check the params"})
            except Exception as e:
                return JsonResponse({"error": e}, status=400)

        elif create_query_string.get("order") == "date":
            years_list = []
            first_line = ['year', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec',
                          'win', 'spr', 'sum', 'aut', 'ann']
            pair_wise_list = []
            mongo_res = collection_name.find(create_query_string)
            try:
                for data in mongo_res:
                    with open("resp.txt", "w+") as file2:
                        file2.write(data.get("data"))
                    with open("resp.txt", "r+") as file_open:
                        for line in file_open.readlines()[6:]:
                            splited_lines = line.split()
                            summed = list(zip(first_line, splited_lines))
                            for i in range(1, len(summed)):
                                list1 = list(summed[i])
                                year = summed[0][1]
                                dic = {}
                                if year not in years_list:
                                    years_list.append(year)
                                    dic[list1[0]] = list1[1]
                                    pair_wise_list.append({year: dic})
                                else:
                                    for dicts in pair_wise_list:
                                        for _, val in enumerate(dicts):
                                            if val == year:
                                                dicts[year].update({list1[0]: list1[1]})

                    if request.GET.get("years"):
                        for pair in pair_wise_list:
                            for _, val in enumerate(pair):
                                if request.GET.get("years") not in years_list:
                                    responses.update({data["parameter"]: {
                                        request.GET.get("years"): "No Data Available for this year"}})
                                elif val == request.GET.get("years"):
                                    responses.update({data["parameter"]: {request.GET.get("years"): pair[val]}})
                    else:
                        responses.update({data["parameter"]: UkWebOpr.pagination_func(pair_wise_list, number_of_elements_per_page,page_number)})
                if not responses:
                    responses.update({"error": "Please check the params"})
            except Exception as e:
                return JsonResponse({"error": e}, status=400)

        # At least user should send the order parameter
        else:
            responses.update({"error": "Please check the params"})

        return JsonResponse(responses, safe=False)

# Bydefault pagnation will send the 10 elemets and 1st page

    @staticmethod
    def put(request):
        """
        This method is to insert single data into db or update the existing data
        """
        body = json.loads(request.body)
        order = body.get("order")
        country = body.get("country")
        parameter = body.get("parameter")
        collection_name = db['weather_data']
        if order and country and parameter:
            response = requests.get(
                f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/{order}/{country}.txt")
            collection_name.update_one({"country": country, "order": order, "parameter": parameter}, {"$set": {"country": country, "data": response.text, "order": order, "parameter": parameter}}, upsert=True)
            return JsonResponse({"status" : "Document updated successfully"}, status=200)
        else:
            return JsonResponse({"status": "Please check the params"}, status=400)