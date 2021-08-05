#START TELEKOM SPEEDTEST WITH CHROME
Start-Process "chrome.exe" "http://kabelspeed.telekom-dienste.de/"

#WAIT FOR TELEKOM SPEEDTEST
Start-Sleep -Seconds 40

#CAPTURE SCREENSHOT
#like https://www.youtube.com/watch?v=3ne7oXTcJhc
 Add-Type -AssemblyName System.Windows.Forms
 Add-Type -AssemblyName System.Drawing

 #to capture screen resolution
 $Screen=[System.Windows.Forms.SystemInformation]::VirtualScreen
 $Width=$Screen.Width
 $Height = $Screen.Height
 $Left = $Screen.Left
 $Top = $Screen.Top

 $bitmap=New-Object System.Drawing.Bitmap $Width, $Height

 $graphic=[System.Drawing.Graphics]::FromImage($bitmap)
 
 #capture screen
 $graphic.CopyFromScreen($Left,$Top,0,0,$bitmap.Size)

 #save the file as "test.jpg"
 $bitmap.Save("C:\Users\dome\Downloads\test.jpg")

#Wait a sec
Start-Sleep -Seconds 1

#rename "test.jpg" with date in name
Rename-Item -Path "C:\Users\dome\Downloads\test.jpg" -NewName ("test_{0:yyyyMMddhhmm}.jpg" -f (get-date))

#end chrome
Stop-Process -Name chrome

$repeat = (New-TimeSpan -Minutes 3)
$duration = ([timeSpan]::maxvalue)
$action = New-ScheduledTaskAction "powershell.exe" "-file C:\Users\dome\Desktop\telekom_script.ps1"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).Date -RepetitionInterval $repeat -RepetitionDuration $duration
$principal = New-ScheduledTaskPrincipal -LogonType InteractiveOrPassword -RunLevel Highest
Register-ScheduledTask CheckExternInactiveUsers –Action $action –Trigger $trigger –Principal $principal