# auto-delete-dynamodb-backups
Auto deleted DynamoDB Backups based on a date (default is older than 6 months)


* The file will automatically pull all of your tables in your AWS account and then dump those tables to search for any backups each table may have. After that it will perform a search of those backups to see if they are older than 6 months, (by default, if you want to change this you need to edit the six_months variable calculation at the top of the file) and then the remove backups function will remove any backups that are found to be older than 6 months.
