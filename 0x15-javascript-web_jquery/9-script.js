/* Made by Facundo Diaz for Holberton School 2021 */
$(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    $.get(url, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
