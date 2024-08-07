window.onload = function () {
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');
  const ulList = $('UL.my_list');

  function addNewList () {
    $('<li></li>').text('Item').appendTo(ulList);
  }

  function removeListItem () {
    $('UL.my_list li:last-child').remove();
  }

  function clearAllItems () {
    ulList.empty();
  }

  addItem.on('click', addNewList);
  removeItem.on('click', removeListItem);
  clearList.on('click', clearAllItems);
};
