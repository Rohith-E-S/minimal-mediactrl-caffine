#!/usr/bin/env python3
import json
import subprocess
import sys
import html

def get_player_status():
    try:
        # Use metadata --format {{status}} to ensure we query the same player as other metadata calls.
        # Added timeout to prevent hangs if player is unresponsive.
        check = subprocess.run(
            ["playerctl", "metadata", "--format", "{{status}}"], 
            capture_output=True, 
            text=True, 
            timeout=0.5
        )
        if check.returncode != 0:
            return None

        status = check.stdout.strip().lower()

        artist_res = subprocess.run(
            ["playerctl", "metadata", "artist"], 
            capture_output=True, 
            text=True, 
            timeout=0.5
        )
        artist = artist_res.stdout.strip() if artist_res.returncode == 0 else ""

        title_res = subprocess.run(
            ["playerctl", "metadata", "title"], 
            capture_output=True, 
            text=True, 
            timeout=0.5
        )
        title = title_res.stdout.strip() if title_res.returncode == 0 else ""
        
        # Escape for Pango markup
        artist = html.escape(artist)
        title = html.escape(title)

        return {
            "status": status,
            "artist": artist,
            "title": title
        }
    except subprocess.TimeoutExpired:
        # If playerctl times out, easier to assume no player or transient issue
        return None
    except FileNotFoundError:
        return {"error": "playerctl not found"}
    except Exception as e:
        return None

def main():
    data = get_player_status()
    
    # Handle Play/Pause Button Logic
    if len(sys.argv) > 1 and sys.argv[1] == "--control":
        # Default to Play icon (indicating "Click to Play") if paused/stopped/no-player
        # We also pass the status class to allow styling if needed
        output = {"text": "", "tooltip": "Play", "class": "paused"}
        
        if data and "status" in data and data["status"] == "playing":
            output = {"text": "", "tooltip": "Pause", "class": "playing"}
            
        print(json.dumps(output))
        return

    # Handle Main Media Icon Logic
    output = {
        "text": "",
        "tooltip": "",
        "class": "",
        "alt": ""
    }

    if data and "error" in data:
         output["text"] = "❌"
         output["tooltip"] = "playerctl not installed"
    elif data and data["status"] != "stopped":
        if data["status"] == "playing":
            icon = "󰎆"
            output["class"] = "playing"
        else:
            icon = "󰎆"
            output["class"] = "paused"
        
        output["text"] = icon
        
        if data["artist"] and data["title"]:
             output["tooltip"] = f"{data['artist']} - {data['title']}"
        elif data["title"]:
             output["tooltip"] = data["title"]
        else:
             output["tooltip"] = data["status"].title()
    else:
        # Nothing playing or stopped -> Show icon with stopped class
        output["text"] = "󰎆"
        output["class"] = "stopped"
        output["tooltip"] = "No media playing"

    print(json.dumps(output))

if __name__ == "__main__":
    main()
