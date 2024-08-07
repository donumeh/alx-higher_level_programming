// Fetches data from api and updates page

$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: function (result) {
    $('DIV#hello').text(result.hello);
  }
});
