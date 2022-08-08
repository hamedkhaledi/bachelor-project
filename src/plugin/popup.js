// for (let elem of document.getElementsByClassName("chip")) {
//     elem.innerHTML = "hi";
//     elem.addEventListener("onClick", changeStyle);
// }

var textNer = undefined;
var textPos = undefined;
window.onload = function () {
    chrome.storage.local.get(['textPOS'], function (item) {
        globalThis.textPos = item.textPOS;
        chrome.storage.local.get(['text'], function (item) {
            globalThis.textNer = item.text;
            let elements = document.getElementsByClassName("chip");
            for (let i = 0; i < elements.length; i++) {
                elements[i].addEventListener("click", changeStyle);
            }
            let checkBox = document.getElementById("selection");
            checkBox.addEventListener("click", changeSelection);
            checkBox.checked = true;
            outHtml();
        });
    });
}

function changeStyle(event) {
    let className = event.target.classList[1]
    let elements = document.getElementsByClassName(className);
    [...elements].forEach(function (part, index) {
            part.classList.toggle(className.split("_")[0]);
            part.classList.toggle(className.split("_")[0] + "_W");
        }, elements
    ); // use arr as this
}

function changeSelection(event) {
    const checkBox = document.getElementById("selection");
    const nerButtons = document.getElementById("nerButtons");
    const posButtons = document.getElementById("posButtons");
    const textBox = document.getElementById("text");
    checkBox.disabled = true;
    if (checkBox.checked === true) {
        textBox.classList.add('visuallyhidden');
        posButtons.classList.add('visuallyhidden');
        setTimeout(function () {
            posButtons.classList.add('hidden');
            nerButtons.classList.remove('hidden');
            globalThis.textPos = document.getElementById("text").innerHTML;
            outHtml();
            checkBox.disabled = false;
            nerButtons.classList.remove('visuallyhidden');
            textBox.classList.remove('visuallyhidden');
        }, 1000);
    } else {
        textBox.classList.add('visuallyhidden');
        nerButtons.classList.add('visuallyhidden');
        setTimeout(function () {
            nerButtons.classList.add('hidden');
            posButtons.classList.remove('hidden');
            globalThis.textNer = document.getElementById("text").innerHTML;
            outHtml();
            checkBox.disabled = false;
            posButtons.classList.remove('visuallyhidden');
            textBox.classList.remove('visuallyhidden');
        }, 1000);
    }
}

function outHtml() {
    let checkBox = document.getElementById("selection");
    if (checkBox.checked === true) {
        if (globalThis.textNer === "loading") {
            document.getElementById("text").innerHTML = "<div class=\"lds-roller\"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>"
        } else if (globalThis.textNer === "Error") {
            document.getElementById("text").innerHTML = "<div class=\"Error\">Oops!</div>"
        } else if (typeof globalThis.textNer !== 'undefined') {
            document.getElementById("text").innerHTML = textNer;
        }
    } else {
        if (globalThis.textPos === "loading") {
            document.getElementById("text").innerHTML = "<div class=\"lds-roller\"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>"
        } else if (globalThis.textPos === "Error") {
            document.getElementById("text").innerHTML = "<div class=\"Error\">Oops!</div>"
        } else if (typeof globalThis.textPos !== 'undefined') {
            document.getElementById("text").innerHTML = textPos;
        }
    }
}

chrome.storage.onChanged.addListener(function (changes, namespace) {
    for (let [key, {oldValue, newValue}] of Object.entries(changes)) {
        if ((key === "text" && oldValue !== newValue)) {
            globalThis.textNer = newValue;
            outHtml();
        }
        if ((key === "textPOS" && oldValue !== newValue)) {
            globalThis.textPos = newValue;
            outHtml();
        }
    }
});