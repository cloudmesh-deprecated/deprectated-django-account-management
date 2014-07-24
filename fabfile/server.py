from fabric.api import task, local
import sys

@task
def mongo():
    """start the mongo server"""
    local("mongod --noauth --dbpath . --port 27777")

@task
def install():
    """install the server"""
    local("python setup.py install")

@task
def start():
    """install the server"""
    install()
    local("cd cloudmesh_django; make server ")


	
