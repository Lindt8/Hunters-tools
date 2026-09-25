# Hunters_tools maintenance plan

Last updated: 2026-09-25

## Current status and next action

- [x] Review the documentation workflow and library compatibility.
- [x] Perform a second, bug-focused review with small synthetic examples.
- [x] Record findings, preservation requirements, and implementation stages here.
- [x] Stage 1 local implementation: establish a small regression suite and plotting gallery.
- [ ] Stage 1 user visual review and authorized commit/push checkpoint.

**Stage 1 tests and examples are implemented; toolkit behavior is unchanged.**
`Hunters_tools.py` has not been edited. There are 21 passing synthetic tests and
a six-figure gallery, with instructions in `tests/README.md`. No packages were
installed and no network access, commits, or pushes were performed in Stage 1.

Next action: review the gallery locally, then commit/push Stage 1 when authorized.
Stage 2 follows that checkpoint; do not start its repairs implicitly. At each
session, read this plan and the applicable AGENTS.md instructions, inspect the
working tree, and preserve unrelated changes. Update this document at each
completed checkpoint.

## Scope and behavior requirements

- Keep the deployable toolkit as one `Hunters_tools.py` file. Tests, examples,
  and maintenance notes may live separately in the repository and must not
  become runtime dependencies.
- Preserve the author's recognizable style, function-description docstrings,
  public interfaces, return structures, defaults, and successful behavior unless
  a change corrects an established bug or is explicitly agreed upon.
- Prefer small, reviewable repairs. No broad refactor, packaging migration,
  documentation replacement, or new `v2` functions is planned.
- Preserve the pdoc3 HTML documentation process.
- Preserve intentional plot styling, manual layout, external legends, padding
  conventions, and useful workarounds. Unusual code alone is not evidence of a
  bug. Check comments, examples, history, and observable behavior first.
- Keep `np`, `plt`, and existing compatibility aliases available for scripts
  using `from Hunters_tools import *`. Do not introduce a restrictive `__all__`
  or remove other exported names without considering downstream usage.
- Moving specialized imports into their functions and making Munch optional
  are agreed directions. When Munch is installed, preserve its existing return
  behavior. When absent, use the intended ordinary-dictionary fallback.
- Do not change scientific reference data or numerical conventions merely to
  modernize them. Separate arithmetic defects from choices needing discussion.
- No packages are to be installed without permission. Network access was
  approved for the review's official-source and GitHub checks; do not treat that
  as authorization for unrelated network activity.
- No commit or push is authorized by the request to begin Stage 1 implementation.

### Usage priorities

Actively used functions include `fancy_plot()` and companions, table generators,
`slugify()`, `tally()`, `rebinner()`, the Lorentz helpers, string formatting and
manipulation, and other small utilities. Low-risk, well-established fixes to
these small functions should be addressed early rather than deferred simply
because they are not plotting functions.

`fancy_3D_plot()` is used less often partly because it is fragile; stabilizing it
is worthwhile after the more frequently used paths.

Ignore the `MC_tools/` directory. Transport parsers and material helpers still
inside `Hunters_tools.py` may be legacy functions superseded by PHITS-Tools or
DCHAIN-Tools. Record defects, but ask about continued use before investing in
substantive repairs. Do not modify those separate dependency repositories.
Treat unfinished experiments such as `energy_resolution_of_peak()` as deferred
new functionality, not automatic bug-fix scope.

### Special rules for tally and rebinner

- The author has high confidence that `rebinner()` works as designed. The review
  found no demonstrated result bug, and a synthetic interval-overlap check
  agreed with its output. **Preserve its results.** Establish regression tests
  first; do not rewrite the algorithm or change counts into densities.
- If a genuine discrepancy with `rebinner()`'s documented intent is later
  demonstrated, discuss the example and intended result before implementation.
- `tally()` and `rebinner()` support older analyses where reproducing previous
  results matters. Do not make `v2` replacements.
- If an agreed result-changing repair requires compatibility support, the author
  accepts an optional `legacy_mode=False` argument. Corrected behavior would be
  the default; `legacy_mode=True` would reproduce the relevant old behavior.
  Add the parameter without breaking existing positional calls, document the
  differences, and test both paths.
- This is permission for that compatibility approach, **not a requirement to
  change either function or add an unnecessary switch**. In particular,
  `rebinner()` has no planned numerical change or legacy switch at present.
