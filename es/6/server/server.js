// 1. Привязать добавление товара в корзину к реальному API.
// 2. Добавить API для удаления товара из корзины.
// 3. *Добавить файл stats.json, в котором будет храниться статистика действий пользователя с корзиной. В файле должны быть поля с названием действия (добавлено/удалено), названием товара, с которым производилось действие и временем, когда оно было совершено.

const express = require('express');
const fs = require('fs');
const cart = require('./cart');

const app = express();

app.use(express.json());
app.use('/', express.static('../public'));
app.use('/cart', cart);
app.get('/products', (req, res) => {
  fs.readFile('db/products.json', 'utf-8', (err, data) => {
    if (err) {
      res.sendStatus(404, JSON.stringify({result: 0, text: err}));
    } else {
      res.send(data)
    }
  })
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listen on port ${port}...`));
