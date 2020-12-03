import sqlite3

connection = sqlite3.connect('musac.db')
cur = connection.cursor()

f=open("exam2question3.txt","w+")

cur.execute('''SELECT FirstName || ' ' || LastName AS customerName, customerID, country 
FROM customers  
WHERE country != 'USA';''')
print(len(cur.fetchall()),file=f)
print("customerName\tcustomerID\tcountry",file=f)
cur.execute('''SELECT FirstName || ' ' || LastName AS customerName, customerID, country 
FROM customers  
WHERE country != 'USA' LIMIT 10;''')
for row in cur:
	print(row[0],"\t",row[1],"\t",row[2],file=f)
print(file=f)

cur.execute( '''
SELECT employees.FirstName || ' ' || employees.LastName AS EmployeeName, invoiceId
FROM employees
INNER JOIN customers ON Customers.SupportRepId = Employees.employeeID
INNER JOIN invoices ON invoices.CustomerId = Customers.customerId;''')
print(len(cur.fetchall()),file=f)
print("EmployeeName\tinvoiceId",file=f)
cur.execute( '''
SELECT employees.FirstName || ' ' || employees.LastName AS EmployeeName, invoiceId
FROM employees
INNER JOIN customers ON Customers.SupportRepId = Employees.employeeID
INNER JOIN invoices ON invoices.CustomerId = Customers.customerId LIMIT 10;''')
for row in cur:
	print(row[0],"\t",row[1],file=f)
print(file=f)



cur.execute('''SELECT invoiceId, COUNT(invoiceLineId)
FROM invoice_items
GROUP BY invoiceId; ''')
print(len(cur.fetchall()),file=f)
print("invoiceId\tCOUNT(invoiceLineId" ,file=f)
cur.execute('''SELECT invoiceId, COUNT(invoiceLineId) 
FROM invoice_items
GROUP BY invoiceId LIMIT 10; ''')
for row in cur:
	print(row[0],"\t",row[1],file=f)
print(file=f)


cur.execute('''SELECT tracks.name, artists.name AS Artist, invoiceLineId
FROM TRACKS
INNER JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
INNER JOIN artists ON albums.ArtistId = artists.ArtistId; ''')
print(len(cur.fetchall()),file=f)
print("Name\tArtist\t invoiceLineId" ,file=f)
cur.execute('''SELECT tracks.name, artists.name, invoiceLineId
FROM TRACKS
INNER JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
INNER JOIN artists ON albums.ArtistId = artists.ArtistId LIMIT 10; ''')
for row in cur:
	print(row[0],"\t",row[1],"\t",row[2],file=f)
print(file=f)


cur.execute('''SELECT name, COUNT(playlist_track.trackId) AS songCount
FROM playlists 
INNER JOIN playlist_track ON playlist_track.playlistId = playlists.PlaylistId
GROUP BY playlists.PlaylistId;''')
print(len(cur.fetchall()),file=f)
print("Name\tsongCount" ,file=f)
cur.execute('''SELECT name, COUNT(playlist_track.trackId) AS songCount
FROM playlists 
INNER JOIN playlist_track ON playlist_track.playlistId = playlists.PlaylistId
GROUP BY playlists.PlaylistId LIMIT 10;''')
for row in cur:
	print(row[0],"\t",row[1],file=f)
print(file=f)


cur.execute('''SELECT tracks.Name, albums.Title AS albumName, media_types.Name AS mediaType, genres.Name AS genre
FROM tracks
INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
INNER JOIN genres ON genres.GenreId = tracks.GenreId;''')
print(len(cur.fetchall()),file=f)
print("Name\talbumName\tmediaType\tgenre" ,file=f)
cur.execute('''SELECT tracks.Name, albums.Title AS albumName, media_types.Name AS mediaType, genres.Name AS genre
FROM tracks
INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
INNER JOIN genres ON genres.GenreId = tracks.GenreId LIMIT 10;''')
for row in cur:
	print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],file=f)
print(file=f)

cur.execute('''SELECT employees.FirstName || ' ' || employees.LastName AS EmployeeName, COUNT(invoiceId) as salesMade
FROM employees
INNER JOIN customers ON Customers.SupportRepId = Employees.employeeID
INNER JOIN invoices ON invoices.CustomerId = Customers.customerId
GROUP BY EmployeeName; ''')
print(len(cur.fetchall()),file=f)
print("EmployeeName\tsalesMade" ,file=f)
cur.execute('''SELECT employees.FirstName || ' ' || employees.LastName AS EmployeeName, COUNT(invoiceId) as salesMade
FROM employees
INNER JOIN customers ON Customers.SupportRepId = Employees.employeeID
INNER JOIN invoices ON invoices.CustomerId = Customers.customerId
GROUP BY EmployeeName LIMIT 10; ''')
for row in cur:
	print(row[0],"\t",row[1],file=f)
