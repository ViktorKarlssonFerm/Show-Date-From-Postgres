
$(document).ready(function() {
    $("#comment-section").api({
        action: 'get comments',
        method: 'POST',
        processData: false,
        contentType: false,
        on: 'now',
        successTest: function(response) {
            return response.success || false;
        },
        onSuccess: function(response) {
            comments = "";
            for (var i = 0; i < response.values.length; i++) {
                date = new Date(response.values[i].created_at);

                alert(date);
                comment = '<div class="comment">';
                comment += '<div class="content">';
                comment += '<a class="author">' + response.values[i].user_name + '</a>';
                comment += '<div class="metadata"><span class="date">' + date + '</span></div>';
                comment += '<div class="text">' + response.values[i].content + '</div>';
                comment += '</div></div>';
                comments += comment;
            }

            $("#comment-section").html(comments);
        },
        onFailure: function(response) {
            alert("Allt gick åta helvete!");
        }
    })
});

$("#create-comment").on("click", function() {
    if ($(".new-comment") != "") {
        $("#comment-form").api({
            action: 'create comment',
            method: 'POST',
            processData: false,
            contentType: false,
            beforeSend: function(settings) {
                settings.data = new FormData(($("#comment-form form").get(0)));
                return settings;
            },
            successTest: function(response) {
                return response.success || false;
            },
            onSuccess: function(response) {
                $(".ui.success.message").removeClass("hidden");
            },
            onFailure: function(response) {
                $(".ui.warning.message").removeClass("hidden");
            }
        })
    }
});
