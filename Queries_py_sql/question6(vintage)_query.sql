WITH first_table AS (
SELECT
        vintages.name AS wine_name,
        countries.name AS country_name,
        vintages.ratings_average,
        vintages.ratings_count,
        (vintages.ratings_average * vintages.ratings_count) AS sum_average
FROM
    vintages
JOIN
    wines ON vintages.wine_id = wines.id
JOIN
    regions ON wines.region_id = regions.id
JOIN
    countries ON regions.country_code = countries.code
)

SELECT
    country_name,
    SUM(ratings_count) AS total_ratings_count,
    ROUND(SUM(sum_average),2) AS total_sum_average,
    ROUND(SUM(sum_average) / SUM(ratings_count),2) AS weighted_average_rating,
    COUNT(wine_name) AS wines_per_country

FROM
    first_table
GROUP BY
    country_name
ORDER BY weighted_average_rating DESC;