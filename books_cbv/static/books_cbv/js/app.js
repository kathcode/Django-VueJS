
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

function getAnimals() {
  return axios.get('/books_cbv/test');
}
var dataAnimal = getAnimals().then(function(response) {
    console.log(response.data);
});

/* Animales */
