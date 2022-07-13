const Title = "ParsNer"
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
        html_div += `<span class = \"NER ${elem['entity_group']}\">` + text.slice(parseInt(elem['start']), parseInt(elem['end'])) + "</span>";
        last_index = parseInt(elem['end']);
    }
    html_div += text.slice(last_index, text.length)
    console.log(html_div)
    return html_div
}

chrome.contextMenus.onClicked.addListener(function (clickData) {
    if (String(clickData.menuItemId === Title) && clickData.selectionText) {

        chrome.storage.sync.set({'text': "loading"}, function () {
        });
        let currentText = String(clickData.selectionText);
        let inputData = [
            {
                "lang": "fa",
                "text": currentText
            }];
        fetch("http://127.0.0.1:8000/nerTest", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Client-Id': 'hamed',
                'Client-Password': '123',
                // 'Access-Control-Allow-Origin': '*',
                // 'Access-Control-Allow-Credentials': 'true'
            },
            body: JSON.stringify(inputData)
        }).then(res => {
            return res.json()
        }).then(data => {
            chrome.storage.sync.set({'text': textToHtml(data['result'][0], currentText)}, function () {
            });
        }).catch((error) => {
            chrome.storage.sync.set({'text': "Error"}, function () {
            });
        });
    }
});
