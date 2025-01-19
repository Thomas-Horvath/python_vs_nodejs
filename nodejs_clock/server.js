const express = require('express');
const app = express();
const port = 3000;


// Statikus fájlok kiszolgálása a "public" mappából
app.use(express.static('public'))


app.listen(port, () => {
    console.log(`A szerer a http://localhost:${port} címen fut!`);
})