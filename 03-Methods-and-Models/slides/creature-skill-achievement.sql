-- Alter and drop existing tables

ALTER TABLE "creature" DROP CONSTRAINT "fk_creature_creature_skill_1";
ALTER TABLE "skill" DROP CONSTRAINT "fk_skill_creature_skill_1";
ALTER TABLE "achievement" DROP CONSTRAINT "fk_achievement_creature_achievement_1";
ALTER TABLE "creature" DROP CONSTRAINT "fk_creature_creature_achievement_1";

DROP TABLE "creature";
DROP TABLE "skill";
DROP TABLE "achievement";
DROP TABLE "creature_skill";
DROP TABLE "creature_achievement";


--create new tables
CREATE TABLE "creature" (
"creature_ID" serial8 NOT NULL,
"creature_type" varchar,
"first_name" varchar,
"last_name" varchar,
"nickname" varchar,
PRIMARY KEY ("creature_ID") 
)
WITHOUT OIDS;
CREATE TABLE "skill" (
"skill_ID" serial8 NOT NULL,
"skill_name" varchar,
"skill_level" varchar,
"skill_constraints" varchar,
PRIMARY KEY ("skill_ID") 
)
WITHOUT OIDS;
CREATE TABLE "achievement" (
"achievement_ID" serial8 NOT NULL,
"name" varchar,
"score" numeric(19),
"achievement_prequisites" varchar,
"achievement_level" varchar,
PRIMARY KEY ("achievement_ID") 
)
WITHOUT OIDS;
CREATE TABLE "creature_skill" (
"creature_id" numeric(19) NOT NULL,
"skill_id" numeric(19) NOT NULL,
PRIMARY KEY ("creature_id", "skill_id") 
)
WITHOUT OIDS;
CREATE TABLE "creature_achievement" (
"creature_ID" numeric(19) NOT NULL,
"achievement_ID" numeric(19) NOT NULL,
"skill_level" varchar NOT NULL,
"skills_used" varchar,
PRIMARY KEY ("creature_ID", "achievement_ID", "skill_level") 
)
WITHOUT OIDS;

-- add foreign keys

ALTER TABLE "creature" ADD CONSTRAINT "fk_creature_creature_skill_1" FOREIGN KEY ("creature_ID") REFERENCES "creature_skill" ("creature_id");
ALTER TABLE "skill" ADD CONSTRAINT "fk_skill_creature_skill_1" FOREIGN KEY ("skill_ID") REFERENCES "creature_skill" ("skill_id");
ALTER TABLE "achievement" ADD CONSTRAINT "fk_achievement_creature_achievement_1" FOREIGN KEY ("achievement_ID") REFERENCES "creature_achievement" ("achievement_ID");
ALTER TABLE "creature" ADD CONSTRAINT "fk_creature_creature_achievement_1" FOREIGN KEY ("creature_ID") REFERENCES "creature_achievement" ("creature_ID");