print(file=f)



cur.execute('''
SELECT employees.FirstName || ' ' || employees.LastName AS employeeName, SUM(invoices.Total) AS total2010Sales
FROM employees
INNER JOIN invoices ON invoices.CustomerId=customers.CustomerId
INNER JOIN customers ON customers.SupportRepId=employees.EmployeeId
WHERE invoices.InvoiceDate >= "2010-01-01 00:00.00" AND invoices.InvoiceDate <= "2010-12-31 23:59.59"
GROUP BY employeeName;''')
print(len(cur.fetchall()),file=f)
print("employeeName\ttotal2010Sales" ,file=f)
cur.execute('''
SELECT employees.FirstName || ' ' || employees.LastName AS employeeName, SUM(invoices.Total) AS total2010Sales
FROM employees
INNER JOIN invoices ON invoices.CustomerId=customers.CustomerId
INNER JOIN customers ON customers.SupportRepId=employees.EmployeeId
WHERE invoices.InvoiceDate >= "2010-01-01 00:00.00" AND invoices.InvoiceDate <= "2010-12-31 23:59.59"
GROUP BY employeeName LIMIT 10;''')
for row in cur:
	print(row[0],"\t",row[1],file=f)
print(file=f)


print(1,file=f)
print("employeeName\ttotal2010Sales" ,file=f)
cur.execute('''
SELECT employees.FirstName || ' ' || employees.LastName AS employeeName, SUM(invoices.Total) AS total2010Sales
FROM employees
INNER JOIN invoices ON invoices.CustomerId=customers.CustomerId
INNER JOIN customers ON customers.SupportRepId=employees.EmployeeId
WHERE invoices.InvoiceDate >= "2010-01-01 00:00.00" AND invoices.InvoiceDate <= "2010-12-31 23:59.59"
GROUP BY employeeName 
ORDER BY total2010Sales DESC
LIMIT 10;''')
row = cur.fetchone()
print(row[0],'\t',row[1],file=f)


cur.execute('''SELECT billingCountry, SUM(invoices.Total) AS totalSales
FROM invoices
GROUP BY billingCountry
ORDER BY totalSales DESC;''')
print(len(cur.fetchall()),file=f)
print("billingCountry\ttotalSales" ,file=f)
cur.execute('''SELECT billingCountry, SUM(invoices.Total) AS totalSales
FROM invoices
GROUP BY billingCountry
ORDER BY totalSales DESC Limit 10;''')
for row in cur:
	print(row[0],"\t",row[1],file=f)
print(file=f)



cur.execute('''SELECT tracks.name as Song, albums.Title as Album , artists.Name as Artist, COUNT(invoice_items.trackId) as totalSold
FROM tracks
INNER JOIN invoice_items ON invoice_items.trackId = tracks.trackId
INNER JOIN invoices ON invoices.invoiceId = invoice_items.invoiceId
INNER JOIN albums ON albums.albumId = tracks.AlbumId
INNER JOIN artists ON artists.ArtistId = albums.ArtistId
WHERE invoices.InvoiceDate >= '2013-01-01 00:00.00'
AND invoices.InvoiceDate <= '2013-12-31 23:59.59'
GROUP BY tracks.trackid
ORDER BY totalSold DESC; ''')
print(len(cur.fetchall()),file=f)
print("Song\tAlbum\tArtist\ttotalSold" ,file=f)
cur.execute('''SELECT tracks.name as Song, albums.Title as Album , artists.Name as Artist, COUNT(invoice_items.trackId) as totalSold
FROM tracks
INNER JOIN invoice_items ON invoice_items.trackId = tracks.trackId
INNER JOIN invoices ON invoices.invoiceId = invoice_items.invoiceId
INNER JOIN albums ON albums.albumId = tracks.AlbumId
INNER JOIN artists ON artists.ArtistId = albums.ArtistId
WHERE invoices.InvoiceDate >= '2013-01-01 00:00.00'
AND invoices.InvoiceDate <= '2013-12-31 23:59.59'
GROUP BY tracks.trackid
ORDER BY totalSold DESC LIMIT 10; ''')
for row in cur:
	print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],file=f)