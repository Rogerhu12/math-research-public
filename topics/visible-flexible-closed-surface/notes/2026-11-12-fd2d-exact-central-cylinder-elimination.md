# Exact central-cylinder elimination in the raw three-field representation

This note concerns only the explicitly cylindrical interval of the physical target, currently $0\le s\le C=.32$. Here $a(s)=a_0$, $a'=a''=0$, and the physical radial bumps vanish identically. The fixed angular chart is the seed-normal chart on this interval, independent of $s$ and of every profile parameter.

## Constructive exact solution

Let $\gamma_c(u)$ be the already defined, closed, unit-material-speed central curve with $|\gamma'_c(u)|=a_0$, and let $e_z$ be its fixed plane normal. Then

$$
 X(s,u)=\gamma_c(u)+s e_z
$$

has exactly the target metric $ds^2+a_0^2du^2$. In the chosen Darboux frame its second-form scalars are

$$
 n(s,u)=n_c(u),\qquad m(s,u)=0,\qquad l(s,u)=0.
$$

This is an explicit admissible central piece, not a numerical approximation or an additional regularity requirement on an unknown surface. It is $C^2$ whenever the given central curve is $C^2$. Its original Gauss and both Codazzi equations vanish identically. The existing accurate central provider and the seed-plus-finite-c representation make this piece directly available for every allowed central parameter vector.

With the new plateau lifting $w_c=1$ on $[0,C]$, the exact finite correction at every computational node in this interval is the same vector: the n coefficients equal `core_coefficients @ c`, and every m/l coefficient is zero. The exact tail lifting has weight zero there. These node values can be eliminated as affine functions of the central parameters. No physical g, central curve, tail parameter or gap condition is changed. The free field begins immediately after C; an explicitly imposed C node retains the complete central trace. The actual field is still continuous and piecewise smooth in s, which is the same representation class as before.

## Compatibility with the raw equations

In physical material coordinates the central equations read

$$
 n_s=\frac1{a_0}m_u,\qquad m_s=\frac1{a_0}l_u,
 \qquad nl-m^2=0.
$$

For a differentiable GC field while $n>0$, write $q=m/n$ and use $l=q^2n$. Direct differentiation gives

$$
 q_s=\frac q{a_0}q_u,\qquad
 n_s=\frac1{a_0}(qn)_u.
$$

Thus the smooth transport solution with initial q=0 is q=0, and n stays equal to its central trace. The same elementary characteristic argument applies to a locally Lipschitz, piecewise differentiable field with matching traces while n is bounded away from zero. This observation explains the unwanted central departures in unconstrained finite iterates; it is **not** asserted as a uniqueness theorem for arbitrary merely continuous weak second forms. The constructive cylinder above needs no such theorem and adds no C3 hypothesis to the surface task.

## Jacobian reduction

Let p contain the explicit blocks `[central c, tail b, profile delta]`. For every fixed central node j,

$$
 dy_{j,n}=C\,dc,\qquad dy_{j,m}=dy_{j,l}=0,
$$

where $C$ denotes the already exposed `core_coefficients` matrix, not the cylinder length. Remove all these field columns from the free solve and add their n-column Jacobian products $J_{j,n}C$ to the central-parameter columns. Keep the original residual rows, the nonlinear gap residual, full high-angular Gauss/Codazzi guidance and all other parameter constraints unchanged. No residual is dropped or declared solved merely because its finite projection is small.

If a previous approximate field is converted to this representation, its central nodes are explicitly replaced by the exact cylinder values and the complete original/full residual is re-evaluated. This conversion is a new initializer; it must not be described as the same saved field or as a converged refinement.
