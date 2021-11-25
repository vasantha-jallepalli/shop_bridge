import json
from typing import Dict

from django.http import HttpResponse, HttpResponseNotFound,\
    HttpResponseBadRequest
from shop_bridge_core.storage import Storage
from django.core.exceptions import ObjectDoesNotExist


def add_item(request):
    if request.method != "POST":
        return HttpResponseNotFound(status=404)

    storage = Storage()
    try:
        item = json.loads(request.body)
    except:
        return HttpResponseBadRequest("A valid json is required")

    try:
        validate_creation_data(item)
    except Exception as msg:
        return HttpResponseBadRequest(msg)

    item_id = storage.add_new_item(item)
    response = {
        "item_id": item_id
    }
    response = json.dumps(response)
    return HttpResponse(response, status=201)


def validate_creation_data(item: Dict):

    if not item.get("name"):
        raise Exception("name is required")
    if not item.get("description"):
        raise Exception("description is required")
    if not item.get("price"):
        raise Exception("price is required")

    if type(item["name"]) != str:
        raise Exception("name should be a valid string value")
    if type(item["description"]) != str:
        raise Exception("description should be a valid string value")
    if type(item["price"]) != float:
        raise Exception("price should be a valid float value")


def update_item(request, item_id):
    if request.method != "PUT":
        return HttpResponseNotFound(status=404)

    storage = Storage()
    try:
        item = json.loads(request.body)
    except:
        return HttpResponseBadRequest("A valid json is required")

    try:
        validate_updation_data(item)
    except Exception as msg:
        return HttpResponseBadRequest(msg)

    try:
        storage.update_item(item_id, item)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest("Item not exist!")

    return HttpResponse("Successfully updated!", status=200)


def validate_updation_data(item: Dict):
    if item.get("name") and type(item["name"]) != str:
        raise Exception("name should be a valid string value")
    if item.get("description") and type(item["description"]) != str:
        raise Exception("description should be a valid string value")
    if item.get("price") and type(item["price"]) != float:
        raise Exception("price should be a valid float value")


def delete_item(request, item_id):
    if request.method != "DELETE":
        return HttpResponseNotFound(status=404)

    storage = Storage()

    storage.delete_item(item_id)

    return HttpResponse("Successfully deleted!", status=200)


def get_items(request):
    if request.method != "GET":
        return HttpResponseNotFound(status=404)

    storage = Storage()

    items = storage.get_all_items()
    response = json.dumps(items)

    return HttpResponse(response, status=200)
