# Python vs. nodeJs



| Lépés                                        | Python (Tkinter)                                              | Node.js (HTML, CSS, JS)                                        |
|----------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
| **Projekt mappa létrehozása**                | Létrehozom a projekt mappát.                                  | Létrehozom a projekt mappát.                                  |
| **Git inicializálása**                       | `git init`                                                     | `git init`                                                     |
| **Virtuális környezet létrehozása**          | `python -m venv venv`                                         | Nincs szükség virtuális környezetre.                           |
| **Virtuális környezet aktiválása**           | `source venv/bin/activate` (Mac/Linux) vagy `.env\Scripts\activate` (Windows) | Nincs szükség aktiválásra.                                    |
| **Függőségek telepítése**                    | `pip install tkinter` (ha nem alapértelmezett)                | `npm init -y` létrehozza a `package.json` fájlt.              |
| **Függőségek mentése fájlba**                | `pip freeze > requirements.txt`                               | Automatikusan a `package.json`-ba kerülnek a függőségek.      |
| **Fájlok létrehozása**                       | `main.py`                                                     | `index.html`, `styles.css`, `script.js`, `server.js`          |
| **Kód írása**                                | Tkinter alapú óra készítése (GUI kód).                        | HTML, CSS, JavaScript kód írása, valamint Node.js szerver.     |
| **Egyszerű szerver készítése**               | Nincs szükség, mert Tkinter külön ablakban futtatja az appot. | Írok egy alap szervert az `http` modul vagy az Express segítségével. |
| **Gitignore fájl létrehozása**               | Hozzáadom a `venv/` mappát a `.gitignore` fájlhoz.            | Hozzáadom a `node_modules/` mappát a `.gitignore` fájlhoz.    |
| **A projekt futtatása**                      | `python main.py`                                              | `node server.js`, majd böngészőben megnyitom az appot.        |

---

### Példa egyszerű Node.js szerverre
Egy alap szerver létrehozása az `Express` modullal:
```javascript
// server.js
const express = require('express');
const app = express();
const PORT = 3000;

// Statikus fájlok kiszolgálása a "public" mappából
app.use(express.static('public'));

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

```

### Lépések a Node.js app futtatásához
1. **Telepítsd az Express-t (opcionális):** `npm install express`
2. Futtasd a szervert: `node server.js`
3. Nyisd meg a böngészőben: [http://localhost:3000](http://localhost:3000).
