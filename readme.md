# WallGUI

WallGUI is the Eel-based puesdo-OS for the Computer Science interactive display. It is modular, so new apps and experiences can be added over time. 

#### The current apps are listed below:
- **Fortune:** *More of a funny quote machine than anything right now*
- **DVD:** *Shows the CSTA logo bouncing around the screen like the old DVD logo*
- **Hat:** *A series of tests for the Pi's SenseHat*

## Use

### Startup Instructions

#### For Original Raspberry Pi
1. Ensure no SSH Connection is Running
2. Open the Linux Terminal
3. Navigate to the WallGUI directory via `cd Desktop/WallGUI`
4. Run `python app.py`
5. Press `alt+F4` to leave the program

### Download Instructions

#### Download WallGUI to a new Raspberry Pi
1. Navigate to [WallGUI GitHub]()
2. Download source code into the `"~/Desktop/WallGUI"` folder or other desired directory
3. Verify that all internal directories remain consistent and have the same local directories as on GitHub
4. Open Terminal and run `pip install Eel`
5. Run WallGUI to verify functionality

#### Download WallGUI to a Raspberry Pi without a SenseHat
1. Navigate to [WallGUI GitHub]()
2. Download source code into the `"~/Desktop/WallGUI"` folder or other desired directory
3. Verify that all internal directories remain consistent
4. Open `app.py` and set `const SENSE_HAT = False`
4. Open Terminal and run `pip install Eel`
5. Run WallGUI to verify functionality 
    - No sense hat features will be available


## Editing

### SSH
**IP Address:** `192.168.153.201`  
**User:** `ncssm`  
**Password:** `1msscn`

**Try the VS Code "Remote - SSH" Extension**  
This allows you to SSH with a nice interface and shows you all the available files as if they were local to your laptop. It also allows for easy editing and file transfer. (You'll also need the "Remote Explorer" Extension)

### New Apps

#### Integrate an HTML program with WallGUI
1. Place HTML app and all its dependencies in the `"WallGUI/web/apps"` directory
2. Place a PNG icon for your app in the `"WallGUI/web/apps/img"` directory
3. Make sure all directories referenced in your code are valid and point to the file's new location.
4. Open the `index.html` file
5. Duplicate the `"app_button"` code inside the `"apps_list"` div, and replace all fields with the names and locations of your new code and icon

```
<button type="button" id="button_name" onclick="location.href='apps/name.html'" class="app_button">
    <img src="apps/img/name.png" alt="?" class="app_img"> <br>
    Name
</button>
```

#### Use Python in Javascript via Eel

I am not going to make a new guide for this, as many better ones are already available online. Instead, here are a few good links:
- Official GitHub: <https://github.com/python-eel/Eel>
- Basic Guide: <https://www.geeksforgeeks.org/create-html-user-interface-using-eel-in-python/>

Note that Eel is browser based, with all the limitations and advantages that provides. Errors are a bit hard to spot, as the code will still run and the program is somewhat power intensive. 