- Preserve `tally()`'s existing normalization meanings. Correcting its scaling
  implementation must not silently introduce a different statistical treatment
  of normalized-bin covariance.

## Testing approach

Establish testing in Stage 1 and grow it with every repair. Start with Python's
built-in `unittest`; a new test framework dependency is not necessary.

All tests must generate their own small synthetic data or contain short,
hard-coded examples. Do not rely on private datasets, external services, PHITS
installations, or large calculations. Parser tests, if later approved, should
use minimal fixtures with provenance and known array-axis meanings.

Use three complementary layers:

1. **Numerical and text regression tests:** known answers, suitable floating-point
   tolerances, exact text where appropriate, conservation checks, and round trips.
   Preserve valid existing outputs. Do not turn known bugs into required behavior
   except in explicitly supported legacy-mode tests.
2. **Plot structure and rendering tests:** use a noninteractive backend; check
   plotted data, error artists, colors, labels, axes ownership, limits, map
   orientation, and absence of caller-data mutation. Actually draw and export
   representative figures, using in-memory output where practical. Close figures
   and isolate global plotting settings between tests.
3. **A reproducible visual gallery:** a separate example script generates a small
   set of plots from synthetic inputs. The author runs it locally and reviews
   appearance, layout, and interactive behavior. Automated success does not
   replace this feedback. Gallery output should not overwrite user figures or
   clutter tracked source files.

Avoid strict whole-image pixel comparisons initially: fonts, backends, and
Matplotlib versions can produce harmless differences. Use structural assertions
and selected visual review to protect the recognizable style. Add image
comparisons later only where they provide a concrete benefit.

For each repair, reproduce the failure, add a focused regression test, implement
the smallest suitable change, and rerun the relevant existing checks. Do not
commit a deliberately failing default suite simply to inventory all known bugs;
this document holds the unresolved findings.

Once the initial checks work locally, run the same automated suite in a separate
GitHub Actions workflow. Include an older supported environment and a current
one once their supported versions are agreed. Keep docs generation separate.

## Implementation stages and stopping points

Every stage follows: **apply the bounded changes -> run checks -> review the
result -> commit and push when authorized -> verify checks/docs -> update this
plan -> pause or explicitly continue**. Record the commit and any remaining
limitations below. A stage may use multiple small commits if its changes prove
too large to review together.

After a push that regenerates documentation, account for the automation's new
commit before the next push. Do not overwrite or rewrite remote history.

### Stage 1 — Test foundation and visual examples

- [x] Add a small passing suite for representative existing working behavior.
- [x] Cover `rebinner()` conservation and nonuniform-bin overlap without changing
      its implementation; establish examples for `tally()` compatibility work.
- [x] Add a synthetic plotting gallery, including asymmetric maps that expose
      orientation errors, and clear instructions for running tests/examples.
- [x] Record the baseline environment and distinguish known failures from
      established behavior.
- [x] Add GitHub test automation once local checks are dependable, or explicitly
      record its deferral. Keep the existing documentation workflow.
- [ ] Commit/push checkpoint; verify automation and update this plan.

Exit condition: a reproducible baseline exists without changing function results.
Commit(s): pending.

Local validation (2026-09-25): `python3 -B -m unittest discover -s tests -v`
passed all 21 tests. The gallery rendered all six PNGs. Representative visual
inspection confirmed the known P12 map discrepancy; the center-map test checks
the intended orientation, while the edge-map defect remains an explicitly labeled
review example. PNG and SVG rendering are exercised in automated plot tests.
The environment matches the review baseline listed below. Gallery exports use
tight bounds to retain external colorbar labels and legends; no runtime layout
code was changed. Interactive GUI behavior and the author's visual acceptance
remain pending.

GitHub automation is explicitly deferred until Stage 2 compatibility repairs
and agreement on supported versions. No workflow or dependency changes were
made. Tests/examples remain separate from the single-file runtime toolkit.

### Stage 2 — Compatibility, specialized imports, and small obvious fixes

- [ ] Replace removed colormap, NumPy scalar-alias, and canvas-title APIs.
- [ ] Move specialized imports locally and make Munch optional, checking exported
      names and behavior with the relevant optional dependencies absent.
- [ ] Repair `slugify()`, small-increment rounding, SI conversion, straightforward
      nuclide/string defects, and invalid element lookup fall-through.
