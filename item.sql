CREATE TABLE "item" (
	"itemID"	INTEGER UNIQUE,
	"itemName"	TEXT,
	"freshDay"	INTEGER,
	PRIMARY KEY("itemID")
);

INSERT INTO item(itemName, freshDay)
VALUES ('milk', '5')

INSERT INTO item(itemName, freshDay)
VALUES ('tangerine', '7')

INSERT INTO item(itemName, freshDay)
VALUES ('eggs', '14')

INSERT INTO item(itemName, freshDay)
VALUES ('banana', '3')

INSERT INTO item(itemName, freshDay)
VALUES ('apple', '6')
