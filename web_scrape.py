import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


url = "https://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&year1=2022&year2=2022&minmsrpsel=0&maxmsrpsel=0&city=0&hwy=0&comb=0&cbvtgasoline=Gasoline&cbvtelectric=Electric&YearSel=2022&make=&mclass=&vfuel=&vtype=Gasoline%2C+Electric&trany=&drive=&cyl=&MpgSel=000&sortBy=Comb&Units=&url=SearchServlet&opt=new&minmsrp=0&maxmsrp=0&minmpg=0&maxmpg=0&sCharge=&tCharge=&startstop=&cylDeact=&rowLimit=200&pageno=1&tabView=0"
response = requests.get(url)
results = soup(response.content, "html.parser")

table_data = results.find_all("td")
columns= [value.text.replace("\n","").replace("\t","").replace("\r","") for value in table_data]
# print(columns)

column_names = ["Vehicle",
                "Blank1",
                "All_MPG",
                "Blank2",
                "Combined_MPG",
                "MPG_Type",
                "City_MPG",
                "HWY_MPG",
                "Blank3",
                "Text1",
                "Text_city",
                "Text_hwy",
                "Fuel_Rate",
                "Text2",
                "Blank4",
                "Annual_Fuel_Cost",
                "MSRP",
                "Car_Spec1",
                "Car_Spec2",
                "Total_Range"
]

car_dict = {}

# enumerate through column_names to load dictionary with the correct and value from columns data
for idx, key in enumerate(column_names):
    car_dict[key] = columns[idx:][::20]

    df = pd.DataFrame(car_dict)
    # print(df)

df.to_csv("Sample_Car_Data.csv",index=False)