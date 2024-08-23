SELECT
    countries.name AS country_name,
    ROUND(SUM(wines.ratings_average)/COUNT(countries.name), 4) AS average_rating
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