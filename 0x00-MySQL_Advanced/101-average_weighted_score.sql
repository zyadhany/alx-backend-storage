-- Procedure: ComputeAverageWeightedScoreForUsers
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE total_score INT;
    DECLARE total_count INT;

    DECLARE user_cursor CURSOR FOR
    SELECT id FROM user;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

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

        IF total_count IS NOT NULL AND total_count != 0 THEN
            UPDATE user SET user.average_score = total_score / total_count
            WHERE user.id = user_id;
        END IF;
    END LOOP;

    CLOSE user_cursor;
    DEALLOCATE PREPARE user_cursor;
END $$

DELIMITER ;
