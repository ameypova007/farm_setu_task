import requests

# For ranked ordered statistics
first_line = ['jan', 'year', 'feb', 'year', 'mar', 'year', 'apr', 'year', 'may', 'year', 'jun', 'year', 'jul', 'year',
              'aug', 'year', 'sep', 'year', 'oct', 'year', 'nov', 'year', 'dec', 'year', 'win', 'year', 'spr', 'year',
              'sum', 'year', 'aut', 'year', 'ann', 'year']
years_list = []
pair_wise_list = []
with open("/Users/ameyprakashmalunjkar/Desktop/resp.txt", "r+") as file_open:
    for line in file_open.readlines()[6:]:
        splitted_lines = line.split()
        summed = list(zip(first_line, splitted_lines))
        for i in range(len(summed) - 1):
            if i % 2 == 0:
                # dic = {}
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
print(pair_wise_list)
# Store this data into mango collection'

years_list = []
first_line = ['year', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'win', 'spr', 'sum', 'aut', 'ann']
pair_wise_list = []
with open("/Users/ameyprakashmalunjkar/Desktop/resp.txt", "r+") as file_open:
    for line in file_open.readlines()[6:]:
        splited_lines = line.split()
        summed = list(zip(first_line, splited_lines))
        for i in range(1, len(summed)):
            list1 = list(summed[i])
            year = summed[0][1]
            dic = {}
            if year not in years_list:
                years_list.append(year)
                dic[list1[0]] =  list1[1]
                pair_wise_list.append({year:dic})
            else:
                for dicts in pair_wise_list:
                    for _,val in enumerate(dicts):
                        if val==year:
                            dicts[year].update({list1[0]:list1[1]})  
