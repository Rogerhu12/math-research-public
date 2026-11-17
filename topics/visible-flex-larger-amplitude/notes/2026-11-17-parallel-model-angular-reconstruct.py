"""Literal FFT angular reconstruction of a height-compatible radial slice.

This is a numerical readout, not an embedding/reach or C2 certificate. The caller
owns the actual height jets and the radial regularity of their interpolant.
In particular, no PDE RHS is substituted for an actual radial derivative.

The default constant planar phase is appropriate for the present even,
pi-periodic height and rho. For other data, phase and phase_r must be values of
one actual radial phase function, not independently chosen gauge values.

All arrays are on phi=2*pi*arange(n)/n, n a positive multiple of four. The
finite planar map is the trigonometric polynomial obtained by the indicated
DFT primitive. Its radial derivative is formed by differentiating the literal
sample-to-coefficient map. The continuum curl formula is a separate diagnostic.
"""

from __future__ import annotations

import numpy as np


def _frequencies(n: int) -> np.ndarray:
    return np.fft.fftfreq(n, d=1.0 / n)


def periodic_primitive(values: np.ndarray) -> np.ndarray:
    """Zero-mean Fourier primitive along axis 0; discard the real Nyquist bin."""
    a = np.asarray(values)
    n = a.shape[0]
    freq = _frequencies(n)
    coeff = np.fft.fft(a, axis=0)
    multiplier = np.zeros(n, dtype=complex)
    nonzero = freq != 0
    multiplier[nonzero] = 1.0 / (1j * freq[nonzero])
    if n % 2 == 0:
        multiplier[n // 2] = 0.0
    out = np.fft.ifft(coeff * multiplier.reshape((n,) + (1,) * (a.ndim - 1)), axis=0)
    return out.real if np.isrealobj(a) else out


def periodic_derivative(values: np.ndarray, order: int = 1) -> np.ndarray:
    """Derivative of the same finite interpolant; real odd derivatives drop Nyquist."""
    a = np.asarray(values)
    n = a.shape[0]
    freq = _frequencies(n)
    multiplier = (1j * freq) ** order
    if np.isrealobj(a) and n % 2 == 0 and order % 2:
        multiplier[n // 2] = 0.0
    out = np.fft.ifft(
        np.fft.fft(a, axis=0)
        * multiplier.reshape((n,) + (1,) * (a.ndim - 1)), axis=0
    )
    return out.real if np.isrealobj(a) else out


def reconstruct_slice(
    *, r: float, w: float, wr: float,
    h: np.ndarray, hr: np.ndarray, hrr: np.ndarray,
    h_phi: np.ndarray, h_phiphi: np.ndarray,
    hr_phi: np.ndarray, hr_phiphi: np.ndarray,
    rho: np.ndarray | float = 1.0,
    rho_phi: np.ndarray | float = 0.0,
    phase: float = np.pi / 2,
    phase_r: float = 0.0,
) -> dict[str, np.ndarray | float]:
    """Return positions, actual radial/angular jets, Gram and curl diagnostics.

    r,w,wr are physical-r background values (wr=dw/dr). h/derivatives must come
    from one actual height. hr_phiphi means d_phi^2(h_r). The caller may obtain
    h by a single radial mean-height primitive; its derivative remains the
    declared exact integrand, with numerical quadrature error reported outside.
    """
    if not (r > 0 and w > 0):
        raise ValueError("r and w must be positive")
    h = np.asarray(h, dtype=float)
    if h.ndim != 1 or h.size < 8 or h.size % 4:
        raise ValueError("one-dimensional angular grid with n >= 8 divisible by 4 required")
    n = h.size
    phi = 2 * np.pi * np.arange(n) / n
    def arr(a):
        return np.broadcast_to(np.asarray(a, dtype=float), (n,))
    hr, hrr, h_phi, h_phiphi, hr_phi, hr_phiphi, rho, rho_phi = map(
        arr, (hr, hrr, h_phi, h_phiphi, hr_phi, hr_phiphi, rho, rho_phi)
    )
    if not np.all(rho > 0):
        raise ValueError("rho must be positive at every input angle")
    E = 1 + w * w
    z = w * w
    zr = 2 * w * wr
    P = h_phi / (r * rho * w)
    K = hr / w - 1
    T = h_phiphi / (r * w * rho**2) - h_phi * rho_phi / (r * w * rho**3)
    U = (hr_phi / w - h_phi / (r * w)) / rho
    y = 1 + K
    A = 2 * K + K * K + E * P * P
    S = 1 - z * P * P
    D = 1 - z * A
    L = y + E * T
    if not (np.all(S > 0) and np.all(D > 0)):
        raise ValueError("height projection leaves S>0,D>0 branch")
    rootD = np.sqrt(D)
    N = 1 + z * y * T / S
    B = A / (rootD * (1 + rootD)) + y * T / (S * rootD)
    BP = E * P * N / rootD**3 + 2 * z * y * T * P / (S**2 * rootD)
    BK = L / rootD**3
    BT = y / (S * rootD)
    Bz = (
        P * P / (rootD * (1 + rootD))
        + A * (A + z * P * P) * (1 + 2 * rootD)
        / (2 * rootD**3 * (1 + rootD)**2)
        + y * T * ((A + z * P * P) / (2 * S * rootD**3)
                   + P * P / (S**2 * rootD))
    )
    Pr = hr_phi / (r * rho * w) - (1 / r + wr / w) * P
    Kr = hrr / w - y * wr / w
    Tr = (
        hr_phiphi / (r * w * rho**2)
        - hr_phi * rho_phi / (r * w * rho**3)
        - (1 / r + wr / w) * T
    )
    omega_phi = rho * (1 + z * B)
    omega_phi_r = rho * (zr * B + z * (BP * Pr + BK * Kr + BT * Tr + Bz * zr))
    alpha = phi + periodic_primitive(omega_phi - 1) + phase
    alpha_r = periodic_primitive(omega_phi_r) + phase_r
    tangent = np.column_stack((np.cos(alpha), np.sin(alpha)))
    clockwise_normal = np.column_stack((np.sin(alpha), -np.cos(alpha)))
    q = np.sqrt(r * r * rho * rho - h_phi * h_phi)
    qr = (r * rho * rho - h_phi * hr_phi) / q
    radial_tangent = -hr * h_phi / q
    radial_normal = r * rho * rootD / q
    desired_radial = radial_tangent[:, None] * tangent + radial_normal[:, None] * clockwise_normal
    angular_density = q[:, None] * tangent
    angular_density_r = qr[:, None] * tangent - (q * alpha_r)[:, None] * clockwise_normal
    xy = periodic_primitive(angular_density)
    xy_r = periodic_primitive(angular_density_r)
    xy_phi = periodic_derivative(xy)
    xy_phiphi = periodic_derivative(xy, 2)
    F = np.column_stack((xy, h))
    Fr = np.column_stack((xy_r, hr))
    Fphi = np.column_stack((xy_phi, h_phi))
    relative_rr = np.einsum("ij,ij->i", Fr, Fr) / E - 1
    relative_rphi = np.einsum("ij,ij->i", Fr, Fphi) / (np.sqrt(E) * r * rho)
    relative_phiphi = np.einsum("ij,ij->i", Fphi, Fphi) / (r * r * rho * rho) - 1
    mean_diag = (relative_rr + relative_phiphi) / 2
    eig_radius = np.hypot((relative_rr - relative_phiphi) / 2, relative_rphi)
    relative_op = np.maximum(np.abs(mean_diag + eig_radius), np.abs(mean_diag - eig_radius))
    # Actual height Darboux defect, with physical phi Christoffel coefficients.
    Hrr = hrr - w * wr * hr / E
    Hrphi = hr_phi - h_phi / r
    Hphiphi = h_phiphi - rho_phi * h_phi / rho + r * rho * rho * hr / E
    curvature = w * wr / (r * E * E)
    defect = (Hrr * Hphiphi - Hrphi * Hrphi) / (E * r * r * rho * rho) - curvature * D / E
    curl_phi = rho * r * E * E * defect / D**1.5
    connection_r = z * y * U / (r * S * rootD)
    mean_turn_error = float(np.mean(omega_phi) - 1)
    continuum_alpha_r = connection_r + periodic_primitive(curl_phi) + phase_r - np.mean(connection_r)
    predicted_e_phi = (
        (radial_normal * mean_turn_error)[:, None] * tangent
        - (q * periodic_primitive(curl_phi) + radial_tangent * mean_turn_error)[:, None]
        * clockwise_normal
    )
    # For the chosen phase, an additional spatially constant alpha_r mismatch
    # creates -q*(phase_r-mean(connection_r))*normal in the continuum derivative.
    predicted_e_phi -= (q * (phase_r - np.mean(connection_r)))[:, None] * clockwise_normal
    predicted_e = periodic_primitive(predicted_e_phi) - np.mean(desired_radial, axis=0)
    actual_e = xy_r - desired_radial
    cross = xy_phi[:, 0] * xy_phiphi[:, 1] - xy_phi[:, 1] * xy_phiphi[:, 0]
    planar_speed = np.linalg.norm(xy_phi, axis=1)
    planar_curvature = cross / planar_speed**3
    return {
        "phi": phi, "F": F, "Fr": Fr, "Fphi": Fphi,
        "xy_phiphi": xy_phiphi, "P": P, "K": K, "T": T, "S": S,
        "D": D, "L": L, "rho": rho, "omega_phi": omega_phi,
        "omega_phi_r": omega_phi_r, "alpha": alpha, "alpha_r": alpha_r,
        "mean_turn_error": mean_turn_error, "sampled_weighted_mean": float(np.mean(rho * B)),
        "sampled_rho_mean": float(np.mean(rho)), "connection_r": connection_r,
        "literal_minus_curl_alpha_r": alpha_r - continuum_alpha_r,
        "height_Darboux_defect": defect, "curl_phi": curl_phi,
        "actual_radial_error": actual_e, "curl_predicted_radial_error": predicted_e,
        "radial_error_identity_gap": actual_e - predicted_e,
        "angular_density_gap": xy_phi - angular_density,
        "relative_rr": relative_rr, "relative_rphi": relative_rphi,
        "relative_phiphi": relative_phiphi, "relative_op": relative_op,
        "planar_curvature": planar_curvature,
        "radial_outward_speed": np.einsum("ij,ij->i", xy_r, clockwise_normal),
        "theta_radial_target": desired_radial,
        "max_relative_op_sample": float(np.max(relative_op)),
    }
