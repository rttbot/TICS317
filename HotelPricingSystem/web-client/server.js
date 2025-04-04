const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());

// Ruta GET para pruebas
app.get('/reservar', (req, res) => {
    res.send('Ruta de reserva disponible');
});

app.post('/reservar', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:5000/reservar', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error al reservar');
    }
});

app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000');
});