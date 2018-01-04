from app import app
from flask import request
from app.constituency_view import ConstituencyData
from app.county_view import CountyData
from app.ward_view import WardData

consituency = ConstituencyData()
county = CountyData()
ward = WardData()

@app.route("/ward")
def ward_routes():
    @app.route("/new", methods=["POST"])
    def create_ward():
        return jsonify(ward.add_new_ward(
            request.form.get('name'),
            request.form.get('constituency_code')
        )), 201

    @app.route("/delete/<int:code>", methods=["DELETE"])
    def delete_ward():
        return ward.delete_ward(code), 204
        
    @app.route("/get/<int:code>", methods=["GET"])
    def get_ward():
        return ward.get_ward(code), 200
        
    @app.route("/get/all", methods=["GET"])
    def get_wards():
        return ward.get_wards(), 200

    @app.route("/update", methods=["PUT"])
    def update_ward():
        return ward.update_ward(
            request.form.get('name'),
            request.form.get('constituency_code')
            request.form.get('code')
        ), 200


@app.route("/constituency")
def constituency_routes():
    
    @app.route("/new", methods=["POST"])
    def create_constituency():
        return jsonify(constituency.add_new_constituency(
            request.form.get('name'),
            request.form.get('county_code')
        )), 201

    @app.route("/delete/<int:code>", methods=["DELETE"])
    def delete_constituency():
        return constituency.delete_constituency(code), 204

    @app.route("/get/<int:code>", methods=["GET"])
    def get_constituency():
        return constituency.get_constituency(code), 200

    @app.route("/get/all", methods=["GET"])
    def get_constituencies():
        return constituency.get_constituencies(), 200
        
    @app.route("/update", methods=["PUT"])
    def update_constituency():
        return constituency.update_constituency(
            request.form.get('name'),
            request.form.get('county_code')
            request.form.get('code')
        ), 200


@app.route("/county")
def county_routes():
    @app.route("/new", methods=["POST"])
    def create_county():
        return jsonify(county.add_new_county(
            request.form.get('name')
        )), 201

    @app.route("/delete/<int:code>", methods=["DELETE"])
    def delete_county():
        return county.delete_county(code), 204
        
    @app.route("/get/<int:code>", methods=["GET"])
    def get_county():
        return county.get_county(code), 200

    @app.route("/get/all", methods=["GET"])
    def get_counties():
        return county.get_counties(), 200
        
    @app.route("/update", methods=["PUT"])
    def update_county():
        return county.update_county(
            request.form.get('name'),
            request.form.get('county_code')
            request.form.get('code')
        ), 200