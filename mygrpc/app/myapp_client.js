var PROTO_PATH = __dirname + '/../protos/myapp.proto';

var grpc = require('grpc');
var myapp_proto = grpc.load(PROTO_PATH).myapp;

function main() {
    var client = new myapp_proto.myapp('localhost:50051',
                                         grpc.credentials.createInsecure());
    client.sayHello({queryString:"Shakeeb"}, function(err, response) {
        response.results.forEach(function(result) {
            console.log('Response recvd: '+ result.response);
        });
    });
}

main();
