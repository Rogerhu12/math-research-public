"""JC: one joint96 composition/DFT row-error bound from the original W balls.

Pure definitions: no IO, numerical imports, original producer, or execution.
The public owner admits the whole original W native/source/process/publication
and the unchanged RW definition before calling.  Metadata checks here do not
authenticate bytes.  All four balls are read DIRECTLY at the exact paths below;
no original H-G norm is inferred by subtraction from a scalar RW row epsilon.
"""

W_NATIVE_SHA256 = 'dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854'
W_SOURCE_SHA256 = 'c1ca128ce18007ec118565beb013a97eaf7c0ccb11962caee474eec092a6c069'
W_RECORD_PATHS = {
    'EH': ('selected', 'physical_true_conjugacy_minus_G_norm'),
    'G0': ('exact_G_periodic_norm',),
    'G1': ('exact_G_derivative_norm',),
    'H1': ('selected', 'physical_true_conjugacy_derivative_Astrip_upper'),
}
PARAMETERS = {
    'row_modes': 96,
    'physical_frequency_factor': 4,
    'physical_period': 'pi/2',
    'normalized_angular_measure': True,
    'original_conjugacy_strip': '1/128',
    'original_selected_loss': '1/250',
    'original_selected_run': '43588332723/1',
    'trial_fourier_cutoff': 1024,
    'grid_points': 4096,
    'fixed_original_waist_normalizer_cutoff': 268435456,
}
OUTPUT_ORDER = (
    'Wiener_strip_interpolation_derivative_lower',
    'saved_derivative_interpolation_lower',
    'complete_interpolation_derivative_lower',
    'joint96_composition_error_upper',
    'joint96_Wiener_input_operator_upper',
    'complete_joint96_DFT_tail_and_alias_upper',
    'complete_joint96_scalar_row_operator_error_upper',
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def original_W_records(whole_W):
    """Read metadata from an already byte-authenticated COMPLETE original W.

    The owner separately validates W_NATIVE_SHA256 and the original complete
    process/publication/source bindings.  This pure check never manufactures
    an actual input or discards the old failed loss trials.
    """
    require(whole_W['kind']
            == 'actual_public_R31_smaller_loss_and_physical_conjugacy_strip'
            and whole_W['complete'] is True
            and whole_W['source_sha256'] == W_SOURCE_SHA256
            and whole_W['public_run_id'] == '43588332723'
            and whole_W['public_run_attempt'] == '1'
            and whole_W['physical_requested_strip'] == '1/128'
            and whole_W['physical_true_conjugacy_strip_proved'] is True,
            'the whole original actual W physical conjugacy')
    rows = whole_W['all_actual_loss_trials']
    require([row['exact_loss'] for row in rows]
            == ['3/200', '1/100', '3/400', '1/200', '1/250',
                '7/2000', '3/1000', '1/400']
            and whole_W['selected'] == rows[4]
            and rows[4]['actual_R31_gates_passed'] is True
            and rows[4]['physical_conjugacy_A1over128_proved'] is True,
            'all eight original loss outcomes and the same selected member')
    records = {}
    for name, path in W_RECORD_PATHS.items():
        value = whole_W
        for key in path:
            value = value[key]
        require(isinstance(value, dict) and isinstance(value.get('ball'), str),
                'the original whole saved W scalar ball: '+name)
        records[name] = value
    return records


def upper(api, value):
    require(value.is_finite() and api.lower(value) >= 0,
            'finite nonnegative original saved upper')
    return value.upper()


def joint_compound_row_error(api, saved_EH, saved_G0, saved_G1, saved_H1):
    """JC.5/7/11--14, preserving the same96 exact RW DFT trials.

    api supplies zero, one, rational, lower, sqrt, exp.  Bounds are computed
    with directed balls.  G1,H1 bound WHOLE derivative Wiener norms whose
    exact zero Fourier coefficient is1; only this identity permits minus1.
    A larger lower bound is selected only between two complete lower bounds
    for the same entire homotopy.  Negative failed candidates are retained.
    """
    eh, g0, g1, h1 = (upper(api, value) for value in
                      (saved_EH, saved_G0, saved_G1, saved_H1))
    require(g1 >= api.one and h1 >= api.one,
            'degree-one derivatives have exact constant Fourier coefficient1')
    sigma = api.rational(1, 128)
    M, N, L = PARAMETERS['row_modes'], PARAMETERS['trial_fourier_cutoff'], PARAMETERS['grid_points']
    require(2*N < L and N < PARAMETERS['fixed_original_waist_normalizer_cutoff'],
            'the unchanged complete RW alias and normalizer conditions')
    m0 = (api.one-(g0+eh)/sigma).lower()
    derivative_upper = g1 if g1 >= h1 else h1
    m1 = (2*api.one-derivative_upper).lower()
    m = m0 if m0 >= m1 else m1
    require(m0.is_finite() and m1.is_finite()
            and m.is_finite() and api.lower(m) > 0,
            'a positive directed Jacobian lower for EVERY interpolation lift')
    root_lower = api.sqrt(m).lower()
    require(api.lower(root_lower) > 0, 'positive square-root lower denominator')
    composition = upper(api, (4*M)*eh/root_lower)
    # A whole joint Wiener operator bound, not96 recreated scalar row targets.
    joint_wiener = upper(api, api.sqrt(api.rational(2*M)).upper()
                           *api.exp((4*M)*(sigma+g0)).upper())
    truncation = api.exp(-4*sigma*(N+1)).upper()
    alias = api.exp(-4*sigma*(L-N)).upper()
    full_tail = upper(api, joint_wiener*(truncation+alias))
    result = {
        OUTPUT_ORDER[0]: m0,
        OUTPUT_ORDER[1]: m1,
        OUTPUT_ORDER[2]: m,
        OUTPUT_ORDER[3]: composition,
        OUTPUT_ORDER[4]: joint_wiener,
        OUTPUT_ORDER[5]: full_tail,
        OUTPUT_ORDER[6]: upper(api, composition+full_tail),
    }
    require(tuple(result) == OUTPUT_ORDER, 'the entire new joint scalar target')
    return result
