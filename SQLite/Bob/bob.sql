-- Schema: CREATE TABLE "bob" ("input" TEXT, "reply" TEXT);
-- Task: update the bob table and set the reply based on the input.

UPDATE bob
SET reply = CASE
    WHEN trim(replace(replace(replace(input,char(9),''),char(10),''),char(13),''))= '' THEN "Fine. Be that way!"
    WHEN substr(trim(input), -1) = '?' AND input = upper(input) AND input != lower(input) THEN "Calm down, I know what I'm doing!"
    WHEN substr(trim(input), -1) = '?' THEN "Sure."
    WHEN input = upper(input) AND input != lower(input) THEN "Whoa, chill out!"
    ELSE "Whatever."
END;
