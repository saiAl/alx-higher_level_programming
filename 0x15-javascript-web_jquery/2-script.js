const $ = window.$;

const target = $('#red_header');
const header = $('header');

target.on('click', function () {
  header.css('color', '#FF0000');
});
