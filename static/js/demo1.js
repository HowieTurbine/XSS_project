$(document).ready(function () {
    $("#but").click(function () {
        data = $('#comment').val();
        console.log(data);
        $('#result').append(data);

    })
});
