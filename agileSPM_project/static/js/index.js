
// Login modal specific Jquery
// $(document).ready(function(){
//     alert("works");
//     $("#user-signup").click(function(){
      
//         $(".modal-signup").show();
//     });
// });

// Show hamburger icon when icon small enough to be used on mobile.
$(document).ready(function(){
    $(".nav-icon").on("click", function(){
        $("nav ul").toggleClass("show");
    });
});

