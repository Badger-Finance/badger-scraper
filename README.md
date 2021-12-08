# badger-scraper
[![Test Run](https://github.com/Badger-Finance/badger-scraper/actions/workflows/test-run.yml/badge.svg)](https://github.com/Badger-Finance/badger-scraper/actions/workflows/test-run.yml)

## Scraper bot to validate Badger App DOM

## Overview
There are two dockerfiles:
1. `Dockerfile`: For building the actual service
2. `ui.Dockerfile`: For building and running v2-ui instance in a separate container

It takes around 5 minutes to build UI container, so, scraper service should wait until UI instance responds with 
HTTP 200 and then it can perform content validations

## Installing
```shell
docker-compose build
```

## Running

```shell
docker-compose up
```
This will compare "https://app.badger.com" HTML content against the value URL in 
`BADGER_APP_COMPARE_URL` env var

## Env vars
Check `.env.example` for example.
- `CHROMEDRIVER_PATH` - PATH to docker chromedriver executable. Default is 
`/usr/local/bin/chromedriver` for Docker runtime
- `DISCORD_WEBHOOK_URL` set this so message to discord will be sent
- `BADGER_APP_COMPARE_URL` - website to compare prod badger.app
- `V2_UI_READ_TOKEN` - GH token to be used to clone UI repo
