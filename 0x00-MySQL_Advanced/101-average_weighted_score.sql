-- Procedure: ComputeAverageWeightedScoreForUsers
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        DECLARE total_score INT;
        DECLARE total_count INT;

        SELECT SUM(corrections.score * projects.weight)
            INTO total_score
            FROM corrections
                INNER JOIN projects
                    ON corrections.project_id = projects.id
            WHERE corrections.user_id = user_id;

        SELECT SUM(projects.weight)
            INTO total_count
            FROM corrections
                INNER JOIN projects
                    ON corrections.project_id = projects.id
            WHERE corrections.user_id = user_id;

        UPDATE users SET users.average_score = total_score / total_count
        WHERE users.id = user_id;

    END LOOP;
    CLOSE cur;
END; $$
DELIMITER ;