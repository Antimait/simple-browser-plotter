document.addEventListener('DOMContentLoaded', () => { reload(); });
setInterval(function() { reload(); }, 6000);

function reload() {
    let req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if(this.readyState === 4 && this.status === 200) {
            let plots = JSON.parse(req.responseText).plots;
            document.body.innerHTML = "";
            plots.forEach(function(plot) {
                let img = document.createElement("img");
                img.src = "/static/plots/"+plot+"?"+ new Date().getTime();
                document.body.appendChild(img);
                document.body.appendChild(document.createElement("br"));
            });
        }
    }
    req.open("GET", "/plots", true);
    req.send();
}