const express = require('express');
const app = express();

app.use("/", function(req, res){
    res.sendFile(__dirname + '/index.html'); //이 파일에서 보내는 파일을 받는다는 뜻인 듯
});

app.listen(8080); //8080 채널을 통해 듣겠다는 뜻 ㅣ 유저는 8080, 서버는 8081

const WebSocket = require('ws');

const socket = new WebSocket.Server({
    port:8081
});

socket.on('connection', (ws, req) => {
    
    ws.on('message', (msg)=>{
        console.log('유저에게로 부터 도착한 메세지 입니다. : ' + msg);
        ws.send('반갑습니다');
    })
});