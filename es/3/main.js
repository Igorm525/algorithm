// 1. Переделайте makeGETRequest() так, чтобы она использовала промисы.
// 2. Добавьте в соответствующие классы методы добавления товара в корзину, удаления товара из корзины и получения списка товаров корзины.
// 3* Переделайте GoodsList так, чтобы fetchGoods() возвращал промис, а render() вызывался в обработчике этого промиса.

const API = 'https://raw.githubusercontent.com/GeekBrainsTutorial/online-store-api/master/responses/';

class Product {
  constructor(obj) {
    this.id = obj.id_product;
    this.title = obj.product_name;
    this.price = obj.price;
  }

  render() {
    return `
      <div class="col-lg-4 col-md-6 mb-4">
          <div class="card h-100">
              <a class="img-wrap" href="#"><img class="card-img-top" src="https://placehold.it/200x150" alt="${this.title}"></a>
              <div class="card-body">
                  <h5 class="card-title"><a class="text-info" href="#">${this.title}</a></h5>
                  <h5>${this.price}</h5>
              </div>
              <div class="card-footer">
                <button class="add btn btn-primary" data-id="${this.id}" data-title="${this.title}" data-price="${this.price}">
                    <i class="fa fa-plus"></i>&nbsp;Добавить
                </button>
              </div>
          </div>
      </div>
    `;
  }
}

class CartItem extends Product {
  constructor(obj) {
    super(obj);
    this.quantity = obj.quantity;
  }

  render() {
    return `
      <span class="cart-item dropdown-item" href="#" data-id="${this.id}">
        ${this.title}&nbsp;<span class="badge badge-primary" data-item-price>${this.price}</span>&nbsp;руб.&nbsp;<span data-item-quantity>${this.quantity}</span>&nbsp;шт.&nbsp;
        <button class="remove btn btn-danger btn-sm" data-id="${this.id}">x</button>
      </span>`;
  }
}

class ProductList {
  constructor(url = 'catalogData.json') {
    this.url = url;
    this.getJson()
      .then(data => this.handleData(data));
  }

  getJson(url = `${API + this.url}`) {
    return fetch(url)
      .then(result => result.json())
      .catch(error => console.log(error));
  }

  handleData(data) {
    this.items = data;
    this.render();
  }

  render() {
    document.querySelector('.products').innerHTML = this.items.map(item => (new Product(item)).render()).join('');
  }
}

class Cart extends ProductList {
  constructor(url = 'getBasket.json') {
    super(url);
    this.cart = this;
    this._init();
    this.getJson()
      .then(data => this.handleData(data.contents));
  }

  _init() {
    document.querySelector('.products').addEventListener('click', event => {
      if (event.target.classList.contains('add')) {
        this.cart.addItem(event.target);
      }
    });
    document.querySelector('.cart').addEventListener('click', event => {
      if (event.target.classList.contains('remove')) {
        this.cart.removeItem(event.target);
      }
    });
  }

  getProduct(target) {
    let id = +target.dataset.id;
    return this.items.find(item => item.id_product === id);
  }

  updateCart(item) {
    let block = document.querySelector(`.cart-item[data-id="${item.id_product}"]`);
    block.querySelector(`[data-item-quantity]`).textContent = `${item.quantity}`;
    block.querySelector(`[data-item-price]`).textContent = `${item.quantity * item.price}`
  }

  addItem(target) {
    this.getJson(`${API}/addToBasket.json`)
      .then(data => {
        if (data.result === 1) {
          let item = this.getProduct(target);
          if (item) {
            item.quantity++;
            this.updateCart(item);
          } else {
            this.items.push({
              id_product: +target.dataset.id,
              product_name: target.dataset.title,
              price: target.dataset.price,
              quantity: 1
            });
            this.render();
          }
        }
      });
  }

  removeItem(target) {
    this.getJson(`${API}/deleteFromBasket.json`)
      .then(data => {
        if (data.result === 1) {
          let item = this.getProduct(target);
          if (item.quantity > 1) {
            item.quantity--;
            this.updateCart(item);
          } else {
            this.items.splice(this.items.indexOf(item), 1);
            document.querySelector(`.cart-item[data-id="${item.id_product}"]`).remove();
          }
        }
      });
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.price);
  }

  render() {
    document.querySelector('.cart').innerHTML = this.items.length ? this.items.map(item => (new CartItem(item)).render()).join('') : '<li class="text-center">Пусто</li>';
  }
}

new ProductList();
new Cart();

