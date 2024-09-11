-- average_score.sql
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE total_score INT;
    DECLARE total_count INT;

    SELECT SUM(score), COUNT(*) INTO total_score, total_count
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users SET users.average_score = total_score / total_count
    WHERE users.id = user_id;
END; $$
DELIMITER ;
