from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches
#login
#Lista con los admins y sus contraseñas
admins =[["admin1" , "root1"], ["admin2", "root2"], ["admin3", "root3"]]

#Lista con las credenciales de usuario normal
usuarios_normales = [["ventas1", "123"], ["ventas2", "456"], ["ventas3", "789"]]
usr = input("Ingrese usuario: ")
passw = input ("Ingrese contraseña: ")

#Se usa es_admin como bandera en la comparación
es_admin = 0
es_user = 0
for admin in admins:
  if admin[0] == usr and admin[1] == passw:
    es_admin = 1
    break
  else:
    continue

#Si identificamos que es admin, le mostramos el menú de administrador
if es_admin == 1:
  flag = 0
  print("\nIngreso como administrador\n")
  print("1. Visualizar productos más vendidos y productos rezagados")
  print("2. Visualizar productos por reseña de servicio")
  print("3. Visualizar total de ingresos, ventas promedio mensuales, total anual y ventas promedio en el año")
  opcion=int(input("\nSeleccione una opción: "))
  seleccion = 0 
  while flag!=1:
    if opcion == 1:
      #Se usan otras dos banderas para tener el codigo en una sección diferente y no se amontone todo aqui
      seleccion = 1
      flag = 1

    elif opcion == 2:
      seleccion = 2
      flag=1
    elif opcion == 3:
      seleccion = 3
      flag=1
    else: 
      print("Opcion incorrecta")
      opcion = int(input("Ingrese una opción válida: "))
else:
  #Si no es admin, averiguamos si es un usuario normal
  for user in usuarios_normales:
    if user[0] == usr and user[1] == passw:
      es_user=1
      break
    else:
      continue
  if es_user==1:
    print("Ingreso como usuario normal")
    print("Ingrese como admin para visualizar información")
  else:
    #Si no es ni admin ni usuario normal, le decimos que ingrese como uno de ellos dos
    print("Credenciales no registradas")
    print("Ingrese un usuario normal o admin registrados")
