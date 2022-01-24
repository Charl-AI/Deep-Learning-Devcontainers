<div align="center">

# Deep Learning Devcontainers

[![Blog](http://img.shields.io/badge/Blog-Post-c044ce.svg)](https://charl-ai.github.io/Deep-Learning-Devcontainers/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

Example devcontainer for Deep Learning projects. This repo contains a Dockerfile/devcontainer.json/requirements.txt combination to build a container for deep learning projects containing a collection of useful packages. A pre-built version of the image is stored on DockerHub, making it fast and easy to pull and use in your own projects. You can read more about why I think devcontainers are a great idea and the design decisions I made in the linked blog post.

## Do I need to install anything to use these containers?

Yes, you will need to have Docker with the Nvidia container runtime installed. Installation instructions can be found [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker). Depending on your setup, you might also need to have [rootless docker configured](https://docs.docker.com/engine/security/rootless/). I am also assuming that you have VScode with the remote development extension pack installed to take advantage of the Devcontainers feature (although you could go without it if you wanted to).

*You will need a GPU + drivers capable of CUDA 11.3 - you can check this by running nvidia-smi and ensuring CUDA Version = 11.3 or greater.*

## How do I use the pre-built image in my own projects?

Simply make a `devcontainer.json` file like the one in this project. Instead of having a 'build' section, it should have an 'image' section which specifies the container name + registry, e.g.

`"image": gcr/example`

Once you've made a `devcontainer.json` file, you can run `Remote Containers: Open folder in Container` from the VScode command palette to automatically pull the image and create a container.

Naturally, you can get a text file of the packages used in the image by doing `pip freeze > requirements.txt`. If you want to create a requirements file which only includes the packages you actually use, consider using a tool such as [pipreqs](https://pypi.org/project/pipreqs/).

## How do I make my own images?

I would recommend copying the `.devcontainer/` directory into your own project. You can then make any edits you want to the `Dockerfile` (e.g. changing the CUDA/Python versions you want to use in the container) and likewise for the `devcontainer.json` (you might want to change the default extensions, settings, build args etc...). You can then use your own `requirements.txt` file to specify which packages to include in the image. You can build the image and launch a container by running `Remote Containers: Open folder in Container` from the VScode command palette.

## How can I try out this environment?

Simply run `Remote containers: Clone Repository in Container Volume` to clone the repository in an isolated volume, build the image, and spin up a container.
