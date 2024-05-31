const $ = window.$;

$('#toggle_header').on('click', function () {
  const cls = $('header').attr('class');

  if (cls === 'green') {
    $('header').removeClass('green');
    $('header').addClass('red');
  }

  if (cls === 'red') {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
