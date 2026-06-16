from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

def get_products(request):

    products = list(
        Product.objects.values(
            'id',
            'name',
            'category',
            'sub_category',
            'price',
            'availability'
        )
    )

    return JsonResponse(products, safe=False)

def get_product(request, id):

    try:

        product = Product.objects.get(id=id)

        data = {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "sub_category": product.sub_category,
            "price": str(product.price),
            "material": product.material,
            "dimension": product.dimension,
            "availability": product.availability,
        }

        return JsonResponse(data)

    except Product.DoesNotExist:

        return JsonResponse(
            {"error": "Product not found"},
            status=404
        )

@csrf_exempt
def create_product(request):

    if request.method == 'POST':

        body = json.loads(request.body)

        product = Product.objects.create(
            name=body['name'],
            category=body['category'],
            sub_category=body['sub_category'],
            price=body['price'],
            tagline=body['tagline'],
            description=body['description'],
            material=body['material'],
            dimension=body['dimension'],
            availability=body['availability'],
            image='products/default.jpg'
        )

        return JsonResponse(
            {
                "message": "Product created",
                "id": product.id
            },
            status=201
        )

    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )
    
@csrf_exempt
def update_product(request, id):

    if request.method == 'PUT':

        try:

            product = Product.objects.get(id=id)

            body = json.loads(request.body)

            product.name = body['name']
            product.price = body['price']
            product.availability = body['availability']

            product.save()

            return JsonResponse({
                "message": "Product updated"
            })

        except Product.DoesNotExist:

            return JsonResponse(
                {"error": "Product not found"},
                status=404
            )

    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )
    
@csrf_exempt
def delete_product(request, id):

    if request.method == 'DELETE':

        try:

            product = Product.objects.get(id=id)

            product.delete()

            return JsonResponse({
                "message": "Product deleted"
            })

        except Product.DoesNotExist:

            return JsonResponse(
                {"error": "Product not found"},
                status=404
            )

    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )
    
