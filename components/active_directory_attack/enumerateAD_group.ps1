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
$Searcher.filter = "(objectClass=Group)"	# search for all user
#$Searcher.filter = "(name=<target group>)"	# search for specific group
$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
	$obj.Properties.name	# print groups
	#$obj.Properties.member	# print members(CN)
}
