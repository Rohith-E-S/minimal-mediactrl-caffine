# Minimalist Waybar Configuration & Media Player

This repository contains my personal [Waybar](https://github.com/Alexays/Waybar) configuration files (`dotfiles`), featuring a custom **Minimalist Expandable Media Player And Caffine toogle**.


## 🎵 Featured: Minimalist Media Player Drawer

A clean, distraction-free media control module that integrates seamlessly into Waybar. It shows a dynamic status icon that expands into a full control suite when clicked.

## ☕ Caffeine (Idle Inhibitor)

A simple toggle button to prevent the screen from locking or sleeping.
- **Icon**: Shows a coffee cup () when activated, and a sleepy eye/bed (󰒲) when deactivated.
- **Usage**: Click to toggle presentation mode/insomnia.


### Features
- **Minimal Footprint**: Only shows a status icon (Music Note) by default.
- **Expandable Controls**: Slides open to reveal Previous, Play/Pause, and Next buttons.
- **Dynamic Icons**: Play/Pause button changes based on actual status ( / ).
- **Metadata Tooltips**: Hovering the icon shows "Artist - Title".
- **Smart Status**: Icon dims when paused and hides/changes when stopped.
- **Robustness**: Handles multiple players, timeouts, and special characters correctly.

### Dependencies
- `waybar`
- `playerctl` (for media control)
- `python3` (for the script)
- A Nerd Font (e.g., `JetBrainsMono Nerd Font` or `FontAwesome`) for icons.

### Installation / Usage

1. **Scripts**:
   Place `scripts/media-player.py` in your Waybar scripts directory.
   ```bash
   chmod +x ~/.config/waybar/scripts/media-player.py
   ```

2. **Configuration (`config.jsonc`)**:
   Add the following group and custom modules:
   ```jsonc
   "group/media": {
       "orientation": "inherit",
       "drawer": {
           "transition-duration": 500,
           "children-class": "media-controls",
           "transition-left-to-right": false
       },
       "modules": [
           "custom/media-icon",
           "custom/media-prev",
           "custom/media-play-pause",
           "custom/media-next"
       ]
   },
   "custom/media-icon": {
       "format": "{}",
       "return-type": "json",
       "max-length": 40,
       "on-click": "playerctl play-pause",
       "on-click-right": "playerctl stop",
       "smooth-scrolling-threshold": 10,
       "on-scroll-up": "playerctl next",
       "on-scroll-down": "playerctl previous",
       "exec": "python3 ~/.config/waybar/scripts/media-player.py",
       "interval": 1
   },
   // ... define media-prev, media-play-pause, media-next (see config)
   ```

3. **Styling (`style.css`)**:
   ```css
   #custom-media-icon {
       min-width: 12px;
       margin: 0 7.5px;
   }
   /* See style.css for full styling */
   ```

## ☕ Caffeine (Idle Inhibitor)

A simple toggle button to prevent the screen from locking or sleeping.

### Features

- **Distraction Free**: A click on caffine icon toggles idle-inhibitor stopping anoyances.
- **Presentation Mode**: Keeps the screen awake for reading, watching videos, or presentations.
- **Visual Feedback**: Distinct icons for active (☕) and inactive (󰒲) states.
- **Battery Saving**: Easily toggle off when not needed to save power.

## 📂 Dotfiles Structure

- `config.jsonc`: Main configuration file.
- `style.css`: Stylesheet (imported themes + custom overrides).
- `scripts/`: Helper scripts (including `media-player.py`).

## 🛠️ Setup

1. Clone this repository to your config folder (or copy files).
2. Ensure dependencies are installed (`sudo pacman -S playerctl python`).
3. Reload Waybar.

---
*Created with the help of Gemini Antigravity.*
