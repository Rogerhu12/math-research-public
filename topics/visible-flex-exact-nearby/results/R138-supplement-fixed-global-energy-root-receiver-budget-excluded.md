# R138：固定全域能量预算下的根接收器门已被严格排除

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**结论范围。** 原 high97 压缩的完整下界与 scalar Neumann 门已在公共 run `44750653724/1` 实际通过。本篇证明另一个具体事实：若继续用 [relative 合同 R.14--R.15](R138-supplement-original-high-compression-and-relative-root-receivers.md) 的同一截顶根迹读出及原 X 保存的全域 `C_E` 预算，则 R.30 的第一门不可能通过。这个结论同时覆盖 R.9 的统一范数实现，以及只把接收器替换成精确有限 Gram 的实现。因此不应为这一固定预算再制作大有限矩阵；必须先改变能量比较，例如支付局部径向权，或使用原 direct inverse 路线。

本篇不证明实际正区问题有核，不排除实际可达根迹上的更强估计，不否定已付 high 正性，也不将任何假设的根迹当成完整 PDE 解。所有比较只消费已完成的 whole 保存球和纯有理放宽，没有运行新科学目标。

## 1. 已成数据只要求四个简单上界

读取同一实际两模的三个完整保存球，得到严格有理放宽

\[
 M_{12}>\frac{189}{10},\qquad
 M_{22}<\frac{601}{250},\qquad
 M_{11}<\frac{457}{1000}.
 \tag{N.1}
\]

它们来自 run `44745192261/1`，基向量是归一 `z96=sqrt(2) sin(384 phi)` 与 `z97=sqrt(2) sin(388 phi)`，不是 raw 曲率两列。

新 run `44750653724/1` 完成原全 high 压缩及 receiver coefficients。其 `complete_new_scalar_bounds` 的完整上端直接给

\[
 b_0<1,\qquad b_1<2,\qquad b_2<2,\qquad g_0<3.
 \tag{N.2}
\]

这里 `b=rho Y`、`b_j>=||partial_phi^j b||_infty`，所以 `b0` 同时上界实际 `abs(rho)`。`g0` 是完整 actual mean 列 `g_m` 的范数；没有令该列为零。

下文固定使用 relative R.15 所读取的**已保存预算常数** `C_E` 与 `Gamma`。原 X 整球给该所选 `C_E>32`，而 `Gamma>=1`。`C_E>32` 是这个已经选择的上界数值的事实，不宣称最优实际系数常数的下界。若另付一个不同、更紧的能量比较，本篇不会自动排除它。

## 2. 任何 R.23 接收器在第 96 列上的必要负费用

沿 relative R.16--R.23，设已经支付原全部 high 压缩
`D_H>=lambda_H I`、`lambda_H>0`，并固定 `0<theta<1`。令 `C=P_H K P_L`。如果有限接收器 `W_L` 满足

\[
 W_L^*W_L\succeq(\theta\lambda_H)^{-1}C^*C-A_L,
 \tag{N.3}
\]

则用单位第96模 `e96`、保留全 high 输出，并只在其第97分量取下界，得到

\[
 \|W_Le_{96}\|^2\ge
 \frac{|M_{12}|^2}{\theta\lambda_H}-M_{11}.
 \tag{N.4}
\]

因为 `lambda_H` 是真实 high 压缩的下界，Rayleigh 比较必有 `lambda_H<=M22`。所以由 (N.1)

\[
 \|W_Le_{96}\|^2>
 \frac{(189/10)^2}{601/250}-\frac{457}{1000}
 =148+\frac{79843}{601000}>148.
 \tag{N.5}
\]

这是所有 (N.3) 接收器必须承担的费用，与后来选择多少有限 high 模无关。未计算的高输出不会使 (N.4) 变小。使用更小的已证 `lambda_H` 或更小 `theta` 只会增大该必要费用。

## 3. R.9 统一 P0/P1 预算必失败

