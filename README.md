# GymJam

## Setup

To setup this project on a standard Unix/Linux environment follow these steps:

### Install `pyenv`

Install [pyenv](https://github.com/pyenv/pyenv) to manage python versions and environments.

```bash
# Install pyenv - https://github.com/pyenv/pyenv-installer
curl https://pyenv.run | bash
```

Afterwards, add the following to your `~/.bashrc` file:

```bash
export PATH=\"$HOME/.pyenv/bin:$PATH\"
eval \"$(pyenv init -)\"
eval \"\\n$(pyenv virtualenv-init -)\"
```

Source your `~/.bashrc` or open a new shell

```bash
source ~/.bashrc
```

Install Python 3.6.3 using `pyenv` at the user level:

```bash
pyenv install 3.6.3
```

Create a virtualenv for the project called `lunarlander`

```bash
pyenv virtualenv 3.6.3 lunarlander
```

Activate the virtualenv

```bash
pyenv activate lunarlander
```

### Install OpenAI Gym

Making sure that the virtualenv has been loader, install `gym` from repository using pip from the repository

```bash
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
```

Then install the `box2d` environment required by `LunarLander-v2`

```bash
pip install -e '.[box2d]'
```

## Run

### Single run

Assuming the virtualenv `lunarlander` has been loaded (if not, run `pyenv activate lunarlander`) run the `lunarlandercolab.py` script:

```bash
python lunarlander.py
```

### Batch Jobs

To run the job on HPC:

```bash
sbatch runscript.sh
```
