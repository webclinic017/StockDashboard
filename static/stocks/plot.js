var cnt = 0;
var limit = 10;
const market_status = document.querySelector('#market-status').textContent
const ws_url = 'ws://' + window.location.host + '/ws/graph/';
const socket = new WebSocket(ws_url);

const waitForOpenConnection = (socket) => {
    return new Promise((resolve, reject) => {
        const maxNumberOfAttempts = 10
        const intervalTime = 200 //ms

        let currentAttempt = 0
        const interval = setInterval(() => {
            if (currentAttempt > maxNumberOfAttempts - 1) {
                clearInterval(interval)
                reject(new Error('Maximum number of attempts exceeded'))
            } else if (socket.readyState === socket.OPEN) {
                clearInterval(interval)
                resolve()
            }
            currentAttempt++
        }, intervalTime)
    })
}

const sendMessage = async (socket, msg) => {
    if (socket.readyState !== socket.OPEN) {
        try {
            await waitForOpenConnection(socket)
            socket.send(msg)
        } catch (err) { console.error(err) }
    } else {
        socket.send(msg)
    }
}

$( document ).ready(function() {
    if (market_status=='Closed'){
        document.querySelector('#data-mode').value = '1mo'
    }

    var numStocks = document.getElementById("stockList").getElementsByTagName("li").length
    if (numStocks>0){
        document.querySelector('#stock-selection').selectedIndex = 1
        message = JSON.stringify({
            'data_mode': document.querySelector('#data-mode').value,
            'stock_select': document.querySelector('#stock-selection').value,
        })
        sendMessage(socket,message)
    }
});

var trace1 = {
    x:[],
    y:[],
    mode: 'lines+markers',
    marker: {
        color: '#DDDF61',
        size: 8
    },
    line: {
        color: '#DDDF61',
        width: 2
    },
    name: 'Bid'
};
var trace2 = {
    x:[],
    y:[],
    mode: 'lines+markers',
    marker: {
        color: '#E51E11',
        size: 8
    },
    line: {
        color: '#E51E11',
        width: 2
    },
    name: 'Ask'
};
var trace3 = {
    x:[],
    y:[],
    mode: 'lines+markers',
    marker: {
        color: '#1587F2',
        size: 8
    },
    line: {
        color: '#1587F2',
        width: 2
    },
    name: 'Historical'
};

var plotData = [trace1,trace2]
var layout = {
    xaxis: {
        range: [1, limit],
        linecolor: 'black',
        linewidth: 2,
        mirror: true,
    },
    yaxis: {
        linecolor: 'black',
        linewidth: 2,
        mirror: true,
        gridcolor: '#C8C8C4',
        //title: 'Price (USD)',
        tickformat: '$',
    },
    plot_bgcolor: '#444',
    showlegend: true,
    legend: {
        x: 1,
        xanchor: 'right',
        y: 1,
        bgcolor: '#2E063F',
        font: {
            family: 'sans-serif',
            size: 12,
            color: '#FFFFFF'
        },
    }
};

//Plotly.newPlot('chart',plotData,layout);

// socket.onmessage = function(event){
//     var data = JSON.parse(event.data);
//     console.log(data.message);

//     var today = new Date();
//     var time = padZero(today.getHours()) + ":" + padZero(today.getMinutes()) + ":" + padZero(today.getSeconds());

//     Plotly.extendTraces('chart',{ 
//         x: [[time]],
//         y: [[data.message]]
//     }, [0]);
//     cnt++;
//     if(cnt > limit) {
//         Plotly.relayout('chart',{
//             xaxis: {
//                 range: [cnt-limit,cnt],
//                 linecolor: 'black',
//                 linewidth: 2,
//                 mirror: true
//             }
//         });
//     }
// }

socket.onmessage = function(event){
    var data = JSON.parse(event.data);
    if (market_status=='Closed'){
        processHistorical(data.x_val,data.y_val)
    }
}

function processHistorical(x_val,y_val){
    trace3.x = x_val
    trace3.y = y_val
    var selection = document.querySelector('#data-mode')
    var data_mode = selection.options[selection.selectedIndex].text
    var stock_select = document.querySelector('#stock-selection').value
    Plotly.newPlot('chart',[trace3],{
        title: {
            text: stock_select + ': ' + data_mode
        },
        yaxis: {
            tickformat: '$'
        }
    });
}

//Handle update button click
document.querySelector('#update-btn').onclick = function(e) {
    var data_mode = document.querySelector('#data-mode').value;
    var stock_select = document.querySelector('#stock-selection').value;
    if (market_status=="Closed" && data_mode=="realTime"){
        document.querySelector('#update-error').style.display = "block"
    }else if (stock_select=='none'){
        alert('Please select a stock!')
    }else{
        document.querySelector('#update-error').style.display = "none"
        socket.send(JSON.stringify({
            'data_mode': data_mode,
            'stock_select': stock_select,
        }));
    }
};

function padZero(num){
    if (num<10){
        return '0'+String(num)
    }else{
        return String(num)
    }
}