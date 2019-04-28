$(document).ready(function () {
    $("#but").click(function () {
         $('#result').empty();
        data = $('#comment').val();
        console.log(data);
        $('#result').append(data);

    })
});
