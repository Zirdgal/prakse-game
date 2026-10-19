# Zird Rhythm Game

Rhythm game about tapping notes. Read more about it in DESIGN.md

## First Time Installation 

- Required `Python 3.11` or higher.   
- All commands should be ran in the `prakse-game` folder.  
- Run all commands `one by one` instead of copying the whole list.
### If you are on Windows (Powershell)
```
python -m venv .venv
.venv\Scripts\active.ps1
pip install -r requirements.txt
```
### If you are on Windows (Command Line)
```
python -m venv .venv
.venv\Scripts\active.bat
pip install -r requirements.txt
```
### If you are on MacOS or Linux
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Launch a Server

- Open a terminal in the `prakse-game` folder. It will stay open as long as you want your Server to be open for.
- If you **do not** see `(.venv)` on the **left side** for these commands, run .venv activation command **given in the earlier examples**, e.g. `.venv\Scripts\active.bat`.

### Run the following command
```
uvicorn api.main:app --reload
```

## Run the Game

- Open a `new` terminal in the `prakse-game` folder.

### Run the following command
```
python -m client.main
```

## Play the game

- For detailed instructions visit DESIGN.md.

## View your results in a **local** leaderboard

- Open https://localhost:8000/ to view the leaderboard


## REST API

| Method | Address                 | What does it do                                                           | Response  | 
|--------|-------------------------|---------------------------------------------------------------------------|-----------|
| POST   | `/scores`               | Save results in {"username": "username", "score": 123, "level": 2} format | 201       |
| GET    | `/scores/top`           | Returns the top 10 game results                                           | 200       |
| GET    | `/players/{name}/stats` | Returns player `username`, `bestScore` and `gamesPlayed`                  | 200 / 404 |

- Username has a 15 character limit, score wont be saved if it's negative. Data is stored locally in `/api/game.db`

## Example Game Screenshot

![Screenshot of Mouiiyo](./img/gameExampleScreenshot.png)

## If you want to make your own custom charts

- Check out the `/dev` folder. In there is `chartMaker.py` and `randomizeChart.py`
- With `chartMaker.py` you set the `SONG_ID_SELECTED` to a new id (for example 4) and add a new folder in `/game/charts/{SONG_ID_SELECTED}`. In this folder you add a `data.txt` file and a `song.txt` file. `data.txt` should follow the `/game/dataexample.txt` format of id in the first line and note spawning speed in the second line. **It is recommended to just use 20 spawning speed** for ~100 bpm songs, lower it for higher bpm, increase it for lower bpm. Also add your song to `/music being a `song{SONG_ID_SELECTED}.mp3` file.
- With the setup ready you can now run the `chartMaker.py` and hit your `lane1` key (Default: A) to the beat of the music. When the music has finished click the constant keybind: `F` which will finish the chartmaking and save it to `/game/charts/{SONG_ID_SELECTED}`.
- Now this generates a single chart that only has lane 1 notes. This is why `randomizeChart.py` exists It will make the notes more interesting instead of being a single lane.
- Now that you have made your own chart to actually play it you have to add the button to `main.py`. Due to time constraints a dynamic level selector was not added.