$(document).ready(function () {
    var namespace = "/senpai";
    var socket = chat.connect("http://" + document.domain + ":" + location.port + namespace);

    socket.on("connect", function() {
        console.log("Connected");
    });

    socket.on("connect", function() {
        console.log("Disconnected");
    });

    socket.on("new-message", function(message) {
        $("#coutput").append(
            "<div>" + message + "</div>"
        );

        $("#coutput").scrollTop($("#coutput")[0].scrollHeight);
    });

    $("#clear-button").on("click", function () {
        $("#cinput").val("");
    });

    $("#chat-form").on("submit", function () {
        socket.emit("new-message", $("#cinput").val());
        $("#cinput").val("");
        return false;
    });

    $("#test-button").on("click", function () {
        var message = "Value " + Math.random();
        console.log("New message sent: ", message);
        socket.emit("new-message", message);
    });
});