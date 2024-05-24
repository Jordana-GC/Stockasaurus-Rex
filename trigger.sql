CREATE TRIGGER IF NOT EXISTS calculate_expiry_date
AFTER INSERT ON item_fridge
FOR EACH ROW
BEGIN
    UPDATE item_fridge
    SET expiryDate = date(NEW.entryDate, '+' || NEW.freshDay || ' days')
    WHERE itemID = NEW.itemID;
END;
