--1
SELECT FirstName || ' ' || LastName AS customerName, customerID, country 
FROM customers  
WHERE country != 'USA';

--2
SELECT employees.FirstName || ' ' || employees.LastName AS EmployeeName, invoiceId
FROM employees
INNER JOIN customers ON Customers.SupportRepId = Employees.employeeID
INNER JOIN invoices ON invoices.CustomerId = Customers.customerId;

--3
SELECT invoiceId, COUNT(invoiceLineId) 
FROM invoice_items
GROUP BY invoiceId;

--4
SELECT tracks.name, artists.name, invoiceLineId
FROM TRACKS
INNER JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
INNER JOIN artists ON albums.ArtistId = artists.ArtistId;

--5
SELECT name, COUNT(playlist_track.trackId) AS songCount
FROM playlists 
INNER JOIN playlist_track ON playlist_track.playlistId = playlists.PlaylistId
GROUP BY playlists.PlaylistId;

--6
SELECT tracks.Name, albums.Title AS albumName, media_types.Name AS mediaType, genres.Name AS genre
FROM tracks
INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
INNER JOIN genres ON genres.GenreId = tracks.GenreId;

--7 
SELECT employees.FirstName || ' ' || employees.LastName AS EmployeeName, COUNT(invoiceId) as salesMade
FROM employees
INNER JOIN customers ON Customers.SupportRepId = Employees.employeeID
INNER JOIN invoices ON invoices.CustomerId = Customers.customerId
GROUP BY EmployeeName;

--8 
CREATE VIEW sales AS
SELECT employees.FirstName || ' ' || employees.LastName AS employeeName, invoices.Total AS totalSales, invoices.InvoiceDate
FROM employees
INNER JOIN invoices ON invoices.CustomerId=customers.CustomerId
INNER JOIN customers ON customers.SupportRepId=employees.EmployeeId
ORDER BY totalSales DESC;

-- round to two decimal places because thats how money works
SELECT employeeName, ROUND(SUM(totalSales),2) AS sales2010
FROM sales
WHERE InvoiceDate >= '2010-01-01 00:00.00'
AND InvoiceDate <= '2010-12-31 23:59.59'
GROUP BY employeeName
ORDER BY sales2010 DESC
LIMIT 1;

--9
-- rounded here again for the same reason
SELECT employeeName,ROUND(SUM(totalSales),2) AS sales
FROM sales
GROUP BY employeeName
ORDER BY totalSales DESC
LIMIT 1;

--10 
SELECT billingCountry, SUM(invoices.Total) AS totalSales
FROM invoices
GROUP BY billingCountry
ORDER BY totalSales DESC;
--USA customers spent the most 

--11
CREATE VIEW trackCount AS
SELECT tracks.name as Song, albums.Title as Album , artists.Name as Artist, COUNT(invoice_items.trackId*invoice_items.quantity) as totalSold
FROM tracks
INNER JOIN invoice_items ON invoice_items.trackId = tracks.trackId
INNER JOIN invoices ON invoices.invoiceId = invoice_items.invoiceId
INNER JOIN albums ON albums.albumId = tracks.AlbumId
INNER JOIN artists ON artists.ArtistId = albums.ArtistId
WHERE invoices.InvoiceDate >= '2013-01-01 00:00.00'
AND invoices.InvoiceDate <= '2013-12-31 23:59.59'
GROUP BY tracks.trackid
ORDER BY totalSold DESC;

SELECT MAX(totalSold) FROM trackCount;