import socket


class Connection:
    def __init__(self):
        self.type = type
        self.HOST = '127.0.0.1'
        self.MAXBYTES = 65535
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.type = 0

    def connection1(self):
        self.s.bind((self.HOST, 1060))
        data, addres = self.s.recvfrom(self.MAXBYTES)
        print('conectado em', addres)
        self.s.sendto(data, (self.HOST, 1061))

    def connection2(self):
        self.s.bind((self.HOST, 1061))
        check = 'conexao feita'
        data = check.encode('ascii')
        self.s.sendto(data, (self.HOST, 1060))
        data, addres = self.s.recvfrom(self.MAXBYTES)
        message = data.decode('ascii')
        print(message)

    def player_life1(self, player):
        p_life = str(player.life).encode('ascii')
        self.s.sendto(p_life, (self.HOST, 1061))
        data, addres = self.s.recvfrom(self.MAXBYTES)
        life_2 = data.decode('ascii')
        life_2 = int(life_2)
        if player.life >= life_2:
            player.life = life_2
        print(life_2)

    def player_life2(self, player):
        p_life = str(player.life).encode('ascii')
        self.s.sendto(p_life, (self.HOST, 1060))
        data, addres = self.s.recvfrom(self.MAXBYTES)
        life_1 = data.decode('ascii')
        life_1 = int(life_1)
        if player.life >= life_1:
            player.life = life_1
        print(life_1)

    def enemy_life1(self, enemy):
        e_life = str(enemy.life).encode('ascii')
        self.s.sendto(e_life, (self.HOST, 1061))
        data, addres = self.s.recvfrom(self.MAXBYTES)
        enemy_2 = data.decode('ascii')
        enemy_2 = int(enemy_2)
        if enemy.life >= enemy_2:
            enemy.life = enemy_2
        print(enemy_2)

    def enemy_life2(self, enemy):
        e_life = str(enemy.life).encode('ascii')
        self.s.sendto(e_life, (self.HOST, 1060))
        data, addres = self.s.recvfrom(self.MAXBYTES)
        enemy_1 = data.decode('ascii')
        enemy_1 = int(enemy_1)
        if enemy.life >= enemy_1:
            enemy.life = enemy_1
        print(enemy_1)

    def player1(self, player, enemy):
        self.player_life1(player)
        self.enemy_life1(enemy)

    def player2(self, player, enemy):
        self.player_life2(player)
        self.enemy_life2(enemy)



