"""Small standard-library evaluation of the existing finite momentum root.

This is a floating candidate constructor, not a validated projected root.
Its returned binary L defines an explicit finite polynomial. Subsequent
Arb calculations must bound that specified candidate and its actual defect.
The complete finite equations are those in tail_outer_saved_port_norms;
only arithmetic/order and the small dense linear solver differ.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import math


def dense_solve(matrix, right):
    """Partial-pivot elimination for this diagnostic finite Newton step."""
    n = len(right)
    a = [list(row)+[right[i]] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if not math.isfinite(a[pivot][k]) or a[pivot][k] == 0:
            raise ArithmeticError("The finite candidate Newton matrix is singular")
        a[k], a[pivot] = a[pivot], a[k]
        for i in range(k+1, n):
            factor = a[i][k]/a[k][k]
            a[i][k] = 0.
            for j in range(k+1, n+1):
                a[i][j] -= factor*a[k][j]
    x = [0.]*n
    for i in range(n-1, -1, -1):
        x[i] = (a[i][n]-math.fsum(a[i][j]*x[j] for j in range(i+1, n)))/a[i][i]
    if not all(map(math.isfinite, x)):
        raise ArithmeticError("The finite candidate Newton step is not finite")
    return x


class PureFiniteMomentumRoot:
    def __init__(self, modes, spacing, quadrature, floor):
        self.M, self.N, self.floor = modes, quadrature, floor
        self.mode = [spacing*(j+1) for j in range(modes)]
        sq = math.sqrt(2.)
        theta = [2*math.pi*k/quadrature for k in range(quadrature)]
        self.cs = [[1.]+[sq*math.cos(t*m) for m in self.mode] for t in theta]
        self.sn = [[sq*math.sin(t*m) for m in self.mode] for t in theta]

    def solve(self, state, *, radius, w, mu):
        M, N = self.M, self.N
        if len(state) != 2*M or not all(map(math.isfinite, state)):
            raise ValueError("The complete finite height/momentum state is required")
        p = [-m*radius**3*state[j]/(math.sqrt(2)*w) for j, m in enumerate(self.mode)]
        pt = [m*p[j] for j, m in enumerate(self.mode)]
        P = [math.fsum(s[j]*p[j] for j in range(M)) for s in self.sn]
        Pt = [math.fsum(c[j+1]*pt[j] for j in range(M)) for c in self.cs]
        E, w2 = 1+w*w, w*w
        target = [0.]+[math.sqrt(12)*mu/(math.sqrt(2)*radius**4*w2)*state[M+j]
                       for j in range(M)]

        def evaluate(L, jacobian):
            q, bm = [], []
            minima = [math.inf]*3
            for k, cs in enumerate(self.cs):
                Lv = math.fsum(a*b for a, b in zip(cs, L))
                K = Lv-Pt[k]
                T = 2*K+K*K+E*P[k]*P[k]
                u = w2*T
                D, S, A = 1-u, 1-w2*P[k]*P[k], 1+Lv+w2*Pt[k]
                if min(D, S, A) <= self.floor:
                    raise ArithmeticError("The finite candidate momentum branch failed")
                minima = [min(minima[i], v) for i, v in enumerate((A, D, S))]
                sd = math.sqrt(D)
                fc = u*(2+sd)/(2*sd*(1+sd)**2)
                gc = w2*(P[k]*P[k]+S*T/(1+sd))/(S*sd)
                q.append(.5*(K*K+E*P[k]*P[k])+K*Pt[k]+T*fc+(1+K)*Pt[k]*gc)
                if jacobian:
                    am = Lv+w2*Pt[k]
                    bm.append(am+(1+am)*math.expm1(-1.5*math.log1p(-u)))
            residual = [L[j]+math.fsum(self.cs[k][j]*q[k] for k in range(N))/N-target[j]
                        for j in range(M+1)]
            scale = max(1e-300, max(map(abs, q)), max(map(abs, target)))
            B = None
            if jacobian:
                B = [[0.]*(M+1) for unused in range(M+1)]
                for i in range(M+1):
                    for j in range(i, M+1):
                        v = math.fsum(self.cs[k][i]*bm[k]*self.cs[k][j]
                                      for k in range(N))/N+(1. if i == j else 0.)
                        B[i][j] = B[j][i] = v
            return residual, B, scale, minima

        L = target.copy()
        for iteration in range(30):
            residual, B, scale, minima = evaluate(L, True)
            error = max(map(abs, residual))
            if error <= 8e-14*scale:
                return L, dict(iterations=iteration, relative_residual=error/scale,
                    sampled_minA=minima[0], sampled_minD=minima[1], sampled_minS=minima[2],
                    arithmetic="Python float/math.fsum; diagnostic finite root only")
            step = dense_solve(B, residual)
            for trial in range(20):
                candidate = [a-2.**(-trial)*b for a, b in zip(L, step)]
                try:
                    rr, unused, unused2, unused3 = evaluate(candidate, False)
                except ArithmeticError:
                    continue
                if max(map(abs, rr)) < error:
                    L = candidate
                    break
            else:
                if error <= 5e-12*scale:
                    return L, dict(iterations=iteration, relative_residual=error/scale,
                        roundoff_fallback=True, sampled_minA=minima[0],
                        sampled_minD=minima[1], sampled_minS=minima[2],
                        arithmetic="Python float/math.fsum; diagnostic finite root only")
                raise ArithmeticError("The finite candidate momentum iteration stalled")
        raise ArithmeticError("The finite candidate momentum iteration budget was exhausted")
