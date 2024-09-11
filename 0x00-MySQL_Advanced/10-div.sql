-- function: SafeDiv
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE res float DEFAULT 0;
    if b != 0 THEN
        SET res = a / b;
    END IF;
    RETURN res;
END; //
DELIMITER;