#Mientras que admin sea ==1 se evaluará cualquier de las tres opciones que ingrese el usuario,al final de los 3 ifs y sus posibles acciones, se incrementa en 1 es_admin para romper el ciclo
while es_admin==1:
  #Aqui evaluaremos lo que seleccione el admin en su menú
  if seleccion == 1:
    # 50 PRODUCTOS MÁS VENDIDOS
    #Comparo cada id de producto en lifestore products con los ids de lifestore sales para contar cuantas veces se repite cada uno
    contador = 0
    total_ventas = []
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0] == venta[1]:
          contador += 1
      #Agrego en una lista aparte el id, la descripción del producto y la cantidad de veces que se repite ese id
      formato = [producto[0], producto[1], contador, producto[3]]
      total_ventas.append(formato)
      contador = 0
    #Ordenamiento con bubble sorte
    #En adelante se reciclará este código cada vez que se necesite
    long = len(total_ventas)
    for i in range(long-1):
      for j in range(0,long-i-1):
        if total_ventas[j][2] < total_ventas[j+1][2]:
          total_ventas[j], total_ventas[j+1] = total_ventas[j+1], total_ventas[j]
    print("\nSe mostrarán los 50 productos con mayores ventas\n")
    #Imprimo los 50 productos con mayores ventas
    for idx in range(0,50):
      print("El producto: ", total_ventas[idx][1], "Se vendió: ", total_ventas[idx][2])

    #50 PRODUCTOS CON MAYORES BÚSQUEDAS
    #Comparo el id de producto en lifestore products con cada id en la lista de lifestore searches, para contar cuantas veces se repite cada uno
    contador = 0
    total_busq = []
    for producto in lifestore_products:
      for busqueda in lifestore_searches:
        if producto[0] == busqueda[1]:
          contador += 1
      formato = [producto[0], producto[1], contador]
      total_busq.append(formato)
      contador = 0
    #Ordenamiento
    long = len(total_busq)
    for i in range(long-1):
      for j in range(0,long-i-1):
        if total_busq[j][2] < total_busq[j+1][2]:
          total_busq[j], total_busq[j+1] = total_busq[j+1], total_busq[j]
    print("\nSe mostrarán los 50 productos con mayores busquedas\n")
    for idx in range(0,50):
      print("El producto: ", total_busq[idx][1], "Se buscó: ", total_busq[idx][2])

    #MAYORES VENTAS  POR CATEGORIA
    #Separo los productos por categoría de la lista total_ventas que ya se encuentran ordenadas
    procesadores = []
    tarjetas_video = []
    tarjetas_madre = []
    dd = []
    usb = []
    pantallas = []
    bocinas = []
    audifonos  = []
    #Separo cada categoría en una lista diferente cada categoría
    for cat in total_ventas:
      if cat[3] == "procesadores":
        procesadores.append(cat)
      elif cat[3] == "tarjetas de video":
        tarjetas_video.append(cat)
      elif cat[3] == "tarjetas madre":
        tarjetas_madre.append(cat)
      elif cat[3] == "discos duros":
        dd.append(cat)
      elif cat[3] == "memorias usb":
        usb.append(cat)
      elif cat[3] == "pantallas":
        pantallas.append(cat)
      elif cat[3] == "bocinas":
        bocinas.append(cat)
      elif cat[3] == "audifonos":
        audifonos.append(cat)
    print("\nSe mostrarán los  productos MAS vendidos por Categoria")
    #Imprimo los mas vendidos de cada categoría
    print("Procesadores\n")
    for idx in range(int(len(procesadores)/2)):
      print("El producto: ", procesadores[idx][1], "Se vendió: ", procesadores[idx][2])

    print("\nTarjetas de video\n")
    for idx in range(0,int(len(tarjetas_video)/2)):
      print("El producto: ", tarjetas_video[idx][1], "Se vendió: ", tarjetas_video[idx][2])
    
    print("\nTarjetas madre\n")
    for idx in range(0,int(len(tarjetas_madre)/2)):
      print("El producto: ", tarjetas_madre[idx][1], "Se vendió: ", tarjetas_madre[idx][2])

    print("\nDiscos duros\n")
    for idx in range(0,int(len(dd)/2)):
      print("El producto: ", dd[idx][1], "Se vendió: ", dd[idx][2])
    
    print("\nMemorias usb\n")
    for idx in range(0,int(len(usb)/2)):
      print("El producto: ", usb[idx][1], "Se vendió: ", usb[idx][2])

    print("\nPantallas\n")
    for idx in range(0,int(len(pantallas)/2)):
      print("El producto: ", pantallas[idx][1], "Se vendió: ", pantallas[idx][2])
    
    print("\nBocinas\n")
    for idx in range(0,int(len(bocinas)/2)):
      print("El producto: ", bocinas[idx][1], "Se vendió: ", bocinas[idx][2])

    print("\nAudifonos\n")
    for idx in range(0,int(len(audifonos)/2)):
      print("El producto: ", audifonos[idx][1], "Se vendió: ", audifonos[idx][2])

    #MENORES VENTAS GENERALES
    #Reciclo lo que ya habia obtenido de contar la cantidad de ventas por producto
    #Para ordenar esta vez de menor a mayor con Bubble sort
    long = len(total_ventas)
    for i in range(long-1):
      for j in range(0,long-i-1):
        if total_ventas[j][2] > total_ventas[j+1][2]:
          total_ventas[j], total_ventas[j+1] = total_ventas[j+1], total_ventas[j]
    print("\nSe mostrarán los 50 productos con MENORES ventas\n")
    for idx in range(0,50):
      print("El producto: ", total_ventas[idx][1], "Se vendió: ", total_ventas[idx][2])

    #MENORES VENTAS POR CATEGORIA
    #Separo de nuevo de la lista ya ordenada de menor a mayor de ventas por categoría
    procesadores = []
    tarjetas_video = []
    tarjetas_madre = []
    dd = []
    usb = []
    pantallas = []
    bocinas = []
    audifonos  = []
    for cat in total_ventas:
      if cat[3] == "procesadores":
        procesadores.append(cat)
      elif cat[3] == "tarjetas de video":
        tarjetas_video.append(cat)
      elif cat[3] == "tarjetas madre":
        tarjetas_madre.append(cat)
      elif cat[3] == "discos duros":
        dd.append(cat)
      elif cat[3] == "memorias usb":
        usb.append(cat)
      elif cat[3] == "pantallas":
        pantallas.append(cat)
      elif cat[3] == "bocinas":
        bocinas.append(cat)
      elif cat[3] == "audifonos":
        audifonos.append(cat)

    print("\nSe mostrarán los  productos MENOS vendidos por Categoria")
    print("Procesadores\n")
    for idx in range(int(len(procesadores)/2)):
      print("El producto: ", procesadores[idx][1], "Se vendió: ", procesadores[idx][2])

    print("\nTarjetas de video\n")
    for idx in range(0,int(len(tarjetas_video)/2)):
      print("El producto: ", tarjetas_video[idx][1], "Se vendió: ", tarjetas_video[idx][2])
    
    print("\nTarjetas madre\n")
    for idx in range(0,int(len(tarjetas_madre)/2)):
      print("El producto: ", tarjetas_madre[idx][1], "Se vendió: ", tarjetas_madre[idx][2])

    print("\nDiscos duros\n")
    for idx in range(0,int(len(dd)/2)):
      print("El producto: ", dd[idx][1], "Se vendió: ", dd[idx][2])
    
    print("\nMemorias usb\n")
    for idx in range(0,int(len(usb)/2)):
      print("El producto: ", usb[idx][1], "Se vendió: ", usb[idx][2])

    print("\nPantallas\n")
    for idx in range(0,int(len(pantallas)/2)):
      print("El producto: ", pantallas[idx][1], "Se vendió: ", pantallas[idx][2])
    
    print("\nBocinas\n")
    for idx in range(0,int(len(bocinas)/2)):
      print("El producto: ", bocinas[idx][1], "Se vendió: ", bocinas[idx][2])

    print("\nAudifonos\n")
    for idx in range(0,int(len(audifonos)/2)):
      print("El producto: ", audifonos[idx][1], "Se vendió: ", audifonos[idx][2])

    #MENORES BUSQUEDAS GENERALES
    #Reciclo lo que ya habia obtenido de contar la cantidad de busquedas por producto
    #Para ordenar esta vez de menor a mayor con Bubble sort
    long = len(total_busq)
    for i in range(long-1):
      for j in range(0,long-i-1):
        if total_busq[j][2] > total_busq[j+1][2]:
          total_busq[j], total_busq[j+1] = total_busq[j+1], total_busq[j]
    print("\nSe mostrarán los 50 productos con MENORES busquedas\n")
    for idx in range(0,50):
      print("El producto: ", total_busq[idx][1], "Se buscó: ", total_busq[idx][2])
      
  if seleccion == 2:
    #MEJORES RESEÑAS
    #Buscaré en lifestore sales, los productos con mejores reseñas, los que encuentre, guardo su id en la lista "resena"
    resena = []
    productos= []
    prod=0
    #Busco en lifestore sales, los productos con reseña 5, los que encuentre, guardo su id en la lista "resena"
    for x in lifestore_sales:
      if x[2] == 5:
        resena.append(x[1])
    #Elimino los ids repetidos en la lista resena, quedandome con ids unicos en la lista productos
    for i in resena:
      if i not in productos:
        productos.append(i)
    #Con la variable prod, controlo cuantos se han impreso, para solo imprimir los 20 primeros
    print("Se mostrarán los 20 productos con Mayor valoración\n")
    for z in productos:
      print("El producto: ", lifestore_products[z][1], "Tuvo una valoración de:", 5)
      prod+=1
      if prod == 20:
        break
    #Utilizando la lista "productos" que ya tiene todos los ids con valoración 5 no repetidos, separaré los ids por categoria accediendo a las categoría en la lista de lifestore products
    procesadores=[]
    video=[]
    madre=[]
    dd=[]
    usb=[]
    pantalla=[]
    bocinas=[]
    audifonos=[]
    for z in productos:
      if lifestore_products[z][3] == "procesadores":
        procesadores.append(lifestore_products[z])
      elif lifestore_products[z][3] == "tarjetas de video":
        video.append(lifestore_products[z])
      elif lifestore_products[z][3] == "tarjetas madre":
        madre.append(lifestore_products[z])
      elif lifestore_products[z][3] == "discos duros":
        dd.append(lifestore_products[z])
      elif lifestore_products[z][3] == "memorias usb":
        usb.append(lifestore_products[z])
      elif lifestore_products[z][3] == "pantallas":
        pantalla.append(lifestore_products[z])
      elif lifestore_products[z][3] == "bocinas":
        bocinas.append(lifestore_products[z])
      elif lifestore_products[z][3] == "audifonos":
        audifonos.append(lifestore_products[z])
    print("\nSe mostrarán los productos con MAYOR valoración por categoría\n")
    #Imprimo los productos por categoría con valoración de 5
    print("Procesadores\n")
    for idx in range(len(procesadores)):
      print("El producto: ", procesadores[idx][1], "Tuvo valoración: ", 5)

    print("\nTarjetas de video\n")
    for idx in range(0,len(video)):
      print("El producto: ", video[idx][1], "Tuvo valoración: ", 5)
    
    print("\nTarjetas madre\n")
    for idx in range(0,len(madre)):
      print("El producto: ", madre[idx][1], "Tuvo valoración: ", 5)

    print("\nDiscos duros\n")
    for idx in range(0,len(dd)):
      print("El producto: ", dd[idx][1], "Tuvo valoración: ", 5)
    
    print("\nMemorias usb\n")
    for idx in range(0,len(usb)):
      print("El producto: ", usb[idx][1], "Tuvo valoración: ", 5)

    print("\nPantallas\n")
    for idx in range(0,len(pantalla)):
      print("El producto: ", pantalla[idx][1], "Tuvo valoración: ", 5)
    
    print("\nBocinas\n")
    for idx in range(0,len(bocinas)):
      print("El producto: ", bocinas[idx][1], "Tuvo valoración: ", 5)

    print("\nAudifonos\n")
    for idx in range(0,len(audifonos)):
      print("El producto: ", audifonos[idx][1], "Tuvo valoración: ", 5)

    #Productos generales con las peores reseñas
    #Busco los productos con valoración de 1 y guardo lps ids en la lista resena
    resena = []
    productos= []
    for x in lifestore_sales:
      if x[2] == 1 :
        resena.append(x[1])
    #Elimino los ids repetidos
    for i in resena:
      if i not in productos:
        productos.append(i)
    print("\nSe mostrarán los  productos con PEOR valoración\n")
    for z in productos:
      print("El producto: ", lifestore_products[z][1], "Tuvo una valoración de:", 1)
    print("\nSe encontraron: ", len(productos), "Con valoración: ", 1)
    print("Se encontraron: 0 productos con valoración 2")
    

  if seleccion == 3:
    en=[]
    feb=[]
    mar=[]
    ab=[]
    may=[]
    jun=[]
    jul=[]
    ag=[]
    sep=[]
    octu=[]
    nov=[]
    dec=[]
    #Itero la lista lifestore sales para acceder al mes de cada venta
    #Con el índice 3:5 me quedo solamente con los dos caracteres del mes. Pregunto si esa venta pertenece a alguno de los 12 meses y si no tuvo devolución, los que cumplan, guardo los ids en una lista aparte
    #Una lista por cada mes
    for x in lifestore_sales:
      if x[3][3:5] == "01" and x[4]==0:
        en.append(x[1])
      elif x[3][3:5] == "02" and x[4]==0:
        feb.append(x[1])
      elif x[3][3:5] == "03" and x[4]==0:
        mar.append(x[1])
      elif x[3][3:5] == "04" and x[4]==0:
        ab.append(x[1])
      elif x[3][3:5] == "05" and x[4]==0:
        may.append(x[1])
      elif x[3][3:5] == "06" and x[4]==0:
        jun.append(x[1])
      elif x[3][3:5] == "07" and x[4]==0:
        jul.append(x[1])
      elif x[3][3:5] == "08" and x[4]==0:
        ag.append(x[1])
      elif x[3][3:5] == "09" and x[4]==0:
        sep.append(x[1])
      elif x[3][3:5] == "10" and x[4]==0:
        octu.append(x[1])
      elif x[3][3:5] == "11" and x[4]==0:
        nov.append(x[1])
      elif x[3][3:5] == "12" and x[4]==0:
        dec.append(x[1])
    #En la lista "ingreso" se meterá el total($) de ventas por cada mes
    ingreso=[]
    #En esta variable se irá haciendo la suma por cada producto vendido
    suma=0
    #Para cada mes, verifico si tan siquiera tiene algo la lista, es decir, si hubo ventas ese mes. Si no hubo, en la lista de ingreso, para ese mes, lo pongo en 0
    if not en:
      ingreso.append(0)
    else:
      #Teniendo los ids de los productos vendidos, accedo a la lista de products por id, para pedir el costo de cada producto e irlo sumando
      for x in en:
        #En flag almaceno el costo del producto en curso
        flag=0
        #Accedo al costo unitario de ese producto
        flag=lifestore_products[x][2]
        #Lo sumo al valor actual de la suma que se lleva en ese mes
        suma=suma+flag
      #Guardo el total de ese mes en la lista de totales por mes
      ingreso.append(suma)
      #Reinicio la variable suma para que esté limpia para el siguiente mes
      suma=0

    #Lo mismo para cada mes, solo lo voy guarando en la  lista ingreso, por posición
    if not feb:
      ingreso.append(0)
    else:
      for x in feb:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not mar:
      ingreso.append(0)
    else:
      for x in mar:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0
    
    if not ab:
      ingreso.append(0)
    else:
      for x in ab:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0
    
    if not may:
      ingreso.append(0)
    else:
      for x in may:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not jun:
      ingreso.append(0)
    else:
      for x in jun:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not jul:
      ingreso.append(0)
    else:
      for x in jul:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0
    
    if not ag:
      ingreso.append(0)
    else:
      for x in ag:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not sep:
      ingreso.append(0)
    else:
      for x in sep:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not octu:
      ingreso.append(0)
    else:
      for x in octu:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not nov:
      ingreso.append(0)
    else:
      for x in nov:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0

    if not dec:
      ingreso.append(0)
    else:
      for x in dec:
        flag=0
        flag=lifestore_products[x][2]
        suma=suma+flag
      ingreso.append(suma)
      suma=0
    #Imprimo el total de ventas netas por cada mes, y la cantidad de productos vendidos en ese mes
    print("\nSe mostrará el total de las ventas mensuales descontando las devoluciones\n")
    print("Enero\n")
    print("Total mensual de ventas: $", ingreso[0])
    print("Cantidad de productos vendidos: ", len(en))

    print("\nFebrero\n")
    print("Total mensual de ventas: $", ingreso[1])
    print("Cantidad de productos vendidos: ", len(feb))

    print("\nMarzo\n")
    print("Total mensual de ventas: $", ingreso[2])
    print("Cantidad de productos vendidos: ", len(mar))

    print("\nAbril\n")
    print("Total mensual de ventas: $", ingreso[3])
    print("Cantidad de productos vendidos: ", len(ab))

    print("\nMayo\n")
    print("Total mensual de ventas: $", ingreso[4])
    print("Cantidad de productos vendidos: ", len(may))

    print("\nJunio\n")
    print("Total mensual de ventas: $", ingreso[5])
    print("Cantidad de productos vendidos: ", len(jun))

    print("\nJulio\n")
    print("Total mensual de ventas: $", ingreso[6])
    print("Cantidad de productos vendidos: ", len(jul))

    print("\nAgosto\n")
    print("Total mensual de ventas: $", ingreso[7])
    print("Cantidad de productos vendidos: ", len(ag))

    print("\nSeptiembre\n")
    print("Total mensual de ventas: $", ingreso[8])
    print("Cantidad de productos vendidos: ", len(sep))

    print("\nOctubre\n")
    print("Total mensual de ventas: $", ingreso[9])
    print("Cantidad de productos vendidos: ", len(octu))

    print("\nNoviembre\n")
    print("Total mensual de ventas: $", ingreso[10])
    print("Cantidad de productos vendidos: ", len(nov))

    print("\nDiciembre\n")
    print("\nTotal mensual de ventas: $", ingreso[11])
    print("Cantidad de productos vendidos: ", len(dec))

    suma=0
    #Sumo las ventas netas por cada mes para sacar la venta neta total del año
    for f in ingreso:
      suma=f+suma
    print("\nEl ingreso total anual fue de : $", suma)
    #Divido entre 12 para sacar el promedio mensual
    print("\nEl ingreso promedio mensual fue de : $", suma/12)

    #Guardo el numero de mes y la cantidad de ventas por cada mes, en una lista, para despues ordenar los meses de mayor a menor 
    ventas_mensuales=[[1,len(en)],[2,len(feb)],[3,len(mar)],[4,len(ab)],[5,len(may)],[6,len(jun)],[7,len(jul)],[8,len(ag)], [9,len(sep)],[10,len(octu)], [11,len(nov)],[12,len(dec)]]
    #Ordeno los meses de mayor a menor ventas
    long = len(ventas_mensuales)
    for i in range(long-1):
      for j in range(0,long-i-1):
        if ventas_mensuales[j][1] < ventas_mensuales[j+1][1]:
          ventas_mensuales[j], ventas_mensuales[j+1] = ventas_mensuales[j+1], ventas_mensuales[j]
    #Accedo a los 3 primeros elementos de la lista ventas_mensuales, pero como no se que mes es el que está en qué lugar, pregunto que mes es, por el numero de mes con el que se guardó la longitud de cada uno
    print("\nSe mostrarán los 3 meses con mayor cantidad de ventas:\n")
    if ventas_mensuales[0][0] == 1:
      print("El mes con mayor ventas fue: Enero", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 2:
      print("El mes con mayor ventas fue: Febrero", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 3:
      print("El mes con mayor ventas fue: Marzo", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 4:
      print("El mes con mayor ventas fue: Abril", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 5:
      print("El mes con mayor ventas fue: Mayo", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 6:
      print("El mes con mayor ventas fue: Junio", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 7:
      print("El mes con mayor ventas fue: Julio", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 8:
      print("El mes con mayor ventas fue: Agosto", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 9:
      print("El mes con mayor ventas fue: Septiembre", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 10:
      print("El mes con mayor ventas fue: Octubre", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 11:
      print("El mes con mayor ventas fue: Noviembre", "Con: ", ventas_mensuales[0][1], "ventas")
    elif ventas_mensuales[0][0] == 12:
      print("El mes con mayor ventas fue: Diciembre", "Con: ", ventas_mensuales[0][1], "ventas")
    
    if ventas_mensuales[1][0] == 1:
      print("El segundo  mes con mayor ventas fue: Enero", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 2:
      print("El segundo mes con mayor ventas fue: Febrero", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 3:
      print("El segundo mes con mayor ventas fue: Marzo", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 4:
      print("El segundo mes con mayor ventas fue: Abril", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 5:
      print("El segundo mes con mayor ventas fue: Mayo", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 6:
      print("El segundo mes con mayor ventas fue: Junio", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 7:
      print("El segundo mes con mayor ventas fue: Julio", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 8:
      print("El segundo mes con mayor ventas fue: Agosto", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 9:
      print("El segundo mes con mayor ventas fue: Septiembre", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 10:
      print("El segundo mes con mayor ventas fue: Octubre", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 11:
      print("El segundo mes con mayor ventas fue: Noviembre", "Con: ", ventas_mensuales[1][1], "ventas")
    elif ventas_mensuales[1][0] == 12:
      print("El segundo mes con mayor ventas fue: Diciembre", "Con: ", ventas_mensuales[1][1], "ventas")
    
    if ventas_mensuales[2][0] == 1:
      print("El tercer  mes con mayor ventas fue: Enero", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 2:
      print("El tercer mes con mayor ventas fue: Febrero", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 3:
      print("El tercer mes con mayor ventas fue: Marzo", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 4:
      print("El tercer mes con mayor ventas fue: Abril", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 5:
      print("El tercer mes con mayor ventas fue: Mayo", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 6:
      print("El tercer mes con mayor ventas fue: Junio", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 7:
      print("El tercer mes con mayor ventas fue: Julio", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 8:
      print("El tercer mes con mayor ventas fue: Agosto", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 9:
      print("El tercer mes con mayor ventas fue: Septiembre", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 10:
      print("El tercer mes con mayor ventas fue: Octubre", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 11:
      print("El tercer mes con mayor ventas fue: Noviembre", "Con: ", ventas_mensuales[2][1], "ventas")
    elif ventas_mensuales[2][0] == 12:
      print("El tercer mes con mayor ventas fue: Diciembre", "Con: ", ventas_mensuales[2][1], "ventas")
    
  es_admin += 1




