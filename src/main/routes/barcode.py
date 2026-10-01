from flask import Blueprint, request, jsonify
from src.helpers.http_request import HttpRequest
from src.helpers.barcode_generate import BarcodeGenerate

barcode_routes_bp = Blueprint("barcode_routes", __name__)


@barcode_routes_bp.route("/barcode-generate", methods=["POST"])
def barcode_generate():
    http_request = HttpRequest(body=request.json)
    barcode_response = BarcodeGenerate.validate_and_generate(request=http_request)
    return jsonify(barcode_response.body), barcode_response.status_code
