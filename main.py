import json

def leeBase(ruta):
    with open(ruta) as file:
        
        data = json.load(file)
        print(data)

        for mail in data['informatica']:
            print( "Correos ", mail["mail"] )
            
            


if __name__ == "__main__":
    print("Inicio este programa")
    ruta = 'baseDatos.json'
    leeBase(ruta)