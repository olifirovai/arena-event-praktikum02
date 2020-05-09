import random

from editor import (
    create_different_characters,
    create_different_equipment,
    equip_characters,
)


def main():
    equipments = create_different_equipment()
    characters = create_different_characters()
    equip_characters(characters, equipments)

    while len(characters) > 1:
        attacking = random.choice(characters)

        defending_characters = characters[:]
        defending_characters.remove(attacking)

        defending = random.choice(defending_characters)

        attacking.make_attack(defending)
        print(attacking.name, 'атакует', defending.name)

        if defending.hp <= 0:
            characters.remove(defending)

    print(characters[0].name)


if __name__ == "__main__":
    main()
