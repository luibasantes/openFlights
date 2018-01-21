function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(window).load(function() {

    var csrftoken = getCookie('csrftoken');

    $("form").on("submit", function( event ) {
      event.preventDefault();
      formArray = $("form").serializeArray();
      var returnArray = {};
      for (var i = 0; i < formArray.length; i++){
        returnArray[formArray[i]['name']] = formArray[i]['value'];
      }

      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
       });

      $.ajax({
        type: 'POST',
        url: '/api/crear_deseo/',
        csrfmiddlewaretoken: '{% csrf_token %}',
        dataType: 'JSON',
        contentType:'application/json',
        data: JSON.stringify(returnArray),
        success: function(){
          alert("Sus datos han sido guardados!")
          console.log("Sus datos han sido enviados!")},
        error: function(error){
          alert("Algo salió mal!");
          console.log(error)},
      });
    });
});