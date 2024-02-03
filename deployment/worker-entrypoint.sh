#!/bin/sh
celery -A core worker --beat -l INFO