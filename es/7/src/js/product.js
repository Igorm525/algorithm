const product = {
  data: function () {
    return {
      products: [],
      filtered: []
    }
  },
  methods: {
    filter(query) {
      this.filtered = this.products.filter(item => {
        return query ? item.product_name.toLowerCase().includes(query) : true;
      });
    },
  },
  created() {
    this.$parent.fetch('products', data => {
      this.products = this.filtered = data;
    });
  },
  template: `
<div class="container">
  <div class="products row">
    <div class="col-lg-4 col-md-6 mb-4" v-for="product in filtered" :product="product" :key="product.id_product">
      <div class="card h-100">
        <a class="img-wrap" href="#"><img class="card-img-top" src="https://placehold.it/200x150"></a>
        <div class="card-body">
          <h5 class="card-title"><a class="text-info" href="#">{{ product.product_name }}</a></h5>
          <h5>{{ product.price }}</h5>
        </div>
        <div class="card-footer">
          <button class="btn btn-primary" @click="$parent.$refs.cart.add(product)"><i class="fa fa-plus"></i>&nbsp;Добавить</button>
        </div>
      </div>
    </div>
  </div>
</div>
`
};

export default product;
