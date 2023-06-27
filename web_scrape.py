import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


url = "https://www.fueleconomy.gov/feg/PowerSearch.do?action=PowerSearch&year1=2022&year2=2022&minmsrpsel=0&maxmsrpsel=0&city=0&highway=0&combined=0&cbvtplugin=Plug-in+Hybrid&YearSel=2022&MakeSel=&MarClassSel=&FuelTypeSel=&VehTypeSel=Plug-in+Hybrid&TranySel=&DriveTypeSel=&CylindersSel=&MpgSel=000&sortBy=Comb&Units=&url=SearchServlet&opt=new&minmsrp=0&maxmsrp=0&minmpg=0&maxmpg=0&sCharge=&tCharge=&startstop=&cylDeact=&rowLimit=200"

# print(columns)

# create/list columns for data
column_names = ["Vehicle",
                "Blank1",
                "All_MPG",
                "Blank2",
                "Combined_MPGe",
                "MPGe_Type",
                "Blank3",
                "Blank4",
                "Blank5",
                "TextCombined",
                "Blank6",
                "Blank7",
                "ElectricCarSpecs",
                "Blank8",
                "Combined_MPG",
                "MPGType",
                "Blank9",
                "Blank0",
                "Blank11",
                "TextCombined2",
                "Blank12",
                "Blank13",
                "GasCarSpec",
                "Blank14",
                "Blank15",
                "Annual_Fuel_Cost",
                "MSRP",
                "Car_Spec1",
                "Car_Spec2",
                "Total_Range"
]
# create dictionary for data to load into:
car_dict = {}


# load request data to variable and parse data via BeautifulSoup
response = requests.get(url)
results = soup(response.content, "html.parser")

# filter table data "td" and clean data
table_data = results.find_all("td")
columns= [value.text.replace("\n","").replace("\t","").replace("\r","") for value in table_data]

print(columns)
# enumerate through column_names to load dictionary with the correct and value from columns data
# since data is in a list, enumerate through and skip every 20 because 20 columns,
# load into dataframe to load into SQL
for idx, key in enumerate(column_names):
    car_dict[key] = columns[idx:][::30]

    df = pd.DataFrame(car_dict)
    # print(df)

df.to_csv("SamplePHybrid_Car_Data.csv",index=False)