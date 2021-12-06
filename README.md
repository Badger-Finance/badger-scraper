# badger-scraper
[![Test Run](https://github.com/Badger-Finance/badger-scraper/actions/workflows/test-run.yml/badge.svg)](https://github.com/Badger-Finance/badger-scraper/actions/workflows/test-run.yml)

## Scraper bot to validate Badger App DOM

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
