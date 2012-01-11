jQuery(document).ready(function($) {
    $('form.comment').submit(function() {
        var comment = $('#id_comment').val();
        if (!comment || comment.length < 4) {
            alert("评论内容不能为空或字数太少！");
            return false;
        }
    });
});