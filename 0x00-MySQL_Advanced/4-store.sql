-- triggers for the store database
CREATE Trigger buy_trigger AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END;
