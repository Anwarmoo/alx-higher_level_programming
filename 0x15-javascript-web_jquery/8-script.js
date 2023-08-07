$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (titles) {
  for (const i of titles.results) {
    $('UL#list_movies').append('<li>' + i.title + '</li>');
  }
});
