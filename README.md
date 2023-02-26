# jhurCubesProject

1. Junseok Hur

2. Any install and run directions I need beyond the basics
- MySQL Workbench
  1. Download and install MySQL Workbench
  2. Open MySQL Workbench and click on the "Start a new connection" icon
  3. In the "Set up a new connection" window, fill in the following details:
     - Connection Name: choose a name for your connection
     - Hostname: db-mysql-nyc1-12016-do-user-13526185-0.b.db.ondigitalocean.com
     - Port: 25060
     - Username: doadmin
     - Password: AVNS_Kh4wgDoWwLrcGGjTc0o
  4. Click on "Test Connection" to verify the details you provided are correct.
  5. If the connection is successful, click on "OK" to close the window and add the connection to the workbench.
  6. Click on the database you want to view to expand it and see all the tables within it.
  7. Double-click on a table to view its contents.

3. a brief description of what your project does
- Received the data file from api site
- Save the entire data into text file
- Data insert into database using sqlite3
- Change the column name
- Create the database cluster using Digitalocean
- Connect to database server

4. a very brief discussion of your database layout and the table(s) you used
- Create database using MySQL
- Set up one table
- Changed unuseful columns name
- mysql.connector to get connection

5. a brief description of what is missing from the project (if anything)
- For the reminder, I wrote the correct data method already at the sprint2. So I just add two more text field to test from sprint2 code.
- Check box automated test
