import pandas as pd

travel_details = pd.read_pickle("/home/odysseus/Documents/Travel_agency_project/Travel_details_org_dataset_pickle.pkl")
print(travel_details)


def get_top_values(col_name,counts):
    top_cities = (travel_details[col_name].value_counts()).to_frame().reset_index().head(n=counts)
    dict_top_city  = top_cities.to_dict('records')
    return dict_top_city

def comparing_data_col(observing_col,relation_col):
    col_comparison = travel_details[[observing_col, relation_col]]
    result_by_comp = col_comparison.groupby(relation_col)
    result_by_comp = result_by_comp.first().reset_index().to_dict('records')
    return result_by_comp

def get_max_value(col_name):
    max_result = travel_details[col_name].max()
    max_result = max_result.to_dict()
    return max_result

def get_min_value(col_name):
    min_result = travel_details[col_name].min()
    min_result = min_result.to_dict()
    return min_result