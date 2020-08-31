document.getElementsByClassName("hover").addEventListener("mouseover", changeColor());

function changeColor(hover) {
    if (hover.style.color == 'black') {
        hover.style.color = 'orange';
    }else {
        hover.style.color = 'orange';
    }

}