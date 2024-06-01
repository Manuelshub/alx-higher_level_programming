$(document).ready(function () {
  $('#toggle_header').click( function () {
    $('header').toggleClass('red green');
    // or
    // $('header').toggleClass('red').toggleClass('green');
  });
});
