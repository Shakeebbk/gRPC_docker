from concurrent import futures
import time

import grpc

import myapp_pb2
import myapp_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class myappServicer(myapp_pb2_grpc.myappServicer):

    def sayHello(self, request, context):
        resp = myapp_pb2.queryResponse()
        res = resp.results.add()
        res.query = request.queryString
        res.response = "Nice to meet you!"
        return resp

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myapp_pb2_grpc.add_myappServicer_to_server(myappServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
      while True:
        time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
      server.stop(0)

if __name__ == '__main__':
  serve()
