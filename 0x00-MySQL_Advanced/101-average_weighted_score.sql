-- Procedure: ComputeAverageWeightedScoreForUsers
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE users ADD COLUMN total_score INT NOT NULL;
    ALTER TABLE users ADD COLUMN num_proect INT NOT NULL;

    UPDATE users
    SET total_score = (
            SELECT SUM(corrections.score * projects.weight)
            FROM corrections
                INNER JOIN projects
                    ON corrections.project_id = projects.id
            WHERE corrections.user_id = users.id
            );
    
    UPDATE users
        SET num_proect = (
            SELECT SUM(projects.weight)
                FROM corrections
                    INNER JOIN projects
                        ON corrections.project_id = projects.id
                WHERE corrections.user_id = users.id
            );

    UPDATE users
        SET users.average_score = users.total_score / users.num_proect;
    
    ALTER TABLE users DROP COLUMN total_score;
    ALTER TABLE users DROP COLUMN num_proect;
END $$
DELIMITER ;
