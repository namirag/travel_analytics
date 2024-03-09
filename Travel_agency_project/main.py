# get_highest_countaccommodation_type
from data_analytics import * 
from flask import Flask,jsonify,json,redirect,request
import requests


app = Flask(__name__)


@app.route("/get_highestcount_nationality", methods = ['GET'])
def get_highest_nationality():
    count = json.loads(request.args.get("range"))
    result = get_top_values(col_name='traveller_nationality', counts=count)
    return jsonify(result)


@app.route("/get_highestcount_cities", methods = ['GET'])
def get_highest_count_cities():
    count = json.loads(request.args.get("range"))
    result = get_top_values(col_name='city', counts=count)
    return jsonify(result)


@app.route("/get_highestcount_countries", methods = ['GET'])
def get_highest_countcountries():
    count = json.loads(request.args.get("range"))
    result = get_top_values(col_name='country', counts=count)
    return jsonify(result)


@app.route("/get_highestcount_accommodationtype", methods = ['GET'])
def get_highest_countaccommodation_type():
    count = json.loads(request.args.get("range"))
    result = get_top_values(col_name='accommodation_type', counts=count)
    return jsonify(result)


@app.route("/data_by_comparison", methods = ['GET'])
def data_by_comparison():
    
    main_col = request.args.get("col_name")
    related_col = request.args.get("compare_col")
    result = comparing_data_col(observing_col=main_col,relation_col=related_col)
    return jsonify(result)


@app.route("/max_value", methods=['GET'])
def max_value():
    field_name = input("Enter column name :")
    result = get_max_value(col_name=field_name)
    return jsonify({f"maximum value of{field_name}": result})


@app.route("/min_value", methods=['GET'])
def min_value():
    field_name = input("Enter column name :")
    result = get_min_value(col_name=field_name)
    return jsonify({f"minimum value of{field_name}": result})


if __name__ == '__main__':
    app.run(debug=False)