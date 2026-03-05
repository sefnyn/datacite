"""
This module reads a list of DOIs and updates the landing page for each DOI on the list.

This module relies on function test_update in another module:
test_update_landing_page.test_update([SHORT_DOI], [LANDING_PAGE])
"""

import test_update_landing_page

def update_landing_pages(dois, new_lp):
    fh = open(dois)
    for doi in fh:
        doi = doi.rstrip()
        print(doi)
        test_update_landing_page.test_update(doi, new_lp)


def main():
    try:
        update_landing_pages(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage:\n", sys.argv[0], "[FILE_CONTAINING_SHORT_DOIS] [NEW_LANDING_PAGE_WITHOUT_RECORD_ID]")

if __name__ == "__main__":
    import sys
    sys.exit(main())
