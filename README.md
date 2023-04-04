# Tiny Redis
## Redis In-Memory Database Implementation in Python

This is an implementation for [CodeCrafters.io](https://codecrafters.io) [Build you own Redis challenge](https://codecrafters.io/challenges/redis).

[![progress-banner](https://app.codecrafters.io/progress/redis/053a4d30-bb2a-4d3b-bfe5-12a9b6aa2b34)](https://app.codecrafters.io/users/a7medayman6)

## Implemented Features

- [x] PING
- [x] ECHO
- [x] SET
- [x] GET
- [x] EXPIARY
- [ ] Storing on disk
- [ ] Save Commands
- [ ] Load Commands from file

## How to Run

- Python >= 3.8 installed
- Clone the repository
```bash
git clone https://github.com/a7medayman6/Tiny-Redis/
```
- Spawn a redis server
```bash
./spaw_redis_server.sh
```

## Test it

- Install Redis-cli
  - [How to Install Redis CLI Without Installing Redis Server](https://redis.com/blog/get-redis-cli-without-installing-redis-server/)
- Run redis commands using redis cli while the server is running.
```bash
redis-cli PING
# PONG

redis-cli ECHO hello world
# hello world

redis-cli SET x 5
# OK

redis-cli GET x
# 5

redis-cli SET y 6 px 10
# OK
```
