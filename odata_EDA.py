# %%
import requests

# %%
# ## Tutorial links
# - https://www.odata.org/getting-started/basic-tutorial/
# - https://www.odata.org/getting-started/advanced-tutorial/
# %%
root_url = "https://services.odata.org/V4/TripPinServiceRW/"
index = requests.get(url=root_url).json()
index
# %%
people = requests.get(url=f"{root_url}People?$top=2&$select=FirstName,LastName").json()
people
# %%
# make a request using urlencoded query string
# curl \
#   --get \
#   --verbose \
#   --header 'Accept: application/json' \
#   --data-urlencode '$filter=Discontinued eq false' \
#   --data-urlencode '$select=ProductName' \
#   --data-urlencode '$top=3' \
#   --data-urlencode '$orderby=ProductID' \
#   --url 'https://services.odata.org/V4/Northwind/Northwind.svc/Products'
# %%
products = requests.get(
    url=f"{root_url}People",
    params={
        "$top": 2,
        "$select": "FirstName,LastName"
    }
).json()
products
# %%
data_binary = """
--batch_36522ad7-fc75-4b56-8c71-56071383e77b
Content-Type: application/http
Content-Transfer-Encoding:binary GET serviceRoot/Airlines HTTP/1.1
Accept: application/json;odata.metadata=minimal --batch_36522ad7-fc75-4b56-8c71-56071383e77b
Content-Type: application/http
Content-Transfer-Encoding:binary
Content-ID: 1 POST serviceRoot/Airlines HTTP/1.1
OData-Version: 4.0
Content-Type: application/json;odata.metadata=minimal
Accept: application/json;odata.metadata=minimal {
"@odata.type" : "Microsoft.OData.SampleService.Models.TripPin.Airline",
"AirlineCode" : "EK",
"Name" : "Emirates Airline"
} --batch_36522ad7-fc75-4b56-8c71-56071383e77b"""
requests.post(
    url=f"{root_url}$batch",
    headers={
        "OData-Version": "4.0",
        "Content-Type": "multipart/mixed; boundary=batch_36522ad7-fc75-4b56-8c71-56071383e77b",
        "Accept": "multipart/mixed"
    },
    data=data_binary
).json()
# %%
