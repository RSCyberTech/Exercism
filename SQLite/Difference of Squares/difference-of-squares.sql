-- Schema: CREATE TABLE "difference-of-squares" ("number" INT", property" TEXT, "result" INT);
-- Task: update the difference-of-squares table and set the result based on the number and property fields.
update "difference-of-squares"
set result = case property
when 'squareOfSum'
then power((number*(number+1)/2),2)
when 'sumOfSquares'
then  (number*(number+1)*(2*number+1))/6
when 'differenceOfSquares'
then power((number*(number+1)/2),2)-(number*(number+1)*(2*number+1))/6
end;