document.getElementById("back_button").onclick = function () {  
    history.back();
}

document.getElementById("button_environment").onclick = function () {  
    eel.app_environment()(function(text) {                      
        document.getElementById("text_output").innerHTML = text;
    })
}

document.getElementById("button_position").onclick = function () {  
    eel.app_position()(function(text) {                      
        document.getElementById("text_output").innerHTML = text;
    })
}

document.getElementById("button_light").onclick = function () {  
    eel.app_light_sensor()(function(text) {                      
        document.getElementById("text_output").innerHTML = text;
    })
}

document.getElementById("button_joystick_position").onclick = function () {  
    eel.app_joystick_pos()(function(text) {                      
        document.getElementById("text_output").innerHTML = text;
    })
}