#!/bin/bash
LOGFILE=/home/deploy/www/BooksApp/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
USER=deploy
ADDRESS=sztosz.tk:8887
source /home/deploy/venv/books/bin/activate
cd /home/deploy/www/BooksApp
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w ${NUM_WORKERS} --bind=${ADDRESS} --user=${USER} \
	--log-level=error --log-file=${LOGFILE} 2>>${LOGFILE} BooksApp.wsgi:application
