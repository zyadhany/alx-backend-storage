-- Query all the bands from the table metal_bands and group them by origin.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC