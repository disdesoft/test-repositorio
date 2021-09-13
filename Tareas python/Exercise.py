print("\n=======================================")
print("CALCULADORA LIBRERIA NUEVA NACIÓN S.A.S.")
print("=========================================")
print('Descuentos:')
print('Categoria 1 = 12%')
print('Categoria 2 = 10%')
print('Categoria 3 = 15%\n')

print('Compra de Jorge')
print('3 libros de la categoria 1 que suman $180.000')
print('2 libros de la categoria 2 que suman $85.000')
print('')

compracat1 = 180000
compracat2 = 85000

descuentocat1 = compracat1*0.12
descuentocat2 = compracat2*0.10

subtotal1 = compracat1 - descuentocat1
subtotal2 = compracat2 - descuentocat2

Total = subtotal1 + subtotal2

print('Jorge debe pagar con descuento: ', Total)


nombre = ('Martha')

print('\nCompra de ', nombre)
print('5 libros de la categoria 1 que suman $300.000')
print('4 libros de la categoria 2 que suman $80.000')
print('1 libro de la categoria 3 que cuesta $22.000\n')

compracat1 = 300000
compracat2 = 80000
compracat3 = 22000

descuentocat1 = compracat1*0.12
descuentocat2 = compracat2*0.10
descuentocat3 = compracat3*0.15

subtotal1 = compracat1 - descuentocat1
subtotal2 = compracat2 - descuentocat2
subtotal3 = compracat3 - descuentocat3


Total = subtotal1 + subtotal2 + subtotal3
print('Martha debe pagar', Total)
print('Como martha tiene $375.000\n')

if Total <= 375000:
    print('A martha le alcanza para pagar')
else:
    print('A martha no le alcanza para pagar')