#restore
Get-Content backup.sql | docker exec -i imagerepo-db-1 /usr/bin/mysql -u root --password=root imagerepo
Write-Host "The database has been restored from backup.sql"