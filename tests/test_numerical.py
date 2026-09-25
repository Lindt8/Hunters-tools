import unittest

from tests.support import ht, np


class RebinnerTests(unittest.TestCase):
    # Values are counts per bin, distributed uniformly within each input bin.
    # They are NOT densities. Widths are deliberately unequal.
    def setUp(self):
        self.edges = np.array([0., 1., 3., 6.])
        self.counts = np.array([4., 8., 6.])

    def test_identity_and_no_input_mutation(self):
        edges_before = self.edges.copy()
        counts_before = self.counts.copy()
        result = ht.rebinner(self.edges, self.edges, self.counts)
        np.testing.assert_array_equal(result, self.counts)
        np.testing.assert_array_equal(self.edges, edges_before)
        np.testing.assert_array_equal(self.counts, counts_before)

    def test_nonuniform_overlap_and_conservation(self):
        output_edges = np.array([0., .5, 2., 4., 6.])
        before = output_edges.copy()
        result = ht.rebinner(output_edges, self.edges, self.counts)
        # Densities in the three input bins are 4, 4, and 2 counts/unit.
        np.testing.assert_allclose(result, [2., 6., 6., 4.], rtol=1e-13)
        self.assertAlmostEqual(result.sum(), self.counts.sum())
        np.testing.assert_array_equal(output_edges, before)

    def test_coarsening(self):
        np.testing.assert_allclose(ht.rebinner([0, 3, 6], self.edges, self.counts), [12, 6])

    def test_partial_range_and_empty_outer_bins(self):
        np.testing.assert_allclose(ht.rebinner([.5, 2, 4], self.edges, self.counts), [6, 6])
        np.testing.assert_allclose(
            ht.rebinner([-2, -1, 0, 6, 7], self.edges, self.counts), [0, 0, 18, 0])

    def test_split_single_bin(self):
        np.testing.assert_allclose(ht.rebinner([0, 1, 3, 4], [0, 4], [8]), [2, 4, 2])


class TallyTests(unittest.TestCase):
    # Interior events avoid known overflow/final-edge inconsistencies (N01).
    # These valid examples protect the return contract for later legacy work.
    data = [.25, .75, 1., 1.5, 2.5, 2.75]
    edges = [0, 1, 3]

    def test_counts_uncertainties_and_event_indices(self):
        for include_indices in (False, True):
            with self.subTest(include_indices=include_indices):
                result = ht.tally(self.data, bin_edges=self.edges,
                                  return_uncertainties=True,
                                  return_event_indices_histogram=include_indices)
                self.assertEqual(len(result), 4 if include_indices else 3)
                counts, edges, errors = result[:3]
                np.testing.assert_array_equal(counts, [2, 4])
                np.testing.assert_array_equal(edges, self.edges)
                np.testing.assert_allclose(errors, [np.sqrt(2), 2])
                if include_indices:
                    self.assertEqual(result[3], [[0, 1], [2, 3, 4, 5]])

    def test_width_scaling_with_absolute_errors(self):
        counts, _, errors = ht.tally(self.data, bin_edges=self.edges,
                                     divide_by_bin_width=True, scaling_factor=3,
                                     return_uncertainties=True)
        np.testing.assert_allclose(counts, [6, 6])
        np.testing.assert_allclose(errors, [3*np.sqrt(2), 3])

    def test_normalization_after_width_before_scaling(self):
        # Deliberately omit uncertainties: combined width/normalization errors
        # are a known bug (N02), not a behavior to freeze into this baseline.
        for mode, expected in [('unity-sum', [1.5, 1.5]), ('unity-max-val', [3, 3])]:
            with self.subTest(normalization=mode):
                counts, _ = ht.tally(self.data, bin_edges=self.edges,
                                     divide_by_bin_width=True,
                                     normalization=mode, scaling_factor=3)
                np.testing.assert_allclose(counts, expected)

    def test_generated_edges(self):
        for settings in ({'nbins': 3}, {'bin_width': 1}):
            with self.subTest(settings=settings):
                counts, edges = ht.tally(self.data, min_bin_left_edge=0,
                                         max_bin_right_edge=3, **settings)
                np.testing.assert_array_equal(edges, [0, 1, 2, 3])
                np.testing.assert_array_equal(counts, [2, 2, 2])


class SmallFunctionTests(unittest.TestCase):
    def test_search_and_safe_quotient(self):
        self.assertEqual(ht.find('a', ['b', 'a', 'a']), 1)
        self.assertIsNone(ht.find('c', ['a', 'b']))
        self.assertEqual(ht.quotient(6, 2), 3)
        self.assertEqual(ht.quotient(6, 0), 0)
        self.assertEqual(ht.quotient(0, 0), 0)

    def test_count_error_roundtrip_and_zero_convention(self):
        self.assertEqual(ht.N_to_relative_error(0), 0)
        self.assertEqual(ht.relative_error_to_N(0), 0)
        self.assertAlmostEqual(ht.N_to_relative_error(25), .2)
        self.assertAlmostEqual(ht.relative_error_to_N(.2), 25)

    def test_lorentz_energy_and_rest(self):
        self.assertEqual(ht.Lorentz_gamma(0), 1)
        self.assertEqual(ht.Lorentz_B2_from_Tn(0), 0)
        # At kinetic energy equal to the documented neutron rest energy,
        # gamma = 2 and beta^2 = 3/4. Nonzero-velocity gamma awaits N05 repair.
        self.assertAlmostEqual(ht.Lorentz_B2_from_Tn(939.5654133), .75)

    def test_color_conversion(self):
        self.assertEqual(ht.hex_to_rgb('#ff8000', opacity=.5), (255, 128, 0, .5))
        np.testing.assert_allclose(ht.hex_to_rgb('#ff8000', out_of_one=True),
                                   [1, 128/255, 0, 1])
        self.assertEqual(ht.rgb_to_hex((255, 128, 0)), '#ff8000')

    def test_slugify_working_text(self):
        # Initial lowercase b and escaped whitespace cases await U08 repair.
        self.assertEqual(ht.slugify('Café sample -- 12'), 'cafe-sample-12')

    def test_nuclide_roundtrip(self):
        self.assertEqual(ht.nuclide_plain_str_to_ZZZAAAM('Co-60'), 270600)
        self.assertEqual(ht.ZZZAAAM_to_nuclide_plain_str(270600), 'Co-60')

    def test_tab_delimited_float_table(self):
        result = ht.Excel_table_generator([[1.25, 2.5], [3., 4.]],
                                          title='Synthetic', float_formatting='{:.2f}')
        self.assertEqual(result, 'Synthetic\n1.25\t2.50\n3.00\t4.00\n')

    def test_bar_coordinates_without_errors(self):
        x, y = ht.generate_line_bar_coordinates([0, 1, 3], [4, 8])
        self.assertEqual(x, [0, 0, 1, 1, 3, 3])
        self.assertEqual(y, [0, 4, 4, 8, 8, 0])
