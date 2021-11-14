# farm_setu_task
1. Create a virtual env and activate it.
2. Install all the requirements from the requirements.txt
3. Run the server using python manage.py runserver
4. Use post method for batch processing to store the web data in DB.
5. url to post/insert data : http://127.0.0.1:8000/uk_data/
6. To insert/update single country use put method
   1.http://127.0.0.1:8000/uk_data/
   body :{"order":"date",
   "parameter":"Tmax",
   "country":"UK"}
7. To get the data use get method and send below params
   1. parameter
   2. order (mandatory)
   3. country
   4. years
   5. http://127.0.0.1:8000/uk_data/?parameter=Tmax&order=date&country=UK&years=2001
   6. Note here pagination is applied (by default it will send 1 page's 10 elements)
   7. You can mention page_number and per_page_element in headers.
   8. Sample curl req with headers 
      1. curl --location --request GET 'http://127.0.0.1:8000/uk_data/?parameter=Tmax&order=date&country=UK&years=2001' \
        --header 'elements-per-page: 10' \
        --header 'page-number: 1'
8. Note: In farm_setu/models.py I have used my mongoDB username and password bydefualt.
9. Please set your mongo creds in below envs.
   "MONGO_USER_NAME"
   "MONGO_USER_PASSWORD"

Some Sample Outputs:
1. POST req : {"status": "data is stored in DB"}
2. GET req (with year): {
    "Tmax": {
        "2001": {
            "jan": "5.3",
            "feb": "6.7",
            "mar": "7.4",
            "apr": "10.4",
            "may": "16.3",
            "jun": "16.9",
            "jul": "19.4",
            "aug": "19.3",
            "sep": "15.7",
            "oct": "15.0",
            "nov": "10.0",
            "dec": "6.3",
            "win": "6.32",
            "spr": "11.38",
            "sum": "18.57",
            "aut": "13.57",
            "ann": "12.43"
        }
    }
}
3. GET req (without year):{
    "Tmax": [
        {
            "1884": {
                "jan": "7.3",
                "feb": "6.8",
                "mar": "8.5",
                "apr": "10.1",
                "may": "14.5",
                "jun": "17.1",
                "jul": "18.8",
                "aug": "20.2",
                "sep": "17.0",
                "oct": "11.8",
                "nov": "7.5",
                "dec": "5.8",
                "win": "---",
                "spr": "11.02",
                "sum": "18.73",
                "aut": "12.10",
                "ann": "12.14"
            }
        },
        {
            "1885": {
                "jan": "4.3",
                "feb": "7.3",
                "mar": "7.2",
                "apr": "10.8",
                "may": "11.8",
                "jun": "17.0",
                "jul": "19.4",
                "aug": "16.8",
                "sep": "15.0",
                "oct": "9.3",
                "nov": "7.5",
                "dec": "5.9",
                "win": "5.75",
                "spr": "9.91",
                "sum": "17.76",
                "aut": "10.58",
                "ann": "11.04"
            }
        },
        {
            "1886": {
                "jan": "3.7",
                "feb": "3.4",
                "mar": "6.1",
                "apr": "10.5",
                "may": "13.1",
                "jun": "16.4",
                "jul": "18.7",
                "aug": "18.5",
                "sep": "16.0",
                "oct": "12.9",
                "nov": "8.6",
                "dec": "4.1",
                "win": "4.36",
                "spr": "9.88",
                "sum": "17.87",
                "aut": "12.51",
                "ann": "11.04"
            }
        },
        {
            "1887": {
                "jan": "4.8",
                "feb": "6.9",
                "mar": "6.7",
                "apr": "9.9",
                "may": "13.0",
                "jun": "19.8",
                "jul": "20.7",
                "aug": "19.1",
                "sep": "14.5",
                "oct": "10.0",
                "nov": "6.6",
                "dec": "4.9",
                "win": "5.23",
                "spr": "9.88",
                "sum": "19.87",
                "aut": "10.37",
                "ann": "11.44"
            }
        },
        {
            "1888": {
                "jan": "5.5",
                "feb": "3.7",
                "mar": "5.2",
                "apr": "9.0",
                "may": "14.1",
                "jun": "16.3",
                "jul": "16.0",
                "aug": "16.9",
                "sep": "15.4",
                "oct": "11.4",
                "nov": "8.9",
                "dec": "7.1",
                "win": "4.74",
                "spr": "9.41",
                "sum": "16.38",
                "aut": "11.91",
                "ann": "10.81"
            }
        },
        {
            "1889": {
                "jan": "5.8",
                "feb": "5.2",
                "mar": "7.3",
                "apr": "9.4",
                "may": "15.8",
                "jun": "19.0",
                "jul": "18.1",
                "aug": "17.2",
                "sep": "15.5",
                "oct": "11.1",
                "nov": "8.9",
                "dec": "6.0",
                "win": "6.06",
                "spr": "10.84",
                "sum": "18.09",
                "aut": "11.82",
                "ann": "11.64"
            }
        },
        {
            "1890": {
                "jan": "7.8",
                "feb": "5.5",
                "mar": "8.7",
                "apr": "10.5",
                "may": "15.2",
                "jun": "16.5",
                "jul": "17.0",
                "aug": "17.2",
                "sep": "17.9",
                "oct": "12.5",
                "nov": "8.3",
                "dec": "2.2",
                "win": "6.49",
                "spr": "11.48",
                "sum": "16.90",
                "aut": "12.92",
                "ann": "11.65"
            }
        },
        {
            "1891": {
                "jan": "4.2",
                "feb": "8.5",
                "mar": "6.4",
                "apr": "9.2",
                "may": "12.8",
                "jun": "17.9",
                "jul": "17.7",
                "aug": "16.7",
                "sep": "16.8",
                "oct": "12.0",
                "nov": "7.6",
                "dec": "6.6",
                "win": "4.84",
                "spr": "9.46",
                "sum": "17.42",
                "aut": "12.14",
                "ann": "11.37"
            }
        },
        {
            "1892": {
                "jan": "4.3",
                "feb": "5.4",
                "mar": "5.8",
                "apr": "11.6",
                "may": "14.6",
                "jun": "16.4",
                "jul": "16.9",
                "aug": "17.7",
                "sep": "14.6",
                "oct": "9.4",
                "nov": "8.7",
                "dec": "4.3",
                "win": "5.43",
                "spr": "10.67",
                "sum": "16.97",
                "aut": "10.88",
                "ann": "10.81"
            }
        },
        {
            "1893": {
                "jan": "4.2",
                "feb": "6.5",
                "mar": "11.1",
                "apr": "14.5",
                "may": "16.4",
                "jun": "19.3",
                "jul": "19.1",
                "aug": "20.3",
                "sep": "15.9",
                "oct": "12.4",
                "nov": "7.2",
                "dec": "7.1",
                "win": "4.96",
                "spr": "13.98",
                "sum": "19.56",
                "aut": "11.86",
                "ann": "12.87"
            }
        }
    ]
}
4. GET req witout country:{
    "Scotland_W": {
        "Tmax": {
            "1967": {
                "feb": "6.4",
                "win": "6.08",
                "jun": "16.2",
                "jan": "5.7",
                "sep": "14.9",
                "mar": "7.5",
                "dec": "6.2",
                "aug": "16.6",
                "nov": "7.8",
                "aut": "11.18",
                "apr": "9.8",
                "ann": "10.80",
                "sum": "16.26",
                "oct": "11.0",
                "spr": "9.57",
                "jul": "16.0",
                "may": "11.4"
            }
        }
    }
}
