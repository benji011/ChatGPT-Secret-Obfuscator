import click
from .replacers import replace_names
from .utils import read_file

@click.command()
@click.argument('filename')
def cli(filename):
    print("Before ---------------------------------------------------")
    code = read_file(filename)
    click.echo(code)

    print("After ---------------------------------------------------")
    modified_code = replace_names(code)
    click.echo(modified_code)
    print("---------------------------------------------------")
