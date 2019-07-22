def main():
  f= open("akademyai.txt","w+")
  for i in range(10):
    f.write('This is line {:2d}\n'.format(i+1))
  f.close()

if __name__== "__main__":
  main()
