import yaml


class Monster(yaml.YAMLObject):
    yaml_tag = u"!Monster"

    def __init__(self, ac, attacks, hp):
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return "%s(hp=%r, ac=%r, attacks=%r)" % (
            self.__class__.__name__,
            self.hp,
            self.ac,
            self.attacks,
        )


print(yaml.dump(Monster(hp=[2, 6], ac=16, attacks=["BITE", "HURT"])))


# register_class(Monster)

# with open("pods.yml", mode="w", encoding="utf-8") as file:
#     yaml.dump([PodManager(3)], file)


monster = yaml.load(
    open("yamlBase.yaml"),
    Loader=yaml.Loader,
)

print(monster)
print(monster.hp)
# with open("jina.txt") as file:
#     print(file)