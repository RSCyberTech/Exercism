-- Schema: CREATE TABLE "color_code" ("color1" TEXT, "color2" TEXT, "result" INT);
-- Task: update the color_code table and set the result based on the two colors.
update color_code set result = case color1
when 'black' then 0
when 'brown' then 1
when 'red' then 2
when 'orange' then 3
when 'yellow' then 4
when 'green' then 5
when 'blue' then 6
when 'violet' then 7
when 'grey' then 8
when 'white' then 9
end;
update color_code set result = case color2
when 'black' then cast((cast(result as text)||cast(0 as text)) as int)
when 'brown' then cast((cast(result as text)||cast(1 as text)) as int)
when 'red' then cast((cast(result as text)||cast(2 as text)) as int)
when 'orange' then cast((cast(result as text)||cast(3 as text)) as int)
when 'yellow' then cast((cast(result as text)||cast(4 as text)) as int)
when 'green' then cast((cast(result as text)||cast(5 as text)) as int)
when 'blue' then cast((cast(result as text)||cast(6 as text)) as int)
when 'violet' then cast((cast(result as text)||cast(7 as text)) as int)
when 'grey' then cast((cast(result as text)||cast(8 as text)) as int)
when 'white' then cast((cast(result as text)||cast(9 as text)) as int)
end;
