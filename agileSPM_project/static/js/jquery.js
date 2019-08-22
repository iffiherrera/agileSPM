
// Sign up modal specific Jquery & JavaScript 
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

// Login 
$(document).ready(function(){
    $("#user-login").click(function(){
      
        $(".modal-login").show();
    });
});

$(document).ready(function(){
    $(".close").click(function(){ 
    $(".modal-login").hide();
    });
});
