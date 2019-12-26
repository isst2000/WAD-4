function loadRating(id) {
    $.ajax({
        dataType: 'json',
        data: {
            'id': id,
        },
        method: 'POST',
    }).done(function (data) {
        $("span[id="' + data.id + '"].text( data.likes );
    });
}