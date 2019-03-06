import product from "./product";
import error from "./error";
import search from "./search";
import cart from "./cart";

const app = {
  el: '#app',
  components: {product, error, search, cart},
  methods: {
    fetch(url, func, method = 'get', obj = {}) {
      let body = method !== 'get' ? {body: JSON.stringify(obj)} : {};
      return fetch(url, {method: method.toUpperCase(), headers: {"Content-Type": "application/json"}, ...body})
        .then(result => result.json())
        .then(data => func(data))
        .catch(error => this.error.errors.messages.push(error.toString()));
    },
  },
};
