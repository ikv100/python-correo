import json

def leeBase(ruta):
    with open(ruta) as file:
        
        data = json.load(file)
        print(data)

        for mail in data['informatica']:
            print( "Correos ", mail["mail"] )
            
        