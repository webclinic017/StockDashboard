tweetSocket.onmessage = function(event){
    var data = JSON.parse(event.data);
    display = document.querySelector('#tweet-feed');
    //console.log(data.ids)
    // for (let i = 0; i < data.urls.length; i++){
    //     url = data.urls[i];
    //     var block = document.createElement("blockquote");
    //     var link = document.createElement("a")
    //     link.setAttribute('href', url)
    //     block.appendChild(link)
    //     display.appendChild(block)
    // }
    
    var html="";
    for (let i = 0; i < data.ids.length; i++){
        id = data.ids[i];
        var tweet = `
        <div class="twitter-tweet twitter-tweet-rendered" style="display: flex; max-width: 550px; width: 100%; margin-top: 10px; margin-bottom: 10px;"><iframe id="twitter-widget-0" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" class="" style="position: static; visibility: visible; width: 300px; height: 336px; display: block; flex-grow: 1;" title="Twitter Tweet" src="https://platform.twitter.com/embed/Tweet.html?dnt=false&amp;embedId=twitter-widget-0&amp;features=eyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3NwYWNlX2NhcmQiOnsiYnVja2V0Ijoib2ZmIiwidmVyc2lvbiI6bnVsbH19&amp;frame=false&amp;hideCard=false&amp;hideThread=false&amp;id=${id}&amp;lang=en&amp;origin=http%3A%2F%2F127.0.0.1%3A8000%2Fupdate%2F3mo%2FFB&amp;sessionId=b723ad24ee5c75a7bf48b75a238e7436c46ddd39&amp;theme=light&amp;widgetsVersion=0a8eea3%3A1643743420422&amp;width=550px" data-tweet-id="${id}"></iframe></div>
        `
        html+=tweet;
    }
    display.innerHTML = html;
}