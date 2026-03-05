"""
This module reads a list of DOIs and updates the landing page for each DOI on the list.

This module relies on function test_update in another module:
test_update_landing_page.test_update([SHORT_DOI], [LANDING_PAGE])
"""

import test_update_landing_page




def main():
    try:
        update_landing_pages(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage:\n", sys.argv[0], "[FILE_CONTAINING_SHORT_DOIS] [LANDING_PAGE_PREFIX]")

if __name__ == "__main__":
    import sys
    sys.exit(main())
