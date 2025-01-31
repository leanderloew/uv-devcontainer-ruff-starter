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


## Questions:
- Why micromamba and not uv?
    - In a scientific context you often need to install packages with binary requirements that are published through conda. Micromamba is (mostly) conda compliant and almost as fast as uv. If uv would ever support conda packages, I would switch.
- Why docker?
    - I have experimented with all sorts of environment managers and at the end of the day you always have to install some complicated dependencies and ship the whole thing - nothing beats a dockerized environment.
- Why all that linting?
    - I'm not a perfectionist, but a big believer in the value of typed code, especially now that we have AI assistance and the small overhead of typing is negligible.

## Background
After 8 years working with Python, I have set up hundreds of environments and it was a pain every time. What starts simple often ends up as a mess. However, as a result, setting up an environment with this project brings me absolute joy. Yes it's opinionated, and yes it's highly specific to VS-Code / Cursors, but I'm so happy with it I wanted to share it.

Some small delightful things: I used to set up JP-servers in docker compose and I could never get it to remember to auto-import local dependencies - this is automatically done here using the jupyter.runStartupCommands :)
Even setting up small things like, did I point to the right python path? Can I import my local dependencies? etc... it was always a pain.
I'm also a strong believer in having the absolute exact same dev environment as the deployment environment (even if this means having to ship a slightly larger docker image to prod).

Another thing that is nicely solved here is bringing your own base container. This was another big pain, e.g. I try to install a complicated package like seleniumbase - an absolute pain. Now I can just use their provided docker image and build my project on top of it, while still having all the necessary packages guaranteed and the exact same micromamba env every time :)

I'm sure there are many more things I'm missing, but I'm happy with the result and I hope you will be too.

## Next Steps:
- Adding a simple FastAPI server, with some best practices I have learned over the years
- Setting up a simple CI/CD pipeline using GitHub Actions and deploying to various cloud providers
- Setting up a simple logging monitoring observability stack
- Setting up a simple DB