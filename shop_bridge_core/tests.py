import json

import pytest

from django.urls import reverse
from shop_bridge_core.models import Item


@pytest.mark.django_db
def test_create_item(client):
    data = {
        "name": "item1",
        "description": "item 1",
        "price": 10.1,
        "metadata": {},
        "availability_status": False
    }
    json_data = json.dumps(data)
    url = reverse('add_item')
    response = client.post(
        url, data=json_data, content_type="application/json")

    assert response.status_code == 201
    content = json.loads(response.content)
    assert Item.objects.filter(id=content["item_id"]).exists()
    item = Item.objects.get(id=content["item_id"])
    assert item.name == data["name"]
    assert item.description == data["description"]
    assert item.price == data["price"]
    assert item.metadata == json.dumps(data["metadata"])


@pytest.mark.django_db
def test_update_item(client):
    item_obj = Item.objects.create(
        name="test",
        description="test description",
        price=10,
    )
    data = {
        "name": "item1",
        "description": "item 1",
        "price": 10.1,
        "metadata": json.dumps({"key": "value"})
    }
    json_data = json.dumps(data)
    url = f"/shop_bridge_core/item/{item_obj.id}/update/v1"
    response = client.put(
        url, data=json_data, content_type="application/json")

    assert response.status_code == 200
    assert Item.objects.filter(id=item_obj.id).exists()
    item = Item.objects.get(id=item_obj.id)
    assert item.name == data["name"]
    assert item.description == data["description"]
    assert item.price == data["price"]
    assert item.metadata == data["metadata"]


@pytest.mark.django_db
def test_delete_item(client):
    item_obj = Item.objects.create(
        name="test",
        description="test description",
        price=10,
    )
    data = {
        "name": "item1",
        "description": "item 1",
        "price": 10.1,
        "metadata": json.dumps({"key": "value"})
    }
    json_data = json.dumps(data)
    url = f"/shop_bridge_core/item/{item_obj.id}/delete/v1"
    response = client.delete(
        url, data=json_data, content_type="application/json")

    assert response.status_code == 200
    assert not Item.objects.filter(id=item_obj.id).exists()


@pytest.mark.django_db
def test_get_items(client):
    item = Item.objects.create(
        name="item1",
        description="item 1",
        price=10.1,
        metadata=json.dumps({"key": "value"})
    )
    data = [{
        "item_id": item.id,
        "name": "item1",
        "description": "item 1",
        "price": 10.1,
        "metadata": json.dumps({"key": "value"}),
        "availability_status": True
    }]
    url = f"/shop_bridge_core/items/v1"
    response = client.get(
        url, content_type="application/json")

    assert response.status_code == 200
    content = json.loads(response.content)
    assert content == data
