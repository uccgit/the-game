# Combat Sequence for Player Versus Enemy and Player VS Mini Boss, Player VERSUS BOSS
# This is just something to get started


class Combat:
    def __init__(self, player_hp, enemy_hp):
        self.player_hp = player_hp
        self.enemy_hp = enemy_hp

    def hp_difference(self):
        while self.player_hp and self.enemy_hp > 0:
            break


class Enemy(Combat):
    def __init__(self):
        pass


class MiniBoss(Combat):
    def __init__(self):
        pass


class Boss(Combat):
    def __init__(self):
        pass
