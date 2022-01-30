var cnt = 0;
var limit = 10;

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

Plotly.newPlot('chart',plotData,layout);

var ws_url = 'ws://' + window.location.host + '/ws/graph/';
var socket = new WebSocket(ws_url);
socket.onmessage = function(event){
    var data = JSON.parse(event.data);
    console.log(data.message);

    var today = new Date();
    var time = padZero(today.getHours()) + ":" + padZero(today.getMinutes()) + ":" + padZero(today.getSeconds());

    Plotly.extendTraces('chart',{ 
        x: [[time]],
        y: [[data.message]]
    }, [0]);
    cnt++;
    if(cnt > limit) {
        Plotly.relayout('chart',{
            xaxis: {
                range: [cnt-limit,cnt],
                linecolor: 'black',
                linewidth: 2,
                mirror: true
            }
        });
    }
    
    function padZero(num){
        if (num<10){
            return '0'+String(num)
        }else{
            return String(num)
        }
    }
}