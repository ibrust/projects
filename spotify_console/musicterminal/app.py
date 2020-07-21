import curses 
import curses.panel 
from curses import wrapper
from curses.textpad import Textbox 
from curses.textpad import rectangle 

from client import Menu 
from client import DataManager


def show_search_screen(stdscr): 
    curses.curs_set(1) 
    stdscr.addstr(1, 2, "Artist name: (Ctrl-G to search)") 

    editwin = curses.newwin(1, 40, 3, 3) 
    rectangle(stdscr, 2, 2, 4, 44) 
    stdscr.refresh() 

    box = Textbox(editwin) 
    box.edit() 

    criteria = box.gather() 
    return criteria 


def clear_screen(stdscr): 
    stdscr.clear() 
    stdscr.refresh() 


def main(stdscr): 

    curses.cbreak() 
    curses.noecho() 
    stdscr.keypad(True) 

    _data_manager = DataManager() 
    criteria = show_search_screen(stdscr) 
    height, width = stdscr.getmaxyx() 
    albums_panel = Menu('List of albums for the selected artist', (height, width, 0, 0)) 
    tracks_panel = Menu('List of tracks for the selected album', (height, width, 0, 0)) 
    artist = _data_manager.search_artist(criteria) 
    albums = _data_manager.get_artist_albums(artist['id'])

    clear_screen(stdscr) 

    
    albums_panel.items = albums             #albums are verified to be working 
    albums_panel.initialize_items()         #appears to be working
    albums_panel.update() 
    albums_panel.show()

    current_panel = albums_panel 

    is_running = True 

    while is_running: 
        curses.doupdate()
        #curses.panel.update_panels()               #this is crashing and I have no idea why, it might be a windows vs linux problem - this is not unicurses
        key = stdscr.getch()
        action = current_panel.handle_events(key)
        if action is not None: 
            action_result = action() 
            if current_panel == albums_panel and action_result is not None: 
                _id, uri = action_result 
                tracks = _data_manager.get_album_tracklist(_id) 
                current_panel.hide()
                current_panel = tracks_panel 
                current_panel.items = tracks 
                current_panel.initialize_items() 
                current_panel.show()
                
            elif current_panel == tracks_panel and action_result is not None: 
                _id, uri = action_result 
                _data_manager.play(uri) 

        if key == curses.KEY_F2: 
            clear_screen(stdscr)
            current_panel.hide()
            criteria = show_search_screen(stdscr) 
            artist = _data_manager.search_artist(criteria) 
            albums = _data_manager.get_artist_albums(artist['id'])
            #clear_screen(stdscr)                   #author put this here but... it didn't clear anything until I moved it above hide. not sure why he put it here.
            current_panel = albums_panel 
            current_panel.items = albums 
            current_panel.initialize_items() 
            current_panel.show()

        if key == ord('q') or key == ord('Q'): 
            is_running = False 

        current_panel.update() 



try: 
    wrapper(main) 
except KeyboardInterrupt: 
    print("Thanks for using this app, bye!") 


