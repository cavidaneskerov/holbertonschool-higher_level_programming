--
SElECT tv_shows.title, tv_show_genres.genre_id
FROM tw_shows
JOIN tw_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
