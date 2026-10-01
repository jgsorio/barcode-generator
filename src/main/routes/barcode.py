from flask import Blueprint, request, jsonify

barcode_routes_bp = Blueprint("barcode_routes", __name__)


@barcode_routes_bp.route("/barcode-generate", methods=["POST"])
def barcode_generate():
    return jsonify({"request": request.json})
