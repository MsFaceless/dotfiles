from invoke import Exit
from invocations.console import confirm

from fabric import task

with open("target_config", "r") as f:
    for line in f.read():
        if "HOST=" in line:
            print(line)
            host = line.split("HOST=")[-1].strip()
        elif "USER=" in line:
            print(line)
            user = line.split("USER=")[-1].strip()
print(user, host)
my_hosts = ["{0}@{1}".format(user, host)]

@task
def test(c):
    result = c.local("./manage.py test my_app", warn=True)
    if not result and not confirm("Tests failed. Continue anyway?"):
        raise Exit("Aborting at user request.")

@task
def commit(c):
    c.local("git add -p && git commit")

@task
def push(c):
    c.local("git push")

@task
def prepare_deploy(c):
    test(c)
    commit(c)
    push(c)

@task(hosts=my_hosts)
def deploy(c):
    code_dir = "/srv/django/myproject"
    if not c.run("test -d {}".format(code_dir), warn=True):
        cmd = "git clone user@vcshost:/path/to/repo/.git {}"
        c.run(cmd.format(code_dir))
    c.run("cd {} && git pull".format(code_dir))
    c.run("cd {} && touch app.wsgi".format(code_dir))
