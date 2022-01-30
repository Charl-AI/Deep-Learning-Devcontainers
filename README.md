<div align="center">

# Deep Learning Devcontainers

[![Blog](http://img.shields.io/badge/Blog-Post-c044ce.svg)](https://charl-ai.github.io/Deep-Learning-Devcontainers/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

Example devcontainer for Deep Learning projects. This repo contains a Dockerfile/devcontainer.json/requirements.txt combination to build a container for deep learning projects containing a collection of useful packages. You can read more about why I think devcontainers are a great idea and the design decisions I made in the linked blog post.

## Do I need to install anything to use these containers?

Yes, you will need to have Docker with the Nvidia container runtime installed. Installation instructions can be found [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker). Depending on your setup, you might also need to have [rootless docker configured](https://docs.docker.com/engine/security/rootless/). I am also assuming that you have VScode with the remote development extension pack installed to take advantage of the Devcontainers feature.

## How can I try out this environment?

Simply run `Remote containers: Clone Repository in Container Volume` from the VScode command palette to clone the repository in an isolated volume, build the image, and spin up a container. Alternatively, you can clone the repository normally and run `Remote containers: Open Folder in Container` - I sometimes find the second method to be a bit more reliable.

## What does this example container do?

This container gives you a Ubuntu 20.04 environment with CUDA 11.3, Python 3.8 and the packages from the `requirements.txt` file. The `main.py` file simply includes some code for checking that the deep learning libraries installed can successfully see your GPU.

*You will need a GPU + drivers capable of CUDA 11.3 - you can check this by running nvidia-smi and ensuring CUDA Version = 11.3 or greater.*

## How can I containerise my own projects?

If your project uses python virtual environments with a requirements.txt file, all you will need to do is copy the `.devcontainer` directory from this project into your own project. You can then make any adjustments you want to the `Dockerfile` and `devcontainer.json`. I wrote an [accompanying blog post](https://charl-ai.github.io/Deep-Learning-Devcontainers/) explaining some relevant concepts for this.
