-- This Script lists all genres not linked to the show Dexter.

-- List all the genres not linked to the show "Dexter"
SELECT tv_genres.name AS name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
AND tv_show_genres.show_id = (
	-- Get the id for the show 'Dexter'
	SELECT id FROM tv_shows
	WHERE title = 'Dexter'
)
WHERE tv_show_genres.genre_id IS NULL
ORDER BY name ASC;
