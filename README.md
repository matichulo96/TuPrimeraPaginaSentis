## 1 - Creación del entorno virtual

```bash
python -m venv .venv
```

## 2 - Activación del entorno virtual (Windows / Powershell)
```bash
.\.venv\Scripts\Activate.ps1
```

## 3 - Instalacion de requirements.txt
```bash
pip install -r requirements.txt
```

## 4 - Puesta en marcha del servidor de desarrollo
```bash
cd bookstore
python migrate.py runserver
```

## 5 - Subir a base de datos las tres paginas
Se puede ingresar a las siguientes páginas para insertar nuevos registros en la base de datos:

http://localhost:8000/insertar/autor

http://localhost:8000/insertar/libro

http://localhost:8000/insertar/editorial

## 6 - Buscar libro en base de datos

Se puede ingresar a la siguiente página para buscar un libro por título en la base de datos>

http://localhost:8000/buscar/libro

