# uv dev container ruff starter

This repo is a simple starter template to get you started with a devcontainer using Cursor.
You can clone it as is and click on "re-open in devcontainer" to get started. You will immediately have access to:
1. Deployment ready dockerized modern Python environment
2. Access to a Jupyter Notebook inside of VS-Code in that container
3. Access to run and debug your code in the container
4. Advanced linting and formatting (ruff + pylance) (Highlighting incorrect imports, accessing non-available properties, etc.)

It includes:

- Package management using uv and Python 3.13
- Dev Container setup with:
    - M1 support (running on amd64), I found a lot of packages don't properly support ARM
    - VSCode extensions to get you running
    - Jupyter Notebook support
    - Auto format on save (ruff)
    - Advanced linting (ruff + pylance)
    - Git / SSH support, forwarding the ssh agent to the container

## Running a FastAPI server locally
- Open a terminal in VS-Code / the container

```
gunicorn -k uvicorn.workers.UvicornWorker \
    -t $TIMEOUT \
    -w $UVI_WORKERS \
    --max-requests 1000 \
    --max-requests-jitter 50 \
    --bind "localhost:$PORT" \
    --preload \
    --graceful-timeout 600 \
    $FASTAPI_APP
```

## Enabling SSH/GitHub support
- On the host machine, run the ssh agent and make sure the correct key is loaded:
```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa # or the key you want to use
```
- That should be enough

## Running a Jupyter Notebook
- Just create a new notebook (I like to put them all in a folder called notebooks)
- Open it in VS-Code
- The first time you open it you need to select the Python environment:
    - Select the corner at the top right
    - Then click Python Environments...
    - Then select the conda environment: * conda (Python 3.13.1) /opt/conda/bin/python (Recommended)

## Running the Debugger
- Navigate to the file you want to run and debug
- Set your breakpoints in the file
- Click on the top right corner at the "play file", and click Python Debugger: Debug Python File
- Remember to use the "Debug Console" to manipulate variables and such

## Running from a remote machine 
- Open Vs-Code/Cursors
- cmd + shift + p => Remote-SSH: Connect to Host...
- Enter the host
- Using the Terminal, clone the Repo at the host (and add relevant secrets files)
- Open the folder in the container
- Everything should work the same out of the box (make sure the SSH-Agent is running on the server) it will be automatically forwarded if the Recommended local packages are installed.


## Next Steps:
- Adding a simple FastAPI server, with some best practices I have learned over the years
- Setting up a simple CI/CD pipeline using GitHub Actions and deploying to various cloud providers
- Setting up a simple logging monitoring observability stack
- Setting up a simple DB