# Generate random 32-character password for mysql
$mysqlpass = -join ((65..90) + (97..122) | Get-Random -Count 32 | % {[char]$_})

Write-Host "Removing old installation (if one exists)"
docker container rm -f cp467-app
docker image rm -f cp467-app

Write-Host "Building the docker image"
docker build -t cp467-app .

Write-Host "Deploying cp467-app website"
docker run --detach --name cp467-app -e MYSQL_PASSWORD=$mysqlpass -p 127.0.0.1:80:5000/tcp cp467-app

Write-Host 'Finished. Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
