-- Schema: CREATE TABLE "darts" ("x" REAL, "y" REAL, score INTEGER);
-- Task: update the darts table and set the score based on the x and y values.

update darts set score=10 where (sqrt(power(abs(x),2)+power(abs(y),2)))<=1;
update darts set score=5 where (sqrt(power(abs(x),2)+power(abs(y),2)))<=5 and (sqrt(power(abs(x),2)+power(abs(y),2)))>1;
update darts set score=1 where (sqrt(power(abs(x),2)+power(abs(y),2)))<=10 and (sqrt(power(abs(x),2)+power(abs(y),2)))>5;
update darts set score=0 where (sqrt(power(abs(x),2)+power(abs(y),2)))>10;
