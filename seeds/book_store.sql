DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);


INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');
