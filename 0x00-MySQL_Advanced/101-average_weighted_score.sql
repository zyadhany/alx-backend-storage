-- Procedure: ComputeAverageWeightedScoreForUsers
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_cursor CURSOR FOR
    SELECT id FROM user;

    OPEN user_cursor;

    FETCH NEXT FROM user_cursor INTO @user_id;

    WHILE @@FETCH_STATUS = 0
    BEGIN

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

        FETCH NEXT FROM user_cursor INTO @user_id;
    END;

END; $$
DELIMITER ;