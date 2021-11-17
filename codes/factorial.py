# [PT-BR] 

n=(input("Digite um numero para calcular seu fatorial: "))
num=int(n)
base=1
conta=1

inicio="%s*" % (n)
print("\nFatorial de {valor}".format(valor=n))
print("\nUsando a formula: n!= n*(n-1)*(n-2)*(n-3)* ... *3*2*1 \n")
print(inicio,end="")

while base<num:
    conta=conta*(num-base)
    if base==num-1:
        aux="(%s-%s)" % (n,str(base))
    else:
        aux="(%s-%s)*" % (n,str(base))
    print(aux,end="")
    base+=1

print("=",sep="",end="\n\n")

inicio="%s *" % (n)
print(inicio,end=" ")

num=int(n)
base=1
conta=1
aux="0"

while base<num:
    conta=conta*(num-base)
    if base==num-1:
        aux="%s " % (num-base)
    else:
        aux="%s * " % (num-base)
    print(aux,end="")
    base+=1

print("=",num*conta)

# *Compilation*
#
# Enter a number to calculate your factorial: 10
#
# Factorial of 10
#
# Usando a formula: n!= n*(n-1)*(n-2)*(n-3)* ... *3*2*1 
#
# 10*(10-1)*(10-2)*(10-3)*(10-4)*(10-5)*(10-6)*(10-7)*(10-8)*(10-9)=
#
# 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
