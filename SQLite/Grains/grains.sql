-- Schema: CREATE TABLE "grains" ("task" TEXT, "square" INT, "result" INT);
-- Task: update the grains table and set the result based on the task (and square fields).
update grains set result=round(power(2,square)/2) where square > 0;
update grains set result=round(power(2,65)/2)-1 where square = 0;
