$.getJSON( "https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    $.each(data.results, function(key, val) {
       $("UL#list_movies").append("<li>" + val.title + "</li>");
    })
});