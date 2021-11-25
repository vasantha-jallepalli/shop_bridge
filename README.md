# initial setup
1. activate virtual environment
2. install requirements by using command `pip install -r requirements.txt`
3. run command to apply migrations `python manage.py migrate`

# runserver
run command to run server `python manage.py runserver`

# To use admin panel
1. run command to create user `python manage.py createsuperuser`
2. open base url + `/admin`
3. login with credential provided while creating user

# Testing
1. run command `pytest` to run tests
2. run command to run jupyter notebook
3. open url
4. open `api_testing.ipynb` and run shells for testing

# API's
- To add item `shop_bridge_core/item/add/v1`
    - `POST` method
    - request
      ```
      {
          "name": "item1",
          "description": "item 1",
          "price": 10.1,
          "metadata": {},
          "availability_status": True
      }
      ```
    - response
       ```
       {
          "item_id": item_id
       }
       ```
- Get items `shop_bridge_core/items/v1`
    - `GET` method
    - response
       ```
       [
          {
             "name": "item1",
             "description": "item 1",
             "price": 10.1,
             "metadata": {},
             "availability_status": True
          }
       ]
       ```
- Update item(update `item_id` in base url)`shop_bridge_core/item/{item_id}/update/v1`
    - `PUT` method
    - request
      ```
      {
          "name": "item1",
          "description": "item 1",
          "price": 10.1,
          "metadata": {},
          "availability_status": True
      }
      ```
- Delete item(update `item_id` in base url)`shop_bridge_core/item/1/delete/v1`
    - `DELETE` method
