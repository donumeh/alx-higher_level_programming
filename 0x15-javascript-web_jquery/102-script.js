// Get the language code and output greeting

window.onload = function () {
  const button = $('INPUT#btn_translate');

  function printLanguage () {
    const value = $('INPUT#language_code').val();

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
};
