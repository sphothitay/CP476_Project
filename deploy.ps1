# Generate random 32-character password for mysql
$mysqlpass = -join ((65..90) + (97..122) | Get-Random -Count 32 | % {[char]$_})

Write-Host "Removing old installation (if one exists)"
docker container rm -f cp476-app
docker image rm -f cp476-app

Write-Host "Building the docker image"
docker build -t cp476-app .

Write-Host "Deploying cp476-app website"
docker run --detach --name cp476-app -e MYSQL_PASSWORD=$mysqlpass -p 127.0.0.1:80:5000/tcp cp476-app

Write-Host 'Finished. Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
