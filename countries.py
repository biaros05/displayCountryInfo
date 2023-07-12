import requests

def fetch_country_info(country_name):
    base_url = "https://restcountries.com/v3.1/name/" + country_name
    response = requests.get(base_url)

    if response.status_code == 200:
        return(response.json())
    else:
        print("Error fetching data: ", response.status_code)

def display_country_info(country_data):
    if country_data is None:
        return
    
    country_data = country_data[0]
    country_name = country_data["name"]["common"]
    country_timezone = country_data["timezones"]
    country_map = country_data["maps"]["googleMaps"]
    country_flag = country_data["flags"]["png"]

    print(f"Name: {country_name}")
    print(f"Timezones: {country_timezone}")
    print(f"Map: {country_map}")
    print(f"Flag: {country_flag}")


def main():
    country_name = input("Enter a country: ")
    country_data = fetch_country_info(country_name)
    display_country_info(country_data)

if __name__ == "__main__":
    main()

