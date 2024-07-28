# PUBG TDM Tracker

[![Build and test with Tox](https://github.com/proafxin/tdm-tracker/actions/workflows/ci.yaml/badge.svg)](https://github.com/proafxin/tdm-tracker/actions/workflows/ci.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/proafxin/statracking/develop.svg)](https://results.pre-commit.ci/latest/github/proafxin/statracking/develop)

PUBG does not keep track of TDM stats. This tool lets you upload screenshots of the final scoreboards and the scores will be saved in a sqlite database.

After all the rounds are over, when the final results are shown, take a screenshot. The system works best for higher quality screenshots. Optimal resolution for most accurate results is 4k.

## How to use locally

Only use it in linux systems with GPU support for [pytorch](https://pytorch.org/get-started/locally/). Steps to run the server:

* Install poetry: `curl -sSL https://install.python-poetry.org | python3 -`
* Install tox: `python3 -m pip install -U tox`
* Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
* Run the server: `tox -e runserver`
* Go to API docs: <http://127.0.0.1:8000/docs>
* Use the endpoint: `/game/pubg/stats`
* Upload the screenshot of the final scoreboard (the scoreboard you are presented with after the game has ended, not the ones inbetween rounds).
* Make sure the image is of decent quality.
* You should see a `200 OK` response like the following:

```json
[
  {
    "game_id": 5,
    "name": "[PYK] PYK-KOONSHY",
    "kill": 29,
    "assist": 4,
    "death": 15,
    "point": 4180,
    "created_at": "2024-07-06T09:10:44.425Z",
    "updated_at": "2024-07-06T09:10:44.425Z",
    "id": 17
  },
  {
    "game_id": 5,
    "name": "Esther-Blanchett",
    "kill": 34,
    "assist": 1,
    "death": 11,
    "point": 4880,
    "created_at": "2024-07-06T09:10:44.427Z",
    "updated_at": "2024-07-06T09:10:44.427Z",
    "id": 18
  },
  {
    "game_id": 5,
    "name": "[VIE] GauhuonGxinhdep",
    "kill": 24,
    "assist": 3,
    "death": 21,
    "point": 3550,
    "created_at": "2024-07-06T09:10:44.429Z",
    "updated_at": "2024-07-06T09:10:44.429Z",
    "id": 19
  },
  {
    "game_id": 5,
    "name": "55216",
    "kill": 30,
    "assist": 3,
    "death": 19,
    "point": 4510,
    "created_at": "2024-07-06T09:10:44.430Z",
    "updated_at": "2024-07-06T09:10:44.431Z",
    "id": 20
  },
  {
    "game_id": 5,
    "name": "Pacman_123",
    "kill": 25,
    "assist": 2,
    "death": 17,
    "point": 3620,
    "created_at": "2024-07-06T09:10:44.432Z",
    "updated_at": "2024-07-06T09:10:44.432Z",
    "id": 21
  },
  {
    "game_id": 5,
    "name": "[RL] Tej_93",
    "kill": 23,
    "assist": 3,
    "death": 21,
    "point": 3740,
    "created_at": "2024-07-06T09:10:44.434Z",
    "updated_at": "2024-07-06T09:10:44.434Z",
    "id": 22
  },
  {
    "game_id": 5,
    "name": "sdasdasdsadweqw",
    "kill": 21,
    "assist": 5,
    "death": 19,
    "point": 3350,
    "created_at": "2024-07-06T09:10:44.435Z",
    "updated_at": "2024-07-06T09:10:44.436Z",
    "id": 23
  },
  {
    "game_id": 5,
    "name": "ZXun-Du",
    "kill": 16,
    "assist": 2,
    "death": 16,
    "point": 2970,
    "created_at": "2024-07-06T09:10:44.437Z",
    "updated_at": "2024-07-06T09:10:44.437Z",
    "id": 24
  },
  {
    "game_id": 5,
    "name": "Bii-Su-Jhin",
    "kill": 13,
    "assist": 2,
    "death": 28,
    "point": 2360,
    "created_at": "2024-07-06T09:10:44.439Z",
    "updated_at": "2024-07-06T09:10:44.439Z",
    "id": 25
  },
  {
    "game_id": 5,
    "name": "JIngwei96",
    "kill": 10,
    "assist": 5,
    "death": 25,
    "point": 2490,
    "created_at": "2024-07-06T09:10:44.440Z",
    "updated_at": "2024-07-06T09:10:44.441Z",
    "id": 26
  },
  {
    "game_id": 5,
    "name": "bot_killer_bot",
    "kill": 12,
    "assist": 0,
    "death": 12,
    "point": 2130,
    "created_at": "2024-07-06T09:10:44.442Z",
    "updated_at": "2024-07-06T09:10:44.442Z",
    "id": 27
  },
  {
    "game_id": 5,
    "name": "Sixpeach6",
    "kill": 7,
    "assist": 4,
    "death": 18,
    "point": 2140,
    "created_at": "2024-07-06T09:10:44.444Z",
    "updated_at": "2024-07-06T09:10:44.444Z",
    "id": 28
  },
  {
    "game_id": 5,
    "name": "bvhjhjgv/ca",
    "kill": 7,
    "assist": 2,
    "death": 14,
    "point": 1720,
    "created_at": "2024-07-06T09:10:44.446Z",
    "updated_at": "2024-07-06T09:10:44.446Z",
    "id": 29
  }
]
```

* To see the changes reflected in the database: install [DB browser for SQLITE](https://sqlitebrowser.org/) and open the file `db.sqlite3` from root directory.
