let canvas = null;

function init() {
    canvas = document.getElementById("canvas");
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;

    logic = new GameLogic(canvas.width, canvas.height);

    requestAnimationFrame(drawFrame);
}

class Player {
    constructor(x, y, radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.width = radius * 2;
        this.height = radius * 2;
        this.velX = 1;
        this.velY = 1;
        
        // Load the image
        this.image = new Image();
        this.image.src = "img/dvd.png";
    }

    move() {
        this.x += this.velX;
        this.y += this.velY;
    }

    render(canvas) {
        let ctx = canvas.getContext('2d');
        ctx.drawImage(this.image, this.x, this.y, this.height, this.width);
    }
}

class GameLogic {
    constructor(width, height) {
        this.player = new Player(25, 25, 50);
    }

    gameTick() {
        this.player.move();

        // Keep player inside bounds
        if (this.player.y + this.player.height > canvas.height || this.player.y < 0) {
            this.player.velY = -this.player.velY;
        }
        if (this.player.x + this.player.width > canvas.width || this.player.x < 0) {
            this.player.velX = -this.player.velX;
        }
    }

    get mobs() {
        return [this.player];
    }
}

function drawFrame() {
    let ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    logic.gameTick();

    let mobs = logic.mobs;
    for (let mob of mobs) {
        mob.render(canvas);
    }

    requestAnimationFrame(drawFrame);
}

window.onload = init;

document.querySelector("canvas").onclick = function () {  
    history.back();
}