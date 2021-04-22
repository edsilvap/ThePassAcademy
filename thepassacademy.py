import myfunc

r = myfunc.rolldice()
a = myfunc.rolldice()
n = myfunc.rolldice()
d = myfunc.rolldice()
o = myfunc.rolldice()
m = myfunc.rolldice()

wordlist = myfunc.list()

randomPass = myfunc.passgen(r, a, n, d, o, m, **wordlist)
randomPassId = r + a + n + d + o + m

myfunc.line()
myfunc.bv()
print(f'\n   \033[1;32mP A S S\n   W O R D [ {randomPass} ]\033[1;m\n   ------- \n   \033[1;34mP A S S\n     I D   [ {randomPassId} ]\033[1;m\n')
myfunc.line()
