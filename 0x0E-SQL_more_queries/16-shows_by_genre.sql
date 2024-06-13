-- This Script lists all shows and all genres linked to that show from
-- the database hbtn_0d_tvshows

SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
ORDER BY title ASC, name ASC;
