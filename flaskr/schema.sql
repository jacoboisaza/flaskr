-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS "report" CASCADE;
DROP TABLE IF EXISTS "post" CASCADE;
DROP TABLE IF EXISTS "reported_post" CASCADE;

CREATE TABLE "user" (
  id serial PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE "report" (
  id serial PRIMARY KEY,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES "user" (id)
);

CREATE TABLE "post" (
  id serial PRIMARY KEY,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES "user" (id)
);

CREATE TABLE "reported_post" (
  id serial PRIMARY KEY,
  report_id INTEGER NOT NULL,
  FOREIGN KEY (report_id) REFERENCES "report" (id),
  post_id INTEGER NOT NULL,
  FOREIGN KEY (post_id) REFERENCES "post" (id)
);