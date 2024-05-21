CREATE TABLE "fridge" (
	"fridgeNumber"	INTEGER UNIQUE,
	"color"	TEXT,
	"brand"	TEXT,
	PRIMARY KEY("fridgeNumber")
);

INSERT INTO item_fridge(color, brand)
VALUES ('Red', 'Samsung')

INSERT INTO item_fridge(color, brand)
VALUES ('Yellow', 'LG')