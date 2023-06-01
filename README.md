# Sudoku Solver
Hey!

This is a Python program without external libraries, that solves Sudoku puzzles using a backtracking algorithm. Given an input Sudoku board, the program finds the solution by iteratively trying different numbers and [Backtracking](https://en.wikipedia.org/wiki/Backtracking).
## Prerequisites

Install Docker 
```sh
sudo apt update -y && sudo apt install docker.io
```
Install Docker Compose Plugin
```sh
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

```

## Usage
1. make sure you have docker installed.
2. Clone the repository to your local machine:
```sh
git clone https://github.com/oriavsapir/Sudoku-Solver.git
```
3. ``` docker run ```
