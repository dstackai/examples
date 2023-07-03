# Examples

Welcome to `dstack-examples`. This repository contains a collection of examples
demonstrating how to use `dstack`.

## 1. Setup

```shell
pip install dstack
dstack start
```

The `dstack start` command starts the Hub server, creating the default project that runs dev environments, pipelines,
and apps locally.

## 2. Projects

To run examples in the cloud (AWS, GCP, Azure),
make sure to create the corresponding [project](https://dstack.ai/docs/guides/projects/)
via the UI.

## 3. Clone the repo

```shell
git clone https://github.com/dstackai/dstack-examples
cd dstack-examples
dstack init
```

## 4. Profiles

Every example may have different GPU and memory requirements.
Before running examples, make sure to configure a [profile](https://dstack.ai/docs/#defining-profiles) with required
resources.

## 5. Run examples

| Example                                  | How to run                                         |
|------------------------------------------|----------------------------------------------------|
| **Run dev environment**                  | `dstack run .`                                     |
| **Run FastAPI demo**                     | `dstack run fastapi-app --reload`                  |
| **Train MNIST model**                    | `dstack run mnist-train`                           |
| **Train MNIST model (with Tensorboard)** | `dstack run mnist-train-tensorboard`               |
| **Run Stable Diffusion demo**            | `dstack run stable-diffusion-app --reload` |
| **Run Dolly Chatbot**                    | `dstack run dolly-chatbot --reload`        |
| **Run XGen Chatbot**                     | `dstack run xgen-chatbot --reload`         |