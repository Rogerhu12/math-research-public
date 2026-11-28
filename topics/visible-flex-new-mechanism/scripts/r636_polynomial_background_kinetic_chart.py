#!/usr/bin/env python3
"""R636 exact piecewise polynomial background plus all R632 C2 directions.

The explicit background is evaluated directly, including its true second
jets; it is never passed through the old cubic velocity-spline rule. That
rule supplies only the independent C2 perturbations. All 257 columns of the
true kinetic/memory chain remain. Science belongs to public Actions only.
"""
from __future__ import annotations
import math
import time
import numpy as np
import r632_true_hermite_kinetic_chart as previous

legacy, reduced, original, paid = previous.legacy, previous.reduced, previous.original, previous.paid
LD, Jet, COUNTS = previous.LD, previous.Jet, previous.COUNTS
identity, ld_text, physical_attainers = previous.identity, previous.ld_text, previous.physical_attainers
IntegralGrid = previous.IntegralGrid
BACKGROUND = {
    "result":"R636", "H":"17/20", "split":"1/4", "terminal_h":"585769/207900",
    "psi_power_coefficients":["0","1","0","4","-7","3"],
    "smoothstep_power_coefficients":["0","0","0","10","-15","6"],
    "h":"H on [0,1/4]; H+(B-H)*S((4*x-1)/3) on [1/4,1]",
    "kappa":"-psi(4*x) on [0,1/4]; -1 on [1/4,1]",
    "perturbations":"all 257 R632 C2 Hermite directions; L is an absolute coordinate",
    "total_center_kappa_x":"-4", "zero_perturbation_physical_length":"4",
    "background_second_jets_not_replaced_by_cubic_velocity_spline":True}


def polynomial_background(x, derivative=0):
    reduced.require_public_science()
    x=np.asarray(x,dtype=LD)
    H,B=LD(17)/20,LD(585769)/207900
    early=x<LD(1)/4
    psi=np.asarray([0,1,0,4,-7,3],dtype=LD)
    smooth=np.asarray([0,0,0,10,-15,6],dtype=LD)
    pp=np.polynomial.polynomial.polyder(psi,m=derivative)
    sp=np.polynomial.polynomial.polyder(smooth,m=derivative)
    h=np.zeros(x.shape,dtype=LD)
    k=np.zeros(x.shape,dtype=LD)
    if derivative==0:
        h[early]=H
        k[~early]=-1
    k[early]=-np.polynomial.polynomial.polyval(4*x[early],pp)*LD(4)**derivative
    h[~early]=(B-H)*np.polynomial.polynomial.polyval((4*x[~early]-1)/3,sp)*(LD(4)/3)**derivative
    if derivative==0:
        h[~early]+=H
    COUNTS["R636_exact_background_derivative_points"]+=x.size
    return h,k


