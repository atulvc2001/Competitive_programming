--
--Table: Users
--
--+----------------+---------+
--| Column Name    | Type    |
--+----------------+---------+
--| user_id        | int     |
--| name           | varchar |
--+----------------+---------+
--user_id is the primary key (column with unique values) for this table.
--This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 --
--
--Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
--
--Return the result table ordered by user_id.
--
--The result format is in the following example.
--
 --
--
--Example 1:
--
--Input: 
--Users table:
--+---------+-------+
--| user_id | name  |
--+---------+-------+
--| 1       | aLice |
--| 2       | bOB   |
--+---------+-------+
--Output: 
--+---------+-------+
--| user_id | name  |
--+---------+-------+
--| 1       | Alice |
--| 2       | Bob   |
--+---------+-------+

-- Answer
SELECT USER_ID, 
UPPER(SUBSTRING(NAME FROM 1 FOR 1)) || '' || LOWER(SUBSTRING(NAME FROM 2))
AS NAME
FROM USERS
ORDER BY USER_ID;
