from app import app
from flask import request
from app.constituency_view import ConstituencyData
from app.county_view import CountyData
from app.ward_view import WardData
from flask import jsonify

constituency = ConstituencyData()
county = CountyData()
ward = WardData()

######################################################
# Default Route
######################################################
@app.route("/")
def home_page_route():
    return jsonify({
        "Message": "This the home page, visit /api/v1 for more information",
    }), 200

@app.route("/api/v1")
def default_route():
    return jsonify({
        "Ward Routes": "/ward/*",
        "Constituency Routes": "/constituency/*",
        "County Routes": "/county/*",
    }), 200


######################################################
# Ward Routes
######################################################
@app.route("/api/v1/ward")
def ward_routes():
    return jsonify({
        "Create a Ward": "[GET] /ward/new",
        "Delete a Ward": "[DELETE] /ward/delete/<int:code>",
        "Fetch a Ward": "[GET] /ward/get/<int:code>",
        "Fetch all Wards": "[GET] /ward/get/all",
        "Update a ward": "[PUT] /ward/update/<int:code>",
    }), 200

@app.route("/api/v1/ward/new", methods=["POST"])
def create_ward():
    return jsonify(ward.add_new_ward(
        request.json.get('name'),
        request.json.get('constituency_code')
    )), 201

@app.route("/api/v1/ward/delete/<int:code>", methods=["DELETE"])
def delete_ward(code):
    county.delete_ward(code)
    return jsonify({}), 204
    
@app.route("/api/v1/ward/get/<int:code>", methods=["GET"])
def get_ward(code):
    return jsonify(ward.fetch_ward(code)), 200
    
@app.route("/api/v1/ward/get/all", methods=["GET"])
def get_wards():
    return jsonify(ward.fetch_all_wards()), 200

@app.route("/api/v1/ward/update/<int:code>", methods=["PUT"])
def update_ward(code):
    return jsonify(ward.update_ward(code,
        request.json.get('name'),
        request.json.get('constituency_code'))), 200


######################################################
# Constituency Routes
######################################################

@app.route("/api/v1/constituency$")
def constituency_routes():
    return jsonify({
        "Create a Constituency": "[POST] /constituency/new",
        "Delete a Constituency": "[DELETE] /constituency/delete/<int:code>",
        "Fetch a Constituency": "[GET] /constituency/get/<int:code>",
        "Fetch all Constituencies": "[GET] /constituency/get/all",
        "Update a Constituency": "[PUT] /constituency/update/<int:code>",
    }), 200
    
@app.route("/api/v1/constituency/new", methods=["POST"])
def create_constituency():
    return jsonify(constituency.add_new_constituency(
        request.json.get('name'),
        request.json.get('county_code')
    )), 201

@app.route("/api/v1/constituency/delete/<int:code>", methods=["DELETE"])
def delete_constituency(code):
    constituency.delete_constituency(code)
    return jsonify({}), 204

@app.route("/api/v1/constituency/get/<int:code>", methods=["GET"])
def get_constituency(code):
    return jsonify(constituency.fetch_constituency(code)), 200

@app.route("/api/v1/constituency/get/all", methods=["GET"])
def get_constituencies():
    return jsonify(constituency.fetch_all_constituencies()), 200
    
@app.route("/api/v1/constituency/update/<int:code>", methods=["PUT"])
def update_constituency(code):
    return jsonify(constituency.update_constituency(code,
        request.json.get('name'),
        request.json.get('county_code'))), 200


######################################################
# County Routes
######################################################

@app.route("/api/v1/county")
def county_routes():
    return jsonify({
        "Create a County": "[POST] /county/new",
        "Delete a County": "[DELETE] /county/delete/<int:code>",
        "Fetch a County": "[GET] /county/get/<int:code>",
        "Fetch all Counties": "[GET] /county/get/all",
        "Update a County": "[PUT] /county/update/<int:code>",
    }), 200

@app.route("/api/v1/county/new", methods=["POST"])
def create_county():
    return jsonify(county.add_new_county(
        request.json.get('name')
    )), 201

@app.route("/api/v1/county/delete/<int:code>", methods=["DELETE"])
def delete_county(code):
    county.delete_county(code)
    return jsonify({}), 204
    
@app.route("/api/v1/county/get/<int:code>", methods=["GET"])
def get_county(code):
    return jsonify(county.fetch_county(code)), 200

@app.route("/api/v1/county/get/all", methods=["GET"])
def get_counties():
    return jsonify(county.fetch_all_counties()), 200
    
@app.route("/api/v1/county/update/<int:code>", methods=["PUT"])
def update_county(code):
    return jsonify(county.update_county(code, request.json.get('name'))), 200