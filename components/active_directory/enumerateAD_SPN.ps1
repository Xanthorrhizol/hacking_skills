#find LDAP provider path of domain controller
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.','DC='))"
$SearchString += $DistinguishedName
$SearchString

#search using LDAP provider
$Sercher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
$objDomain = New-Object System.DirectoryServices.DirectoryEntry
$Searcher.SearchRoot = $objDomain
$Searcher.filter = "serviceprincipalname=*http*"	# search for http
#$Searcher.filter = "serviceprincipalname=*<keyword>*"	# search for keyword
$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
	Foreach($prop in $obj.Properties)
	{
		$prop
	}
}
