$(document).ready(function() {
  $("#moveleft").click(function() {
    $.ajax({
            url:  '/remote/left',
            type: 'GET',
            data: { command:'left' }
    });
  });
  
  $("#moveright").click(function() {
    $.ajax({
            url:  '/remote/right',
            type: 'GET',
            data: { command:'right' }
    });
  });

  $("#moveback").click(function() {
    var isRunning = $("#start").is(":checked") ? 1:0;
    $.ajax({
            url:  '/remote/back',
            type: 'GET',
            data: { command:'right' }
    });
  });

  $("#play").click(function() {
    var cmd ='start';
    $.ajax({
            url:  '/remote/play',
            type: 'GET',
            data: { command:cmd }
    });
  });
  
  $("#pause").click(function() {
    var cmd ='stop'; 
    $.ajax({
            url:  '/remote/pause',
            type: 'GET',
            data: { command:cmd }
    });
  });
});
