var myBtn = document.querySelectorAll("button")
    remo = document.querySelector(".t");

for (let i = 0; i < 100; i++) {
    myBtn[i].innerHTML = "Waiting";

    myBtn[i].onclick = function () {
    switch (myBtn[i].innerHTML) {
        case "Waiting":
            myBtn[i].innerHTML = "In progress"
            myBtn[i].classList.add("btn-success")
            myBtn[i].classList.remove("btn-warning")
            break;
        case "In progress":
            myBtn[i].innerHTML = "In Oven"
            myBtn[i].classList.add("btn-danger")
            myBtn[i].classList.remove("btn-success")
            break;
        case "In Oven":
            myBtn[i].innerHTML = "Done"
            myBtn[i].classList.add("btn-secondary")
            myBtn[i].classList.remove("btn-danger")
            myBtn.setAttribute("style", "cursor:default;");
            /*remo.setAttribute("style", "display:none;"); */
            break;
        default:
            myBtn.innerHTML == "waiting"
    }
};

}
