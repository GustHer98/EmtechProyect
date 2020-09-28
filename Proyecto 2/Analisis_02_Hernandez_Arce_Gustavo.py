import csv

#lectura del archivo csv convirtiendolo en una lista
#de diccionarios
def lectura():
    lista=[]
    with open("synergy_logistics_database.csv", "r", encoding="utf-8") as archivo:
        lector=csv.DictReader(archivo)
        for linea in lector:
            lista.append(linea)
    return lista

#función para la consigna 1
def filtra_rutas(direccion, lista_lec):
  contador=0
  rutas_contadas=[]
  suma=0
  conteo_rutas=[]
  lista = []
  #separo los diccionarios de la direccion correspondiente, es decir, en exportaciones e importaciones, uno por cada llamado de la función
  for y in lista_lec:
    if y["direction"] == direccion:
      lista.append(y)
  #itero en cada lista
  for ruta in lista:
    if ruta["direction"] == direccion:
      #se guardan los valores de las rutas en turno para preguntar si ya estan en la lista de las rutas contadas
      ruta_actual = [ruta["origin"],ruta["destination"]]
      if ruta_actual not in rutas_contadas:
        #se vuelve a iterar sobre la lista, ahora para comparar la ruta en turno con todas las demás y contar cuantas veces se repite
        for mov in lista:
          if ruta_actual == [mov["origin"],mov["destination"]]:
            contador += 1
            #se cuentan las veces que se repite esa ruta y se suma el valor que brinda
            suma+=int(mov["total_value"])
        rutas_contadas.append(ruta_actual)
        formato = [ruta["origin"],ruta["destination"],contador,suma]
        conteo_rutas.append(formato)
        #se reinician los contadores para la siguiente iteración
        contador=0
        suma=0
  #se ordenan las rutas por el valor que brindan
  conteo_rutas.sort(reverse=True, key=lambda x:x[3])
  #se devuelve la lista con las rutas, las veces que se repiten y el valor
  return conteo_rutas

def transporte(direccion, lista_lec):
  suma=0
  transp=[]
  transp_actual=[]
  transp_suma=[]
  lista=[]
  #separo los diccionarios de la direccion correspondiente, es decir, en exportaciones e importaciones, uno por cada llamado de la función
  for y in lista_lec:
    if y["direction"] == direccion:
      lista.append(y)
   #se guardan los valores de los transportes en turno
  for t in lista:
    if t["direction"] == direccion:
      transp_actual = [t["transport_mode"]]
      if transp_actual not in transp:
        #se itera de nuevo la lista con el transporte en turno para sumar los valores del mismo transporte
        for mov in lista:
          if transp_actual == [mov["transport_mode"]]:
            #se suma el valor que genera cada transporte 
            suma+=int(mov["total_value"])
        transp.append(transp_actual)
        formato = [t["transport_mode"], suma]
        transp_suma.append(formato)
        suma=0
  #se ordenan los transportes por el valor que generan
  transp_suma.sort(reverse=True, key=lambda x:x[1])
  return transp_suma

def Consigna_3(direccion, lista_lec):
  rutas_contadas=[]
  suma=0
  conteo_rutas=[]
  suma_total=0
  lista=[]
  #para las exportaciones se tomara el país de origen, para las importaciones los países de Destino
  if direccion == "Exports":
    x = "origin"
  elif direccion == "Imports":
    x= "destination"

  #se hace lo mismo que en la consigna 1, pero en este caso solo se guarda el país dependiendo de la dirección
  for y in lista_lec:
    if y["direction"] == direccion:
      lista.append(y)
  for pais in lista:
    if pais["direction"] == direccion:
      pais_actual = [pais[x]]
      if pais_actual not in rutas_contadas:
        for mov in lista:
          if pais_actual == [mov[x]]:
            #se hace la suma del valor que genera cada país depediendo de si exporta o importa
            suma+=int(mov["total_value"])
        rutas_contadas.append(pais_actual)
        formato = [pais[x],suma]
        conteo_rutas.append(formato)
        suma=0
  conteo_rutas.sort(reverse=True, key=lambda x:x[1])
  #se hace la suma del valor total de exportaciones y de importaciones
  for y in conteo_rutas:
    suma_total += int(y[1])
  #para cada valor total que genera cada país, se divide entre el valor total de importaciones o exportaciones(dependiendo el caso) y se multiplica por 100 para sacar lo que ese valor por país representa en porcentaje
  for z in conteo_rutas:
    z[1] = (z[1]/suma_total)*100
  #se imprime la lista con los valores de cada país por porcentaje
  return conteo_rutas
