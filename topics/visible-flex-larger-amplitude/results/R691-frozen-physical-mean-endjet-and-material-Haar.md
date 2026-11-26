# R691：冻结有限物理均值的末端兼容性与真正材料 Haar 目标

日期：2026-11-26。会话：Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：本文的目标末端必要条件和后续 Haar 角矩恒等式已证明；未对当前实际场填入新的兼容性数值，未宣称任意目标存在非圆精确实现。** 当前 physical 均值与幅度保护实际求解继续；本文同时给出替代目标的可实现定义，不以目标风险诊断停下。深谷替代输入另见 [R690](R690-quasimonotone-tail-and-deep-valley-input.md)。

## 1. 现有结论的准确范围

[R669](../results/R669-same-g-axisymmetric-tail-linear-uniqueness-and-endpoint-defect.md) 的原五次末胞高度缺项已由 [R671](../results/R671-exact-reference-tail-affine-lift.md) 的完整准确 f/h/k 补上；不能把当前准确尾重新归咎于旧 $t^8$ 障碍。R671 的 $\lambda=1,\eta=1,q=0$ 末段确实准确等距于原 scalar。尚未支付的是非圆 core 与准确尾之间的完整连接。

[R623](../results/R623-finite-material-height-and-highest-mode-defect.md) 限制有限**材料角**高度；当前有限物理 $\phi$ 基经非线性材料换元 $\theta=\Theta(\phi)$ 后通常已有无限材料谱。不能套错带宽变量来否定当前表示，也不能把固定有限层无字面零误差推成逐层逼近的正误差地板。

