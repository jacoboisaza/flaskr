-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS "bookmark" CASCADE;
DROP TABLE IF EXISTS "family" CASCADE;
DROP TABLE IF EXISTS "family_leaders" CASCADE;
DROP TABLE IF EXISTS "position" CASCADE;
DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS "post" CASCADE;

CREATE TABLE "family" (
  id serial PRIMARY KEY
);

CREATE TABLE "user" (
  id serial PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  family_id INTEGER,
  FOREIGN KEY (family_id) REFERENCES "family" (id)
);

CREATE TABLE "family_leader" (
  id serial PRIMARY KEY,
  leader_id INTEGER NOT NULL,
  FOREIGN KEY (leader_id) REFERENCES "user" (id),
  family_id INTEGER NOT NULL,
  FOREIGN KEY (family_id) REFERENCES "family" (id)
);

CREATE TABLE "post" (
  id serial PRIMARY KEY,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES "user" (id)
);

CREATE TABLE "bookmark" (
  id serial PRIMARY KEY,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES "user" (id) ON DELETE CASCADE ,
  FOREIGN KEY (post_id) REFERENCES "post" (id) ON DELETE CASCADE
);

CREATE TABLE "position" (
  id serial PRIMARY KEY,
  person_id INTEGER NOT NULL,
  FOREIGN KEY (person_id) REFERENCES "user" (id)
);
