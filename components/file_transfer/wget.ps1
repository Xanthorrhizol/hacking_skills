$webClient = New-Object System.Net.WebClient
$url = "<target url>/<file to downlaod>"
$file = "<output file>"
$webClient.DownloadFile($url, $file)
