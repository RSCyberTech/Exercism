-- Schema: CREATE TABLE "leap" ( "year" INT, "is_leap" BOOL);
-- Task: update the leap table and set the is_leap based on the year field.
update leap set is_leap=case
when mod(year,100)=0 then (case when mod(year,400)=0 then 1 else 0 end)
when mod(year,4)=0 then 1 
else 0
end;
