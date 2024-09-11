-- procedure AddBonus
DELIMITER //
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE project_id INT;
    DECLARE project_cound INT;

    SELECT COUNT(*) INTO project_cound FROM projects WHERE name = project_name;

    if project_cound = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END; //
DELIMITER ;
