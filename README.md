# Manage DataCite DOIs

## get_all_dois.py [PREFIX]
This script attempts to retrieve all, findable DOIs with prefix *PREFIX* and export the results in CSV format.  This script does not currently work because the DataCite API has a bug; namely, the API returns 319 DOIs and then suddenly stops.

Output files are:  dois.csv | dois.json

## get_doi_from_json.py [PREFIX]
This script retrieves all, findable DOIs with prefix *PREFIX*.  Then the JSON data is read, parsed and analysed.

For example:
> ./bin/python3 get_doi_from_json.py 10.15128  
> Getting JSON metadata from DataCite...  
> Reading JSON metadata...  
> Created new file: dois.txt  
> Found 617 DOIs with prefix 10.15128  
