import requests

API_KEY = "bb794ac36e73c0a3f94acca306b5adc9"

def get_data(place, forecat_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        return "404"
    else:
        filtered_data = data["list"]
        filtered_data = filtered_data[:8*forecat_days]
        return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecat_days=3))