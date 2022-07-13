// for (let elem of document.getElementsByClassName("chip")) {
//     elem.innerHTML = "hi";
//     elem.addEventListener("onClick", changeStyle);
// }
window.onload = function () {
    let elements = document.getElementsByClassName("chip");
    for (let i = 0; i < elements.length; i++) {
        elements[i].addEventListener("click", changeStyle);
    }
}
const colors = {
    "PER": "#aadb51",
    "ORG": "#ffe05d",
    "LOC": "lightpink",
    "DAT": "lightblue",
    "TIM": "crimson",
    "PCT": "lightsalmon",
    "MON": "mediumpurple",

}

function changeStyle(event) {
    let className = event.target.className.split(" ")[0]
    let elements = document.getElementsByClassName(className);
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].style.backgroundColor === "rgba(0, 0, 0, 0)") {
            elements[i].style.backgroundColor = colors[className];
        } else {
            elements[i].style.backgroundColor = "rgb(0,0,0,0)";
        }
    }
}

function outHtml(text) {
    if (text === "loading") {
        document.getElementById("text").innerHTML = "<div class=\"lds-roller\"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>"
    } else if (text === "Error") {
        document.getElementById("text").innerHTML = "<div class=\"Error\">Oops!</div>"
    } else if (typeof text !== 'undefined') {
        document.getElementById("text").innerHTML = text
    }

}

chrome.storage.sync.get(['text'], function (item) {
    outHtml(item.text);
});
chrome.storage.onChanged.addListener(function (changes, namespace) {
    for (let [key, {oldValue, newValue}] of Object.entries(changes)) {
        if (key === "text" && oldValue !== newValue) {
            outHtml(newValue);
        }
    }
});