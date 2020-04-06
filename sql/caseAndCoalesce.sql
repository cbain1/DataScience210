-- windspeed of swallows (LOL), CASE is basically like if statements
SELECT report_code, year, month, day, wind_speed,
CASE 
    WHEN wind_speed>=40 THEN 'HIGH'
    WHEN wind_speed>=30 AND wind_speed <=40 THEN 'MODERATE'
    ELSE 'LOW'
END AS wind_severity
FROM Station_data;

-- CASE statements use short circuiting to improve runtime
        -- short circuiting operates sequentially, so you don't have to check a condition before, basically it auto puts else if statements after the first when
SELECT report_code, year, month, day, wind_speed,
CASE 
    WHEN wind_speed>=40 THEN 'HIGH'
    WHEN wind_speed>=30 THEN 'MODERATE'
    ELSE 'LOW'
END AS wind_severity
FROM Station_data; 

-- you can also "bar graphing" using CASE   
SELECT year, 
CASE 
    WHEN wind_speed>=40 THEN 'HIGH'
    WHEN wind_speed>=30 THEN 'MODERATE'
    ELSE 'LOW'
END AS wind_severity, COUNT(*)AS record_count
FROM station_data
GROUP BY year, wind_severity;

-- aggregate parcipitation into two different categories: tornado and non-tornado 
SELECT year, month, 
COALESCE(SUM(CASE WHEN tornado=1 THEN precipitation ELSE 0 END),0) AS tornado_precipitation,
COALESCE(SUM(CASE WHEN tornado=0 THEN precipitation ELSE 0 END),0) AS non_tornado_precipitation
FROM station_data
GROUP BY year, month;

--calculate the max
SELECT year, month, 
COALESCE(MAX(CASE WHEN tornado=1 THEN precipitation ELSE 0 END),0) AS tornado_precipitation,
COALESCE(MAX(CASE WHEN tornado=0 THEN precipitation ELSE 0 END),0) AS non_tornado_precipitation
FROM station_data
GROUP BY year, month;

-- calculate the min
SELECT year, month, 
COALESCE(MIN(CASE WHEN tornado=1 THEN precipitation ELSE 0 END),0) AS tornado_precipitation,
COALESCE(MIN(CASE WHEN tornado=0 THEN precipitation ELSE 0 END),0) AS non_tornado_precipitation
FROM station_data
GROUP BY year, month;

-- this may fail on a min/max/avg aggregation
-- for avg, if we set the case value to 0, we will still increase the denominator, but if we set to null we will not 
SELECT year, month, 
COALESCE(AVG(CASE WHEN tornado=1 THEN precipitation ELSE NULL END),0) AS tornado_precipitation,
COALESCE(AVG(CASE WHEN tornado=0 THEN precipitation ELSE NULL END),0) AS non_tornado_precipitation
FROM station_data
GROUP BY year, month;

--write a query to find out if the tornado value ever differs across the tuple(year, month)
SELECT year, month, COUNT(*) AS occurences, SUM(CASE WHEN tornado=1 THEN 1 ELSE 0 END) AS tornado_sum
FROM station_data
WHERE occurences<>tornado_sum
GROUP BY year, month;