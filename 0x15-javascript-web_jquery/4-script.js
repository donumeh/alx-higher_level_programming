// Get the element to click on
const elementToClick = $('DIV#toggle_header');

function changeColor () {
  const header = $('header');

  header.toggleClass('red', !header.hasClass('red'));
  header.toggleClass('green', !header.hasClass('green'));
}

elementToClick.on('click', changeColor);
