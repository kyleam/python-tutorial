#!/usr/bin/env bash
src="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
dest=$HOME/dropbox-gmail/Dropbox/public/python-tutorials

srcdirs=( doc data code )

for dir in ${srcdirs[@]}; do
    if ! [[ -e "$dest/$dir" ]]; then
        ln -s "$src/$dir" "$dest/$dir"
    fi
done
