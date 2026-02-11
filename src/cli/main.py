import typer
from typing import List

app = typer.Typer()

@app.command()
def convert(input_file: str, output_format: str):
    """Convert an image to the specified format"""
    # Implementation for conversion logic goes here
    typer.echo(f'Converting {input_file} to {output_format}')

@app.command()
def batch_convert(input_files: List[str], output_format: str):
    """Convert multiple images to the specified format"""
    for input_file in input_files:
        convert(input_file, output_format)

if __name__ == '__main__':
    app()
