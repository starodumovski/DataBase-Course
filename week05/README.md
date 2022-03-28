# Lab05

### Exercise 1(SQL)
```sql
CREATE TABLE Shipping_addresses
(
addressId INT NOT NULL PRIMARY KEY,
city CHAR(50),
district CHAR(50),
street CHAR(50),
house INT
);
CREATE TABLE Customer
(
clientId INT NOT NULL PRIMARY KEY,
balance INT,
creditLimit INT,
discount INT,
address CHAR(50),
FOREIGN KEY (address)
REFERENCES Shipping_addresses(addressId),
);
CREATE TABLE Orderr
(
client INT,
orderId INT NOT NULL PRIMARY KEY,
date char(10),
address CHAR(50),
FOREIGN KEY (address)
REFERENCES Shipping_addresses(addressId),
FOREIGN KEY (client)
REFERENCES Customer(clientId)
);
CREATE TABLE Item
(
itemId INT NOT NULL PRIMARY KEY,
description CHAR(50)
);
CREATE TABLE Includes
(
includesId INT NOT NULL PRIMARY KEY,
quantity INT,
oID INT NOT NULL,
iID INT,
FOREIGN KEY (oID)
REFERENCES Orderr(orderId),
FOREIGN KEY (iID)
REFERENCES Item(itemId)
);
CREATE TABLE Manufacturer
(
manufactureId INT NOT NULL PRIMARY KEY,
phonenumber INT
);
CREATE TABLE Produce
(
produceId INT NOT NULL PRIMARY KEY,
quantity INT,
iID INT NOT NULL,
mID INT,
FOREIGN KEY (mID)
REFERENCES Manufacturer(manufacturerId),
FOREIGN KEY (iID)
REFERENCES Item(ItemId)
);
```

### Exercise 2(SQL)

```sql
CREATE TABLE Item (
itemId INT NOT NULL PRIMARY KEY
);

CREATE TABLE Plant
(
plantId INT NOT NULL PRIMARY KEY,
iId INT,
FOREIGN KEY (iId)
REFERENCES Item(itemId)
);

CREATE TABLE Company
(
companyId INT NOT NULL PRIMARY KEY,
pId INT,
FOREIGN KEY (pId)
REFERENCES Plant(plantId)
);

CREATE TABLE "Group"
(
groupId INT NOT NULL PRIMARY KEY,
cId INT,
FOREIGN KEY (cId)
REFERENCES Company(companyId)
);

CREATE TABLE Structure
(
companyId INT NOT NULL PRIMARY KEY,
daughter INT,
FOREIGN KEY (daughter)
REFERENCES Company(companyId)
);
```

### Exercise 3(SQL)
```sql
CREATE TABLE Airport
(
IATACode INT NOT NULL PRIMARY KEY
);

CREATE TABLE FlightLeg
(
flightLegId INT NOT NULL PRIMARY KEY,
startAirport INT, 
endAirport INT,
FOREIGN KEY (startAirport)
REFERENCES Airport(IATACode),
FOREIGN KEY (endAirport)
REFERENCES Airport(IATACode),
);

CREATE TABLE DailyFlightLegCombination
(
DFLegId INT NOT NULL PRIMARY KEY,
flId INT,
FOREIGN KEY (flId)
REFERENCES FlightLeg(flightLegId)
);

CREATE TABLE Flight
(
flightNum INT NOT NULL PRIMARY KEY,
flId INT,
FOREIGN KEY (flId)
REFERENCES FlightLeg(flightLegId)
);

CREATE TABLE AircraftType
(
dailyId INT NOT NULL PRIMARY KEY,
FOREIGN KEY (dailyId)
REFERENCES DailyFlightLegCombination(DFLegId)
);

CREATE TABLE "Can Land"
(
IATACode INT NOT NULL PRIMARY KEY,
typeID INT NOT NULL PRIMARY KEY
);

```