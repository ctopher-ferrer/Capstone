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


ALTER table Vehicle_Data
add column IsLuxuryBrand TEXT

UPDATE Vehicle_Data
SET IsLuxuryBrand = IIF(VehicleBrand in (SELECT BrandName from LuxuryCarBrands),'Yes','No')



create table Annual_Maintenance_Cost (
VehicleType TEXT,
AnnualMaintenanceCost INT )

INSERT into Annual_Maintenance_Cost (VehicleType,AnnualMaintenanceCost)
VALUES
("Regular Gasoline",949),
("Electric Vehicle",619),
("Hybrid",949)