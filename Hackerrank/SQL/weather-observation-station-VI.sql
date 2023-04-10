/*
Enter your query here.
*/
SELECT DISTINCT CITY FROM STATION 
    WHERE LEFT(CITY , 1) IN ('a','e','i','o','u');

/*
An alternative solution is to use expression like WHERE CITY LIKE [aeiouAEIOU]%
This command performs the same function as the above code
 */
