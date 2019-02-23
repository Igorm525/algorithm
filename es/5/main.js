// 1. Добавить методы и обработчики событий для поля поиска. Создать в объекте данных поле searchLine и привязать к нему содержимое поля ввода. На кнопку «Искать» добавить обработчик клика, вызывающий метод FilterGoods.
// 2. Добавить корзину. В html-шаблон добавить разметку корзины. Добавить в объект данных поле isVisibleCart, управляющее видимостью корзины.
// 3. *Добавлять в .goods-list заглушку с текстом «Нет данных» в случае, если список товаров пуст.

const API = 'https://raw.githubusercontent.com/GeekBrainsTutorial/online-store-api/master/responses/';

const app = new Vue({
  el: '#app',
  data: {
    products: [],
    cartProducts: [],
    filteredProducts: [],
    searchLine: '',
    isVisibleCart: true
  },
  methods: {
    filter() {
      this.filteredProducts = this.searchLine
        ? this.filteredProducts.filter(el => { return el.product_name.toLowerCase().includes(this.searchLine); })
        : this.products;
    },
    add(item) {
      this.fetch('addToBasket', data => {
        if (data.result === 1) {
          if (this.cartProducts.indexOf(item)) {
            this.cartProducts.find(el => el.id_product === item.id_product).quantity++;
          } else {
            item.quantity = 1;
            this.cartProducts.push(item);
          }
        }
      });
    },
    remove(item) {
      this.fetch('deleteFromBasket', data => {
        if (data.result === 1) {
          if (item.quantity > 1) {
            item.quantity--;
          } else {
            this.cartProducts.splice(this.cartProducts.indexOf(item), 1);
          }
        }
      });
    },
    fetch(url, func) {
      return fetch(`${API}/${url}.json`)
        .then(result => result.json())
        .then(data => func(data))
        .catch(error => console.log(error));
    },
  },
  mounted() {
    this.fetch('catalogData', data => {
      this.products = data;
      this.filteredProducts = data;
    });
    this.fetch('getBasket', data => {
      this.cartProducts = data.contents;
    });
  }
});

