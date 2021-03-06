<p align="center">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg">
</p>
<p align="center">
  <a href="https://travis-ci.com/vishakha-lall/MapBot">
    <img alt="Travis CI Build Status" src="https://travis-ci.com/vishakha-lall/MapBot.svg?branch=gssoc-master">
  </a>
  <a href="https://github.com/vishakha-lall/MapBot/">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/vishakha-lall/MapBot?color=darkblue&label=%20&logo=github">
  </a>
</p>
<hr>
<p align="center">
  <a href="http://t.me/ChristopherMapbot">
    <img alt="Telegram Bot" src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="15%"">
  </a>
  <a href="https://christopher-mapbot.herokuapp.com/">
    <img alt="Heroku App" src="https://user-images.githubusercontent.com/39518771/82949337-0cc59000-9fc1-11ea-94b6-f7e31d18e805.jpg" width="35%" >
  </a>
  <a href="http://m.me/christophermapbot">
    <img alt="Messenger Bot" src="https://user-images.githubusercontent.com/39518771/83188624-a15cf900-a14d-11ea-8359-72dac011eb6f.png" width="15%" >
  </a>
</p>
<hr>

# MapBot :earth_africa:

#### Hey! I'm your friendly navigator bot! Try me out, not to brag but I'm FUN!



### What I do?

I aim to give users a new way to interact with Google Maps through engaging text-based conversational interfaces.

### How old am I?

I'm only a baby bot right now, I need you to feed me with logic, data and inspiration.

### What is the motivation behind building me?

The primary motivation of the developers of MapBot is to provide a playground to tech enthusiasts, both beginners and advanced to try algorithms, approaches and ideas while contributing to a real-life project.

### What I aspire to be one day?

- I want to help users in the most comprehensive way.
- I want to give 'geeks' a platform to try out all things 'cool'.

------

### Are you here for GSSoC 2020?

Check out all related information [here](GSSoC.md)

------

### What are some pre-requisites?

- PostgreSQL
  - Install the Core Distribution of PostgreSQL from the [official PostgreSQL downloads page](https://www.postgresql.org/download/)
  - Reference videos for installation:
    - For Linux: [YouTube](https://www.youtube.com/watch?v=-LwI4HMR_Eg)
    - For Windows: [YouTube](https://www.youtube.com/watch?v=e1MwsT5FJRQ)
    - For macOS: [YouTube](https://www.youtube.com/watch?v=5AOkxqFaYEE)
  - Create a password for user `postgres`
  - Create a database named `mapbot`:
    - `psql -U postgres -h localhost`
    - Enter the password when prompted.
    - Execute SQL: `CREATE DATABASE mapbot;`
-----

### Setting Up

<details>
<summary><strong>How to set me up on CLI?</strong></summary>
<br>

- Clone the repository
- Verify existence of the **mapbot** database in PostgreSQL
- Run `git update-index --assume-unchanged ENV/.env`
- Fill the existing template in `ENV/.env` with the corresponding values following the `KEY=VALUE` format
- Install dependencies from `requirements.txt` file. Run `pip install -r requirements.txt`
- You're all set up, run the `init.py` file. `python init.py`
- It is recommended that you set this project up in a virtual environment to keep the dependencies separated and for easier debugging. Here's how you can do that -
    1. [Python](https://realpython.com/python-virtual-environments-a-primer/#why-the-need-for-virtual-environments)
    2. [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

</details>

------

<details>
<summary><strong>How to use me with an UI?</strong></summary>
<br>

- Want to set up the UI locally? Head to the [other branch](https://github.com/vishakha-lall/MapBot/tree/gssoc-master).
- Want the cloud hosted UI?
  - Wake me up at [Heroku UI](https://christopher-mapbot.herokuapp.com/)
  - Once I'm awake, happy interacting.

</details>

------

<details>
<summary><strong>How to deploy on Docker?</strong></summary>
<br>

#### What are some pre-requisites? (with Docker)

- Docker
  - Take a look at [this](https://docs.docker.com/install/) for detailed installation instructions for Docker on Windows, Linux and Mac systems.
  - Verify the installations by `docker --version` and `docker-compose --version`

#### How to set me up Docker style?
- Clone the repository
- Fill up the `GCLOUD_API_KEY` in `ENV/docker.env`
- Run `docker-compose up`
- Visit `localhost:5000` to interact with the deployment

</details>

------

<details>
<summary><strong>How to use me on Telegram?</strong></summary>
<br>

- Want to create your own Telegram Bot? Head to the [other branch](https://github.com/vishakha-lall/MapBot/tree/gssoc-master).
- Want to use a cloud hosted version of me?
  - Hit me up at my telegram bot username [@ChristopherMapbot](http://t.me/ChristopherMapbot) to initiate a chat.
  - P.S.: I generally sleep when unused. So, may need some time to answer the first text
  - Just type "Bye" in the chat to let me know you're done and I'll get back to sleep.

</details>

------

<details>
<summary><strong>How to set me up on Slack?</strong></summary>
<br>

- Clone the repository
- Verify existence of the **mapbot** database in PostgreSQL
- Run `git update-index --assume-unchanged ENV/.env`
- Fill the existing template in `ENV/.env` with the corresponding values following the `KEY=VALUE` format
- Follow the steps prompted [here](https://api.slack.com/apps?new_classic_app=1) to create a **classic** slack app. Navigate to **Basic Information** section of the slack app. Under the **Add features and functionality** subheading click on **Bots**. Click on **Add Legacy Bot User** and enter the **display name** and **default username** of your bot. Navigate to **Basic Information** section of the slack app on the sidebar and copy the **Client ID** and **Client Secret** and then paste these to the `ENV/.env` file as: `SLACK_CLIENT_ID=<Your Client ID>` and `SLACK_CLIENT_SECRET=<Your Client Secret>`. Navigate to the **OAuth & Permissions** section. Under the **Redirect URLs** subheading add `http://localhost:5000/post_auth`.
- Install dependencies from `requirements.txt` file. Run `pip install -r requirements.txt`
- Run `python app.py`. The server will start at your localhost. Navigate to `http://localhost:5000/begin_auth`. Click `Add to Slack` button. Select the workspace from the top right and hit `Allow`. Successfully completing this step would automate the creation of  `SLACK_BOT_TOKEN` in the `ENV/.env` file.
- In another terminal, run `python slackbot.py`.
- Open the workspace in Slack and invite the bot to the channel: `@YOUR_BOT_DEFAULT_USERNAME` message in the channel. Click on **Invite to Channel**.

</details>

------

<details>
<summary><strong>How to use me on Messenger?</strong></summary>
<br>

- Want to create your own Messenger Bot? Head to the [other branch](https://github.com/vishakha-lall/MapBot/tree/gssoc-master).
- Want to use a cloud hosted version of me?
  - Hit me up on [Messenger](http://m.me/christophermapbot) to initiate a chat.
  - P.S.: I generally sleep when unused. So, may need some time to answer the first text.
  - Just type "Bye" in the chat to let me know you're done and I'll get back to sleep.

</details>

------

### How do I work?

The `/analysis` folder contains data files for the project. The `sentences.csv` contains the base training dataset which is used to classify the user's input into three classes - *Statement*, *Question*, and *Chat*. Going through some examples would clarify the difference between statement and chat. The `featuresDump.csv` is the result of text pre-processing done using the code in `features.py` and `featuresDump.py`.

------
### Want to see me in action?

Here's a [Medium article](http://bit.ly/39Y9WCq) with the some superficial explanations, there are some video links too!
