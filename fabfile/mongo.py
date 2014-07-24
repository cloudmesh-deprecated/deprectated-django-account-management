from fabric.api import task, local
import sys

@task
def start():
    """start the mongo server"""
	local("mongod --noauth --dbpath . --port 27777")
