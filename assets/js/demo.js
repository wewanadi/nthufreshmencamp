$(function() {

  $('.password-holder .unlock').click(function(e) {     
    var errorMessage = $('.error-message');
    var passwordDiv = $(this).parent();
    var pwd = document.getElementById("password").value;
    var id = document.getElementById("id").value;
    var msg = document.getElementById("message");

    if(passwordDiv.children('input').val()) {
        if (pwd==="@1019873212333"&&id==="101987321"){
      var tl = new TimelineMax();
      tl.fromTo(passwordDiv, 0.3, {x:-1}, { x:1, ease:RoughEase.ease.config({ strength:8, points:40, template:Linear.easeNone, randomize:false }) , clearProps:"x" })
        .to($('body'), 0.15, { backgroundColor: 'green' })
        .to(errorMessage, 0.15, { autoAlpha: 1, y: -16 }, "-=0.15")
        // .to(passwordDiv, 0.15, { className: "+=false" }, "-=0.15")
        .to(passwordDiv, 0.15, { className: "-=false" }, "+=2.5")
        .to($('body'), 0.15, { backgroundColor: '#EDF0F9' }, "+=0.65")
        .to(errorMessage, 0.15, { autoAlpha: 0, y: 0 }, "-=0.15");
        msg.textContent = "Correct, Loading...";
        setTimeout(() => {          window.location.href = "https://sites.google.com/view/nthurationing-plan-101987321";}, 1500);

        }
        else{
          var tl = new TimelineMax();
          tl.fromTo(passwordDiv, 0.3, {x:-1}, { x:1, ease:RoughEase.ease.config({ strength:8, points:40, template:Linear.easeNone, randomize:false }) , clearProps:"x" })
            .to($('body'), 0.15, { backgroundColor: '#E74C3C' })
            .to(errorMessage, 0.15, { autoAlpha: 1, y: -16 }, "-=0.15")
            .to(passwordDiv, 0.15, { className: "+=false" }, "-=0.15")
            .to(passwordDiv, 0.15, { className: "-=false" }, "+=2.5")
            .to($('body'), 0.15, { backgroundColor: '#EDF0F9' }, "+=0.65")
            .to(errorMessage, 0.15, { autoAlpha: 0, y: 0 }, "-=0.15");
        }
    }
  })
});
