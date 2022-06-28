#!/usr/bin/env bash
wget https://github.com/h2oai/wave/releases/download/v0.22.0/wave-0.22.0-linux-amd64.tar.gz &&
mkdir wave && tar -xvf wave-0.22.0-linux-amd64.tar.gz -C wave --strip-components 1 &&
chmod +x wave/waved &&
rm wave-0.22.0-linux-amd64.tar.gz
