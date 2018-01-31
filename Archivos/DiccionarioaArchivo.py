cines = {'Riocentro Ceibos': {'pelicula':{'nombre':'Coco','categoria':'infantil'},'reservas':25, 'asientos':30, 'tipo': '3D', 'horarios': ['10h30', '13h45', '15h30', '18h00']},
         'Riocentro Dorado': {'reservas':20, 'asientos':25, 'tipo': 'Digital', 'pelicula':{'nombre':'Jumanji', 'categoria':'aventura'}, 'horarios': ['12h30', '14h50', '18h30', '20h40']},
         'San Marino': {'reservas':24, 'asientos':32, 'tipo': '3D', 'pelicula':{'nombre':'JUMANJI', 'categoria':'aventura'}, 'horarios': ['11h30', '14h15', '19h30']},
         'Riocentro entre Ríos': {'reservas':32, 'asientos':32, 'tipo': 'Digital', 'pelicula':{'nombre':'Coco', 'categoria':'infantil'}, 'horarios': ['9h30', '12h15']},
         'Av. 6 diciembre': {'reservas':29, 'asientos':32, 'tipo': 'Digital', 'pelicula':{'nombre':'Starwars', 'categoria':'ficcion'}, 'horarios': ['17h30', '20h45', '23h30']},
         'Riocentro Norte': {'reservas':28, 'asientos':32, 'tipo': '3D', 'pelicula':{'nombre':'Implacable', 'categoria':'suspenso'}}}


def escribeCines(cines):
    archivo = open("cines.txt","a")
    for k, v in cines.items():
        cc = k
        pelicula = v.get("pelicula").get("nombre")
        categoria = v.get("pelicula").get("categoria")
        res = v.get("reservas")
        asi = v.get("asientos")
        tipSala = v.get("tipo")
        linea = k+","+pelicula+"-"+categoria+"|"+str(res)+"|"+str(asi)+"|"+tipSala
        archivo.write(linea+"\n")
    archivo.close()

escribeCines("cines.txt")