jQuery(document).ready(function($) {
    $('form.comment').submit(function() {
        var comment = $('#id_comment').val();
        if (!comment || comment.length < 4) {
            alert("评论内容不能为空或字数太少！");
            return false;
        }
    });
});

/*
jQuery.ajaxSetup({
    data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
});
*/

jQuery('html').ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

function join_s(id) {
    //var join = $(".prj_join");
    $.get('/project/prj_s/', {'id': id}, function() {
        //alert(join);
        jQuery('span.prj_join').html('projects/a.html');
    })
}

function un_join(id) {
    $.get('/project/prj_rm/', {'id': id});
}