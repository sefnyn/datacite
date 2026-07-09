def read(file):
  fh = open(file)
  fh2 = open('sufia_ids.txt', 'w')
  for line in fh:
      doi = line.split("/")
      fh2.write(doi[1])

def main():
    try:
        read(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "file_containing_DOIs")

if __name__ == "__main__":
    import sys
    sys.exit(main())