- [ ] Repair figure-save path/fallback handling and the first bar uncertainty.
- [ ] Add regression tests alongside each fix and update affected docstrings.
- [ ] Commit/push checkpoint; verify tests/docs and update this plan.

Exit condition: these focused repairs work while ordinary existing examples and
wildcard-import usage remain compatible. Split imports, compatibility, and
utility fixes into separate commits if that makes review clearer.
Commit(s): pending.

### Stage 3 — fancy_plot and plotting companions

- [ ] Normalize supported single/multiple datasets, dictionaries, lists, arrays,
      and optional uncertainty inputs without flattening ragged datasets.
- [ ] Correct per-dataset errors/colors and asymmetric-list error bands.
- [ ] Honor supplied figures/axes and retain intended repeated-call behavior.
- [ ] Correct finite/logarithmic extrema while preserving normal padding and
      the current intentional suppression of custom x-bound padding.
- [ ] Repair secondary-axis updates and check error-box/colorbar behavior.
- [ ] Review the gallery with the author for legends, manual layout, bounds,
      styling, and interactive changes. Do not restore disabled experiments.
- [ ] Commit/push checkpoint; verify tests/docs and update this plan.

Exit condition: equivalent supported input forms produce equivalent results,
and normal plots retain their appearance. Input handling and bounds/companions
are natural separate commits within this stage.
Commit(s): pending.

### Stage 4 — Table generation

- [ ] Preserve heterogeneous values until formatting; handle NumPy numeric types.
- [ ] Correct numeric headers, varying row spans, and row-zero horizontal rules.
- [ ] Correct named colormaps and floating-point color working arrays.
- [ ] Define and test logarithmic zero handling and constant-value colors.
- [ ] Preserve Excel/LaTeX structure and existing keyword spellings, including
      `coulmn_formatting`.
- [ ] Commit/push checkpoint; verify tests/docs and update this plan.

Exit condition: exact-output tests cover working tables and repaired examples;
color computations no longer silently lose valid cells.
Commit(s): pending.

### Stage 5 — Histograms, time, geometry, and Lorentz helpers

- [ ] Correct `tally()` edge/overflow consistency and uncertainty scaling.
- [ ] Identify the exact old behaviors requiring `legacy_mode`; test both modes
      if result-changing repairs are implemented.
- [ ] Keep `rebinner()` unchanged unless a demonstrated defect is discussed and
      an explicit behavior decision is made.
- [ ] Fix time-format terminal cases; agree on year-duration conventions before
      changing year/day decomposition.
- [ ] Repair circumcenter handling of valid horizontal/vertical-side triangles.
- [ ] Correct the vacuum-light-speed use in `Lorentz_gamma()` with known-answer
      checks and an explicit note about the numerical change.
- [ ] Clarify `circ_solid_angle()`'s intended geometry before any generalization.
- [ ] Commit/push checkpoint; verify tests/docs and update this plan.

Exit condition: independent calculations agree, histogram modes have documented
behavior, and compatibility-sensitive changes are explicit.
Commit(s): pending.

### Stage 6 — Distribution fitting and statistics

- [ ] Correct custom-model evaluation, supported distribution names, and list
      input handling.
- [ ] Correct width initialization, distribution-specific metadata, and p-value
      text. Resolve FWHM meaning for custom models and double Gaussians.
- [ ] Agree on chi-squared interpretation and preserve the distinction between
      shape comparison, absolute predictions, and uncertainty-weighted residuals.
- [ ] Make parameter counts, returned degrees of freedom, statistics, and
      p-values consistent with that interpretation.
- [ ] Keep the experimental lmfit branch disabled unless its repair is needed.
- [ ] Commit/push checkpoint; verify tests/docs and update this plan.

Exit condition: synthetic fits recover the intended model; reported metadata
and statistical quantities agree with independent checks and documented meaning.
Commit(s): pending.

### Stage 7 — Stabilize fancy_3D_plot

- [ ] Correct dataset shapes, map center/edge orientation, and input-list mutation.
- [ ] Repair zero-valued limits, face-color arrays, trisurfaces, and contour
      colorbar failures.
- [ ] Separate native 2D-map log axes from manual 3D coordinate transformations.
- [ ] Check supported styles, clipping, colormap normalization, legends, and
      square/rectangular datasets using distinguishable synthetic patterns.
