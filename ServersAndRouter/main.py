class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    _next_ip = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server._next_ip
        Server._next_ip += 1

    def send_data(self, data) -> None:
        router.buffer.append(data)

    def get_data(self) -> list:
        response = self.buffer.copy()
        self.buffer.clear()
        return response
    
    def get_ip(self):
        return self.ip
    
    def __repr__(self):
        return f"Сервер №{self.get_ip()}"


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server: Server) -> None:
        self.servers[server.get_ip()] = server

    def unlink(self, server: Server) -> None:
        if server.get_ip() in self.servers:
            del self.servers[server.get_ip()]

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
            else:
                return
        self.buffer.clear()

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()