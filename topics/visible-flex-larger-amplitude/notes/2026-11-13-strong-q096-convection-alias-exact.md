# 当前固定角图：28 模 convection 均值的有限角平均误差

日期：2026-11-13。范围：原 q096 固定参考角图的 convective 部分，连续角平均与原有限均匀角网格之间的一个独立误差。没有加载 M24/M28 场，没有修改物理 g、求解器或 MJS；法向速度的非线性均值不在本结论内。

## 1. 与既有实际固定图完全相同的输入

沿用 [既有连续 convection 权重](2026-11-13-strong-q096-convection-mean-exact.md) 的精确 binary64 解释：
\[
 \theta=\psi+b(s)A(\psi),\quad
 A=\frac{d_2}{2}\sin2\psi+\frac{d_4}{4}\sin4\psi,\quad
 B=A_\psi=d_2\cos2\psi+d_4\cos4\psi,
\]
\[
 c_2=q=\frac{3242591731706757}{36028797018963968},\quad
 c_4=-\frac{7337147526749689}{1152921504606846976},
\quad L=\frac{7092420367637499}{2251799813685248},
\]
\(d_2=-3c_2,d_4=-15c_4\)，\(b=1-S(s/L)\)。这里 q 是 normalized raw 状态的 gauge，不是实际核心 q1。

用
\[
 r=|d_2|+|d_4|<1,\quad A_*=\frac{|d_2|}{2}+\frac{|d_4|}{4},
\quad B_1=\frac{15}{8L},\quad B_2=\frac6{L^2}
\]
分别控制 \(|B|,|A|,|b_s|,|b_{ss}|\)。既有图证书 SHA
da4709e9bfdc6330e440c8a69a556ddd760ffd364bb05fa45a4caf28eff4e618；
既有连续 convection 结果 SHA
7a58d73cd20c45f790e5c930b5136fc87470267cd3c14088be557fe2f9d86e02。
本次又以同一精确有理输入核了 r<1。

## 2. 原均匀角平均精确保留的一整段级数

定义连续功能和有限 N 角功能
\[
 C_j(b)=\left\langle\frac{A\sin(2j\psi)}{1+bB}\right\rangle,\qquad
 C_{j,N}(b)=\frac1N\sum_{\ell=0}^{N-1}
 \frac{A(\psi_\ell)\sin(2j\psi_\ell)}{1+bB(\psi_\ell)} ,
\]
其中 \(\psi_\ell=\psi_0+2\pi\ell/N\)，\(\psi_0\) 为任意与 s 无关的相移。

对 \(1\le j\le M=28\)，多项式
\(A\sin(2j\psi)B^k\) 的最大物理角频率至多 \(2j+4+4k\)。
均匀网格对频率绝对值小于 N 的每个 Fourier 单项准确给出连续平均：
非零频率的根单位和为零，零频率的平均为一。这个等式对所有相移 \(\psi_0\) 同时成立。

因此取
\[
 K_N=\left\lfloor\frac{N-1-(2M+4)}4\right\rfloor,\qquad n_N=K_N+1,
\]
几何展开中 k=0,...,K_N 的全部项，在两种角功能里完全相等。这里用的是“取均值无 alias”的频率条件 <N，不是场重构所用的 Nyquist <N/2 条件。

## 3. 剩余项及其 b 导数的严格界

几何级数在全部 \(0\le b\le1,\psi\) 上绝对一致收敛。连续平均和有限等权平均的正算子范数都为一，故
\[
 |C_{j,N}-C_j|\le
 E_N=\frac{2A_*r^{n_N}}{1-r}.
\]
逐项求导后，同一个有限 k 段仍准确消去，余项为
\[
 |\partial_b(C_{j,N}-C_j)|\le
 E'_N=2A_*r^{n_N}
 \left(\frac{n_N}{1-r}+\frac r{(1-r)^2}\right).
\]
没有将导数级数漏掉一个 r，也没有假设 b 远离零；n_N≥1 时整个闭区间都有效。

实际非均值高度为
\[
 Z=q\sum_{j=1}^{28}Y_j(s)\cos(2j\psi).
\]
令
\[
 T=\sum_{j=1}^{28}(2j)\sup_s|Y_j(s)|,\qquad
 T_1=\sum_{j=1}^{28}(2j)\sup_s|Y'_j(s)|.
\]
这两个范数必须以后从同一实际物理五次场支付。对完整 convection 均值
\(m_{\rm conv}=\langle vZ_\psi\rangle\)，有
\[
 |m_{{\rm conv},N}-m_{\rm conv}|
 \le w_{1,N}T,\qquad w_{1,N}=|q|B_1E_N,
\]
\[
 |m'_{{\rm conv},N}-m'_{\rm conv}|
 \le w_{2,N}T+w_{1,N}T_1,\qquad
 w_{2,N}=|q|(B_2E_N+B_1^2E'_N).
\]
q 已在这些权中，不能再次乘。对同一 N、同一固定图的两场差，也可用 \(\Delta Y\) 的上述范数；N 不同则分别支付各自误差。

## 4. 本次实际完成的精确常数

源 computations/strong_q096_convection_alias_exact.js 只用既有精确有理 helper；在 functions JavaScript isolate 真执行，8 组检查全部为真。所有幂、尾、导数恒等及向外 dyadic cap 都用 BigInt，有理 cap 保留约 96 位相对精度；不是把极小量向零舍入。

| N | 准确消去的幂 k | w1 严格上界 | w2 严格上界 |
|---:|---:|---:|---:|
| 768 | 0...176 | \(2^{-262}\) | \(2^{-255}\) |
| 1024 | 0...240 | \(2^{-355}\) | \(2^{-348}\) |
| 1168 | 0...276 | \(2^{-407}\) | \(2^{-400}\) |
| 1360 | 0...324 | \(2^{-477}\) | \(2^{-469}\) |
| 1536 | 0...368 | \(2^{-541}\) | \(2^{-533}\) |

这些分别覆盖当前求解/审计/比较使用的角数，但仍只是“乘以 T、T1 的系数”。没有把未知实际场范数设成一；也没有报告当前曲面的完整均值误差已达到表内量级。完整精确输出见 [实际结果](2026-11-13-strong-q096-convection-alias-exact.json)。

## 5. 仍需独立支付

- 本条只控制理想精确角图上的 convection 分量。完整 normal velocity 的非线性角平均及其 s 导数仍需实际域/场盒。
- 原三角函数、图、除法与有限 np.mean 的浮点评价误差尚未计入；这里没有重建原 NumPy 角表。
- 实际 T、T1、原径向 Gauss6 误差与累计舍入、两个不同 coarse/fine 网格的误差仍按 R111 分账。
- 原背景与非均值 knot jets 的一致性、M28 的真实尾审计和物理展开、有限场到真 PDE、闭面族和 reach 仍为独立门。
- 无物理 RHS、无 Node worker、无 Newton；冻结 MJS/Python 恢复树没有修改。
