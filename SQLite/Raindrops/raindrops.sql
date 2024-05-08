-- Schema: CREATE TABLE "raindrops" ("number" INT, "sound" TEXT);
-- Task: update the raindrops table and set the sound based on the number.
update raindrops set sound=sound||'Pling' where mod(number,3)=0;
update raindrops set sound=sound||'Plang' where mod(number,5)=0;
update raindrops set sound=sound||'Plong' where mod(number,7)=0;
update raindrops set sound=cast(number as Text) where sound="";
