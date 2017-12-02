DROP TABLE IF EXISTS "course" CASCADE;
CREATE TABLE "course" (
 "id" SERIAL PRIMARY KEY,
 "name" VARCHAR(50) UNIQUE NOT NULL,
 "price" NUMERIC(8,2) NOT NULL
);

DROP TABLE IF EXISTS "lecture" CASCADE;
CREATE TABLE "lecture" (
 "id" SERIAL PRIMARY KEY,
 "name" VARCHAR(50) NOT NULL,
 "course_id" INT4 REFERENCES "course"("id") ON DELETE CASCADE,
 "content" TEXT NOT NULL
);

DROP TABLE IF EXISTS "user" CASCADE;
CREATE TABLE "user" (
 "id" SERIAL PRIMARY KEY,
 "login" VARCHAR(50) UNIQUE NOT NULL,
 "password" VARCHAR(256) NOT NULL
);

DROP TABLE IF EXISTS "mark" CASCADE;
CREATE TABLE "mark" (
 "course_id" INT4 REFERENCES "course"("id") ON DELETE CASCADE,
 "user_id" INT4 REFERENCES "user"("id") ON DELETE CASCADE,
 "mark" NUMERIC(1,1) CHECK ("mark" > 0 AND "mark" <= 5.0),
 "comment" TEXT,
 "date" TIMESTAMP NOT NULL,
 PRIMARY KEY ("course_id", "user_id")
);

DROP TABLE IF EXISTS "session" CASCADE;
CREATE TABLE "session"(
 "id" SERIAL PRIMARY KEY,
 "start_date" DATE NOT NULL,
 "end_date" DATE NOT NULL,
 "course_id" INT4 REFERENCES "course"("id") ON DELETE CASCADE
);

DROP TABLE IF EXISTS "session_users" CASCADE;
CREATE TABLE "session_users"(
 "session_id" INT4 NOT NULL,
 "user_id" INT4 NOT NULL,
 PRIMARY KEY ("session_id", "user_id"),
 FOREIGN KEY ("session_id") REFERENCES "session"("id") ON DELETE CASCADE,
 FOREIGN KEY ("user_id") REFERENCES "user"("id") ON DELETE CASCADE
);

