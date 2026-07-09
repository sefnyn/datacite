def read(file):
  fh = open(file)
  fh2 = open('sufia_ids.txt', 'w')
  for line in fh:
      



def main():
    try:
        read(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "file containing DOIs")

if __name__ == "__main__":
    import sys
    sys.exit(main())
