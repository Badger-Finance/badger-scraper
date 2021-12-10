#!/bin/bash
until $(curl -f --silent http://localhost:3000); do
    printf '.'
    sleep 10
done