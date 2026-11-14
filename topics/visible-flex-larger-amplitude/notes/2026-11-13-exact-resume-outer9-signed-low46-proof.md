# 原 cell9 的真实有符号 low46 Cauchy 传播

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-13。

本条保持原背景、原 cell9 的全部九段与原参数域，首次计算从 node10 到 node9 的实际低46齐次传播。它直接接续 R87 已成功的 cell11/10 传播。本文不把齐次像称为新段的完整非线性解；完整强迫与所有非低频仍须另付。

## 1. 同一背景及初值

冻结入口为 `outer9-low46-inputs/manifest.json`，SHA256
`e5973f185f1157aaa3743077ec5869ca5bed6fe5ec750142b6b0bec9a861b15f`。
其中列明旧成功主包、原 ready、原 cell9 全部材料的主清单、R119 的逐分量后验、R141 同场的实际 low 帽及十份不改动的 Taylor/源/射影实现。

原 cell9 的 `lengthScale=1`，valley control 准确为零，无 custom pulse cap、valley cap 或 warp weights。原 orientation、protectCell、capTransition、curvatureBound 等参数逐项保持。以真实 `delta9,mu9,rc,R9,alpha9` 计算

\[
 W_{\rm raw}=\frac{\mu_9}{r_c^7}
 \max\left(1,\frac{R_9}{\delta_9},\frac{\delta_9}{\alpha_9},
                  \frac1{\delta_9},2^{11/4}\right).
\]

实际执行必须严格核 `W_raw < slopeCap exp(-capTransition)`。所以本胞元的 cap 不活动，warp=1，chi=j0=1；新源码仅声明这个 cell9 身份，不把它延伸到后续有真实 cap/valley 的胞元。物理半径的九段端口取原 R26 正宽度的前缀与后缀包络的交集。相交只消费同一真实半径的两个已付区间，未重新执行旧积分。

对每个物理频率 `m=2,4,...,92`，取原 R87 node10 的实际 `S0` 射影列。它仍满足原内侧真 far 条件，未换成有限 Robin 条件。令

\[
 F(x)=\sqrt{r(x)w(x)^3},\qquad
 Y_m=F(x)(P_m^{\sin},K_m^{\cos})^T,
\]

以及

\[
 \lambda_m=\frac{Q_{m,\rm prescribed}^{\rm outer}}
 {Q_m^{S_0}(\mathrm{node10})}.
\]

分母分别与 R87 和新有符号 geometry 包交核，并严格排除零。真实线性参考场为 `L_R=lambda_m S0/F`。全20个非零 prescribed outer heights 原样保留；其余26个准确零。另两列在 node10 重置为单位矩阵，表示新段的 Cauchy 基列，不重复传播旧 node12 两基列。

## 2. 实际非线性初值的齐次误差接口

R119 的 `K_error_cap[m]` 与共同半径均为 `local-V` 规范下的 `W_(1/64)` strong 帽。R141 的 `low_caps[24][m]` 是同一既存完整场相对 `C_L` 的逐模式、两个物理分量之和的 strong 帽；原共同变条带在该端口不小于 `1/64`。令

\[
 e_m=\frac{V_{10}^{\rm upper}}
 {(1+m)e^{m/64}}
 \left(\min(k_m^{119},r^{119}_{\rm common})+u_{24,m}^{141}\right).
\]

这里 `V10upper` 是原末叶已付的真实 local-V 上界，只作端口分子的上界。它未被用作 `V` 或 `F` 的下界。两个差场均共用原 node10 prescribed height：`C_L` 与 `L_R` 的外侧 height 相同，而 `u` 使用原齐次低 Green，所以

\[
 \delta P_m(\mathrm{node10})=0,\qquad
 |\delta K_m(\mathrm{node10})|\le e_m.
\]

该误差为复参数域上的复圆盘半径。真实线性参考的区间是实系数背景产生的有符号区间；不能把一个实区间误称为全部复场的包络。本运行的参数域准确为 R141 `expanded_profile`：`S_product<=3/4`、`T_l1<=1/32`，并保留原全部 `4b_m` 细轴。R119 的更大已证域仅作限制使用。

若 `Phi_m(x,node10)` 是新段 trace-zero 基矩阵，则齐次误差的两个分量准确满足

\[
 |\delta (P_m,K_m)_i(x)|
 \le \frac{F(\mathrm{node10})^{\rm upper}e_m}{F(x)^{\rm lower}}
       |\Phi_m(x,\mathrm{node10})_{i,K}|.
\]

没有额外 frame 因子或第二次 `F0` 收费。完整非线性场后续还需加同一方程的 Duhamel 源项，本文未忽略或宣称该项为零。

## 3. 真实 trace-zero 方程及验证传播

置 `s=r_x/r`、`ell=w_x/w`。原物理齐次系统为

\[
 \partial_x\binom P K=
 \begin{pmatrix}-s-\ell&-ms\\-m\ell&-2\ell\end{pmatrix}
 \binom P K.
\]

换成 `Y=F(P,K)` 后得到

