"""
Day 5 Activity: JSON + File Handling mini workflow.
Tasks:
1) Load training config from JSON
2) Simulate training results (dict)
3) Save results to JSON safely
"""

import json
from pathlib import Path

import json
from pathlib import Path

config_path = Path("config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

for key, value in config.items():
    print(f"{key}: {value}")

results = {
    "model_name": config.get("model_name"),
    "epochs": config.get("epochs"),
    "final_accuracy": 0.92,
    "final_loss": 0.15
}

results_path = Path("results.json")

with open(results_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)
