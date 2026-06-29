"""
This module reads a list of DOIs and updates the landing page for each DOI on the list.

This module relies on function test_update in another module:
test_update_landing_page.test_update([DATACITE_USER] [SHORT_DOI], [LANDING_PAGE])
"""

import test_update_landing_page
import getpass

def update_landing_pages(user, dois, lp):
    fh1 = open('success.log', 'w')
    fh2 = open('fail.log', 'w')
    # Get password
    pwd = getpass.getpass(prompt="Enter password for user " + user + " (N.B.: you will *not* see any input as you type): ", stream=None)
    fh = open(dois)
    for doi in fh:
        doi = doi.rstrip()
        parts = doi.split("/")
        prefix = parts[0]
        suffix = parts[1]
        if lp.endswith("/"):
            new_lp = lp + suffix
        else:
            new_lp = lp + "/" + suffix
        result = test_update_landing_page.test_update(user, pwd, doi, new_lp)
        if result is True:
            fh1.write(doi + "\n")
        else:
            fh2.write(doi + "\n")


def main():
    try:
        update_landing_pages(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print("Usage:\n", sys.argv[0], "[DATACITE_USER] [FILE_CONTAINING_SHORT_DOIS] [LANDING_PAGE_PREFIX]")

if __name__ == "__main__":
    import sys
    sys.exit(main())