- [ ] Preserve intentional 3D styling; keep custom minor-grid classes disabled.
- [ ] Review representative plots with the author.
- [ ] Commit/push checkpoint; verify tests/docs and update this plan.

Exit condition: supported styles render correctly without changing data
orientation, corrupting caller inputs, or misrepresenting logarithmic positions.
Commit(s): pending.

## Findings register

All entries below are **open** unless explicitly marked otherwise. “Reproduced”
means observed in a small runtime check during the review; “inspection” means
the code establishes the concern but full behavior/fixtures need more work.
Line numbers are deliberately omitted because they will drift; use function
names and code descriptions to locate findings.

### Compatibility and imports

| ID | Finding | Evidence / treatment |
| --- | --- | --- |
| C01 | `get_colormap()` uses `cm.get_cmap`, removed in Matplotlib 3.11. | Deprecation reproduced on 3.10.8; removal verified in official notes. Use supported lookup. |
| C02 | `np.float` remains in the 3D colorbar formatter and legacy parsers. | Scientific-notation colorbar failure reproduced; replace with built-in `float`. |
| C03 | `fancy_save_plot()` calls removed canvas `get_window_title()`. | Untitled-figure failure reproduced. Use manager API with a real final fallback. |
| C04 | Array truth checks and comparisons to empty-list sentinels fail. | Reproduced for plot inputs/colors and empty arrays. Normalize inputs and test absence explicitly. |
| C05 | Custom 3D axes use obsolete constructors/methods. | Already disabled. No need to restore them in early stages. |
| C06 | Private colorbar/3D attributes are fragile; error-box autoscaling changed in Matplotlib 3.11. | Inspect `sm._A`, private surface-color copies, `_axinfo`, and collection bounds. Do not remove working hacks indiscriminately. |
| C07 | Eager specialized imports make unrelated functions require SciPy/lmfit/Munch. | Inspection. Make imports local where appropriate while considering exported names. |

### Plotting and saving

| ID | Finding | Evidence / treatment |
| --- | --- | --- |
| P01 | A flat single y-dataset is wrapped but its corresponding x input is not. | Reproduced dimension error; nested input works. |
| P02 | `fancy_plot()` overwrites supplied `ax` using current-figure `plt.subplot`. | Reproduced returned figure/axes belonging to different figures. |
| P03 | Uncertainty presence is controlled by the first dataset. | `[[], [.1,.2,.3]]` silently suppresses errors on the second dataset. |
| P04 | The first color's automatic-color sentinel controls other datasets. | `['#FDFEFC','red']` ignores red; reversing the order renders the sentinel literally. |
| P05 | Asymmetric error lists are indexed as NumPy arrays. | Reproduced tuple-indexing error with nested lists. |
| P06 | Dictionary input plus empty positional lists fails; dictionary key validation combines `elinewidth, capsize` into one string. | Reproduced crash and false warnings; individual settings are actually applied. |
| P07 | Log limits use nonpositive values and fixed initial extrema. | Mixed signed data fail; values near `1e-20` produce bounds extending toward `1e-14`. Preserve normal padding rules when fixing extrema. |
| P08 | Secondary log-axis ticks remain fixed after changing primary limits. | Reproduced limits moving to `[1000,100000]` with old `[1,3,10,30,100]` ticks. |
| P09 | `fancy_save_plot()` does not normalize a string directory to `Path`. | Reproduced without writing figures by mocking `savefig`. |
| P10 | `generate_line_bar_coordinates()` initializes an uncertainty using `yvals[0]`. | Reproduced count 10 appearing where uncertainty 1 belongs. |
| P11 | Flat NumPy z-data are converted to an unwrapped list in `fancy_3D_plot()`. | Reproduced failure interpreting individual numbers as datasets. |
| P12 | Edge-coordinate map shape inference can incorrectly transpose square data. | The same asymmetric cell values render differently with corresponding centers versus edges. |
| P13 | Automatic 3D transposition replaces entries in the caller's dataset list. | Reproduced external entry shape changing from `(2,3)` to `(3,2)`. |
| P14 | 2D-map x/y log coordinates are transformed before setting native log axes. | Reproduced `[10,100,1000]` becoming log coordinates on an already-logarithmic axis. |
| P15 | Zero-valued clipping bounds are treated as absent. | Reproduced negative z-values remaining with lower bound zero and `OoB_z_handling='limits'`. |
| P16 | NumPy face-color arrays fail whole-array comparisons to `None`. | Reproduced. |
| P17 | Trisurface paths access nonexistent `_facecolors3d` / `_edgecolors3d`. | Reproduced `AttributeError`; evaluate retiring the old legend workaround. |
| P18 | Line-contour colorbars can have `solids=None`. | Reproduced `map_contour` failure on unconditional `set_edgecolor`. |

