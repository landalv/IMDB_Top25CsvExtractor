# IMDB Top 25 Extractor

Este proyecto es un script de Python que toma como entrada un archivo CSV con el top 50 de películas (por defecto `IMDB_Top50.csv`) y produce un archivo de salida en formato JSON con el top 25 de las películas. El JSON resultante contiene el nombre de la película, su duración en minutos y su posición en la lista.
este proyecto se encuentra alojado en [github](https://github.com/landalv/IMDB_Top25CsvExtractor).

## Características

- **Entrada**: Acepta un archivo CSV con el listado de las películas. Este CSV debe tenr formato expecificado como el que se encuentra en el [archivo de ejemplo](https://drive.google.com/file/d/1zue8yX7khIwjm0ooXLKLfyPNRaC3OFMY/view?usp=sharing).
- **Salida**: Genera un archivo JSON con el top 25 de películas, con el formato especificado.
- **Flags**:
  - `--input`: Especifica el archivo CSV de entrada. Si no se proporciona, se utiliza `IMDB_Top50.csv` por defecto.
  - `--output`: Define el nombre o ruta del archivo JSON de salida. Si no se proporciona, se guarda con el nombre `Top25_IMDB.json`.
  - `--input-url`: Permite descargar un archivo CSV desde una URL. Este archivo se guarda con el nombre especificado en `--input` y se procesa de la misma manera.

## Formato de salida

El archivo JSON de salida contiene una lista de objetos, cada uno representando una película del top 25 con el siguiente formato:

```json
{
    "peliculas":[
        {
            "pelicula": "Nombre de la película",
            "duracion": 120,
            "puesto": 1
        },
        {
            "pelicula": "Otra película",
            "duracion": 150,
            "puesto": 2
        },
        ...
    ]
}
```

## Requisitos
- Python 3.13.0 (establecido en entrono virtual adjunto)
- libreria utils (adjunta) para gestión de logs

## Uso
Ejecutar el script de la siguiente manera:
```bash
python main.py [--input IMDB_Top50.csv] [--output salida.json] [--input-url URL]
```
### Ejemplos
1. Ejecutar con el archivo CSV por defecto (IMDB_Top50.csv):

```bash
python main.py
```
2. Especificar un archivo CSV de entrada:

```bash
python main.py --input otro_archivo.csv
```
3. Especificar un archivo JSON de salida:
```bash
python main.py --output mi_salida.json
```
4. Descargar un archivo CSV desde una URL:
```bash
python main.py --input-url https://drive.google.com/uc?export=download&id=1zue8yX7khIwjm0ooXLKLfyPNRaC3OFMY --input IMDB_Descargado.csv
```
> Nota: En este caso, el archivo CSV se descargará y guardará con el nombre IMDB_Descargado.csv y luego será utilizado como entrada para el proceso.

