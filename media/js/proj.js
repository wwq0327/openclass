jQuery(document).ready(function($) {
    $('form.comment').submit(function() {
        var comment = $('#id_comment').val();
        if (!comment || comment.length) {
            alert("暂时还不能贴任何内容");
            return false;
        }
    });
});