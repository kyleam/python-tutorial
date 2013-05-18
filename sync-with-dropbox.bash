#!/usr/bin/env bash
src="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
dest=$HOME/dropbox-gmail/Dropbox/public/python-tutorials

for pdf in *.pdf; do
    if ! [[ -e "$dest/$pdf" ]]; then
        ln -s  $src/$pdf $dest/$pdf
    fi
done

if ! [[ -e "$dest/data" ]]; then
    ln -s "$src/data" "$dest/data"
fi
