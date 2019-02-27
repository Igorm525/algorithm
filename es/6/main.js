// 1. Вынести поиск в отдельный компонент.
// 2. Вынести корзину в отдельный компонент.
// 3. *Создать компонент с сообщением об ошибке. Компонент должен отображаться, когда не удаётся выполнить запрос к серверу.

const API = 'https://raw.githubusercontent.com/GeekBrainsTutorial/online-store-api/master/responses/';


Vue.component('search', {
  props: ['query'],
  template: `
<div class="container">
    <form class="mb-5 form-inline" @submit.prevent="$emit('filter', query)">
        <i class="fas fa-search" aria-hidden="true"></i>
        <input class="form-control form-control-sm ml-3 w-75" v-model="query" type="text" placeholder="Search" aria-label="Search">
    </form>
</div>
  `
});

Vue.component('cart', {
  props: ['products', 'visibility'],
  methods: {
    total() {
      return this.products.reduce((acc, item) => acc + item.price, 0);
    },
  },
  template: `
<li class="nav-item dropdown" v-show="visibility">
    <a class="nav-link" href="#" role="button" data-toggle="dropdown">
        <i class="fas fa-shopping-basket text-warning"></i>&nbsp;Корзина<span class="caret"></span>
    </a>
    <ul class="cart dropdown-menu">
        <cart-product v-for="product in products" :product="product" :key="product.id_product"></cart-product>
        <span class="dropdown-item" v-if="products.length">Всего&nbsp;на:&nbsp;<span class="badge badge-info">{{ total() }}</span>&nbsp;руб.</span>
        <span class="dropdown-item" v-else>Корзина пуста</span>
    </ul>
</li>
  `
});

Vue.component('cart-product', {
  props: ['product'],
  template: `
    <span class="cart-item dropdown-item" href="#">
        {{ product.product_name }}&nbsp;
        <span class="badge badge-warning">{{ product.price }}</span>&nbsp;руб.&nbsp;
        <span>{{ product.quantity }}</span>&nbsp;шт.&nbsp;
        <button class="remove btn btn-danger btn-sm" @click="$parent.$emit('remove', product)">x</button>
    </span>
`
});

Vue.component('products', {
  props: ['products'],
  template: `
<div class="container">
  <div class="products row">
    <product v-for="product in products" :product="product" :key="product.id_product"></product>
  </div>
</div>
`
});

Vue.component('product', {
  props: ['product'],
  template: `
<div class="col-lg-4 col-md-6 mb-4" >
    <div class="card h-100">
        <a class="img-wrap" href="#"><img class="card-img-top" src="https://placehold.it/200x150"></a>
        <div class="card-body">
            <h5 class="card-title"><a class="text-info" href="#">{{ product.product_name }}</a></h5>
            <h5>{{ product.price }}</h5>
        </div>
        <div class="card-footer">
            <button class="btn btn-primary" @click="$parent.$emit('add-product', product)"><i class="fa fa-plus"></i>&nbsp;Добавить</button>
        </div>
    </div>
</div>
  `
});

Vue.component('errors', {
  props: ['messages'],
  template: `
<div class="container">
  <div class="row" v-for="message in messages">
    <div class="alert alert-primary alert-dismissible fade show" role="alert">{{ message }}<button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button></div>
  </div>
</div>
`
});

const app = new Vue({
  el: '#app',
  data: {
    products: [],
    cartProducts: [],
    filteredProducts: [],
    errorMessages: [],
    isVisibleCart: true
  },
  methods: {
    addProduct(item) {
      this.fetch('addToBasket', data => {
        if (data.result === 1) {
          let existed = this.cartProducts.find(el => el.id_product === item.id_product);
          if (existed) {
            existed.quantity++;
            existed.price += item.price;
          } else {
            let product = Object.assign({quantity: 1}, item);
            this.cartProducts.push(product);
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
    filter(query) {
      this.filteredProducts = this.products.filter(item => {
        return query ? item.product_name.toLowerCase().includes(query) : true;
      });
    },
    fetch(url, func) {
      return fetch(`${API}/${url}.json`)
        .then(result => result.json())
        .then(data => func(data))
        .catch(error => this.errorMessages.push('Произошла ошибка отправки'));
    },
  },
  mounted() {
    this.fetch('getBasket', data => {
      this.cartProducts = data.contents;
    });
    this.fetch('catalogData', data => {
      this.products = this.filteredProducts = data;
    });
  },
});

