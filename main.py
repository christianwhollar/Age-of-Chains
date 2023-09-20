from agents.dispatcher import Dispatcher

if __name__ == '__main__':
    d = Dispatcher()
    response = d.generate_response('Hello there!')
    print(response)