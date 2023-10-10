
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('test_album1', 2021, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('test_album2', 2022, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('test_album3', 2023, 3);
