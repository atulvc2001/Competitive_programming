/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CITY,LENGTH(CITY)
FROM (SELECT CITY, LENGTH(CITY) 
FROM STATION ORDER BY LENGTH(CITY), CITY) 
WHERE ROWNUM=1;

SELECT CITY,LENGTH(CITY)
FROM (SELECT CITY, LENGTH(CITY) 
        FROM STATION 
        ORDER BY LENGTH(CITY) DESC, CITY)
        WHERE ROWNUM=1;
