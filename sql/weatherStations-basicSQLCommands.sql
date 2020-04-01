SELECT * FROM station_data;

SELECT COUNT(*) FROM station_data;

SELECT * FROM station_data WHERE year=2010 AND rain=1;

SELECT * FROM station_data WHERE rain=1;

SELECT * FROM station_data WHERE rain=1 AND precipitation <> 0;

SELECT * FROM station_data WHERE year <= 2005 AND year >= 2001;

SELECT * FROM station_data WHERE month%3=0;

SELECT * FROM station_data WHERE month IN(3,6,9,12);

SELECT * FROM station_data WHERE month NOT IN(3,6,9,12);

SELECT * FROM station_data WHERE month=3 OR month=6 OR month=9 OR month=12;

SELECT * FROM station_data WHERE report_code='513A63';

SELECT * FROM station_data WHERE report_code IN ('513A63','1F8A7B','EF616A');

SELECT * FROM station_data WHERE length(report_code)!=6;

SELECT * FROM station_data WHERE report_code LIKE 'A%';

SELECT * FROM station_data WHERE report_code LIKE 'A_C%';

SELECT * FROM station_data WHERE thunder AND fog;

SELECT * FROM station_data WHERE snow_depth IS NULL;

-- count here is an aggregator, so it will count things... hence why it's called count
SELECT COUNT(*) AS record_count FROM station_data;

SELECT COUNT(*) AS record_count FROM station_data WHERE tornado;

-- will produce the years where there were tornados in station_data
SELECT year FROM station_data WHERE tornado;

-- will produce the count for how many tornados there were each year 
SELECT year, COUNT(*) AS record_count FROM station_data WHERE tornado GROUP BY year;

SELECT year, month, COUNT(*) AS record_count FROM station_data WHERE tornado GROUP BY year, month;

-- GROUP BY  tells you how you want count to work
SELECT year, month, COUNT(*) AS record_count FROM station_data WHERE tornado GROUP BY 1,2;

-- ORDER BY only changes how the data looks, not what the results really are
SELECT year, month, COUNT(*) AS record_count FROM station_data WHERE tornado GROUP BY 1,2 ORDER BY 2,1;

-- DESC makes them sort in descending order instead of ascending order
SELECT year, month, COUNT(*) AS record_count FROM station_data WHERE tornado GROUP BY 1,2 ORDER BY 2,1 DESC;

SELECT COUNT(*) FROM station_data WHERE snow_depth IS NULL;

-- by default, when you do a COUNT, it only gives you the non-null entries by default, hence why we have to specify in the above query
SELECT COUNT(snow_depth) AS snow_depth_count FROM station_data;

SELECT rowid FROM station_data;

-- want to know what the average temp (2 sigfigs) of each month for all years (2000+)
SELECT month, ROUND(AVG(temperature),2) AS average_temp FROM station_data WHERE year >=2000 GROUP BY month; 

-- another aggregation function is SUM, you can google a full list if you want 

-- want to know a list of the total snowfall for each month of the year (year>=2000)
SELECT month, SUM(snow_depth) AS total_snowfall FROM station_data WHERE year>=2000 GROUP BY month;

-- having is the analogous command for WHERE, but on groups (or aggregations) instead of on records
-- having is a way to filter groups created by the GROUP option in SELECT, the filter includes/excludes groups based on this condition

-- find all precipitation by year, here HAVING operates on the group wateriscoming
SELECT year, ROUND(SUM(snow_depth),2) AS winteriscoming, ROUND(SUM(precipitation),2) AS wateriscoming
FROM station_data
WHERE year>=2000
GROUP BY year
HAVING wateriscoming >30;

-- distinct records makes sure that every record is unique
SELECT DISTINCT station_number, year
FROM station_data
ORDER BY station_number;

SELECT DISTINCT station_number, year
FROM station_data;

-- the list of unique stations, together with their first year of operation
SELECT DISTINCT station_number, MIN(year)
FROM station_data
GROUP BY station_number
ORDER BY station_number;

-- distinct is unnecesary here because of the way we are aggregating
SELECT DISTINCT station_number, day, MIN(year)
FROM station_data
GROUP BY station_number,day
ORDER BY station_number,day;