# Gestió d'usuaris amb Flask, Redis i Docker

Aquest projecte és una aplicació web molt simple per gestionar usuaris amb alta, baixa i llistat, utilitzant:

- Backend en **Flask** (Python)
- Base de dades **Redis**
- Frontend en HTML+JavaScript
- Contenidors Docker amb `docker-compose`

---

## Descripció general

L'aplicació permet:

- Afegir usuaris (nom, password, rol)
- Llistar usuaris
- Eliminar usuaris

La informació es guarda a Redis i es mostra en un frontend senzill. El projecte es pot desplegar fàcilment amb Docker.

---

## Fitxers i carpetes

### `redis_app.py`

És el servidor Flask que:

- Serveix el frontend (`index.html`)
- Gestiona les rutes API per afegir (`/add`), llistar (`/list`) i eliminar (`/delete/<username>`) usuaris
- Es comunica amb Redis per guardar i recuperar dades

---

### `static/index.html`

El frontend HTML amb JavaScript que:

- Mostra un formulari per afegir usuaris
- Llista els usuaris actuals
- Permet eliminar usuaris amb un botó 🗑️
- Fa peticions AJAX al backend per interaccionar amb Redis

---

### `Dockerfile`

Defineix la imatge Docker per executar el servidor Flask:

- Partim d’una imatge base de Python
- Copiem els fitxers de l’aplicació
- Instal·lem les dependències (Flask i redis-py)
- Exposem el port 5000 i executem el servidor

---

### `docker-compose.yml`

Configura el desplegament de l’aplicació amb dos serveis:

- **web**: el servidor Flask (construït a partir del Dockerfile)
- **redis**: el contenidor oficial de Redis

També exposa els ports 5000 (app) i 6379 (Redis).

---

## Desplegament

Per executar localment (amb Docker i docker-compose):

```bash
git clone https://github.com/iesbillenguatges/hosted-runners.git
cd hosted-runners
docker-compose up --build
