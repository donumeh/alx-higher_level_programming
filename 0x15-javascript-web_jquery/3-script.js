// Click on header to change color
const headerToClick = $('DIV#red_header');

function changeElementColor () {
  const header = $('header');

  header.addClass('red');
}

headerToClick.on('click', changeElementColor);
