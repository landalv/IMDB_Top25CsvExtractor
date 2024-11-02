import datetime
import logging
import os
from time import sleep
import traceback

class Logger:
    
        
    def __set_logger(self, lv=logging.INFO):
        #Definimos el formato de loggings por defecto
        LOG_FORMAT = '[{asctime}] {levelname} - {message}'

        class CustomFormatter(logging.Formatter):
            def format(self, record):
                format = LOG_FORMAT
                formatter = logging.Formatter(format, style="{")
                return formatter.format(record)
        
        logger = logging.getLogger(__name__)
        logger.setLevel(lv)
            
        handlers = logging.StreamHandler()
        handlers.setFormatter(CustomFormatter())
        
        if(logger.hasHandlers()):
            logger.handlers.clear()
        
        logger.addHandler(handlers)
        return logger

        logging.basicConfig(
            level=lv,
            handlers=[handlers]
        )
        
    
    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)
            if(level=="critical"):
                logger.critical(message)
            elif(level=="debug"):
                logger.debug(message)
            elif(level=="info"):
                logger.info(message)
            elif(level=="warning"):
                logger.warning(message)
            elif(level=="error"):
                logger.error(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
    
    @classmethod
    def info(self,msg):
        self.add_to_log(level="info", message=msg)
    @classmethod
    def debug(self,msg):
        self.add_to_log(level="debug", message=msg)
    @classmethod
    def warning(self,msg):
        self.add_to_log(level="warning", message=msg)
    @classmethod
    def error(self,msg):
        self.add_to_log(level="error", message=msg)
    @classmethod
    def critical(self,msg):
        self.add_to_log(level="critical", message=msg)

class LoggerFile:
    
    logFile = f'./logs/errorlog - {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}.log'
    logFolders = []
    
    def __init__(self, filename=f'./logs/errorlog - {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}.log'):
        self.logFile = filename
    
        
        
    def __set_logger(self, lv=logging.DEBUG):
        #Definimos el formato de loggings por defecto
        LOG_FORMAT = '[{asctime}] {levelname} - {message}'
        
        log_path = self.logFile
        log_directory = ''
        
        ###Creamos la ruta de directoios de log si no existe
        folders = log_path.split('/')
        folders.pop(-1)
        #print (folders)
        
        for x in range(1, len(folders)):
            folders[x]=os.path.join(folders[x-1],folders[x])
        
        if folders[0]=='.':
            folders.pop(0)
        
        self.logFolders=folders
        
        #Creamos las carpetas de los logs en cascada
        for folder in folders:
            try:
                os.stat(folder)
            except:
                os.mkdir(folder)
        ###
        

        logger = logging.getLogger(__name__)
        logger.setLevel(lv)
        
        #log_path = os.path.join(log_directory, log_filename)
        
        
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(lv)
        
        formatter = logging.Formatter(LOG_FORMAT, style="{")
        file_handler.setFormatter(formatter)
        
        if(logger.hasHandlers()):
            logger.handlers.clear()
        
        logger.addHandler(file_handler)
        return logger
    
    def deleteLogFile(self):
        os.remove(self.logFile)
        
    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)
            if(level=="critical"):
                logger.critical(message)
            elif(level=="debug"):
                logger.debug(message)
            elif(level=="info"):
                logger.info(message)
            elif(level=="warning"):
                logger.warning(message)
            elif(level=="error"):
                logger.error(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
    
    @classmethod
    def info(self,msg):
        self.add_to_log(level="info", message=msg)
    @classmethod
    def debug(self,msg):
        self.add_to_log(level="debug", message=msg)
    @classmethod
    def warning(self,msg):
        self.add_to_log(level="warning", message=msg)
    @classmethod
    def error(self,msg):
        self.add_to_log(level="error", message=msg)
    @classmethod
    def critical(self,msg):
        self.add_to_log(level="critical", message=msg)

class ColorLogger:
    
        
    def __set_logger(self, lv=logging.DEBUG):
        #Definimos el formato de loggings por defecto
        LOG_FORMAT = '[{asctime}] {levelname} - {message}'
        #Definimos los colores en ASCII para cada nivel
        FORMATS={
            logging.DEBUG: f"\33[32m{LOG_FORMAT}\33[0m",
            logging.INFO: f"\33[34m{LOG_FORMAT}\33[0m",
            logging.WARNING: f"\33[33m{LOG_FORMAT}\33[0m",
            logging.ERROR: f"\33[31m{LOG_FORMAT}\33[0m",
            logging.CRITICAL: f"\33[35m{LOG_FORMAT}\33[0m"
        }

        class CustomFormatter(logging.Formatter):
            def format(self, record):
                format = FORMATS[record.levelno]
                formatter = logging.Formatter(format, style="{")
                return formatter.format(record)
        
        logger = logging.getLogger(__name__)
        logger.setLevel(lv)
            
        handlers = logging.StreamHandler()
        handlers.setFormatter(CustomFormatter())
        
        if(logger.hasHandlers()):
            logger.handlers.clear()
        
        logger.addHandler(handlers)
        return logger

        logging.basicConfig(
            level=lv,
            handlers=[handlers]
        )
        
    
    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)
            if(level=="critical"):
                logger.critical(message)
            elif(level=="debug"):
                logger.debug(message)
            elif(level=="info"):
                logger.info(message)
            elif(level=="warning"):
                logger.warning(message)
            elif(level=="error"):
                logger.error(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
    
    @classmethod
    def info(self,msg):
        self.add_to_log(level="info", message=msg)
    @classmethod
    def debug(self,msg):
        self.add_to_log(level="debug", message=msg)
    @classmethod
    def warning(self,msg):
        self.add_to_log(level="warning", message=msg)
    @classmethod
    def error(self,msg):
        self.add_to_log(level="error", message=msg)
    @classmethod
    def critical(self,msg):
        self.add_to_log(level="critical", message=msg)

