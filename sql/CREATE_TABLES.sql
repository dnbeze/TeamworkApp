-- Table: public.user
DROP TABLE IF EXISTS public."user" CASCADE;
CREATE TABLE IF NOT EXISTS public."user"
(
    "userID" integer PRIMARY KEY,
    username char(100) NOT NULL,
    password char(100) NOT NULL
);


INSERT INTO public."user" VALUES
	(1, 'test', 'test');

--SELECT * FROM public."user"



-- Table: public.userInfo
DROP TABLE IF EXISTS public."userInfo" CASCADE;
CREATE TABLE IF NOT EXISTS public."userInfo"
(
    "userID" integer PRIMARY KEY NOT NULL,
    FirstName char(100) NOT NULL,
    LastName char(100) NOT NULL,
	Email char(100) NOT NULL,
	FOREIGN KEY ("userID") REFERENCES public."user" ("userID")
);

INSERT INTO public."userInfo" VALUES
	(1, 'Test', 'User', 'TestUser@TestUser.com');
	
	
-- Table: public.workout
DROP TABLE IF EXISTS public."workout" CASCADE;
CREATE TABLE IF NOT EXISTS public."workout"
(
    "workoutID" integer PRIMARY KEY NOT NULL,
    Weight char(100) NOT NULL,
    Repetitions integer NOT NULL,
	"userID" integer REFERENCES public."userInfo" ("userID") NOT NULL
);

INSERT INTO public."workout" VALUES
	(1, '155', 12, 1);
	
	
-- Table: public.workoutDetail
DROP TABLE IF EXISTS public."workoutDetail" CASCADE;
CREATE TABLE IF NOT EXISTS public."workoutDetail"
(
    "workoutID" integer REFERENCES public."workout" ("workoutID") NOT NULL,
    WorkoutName char(100) NOT NULL,
    WorkoutType char(100) NOT NULL,
	BodyPart char(100) NOT NULL
);

INSERT INTO public."workoutDetail" VALUES
	(1, 'Bench Press', 'Bench', 'Chest');
	
