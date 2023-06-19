//my query
$(document).ready(function () {
    $(".allice").mouseover(function(){
      $(".allice").css({"letter-spacing":"4px","transition":"letter-spacing 1.3s"});
    });
    $(".allice").mouseout(function(){
        $(".allice").css({"letter-spacing":"2px","transition":"letter-spacing 1.3s"});
    });

    // $(".login").mouseover(function(){
    //   $(".logo").css({"color":"#AB7B60","transform":"rotate(360deg)","transition":"transform 0.8s"});
    // });
    // $(".login").mouseout(function(){
    //   $(".logo").css({"color":"#102a42","transform-origin":"19px ","transform":"rotate(-0deg)","transition":"transform 1.3s"});
    // });
});



(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy on scroll event listener 
   */
    const onscroll = (el, listener) => {
      el.addEventListener('scroll', listener)
    }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('.top-bar')
  let selectNav = select('.navigation')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 50) {
        selectHeader.classList.add('hide')
        selectNav.classList.add('nav-up')
        
      }
      else{
        selectHeader.classList.remove('hide')
        selectNav.classList.remove('nav-up')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
 let backtotop = select('.back-to-top')
 if (backtotop) {
   const toggleBacktotop = () => {
     if (window.scrollY > 100) {
       backtotop.classList.add('active')
     } else {
       backtotop.classList.remove('active')
     }
   }
   window.addEventListener('load', toggleBacktotop)
   onscroll(document, toggleBacktotop)
 }
})()

// font
WebFont.load({
  google: {"families":["Poppins:300,400,500,600,700","Roboto:300,400,500,600,700"]},
  active: function() {
      sessionStorage.fonts = true;
  }
});