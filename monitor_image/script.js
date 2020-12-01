var page = 0;

function load() {
    if (page === 0) {
        for (var i = 0; i < 20; i++) {
            document.getElementById(i.toString()).src = "images/image_" + i;
        }
    }
    if (page < 1) {
        var x = document.getElementById("back");
        x.style.visibility = "hidden";
    }
    document.getElementById("back").addEventListener("click", function() {
        page += 1;
        for (var i = 20 * page; i < 20 * page; i++) {
            var j = i - 20 * page;
            document.getElementById(j.toString()).src = "images/image_" + i;
        }
    });
    document.getElementById("next").addEventListener("click", function() {
        page -= 1;
        for (var i = 20 * page; i < 20 * page; i++) {
            var j = i - 20 * page;
            document.getElementById(j.toString()).src = "images/image_" + i;
        }
    });


}