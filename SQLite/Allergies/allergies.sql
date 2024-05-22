-- Schema: CREATE TABLE "allergies" ("task" TEXT, "item" TEXT, "score" INT NOT NULL, "result" TEXT);
-- Task: update the bob allergies and set the result based on the task.
--       - The `allergicTo` task expects `true` or `false` based on the `score` and the `item` fields.
--       - For the `list` task you have to write corresponding items to the result field

create temp table matches (kkey text, vvalue int);
insert into matches(kkey,vvalue) values
    ('eggs', 1),
    ('peanuts', 2),
    ('shellfish', 4),
    ('strawberries', 8),
    ('tomatoes', 16),
    ('chocolate', 32),
    ('pollen', 64),
    ('cats', 128);

update allergies set result = (
    case
    when (select vvalue from matches where kkey = item) & score
    then 'true'
    else 'false'
    end
)
where task ='allergicTo';

update allergies set result = (
    case
    when score = 0 then ''
    else
    (select group_concat(kkey ,', ')
    from matches
    where ((score&255)&vvalue)=vvalue)
    end
)
where task ='list';
