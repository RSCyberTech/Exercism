-- Schema: CREATE TABLE "twofer" ("input" TEXT, "response" TEXT);
-- Task: update the twofer table and set the response based on the input.
update twofer set response = 'One for '|| iif(input=='' or input==null,'you',input) || ', one for me.'
