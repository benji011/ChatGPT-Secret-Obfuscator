import click
from .replacers import replace_names
from .utils import read_file

@click.command()
@click.argument('filename')
@click.option('--output', '-o', default=None, help='Output file name')
def cli(filename, output):
    code = read_file(filename)
    modified_code = replace_names(code)
    click.echo(modified_code)
