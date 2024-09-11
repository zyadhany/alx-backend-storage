-- Index the name and score columns in the names table
CREATE INDEX idx_name_first_score on names(name(1), score);
