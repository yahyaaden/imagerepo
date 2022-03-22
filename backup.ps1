#backup
docker exec imagerepo-db-1 /usr/bin/mysqldump -u root --password=root imagerepo | Set-Content backup.sql
Write-Host "The database has been stored in backup.sql"
