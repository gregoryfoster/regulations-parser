import logging
from regparser.tree.depth.derive import derive_depths

import click

logger = logging.getLogger(__name__)


@click.command()
@click.argument('markers', type=click.STRING, required=True)
def outline_depths(markers) -> None:
    """
    Infer an outline's structure.
    Return a list of outline depths for a given list of space-separated markers.
    """

    # Input is space-separated.
    marker_list = markers.split(' ')
    all_solutions = derive_depths(marker_list, [])
    depths = {tuple(str(a.depth) for a in s) for s in all_solutions}.pop()

    # Expected output is space-separated.
    formatted_output = ' '.join(depths)

    print(formatted_output)


if __name__ == '__main__':
    """Enable running this command directly. E.g.,
    `$ python regparser/commands/outline_depths.py`. This can save 1.5 seconds
    or more of startup time.
    """
    outline_depths()
