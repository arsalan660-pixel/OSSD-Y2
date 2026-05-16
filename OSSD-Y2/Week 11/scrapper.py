import requests
from bs4 import BeautifulSoup


car=input("Enter name :")
url=f'https://www.pakwheels.com/new-cars/pricelist/{car}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
response=requests.get(url, headers=headers)


if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
    tables=soup.find_all('table')
    if not tables:
        print("No tables found on the webpage.")
    for table in tables:
        rows=table.find_all('tr')
        for row in rows:
            cols=row.find_all('td')
            if len(cols)>= 2:
                name=cols[0].get_text()
                price=cols[1].get_text()
                print(f"Name: {name}, Price: {price}")     
else:
    print("Failed to retrieve the webpage.")  
#create a function to scrape data from the webpage, the above code can be used inside the function
def scrapper():
    car1 = input("Enter your car name :")
    url1= f'https://www.pakwheels.com/new-cars/pricelist/{car1}'
    header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response=requests.get(url1,headers=header)
    my_cars=[]
    if response.status_code==200 :
        soup=BeautifulSoup(response.text,'html.parser')
        tables=soup.find_all('table')
        if not tables:
            print("No tables found in this webpage")
            return my_cars
        for table in tables:
                rows=table.find_all('tr')
                for row in rows :
                    cols=row.find_all('td')
                    if len(cols)>=2 :
                        name=cols[0].get_text()
                        price=cols[1].get_text()
                        print(f"Name : {name} , Price{price}")
                        my_cars.append(name + "," + price)
        return my_cars
    else :
        print("No data found")
        return my_cars
# create a function to save data to a csv file
def save_to_file(data, filename):
    if not data :
        print("No data to save ")
        return
    file=open(filename,'w')
    file.write("Name,Price\n")
    for car in data :
        file.write(car + "\n")
    file.close()
    print(f"data is stored in {filename}")

print("=== PakWheels Car Price Scraper ===\n")
car_data = scrapper()  
save_to_file(car_data, "car_prices.csv")
