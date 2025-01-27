#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./deploy.sh

This script deploys the service in the production server.'
    exit
fi

cd "$(dirname "$0")"

main() {
    # check venv is enabled
    if [[ -z "${VIRTUAL_ENV}" ]]; then
        exit
    fi

    # make sure linting checks pass
    make lint

    # static
    python manage.py collectstatic --noinput

    # make sure latest requirements are installed
    pip install -U pip
    pip install -r requirements.txt

    # make sure tests pass
    make test

    # push origin srht
    git push -v origin main

    # push on github
    git push -v github main

    # pull on server and reload
    ssh deploy@95.217.30.133 'cd /var/www/mataroa ' \
        '&& git pull ' \
        '&& source .venv/bin/activate ' \
        '&& pip install -U pip ' \
        '&& pip install -r requirements.txt ' \
        '&& python manage.py collectstatic --noinput ' \
        '&& source .envrc && python manage.py migrate ' \
        '&& sudo systemctl reload mataroa.uwsgi'
}

main "$@"
