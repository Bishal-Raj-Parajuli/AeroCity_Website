jQuery(document).ready(function () {

  jQuery(".hero-slider").slick({
    autoplay: true,
    lazyLoad: "ondemand",
    autoplaySpeed: 3000,
    arrows: false,
    fade: true,
    dots: true,
  });


  // for hotel beauty-slider

  $('.single-main-thumb').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.pager-thumbnail'
  });
  $('.pager-thumbnail').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.single-main-thumb',
    dots: false,
    centerMode: false,
    focusOnSelect: true
  });

  jQuery('.gallery-slider').slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: false,
    lazyLoad: "ondemand",
    autoplaySpeed: 3000,
    arrows: true,
    dots: false,
    responsive: [{
        breakpoint: 1150,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 850,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 650,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });




    // Implement go to top.
    var $scroll_obj = jQuery("#btn-scrollup");
    jQuery(window).on("scroll", function () {
        if (jQuery(this).scrollTop() > 100) {
            $scroll_obj.fadeIn();
        } else {
            $scroll_obj.fadeOut();
        }
    });

    $scroll_obj.on("click", function () {
        jQuery("html, body").animate({
                scrollTop: 0,
            },
            600
        );
        return false;
    });



  jQuery(".mobile-menu-icon span").on("click", function () {
    jQuery(".body-overlay").fadeIn();
  });
  jQuery(".body-overlay, .close-menu ").on("click", function () {
    jQuery(".body-overlay").fadeOut();
  });
  jQuery(".mobile-menu-icon span").on("click", function () {
    jQuery(".mobile-navigation").addClass("active");
  });
  jQuery(".body-overlay, .close-menu ").on("click", function () {
    jQuery(".mobile-navigation").removeClass("active");
  });

});