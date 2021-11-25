from typing import List, Dict

from shop_bridge_core.models import Item


class Storage:
    @staticmethod
    def add_new_item(item: Dict):
        item_obj = Item.objects.create(
            name=item["name"],
            description=item["description"],
            price=item["price"],
            metadata=item["metadata"],
            availability_status=item.get("availability_status", True)
        )

        return item_obj.id

    @staticmethod
    def get_all_items() -> List[Dict]:
        items = Item.objects.all()
        items = [
            {
                "item_id": item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "metadata": item.metadata,
                "availability_status": item.availability_status
            }
            for item in items
        ]
        return items

    @staticmethod
    def update_item(item_id: str, item_details: Dict):
        item = Item.objects.get(id=item_id)
        if item_details.get("name"):
            item.name = item_details.get("name")
        if item_details.get("description"):
            item.description = item_details.get("description")
        if item_details.get("price"):
            item.price = item_details.get("price")
        if item_details.get("metadata"):
            item.metadata = item_details.get("metadata")
        if item_details.get("availability_status"):
            item.metadata = item_details.get("availability_status")

        item.save()

    @staticmethod
    def delete_item(item_id: str):
        Item.objects.filter(id=item_id).delete()
