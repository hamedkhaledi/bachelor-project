const Title = "Pars Ner"
const menuItem = {
    "id": Title, "title": Title, "contexts": ["selection"]
};

chrome.contextMenus.create(menuItem);

function textToHtml(data, text) {
    let html_div = "";
    let last_index = 0;
    console.log(data)
    for (const elem of data) {
        if (last_index < parseInt(elem['start'])) {
            html_div += text.slice(last_index, parseInt(elem['start']))
        }
        html_div += `<span class = \"NER ${elem['entity_group'].split("_")[0]}\">` + text.slice(parseInt(elem['start']), parseInt(elem['end'])) + "</span>";
        last_index = parseInt(elem['end']);
    }
    html_div += text.slice(last_index, text.length);
    console.log(html_div);
    return html_div;
}

chrome.contextMenus.onClicked.addListener(function (clickData) {
    if (String(clickData.menuItemId === Title) && clickData.selectionText) {
        chrome.storage.local.set({'text': "loading"}, function () {
        });
        chrome.storage.local.set({'textPOS': "loading"}, function () {
        });
        let currentText = String(clickData.selectionText);
        let inputData = [
            {
                "lang": "fa",
                "text": currentText
            }];
        let request = {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Client-Id': 'hamed',
                'Client-Password': '123'
            },
            body: JSON.stringify(inputData)
        }
        fetch("http://127.0.0.1:8000/nerTest", request).then(res => {
            return res.json();
        }).then(data => {
            chrome.storage.local.set({'text': textToHtml(data['result'][0], currentText)}, function () {
            });
        }).catch((error) => {
            chrome.storage.local.set({'text': "Error"}, function () {
            });
        });

        fetch("http://127.0.0.1:8000/posTest", request).then(res => {
            return res.json();
        }).then(data => {
            chrome.storage.local.set({'textPOS': textToHtml(data['result'][0], currentText)}, function () {
            });
        }).catch((error) => {
            chrome.storage.local.set({'textPOS': "Error"}, function () {
            });
        });
    }
});