对纯 low 接收器，R.8 具有

\[
 \Psi_0=\|N_L^{-1}W_L^*\|\ge\|W_Le_{96}\|/384,
 \qquad
 \Psi_1=\|W_L^*\|\ge\|W_Le_{96}\|.
\]

其 Neumann 放大不小于1。R.9 的 `V0>=||Y+uX||_infty>=1`，其余相加费用非负，故该指定预算必给

\[
 P_0\ge\sqrt{148}/384,\qquad P_1\ge\sqrt{148}.
\]

R.12 因而有

\[
 \mathcal N_W^2\ge\sqrt{40}P_0P_1
                   >148\sqrt{40}/384.
 \tag{N.6}
\]

R.15 的 `alpha_E` 各项非负，其第一项便迫使

\[
 \alpha_E^2\ge\frac{\Gamma^2C_E}{\rho^2}\mathcal N_W^2
             >\frac{74}{\rho^2},
 \tag{N.7}
\]

末步只用了 `Gamma>=1`、所选 `C_E>32` 和 `sqrt(40)>6`。R.30 的第一门要求
`a_EE^GB+alpha_E^2+...<2`；由于其他费用非负，仅此已经要求 `rho^2>37`。
实际 (N.2) 给 `abs(rho)<1`，故这个统一预算实际上有 `alpha_E^2>74`，不能通过该门。

## 4. 精确接收器 Gram 也不能修复同一个全域 CE 因子

本节不使用 R.9 的 `P0/P1` 三角上界。设 `P_c` 是 relative R.5 的真正对偶行，`|c|=1`；若这个行被精确计算，令

