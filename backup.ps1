#We take the command input and store it in a variable
$getarg = $args[0]

#We check if the variable meets the criteria of our conditions:

if ($getarg -eq "backup")
{
    #store database in the backup.sql in the backup folder
    docker exec imagerepo-db-1 /usr/bin/mysqldump -u root --password=root imagerepo | Set-Content ./backup/backup.sql
    Write-Host "The database has been stored in backup.sql" -ForegroundColor Green
}

elseif ($getarg -eq "restore")
{
    #restore database from backup.sql in the backup folder
    Get-Content ./backup/backup.sql | docker exec -i imagerepo-db-1 /usr/bin/mysql -u root --password=root imagerepo
    Write-Host "The database has been restored from backup.sql" -ForegroundColor Blue
}
else
{
    Write-Host "The command does not meet the conditions of the script!" -ForegroundColor Red
}