import json
from pathlib import Path

class SettingsManager:
    def __init__(self):
        self.settings_file = Path(__file__).parent.parent / "misc" / "configs" / "settings.json"
        self.defaults = {
            "universal": {
                "volume": 100,
                "fullscreen": False,
                "language": "EN"
            },
            "shinigami": {
                "speed": 5,
                "attack": 10
            },
            "hollows": {
                "speed": 4,
                "attack": 8
            },
            "quiggers": {
                "speed": 3,
                "attack": 7
            },
            "fullbringers": {
                "speed": 4,
                "attack": 9
            }
        }
        self.data = {}

    def load(self):
        """Load settings from file, fallback to defaults if missing."""
        if self.settings_file.exists():
            try:
                with open(self.settings_file, "r") as f:
                    self.data = json.load(f)
                print("Settings loaded successfully.")
            except Exception as e:
                print("Error loading settings, using defaults:", e)
                self.data = self.defaults.copy()
        else:
            print("Settings file not found, using defaults.")
            self.data = self.defaults.copy()

    def save(self):
        """Save current settings to file."""
        self.settings_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.settings_file, "w") as f:
            json.dump(self.data, f, indent=4)
        print("Settings saved successfully.")

    def get(self, category, key, fallback=None):
        """Get a specific setting, fallback to defaults if missing."""
        return self.data.get(category, {}).get(key, self.defaults.get(category, {}).get(key, fallback))

    def set(self, category, key, value):
        """Set a specific setting and optionally auto-save."""
        if category not in self.data:
            self.data[category] = {}
        self.data[category][key] = value
