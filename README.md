# python-efg-template
A template repository to track python logs into Grafana, through Fluentd.

## Prerequisites

In order to use this repository, you should be familiar with base concepts of these topics:

- Python
- Elasticsearch
- Grafana
- FluentD
- Docker

## Repo structure

- `.devcontainer` → folder for devcontainer.json configuration file. Here you can find basic configurations for you VSCode devcontainer environment. If you want to use it, make sure your Docker Desktop is running, type `Ctrl+Shift+P` inside VSCode window and select for `Dev Containers: Rebuild and Reopen in Container`. VSCode will automatically open the same view of your project, but inside e a container.
- `app` → here the python code whose logs you want to track.
- `cli` → .sh scripts to initialize your dev environment. If you are working in a devcontainer, these scripts will be run automatically.
- `logstash` → this folder contains the `logstash.conf` configuration file. Please check the official documentation to dive deeper.
- `compose.yaml` → docker-compose file to start EFG and Python services.
- `Dockerfile` → to build your Python app service.

## How to use it

### Local

Inside your terminal window, move under your project path and run the following commands:

```bash
pip install -r requirements.txt
docker compose up -d --build
```

### DevContainer

If you activated devcontainer all should be set up. At the start of your devcontainer, docker automatically runs the cli/start.sh file, which starts all compose services.

Just keep in mind that now you are running docker containers inside a docker container, so you won’t be able to see those in your docker desktop. If you want to check the status of python services you must do it through command line, with commands like:

```bash
docker ps --all
docker logs <CONTAINER_ID>
```

### Check logs

> ⚠️ This is the same for both local and devcontainer development

Now that all compose services are up and running, next step is to check your python logs inside the Grafana dashboard.

Inside your browser, go to **`http://localhost:3000`** IP address, you will be redirected to the Grafana login page.<br>
Once you are here, follow these steps:

1. Login with default credentials (you will asked to change password after first login):
    - username: admin
    - password: admin
2. On the left burger menu, go under `Connections` section and click on `Data sources`. Then click on the button `Add data source`. We now want to add Elasticsearch as our log data-source.
3. In the search-bar look for Elasticsearch and click on the below result. Now you have to configure your elastic connection.
4. In the name field, put the name you want to give to this data-source (you can leave the default as for now)
5. In the url box, put this: `http://elasticsearch:9200`. The host name must match the service name you put in the compose file for the elasticsearch service.
6. Set `Index name` box to `fluentd-*`, then leave every other setup as default.
7. Click on `Save & test`
8. Open again the burger menu, click on the `Dashboard` section, then the `Create dashboard` button, then the `Add visualization` button.
9. It will open a new dashboard, asking you to choose the data-source. Select the elasticsearch you created before.
10. Now your dashboard is ready. To check python logs, follow these steps:
    1. In the below `query` tab, select the `Logs` query type
    2. Activate the `Table view` toggle above the page

    You'll see a table with all your python log messages, with the `@timestamp`. Move the cursor to the right of the table to see the `message` column with the printed message.
11. Save your dashboard with the `save` button on the right of the page.

If everything went right, you'll see your new dashboard. Follow the image below to check log messages from the created dashboard.

![alt text](images/Dashboard%20data.png)

## Implement your own python app

As for now you just worked with a basic example of python app, but you are encouraged to implement your own. Just put your code inside `./app` folder.
