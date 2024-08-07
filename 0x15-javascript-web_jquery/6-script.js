// Updates the text of the <header> to `New Header!!!`

function updateText () {
  $('header').text('New Header!!!');
}

const elementToClick = $('DIV#update_header');

elementToClick.on('click', updateText);
