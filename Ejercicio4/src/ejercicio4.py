#Diseniar una calculadora

a=float(input('Bienvenido ingrese primer numero:'))
b=float(input('Bienvenido ingrese segundo numero:'))
print 'A continuacion le mostraremos un menu con las opciones disponibles:'
print ('1).- Sumar numeros')
print ('2).- Restar primer numero con el segundo numero')
print ('3).- Multiplicar numeros')
print ('4).- Dividir primer numero entre el segundo numero')
print ('5).- Primer numero al exponente del segundo numero')
print ('6).- Primer y segundo numero al cuadrado')
print ('7).- Raiz cuadrada del primer y segundo numero')
c=input('Ingrese opcion a realizar:')
if c==1:
    d=a+b
    d=round(d,2)
    print 'La suma de los valores es', d
else:
    if c==2:
        d=a-b
        d=round(d,2)
        print 'La resta del primer valor con el segundo es', d
    else:
        if c==3:
            d=a*b
            d=round(d,2)
            print 'El producto de los valores es', d
        else:
            if c==4:
                d=a/b
                d=round(d,2)
                print 'El cociente de los numeros es', d
            else:
                if c==5:
                    d=a**b
                    d=round(d,2)
                    print 'El primer numero elevado al segundo es', d
                else:
                    if c==6:
                        d=a**2
                        d=round(d,2)
                        e=b**2
                        e=round(d,2)
                        print 'El cuadrado del primer valor es', d
                        print 'El cuadrado del segundo valor es',e
                    else:
                        import math
                        if c==7:
                            d=math.sqrt(a)
                            d=round(d,2)
                            e=math.sqrt(b)
                            e=round(e,2)
                            print 'La raiz cuadrada del primer valor es', d
                            print 'La raiz cuadrada del segundo valor es', e
                        else:
                            print 'Ingrese una de las opciones mencionadas en el menu anteriormente'
