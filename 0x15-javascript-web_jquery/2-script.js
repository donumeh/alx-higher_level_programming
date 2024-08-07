// Get the red header text
const redHeaderText = $('DIV#red_header');

function changeHeaderColor () {
  const header = $('header');

  header.css('color', '#FF0000');
}

redHeaderText.on('click', changeHeaderColor);