实际阅读了用户自己的 [2611.00534v1](https://hexagonmath.org/pdf/2611.00534v1) §3.2、Appendix A 和定理10.3。这里只将它作为用户提供的机制参考，**不是独立验证**。其单调尾讨论是线性参考问题，有限谱讨论须核材料坐标；定理10.3 所陈述的度量与高度共同调整，未声称任意有限场的旋转均值具有非圆准确实现。本文不搬用该文的存在结论、幅度常数或收敛保证；不使用撤回的 0709.3202 作为障碍。

R684/R689 支付了有限均值目标的明确连续定义和条件证书接口。正定、旋转不变与可以严格求值，并不同时支付这个目标的准确非圆实现。下面给出当前表示中可直接看见的区别。

## 2. 固定有限物理均值的末端三阶兼容性

仅在当前 $\lambda=1,\eta=1$ 的最后一个共同 Hermite 胞讨论，令 $t=S-s$，用材料角表示欧氏向量。由 R669/R671，

$$a(S-t)=R+t+O(t^9),\qquad H-I(S-t)=H+O(t^5).$$

residual 在帽端的零三 jet 使任一该有限层场具有

$$F(S-t,\theta)=(R+t)e_r(\theta)+He_z+t^3U_3(\theta)+O(t^4).\tag{1}$$

写 $U_3=u_r e_r+u_\theta e_\theta+u_z e_z$。$u_\theta$ 的下标表示切向分量，$\partial_\theta$ 表示微分。有限物理谱经换元是否成为无限材料谱不影响 (1)。直接微分并保留旋转标架 connection，得到

$$
\begin{aligned}
|F_s|^2&=1+6u_r(\theta)t^2+O(t^3),\\
F_s\cdot F_\theta&=-3R u_\theta(\theta)t^2+O(t^3),\\
|F_\theta|^2&=(R+t)^2+2R\{u_r(\theta)+\partial_\theta u_\theta(\theta)\}t^3+O(t^4).
\end{aligned}\tag{2}
$$

冻结场 $F_*$，令 $\langle\cdot\rangle_*$ 为其已经固定的有限物理角规则，物理节点 $\phi_j=2\pi j/N_*$、材料角 $\Theta_*(\phi_j)$。冻结目标的准确展开为

$$
\begin{aligned}
E_*(S-t)&=1+6A_*t^2+O(t^3),
& A_*&=\langle u_{3,r}^*\rangle_*,\\
C_*(S-t)&=(R+t)^2+2RB_*t^3+O(t^4),
& B_*&=\langle u_{3,r}^*+\partial_\theta u_{3,\theta}^*\rangle_*.
\end{aligned}\tag{3}
$$

若另一有限 R671 场准确实现此目标，交叉方程先给 $u_{3,\theta}=0$，径向方程给 $u_{3,r}=A_*$，角向方程再给 $u_{3,r}=B_*$。因此必须有

$$\boxed{B_*-A_*=\langle\partial_\theta u_{3,\theta}^*\rangle_*=0.}\tag{4}$$

这不是对原固定 g 重证 R669，而是由有限场均值**先定义新目标后**的一条目标 jet 必要条件。它适用于每个有限 quintic 层，即使末胞缩小、自由 core 与材料映射改变；只要仍有 (1)，同一个冻结 $E_*,C_*$ 的系数不能移动。

有限物理角规则中 (4) 的左端为

$$\frac1{N_*}\sum_j\frac{\partial_\phi u_{3,\theta}^*(\phi_j)}{\rho_*(\phi_j)},$$

一般没有准确的离散积分分部恒等式使它为零。即使改成完整物理角积分也不自动为零，因为 $1/\rho_*$ 随角变化。完整材料 Haar 积分则对周期 $u_{3,\theta}^*$ 自动满足 (4)；但有限材料加权求积仍须支付自身别名误差，不能默称 Haar。满足 (4) 仅消掉一条必要条件，仍不证明全部非线性边界问题可解。

**范围。** 本文未计算当前实际父的 $B_*-A_*$，未报告它非零，也未设立新的冻结门。即使某个输入的 (4) 非零，也只排除具有 (1) 的有限层字面准确根；未排除较弱端点正则的 $C^2$ 极限，未给对径向精化一致的 Gram 正误差下界。误差可以集中到缩短的末胞，README 的真正同目标精化仍须实际做；当前均值求解不因本条观察中止。

可选实际诊断只需读冻结父末胞的准确 $U_3^*$，按**同一个**均值规则计算 (4)，记录目标身份与载体误差。若为改善设计改用另一平均、修正目标尾或换 scalar，须明确是另一输入，不得在已经声明的固定目标精化中移动 g。


## 3. 连续 physical 平均仍不自动修正，材料 Haar 才给准确消去

连续 physical 平均是 $(2\pi)^{-1}\int_0^{2\pi}(\cdot)\,d\phi$。对周期 $u=u_{3,\theta}^*$，准确积分分部给

$$
\frac1{2\pi}\int\partial_\theta u\,d\phi
=\frac1{2\pi}\int\frac{u_\phi}{\rho}\,d\phi
=\frac1{2\pi}\int u\,\frac{\rho_\phi}{\rho^2}\,d\phi.
\tag{5}
$$

右端一般不为零。提高 physical 求积 N 只使其趋近这个通常非零的积分，不从根源修复 (4)。这是坐标测度问题，不只是一条有限求积精度问题。

真正材料 Haar 平均使用固定材料圆的均匀测度 $d\theta/(2\pi)$。在当前物理参数中 $d\theta=\rho(\phi)d\phi$，因此

$$
\overline E_H(s)=\frac1{2\pi}\int_0^{2\pi}\rho\,|F_s|^2\,d\phi,\qquad
\overline C_H(s)=\frac1{2\pi}\int_0^{2\pi}\frac{|F_\phi|^2}{\rho}\,d\phi.
\tag{6}
$$

$\int\rho\,d\phi=2\pi$ 是完整材料转一圈的准确恒等式，不能用浮点求积总量另定义目标。交叉平均为 $(2\pi)^{-1}\int F_s\cdot F_\phi\,d\phi$；现有精确反射 parity 使它为零。完整旋转目标为 $\overline E_H ds^2+\overline C_H d\theta^2$。若 F 浸入且 $\rho>0$，两对角系数正；固定后它关于材料旋转不变，所以已有相位共轭结构保留。

式 (4) 在这个平均下是周期函数导数的完整积分，准确为零。这里只支付这条相容性；仍不能由此断言全部非线性兼容性、非圆实现、reach 或可见幅度。若选择这个目标，应明确另开 true-material-Haar 设计或冻结输入，当前已经声明的 finite-physical 目标保持原身份。

## 4. 冻结 core 后，准确 Haar 目标只需要有限组角矩

角基 $B_i(\phi)$ 取原 q 的完整欧氏向量基（包含旋转物理标架），不删模式。把冻结场写成

$$F=q+f e_r(\Theta)+z e_z,\quad q=\sum_i q_i(s)B_i,\quad
u_i=q_i'(s),\quad d=z_s=h_sH+k_s.$$

记 $D_i=\partial_\phi B_i$，其导数必须包含旋转标架 connection。定义精确的固定角矩

$$
\begin{aligned}
P_{ij}&=\frac1{2\pi}\int\rho\,B_i\cdot B_j\,d\phi,&
Q_{ij}&=\frac1{2\pi}\int\frac{D_i\cdot D_j}{\rho}\,d\phi,\\
\ell_i&=\frac1{2\pi}\int D_i\cdot e_\theta(\Theta)\,d\phi,&
b_i&=\frac1{2\pi}\int\rho\,B_i\cdot e_z\,d\phi.
\end{aligned}\tag{7}
$$

周期积分分部给**同一个**交叉向量

$$\ell_i=\frac1{2\pi}\int\rho\,B_i\cdot e_r(\Theta)\,d\phi.\tag{8}$$

证明是对周期内积 $B_i\cdot e_\theta(\Theta)$ 微分：其导数为 $D_i\cdot e_\theta-\rho B_i\cdot e_r$，整圈积分为0。不能分别用两个未支付误差的 quadrature 数组替代两边，再假定它们逐字一致。

展开完整平方后，(6) 等于

$$
\boxed{
\begin{aligned}
\overline E_H&=u^TPu+2f_s\ell^Tu+2d\,b^Tu+f_s^2+d^2,\\
\overline C_H&=q^TQq+2f\,\ell^Tq+f^2.
\end{aligned}}
\tag{9}
$$

这保留所有原 q/core/H 与准确 f/h/k；没有少数模截断。冻结 F* 后，P/Q/ℓ/b 也全部冻结，只算一次。其后任意新 s 上，目标由冻结共享 quintic 的 q/q_s、准确 scalar 及固定角矩二次型给出，不必每次重新扫 2048 个角。精化当前候选的 mesh/M/N 不改变冻结目标的任何角矩或 q*。

### 4.1 与原完整角基直接对接

原模式为 $\nu_j=2j$，基依次为 $R_j=\cos(\nu_j\phi)e_r(\phi)$、$T_j=\sin(\nu_j\phi)e_\theta(\phi)$ 和 $Z_j=\cos(\nu_j\phi)e_z$，R/Z 含常模，T 从1开始。令

$$\gamma_k(w)=\frac1{2\pi}\int w(\phi)\cos(2k\phi)\,d\phi.$$

则

$$C_{ij}(w)=\tfrac12\{\gamma_{|i-j|}(w)+\gamma_{i+j}(w)\},\quad
S_{ij}(w)=\tfrac12\{\gamma_{|i-j|}(w)-\gamma_{i+j}(w)\}.\tag{10}$$

P 的 R/R、Z/Z 块为 C(ρ)，T/T 块为 S(ρ)，其它块为0。Q 的完整非零块为

$$
\begin{aligned}
Q_{R_iR_j}&=\nu_i\nu_jS_{ij}(1/\rho)+C_{ij}(1/\rho),\\
Q_{T_iT_j}&=S_{ij}(1/\rho)+\nu_i\nu_jC_{ij}(1/\rho),\\
Q_{R_iT_j}&=\nu_iS_{ij}(1/\rho)+\nu_jC_{ij}(1/\rho),\\
Q_{Z_iZ_j}&=\nu_i\nu_jS_{ij}(1/\rho).
\end{aligned}\tag{11}
$$

这包括完整 R/T 交叉块与 R 常模的角导数；Z 常模的 Q 行为零。原 q 角三块的打包次序保持。

设 $\delta=\Theta-\phi$，并记

$$c_j=\frac1{2\pi}\int\cos(\nu_j\phi)\cos\delta\,d\phi,\qquad
s_j=\frac1{2\pi}\int\sin(\nu_j\phi)\sin\delta\,d\phi.$$

由同一个 ℓ 的第一种定义，

$$\ell_{R_j}=c_j+\nu_js_j,\qquad
\ell_{T_j}=\nu_jc_j+s_j,\qquad \ell_{Z_j}=0.\tag{12}$$

$b$ 只有 Z 块，其值为 $\gamma_j(\rho)$。ρ 的 Fourier 系数本来有限，P 与 b 可直接准确代数形成；Q 只需 $1/\rho$ 的余弦矩至2M，ℓ只需上列 c/s 至M。无需保存一个巨大的角×径×模 raw 表。

### 4.2 准确矩的实际求积与误差接口

目标中角矩按完整积分定义，工作角数 Q 仅控制积分载体精度，不成为数学定义。若周期函数 w 的 p 阶导数全域不超过 $A_p$、$p\ge2$，则 Fourier 系数分部积分给 $|\widehat w_n|\le A_p/|n|^p$。均匀 Q 点 DFT 的目标频率 $|n|\le n_0<Q$ 满足

$$
|\widehat w_n^{(Q)}-\widehat w_n|
\le \frac{4A_p}{(Q-n_0)^p},
\tag{13}
$$

因为所有非零 alias 仍保留，且 $\zeta(p)<2$。普通浮点 FFT 误差**另外**支付，不能只加 (13) 就称严格矩盒。

一个可直接实现的完整入口用原准确 binary core 的有限三角定义，在全部 Q 网格点向外求 ρ/δ，再向外求倒数、sin/cos 与有限 DFT。由网格 ρ 下端减去 $\pi\|\rho_\phi\|_\infty/Q$ 可得到完整 $\rho_{\min}>0$；若该下界太松，增加工作 Q 是求积/包围细化，不修改 core 或目标。

倒数导数的准确上界递推为

$$
R_0=1/\rho_{\min},\qquad
R_j=\rho_{\min}^{-1}\sum_{k=1}^j\binom jk
\|\rho^{(k)}\|_\infty R_{j-k}.
\tag{14}
$$

$\rho^{(k)}$ 的上界直接取完整 Fourier l1 和。对 $e^{i\delta}$，完整 Bell 递推给 sinδ/cosδ 的 p 阶导数界；取所有 δ 模，不把高模或非线性 alias 丢掉。然后以 (13) 分别扩大 reciprocal 与 c/s 的 DFT 盒。所得一组角矩可在 runner 保存并供冻结径向目标反复消费；发表紧凑统一误差、ρ正下界、工作分辨率与完整源/冻结父身份，矩 arrays 不入 git。

## 5. moving 设计与 frozen 求解有不同导数责任

### 5.1 moving 设计：必须微分角矩的全部 core 依赖

设计时 q/H/core 都可变，P/Q/ℓ/b 不能假装常量。对于实际原自由 core 方向，$\dot\rho=\partial_\phi\dot\Theta$，完整一阶变化为

$$
\begin{aligned}
\dot P_{ij}&=\langle\dot\rho B_i\cdot B_j\rangle_\phi,&
\dot Q_{ij}&=-\langle\dot\rho D_i\cdot D_j/\rho^2\rangle_\phi,\\
\dot\ell_i&=-\langle\dot\Theta D_i\cdot e_r(\Theta)\rangle_\phi,&
\dot b_i&=\langle\dot\rho B_i\cdot e_z\rangle_\phi.
\end{aligned}\tag{15}
$$

ℓ 的另一种表达式给完全相同的变化，等价性使用 $\dot\rho=\partial_\phi\dot\Theta$ 的完整积分分部。原端口/core 链对 q/u 的变化仍由完整原算子支付，不因增加 (15) 重复或删除。

固定 scalar/profile 后 $\dot d=h_s\dot H$，所以

$$
\begin{aligned}
\dot{\overline E}_H={}&2u^TP\dot u+u^T\dot Pu
+2f_s(\ell^T\dot u+\dot\ell^Tu)\\
&+2d(b^T\dot u+\dot b^Tu)
+2\dot d(b^Tu+d),\\
\dot{\overline C}_H={}&2q^TQ\dot q+q^T\dot Qq
+2f(\ell^T\dot q+\dot\ell^Tq).
\end{aligned}\tag{16}
$$

对真实材料 Gram $(E,B,C)$ 形成 $r_{11}=E/\overline E_H-1$、$r_{22}=C/\overline C_H-1$、$r_{12}=B/\sqrt{\overline E_H\overline C_H}$，完整变化为

$$
\begin{aligned}
\dot r_{11}&=\dot E/\overline E_H-(1+r_{11})\dot{\overline E}_H/\overline E_H,\\
\dot r_{22}&=\dot C/\overline C_H-(1+r_{22})\dot{\overline C}_H/\overline C_H,\\
\dot r_{12}&=\dot B/\sqrt{\overline E_H\overline C_H}
-\tfrac12r_{12}(\dot{\overline E}_H/\overline E_H+\dot{\overline C}_H/\overline C_H).
\end{aligned}\tag{17}
$$

(15)–(17) 可逐项转置为完整 J*；任何不计倒数ρ或Θ方向的简化都不是这个 moving 目标的全导数。现有 R684 material 有限求积算子已保全部权重导数，能作为明确有限 quadrature 的数值设计入口；它仍不是无误差的 true-Haar 目标。把其工作 Q 提高后与完整角矩误差对照，才可把数字理解为同一个积分目标的近似。

### 5.2 frozen 求解：不再微分目标角矩或目标均值

选定 F* 后，定义 (6) 或等价 (7)–(9) 的完整连续 g*，连同固定 core、原准确 scalar/profile、q*共享节点、H*、cap recipe 与来源全部冻结。新的候选可改变自由 core 和分辨率，但目标角矩与 q*/H* 不动。

此时仅对当前物理 Gram 作固定正对角 target scaling；$\dot{\overline E}_H=\dot{\overline C}_H=0$，不能保留 (17) 中 moving 均值投影。每个新径点从冻结 q*与准确 profile 求 (9)，其 scalar 与角矩载体误差独立进入连续证书。工作积分 Q/精度改变不改变 g*；若将近似矩本身改作定义，必须另声明新目标，而不能称 true Haar 的同目标精化。

真正的固定目标求解仍需全域相对 Gram、同一 g* 的实际 mesh/M/N 精化和完整同场几何。本文证明修复一个已识别的目标兼容性机制，并给出全自由量的 moving/frozen 接口；没有把必要条件或准确积分表示升级为非圆精确 flex 的存在结论。
