#!/usr/bin/env python3
import secrets
import sys

nombre_lignes = int(sys.argv[1]) if len(sys.argv) > 1 else 1

for _ in range(nombre_lignes):
    nombres = [f"{secrets.randbelow(10_000):04d}" for _ in range(15)]
    print(" - ".join(nombres))
