$(document).ready(function () {
    if ($("#evidenziaelemento").length != 0) {
        $('html, body').animate({
            scrollTop: $("#evidenziaelemento").offset().top
        }, 2000);
    }
});