import grpc

import myapp_pb2
import myapp_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = myapp_pb2_grpc.myappStub(channel)
    response = stub.sayHello(myapp_pb2.queryRequest(queryString="Shakeeb"))
    for resp in response.results:
        print(resp.query+",", resp.response)

if __name__ == '__main__':
  run()
