# SQL

## export to csv file
```
mysql -h 127.0.0.1 -uroot -P 3306 -p database_name -e "SELECT * FROM users" > a.csv
```