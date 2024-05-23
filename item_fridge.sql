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
VALUES ( 1, 'tangerine', 7, '2024-05-17')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 2, 'eggs', 14, '2024-05-17')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 2, 'banana', 4, '2024-05-16')

INSERT INTO item_fridge(fridgeNumber, itemName, freshDay, entryDate)
VALUES ( 2, 'apple', 6, '2024-05-19')

UPDATE item_fridge
SET expiryDate = DATE(entryDate, '+' || freshDay || ' days');