\[
 \mathcal N_{\rm exact}^2
 =\sup_{|c|=1}\left[
 \delta\|P_c'\|_2^2+\sqrt{40}\|P_c'\|_{\dot H^{-1/2}}^2
                  +(40/d_-)\|P_c'\|_{\dot H^{-1}}^2\right].
 \tag{N.8}
\]

这是 RT.16 / relative R.12 所允许的完整有限 Gram；不是把各行分别估计后的和。下面说明即使使用它，也不能通过同一个 R.15 预算。

在根代数中取 `z=e96`、`h=0`。这里仅构造一个满足原 root 行和 mean 相容式的根数据；不声称它延拓成实际齐次 PDE 解。记

\[
 R=\sqrt2\cos(384\phi),\quad
 \ell_{96}=\mathcal D^{-1}\langle\mathbf b'R\rangle\cdot\ell,
\]
\[
 w_{96}=-\mathbf bR+I(\mathbf b'R-g_m\ell_{96}).
 \tag{N.9}
\]

这是原 U/HP 的完整准确根旋转，mean rank 未删除，`I` 是环境 primitive。对该单模，周期系数平均分部积分给

\[
 |\ell_{96}|\le\frac{20}{17}\min(b_1,b_2/384).
\]

由 `||R||2=1`、`||R'||2=384` 和 homogeneous Sobolev 插值，

\[
 \|\mathbf bR\|_{\dot H^{1/2}}^2
 \le\|\mathbf bR\|_2\|(\mathbf bR)'\|_2
 \le b_0(b_1+384b_0).
\]

在全部非零环境整数频率上
`||I||_(L2 to dotH^(1/2))<=1`；这包含了完整 `g_m` 平均的去零模操作。故

\[
 \|w_{96}\|_{\dot H^{1/2}}\le\Xi_{96}:=
 \sqrt{b_0(b_1+384b_0)}+b_1
             +g_0\frac{20}{17}\min(b_1,b_2/384).
 \tag{N.10}
\]

选择 `c` 与 `W_L e96` 同向。准确 R.6 给

\[
 |\rho|\|W_Le_{96}\|
 =|\langle P_c',w_{96}\rangle|
 \le\|P_c'\|_{\dot H^{-1/2}}\|w_{96}\|_{\dot H^{1/2}}.
 \tag{N.11}
\]

这里 `P_c'` 的严格零平均来自周期导数，故 homogeneous 配对合法；并未删除 `h` 的 mean，测试中本来取 `h=0`。若 `Xi96=0`，(N.11) 已与 (N.5) 矛盾；否则由 (N.5)、(N.8)--(N.11)

\[
 \mathcal N_{\rm exact}^2>
 \frac{148\sqrt{40}\rho^2}{\Xi_{96}^2}.
 \tag{N.12}
\]

因此，R.15 即便用真正完整 Gram，也必须有

\[
 \boxed{\quad
 \alpha_E^2>
      \frac{148\sqrt{40}\,\Gamma^2C_E}{\Xi_{96}^2}.
 \quad}
 \tag{N.13}
\]

由 (N.2) 作纯有理放宽，

\[
 \Xi_{96}<\sqrt{386}+2+\frac{120}{6528}
          =\sqrt{386}+2+\frac5{272}<22.
 \tag{N.14}
\]

最后一步可直接核 `sqrt(386)<79/4`，因为 `6176<6241`，且
`79/4+2+5/272<22`。所以 `Xi96^2<484`，无需求新的科学数值。
又使用同一旧预算 `C_E>32`、`Gamma>=1`、`sqrt(40)>6`，得到

\[
 \boxed{\quad
 \alpha_E^2>\frac{148\cdot6\cdot32}{484}
            =\frac{7104}{121}>58>2.
 \quad}
 \tag{N.15}
\]

这排除了“保持原全域 `C_E` 和同一 RT 根读出，只改用更精确有限接收器 Gram”的修补方案。若改变根层容量、局部能量权、根负部与体能量的联合估计，或改用已列 direct inverse 路线，(N.15) 不自动适用。

## 5. 结论与已付量如何保留

新 high 正性与 Neumann 逆仍是实际已付输入；失败的是另一个明确的全域充分预算。原 `96/97` 负方向并未证明全问题奇异，本篇也没有新增这种断言。旧 Y 的完整 `r_E/r_B`、mean 和非齐次项都仍保留；为得到必要下界，我们只丢弃了最终预算中非负的额外费用。

下一次科学任务应先给出能绕过 (N.15) 的新比较式，再决定是否需要全 `A_L/C` 矩阵。任何后续有限矩阵继续直接复用已成 `96/97` 三球，其余新项才是新目标。

### 完整公开数据

- [signed actual](../notes/root_two_mode_form_ci/run-44745192261-1/root-two-mode-conclusion.json)，SHA-256 `95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2`。
- [new high actual](../notes/original_high_root_lower_bound_ci/run-44750653724-1/original-high-root-lower-bound.json)，`53310` bytes，SHA-256 `f3f97be683009e9c8ae461c25dfd17d782a61ea6feaf9b8b7967b3e28a9e835d`；execution `15691` bytes，SHA-256 `e753dd0ea848302ccbe41dc90a3cd8ab1a1a211985d7a7d3691d7ab6384a7687`。
- [original X actual](../notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json)，SHA-256 `1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec`。新 high 原件完整嵌入 signed 原件，后者完整嵌入 X；各旧 whole 对象和 false scope 原样保留。

数学来源为 [relative 篇](R138-supplement-original-high-compression-and-relative-root-receivers.md) R.3--R.15、R.22--R.30，[RT](R138-supplement-capped-curvature-root-trace-and-finite-receivers.md).13--19，[HP](R138-supplement-original-high-principal-and-signed-compact-bound.md).6--13，以及[新 high 消费合同](../notes/2026-11-20-R138-original-high-root-lower-bound-contract.md) HC.10--HC.16。所有角范数在本篇均归一；`E=calE/(2*pi)` 与 `B=calB/(2*pi)` 沿 relative 合同，故没有额外 `2*pi` 费。
