#!/usr/bin/env python3
"""Запуск движка OpenSpec.

На машину движок не ставится: uvx собирает пакет из git и держит его
в своём кеше (~/.cache/uv). В проекте нет ни одного файла движка.

Версия задаётся веткой или тегом в ENGINE ниже. Файл в .gitignore — его
создаёт `openspec --init` у каждого одинаковым, из того же источника.
Чтобы сменить версию для всей команды, правь ENGINE_SOURCE в движке,
а не эту строку: локальная правка переживёт только до следующего --init.

Запуск:
    macOS / Linux   ./openspec.py --codegen --change 1
    Windows         python openspec.py --codegen --change 1

Единственное требование к машине — установленный uv (даёт команду uvx).
Python для самого движка uv скачает себе сам, системный не нужен.

Файл создан командой openspec --init.
"""
import shutil
import subprocess
import sys

# Источник движка. Ветка (@master) — всегда свежий, но меняется сам.
# Тег (@v0.5.0) или SHA — фиксирует версию намертво.
ENGINE = "__ENGINE_SOURCE__"

if shutil.which("uvx") is None:
    sys.exit(
        "✖ Не найден uvx (входит в uv).\n"
        "  macOS / Linux:  brew install uv\n"
        "  Windows:        winget install astral-sh.uv\n"
        "  Либо:           https://docs.astral.sh/uv/getting-started/installation/"
    )

sys.exit(subprocess.call(
    ["uvx", "--quiet", "--from", ENGINE, "openspec", *sys.argv[1:]]))
