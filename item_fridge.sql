CREATE TABLE "item_fridge" (
	"itemID"	INTEGER UNIQUE,
	"fridgeNumber"	TEXT,
	"itemName"	VARCHAR(255),
	"freshDay"	INTEGER,
	"entryDate"	TEXT,
	"expiryDate"	TEXT,
	"exitDate"	TEXT,
	PRIMARY KEY("itemID" AUTOINCREMENT)
);

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 1, 'milk', 5, '2024-05-16')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 1, 'broccoli', 5, '2024-05-17')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 2, 'eggs', 14, '2024-05-17')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 2, 'banana', 4, '2024-05-16')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 2, 'yoghurt', 10, '2024-05-18')

