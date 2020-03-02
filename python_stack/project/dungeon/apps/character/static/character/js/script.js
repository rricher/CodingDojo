$(document).ready(function(){
    console.log($('li'))
    var list = $('li')
    var i = 0
    list.first().addClass('selected')
    console.log('your in char')
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
            $('#data').val(data);
            $('#char').submit();
            $('#class').submit();
        }
    })
});