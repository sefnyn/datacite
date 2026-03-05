# Manage DataCite DOIs

## get_all_dois.py [PREFIX]
This script attempts to retrieve all, findable DOIs with prefix *PREFIX* and export the results in CSV format.  This script does not currently work because the DataCite API has a bug; namely, the API returns 319 DOIs and then suddenly stops.

Output files are:  dois.csv | dois.json

## get_doi_from_json.py [PREFIX]
This script calls the **production** DataCite API and retrieves all, findable DOIs with prefix *PREFIX*.  Then the JSON data is read, parsed and analysed.

For example:
> source ./bin/activate   # activate virtual environment  
> python3 get_doi_from_json.py 10.15128  
> Found 618 DOIs with prefix 10.15128  
> Created new file with 608 DOIs that resolve to collections server: dois_resolve2collections.txt  
> Created new file with 10 DOIs that resolve elsewhere: dois_resolve_elsewhere.txt  

## test_update_landing_page.py [SHORT_DOI] [LANDING_PAGE]
This script updates the landing page for exactly one DOI by calling the DataCite **Test** API

For example:
> python3 test_update_landing_page.py 10.4124/R90R967372K https://collections-test.durham.ac.uk/files/r90r967372k  
> Enter password for DataCite user (N.B.: you will *not* see any input as you type):  
> Success.  Updated landing page for DOI 10.4124/R90R967372K  


