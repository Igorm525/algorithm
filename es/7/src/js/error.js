import product from "./product";

const error = {
  data: function () {
    return {
      messages: [],
    }
  },
  template: `
<div class="container">
  <div class="row" v-for="message in messages">
    <div class="alert alert-primary alert-dismissible fade show" role="alert">{{ message }}<button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button></div>
  </div>
</div>
`
};

export default error;