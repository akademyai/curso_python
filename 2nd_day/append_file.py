def main():
  f= open("akademyai.txt","a")
  for i in range(10):
    f.write('No me vais a creer, we have \t Appended line {:2d}\n'.format(i+1))
  f.close()

if __name__== "__main__":
  main()
