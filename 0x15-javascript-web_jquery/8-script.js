const $ = window.$;

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (idx, element) {
    $('#list_movies').append('<li>' + element.title + '</li>');
  });
});
