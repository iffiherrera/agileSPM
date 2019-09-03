
/** SCRUM BUTTONS */

// Download button 
$(document).ready(function(){
    $(".download-btn").click(function(){ 
        var url = $(".download-btn").attr("data-link");
        window.location = url;
    });
});

// Document button 
$(document).ready(function(){
    $(".doc-btn").click(function(){ 
        var url = $(".doc-btn").attr("data-link");
        window.location = url;
    });
});

/** KANBAN BUTTONS */

// Download button 
$(document).ready(function(){
    $(".download-kanban-btn").click(function(){ 
        var url = $(".download-kanban-btn").attr("data-link");
        window.location = url;
    });
});

// Document button 
$(document).ready(function(){
    $(".doc-kanban-btn").click(function(){ 
        var url = $(".doc-kanban-btn").attr("data-link");
        window.location = url;
    });
});


/** SCRUMBAN BUTTONS */

// Download button 
$(document).ready(function(){
    $(".download-scrumban-btn").click(function(){ 
        var url = $(".download-scrumban-btn").attr("data-link");
        window.location = url;
    });
});

// Document button 
$(document).ready(function(){
    $(".doc-scrumban-btn").click(function(){ 
        var url = $(".doc-scrumban-btn").attr("data-link");
        window.location = url;
    });
});