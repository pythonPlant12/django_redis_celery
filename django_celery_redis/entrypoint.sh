#!/bin/ash

# First line is a Unix special start point where I indicate the 
# interpeter used for this entrypoint script, as I will run alpine,
# instead of using bash, I'll use ash 
echo "Apply database migrations"
python manage.py migrate

# This command is to execute all the commands inside of entrypoing
# It is a common practise to add this line at the end of this file
exec"$@"