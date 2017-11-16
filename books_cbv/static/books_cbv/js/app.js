/*
 * Validate the form to login
 */

var urlStartLogin;

function validateForm() { 
  if(urlStartLogin === 'admin') {
    var btn = document.getElementById("btnAdmin");
    btn.click();
    return false;
  }

  if (urlStartLogin === 'cliente') {
    var btn = document.getElementById("btnCliente");
    btn.click();
    return false;
  }

  return false;
}

/* Animales */
var moduleAnimalView = new Vue({
  el: '#animalList',
  data: {
    animals: []
  },
  methods: {
    mounted: function() {
      debugger
      axios.get(`/books_cbv/test`)
      .then(response => {
        debugger
        this.animals = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  }
})
