# Tests and visual review

Run from the repository root with an environment that already has the toolkit's
dependencies installed:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B examples/plot_gallery.py
```

No test framework needs installing: the suite uses Python's `unittest` and the
toolkit's existing dependencies. Nothing is downloaded. Tests import this checkout
of `Hunters_tools.py`; they use synthetic inputs, not scientific data files.
Until Stage 2 moves specialized imports, even simple tests require all dependencies
currently imported by the toolkit (see `requirements.txt`).

An `OK` at the end of the test command means every discovered test passed. A
failure shows the test name and expected/actual values. Keep that output when
reporting a problem. To run only numerical tests:

```sh
python3 -B -m unittest tests.test_numerical -v
```

The tests select Matplotlib's noninteractive Agg backend before importing the
toolkit. They restore plotting settings between tests, close figures, and export
test images to memory. Disposable Matplotlib configuration stays in ignored
`tests/.runtime-*` directories and is removed on normal process exit. Run tests in
a separate Python process rather than inside a session containing valuable plots.

## What the baseline protects

- Rebinning preserves integrated counts over the covered range, including unequal
  bin widths, partial overlaps, splitting, coarsening, identity, and empty ranges.
- Tally examples cover valid interior events, exact internal edges, event-index
  alignment, count uncertainties, generated edges, and normalization order.
- Small helpers cover known answers, zero conventions, strings, color conversion,
  nuclide conversion, and exact tab-delimited table formatting.
- Plot tests inspect line data, colors, labels, error-bar endpoints, scale/limits,
  center-based map orientation and inferred cell boundaries,
  figure ownership in the default path, and PNG/SVG rendering. They do not assert
  whole-image pixel equality, which can change with fonts and library versions.

These are representative checks, not comprehensive certification. Known bugs in
`MAINTENANCE_PLAN.md` are intentionally not required to pass as existing behavior.
In particular, tally overflow/final-edge handling (N01), combined width-normalized
uncertainties (N02), nonzero-velocity Lorentz gamma (N05), and malformed slugify
outputs (U08) need targeted tests when those repairs are implemented. No legacy
switch is added in Stage 1. Rebinning results remain unchanged.

## Review the gallery

Each run writes six PNG files and environment information into a **new** directory
under `examples/plot_output/`, ignored by Git. Previous runs are preserved for
comparison. Rendering errors terminate the command rather than silently omitting
a figure. The gallery uses direct `fig.savefig()` because repairs to the toolkit's
save helper are scheduled for Stage 2.
Exports use `bbox_inches='tight'` with external legends explicitly included in
`bbox_extra_artists`, preserving legends and colorbar labels. Tight bounds alone
cropped the legends in the initial gallery. A regression test now uses the same
export function as the gallery, checks that right-side and bottom legends fit
inside the saved PNG, and checks for drawn pixels in their image regions.
This does not change the toolkit's layout or interactive window behavior.

Editable `show_plots` and `save_plots` settings are near the top of the script.
To try zoom/pan and further interactive review locally, set `show_plots = True`
and run with an environment that has a working GUI backend. Keep `save_plots = True`
to retain images for comparison. Headless rendering does not test GUI interaction.

Review these features:

1. Curves: colors, markers, readable labels, and the external legend.
2. Errors: the bars and shaded band represent a constant absolute uncertainty
   of 0.25; check clipping and readability.
3. Log plot: both axes are logarithmic, with the requested limits.
4. Bins: boundaries are 0, 1, 3, 6; heights are counts 4, 8, 6, not densities.
5. Map pair: both plots describe the same cells using centers versus edges.
   Intended values are lower-left 1, lower-right 3, upper-left 2, upper-right 4.
   **The edge map currently exposes P12, an orientation bug.** Do not approve
   its current arrangement as the desired baseline. This is a review example,
   not a passing numerical assertion about the buggy path.

For feedback, give the figure name, the environment from its README, and what
should look or behave differently. Small edits to gallery data/settings can then
make that behavior reproducible before fixing it. Extend tests alongside fixes;
do not freeze unrelated accidental behavior simply to make the suite pass.

## Environment and automation

Initial local baseline: Python 3.14.2, NumPy 2.3.5, Matplotlib 3.10.8,
SciPy 1.16.3, Munch 4.0.0, lmfit 1.3.4. This records what was tested; it does not
declare minimum supported versions or pin runtime dependencies.

GitHub test automation is explicitly deferred until Stage 2 compatibility repairs
and agreement on supported Python/library versions. The separate documentation
workflow remains unchanged. A future test workflow should run this same unittest
command on the agreed older and current environments. Local success here does
not certify untested library releases.
