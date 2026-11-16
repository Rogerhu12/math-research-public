# Complete twelve-gradient normal-form consumer

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.

This is the complete original parameter calculation, after the verified global Bell coordinates and actual squarefree32 basis. It retains all seventeen gradient generators and computes the twelve canonical representatives in the sixteen low squarefree coordinates. It does not claim to solve the remaining ideal.

## Source and input

- Source: notes/2026-11-16-r150-original-complete-twelve-gradient-low-normal-forms-v2-789f.py.
- Source blob: eadc4a38cf435ab600fbc1082a4ee9e542cc2294.
- Source bytes/SHA-256: 19286 / 23f99635b7abe21ff9bd621175fd2d9d82ffd6146690cac7c7b893f443382117.
- Inputs: notes/2026-11-16-r150-original-complete-twelve-gradient-low-normal-forms-inputs-v2-789f.json.
- Exact runtime: Python 3.12, python-flint 0.9.0.
- Budget: 600 seconds, 4096 MiB. Actual successful elapsed time: 146.2035727620023 seconds.

The two parent gzip models are verified by whole file SHA, uncompressed SHA, and their exact semantic binding. Their generator sources and original full file identities appear in the inputs manifest. No network input is used.

## Invocation

~~~text
python 2026-11-16-r150-original-complete-twelve-gradient-low-normal-forms-v2-789f.py \
  --hyperbolic <complete-original-hyperbolic-coordinate-model.json.gz> \
  --squarefree <complete-original-squarefree32-fixed-reduction-operators.json.gz> \
  --out <temporary-output-directory> --seconds 600 --memory-mib 4096
~~~

## Mathematical gates

The literal original physical N/Gamma polynomials are reconstructed in all free parameters. The complete inverse Jacobian is differentiated and compared entrywise. The five u gradients have their exact previously verified quadratic parts, symmetric linear Hessian coefficient matrix, and independently verified constant terms.

For each remaining gradient
$$
G=\alpha z+\beta v+\gamma u+\delta,\quad F=Qz+Pv+Au+b,
$$
the exact constant inverse $Q^{-1}$ gives
$$
\lambda=\alpha Q^{-1},\qquad
N=(\beta-\lambda P)v+(\gamma-\lambda A)u+\delta-\lambda b.
$$
Every full polynomial $G-N-\lambda F$ must be zero. The first six correction rows are linear in y; the last six are fixed elements of the cubic field. Parameter division is not introduced.

## Temporary output contract

The complete five-gradient coefficient file is saved once. Each verified remaining row is then saved as complete-original-normal-form-NN.json.gz, containing all sixteen parameter coefficient polynomials and all five original correction polynomials. Polynomial entries use the existing original format: a sorted array of exponent-vector and exact rational-coefficient-string pairs in variable order d,y0,...,y5,w0,...,w5,u0,...,u4.

All JSON is emitted canonically through streaming gzip. Each descriptor includes whole compressed byte count and SHA-256, logical byte count and SHA-256. The final model contains exactly twelve verified row descriptors and the five-gradient descriptor under one binding. It is an index to complete arrays, not a replacement of those arrays by a rank summary.

A per-row checkpoint is written only after that complete row file and its original product have finished. The current executable does not skip mathematical preparation on rerun; downstream consumers may use completed output descriptors. A partial row file is never accepted as complete.

The final small receipt records all actual gates and diagnostics. A budget exception records status budget-checkpoint and parameters.error; other handled exceptions record failed. An externally killed process has no completed receipt unless its final file was actually written.

## Actual identity and scope

The successful v2 binding is 8fb21996da88d9abaa7d8a0c96208129603808d7c5c1e03b9acf6caa1dca6545. The exact execution manifest is notes/r150-nonrankone-execution-789f/20261116-local-complete-twelve-gradient-low-normal-forms-v2.json. It includes all output hashes and preserves the earlier aggregate-serialization exit137 as a failure.

All twelve rows are remaining ideal generators. Their linear row span alone is not the ideal they generate in the finite free32 algebra. Products and the normalized relation y dot w = 1 remain part of the subsequent problem.
