const cart = {
  data: function () {
    return {
      products: [],
    }
  },
  methods: {
    add(item) {
      let existed = this.products.find(el => el.id_product === item.id_product);
      if (existed) {
        this.$parent.fetch(`cart/${existed.id_product}`, data => {
          if (data.result === 1) {
            existed.quantity++;
            existed.price += item.price;
          }
        }, 'put', {quantity: 1});
      } else {
        let product = Object.assign({quantity: 1}, item);
        this.$parent.fetch('cart', data => {
          if (data.result === 1) {
            this.products.push(product);
          }
        }, 'post', product);
      }
    },
    remove(item) {
      this.$parent.fetch(`cart/${item.id_product}`, data => {
        if (data.result === 1) {
          if (item.quantity > 1) {
            item.quantity--;
          } else {
            this.products.splice(this.products.indexOf(item), 1);
          }
        }
      }, 'delete');
    },
    total() {
      return this.products.reduce((acc, item) => acc + item.price, 0);
    },
  },
  created() {
    this.$parent.fetch('cart', data => {
      this.products = data.contents;
    });
  },
  template: `
<li class="nav-item dropdown">
  <a class="nav-link" href="#" role="button" data-toggle="dropdown">
    <i class="fas fa-shopping-basket text-warning"></i>&nbsp;Корзина<span class="caret"></span>
  </a>
  <ul class="cart dropdown-menu">
    <span class="cart-item dropdown-item" href="#" v-for="product in products" :product="product" :key="product.id_product">
      {{ product.product_name }}&nbsp;
      <span class="badge badge-warning">{{ product.price }}</span>&nbsp;руб.&nbsp;
      <span>{{ product.quantity }}</span>&nbsp;шт.&nbsp;
      <button class="remove btn btn-danger btn-sm" @click="remove(product)">x</button>
    </span>
    <span class="dropdown-item" v-if="products.length">Всего&nbsp;на:&nbsp;<span class="badge badge-info">{{ total() }}</span>&nbsp;руб.</span>
    <span class="dropdown-item" v-else>Корзина пуста</span>
  </ul>
</li>
  `
};

export default cart;
