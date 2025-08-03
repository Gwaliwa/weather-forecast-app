import requests

API_KEY = "5832303d3d5709adc0ac16ec6e986e29"

def get_data(place, forecast_days=None, kind=None):
    url= f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    #filter data
    n_value = 8 * forecast_days
    filtered_data = filtered_data[:n_value]

    response = requests.get(url)
    data=response.json()
    filtered_data = data["list"]
    n_value = 8 * forecast_days
    filtered_data = filtered_data[:n_value]
    return (filtered_data)



if __name__== "__main__":
    print(get_data(place="Tokyo", forecast_days=3))


