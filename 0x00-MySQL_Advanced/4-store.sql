-- triggers for the store database
CREATE Trigger buy_trigger AFTER INSERT ON orders FOR EACH ROW
    UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;
