-- function: SafeDiv
CREATE FUNCTION SafeDiv(a INT, b INT)
BEGIN
    if n = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;
