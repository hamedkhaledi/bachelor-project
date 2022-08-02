// for (let elem of document.getElementsByClassName("chip")) {
//     elem.innerHTML = "hi";
//     elem.addEventListener("onClick", changeStyle);
// }
window.onload = function () {
    let elements = document.getElementsByClassName("chip");
    for (let i = 0; i < elements.length; i++) {
        elements[i].addEventListener("click", changeStyle);
    }

    var checkBox = document.getElementById("selection");
    checkBox.addEventListener("click", changeSelection);
    checkBox.checked = "true";
}
const colors = {
    "PER": "#aadb51",
    "ADJ": "#aadb51",
    "ORG": "#ffe05d",
    "V": "#ffe05d",
    "LOC": "lightpink",
    "N": "lightpink",
    "DAT": "lightblue",
    "P": "lightblue",
    "TIM": "crimson",
    "DELM": "crimson",
    "PCT": "lightsalmon",
    "ADV": "lightsalmon",
    "MON": "mediumpurple",
    "CON": "mediumpurple",

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

function changeSelection(event) {
    var checkBox = document.getElementById("selection");
    var textSpan = document.getElementById("statusText");
    var nerButtons = document.getElementById("nerButtons");
    var posButtons = document.getElementById("posButtons");
    if (checkBox.checked === true) {
        textSpan.style.color = "limeGreen";
        textSpan.innerHTML = "NER";
        posButtons.classList.add('visuallyhidden');
        posButtons.classList.add('hidden');
        nerButtons.classList.remove('hidden');
        setTimeout(function () {
            nerButtons.classList.remove('visuallyhidden');
        }, 20);


    } else {
        textSpan.style.color = "darkRed";
        textSpan.innerHTML = "POS";
        posButtons.classList.remove('hidden');
        nerButtons.classList.add('visuallyhidden');
        nerButtons.classList.add('hidden');
        setTimeout(function () {
            posButtons.classList.remove('visuallyhidden');
        }, 20);
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