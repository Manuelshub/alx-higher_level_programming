$(document).on('keypress', function (e) {
  if (e.which === 13) {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  }
});
