// Get the language code and output greeting

window.onload = function () {
  const button = $('INPUT#btn_translate');
  const input = $('INPUT#language_code');

  function printLanguage () {
    const value = input.val();

    if (value) {
      const uri = 'https://hellosalut.stefanbohacek.dev/?lang=' + value;

      $.ajax({
        url: uri,
        success: function (result) {
          const helloTranslation = $('DIV#hello');

          helloTranslation.text(result.hello);
        }
      });
    }
  }

  button.on('click', printLanguage);
  input.on('keypress', function (event) {
    if (event.key === 'Enter') {
      printLanguage();
    }
  });
};
