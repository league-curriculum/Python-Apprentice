# Getting Started with Codespaces

## Create a Codespace

A Codespace is basically Visual Studio Code running on the web. If you use VS Code
on your local machine, Codespaces will be very familiar. 

### Use the Button

You can create codespace for the Python Level 1 repository by pressing the button below. 

<span style="background-color: orange; padding: 10px 24px; margin-bottom: 10px; margin-right: 7px;">
<a href="https://codespaces.new/league-curriculum/Python-Level-1" target="_blank" style="color: white; font-size: 12pt; align-items: center; row-gap: 7px; column-gap: 7px;">
<img src="https://images.jointheleague.org/p3logos/github-mark-white.png" alt="Open in Codespaces" style="width: 20px; vertical-align: middle;">Open in Codespaces
</a></span>

### Manual Process

On the [repository page](https://github.com/league-curriculum/Python-Level-1), click on the green "<> Code" button, after the window
pops up, click on the "Codespaces" tab. It will look like this: 

<center><img src="https://images.jointheleague.org/module-navigation/create_codespace.png" style="width: 500px;"></center>

Click on the "Create codespace on master"  button. A new tab or window will open, and
it will read that it is "Setting up your codespace". This may take a few
minutes. When it is done, you will have a Visual Studio Code window, which will look like this: 

<center><img src="https://images.jointheleague.org/module-navigation/vscode.png" width="600px"></center>

## Open a Virtual Screen on the Web

Your Codespace is running your code in a data center far away, and that server
doesn't have a screen, so if you want to see your program output, you have to
create a virtual screen. 

In the bottom pane of the VSCode window, click on the "PORTS" tab. ( If you don't see a 
"PORTS" tab, you probably can skip this step. )

<center><img src="https://images.jointheleague.org/module-navigation/ports_pane.png" width="600px"></center>

Hover over the "Forwarded Address" for port 6080. You will see a small icon
that looks like a split box with a magnifying lens Click on it. This will
open a new browser window with a "noVNC" logo. 

You might need to drag the browser window to the right side of the screen. Your
screen should look something like:

<center><img src="https://images.jointheleague.org/module-navigation/browser_window.png" width="600px"></center>

Click on "Connect". If it asks for a password,  enter the passwod: "code4life"


Now you have a virtual screen running. When your program writes to the screen, it will show up in this window. 
