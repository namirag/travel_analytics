import requests
import pandas as pd
import json
     

def trip_data(counts=2):
    # if('http://127.0.0.1:5000/get_highestcount_nationality'.split('/')[3].split('_')[2] == 'nationality'):
     varition_graph = int(input("Enter your choice\n1. Univariate\n2. Bivariate\n3. Multivariate\nchoice: "))

     if (varition_graph == 1):
          try:
               counts = int(input("Enter a number to get top results: "))
          except Exception as err:
               print(f"caught an error: {err}")
          finally:
               print(f"using default value of count {counts}\nif you want to set a new range run code again.")

          print("Enter your choice.")
          choice = int(input("1. Accomodation\n2. City\n3. Country\n4. Nationality\n:-"))
          if(choice == 1):
               url = f'http://127.0.0.1:5000/get_highestcount_accommodationtype?range={counts}'
               api_endpoint = 'accommodation type'
               response = requests.request("GET", url)
               response = response.json()
               return {api_endpoint:response}
          elif(choice == 2):
               url = f'http://127.0.0.1:5000/get_highestcount_cities?range={counts}'
               api_endpoint = 'cities'
               response = requests.request("GET", url)
               response = response.json()
               return {api_endpoint:response}
          elif(choice == 3):
               url = f'http://127.0.0.1:5000/get_highestcount_countries?range={counts}'
               api_endpoint = 'countries'
               response = requests.request("GET", url)
               response = response.json()
               return {api_endpoint:response}
          elif(choice == 4):
               url = f'http://127.0.0.1:5000/get_highestcount_nationality?range={counts}'
               api_endpoint = 'nationality'

     elif(varition_graph == 2):
          xaxis_data = input("Enter x-axis column name to compare: ")
          yaxis_data = input("Enter y-axis column name to compare\nallow only digit field: ")
          url = f'http://127.0.0.1:5000/data_by_comparison?col_name={xaxis_data}&compare_col={yaxis_data}'
          # api_endpoint = {xaxis_data:yaxis_data}
          response = requests.request("GET", url)
          response = response.json()
          return response
     
     elif(varition_graph == 3):
          xaxis_data = input("Enter x-axis column name to compare: ")
          yaxis_data = input("Enter y-axis column name to compare\nallow only digit field: ")
          url = f'http://127.0.0.1:5000/data_by_comparison?col_name={xaxis_data}&compare_col={yaxis_data}'
          # api_endpoint = {xaxis_data:yaxis_data}
          response = requests.request("GET", url)
          response = response.json()
          return {api_endpoint:response}


def parsing_response_data(api_response):

     # print(type(api_response))
     if type(api_response) == list:
          print('list')
          x_col = list((api_response[0]).keys())[0]
          y_col = list((api_response[0]).keys())[1]
          x_vals = []
          y_vals = []
          for val in api_response:
               for key,value in val.items():
                    if key == x_col:
                         y_vals.append(val[key])
                    else:
                         x_vals.append(value)
          # print({x_col:x_vals,y_col:y_vals})
          return {x_col:x_vals,y_col:y_vals}
     else:
          print('dict')
          api_name = list(api_response.keys())[0]
          print(api_name)
          api_data = list(api_response.values())[0]
          print(api_data)
          x_vals = []
          y_vals = []
          for val in api_data:
               for key, value in val.items():
                    if key == 'count':
                         y_vals.append(val[key])
                    else:
                         x_vals.append(value)
          print(f"x - {x_vals}")
          print(f"y - {y_vals}")
          print({api_name:x_vals,'Counts':y_vals})
          return {api_name:x_vals,'Counts':y_vals}

     
     

# resp = trip_data()
# parsing_response_data(api_response=resp)