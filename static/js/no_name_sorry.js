var command_history = [];
var i = command_history.length;

$(document).click(()=> {
    $("input:text").focus();
});

$(document).keydown(function (e) {
    var key = e.which;
    if(key == 13)  // the enter key code
    {
        let command = $("input").last().val();
        
        if (command != ""){
            command_history.push(command);
        }

        i = command_history.length;

        $.ajax({
            url: "/terminal",
            type: "get",
            data: { "command" : command, "history" : JSON.stringify(command_history) },
            success: (response) => {
                $("input").attr("disabled", "disabled");
                $(".terminal-content").append(response);
                $("input").focus(); 
            },
            error: (e) => {                       
                if(e.status == 302){
                    $(".terminal-content *").remove();
                    $(".terminal-content").append(e.responseText);
                    $("input").focus(); 
                }
            }
        });
    }
    else if(key == 38)  // the up key code
    {
        e.preventDefault();

        i = i > 0 ? i - 1 : -1;

        let command = i == -1 ? "" : command_history[i];
        
        $("input").last().val(command);
    }
    else if(key == 40)  // the down key code
    {
        e.preventDefault();

        i = i == command_history.length ? command_history.length : i + 1;
        
        let command = i == command_history.length ? "" : command_history[i];

        $("input").last().val(command);
    }
 });