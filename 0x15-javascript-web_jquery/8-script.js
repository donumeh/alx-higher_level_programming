$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (result) {
    result.results.forEach(function (item) {
      $('UL#list_movies').append($('<li></li>').text(item.title));
    });
  }
});
