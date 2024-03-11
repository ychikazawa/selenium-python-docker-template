# selenium-python-docker-template
Selenium + Python + Docker environment template.
This uses chrome driver.

## Requirement

- [Docker](https://www.docker.com/)

## Usage

Create .env file:

```shell
cp .env.example .env
```

Build & run container:

```shell
docker-compose up --build
```

Run script:

```shell
docker-compose exec app python app.py
```

### Jupyter Notebook

You can use jupyter for test.

http://localhost:8888/

### Example: selenium env

- Selenium Driver: http://localhost:4444
- noVNC Server: http://localhost:7900
  - default password: secret


## Licence

This software is released under the MIT License, see [LICENSE](https://github.com/Haru0517/python-docker-template/blob/master/LICENSE).

## Author

[Yuto Chikazawa](https://github.com/Haru0517)