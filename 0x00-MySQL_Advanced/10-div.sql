-- function: SafeDiv
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
BEGIN
    DECLARE res float DEFAULT 0;
    if b != 0 THEN
        res = a / b;
    END IF;
    RETURN res;
END; //
DELIMITER;
