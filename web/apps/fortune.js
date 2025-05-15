document.getElementById("fortune_button").onclick = function () {  
    eel.app_fortune_request()(function(text) {                      
        document.querySelector(".fortune_text").innerHTML = text;
    })
}

document.getElementById("back_button").onclick = function () {  
    history.back();
}