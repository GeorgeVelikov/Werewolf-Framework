import Shared.constants.GameConstants as GameConstants;

from Client.screens.MainMenuScreen import MainMenuScreen;
from Client.screens.GameListScreen import GameListScreen;

import tkinter as tk
import tkinter.ttk as ttk

def ShowMainMenu(window):
    window.DisplayScreen(MainMenuScreen);

def ShowGameList(window):
    window.DisplayScreen(GameListScreen);
