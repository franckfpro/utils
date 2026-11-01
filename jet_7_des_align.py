#!/usr/bin/env python3
import argparse
import random

DICES = [4, 6, 8, 10, 12, 20, 100]

def roll_dices():
    return {d: random.randint(1, d) for d in DICES}

def format_roll(roll):
    padding = {4: 1, 6: 1, 8: 1, 10: 2, 12: 2, 20: 2, 100: 3}
    return " - ".join(f"D{d}={v:0{padding[d]}d}" for d, v in roll.items())

def main():
    parser = argparse.ArgumentParser(description="Génère des jets aléatoires pour les 7 dés de JDR.")
    parser.add_argument("-n", "--nombre", type=int, default=1, help="Nombre de sorties désirées (par défaut: 1)")
    args = parser.parse_args()

    for _ in range(args.nombre):
        roll = roll_dices()
        print(format_roll(roll))

if __name__ == "__main__":
    main()
