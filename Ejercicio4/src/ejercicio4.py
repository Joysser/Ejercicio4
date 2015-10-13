
#Crear una calculadora

a=float(input('Ingrese primera variable'))
b=float(input('Ingrese segunda variable'))
print 'Seleccione una de las opciones que desee realizar'
print '1.-Sumar las variables'
print '2.-Restar las variables'
print '3.-Multiplicar las variables'
print '4.-Dividir las variables'
print '5.-Potencia de la primera varible elevada a la segunda variable'
c=input('Ingrese opcion a realizar')
if c==1:
    d=a+b
    print d
else:
    if c==2:
        d=a-b
        print d
    else:
        if c==3:
            d=a*b
            print d
        else:
            if c==4:
                d=a/b
                print d
            else:
                if c==5:
                    d=a**b
                    print d
                else:
                    print 'Ingrese una de las opciones validas mencionadas anteriormente'
