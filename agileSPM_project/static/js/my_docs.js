/**
 * Scrum buttons 
 */

// Edit button
$(document).ready(function(){
    $("#edit-btn").click(function(){ 
        var url = $("#edit-btn").attr("data-link");
        window.location = url;
    });
});
// Delete button
$(document).ready(function(){
    $("#delete-btn").click(function(){ 
        var url = $("#delete-btn").attr("data-link");
        window.location = url;
    });
});
// Duplicate button
$(document).ready(function(){
    $("#duplicate-btn").click(function(){ 
        var url = $("#duplicate-btn").attr("data-link");
        window.location = url;
    });
});
//Save button 
$(document).ready(function(){
    $("#save-btn").click(function(){ 
        var url = $("#save-btn").attr("data-link");
        window.location = url;
    });
});

/**
 * Kanban buttons
 */

// Edit button
$(document).ready(function(){
    $("#edit-btn-kanban").click(function(){ 
        var url = $("#edit-btn-kanban").attr("data-link");
        window.location = url;
    });
});
// Delete button
$(document).ready(function(){
    $("#delete-btn-kanban").click(function(){ 
        var url = $("#delete-btn-kanban").attr("data-link");
        window.location = url;
    });
});
// Duplicate button
$(document).ready(function(){
    $("#duplicate-btn-kanban").click(function(){ 
        var url = $("#duplicate-btn-kanban").attr("data-link");
        window.location = url;
    });
});
//Save button 
$(document).ready(function(){
    $("#save-btn-kanban").click(function(){ 
        var url = $("#save-btn-kanban").attr("data-link");
        window.location = url;
    });
});

 /**
 * Scrumban buttons
 */
// Edit button
$(document).ready(function(){
    $("#edit-btn-sb").click(function(){ 
        var url = $("#edit-btn-sb").attr("data-link");
        window.location = url;
    });
});
// Delete button
$(document).ready(function(){
    $("#delete-btn-sb").click(function(){ 
        var url = $("#delete-btn-sb").attr("data-link");
        window.location = url;
    });
});
// Duplicate button
$(document).ready(function(){
    $("#duplicate-btn-sb").click(function(){ 
        var url = $("#duplicate-btn-sb").attr("data-link");
        window.location = url;
    });
});
//Save button 
$(document).ready(function(){
    $("#save-btn-sb").click(function(){ 
        var url = $("#save-btn-sb").attr("data-link");
        window.location = url;
    });
});

/** Done page buttons */