\[
 Y'=M_mY,\qquad
 M_m=\begin{pmatrix}(\ell-s)/2&-ms\\-m\ell&-(\ell-s)/2\end{pmatrix}.
\]

故准确基矩阵行列式为一，原射影列的单调 ratio 传播合法。每个真实源临界点仍按原160位 dyadic brackets 单独包住；其余区间使用原24阶 Taylor。原 source series、radius series、signed Taylor coefficients、max-mode92 coefficientwise absolute derivative majorant 与 `2^-100` 余项门完全不变；Arb256位、单线程。发生门失败时只对该新段 dyadic 二分，未降低精度、Taylor阶数或阈值。

在一个完整成功子步 `[a,b]`，以 `span=b-a` 缩放生成矩阵。取

\[
 B=\sqrt{|\ell\,\mathrm{span}|_{\rm up}/|s\,\mathrm{span}|_{\rm up}},
 \quad
 q=|d\,\mathrm{span}|_{\rm up}
 +\max(92|s\,\mathrm{span}|_{\rm up}B,
       92|\ell\,\mathrm{span}|_{\rm up}/B)<1/2,
\]

在零分量退化时取 `B=1`。原比较给全部部分时间的分量绝对矩阵界

\[
 \frac1{1-q}\begin{pmatrix}1&1/B\\B&1\end{pmatrix}.
\]

更细的部分时间有符号包使用 `I + [0,M]`，并逐项加入

\[
 \frac{q^2}{1-q}\begin{pmatrix}1&1/B\\B&1\end{pmatrix}
\]

作二阶以上 Peano 项。`[0,M]` 是整子步生成矩阵与零的区间 hull，包含任意部分时间的一阶积分；不会给当步生成的源免费整步衰减。该包只用于连续子步内读出，端点仍用更紧的原高阶 Taylor。

所有46个局部 signed flow、整片 `r,w,r_x,ell`、两个初值误差分量和真实线性中心的部分时间包都完整保存。每个分母先核严格正，每个输出先核有限；不允许 NaN 被 `max` 忽略。

## 4. 范数及可复用数据

连续强帽的次序是先对每个物理分量在整子步取上确界，再对46个模式求和：

\[
 \sum_{m=2,4,\ldots,92}(1+m)e^{m/64}
 \left(\sup_x |P_m(x)|+\sup_x|K_m(x)|\right).
\]

各子步的逐模式分量帽先在整个 source segment、再在整个胞元取 `max`，因此没有把频率求和移进径向上确界，也没有把两个分量的共同点态最大值冒充两个独立径向上确界。初值误差已包含在这些齐次读出帽中。

保存的 `local_signed_flow` 与 `partial_absolute_majorant` 可接以后同一实际源的逐片 Duhamel 递推。当前新结果只认证真实低46齐次贡献；它不声称完整外延拓、非低频源、完整均值修复或闭曲面已由此完成。

## 5. 实际执行记录

本次新原胞元计算已正式退出 0；`wait4` 实测 655.544241905 s，峰值 34732 KiB，小于原 96 MiB guard。主包的 164 个完整门全部为真。实际完成九段、1373 个 Taylor 子步和 4 个160位临界点括区；另 1269 次被原数学门要求细分的尝试被记录，没有作为成功子步使用。

全胞元的连续低46齐次 strong 上界为

\[
 R_{9,\mathrm{hom}}\le 1.4154201797388365e-08<2^{-26}<1/128.
\]

这是46个真实线性中心分量加实际 node10 初K误差的齐次传播，仍没有包括 cell9 内新生成的完整非线性源。谷段最大预算在原 segment3；全胞元的逐模式径向上确界先合并后求和，所以结果略大于单个最坏段之和。这个小域检验只说明下一步完整 mean/inverse 估计存在可用的实际半径，并未代替新的自映门。

主包 `outer9-signed-low46-r1.json`：SHA256 `c19d33f403f42c0b98ada4572aa58f860f17d922cd5e353d680d477d75640c07`。
资源 `outer9-signed-low46-run1-resource.json`：SHA256 `cb0357dd4765b762bf97cd3956458424ef7e0de29d2a63bcdd7f76158d048a8c`。
实际源码：SHA256 `3af09865da2c68cd3d2b09ff3b09c40e48abacadc7f3632bcb27c84817ea8a2c`。

完整逐步矩阵与连续 profiles 共 117 个可再生压缩片，逐段 checkpoint 共 9 个，路径/字节/SHA 全列在主包。按仓库规矩11，这些可由已冻源和原数据重新生成的大派生包保留在 scratch；本条归档完整源、参数、正式资源、最终全部46列、连续逐模式帽及全片校验和。未重复旧 cell11/10 ODE。

复现命令的结构为：设原 flint 依赖路径、四个 BLAS/OpenMP 线程数为1，再用 `strong_resource_run.py --out <fresh-resource> -- python <frozen-source> --out-prefix <fresh-primary-prefix>`；固定输入清单、precision/order/root/remainder 全由主包与源码绑定。源默认 RSS guard 为98304 KiB，不放宽数值门。

