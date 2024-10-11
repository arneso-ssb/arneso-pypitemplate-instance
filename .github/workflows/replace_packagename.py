"""This file adds a 'ssb-' prefix to the package name in pyproject.toml."""

from pathlib import Path

import tomlkit

with Path("pyproject.toml").open(encoding="utf-8") as file:
    data = tomlkit.parse(file.read())

if "tool" in data and "poetry" in data["tool"] and "name" in data["tool"]["poetry"]:
    name = data["tool"]["poetry"]["name"]
    data["tool"]["poetry"]["name"] = f"ssb-{name}"

with Path("pyproject.toml").open("w", encoding="utf-8") as file:
    tomlkit.dump(data, file)
