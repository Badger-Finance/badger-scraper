#!/bin/bash
until $(curl --output /dev/null -vfs http://localhost:3000); do
    printf '.'
    sleep 10
done