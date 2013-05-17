#!/usr/bin/env bash
src="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
dest=$HOME/dropbox-gmail/Dropbox/public/python-tutorials

for pdf in *.pdf; do
    ln -sf  $src/$pdf $dest/$pdf
done
