from src.helpers.http_request import HttpRequest
from src.helpers.http_response import HttpResponse
from barcode import generate
from barcode.writer import ImageWriter
import os


class BarcodeGenerate:
    @staticmethod
    def validate_and_generate(request: HttpRequest) -> HttpResponse:
        body = request.body
        product_code = body.get("product_code")

        # Perform validation and generate the barcode
        try:
            # Generate the barcode
            if not os.path.exists("images"):
                os.makedirs("images")

            barcode = generate(
                "Code128",
                product_code,
                output=f"images/{product_code}",
                writer=ImageWriter(),
            )
            return HttpResponse(
                200, {"message": "Barcode generated successfully", "file": barcode}
            )

        except Exception as e:
            return HttpResponse(400, {"message": f"Error generating barcode: {str(e)}"})
