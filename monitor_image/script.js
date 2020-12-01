counted = 0;

function load() {
    for (var i = 20 * counted; i < 20 * counted + 20; i++) {
        document.getElementById((i - 20 * counted).toString()).src = "images/image_" + i;
    }
}

function upward() {
    counted += 1;
    for (var i = 20 * counted; i < 20 * counted + 20; i++) {
        document.getElementsByClassName("gallery-inner").innerHTML = " <div class='gallery-item'> <img id='" + i + "' src=' '></div>"
    }
    load();
}

function backward() {
    counted -= 1;
    if (counted < 0)
        counted += 1;
    for (var i = 20 * counted; i < 20 * counted + 20; i++) {
        document.getElementsByClassName("gallery-inner").innerHTML = " <div class='gallery-item'> <img id='" + i + "' src=' '></div>"
    }
    load();
}