$(document).ready(function(){
    function getlist() {
        var list = $('li');
        var i = 0;
        list.first().addClass('selected');
    }
    var list = $('li');
    var i = 0;
    list.first().addClass('selected');
    $(document).keyup(function(e){
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
            $('#data').val(data);
            $('#attacked').submit(function() {
                $.ajax({
                    url: "/battle/attacked",
                    method: 'POST',
                    data: $(this).serialize(),

                }).done(function(e) {
                    $('.actionbar').html(e)
                    getlist()
                })
            });
            $('#ability').submit()
        }
    })
});