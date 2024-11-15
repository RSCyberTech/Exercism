-- Schema: CREATE TABLE "eliuds-eggs" ("number" INT, "result" INT);
-- Task: update the eliuds-eggs table and set the result based on the number field.

update "eliuds-eggs" set result = (
    with recursive cte (number,n, c) as(
        select number,number,0 from "eliuds-eggs"
        union all
        select number,n>>1,n&1 from cte
        where n > 0
    )
    select sum(c) from cte where cte.number = "eliuds-eggs".number
);
