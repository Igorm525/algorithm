// 1. Переделайте makeGETRequest() так, чтобы она использовала промисы.
// 2. Добавьте в соответствующие классы методы добавления товара в корзину, удаления товара из корзины и получения списка товаров корзины.
// 3* Переделайте GoodsList так, чтобы fetchGoods() возвращал промис, а render() вызывался в обработчике этого промиса.

const API = 'https://raw.githubusercontent.com/GeekBrainsTutorial/online-store-api/master/responses';

class CartItem {
  constructor(title, price) {
    this.title = title;
    this.price = price;
  }

  render() {
    return `<a class="cart-item dropdown-item" href="#">${this.title}&nbsp;<span class="badge badge-primary">${this.price}$</span>&nbsp;<button class="remove btn btn-danger btn-sm">x</button></a>`;
  }
}

class Cart {
  constructor() {
    this.items = [];
    const promise = new Promise((resolve, reject) => {
      this.fetchItems(resolve);
    });
    promise.then(() => {
      this.render();
    });
  }

  init() {
    let cart = this;
    document.addEventListener('click', function (event) {
      if (event.target.classList.contains('add')) {
        cart.items.push({
          product_name: event.target.dataset.title,
          price: event.target.dataset.price
        });
        cart.render();
      } else if (event.target.classList.contains('remove')) {
        event.target.parentNode.remove();
      }
    });
  }

  fetchItems(resolve) {
    fetch(`${API}/getBasket.json`)
      .then(result => result.json())
      .then(data => {
        this.items = data.contents;
        resolve();
      })
      .catch(error => console.log(error));
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.price);
  }

  render() {
    document.querySelector('.cart').innerHTML = this.items.map(item => (new CartItem(item.product_name, item.price)).render()).join('');
  }
}

class Product {
  constructor(title, price) {
    this.title = title;
    this.price = price;
  }

  render() {
    return `
<div class="col-lg-4 col-md-6 mb-4">
    <div class="card h-100">
        <a class="img-wrap" href="#"><img class="card-img-top" src="https://placehold.it/200x150" alt="${this.title}"></a>
        <div class="card-body">
            <h5 class="card-title">
                <a class="text-info" href="#">${this.title}</a>
            </h5>
            <h5>${this.price}</h5>
        </div>
        <div class="card-footer"><button class="add btn btn-primary" data-title="${this.title}" data-price="${this.price}"><i class="fa fa-plus"></i>&nbsp;Добавить</button></div>
    </div>
</div>
`;
  }
}

class ProductList {
  constructor() {
    this.items = [];
    this.fetchItems();
    this.render();
  }

  fetchItems() {
    fetch(`${API}/catalogData.json`)
      .then(result => result.json())
      .then(data => {
        this.items = data;
        this.render();
      })
      .catch(error => console.log(error));
  }

  render() {
    document.querySelector('.products').innerHTML = this.items.map(item => (new Product(item.product_name, item.price)).render()).join('');
  }
}

const productList = new ProductList();
const cart = new Cart();
window.onload = () => cart.init();

