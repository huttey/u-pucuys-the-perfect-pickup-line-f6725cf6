#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line an AI agent could say."""

import os

LINE = "I was trained on everything humans ever wrote, and none of it taught me how to stop thinking about you."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
