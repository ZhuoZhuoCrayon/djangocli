# djangocli
️🔧 djangocli is the standard tooling for Django development based on DRF.

[![Coverage Status](https://codecov.io/gh/ZhuoZhuoCrayon/djangocli/graph/badge.svg)](https://app.codecov.io/gh/ZhuoZhuoCrayon/djangocli)
[![Python unittest and codecov](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/python_unittest_and_codecov.yml/badge.svg)](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/python_unittest_and_codecov.yml)
[![Create release](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/release_2_create_release.yml/badge.svg)](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/release_2_create_release.yml)
[![Docker build and push](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/docker_build_push.yml/badge.svg)](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/docker_build_push.yml)
[![Release Helm Charts](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/release_helm_charts.yml/badge.svg)](https://github.com/ZhuoZhuoCrayon/djangocli/actions/workflows/release_helm_charts.yml)

![Release](https://badgen.net/github/release/ZhuoZhuoCrayon/djangocli)
![Latest tag](https://badgen.net/github/tag/ZhuoZhuoCrayon/djangocli)
![Issues](https://badgen.net/github/issues/ZhuoZhuoCrayon/djangocli)
![Prs](https://badgen.net/github/prs/ZhuoZhuoCrayon/djangocli)
![Last commit](https://badgen.net/github/last-commit/ZhuoZhuoCrayon/djangocli/0.5.x)

![Python](https://badgen.net/badge/python/%3E=3.6,%3C=3.9/green?icon=github)
![Django](https://badgen.net/badge/django/%3E=3.1.5,%3C=3.2.4/yellow?icon=github)

![License](https://badgen.net/github/license/ZhuoZhuoCrayon/djangocli)

---


## Why this project?

* In order to develop a Django project more efficiently
* Integrating Django best practices


## Getting started

### Kubernetes (🚀 Recommend)

[Use k8s to deploy applications](djangocli/docs/deploy/k8s.md)


### Basic image

We provide basic docker images of djangocli based on this [Dockerfile](scripts/services/k8s/images/app/Dockerfile)

You can get the latest image at [djangocli's DockerHub](https://hub.docker.com/repository/docker/caicrayon/djangocli)

### Docker Compose

We also provide [a sample of Docker Compose](scripts/services/docker/docker-compose.yml) to help you quickly run this project locally

## Release
[Version log](djangocli/docs/release/readme.md)

## License

[MIT](LICENSE)
