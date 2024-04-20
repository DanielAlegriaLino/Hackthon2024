import zipfile
import os

def zip_tostr(archivo_zip):
    contenido_txt = None

    try:
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            archivos_en_zip = zip_ref.namelist()
            
            for archivo in archivos_en_zip:
                if archivo.endswith('.txt'):
                    with zip_ref.open(archivo) as txt_file:
                        contenido_txt = txt_file.read().decode('utf-8')
                    break  
    except Exception as e:
        print("Error al abrir el archivo zip:", e)
    
    return contenido_txt
    