### Tables and utilities

| ID | Finding | Evidence / treatment |
| --- | --- | --- |
| U01 | Named LaTeX colormaps reference `cmap` before assignment. | Reproduced with `colormap='viridis'`; use the provided `colormap`. |
| U02 | Color work arrays retain integer dtype. | NaN assignment fails; fractional transforms can truncate. Use a float working copy. |
| U03 | Zero/constant logarithmic color normalization loses valid cells. | `[0.,1.,10.]` produced no colored cells; constant data divide by zero. Define constant-range behavior. |
| U04 | Mixed table inputs coerce numeric values to strings; float32 formatting is skipped. | Reproduced ignored formatting in Excel output. Preserve types until formatting. |
| U05 | LaTeX multirow logic indexes a span by header-column index. | Headers `['A','B']`, spans `[1,2]` lose B's grouping. |
| U06 | `hline_row_indices=0` is ignored; numeric column headers fail concatenation. | Reproduced both; `[0]` is the current workaround for the first. |
| U07 | Small-increment rounding is truncated by a near-integer heuristic. | Upward rounding `.0011` to `.001` and downward rounding `.0029` to `.001` both return zero. |
| U08 | `slugify()` retains an extra bytes-prefix b and fails on empty input. | `'banana'` becomes `'bbanana'`; empty input raises `IndexError`. Preserve normal slug conventions. |
| U09 | SI conversion has invalid calls/indexing, reversed exponent subtraction, and an invalid-target error path. | Inspection plus reproduced failures. Kilo to base units must multiply by 1000. |
| U10 | Time formatters have terminal-case and year/day decomposition errors. | Subsecond/zero `single_largest` fails; four Julian years in `single_integer` returns `0s`; mixed output can contain negative days. |
| U11 | Invalid element symbols fall through as index -1. | `'Qq'` returns Oganesson or mass 294 after a warning. |
| U12 | `nuclide_to_Latex_form()` leaves `symbol` undefined for string Z; natural-element parsing fails. | Inspection of first; `'natFe'` loses Fe and `'Fe-nat'` raises `IndexError`. Normal isotope round trips passed. |

### Numerical methods and statistics

| ID | Finding | Evidence / treatment |
| --- | --- | --- |
| N01 | `tally()` paths differ on overflow and the final bin edge. | Reproduced count changes when enabling event-index output. Preserve reproducibility through agreed legacy support. |
| N02 | `tally()` uncertainties and values use different normalization factors after width division. | Reproduced; compute and apply consistent scaling factors. |
| N03 | `rebinner()` result change proposed? **No.** | Independent overlap check passed; author confirms intended behavior. Add tests, preserve implementation/results. |
| N04 | `circumcenter()` divides by a horizontal-side slope denominator. | Triangle `(0,0),(1,0),(0,1)` raises division by zero. |
| N05 | `Lorentz_gamma()` uses light speed in air. | Reproduced NaN at `0.9999` times vacuum c; use the vacuum constant for the Lorentz factor. |
| N06 | `circ_solid_angle()` has an unstated restricted geometry. | Its cone formula is appropriate for symmetric on-axis geometry, not a general off-axis disk. Clarify intended domain before changing results. |
| N07 | `r_squared()` / `chi_squared()` reject documented plain-list inputs. | Reproduced. |
| N08 | Custom fits optimize one model but return values from a named built-in model. | Quadratic parameters recovered near `(2,3,4)`, then Gaussian y-values and incorrect R-squared returned. |
| N09 | Distribution-name validation rejects logistic after lowercasing; initial sigma is variance. | Logistic rejection reproduced; variance initialization established by inspection. |
| N10 | Gaussian FWHM is used for other distributions. | Implemented sech with sigma 1 has FWHM about 5.2678, but reports 2.3548. Composite/custom-model metadata needs an explicit definition. |
| N11 | Ordinary p-value text is never formatted. | Reproduced literal `p = {:4g}`. |
| N12 | Chi-squared returns N-p degrees of freedom while its SciPy call uses N-1-p; double-Gaussian fits hard-code three parameters. | Inspection and runtime checks. Choose the statistical interpretation before a coordinated correction; the normalization itself is not inherently wrong. |
| N13 | Disabled lmfit branch confuses integrated-area amplitude with peak height. | Source/docs verified; keep disabled unless needed. |

