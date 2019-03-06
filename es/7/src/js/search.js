import error from "./error";

const search = {
  data() {
    return {
      query: ''
    }
  },
  template: `
<div class="container">
    <form class="mb-5 form-inline" @submit.prevent="$parent.$refs.products.filter(query)" >
        <i class="fas fa-search" aria-hidden="true"></i>
        <input class="form-control form-control-sm ml-3 w-75" v-model="query" type="text" placeholder="Search" aria-label="Search">
    </form>
</div>
  `
};

export default search;