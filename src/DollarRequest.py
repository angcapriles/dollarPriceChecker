import requests

def fetchDolarPrice():
    _url = "https://s3.amazonaws.com/dolartoday/data.json"
    r = requests.get(_url)
    return {"date":r.json()['_timestamp']['fecha'], "price":r.json()['USD']['promedio']}
if __name__ == "__main__":
    r = fetchDolarPrice()
    print(r)

