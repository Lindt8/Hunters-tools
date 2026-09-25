"""Generate small synthetic figures for manual review; see tests/README.md."""

from pathlib import Path
import sys
import os
import tempfile

# Editable settings. Each run creates a new directory, preserving earlier images.
show_plots = False
save_plots = True
output_root = Path(__file__).resolve().parent / 'plot_output'

# Use this checkout even when Hunters_tools is also on PYTHONPATH.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def generate_figures():
    """Return named (figure, axes) pairs, using fresh data for every example."""
    import numpy as np
    import Hunters_tools as ht

    figures = {}
    x = np.linspace(1, 10, 12)
    figures['01_lines'] = ht.fancy_plot(
        [x, x], [2 + np.sin(x), 3 + np.cos(x)], figi=1,
        x_scale='linear', y_scale='linear', linestyle='-',
        data_labels=['2 + sin(x)', '3 + cos(x)'],
        title_str='Synthetic curves', x_label_str='Time (s)', y_label_str='Signal (a.u.)')

    figures['02_errors'] = ht.fancy_plot(
        [x], [2 + np.sqrt(x)], yerr_lists=[np.full(x.shape, .25)], figi=2,
        x_scale='linear', y_scale='linear', linestyle='-', errorstyle='bar-band',
        title_str='Absolute uncertainty: 0.25', x_label_str='Time (s)',
        y_label_str='Signal (a.u.)')

    figures['03_log'] = ht.fancy_plot(
        [x], [x**2], figi=3, linestyle='-',
        x_limits=[.8, 12], y_limits=[.8, 150],
        title_str='Log scales: y = x squared', x_label_str='x (a.u.)', y_label_str='y (a.u.)')

    bar_x, bar_y = ht.generate_line_bar_coordinates([0, 1, 3, 6], [4, 8, 6])
    figures['04_bins'] = ht.fancy_plot(
        [bar_x], [bar_y], figi=4, x_scale='linear', y_scale='linear',
        linestyle='-', marker='', title_str='Unequal bin widths',
        x_label_str='Position (cm)', y_label_str='Counts per bin')

    # z[x_index, y_index]: columns have y centers 1 and 3; rows x centers 1 and 3.
    # Intended lower-left=1, lower-right=3, upper-left=2, upper-right=4.
    # The explicit-edge example currently exposes known issue P12. Keep it
    # visible for review, but do not assert the incorrect orientation in tests.
    for number, name, coordinates in [(5, 'map_centers', [1., 3.]),
                                      (6, 'map_edges_known_P12', [0., 2., 4.])]:
        figures[f'{number:02d}_{name}'] = ht.fancy_3D_plot(
            [coordinates.copy()], [coordinates.copy()], [np.array([[1., 2.], [3., 4.]])],
            plot_styles='map_pcolormesh', figi=number,
            title_str=name.replace('_', ' '), x_label_str='x (cm)', y_label_str='y (cm)',
            z_label_str='Cell value', linewidth=0)
    return figures


def main():
    output_root.mkdir(parents=True, exist_ok=True)
    # A temporary configuration keeps these examples from writing to the user's
    # global Matplotlib configuration directory. It is removed after rendering.
    with tempfile.TemporaryDirectory(prefix='.mpl-', dir=output_root) as config_dir:
        os.environ['MPLCONFIGDIR'] = config_dir
        import matplotlib
        if not show_plots:
            matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import importlib.metadata

        with matplotlib.rc_context():
            try:
                figures = generate_figures()
                if save_plots:
                    output_dir = Path(tempfile.mkdtemp(prefix='gallery-', dir=output_root))
                    for name, (fig, ax) in figures.items():
                        fig.savefig(output_dir / (name + '.png'), dpi=120, bbox_inches='tight')
                    versions = '\n'.join(
                        f'{package}: {importlib.metadata.version(package)}'
                        for package in ('numpy', 'matplotlib', 'scipy', 'munch', 'lmfit'))
                    (output_dir / 'README.txt').write_text(
                        f'Python: {sys.version}\n{versions}\n\n'
                        'Review instructions: tests/README.md\n'
                        'P12: map centers and edges should show identical cells.\n'
                        'Expected lower-left=1, lower-right=3, upper-left=2, upper-right=4.\n'
                        'The explicit-edge map currently disagrees; this is a known bug.\n',
                        encoding='utf-8')
                    print(f'Gallery saved to {output_dir}')
                if show_plots:
                    plt.show()
            finally:
                plt.close('all')


if __name__ == '__main__':
    main()
