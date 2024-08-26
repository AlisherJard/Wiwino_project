WITH first_table AS (
    SELECT
        wines.name AS wine_name,
        countries.name AS country_name,
        ratings_average,
        ratings_count,
        (ratings_average * ratings_count) AS sum_average
    FROM
        wines
    JOIN
        regions ON wines.region_id = regions.id
    JOIN
        countries ON regions.country_code = countries.code
)

SELECT
    country_name,
    SUM(ratings_count) AS total_ratings_count,
    SUM(sum_average) AS total_sum_average,
    ROUND(SUM(sum_average) / SUM(ratings_count),2) AS weighted_average_rating,
    COUNT(wine_name) AS wines_per_country
FROM
    first_table
GROUP BY
    country_name
ORDER BY weighted_average_rating DESC;