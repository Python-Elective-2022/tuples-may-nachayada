def skip_tuples(tuple):
  return tuple[::2]

def main():
  print(skip_tuples(('one', 'two', 'three', 'four', 'five')))

if __name__ == '__main__':
  main()