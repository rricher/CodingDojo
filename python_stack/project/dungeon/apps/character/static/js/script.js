$(document).ready(function(){
    console.log($('li'))
    var list = $('li')
    var i = 0
    list.first().addClass('selected')
    $(document).keyup(function(e){
        console.log(e.keyCode)
        if (e.keyCode == 40) {
            if (i < list.length -1) {
                list.eq(i).removeClass('selected');
                i ++;
                list.eq(i).addClass('selected');
            }
        }
        if (e.keyCode == 38) {
            if (i > 0) {
                list.eq(i).removeClass('selected');
                i --;
                list.eq(i).addClass('selected');
            }
        }
        if (e.keyCode == 13) {
            list.eq(i).removeClass('selected');
            data = list.eq(i).attr('class');
            console.log(data)
            $('#data').val(data);
                console.log('made it to the submit', $('form').serialize())
                $.ajax({
                    url: '/character/select/',
                    method: "post",
                    data: $('form').serialize(),
                    success: function(serverResponse) {
                        console.log('recieved this from the server', serverResponse)
                    }
            });
        }
    })
});