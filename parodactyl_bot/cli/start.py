import click


@click.group()
def run() -> None:
    """ Запустить один из выбранных сервисов """


@click.command()
def dev() -> None:
    pass
