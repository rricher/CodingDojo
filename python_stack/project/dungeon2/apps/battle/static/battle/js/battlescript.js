$(document).ready(function () {
    var i = 0;
    document.getElementsByTagName("li")[i].classList.add("selected");
    $(document).on("keyup", function (e) {
        if (e.keyCode == 40) {
            if (i < $('li').length - 1) {
                // $('li').eq(i).removeClass('selected');
                document.getElementsByClassName("selected")[0].classList.remove("selected");
                i++;
                // $('li').eq(i).addClass('selected');
                document.getElementsByTagName("li")[i].classList.add("selected");
            }
        }
        if (e.keyCode == 38) {
            console.log(i)
            if (i > 0) {
                document.getElementsByClassName("selected")[0].classList.remove("selected");
                i--;
                document.getElementsByTagName("li")[i].classList.add("selected");
            }
        }
        if (e.keyCode == 13) {
            document.getElementsByClassName("selected")[0].classList.remove("selected");
            data = $('li').eq(i).attr('class');
            $('#data').val(data);
            if ($("#attacked").length) {
                $('#attacked').submit(function (e) {
                    e.preventDefault()
                    $.ajax({
                        url: "/battle/attacked/",
                        method: 'post',
                        data: $(this).serialize(),
                        success: function (e) {
                            $('.actionbar').html(e)
                            i = 0
                            document.getElementsByTagName("li")[i].classList.add("selected");
                        }
                    })
                })
                $('#attacked').submit()
            }
            if ($("#ability").length) {
                data2 = $("li").eq(i).attr('class');
                $('#data2').val(data2);
                $('#ability').submit()
            }
        }
    })
});