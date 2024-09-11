-- procedure AddBonus
DELIMITER //
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE total_score INT;
    DECLARE total_count INT;

    SELECT SUM(corrections.score * projects.weight) INTO total_score,
            SUM(projects.weight) INTO total_count
    FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    UPDATE users SET users.average_score = total_score / total_count
    WHERE users.id = user_id;
END; //
DELIMITER ;
