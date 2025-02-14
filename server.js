const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('<h1>Hello world!</h1>');
});

app.get('/about', (req, res) => {
    res.send('<h1>About page</h1><p>Its me</p>');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});