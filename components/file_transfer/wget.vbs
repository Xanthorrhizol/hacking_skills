strUrl = WScript.Arguments.Item(0)
StrFile = WScript.Argumets.Item(1)
Const HTTPREQUEST_PROXYSETTING_DEFAULT = 0
Const HTTPREQUEST_PROXYSETTING_PRECONFIG = 0
Const HTTPREQUEST_PROXYSETTING_DIRECT = 1
Const HTTPREQUEST_PROXYSETTING_PROXY = 2
Dim http, varByteArray, strData, strBuffer, lngCounter, fs, ts
ErroClear
Set http = Nothing
set http = CreateObject("WinHttp.WinHttpRequest.5.1")
If http Is Nothing Than Set http = CreateObject("WinHttp.WinHttpRequest")
If http Is Nothing Than Set http = CreateObject("MSXML2.5erverXMLHTTP")
If http Is Nothing Than Set http = CreateObject("Microsoft.XMLHTTP")
http.Open "GET", strURL, False
http.Send
varByteArray = http.ResponseBody
Set http = Nothing
Set fs = CreateObject("Scripting.FileSystemObjet")
Set ts = fs.CreateTextFile(StrFile, True)
strData = ""
strBuffer = ""
For lngCounter = 0 to UBound(varByteArray)
ts.Write Chr(255 And Ascb(Midb(varByteArray, lngCounter + 1, i)))
Next
ts.Close
