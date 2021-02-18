# POLYRIZE - MAGIC LIST APP AND ITEM REFINING

THE APP IS IN PIPENV - PIPFILE IS INCLUDED

INSTRUCTIONS:
1. Run the command "pipfile lock"
2. Run the app with the requested routes

## PART 1 - MAGIC LIST
The magic list is lying in models.magic_list.py
It is an implementation of a class inherited from 'list'

## PART 2 - ITEM REFINING
This is a Sanic based app.
The available routes are:
1. 'login/' - which contains the login section (jwt not yet supported)
2. 'items_refine/' - Expects a json with 'items' key which contains a list of items - returns a refined dict as requested
