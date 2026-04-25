# Get and display the current computer name
$computerName = $env:COMPUTERNAME

Write-Host "Computer Name: $computerName" -ForegroundColor Cyan

# Copy the computer name to the clipboard
$computerName | Set-Clipboard

Write-Host "Computer name has been copied to your clipboard." -ForegroundColor Green

# Wait for user input
Read-Host -Prompt "Press Enter to exit"