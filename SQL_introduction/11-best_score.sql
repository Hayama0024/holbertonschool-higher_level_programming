-- Select all names and scores from second_table
-- Only scores greater than or equal to 10
-- Results are ordered by score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
