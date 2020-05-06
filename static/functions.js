
$("#create-comment").on("click", function() {
    if ($(".new-comment") != "") {
        $("#comment-form").api({
            action: 'create comment',
            method: 'POST',
            processData: false,
            contentType: false,
            beforeSend: function(settings) {
                settings.data = new FormData(($("comment-form").get(0)));
                return settings;
            },
            successTest: function(response) {
                return response.success || false;
            },
            onSuccess: function() {
                location.reload();
                $(".ui.success.message").removeClass("hidden");
            },
            onFailure: function() {
                $(".ui.warning.message").removeClass("hidden");
            }
        })
    }
});
