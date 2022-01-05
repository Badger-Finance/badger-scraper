#!/bin/bash
timeout 15m serve -s ./build
if [ $? -eq 124 ]
then
    echo "Successfully served UI for 15 min"
fi