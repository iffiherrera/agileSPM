
/********* NAVIGATION BAR  ************/

// Logo home button
$("#logo-btn").on('click', function(){
    var url = $("#logo-btn").attr("href");
     window.location = url;
});
// Login button
$("#user-login").on('click', function(){
    var url = $("#user-login").attr("data-link");
     window.location = url;
});
// Logout button
$("#user-logout").on('click', function(){
    var url = $("#user-logout").attr("href");
     window.location = url;
});
// Sign up button
$("#user-signup").on('click', function(){
    var url = $("#user-signup").attr("data-link");
     window.location = url;
});
// Scrum button 
$(".scrum-btn").on('click', function(){
    var url = $("scrum-btn").attr("data-link");
     window.location = url;
});
// Kanban button
$(".logo-btn").on('click', function(){
    var url = $("li.home-btn").attr("data-link");
     window.location = url;
});
// Scrumban button
$(".logo-btn").on('click', function(){
    var url = $("li.home-btn").attr("data-link");
     window.location = url;
});

// Show hamburger icon when icon small enough to be used on mobile.
$(document).ready(function(){
    $(".nav-icon").on("click", function(){
        $("nav ul").toggleClass("show");
    });
});

/********* MODAL  ************/

// Sign up modal 
$(document).ready(function(){
    $("#user-signup").click(function(){
      
        $(".modal-signup").show();
    });
});

$(document).ready(function(){
    $(".close").click(function(){ 
    $(".modal-signup").hide();
    });
});

// Login modal 
$(document).ready(function(){
    $("#user-login").click(function(){
      
        $(".modal-content").show();
    });
});

$(document).ready(function(){
    $(".close").click(function(){ 
    $(".modal").hide();
    });
});

// Sign up button from Modal 
$(function () {
    
    $(".signup-btn").modalForm({formURL: "{% url 'signup' %}"});

  });

/** Get started button */
