#!/usr/bin/env python
# coding: utf-8

# In[1]:


from travel_resp import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def bargraph_plotting():
    response = trip_data()
    modified_reponse = parsing_response_data(api_response=response)
# def bar_graph_plotting():
#     response = parsing_response_data()
#     travel_df = pd.DataFrame(response)
#     # result_value = list(response.values())[0]
#     # result_key = list(response.keys())[0]
#     # print(f"key - {result_key}, value - {result_value})")
#     # travel_df = pd.DataFrame(result_value).T.reset_index()
#     print(f"dataframe\n {travel_df}")
#     x_axis = travel_df.columns[0]
#     # y_axis = travel_df.columns[1]
#     # print(f"graph_  - {result_value}")
#     sns.barplot(data=travel_df, x = x_axis, y = 'counts')
#     plt.xticks(rotation=45)
#     plt.xlabel(x_axis)
#     plt.ylabel('counts')
#     plt.title('Highest datas')
#     plt.show()

# # def area_graph_plotting():
# #     result = parsing_response_data()
# #     travel_df = pd.DataFrame(result).T.reset_index()
# #     travel_df.columns = ['']
# #     print(travel_df)


bargraph_plotting()


# In[5]:


def name_api():
    num = int(input("Enter number: "))
    name = 'city'
    return {num:name}
def checking_number():
    api = name_api()
    number = list(api.keys())[0]
    print(number)
    api_name = list(api.values())[0]
    print(api_name)
    url = f"http://{api_name}?range={number}"
    print(url)
checking_number()


# In[10]:


try:
    count = int(input("Enter a number: "))
    if count == None or count == 0:
        count = 2
        print(count)
except Exception as err:
    print(err)


# In[ ]:




