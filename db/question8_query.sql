SELECT countries.name AS Countries,
        keywords.name AS Keywords,
        ROUND(AVG(wines.ratings_average),2) AS Ratings_Average
FROM keywords_wine
JOIN keywords ON keywords_wine.keyword_id = keywords.id
JOIN wines ON keywords_wine.wine_id = wines.id
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE countries.name IN ('Espagne', 'Italie')
GROUP BY Keywords
ORDER BY Ratings_Average DESC;