
$(document).ready(function(){
    footerPush();
});

function footerPush(){
    if($('footer').offset().top + $('footer').outerHeight() < $(window).height()){
        // 80 = 80px for the default footer.margin-top
        $('footer').css('margin-top', 80+$(window).height()-($('footer').offset().top+$('footer').outerHeight()));
    }
}