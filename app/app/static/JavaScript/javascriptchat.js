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
        $("#chat-output").append(
            "<div>" + message + "</div>"
        );

        $("#chat-output").scrollTop($("#chat-output")[0].scrollHeight);
    });

    $("#clear-button").on("click", function () {
        $("#chat-input").val("");
    });

    $("#chat-form").on("submit", function () {
        socket.emit("new-message", $("#chat-input").val());
        $("#chat-input").val("");
        return false;
    });

    $("#test-button").on("click", function () {
        var message = "Value " + Math.random();
        console.log("New message sent: ", message);
        socket.emit("new-message", message);
    });
});