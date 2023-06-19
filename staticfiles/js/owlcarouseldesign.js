// owl carousel
$(".owl-carousel").owlCarousel({
  nav: false, // Show next and prev buttons
  responsive: {
    0: {
      items: 2,
    },
    700: {
      items: 3,
    },
    1000: {
      items: 5,
    },
  },
  margin: 20,
  smartSpeed: 15000,
  dotsSpeed: 1000,
  dots: true,
  nav: true,
  dragEndSpeed: 1000,
  singleItem: true,
  animateIn: "fadeIn",
  animateOut: "fadeOut",
  pagination: false,
  autoplay: true,
  autoplayTimeout: 6000,
  autoplayHoverPause: false,
  loop: true,
  afterAction: function (el) {
    //remove class active
    this.$owlItems.removeClass("active");

    //add class active
    this.$owlItems //owl internal $ object containing items
      .eq(this.currentItem + 1)
      .addClass("active");
  },
});
