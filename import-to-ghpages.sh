#!/usr/bin/env bash

git checkout -q master || exit 1
git branch -Dq gh-pages || exit 1
masterid=$(git log --pretty=format:'%h' -n1)
ghp-import -m"master: $masterid" output
