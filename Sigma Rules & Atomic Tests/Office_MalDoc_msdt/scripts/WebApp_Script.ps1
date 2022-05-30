
#  Version:        1.0
#  Author:         <CyberCastle [Assem Morad]>
#  Creation Date:  <12/5/2022>
#  Purpose/Change: WebApp for MSDT vuln
#  Usage:          Refer to -h param


param(
    [Parameter()]
    [String]$SelectMode,
    [Switch]$help
)



function IIS_Installation {

  $BitsApp = 'Web-Server'
  foreach ($App in $BitsApp)
   {
        if ((Get-WindowsFeature -Name $App|select -ExpandProperty Installed) -ne 'True')
         {
            Write-host "$App not installed"
            Write-host "[+] Installing $App ....."
            $InstallApp = Install-WindowsFeature -name $App -IncludeManagementTools
            
            if ((Get-WindowsFeature -Name $App|select -ExpandProperty Installed) -eq 'True')
                 {
                    Write-Host "installed $App Feature"
                 }

             else 

                 {
                    Write-Host "[-] Failed to Install $App Feature !"
                 }
         }

        else
            {
              Write-host  "$App already installed"
            }

   }
}
  

function Web_Directory {

    $PsyDir= "$env:TEMP/test"

    if(Test-Path $PsyDir)
         {
             Write-Host "The Directory 'test' already exists at $env:TEMP"
         }

    else
         {
             Write-Host "The Directory 'test' not exists at $env:TEMP"
             Write-Host "[+] Creating 'test' Directory ..... "
             $CrtDir=New-Item $env:TEMP/test -ItemType Directory 
       
             if (Test-Path $PsyDir)
                 {
                     Write-host "Created 'test' Directory at $env:TEMP"
                 }
             else
                 {
                     Write-Host "[-] Failed to create 'test' Directory !"
                 }
        } 
}


  function WebDir_Permession {

    $Acl4test = Get-Acl "$env:TEMP\test"
    $GroupAdd = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
    
    if ((Get-Acl -Path $env:TEMP\test | where {$_.AccessToString -like "Everyone*FullControl*" }))
           {

               Write-Host "The New ACL already Applied on 'test' Directory"

           }
    else
           {

               Write-Host "The New acl not applied on $env:TEMP\test"
               Write-Host "[+] Appling the New Acl to $env:TEMP\test ......"
               $Acl4test.SetAccessRule($GroupAdd)
               $assign_Acl= Set-Acl "$env:TEMP\test" $Acl4test

               if ((Get-Acl -Path $env:TEMP\test | where {$_.AccessToString -like "Everyone*FullControl*" }))

                    {
                         Write-Host "Applied the new ACL to $env:TEMP\test"
                    }

               else

                    {
                        Write-Host "[-] Failed to Apply the new ACL to $env:TEMP\test !"
                    }
                
           }

}


function WebApp_Creation {    
  
    if (Get-WebApplication  -Name test)

        {
            
            Write-Host "The 'test' WebApp already exists"
        }

    else

        {
             Write-Host "The 'test' WebApp Not exists"
             Write-Host "[+] Creating The 'test' WebApp  ....."
             $Crt_VrtDir= New-WebApplication -Name "test" -Site "Default Web Site" -PhysicalPath "$env:TEMP\test" -ApplicationPool "DefaultAppPool"

             if (Get-WebApplication  -Name test)
                 {

                     Write-host "Created The 'test' WebApp "

                 }

             else
                 {

                     Write-Host "[-] Failed to create The 'test' WebApp !"

                 }
        }
}

  function Enable_DirectoryBrowsing {
      
        if ((Get-WebConfigurationProperty -filter /system.webServer/directoryBrowse -name enabled -PSPath 'IIS:\Sites\Default Web Site\test' | where {$_.Value -like "True"}))
        
            {
                Write-Host "Directory Browsing already enabled on 'test' Directory" 
            }

        else

            {
                Write-Host "The Directory Browsing is Disabled on 'test' Directory"
                Write-Host "[+] Enabling Directory Browsing of 'test' Directory"
                $Enb_DirBrws= Set-WebConfigurationProperty -filter /system.webServer/directoryBrowse -name enabled -value true -PSPath 'IIS:\Sites\Default Web Site\test'

                if ((Get-WebConfigurationProperty -filter /system.webServer/directoryBrowse -name enabled -PSPath 'IIS:\Sites\Default Web Site\test' | where {$_.Value -like "True"}))
                    
                       {
                            Write-Host "Enabled Directory Browsing of 'test' Directory"
                       }

                else
                   
                       {
                              Write-Host "[-] Failed to Enable Directory Browsing of 'test' Directory !"
                       }

              }
}
                                            
function Uninstall_WebApp{ 
    $WebDir= "$env:TEMP/test"
    if (Test-Path -Path $WebDir)

    {  
         Write-Host "The 'test' Directory exists at $env:TEMP"
         Write-Host "[+] Removing $BitsDir ...."
         $Remove_Dir = Remove-Item -Path $WebDir -Recurse -Force
        
         if (Test-Path -Path $BitsDir)

            {
                Write-Host "Removed the 'test' Directory"
            }

         else

            {
                Write-Host "[-] Failed to remove 'test' Directory"
            }


    }

    else 

    {
          Write-Host "The 'test' Directory already Not exists!"
    }


    
    $Feature = 'Web-Server'

    foreach ($App in $Feature)
    {
        if ((Get-WindowsFeature -Name $App|select -ExpandProperty Installed) -ne 'True')
        
             {
                   Write-host "$app Feature already not Installed "
            
             }

        else

            {
              Write-Host  "$app Feature is installed"
              Write-host  "[+] Removing $App Feature ......."
              $UninstallApp = Uninstall-WindowsFeature -Name Web-Server
             
              if ((Get-WindowsFeature -Name $App|select -ExpandProperty Installed) -ne 'True')
              
                  {
                         Write-Host "Removed $App Feature" 
                  }

               else

                  {
                        Write-Host "[-] Failed to uninstall $App Feature !"
                  }

            }

   }

}



if ($help)
    {

		write-host "`nDescription: A simple script that creates a BITS server to be used later for Data Exhilaration via Bitsadmin.`n[Note]: This Script Tested only on Windows Server 2019! `n`nHow to Use This Script!`n`nOptions:`n-SelectMode: Select One of the two Mode (Install/Uninstall) <Required> `n `nExample:`n.\Bits_Upload.ps1 -SelectMode Install`n.\Bits_Upload.ps1 -SelectMode Uninstall`n " 
	
    }


elseif ($SelectMode -eq 'Install' )
    { 

        IIS_Installation
        Web_Directory
        WebDir_Permession
        WebApp_Creation
        Enable_DirectoryBrowsing
        write-host "Done!"
    }

elseif($SelectMode -eq 'Uninstall')
    {
        Uninstall_WebApp
    }
