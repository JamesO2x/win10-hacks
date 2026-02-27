# Generate a new GUID and store it in a variable
$newGuid = (New-Guid).Guid.ToUpper()

# Output the GUID to the console
Write-Host "Generated GUID: $newGuid" -ForegroundColor Cyan

# Copy the GUID to the clipboard
$newGuid | Set-Clipboard

Write-Host "GUID has been copied to your clipboard." -ForegroundColor Green

# Wait for user input
Read-Host -Prompt "Press Enter to exit"
