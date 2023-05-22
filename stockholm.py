from cryptography.fernet import Fernet
import sys, os

extension = ".ft"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            path_to_encrypt = sys.argv[1]
            items = os.listdir(path_to_encrypt)
            print(items)            
        except:
            print ("No se encontraron ficheros para encryptar")
    else:
        print("La cantidad de argumentos es erronea.")
