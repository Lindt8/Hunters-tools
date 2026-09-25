import copy
import io
import unittest

from tests.support import ht, matplotlib, np, plt


class PlottingTests(unittest.TestCase):
    def setUp(self):
        self.settings = matplotlib.rc_context()
        self.settings.__enter__()
        self.addCleanup(self.settings.__exit__, None, None, None)
        self.addCleanup(plt.close, 'all')

    def assert_renders(self, fig):
        fig.canvas.draw()
        for file_format in ('png', 'svg'):
            with self.subTest(file_format=file_format), io.BytesIO() as output:
                fig.savefig(output, format=file_format)
                self.assertGreater(output.tell(), 100)

    def test_multiple_lines_labels_colors_and_no_mutation(self):
        x = [[1., 2., 4.], [1., 3., 4.]]
        y = [[2., 4., 3.], [3., 2., 5.]]
        before = copy.deepcopy((x, y))
        fig, ax = ht.fancy_plot(x, y, x_scale='linear', y_scale='linear',
                               color=['#123456', '#654321'], linestyle='-',
                               data_labels=['First', 'Second'], title_str='Synthetic lines',
                               x_label_str='Time (s)', y_label_str='Signal (a.u.)')
        self.assertIs(ax.figure, fig)
        self.assertEqual(len(ax.lines), 2)
        for i, line in enumerate(ax.lines):
            np.testing.assert_array_equal(line.get_xdata(), x[i])
            np.testing.assert_array_equal(line.get_ydata(), y[i])
        self.assertEqual([line.get_color() for line in ax.lines], ['#123456', '#654321'])
        self.assertEqual([t.get_text() for t in ax.get_legend().get_texts()], ['First', 'Second'])
        self.assertEqual(ax.get_xlabel(), 'Time (s)')
        self.assertEqual(ax.get_ylabel(), 'Signal (a.u.)')
        self.assertEqual(ax.get_title(), 'Synthetic lines')
        self.assertEqual((x, y), before)
        self.assert_renders(fig)

    def test_symmetric_absolute_error_bars(self):
        fig, ax = ht.fancy_plot([[1., 2., 3.]], [[2., 4., 6.]],
                               yerr_lists=[[.2, .4, .6]], errorstyle='bar',
                               x_scale='linear', y_scale='linear')
        self.assertEqual(len(ax.containers), 1)
        bars = ax.containers[0].lines[2][0]
        np.testing.assert_allclose(bars.get_segments(),
                                   [[[1, 1.8], [1, 2.2]], [[2, 3.6], [2, 4.4]],
                                    [[3, 5.4], [3, 6.6]]])
        self.assert_renders(fig)

    def test_logarithmic_scales_and_explicit_limits(self):
        fig, ax = ht.fancy_plot([[1., 10., 100.]], [[1., 4., 9.]],
                               x_limits=[.5, 200], y_limits=[.1, 20])
        self.assertEqual(ax.get_xscale(), 'log')
        self.assertEqual(ax.get_yscale(), 'log')
        np.testing.assert_allclose(ax.get_xlim(), [.5, 200])
        np.testing.assert_allclose(ax.get_ylim(), [.1, 20])
        self.assert_renders(fig)

    def test_map_center_coordinates_and_orientation(self):
        # z is indexed [x, y]; QuadMesh stores display rows [y, x].
        # Unequal off-diagonal values expose accidental transposition.
        fig, ax = ht.fancy_3D_plot(
            [[1., 3.]], [[1., 3.]], [np.array([[1., 2.], [3., 4.]])],
            plot_styles='map_pcolormesh', linewidth=0)
        mesh = ax.collections[0]
        np.testing.assert_array_equal(mesh.get_array(), [[1, 3], [2, 4]])
        coordinates = mesh.get_coordinates()
        np.testing.assert_allclose(coordinates[0, :, 0], [0, 2, 4])
        np.testing.assert_allclose(coordinates[:, 0, 1], [0, 2, 4])
        self.assert_renders(fig)
