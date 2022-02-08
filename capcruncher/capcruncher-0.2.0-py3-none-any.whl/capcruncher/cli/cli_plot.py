import click 

@click.group()
def cli():
    """
    Generates plots for the outputs produced by CapCruncher.

    See subcommands for details
    """

@cli.command()
@click.argument("files", nargs=-1)
@click.option("-o", "--output_prefix", default="template", help='Output prefix for template file')
@click.option("-d", "--design_matrix", help='TSV file with the columns: sample condition')
@click.option("-v", "--viewpoint", help='Sets the template viewpoint')
@click.option("-b", "--binsize", help='Sets the template binsize')
def make_template(*args, **kwargs):
    """
    Generates a template for the supplied files. This can be edited to customise the plot.
    """

    from capcruncher.cli.plot import make_template
    make_template(*args, **kwargs)

@cli.command()
@click.option('-r', '--region', required=True, help='Genomic coordinates of the region to plot')
@click.option("-c", "--config", required=True, help='Configuration file generated by the make_template command')
@click.option("-o", "--output", default='capcruncher_plot.png')
@click.option("--x-axis", is_flag=True)
@click.option("--no-scale-bar", is_flag=True)
def make_plot(*args, **kwargs):
    """
    Generates a plot for the genomic region specified using the suplied configuration file.
    """
    from capcruncher.cli.plot import plot_reporters
    plot_reporters(*args, **kwargs)
