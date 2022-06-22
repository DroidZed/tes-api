#! /bin/zsh

if [[ $1 == 'dev' ]] || [[ $# == 0 ]] then
    pdm run python3 main.py
fi