### Deferred legacy findings

- `parse_tally_dump_file()`: default dataframe return uses undefined `pd`;
  reproduced. ASCII directional records omit `rho`; reproduced argument-count
  failure. Azimuth uses position coordinates despite the direction-angle
  description; review intent before changing it.
- `parse_ttrack_file()` / `parse_dyld_files()`: removed `np.float` calls and
  potential mesh-dimension/indexing defects. Require representative fixtures and
  a decision about maintaining these old copies before substantive changes.
- `fetch_MC_material()`: machine-specific path assumptions and an error path
  continuing without a library file; depends on the excluded legacy directory.
- `energy_resolution_of_peak()`: a stub returning `None`, not a completed feature.

## Behavior-sensitive decisions still open

- Year-duration convention and supported negative-duration behavior.
- Constant-valued table colors and logarithmic zero/nonpositive handling.
- Chi-squared interpretation and meaningful metadata for custom/composite fits.
- Exact `tally()` legacy behavior to preserve for result-changing repairs.
- Whether any legacy transport functions need continued maintenance here.
- Minimum supported Python/library versions for automated compatibility checks.

Preserve for now: suppression of custom x-bound padding, manual plot layout,
automatic-color sentinel semantics, y-band priority when both error directions
exist, documented zero conventions in small helpers, and the disabled status
of experimental plotting/fitting branches.

## Documentation automation and review evidence

`.github/workflows/docs.yml` runs on pushes to `master` changing
`Hunters_tools.py` or `docs/build_docs.py`. It uses Python 3.10 and
`pdoc3==0.10.0`, builds `docs/index.html`, and commits it back with
`Auto-update docs [skip ci]`. Changes only to requirements or the workflow do
not currently trigger this job. Its dependency installation uses `|| true`;
consider removing that failure suppression when maintaining CI.

The latest reviewed [Generate Docs run](https://github.com/Lindt8/Hunters-tools/actions/runs/23118436305)
and [Pages deployment](https://github.com/Lindt8/Hunters-tools/actions/runs/23118440563)
succeeded on 2026-03-15. A successful docs build is not a functional test and,
with Python 3.10, does not exercise the newest library releases.

Review runtime: Python 3.14.2, NumPy 2.3.5, Matplotlib 3.10.8, SciPy 1.16.3,
lmfit 1.3.4, Munch 4.0.0. Newer-library findings were checked against official
release notes, not an upgraded local environment. The script parsed with
`SyntaxWarning` treated as an error. Selected plot paths were rendered using a
noninteractive backend; save-helper failures were checked without writing user
figures. These checks are not exhaustive scientific validation. Reference-table
lengths/energy ordering were checked, not their physical source values.

Useful references:

- [Matplotlib 3.11 API changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.11.0.html)
- [Matplotlib 3.6 API changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html)
- [NumPy 1.24 expired deprecations](https://numpy.org/doc/stable/release/1.24.0-notes.html#expired-deprecations)
- [NumPy 2.2 empty-array truth checks](https://numpy.org/doc/stable/release/2.2.0-notes.html#expired-deprecations)
- [SciPy interp1d: legacy, with no current removal plan](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html)
- [SciPy chisquare definitions and assumptions](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
- [lmfit GaussianModel amplitude convention](https://lmfit.github.io/lmfit-py/builtin_models.html#gaussianmodel)
- [Vacuum speed of light in relativity](https://www.einstein-online.info/en/explandict/speed-of-light/)

## Progress log

| Date | Work | Validation / commit |
| --- | --- | --- |
| 2026-09-24 | Two read-only review passes; documented the plan and updated priorities. | Synthetic checks described above; implementation and commits pending. |
| 2026-09-25 | Stage 1: synthetic unittest suite, visual gallery, running instructions, and ignored disposable output. Toolkit unchanged. | 21 tests passed; six gallery figures rendered; user visual review and commit/push pending. GitHub tests explicitly deferred. |
