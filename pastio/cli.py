import click
from .user import User
from .settings import Settings


@click.command('register')
def register():
    pass

@click.group()
@click.option('--user')
@click.option('--password')
def cli(user, password):
    if not (user and password):
        user_name = Settings.get('user_name')
        password = Settings.get('password')
    else:
        user_name = user
        password = password
    User.login(user_name, password)


@cli.command("in")
@click.argument("data", type=click.File("r"), default='-')
def copy(data):
    User.copy_to_cloud(data.read())


@cli.command("out")
def paste():
    click.echo(User.get_from_cloud())


@cli.group("history")
def history():
    pass


@history.command("show")
@click.option('-v', '--verbose', is_flag=True, default=False)
def history_show(verbose):
    for record in User.get_history():
        if verbose:
            click.echo("{time:30} {host:20} {value}".format(**record))
        else:
            click.echo("{}".format(record.get('value')))


@history.command("wipe")
def wipe():
    User.wipe()
