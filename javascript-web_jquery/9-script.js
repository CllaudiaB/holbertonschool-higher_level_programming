$.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    $("DIV#hello").append(data.hello);
});