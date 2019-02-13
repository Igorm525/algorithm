// 1. Добавьте пустые классы для корзины товаров и элемента корзины товаров. Продумайте, какие методы понадобятся для работы с этими сущностями.
// 2. Добавьте для GoodsList метод, определяющий суммарную стоимость всех товаров.
// 3. *Некая сеть фастфуда предлагает несколько видов гамбургеров:
// ### Маленький (50 рублей, 20 калорий).
// ### Большой (100 рублей, 40 калорий). ### Гамбургер может быть с одним из нескольких видов начинок (обязательно):
// ### С сыром (+10 рублей, +20 калорий).
// ### С салатом (+20 рублей, +5 калорий).
// ### С картофелем (+15 рублей, +10 калорий). ### Дополнительно гамбургер можно посыпать приправой (+15 рублей, +0 калорий) и полить майонезом (+20 рублей, +5 калорий). ### 3Напишите программу, рассчитывающую стоимость и калорийность гамбургера. Можно использовать примерную архитектуру класса из методички, но можно использовать и свою.
//

class CartItem {
  constructor(title, price) {
    this.title = title;
    this.price = price;
  }
  render() {
    return `<div class="cart-item"><h3>${this.title}</h3><p>${this.price}</p></div>`;
  }
}

class Cart {
  constructor(items) {
    this.items = items;
  }
  getTotal() {
    return this.items.reduce((total, item) => total + item.price);
  }
  render() {
    document.querySelector('.cart').innerHTML = this.items.map(item => (new CartItem(item.title, item.price)).render()).join('');
  }
}

class GoodsItem {
  constructor(title, price) {
    this.title = title;
    this.price = price;
  }
  render() {
    return `<div class="goods-item"><h3>${this.title}</h3><p>${this.price}</p></div>`;
  }
}

class GoodsList {
  constructor() {
    this.goods = [];
  }
  getTotal() {
    return this.goods.reduce((total, item) => total + item.price);
  }
  fetchGoods() {
    this.goods = [
      { title: 'Shirt', price: 150 },
      { title: 'Socks', price: 50 },
      { title: 'Jacket', price: 350 },
      { title: 'Shoes', price: 250 },
    ];
  }
  render() {
    let listHtml = '';
    this.goods.forEach(good => {
      const goodItem = new GoodsItem(good.title, good.price);
      listHtml += goodItem.render();
    });
    document.querySelector('.goods-list').innerHTML = listHtml;
  }
}

const list = new GoodsList();
list.fetchGoods();
list.render();

const products = [
    {title: 'Notebook', price: 2000, img: 'http://pluspng.com/img-png/free-png-laptop-laptop-free-png-image-2046.png'},
    {title: 'Mouse', price: 20, img: 'http://pluspng.com/img-png/mouse-hd-png-avid-media-composer-or-many-othernle-s-the-bella-corporation-has-a-mouse-that-will-improve-your-editing-workflow-the-hd-mouse-is-an-incredibly-504.png'},
    {title: 'Keyboard', price: 35, img: 'http://pluspng.com/img-png/keyboard-hd-png-keyboard-png-hd-png-image-419.png'},
];

const renderProduct = (item) => `
<div class="col-lg-4 col-md-6 mb-4">
    <div class="card h-100">
        <a class="img-wrap" href="#"><img class="card-img-top" src="${item.img}" alt="${item.title}"></a>
        <div class="card-body">
            <h5 class="card-title">
                <a class="text-info" href="#">${item.title}</a>
            </h5>
            <h5>${item.price}</h5>
        </div>
    </div>
</div>
`;

const renderPage = (list = products) => {
    document.querySelector('.products').innerHTML = list.map(item => renderProduct(item)).join('');
};

renderPage();

