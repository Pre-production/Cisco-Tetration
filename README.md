# Cisco Tetration GET and DELETE (sensors/scopes objects) requests
This is an example of sending GET request to obtain a list of sensors objects present to the Cisco Tetration cluster (pre-checks-get.py)
In order to use it, code needs to be adapted according to the parameters you have: 
API_ENDPOINT="https://10.10.10.10"
should be specified the IP address or domain name of your Tetration cluster. 
It's always better to specify the IP rather than the Domain name, because if you are working from the DMZ Jump host most probably you will not have a DNS resolver on it.
!!! This should be done for the files 'post-checks-get.py' and 'to_delete_uuids.py' as well.

Next, you have to generate API Keys on the Tetration GUI, navigate to the Gears sign on the top right corner, and choose 'API Keys' in the drop-down. Then mark all the limitations and generate your keys in JSON format (api_credentials.json). Download the file with the keys and move it to the same directory where 'pre-checks-get.py' is located.
Those are all modifications you need to implement to make this script work for your cluster.

One more important thing is that you could possibly do not have connectivity to the internet if you are accessing the Tetration cluster from the DMZ Jump host (Windows or Linux).
In this case, connectivity to the internet is needed to import package 'tetpyclient'.
In case if you have a Windows Jump host, to bypass this issue and to avoid manual transferring of the package from your local machine to the Jump host you need to 'freeze' this script. In order to do this, you need to download 'pyinstaller' tool: C:\Users\yourusername>pip install pyinstaller
Identify the directory where pyinstaller.exe was installed to and copy it.
Then navigate to the directory where your script is located and type the command in CLI:
C:\Users\yourusername\Documents\some_folder_with_script>*paste directory where pyinstaller.exe is here*\pyinstaller.exe pre-checks-get.py --onefile
--onefile attribute will make your script a single file without any file-helpers.

After that, you will see folders _pycache_, build, dist being created. Navigate to 'dist' folder and find a 'freezed' version of the file 'pre-checks-get.py' > pre-checks-get.exe
Now you can copy pre-checks-get.exe to your Jump host and execute it from the GUI simply double-clicking on it.
!!! This should be done for the files 'post-checks-get.py' and 'to_delete_uuids.py' as well if you need them to be executed from DMZ Jump host.

* In case if you have a Linux Jump host you will have to do the pretty same procedure, but at the end, you will have .bin file generated instead of .exe

The result of the script 'pre-checks-get.py' will be generated file 'active_sensors_list.txt' where you will have the format: UUID_of_the_sensor hostname

Now we have to work with the list of devices that needs to be removed (as I was given with such) in .txt format (assuming this list calls 'servers_to_be_removed.txt' but you can change it in the script):
hostname1
hostname2
Hostname3
.
.
.
In order to avoid mistakes, we have to filter the list from duplicates first with 'unique_name_filter.py' which will generate 'unique_list.txt'

Now we need to filter the UUIDs of present sensors according to the hostnames which need to be removed by the script 'to_filter_lists.py'
The result of this script will be the file 'uuids_list.txt' generated.

Finally, you want to remove sensors by their uuids, by executing file 'to_delete_uuids'
And probably after execution, you would like to check which sensors have been removed.
One cool feature here is that sensors will remain active and visible for simple GET requests for about 24 hours, BUT the 'deleted_at' attribute with UNIX time format will be now added to them.
This design is made for cases if the sensor would be removed mistakenly, so it will be easy to resurrect it.

To check the removed sensors, execute 'post-checks-get' and 'deleted_servers_list.txt' will be generated with the list of removed sensors with the UNIX time-format frame.

!!! These scripts are adapted for working with the 'sensors' objects only, in order to use them for 'scopes' objects you will need to change resp.json()['results'] to resp.json().get('results') and change 'uuid' - parameter of the output to 'id'.
In the 'to_delete_uuids.py' - restclient.delete('/sensors/'+string) should be changed to restclient.delete('/scopes/'+string)