#Función para quedarme con los primeros países que sumen 80% de valor dependiendo de exportación o importación
def porcentaje(lista):
  suma = 0
  nueva_lista=[]
  for x in lista:
    if suma < 80:
      suma+=x[1]
      nueva_lista.append(x)
    else:
      break
  return nueva_lista

def main():
  #llamo la función que leerá el archivo
  lista=lectura()
  #menú para seleccionar opción
  print("1. Mejores rutas de exportación y exportación\n")
  print("2. Medio de transporte utilizado\n")
  print("3. Valor total de importaciones y exportaciones\n")
  opcion=int(input("Ingrese una opción: "))
  if opcion == 1:
    #listas donde se llamarán la función que filtra las rutas para exportación e importación
    rutas_exp=[]
    rutas_imp=[]
    c=0
    rutas_exp=filtra_rutas("Exports", lista)
    rutas_imp=filtra_rutas("Imports", lista)
    print("\nSe muestran las 10 rutas más demandas en exportaciones:\n")
    for x in rutas_exp:
      #impresión de las 10 primeras rutas de exportación ordenadas por valor
      print("Origen: ", x[0], "Destino: ", x[1],"Repeticiones: ", x[2], "Valor: ", x[3])
      c+=1
      if c == 10:
        c=0
        break
      #impresión de las 10 primeras de importación ordenadas por valor
    print("\nSe muestran las 10 rutas más demandas en importaciones:\n")
    for y in rutas_imp:
      print("Origen: ", y[0], "Destino: ", y[1],"Repeticiones: ", y[2], "Valor: ", y[3])
      c+=1
      if c == 10:
        break
  else:
    if opcion == 2:
      exports=[]
      imports=[]
      c=0
      #llamado de la función que filtrará los medios de transporte
      exports=transporte("Exports", lista)
      imports=transporte("Imports", lista)
      print("Se muestran los 3 medios de transporte más importantes en exportaciones:\n")
      for x in exports:
        #impresión de los 3 primeros medios de transporte ordenados por valor
        print("Transporte: ", x[0], "Valor: ", x[1])
        c+=1
        if c == 3:
          c=0
          break
      print("\nSe muestran los 3 medios de transporte más importantes en importaciones:\n")
      for y in imports:
        print("Transporte: ", y[0], "Valor: ", y[1])
        c+=1
        if c== 3:
          break
    else:
      if opcion == 3:
        exports=[]
        imports=[]
        #llamado de la función que devolverá los porcentajes que genera cada país
        exports = Consigna_3("Exports", lista)
        imports = Consigna_3("Imports", lista)
        #paso las listas para que se quede únicamente con las primeras sumen 80% con un error de +-2
        exports = porcentaje(exports)
        imports = porcentaje(imports)
        print("\nSe muestran los países que generan el 80% del valor de exportaciones:\n")
        #impresión de los países que generan el 80% del valor total de exportaciones e importaciones
        for y in exports:
          print("País: ", y[0], "Porcentaje: ", y[1])
        print("\nSe muestran los países que generan el 80% del valor de importaciones:\n")
        for x in imports:
          print("País: ", x[0], "Porcentaje: ", x[1])
      else:
        print("Ingrese una opción válida\n")

  return
main()
 