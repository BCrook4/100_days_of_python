import requests
from datetime import datetime

USERNAME = "bcrook3"
TOKEN = "wr4h829e2hdqefbkas23"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "mins",
    "type": "int",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().date()
today = today.strftime("%Y%m%d")
# print(today)


choice_valid = False
while not choice_valid:
    user_choice = str(input("What would you like to do? Add new pixel, update a pixel, or delete a pixel? (add/update/delete)")).lower()

    if user_choice == "add":
        quantity = str(input("How many minutes of programming did you do today?"))

        pixel_params = {
            "date": today,
            "quantity": quantity,
        }

        response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
        print(response.text)
        break

    elif user_choice == "update":
        date_to_update = str(input("Which day would yo like to update? (yyyyMMdd)"))
        updated_quantity = str(input("What is the updated minutes for this date?"))

        pixel_update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

        update_params = {
            "quantity": updated_quantity,
        }

        response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
        response.raise_for_status()
        print(response.text)
        break

    elif user_choice == "delete":

        date_to_delete = str(input("Which day would yo like to delete? (yyyyMMdd)" ))

        pixel_delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"

        response = requests.delete(url=pixel_delete_endpoint, headers=headers)
        print(response.text)
        break


