from sys import stdin

for _ in xrange(int(stdin.readline())):
    num = int(stdin.readline())
    print ' '.join(['!!!' + word + '!!!' if word.isupper() else word for word in stdin.readline().rstrip('\n').split()]).replace('.', '!!!')
