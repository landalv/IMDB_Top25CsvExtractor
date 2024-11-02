import argparse
import csv
import json
import os
from urllib import request

from utils.Logger import LoggerFile
from utils.Logger import ColorLogger as logger

logfile = LoggerFile()

def createJson(data, fname = "IMDB.json"):
    try:
        #comprobación si existe el archivo anteriormente
        if os.path.isfile(fname):
            logger.info(f'Borrando archivo {fname} para regenerarlo')
            logfile.info(f'Borrando archivo {fname} para regenerarlo')
            os.remove(fname)
            
        #generación del archivo
        logger.info(f"Generando {fname}")
        logfile.info(f"Generando {fname}")
        
        
        
        out_path = fname
        ###Creamos la ruta de directoios de out si no existe
        folders = out_path.split('/')
        folders.pop(-1)
        logger.debug(f"Carpetas a crear:{folders}")
        logfile.debug(f"Carpetas a crear:{folders}")
        if folders!=[]:
            for x in range(1, len(folders)):
                folders[x]=os.path.join(folders[x-1],folders[x])
            
            if folders[0]=='.':
                folders.pop(0)
            
            #Creamos las carpetas de los output en cascada
            logger.debug(f"Carpetas a crear:{folders}")
            logfile.debug(f"Carpetas a crear:{folders}")
            for folder in folders:
                try:
                    os.stat(folder)
                except:
                    os.mkdir(folder)
        ###
        
        
        
        
        with open(fname, "w") as j:
            json.dump(data, j, indent=4)
    except Exception as ex:
        logger.error(f"Error al crear el archivo {fname}.")
        logfile.error(f"Error al leer el archivo {fname}.")
        exit(1)

def csvToArray(csv_file='IMDB_Top50.csv', csv_file_url = '', top_length=25):
    #añadir comprobción de que el archivo IMDB_Top.csv existe y sino ir a buscarlos a internet (https://drive.google.com/file/d/1zue8yX7khIwjm0ooXLKLfyPNRaC3OFMY/view?usp=sharing)
    
    #leyendo archivo csv
    logger.info(f'Leyendo archivo {csv_file}')
    logfile.info(f'Leyendo archivo {csv_file}')
    try:
        array = []
        in_path = csv_file
        ###Creamos la ruta de directoios de input si no existe
        folders = in_path.split('/')
        folders.pop(-1)
        logger.debug(f"Carpetas a crear:{folders}")
        logfile.debug(f"Carpetas a crear:{folders}")
        if folders!=[]:
            for x in range(1, len(folders)):
                folders[x]=os.path.join(folders[x-1],folders[x])
            
            if folders[0]=='.':
                folders.pop(0)
            
            #Creamos las carpetas de los output en cascada
            logger.debug(f"Carpetas a crear:{folders}")
            logfile.debug(f"Carpetas a crear:{folders}")
            for folder in folders:
                try:
                    os.stat(folder)
                except:
                    os.mkdir(folder)
        ###
        
        
        if (csv_file_url!=''):
            request.urlretrieve(csv_file_url, csv_file)
            
        if (not os.path.exists(csv_file)):
            csv_file_url = "https://drive.google.com/uc?export=download&id=1zue8yX7khIwjm0ooXLKLfyPNRaC3OFMY"
            logger.info(f'No se ha podido encontrar el archivo {csv_file}, asi que procederé a descargarlo de {csv_file_url}')
            logfile.info(f'No se ha podido encontrar el archivo {csv_file}, asi que procederé a descargarlo de {csv_file_url}')
            request.urlretrieve(csv_file_url, csv_file)
        
        
        with open(file=csv_file) as f:
            csv_reader = csv.reader(f, delimiter=',')
            position = 0
            for row in csv_reader:
                if position:
                    split_time = row[0].split("H")
                    split_time[0] = int(split_time[0])*60
                    split_time[1] = int(split_time[1][:-1])
                    minutes = split_time[0]+split_time[1]
                    
                    if (position <= top_length):
                        logger.debug("Posicion: {0}, Duración: {1}, Nombre: {2}".format(position, minutes, row[1]))
                        logfile.debug("Posicion: {0}, Duración: {1}, Nombre: {2}".format(position, minutes, row[1]))
                        array.append({"pelicula":row[1], "duracion":minutes, "puesto":position})
                position += 1   
            return array
    except Exception as ex:
        logger.error(f"Error al leer el archivo {csv_file}.")
        logfile.error(f"Error al leer el archivo {csv_file}.")
        exit(1)
        
def main():
    #paso de parametros al script
    parse = argparse.ArgumentParser()
    parse.add_argument("--input", type=str,default="assets/IMDB_Top50.csv",help="ruta de acceso al archivo .csv del cual se sacan los datos.")
    parse.add_argument("--input-url", type=str,default="",help="url al archivo .csv del cual se sacan los datos.")
    parse.add_argument("--output", type=str,default="assets/IMDB.json",help="ruta de acceso al archivo .json al cual creará con los datos de salida.")
    args=parse.parse_args()
    logger.debug("Parametros de entrada: {0}".format(args))
    logfile.debug("Parametros de entrada: {0}".format(args))
    #print(args)
    
    
    #ejecución del programa
    data = {"peliculas":csvToArray(csv_file=str(args.input), csv_file_url=str(args.input_url))}
    createJson(data, fname=str(args.output))
    logger.info("----------------------DATOS DE SALIDA----------------------")
    print(data)
    logfile.info("----------------------DATOS DE SALIDA----------------------")
    logfile.info(data)
    #borramos el logfile si no ha ocurrido ningun error que haga exit(1)
    logfile.deleteLogFile()
    

if __name__ == '__main__':
    main()    
