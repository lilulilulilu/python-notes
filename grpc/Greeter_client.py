import helloworld_pb2_grpc
import grpc
import helloworld_pb2

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:30005") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="bob"))
        
    print("Greeter client received: " + response.message)