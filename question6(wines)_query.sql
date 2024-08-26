SELECT
    countries.name AS country_name,
    ROUND(SUM(wines.ratings_average)/COUNT(countries.name), 4) AS average_rating,
    ROUND(AVG(wines.ratings_count),0) AS avg_ratings_count,
    COUNT(wines.name) AS wines_per_country
FROM
    wines
JOIN
    regions ON wines.region_id = regions.id
JOIN
    countries ON regions.country_code = countries.code
GROUP BY
    countries.name
ORDER BY
    average_rating DESC;