-- Script that lists all shows contained in hbtn_0d_tvshows

SELECT
	tv_shows.title AS title,
	tv_show_genres.genre_id AS genre_id
FROM
	tv_shows
JOIN
	tv_show_genres
ON
	tv_shows.id = tv_show_genres.show_id
JOIN
	tv_genres
ON
	tv_genres.id = tv_show_genres.genre_id
ORDER BY
	tv_shows.title ASC,
	tv_show_genres.genre_id ASC;
