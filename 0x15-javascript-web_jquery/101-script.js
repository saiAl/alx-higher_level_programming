const $ = window.$;

document.addEventListener('DOMContentLoaded', function () {
  // add new item to a list
  $('#add_item').on('click', function () {
    $('.my_list').append('<li>item</li>');
  });

  // remove item from a list
  $('#remove_item').on('click', function () {
    $('.my_list li').eq(-1).remove();
  });

  // clear all list item
  $('#clear_list').on('click', function () {
    $('.my_list li').remove();
  });
});
