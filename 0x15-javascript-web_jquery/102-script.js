const $ = window.$;

document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').on('click', function () {
    const value = $('#language_code').val();
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + value, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
