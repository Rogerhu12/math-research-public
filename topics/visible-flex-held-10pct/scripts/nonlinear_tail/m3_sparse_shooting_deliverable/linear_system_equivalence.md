# All-node Newton equations for the same finite tail problem

This is a change of finite numerical linear algebra. It does not change the
Darboux/root equations, the physical metric, the integration scheme, the
mean recovery, the positive-root guards, the nonlinear residual normalization,
the original line search, or the final acceptance tolerance. It also does not
assert an infinite tail or an embedded closed family.

Write the stored state at node n as y_n=(q_n,p_n), with M components in each
part. The original stage map Phi_n maps node n+1 to node n, including the
original momentum port normalization. The original equations are

r_n=Phi_n(y_{n+1})-y_n=0,
q_0=h,
p_L-G_L q_L=0,

where the same finite far graph G_L is diagonal. Put J_n=D Phi_n at the
current nonlinear trial. The exact Newton system is

w_n-J_n w_{n+1}=r_n,
(w_0)_q=h-q_0,
(w_L)_p-G_L(w_L)_q=-(p_L-G_Lq_L).

These signs follow directly by linearizing r_n: its differential is
J_n w_{n+1}-w_n. No nonlinear term is discarded beyond the definition of a
Newton step. The M homogeneous cut-variation columns are obtained from the
same system with all stage/deep right sides zero and (w_0)_q equal to the
successive coordinate vectors. Their node-zero momentum components give the
same cut tangent graph as the original elimination whenever both are defined.
The original physical-height chain rule and finite-difference jet Jacobian
then consume this graph unchanged.

The original solver recursively writes a momentum graph and inverts
T11+T12*g at every stage. A failed or ill-conditioned intermediate projection
is not by itself singularity of the full boundary-value linear system. The
new solver retains every q_n and p_n and factors this full sparse system.
If that full system is singular, sparse LU still fails; no equation is
removed or replaced by a least-squares fit.

Let s_n>0 be exactly the original first-mode residual normalization. The
implementation writes w_n=s_n*z_n and divides each stage row by s_n.
Thus its diagonal block is I, its adjacent block is
-(s_{n+1}/s_n)*J_n, its cut right side is (h-q_0)/s_0, and its deep right side
is -(p_L-G_Lq_L)/s_L. This is invertible diagonal row/column scaling of the
same Newton system. The stored physical correction is recovered as s_n*z_n.

The Python helper evaluates the residual of these equations separately in
long-double arithmetic after the float64 sparse factorization, with up to
two residual corrections. The nonlinear worker retains its own original
line search and residual acceptance. Both original nonlinear D/S/A guards
remain active. The old `chartCondition` becomes null because no intermediate
Riccati graph is used; null is not a claim that the complete BVP has condition
number one or is uniformly well conditioned.

## Implementation and initial diagnostic correction

The generator copies the immutable 70-source closure into a separate
scratch directory and changes only the original stage-core Newton correction
and cut-tangent linear solve, plus the helper invocation. The source
factory, stage maps, guard code and original cache remain untouched. Source
and helper hashes are recorded in `sparse-source-change.json`.

An initial additional linear check used a purely componentwise backward
error. A homogeneous boundary row containing only machine-roundoff leakage
can have componentwise relative error one although its absolute residual is
less than 1e-15. The first test therefore stopped at that new check, before
claiming any nonlinear result. That helper is preserved as
`sparse_shooting_linear_v1.py`, with its failed trace. Version 2 uses the
standard normwise backward error for this extra linear check and retains
the absolute linear residual and the componentwise value as diagnostics.
The original nonlinear acceptance and geometric guards were never changed.
The global normwise error alone does not estimate the condition number or
certify the nonlinear solution.

A real nearby complete M8 input is used for comparison: multiply the already
coupled q≈.020001225 prefix's complete worker height by 1.000001. This scaled
input is only a numerical validation vector, not a newly coupled prefix or
a family at the corresponding scaled core amplitude. The sparse backend's
accepted checkpoint is then handed to the unmodified original worker at
exactly the same physical parameters and complete input. Its original
residual, all height jets, audit, and full cut Jacobian are compared.
