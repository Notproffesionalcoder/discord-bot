# Discord Bot (Simple Heroku Connect)

A simple/basic Discord Bot written in python that can be easily deployed onto heroku with minimal implementations.

## Cloud Hosting (Heroku)

- Create a [GitHub Account](https://github.com/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) and a [Heroku Account](https://signup.heroku.com).
- In GitHub `Fork` [this repository](https://github.com/TheYoBots/discord-bot).
- Create a [new app](https://dashboard.heroku.com/new-app) in Heroku and select a suitable name for your app (region won't really matter).
- In your newly created heroku app, go to the `Deploy` tab and under `Deployment method` select `GitHub (Connect to GitHub)`.
- Then Click on `search` and select (`connect`) your fork of this repository.
- Now choose the `master` branch and click on `Enable Automatic Deploys` and then click `Deploy branch` with the `master` branch selected.
- Now wait for the deployment to complete and once it is done go to the `Resources` tab and enable `worker (python bot/main.py)` dynos (If you don't see anything to enable, refresh your page and you will be able to see it).
- Finally go to your `Settings` tab and then under `Config Vars` click on `Reveal Config Vars` and then in the place of `key` type in `TOKEN` and in the place of `value` add your Discord Bot Token.
- Now your Discord Bot is up and running, cloud hosted onto Heroku!

## Hostless

To run this Discord Bot locally in your own terminal, then you'll simply have to run `python bot/main.py` to this code and replace `TOKEN` in the `bot/main.py` file with your Discord Bot Token.

## Features

- Bot Prefix: `!`
- Bot Support: `!support`
- Bot Commands: `!test`, `!source`, `!say <value>`, `!ping`, `!meme`, `!guessthenumber`
  - `!test`: To check whether to bot is working in your server.
  - `!source`: Source Code of the Discord Bot.
  - `!say <value>`: Tell the Bot to say something. For example, `!say hi` will mike the Bot say, "{Author} says hi".
  - `!ping`: Gives the latency of the author in ms.
  - `!meme`: Generates a random (child safe) meme from dank memers `hot` category memes (https://www.reddit.com/r/dankmemes/new.json?sort=hot).
  - `!guessthenumber`: A game where you'll have to guess the number (from 1 to 10) that the Bot is thinking of.

