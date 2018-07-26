# SimpleBugTracker
Inspired by a post on HackerNews, this uses the SimpleCLI modules I wrote to track bugs locally into a JSON document. The tracker creates a data.json file to store the data.

This builds upon the [SimpleCLI](https://github.com/normanzhao/SimpleCLI) modules I built.

All commands and their associated run functions are in functions.py. These run functions call upon methods located in io.py. The scripts are laid out this way to decouple the commands that user interacts with, and the methods that actually do the anything. This is an attempt at dependency injection so the business logic can be changed at at anytime. The command functions do not and will not know how their methods is actually executed.
