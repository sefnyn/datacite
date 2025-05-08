#!/usr/bin/env python3
"""

This module calls the British Library's DataCite API (called MDS)

"""

import sys
import codecs
import getpass
import httplib2 # 3rd party module

ENDPOINT = "https://mds.datacite.org/" # v2
#ENDPOINT = "https://test.datacite.org/mds/" # v2
DOI_RESOURCE = "doi"
METADATA_RESOURCE = "metadata"
MDS_ID = "XFIR"


def mint_doi(doi, filename, landing_page):
    fh = None
    try:
        fh = codecs.open(filename, "r", encoding="utf-8")
        xml_body = fh.read()
        if confirmation(doi, filename, landing_page):
 
            # Get password
            pwd = getpass.getpass(prompt="Enter MDS password (N.B.: you will *not* see any input as you type): ", stream=None)
            if not pwd:
                raise CancelledError()

            # create Http object
            h = httplib2.Http()
            h.add_credentials(MDS_ID, pwd)

            body = "doi={0}\nurl={1}".format(doi, landing_page)

            header = {"Content-Type" : "application/xml;charset=UTF-8"}
            status2 = send_request(h, METADATA_RESOURCE, xml_body, header, "Making request to store metadata in MDS")

            input("Press ENTER to continue")

            header = {"Content-Type" : "text/plain;charset=UTF-8"}
            status1 = send_request(h, DOI_RESOURCE, body, header, "Requesting new DOI from DataCite MDS")

            if (status1 == 201 and status2 == 201):
                status = 201
            return status
    except IOError as err:
        print("Error opening file: ", err)
    except EnvironmentError as err:
        print("ERROR", err)
    finally:
        if fh is not None:
            fh.close()


def confirmation(doi, filename, landing_page):
       # Get confirmation
        if (GetString.get("""
Please note you are about to do something which CANNOT BE UNDONE.  Even the BL cannot remove a DOI from the DataCite system.  Please confirm the following details are correct before trying to mint a DOI:
    DOI: {doi}
    DataCite metadata record: {filename}
    Landing page: {landing_page}

N.B.: The metadata and the landing page URL can indeed be modified at a later date, if necessary.

Enter "yes" to confirm""".format(**locals())).lower()
            not in {"yes"}):
                raise CancelledError()
        return True


def send_request(http, resource, body, hdr, msg):
    # OK, send request
    uri = ENDPOINT + resource
    print("\n{0}: {1}".format(msg, uri))
    response, content = http.request(uri,
                                     "POST",
                                     body = body.encode("utf-8"),
                                     headers = hdr)
    if (response.status == 201):
        print("Success!\n")
        return response.status
    else:
        print (str(response.status) + " : " + response.reason)
        raise CancelledError()


if __name__ == "__main__":
    mint("10.5072/imf/ifs/2011-06", "/home/ns/test.xml")
#[EOF]
