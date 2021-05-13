/* Made by Facundo Diaz for Holberton School 2021 */
$(function () {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    $.get(url, function (data, textStatus) {
      $('#character').text(data.name);
    });
  });