class PolynomialBackgroundChart(previous.TrueHermiteKineticChart):
    """The fixed rational background plus homogeneous 257-column directions."""
    def __init__(self,knots,grid,clock):
        super().__init__(knots,grid,-4,clock)
        self.cache_parameters=self.cache_curve=None
        started=time.monotonic()
        clock.check("before_R636_exact_background_definition")
        self.background_h,self.background_k=[],[]
        for derivative in range(3):
            h,k=polynomial_background(grid.x,derivative)
            self.background_h.append(h)
            self.background_k.append(k)
        # For each actual cell, Taylor-to-Bernstein conversion is exact
        # algebra for degree 5. LD evaluates the defining rational constants;
        # it is a floating realization, never an interval certificate.
        left=np.asarray(self.knots[:-1],dtype=LD)
        width=np.asarray(np.diff(self.knots),dtype=LD)
        hc=np.zeros((6,len(left)),dtype=LD)
        kc=np.zeros_like(hc)
        for j in range(6):
            h,k=polynomial_background(left,j)
            h=h*width**j/LD(math.factorial(j))
            k=k*width**j/LD(math.factorial(j))
            for i in range(j,6):
                scale=LD(math.comb(i,j))/math.comb(5,j)
                hc[i]+=scale*h
                kc[i]+=scale*k
        self.background_h_coeff=[hc,5*np.diff(hc,axis=0)/width]
        self.background_k_coeff=[kc,5*np.diff(kc,axis=0)/width]
        COUNTS["R636_background_basis_constructions"]+=1
        COUNTS["R636_background_basis_seconds"]+=time.monotonic()-started
        clock.check("after_R636_exact_background_definition")

    def initial_parameters(self):
        q=np.zeros(self.dimension)
        q[-1]=4.
        return q

    def source_parameters(self,payload):
        raise ValueError("The R636 affine background requires its own perturbation coordinates")

    def height_fraction(self, q, direction, maximum=1., safety=.95):
        """Exact affine Bernstein height/L prefix cap, no dropped field row."""
        coeff = self.background_h_coeff[0]+np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(q, dtype=LD))
        change = np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(direction, dtype=LD))
        cap = LD(maximum)
        for positive, margin in ((change, LD(3)-coeff), (-change, coeff-LD(".8"))):
            mask = positive > 0
            if np.any(mask):
                cap = min(cap, LD(safety)*np.min(margin[mask]/positive[mask]))
        dL, length = LD(direction[-1]), LD(q[-1])
        if dL > 0:
            cap = min(cap, LD(safety)*(LD("7.9")-length)/dL)
        elif dL < 0:
            cap = min(cap, LD(safety)*(length-LD("2.1"))/-dL)
        return max(0., float(cap))

    def evaluate(self, parameters, derivatives=True, fixed_alpha=None, fixed_center=None,
                 enforce_box=True):
        reduced.require_public_science()
        if (derivatives and fixed_alpha is None and fixed_center is None and enforce_box
                and self.cache_parameters is not None
                and np.array_equal(np.asarray(parameters,float),self.cache_parameters)):
            COUNTS["R636_same_shape_complete_chain_cache_reuses"]+=1
            self.latest_geometry=self.cache_curve["physical_attainers"]
            self.latest_curve=self.cache_curve
            return self.cache_curve
        start = time.monotonic()
        self.evaluations += 1
        self.jet_evaluations += int(derivatives)
        q = np.asarray(parameters, float).copy()
        self.last_parameters = q
        if q.shape != (self.dimension,) or not np.all(np.isfinite(q)) or not 2.1 <= q[-1] <= 7.9:
            raise ValueError("The complete true shape and unchanged original L box are required")
        self.clock.check("before_R632_true_geometry_and_global_amplitude")
        dimension = self.dimension if derivatives else 0
        unit = np.eye(self.dimension, dtype=LD) if derivatives else None
        length = Jet(q[-1], unit[-1] if derivatives else np.zeros(0))
        h = [offset+basis@np.asarray(q, dtype=LD) for offset,basis in zip(self.background_h,self.h_basis)]
        k = [off+basis@np.asarray(q, dtype=LD) for off,basis in zip(self.background_k,self.k_basis)]
        rows = []
        for i in range(len(self.grid.x)):
            if not h[0][i] > 0:
                raise FloatingPointError("R632 requires positive actual h before true integrals")
            rows.append([Jet(h[j][i], self.h_basis[j][i] if derivatives else np.zeros(0)) for j in range(3)]
                        +[Jet(k[j][i], self.k_basis[j][i] if derivatives else np.zeros(0)) for j in range(3)])
        zero = rows[0][0]*0
        U, K = zero, zero
        for weight, (hv, hx, _, kv, _, _) in zip(self.grid.weights, rows):
            U += weight*(hx/hv)**2
            K += weight*kv*kv
        if not U.value > 0 or not K.value > 0:
            raise FloatingPointError("Outside the R632 U>0,K_kappa>0 amplitude graph")
        alpha = ((1+U/length**2)/K)**LD(".5") if fixed_alpha is None else Jet(LD(fixed_alpha), np.zeros(dimension))
        eta_kappa = self.grid.integrate([[row[4]/(2*row[0])] for row in rows])
        geometry, acceleration = [], []
        for row, eta in zip(rows, eta_kappa):
            hv, hx, hxx, kv, kx, kxx = row
            geometry.append([hv, alpha*kv, alpha*eta[0], hx/length, alpha*kx/length])
            acceleration.append([hxx/length**2, alpha*kxx/length**2])
        report = physical_attainers(geometry, self.grid.x, length.value)
        hc = self.background_h_coeff[0]+np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(q, dtype=LD))
        kc = self.background_k_coeff[0]+np.einsum("ijk,k->ij", self.k_coeff[0], np.asarray(q, dtype=LD))
        hg = (self.background_h_coeff[1]+np.einsum("ijk,k->ij", self.h_coeff[1], np.asarray(q, dtype=LD)))/length.value
        kg = (self.background_k_coeff[1]+np.einsum("ijk,k->ij", self.k_coeff[1], np.asarray(q, dtype=LD)))*alpha.value/length.value
        bounds = {name:[float(np.min(value)), float(np.max(value))] for name, value in
                  (("h", hc), ("k", alpha.value*kc), ("gamma", hg), ("upsilon", kg))}
        hull_okay = bool(np.min(hc)>LD(".8") and np.max(hc)<3 and
                         np.max(np.abs(alpha.value*kc))<2 and np.max(np.abs(hg))<6 and np.max(np.abs(kg))<6)
        report.update(Bernstein_polynomial_hull_bounds=bounds,
            actual_shape_parameter_identity=identity(q.tolist()),
            polynomial_hull_is_sufficient_not_necessary_for_physical_box=True,
            polynomial_hull_float_arithmetic_is_not_interval_certification=True,
            all_polynomial_hull_fields_in_original_box=hull_okay,
            U=float(U.value), K_kappa=float(K.value), alpha=float(alpha.value),
            alpha_LD_decimal=ld_text(alpha.value), actual_K=float(alpha.value**2*K.value),
            actual_kinetic_identity=float(alpha.value**2*K.value-1-U.value/length.value**2),
            fixed_center_kappa_x=ld_text(self.c), fixed_polynomial_background=BACKGROUND,
            shape_coordinates_are_perturbations_about_exact_R636_background=True, physical_center_v=float(geometry[0][4].value),
            physical_center_a=float(acceleration[0][0].value),
            physical_center_beta=float(acceleration[0][0].value-geometry[0][0].value*geometry[0][4].value**2/4))
        self.latest_geometry = report
        if enforce_box and (not report["all_sampled_original_physical_fields_in_box"] or not hull_okay):
            raise FloatingPointError("R632 true physical fields or sufficient polynomial hull leave original box")
        density = [[length*v for v in paid.density(row)] for row in geometry]
        primitive = self.grid.integrate(density)
        total = primitive[-1]
        if fixed_center is None:
            history = [[row[j]-total[j] if j in original.ODD else row[j] for j in range(8)] for row in primitive]
        else:
            center = [Jet(LD(v), np.zeros(dimension)) for v in fixed_center]
            history = [[center[j]+row[j] for j in range(8)] for row in primitive]
        height = geometry[0][0]
        end = [total[1]/length, (8*total[3]+2*total[1])/length,
               8*height**2*total[4]/length, 4*height**2*total[6]/length]
        curve = {"shape_parameters":q, "parameters":q, "geometry":geometry,
            "acceleration":acceleration, "history":history, "total_integral":total,
            "end":end, "reduced_end":[end[i] for i in (0, 2, 3)],
            "length":length, "grid":self.grid, "alpha":alpha,
            "physical_attainers":report, "knots":self.knots,
            "independent_memory_coordinates":0,
            "fixed_physical_alpha_and_center":fixed_alpha is not None,
            "fixed_polynomial_background":BACKGROUND}
        self.latest_curve = curve
        if derivatives and fixed_alpha is None and fixed_center is None and enforce_box:
            self.cache_parameters=q.copy()
            self.cache_curve=curve
        COUNTS["true_curve_evaluations"] += 1
        COUNTS["true_curve_seconds"] += time.monotonic()-start
        self.clock.check("after_R632_true_geometry_memory_and_end_chain")
        return curve
