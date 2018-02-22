import boto3
import time
from datetime import datetime
import datetime as dt
from datetime import date
from dateutil.relativedelta import relativedelta

six_months = date.today() + relativedelta(months=-6)
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
paginator = client.get_paginator("list_tables")
all_tables = []
remove_backup = []

#Function to gather all of the dynamodb tables
def gettables():
        get_all_tables = paginator.paginate()
        for page in get_all_tables:
                for table in page["TableNames"]:
                        all_tables.append(table)

#Function to find the backups that are older than 6 months
def getbackups():
        for table in all_tables:
                backups = client.list_backups(
                        Limit=25,
                        TableName=table,
                        TimeRangeUpperBound=datetime(year=six_months.year, month=six_months.month, day=six_months.day)
                )
                for backup_summary in backups["BackupSummaries"]:
                        backup_arn = backup_summary["BackupArn"]
                        remove_backup.append(backup_arn)

#Function to remove the backups we found in the getbackups function.
def removebackups():
        for arn in remove_backup:
                response = client.delete_backup(
                        BackupArn= arn
                )

gettables()
getbackups()
removebackups()
