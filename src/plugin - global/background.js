const Title = "Pars NER2"
const menuItem = {
    "id": Title, "title": Title, "contexts": ["selection"]
};

chrome.contextMenus.create(menuItem);

function textToHtml(data, text) {
    let html_div = "";
    let last_index = 0;
    console.log(data)
    for (const elem of data) {
        let start_index = text.slice(last_index, text.length).indexOf(elem["word"]) + last_index
        console.log(elem["word"], start_index)
        if (last_index < start_index) {
            html_div += text.slice(last_index, start_index)
        }
        last_index = start_index + elem['word'].length;
        html_div += `<span class = \"NER ${elem['entity_group'].split("_")[0]}\">` + elem['word'] + "</span>";
    }
    html_div += text.slice(last_index, text.length);
    console.log(html_div);
    return html_div;
}

function requestNer(currentText, inputData, request) {
    fetch("https://api-inference.huggingface.co/models/hamedkhaledi/persain-flair-ner", request).then(res => {
        return res.json();
    }).then(data => {
        console.log("data : ", data);
        if (data["error"] !== undefined) {
            setTimeout(() => requestNer(currentText, inputData, request), 10000);
            return;
        }
        chrome.storage.local.set({'text': textToHtml(data, currentText)}, function () {
        });
    }).catch((error) => {
        chrome.storage.local.set({'text': "Error"}, function () {
        });
    });
}

function requestPos(currentText, inputData, request) {
    fetch("https://api-inference.huggingface.co/models/hamedkhaledi/persian-flair-pos", request).then(res => {
        return res.json();
    }).then(data => {
        console.log("data : ", data);
        if (data["error"] !== undefined) {
            setTimeout(() => requestPos(currentText, inputData, request), 10000);
            return;
        }
        chrome.storage.local.set({'textPOS': textToHtml(data, currentText)}, function () {
        });
    }).catch((error) => {
        chrome.storage.local.set({'textPOS': "Error"}, function () {
        });
    });
}

chrome.contextMenus.onClicked.addListener(function (clickData) {
    if (String(clickData.menuItemId === Title) && clickData.selectionText) {
        chrome.storage.local.set({'text': "loading"}, function () {
        });
        chrome.storage.local.set({'textPOS': "loading"}, function () {
        });
        let currentText = String(clickData.selectionText);
        let inputData = {"inputs": currentText}
        let request = {
            method: "POST",
            headers: {
                Authorization: "Bearer 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"
            },
            body: JSON.stringify(inputData)
        }
        requestNer(currentText, inputData, request)
        requestPos(currentText, inputData, request)
    }
});
