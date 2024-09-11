-- Index the first letter of the name column in the names table
CREATE INDEX my_names ON names(name(1));
