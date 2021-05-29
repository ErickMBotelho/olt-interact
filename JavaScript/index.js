const { TelnetSocket } = require("telnet-stream")
const net = require("net")

connection = net.createConnection(23, "10.10.0.30");
tn = new TelnetSocket(connection)

tn.on("close", function () {
    console.log("Conexão encerrada!")
    return process.exit()
})

tn.on("data", function (buffer) {
    return process.stdout.write(buffer.toString("utf8"))
})

process.stdin.on("data", function (buffer) {
    return tn.write(buffer.toString("utf8"));
});

function oltInteract(command) {
    return tn.write(command.toString("utf8") + '\r\n')
}

oltInteract("GEPON\r\nGEPON\r\nEN\r\nGEPON")
oltInteract("cd gpononu")
// oltInteract("show cpu_using slot 3 link 15 onu 6")
// oltInteract("show optic_module slot 3 link 15 onu 6")
// oltInteract("show onu_time slot 3 link 15 onu 6")
// oltInteract("show wifi_serv slot 3 link 15 onu 6")
// oltInteract("list")
oltInteract("show authorization slot all link all")
// oltInteract("cd .\r\nq")
