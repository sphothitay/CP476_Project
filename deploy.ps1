Write-Host "Removing old installation (if one exists)"
docker container rm -f cp476-app
docker image rm -f cp476-app

Write-Host "Building the docker image"
docker build -t cp476-app .

Write-Host "Deploying cp476-app website"
docker run --detach --name cp476-app -p 127.0.0.1:80:5000/tcp cp476-app

Write-Host 'Finished. Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
