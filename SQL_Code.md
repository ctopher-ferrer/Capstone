Convert MSRP to integer by removing comma and dollar sign
```SQL
UPDATE Vehicle_Data
set MSRP = replace(replace(MSRP,'$',''),',','')
```

Convert Annual_Fuel_Cost to integer by removing comma and dollar sign
```SQL
UPDATE Vehicle_Data
set Annual_Fuel_Cost = replace(replace(Annual_Fuel_Cost,'$',''),',','')
```

Input zero
```SQL
UPDATE Vehicle_Data
set MSRP = replace(MSRP,' ','0')
```


ALTER table Vehicle_Data
add column Year INTEGER

UPDATE Vehicle_Data
set Year = 2022

UPDATE Vehicle_Data
set Vehicle = replace(Vehicle,'2022 ','')

UPDATE Vehicle_Data
set Vehicle = replace(Vehicle,', Electricity','')

UPDATE Vehicle_Data
set Vehicle = replace(Vehicle,', Regular Gasoline','')

<!-- scrap data below -->
create table VehicleCost as
select Vehicle, MSRP,Annual_Fuel_Cost, MSRP/5 as AnnualMSRP, MSRP/5+Annual_Fuel_Cost as Annual_Payment1, 
(MSRP/5)*2+(Annual_Fuel_Cost*2) as Annual_Payment2, (MSRP/5)*3+(Annual_Fuel_Cost*3) as Annual_Payment3,
(MSRP/5)*4+(Annual_Fuel_Cost*4) as Annual_Payment4, (MSRP/5)*5+(Annual_Fuel_Cost*5) as Annual_Payment5,
(MSRP/5)*5+(Annual_Fuel_Cost*6) as Annual_Payment6, (MSRP/5)*5+(Annual_Fuel_Cost*7) as Annual_Payment7,
(MSRP/5)*5+(Annual_Fuel_Cost*8) as Annual_Payment8, (MSRP/5)*5+(Annual_Fuel_Cost*9) as Annual_Payment9,
(MSRP/5)*5+(Annual_Fuel_Cost*10) as Annual_Payment10,(MSRP/5)*5+(Annual_Fuel_Cost*11) as Annual_Payment11,
(MSRP/5)*5+(Annual_Fuel_Cost*12) as Annual_Payment12
from Vehicle_Data
where MSRP <> 0
order by Annual_Payment12 desc
<!-- scrap data above-->

ALTER table Vehicle_Data
add column IsLuxuryBrand TEXT

UPDATE Vehicle_Data
SET IsLuxuryBrand = IIF(VehicleBrand in (SELECT BrandName from LuxuryCarBrands),'Yes','No')
		