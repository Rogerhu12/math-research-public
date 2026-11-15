# R271 附录：低物理孔输入的真实借位四次幂界、完整 Gram 压缩及 Green 低孔输出

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文把原 N/Y 算子的环境头幂阈值替换为输入向量的实际物理孔数。对所有头长 $m$、所有 $s,k\ge0$，在原物理内积中有
$$
\|A_m^kP_{\le s}\|
\le6^k\exp[-\gamma(k-s)_+^4],
\qquad \gamma=\frac{770}{4^4}.
$$
这里 $P_{\le s}$ 是二进制物理孔数不超过 $s$ 的投影，不是前 $s$ 个整数头、Jordan 头或尾核高度投影。

推论保留完整核 Gram：低孔压缩有显式上界，完整逆在同一低孔测试上的二次型有相应下界。另对已付等权长池的完整 Moore–Penrose 列，可以在不改 forcing、不截断完整逆的条件下控制其低孔输出。N 型还有同一完整 bosonic 核投影下的低孔测试反馈行下界。

本文没有证明完整逆保持低孔支持，没有给原连续尾完整 Green 列的统一上界，也没有给原 $W$ 的移动反馈行上界。普通 ISP 与原 $N=M$ 仍 OPEN。

依赖和去重：
- [R234 真实四次环境头幂](R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md) 用环境阈值 $k\ge\max(2m,16)$。
- [低输出与平方对数稳定域](R239-appendix-low-output-identities-and-log-squared-stable-range.md) 保原头、混合幂及实际修复；其中仍是环境头参数。
- [逐列低高度泄漏](R271-appendix-columnwise-low-height-leakage-and-sharp-cubic-log-common-cost.md) 控制原物理源头前缀与尾核高度，不是本文的物理 popcount 条件。
- [完整等权池 Green 列](R271-appendix-uniform-pool-exact-green-column-and-true-head-power-budget.md) 提供下文 §5 的完整最小者公式。
- [联合归一 bit 反馈](R271-appendix-joint-normalized-bit-feedback-and-physical-kernel-row-bound.md) 提供 §6 的同一完整核伴随。

## 1. 原权、实际孔数和单项的借位

在原物理基 $(e_n)_{n\ge0}$ 上，记
$$
Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\qquad
d_i=W_{2^i},\qquad N_i=\frac{B^{2^i}}{d_i}.
\tag{1.1}
$$
原二进位乘积身份及相邻权比为
$$
W_n=\prod_{j:n_j=1}d_j,\qquad
\eta_j=\frac{d_{j+1}}{d_j^2}
=\frac{\alpha_{j+1}}{\alpha_j}
\le e^{-770\,16^j}.
\tag{1.2}
$$
其中 $n_j\in\{0,1\}$ 是 $n$ 的二进位。设
$$
\ell(n)=\sum_j n_j,\qquad
P_{\le s}e_n=\mathbf1_{\{\ell(n)\le s\}}e_n.
\tag{1.3}
$$

取有限非负整数族 $(k_j)$，置
$$
k=\sum_jk_j,\qquad r=\sum_jk_j2^j,\qquad
M_k=\prod_jN_j^{k_j}.
$$
若 $n<r$，则 $M_ke_n=0$。若 $n\ge r$，令 $t=n-r$，其二进位为 $t_j$。将 $t+\sum_jk_j2^j=n$ 逐位相加，得到唯一有限非负整数族 $(c_j)$：
$$
c_{-1}=0,\qquad
k_j+t_j+c_{j-1}=n_j+2c_j.
\tag{1.4}
$$
它等价于从 $n$ 中逐位删除全部 $k_j$ 次时的真实借位计数。特别这里既计算了同位多次删除，也计算了输入该位原本为空时的借位。

由 (1.2)--(1.4)，实际非零系数严格为
$$
\begin{aligned}
M_ke_n
&=\frac{W_n}{W_{n-r}\prod_jd_j^{k_j}}e_{n-r}\\
&=\left(\prod_jd_j^{\,n_j-t_j-k_j}\right)e_{n-r}
=\left(\prod_j\eta_j^{c_j}\right)e_{n-r}.
\end{aligned}
\tag{1.5}
$$
没有把单项换成一个抽象 Boolean 删除算子，也没有先把 $(k_j)$ 归并成 $r$ 的标准二进位。后者会丢失归一分母 $\prod_jd_j^{k_j}$ 的真实费用。例如 $N_0^4e_4$ 对应 $k_0=4$，(1.4) 给 $c_0=2,c_1=1$、$C=3$，并保系数 $\eta_0^2\eta_1$；若只将标准整数 $4+0=4$ 作两数加法，则错误地看不到这些 carry。

对 (1.4) 求和，所有族均有限，得
$$
C:=\sum_jc_j
=k+\ell(n-r)-\ell(n).
\tag{1.6}
$$
因此在输入 $\ell(n)\le s$ 时，
$$
C\ge(k-s)_+.
\tag{1.7}
$$
这正是环境阈值可以换成实际输入孔数的原因。

## 2. 加权借位能量和完整单项范数

置
$$
E=\sum_{j\ge0}16^jc_j.
$$
若 $E=0$，则全部 $c_j=0$，所需结论直接成立。否则令
$$
K=\max\{j:c_j>0\}.
$$
该最大值存在，因为 (1.4) 保留的是有限多个加数的逐位 carry：每位的 $k_j$ 是该词尚未归并的乘数频数，允许大于 $1$；它不是整数 $r$ 的标准二进位。有限多重加数相加后只有有限个 carry。由 (1.4) 以及 $n_{j+1}\le1$、$k_{j+1},t_{j+1}\ge0$，
$$
2c_{j+1}\ge c_j-1,\qquad c_j\le2c_{j+1}+1.
\tag{2.1}
$$
在顶部 $c_{K+1}=0$，所以 $c_K=1$。从顶部反向迭代，
$$
c_j\le2^{K-j+1}-1\qquad(0\le j\le K).
$$
于是
$$
C\le\sum_{j=0}^K(2^{K-j+1}-1)
=2^{K+2}-K-3<4\cdot2^K.
$$
另一方面 $E\ge16^K$，因此
$$
\boxed{
E\ge\left(\frac C4\right)^4
\ge\frac{(k-s)_+^4}{4^4}.
}
\tag{2.2}
$$
这一步保留顶部 carry，避免把各个 $c_j$ 的尾传播分别求和。顶部锐化由本课题 root 提出，以上为原实际计数上的完整证明。

由 (1.2)、(1.5)、(2.2)，在所有低孔输入基向量上，
$$
\|M_ke_n\|
\le\exp[-\gamma(k-s)_+^4],
\qquad\gamma=\frac{770}{4^4}.
$$
固定 $M_k$ 是一个实际加权单向移位；不同非零输入有不同输出。因此它在输入投影后的范数是这些真实系数的上确界，而不需对输入坐标再作三角估计。由此
$$
\boxed{
\left\|\left(\prod_jN_j^{k_j}\right)P_{\le s}\right\|
\le\exp[-\gamma(k-s)_+^4].
}
\tag{2.3}
$$
这对任意有限指标族成立。有限 $m$ 头上的限制也成立；移位越出该头时，相应项为零。

## 3. 两个原模型的全部幂

沿用原权 $b_i=(i+1)^{-2}$，原两个算子为
$$
T_N=\sum_{i\ge0}b_iN_i,\qquad
T_Y=\sum_{i\ge0}b_iN_i(I+N_i)^{-1}.
\tag{3.1}
$$
其有限头限制记为 $A_m$。所有 $N_i$ 都是同一个 $B$ 的幂，彼此及其 Cayley 逆对易。

由 $N_i^2=\eta_iN_{i+1}$、$\|N_i\|\le1$，
$$
\|(I+N_i)^{-1}\|
=\|(I-N_i)(I-N_i^2)^{-1}\|
\le\frac2{1-e^{-770}}<3.
\tag{3.2}
$$
N 型 $k$ 次展开的系数绝对和小于 $2^k$，(2.3) 遂给
$$
\|A_{m,N}^kP_{\le s}\|
\le2^k e^{-\gamma(k-s)_+^4}.
\tag{3.3}
$$

Y 型每一展开单项有 $k$ 个 Cayley 逆。先利用真正对易性将它们全部移到该单项的左侧，再将 (2.3) 用于右侧的 $k$ 次实际删除：
$$
\left\|
\left[\prod_{\nu=1}^k(I+N_{i_\nu})^{-1}\right]
\left[\prod_{\nu=1}^kN_{i_\nu}\right]P_{\le s}
\right\|
\le3^k e^{-\gamma(k-s)_+^4}.
$$
这里没有假设 Cayley 逆保持低孔空间。相加得到两个模型共同的界
$$
\boxed{
\|A_m^kP_{\le s}\|
\le6^k e^{-\gamma(k-s)_+^4}
\qquad(m,s,k\ge0).
}
\tag{3.4}
$$
$k=0$ 按恒等算子解释。全局 (3.1) 的级数按算子范数收敛，故先取有限和再取极限，同一界亦给
$$
\boxed{
\|T_{N/Y}^kP_{\le s}\|
\le6^k e^{-\gamma(k-s)_+^4}.
}
\tag{3.5}
$$

(3.4) 不要求低孔输入具有固定整数位置支撑。例如单孔 $e_{2^j}$ 可以随 $j$ 移到任意高物理位，仍使用同一个 $s=1$ 常数。

## 4. 低源 Gram 上界与完整逆的正确方向

对任意 $S>0$，定义同一真实头的 bosonic Gram
$$
H_m(S)=\sum_{j<2^m}\frac{(A_m^j)^*A_m^j}{S^j j!}\succeq I.
\tag{4.1}
$$
定义标量
$$
D_s(S)=\sum_{j\ge0}
\frac{(36/S)^j e^{-2\gamma(j-s)_+^4}}{j!}.
\tag{4.2}
$$
则 (3.4) 逐项给
$$
\boxed{
P_{\le s}H_m(S)P_{\le s}
\preceq D_s(S)P_{\le s}.
}
\tag{4.3}
$$
这是完整 $H_m$ 的压缩，没有先删掉其他物理头。

一个方便的显式常数是
$$
\tau=\max\{0,\log(36/S)\},\qquad
\boxed{D_s(S)\le\exp[1+s\tau+\tau^{4/3}].}
\tag{4.4}
$$
确实，若 $x=(j-s)_+$，则
$$
\tau j-2\gamma x^4
\le s\tau+\sup_{x\ge0}(\tau x-\gamma x^4)-\gamma x^4.
$$
而
$$
\sup_{x\ge0}(\tau x-\gamma x^4)
=\frac3{4^{4/3}\gamma^{1/3}}\tau^{4/3}
\le\tau^{4/3},
$$
最后一步由 $\gamma=770/256\ge27/256$。再用 $\sum_{j\ge0}1/j!=e$ 即得 (4.4)。

完整逆必须按真实 Schur 次序处理。将 $H_m$ 对
$P=P_{\le s}$ 和 $I-P$ 分块为
$$
H_m=\begin{pmatrix}A&C\\C^*&D\end{pmatrix},\qquad D\succeq I.
$$
于是
$$
PH_m^{-1}P=(A-CD^{-1}C^*)^{-1}\succeq A^{-1}.
$$
结合 (4.3)，得到
$$
\boxed{
P_{\le s}H_m(S)^{-1}P_{\le s}
\succeq D_s(S)^{-1}P_{\le s}.
}
\tag{4.5}
$$
特别对真正低孔 $f$，
$$
\langle H_m(S)^{-1}f,f\rangle
\ge D_s(S)^{-1}\|f\|^2.
\tag{4.6}
$$
这里是完整逆的二次型下界。它没有给 $H_m^{-1}f$ 的低孔支持，不能将 (4.3) 偷换成整个 $H_m$ 的上界或整个逆的上界。

对原
$$
S_m=\sum_{i\ge m}(i+1)^{-4},
\qquad
\frac1{3(m+1)^3}\le S_m\le\frac1{3m^3},
$$
固定 $s$ 时
$$
\log D_s(S_m)
=O\!\left(s\log(m+1)+(\log(m+1))^{4/3}\right).
\tag{4.7}
$$
这改善的是低源压缩的费用，不是环境 $C_m$ 的全域费用。

## 5. 完整等权池 Green 列的低孔输出

本节严格沿用完整 Green 稿中的实际模型。取 $A=A_m$、$d=2^m$，另取 $L\ge2d$ 个等权 Boolean 位，权 $t>0$，记
$$
S=Lt^2,\quad D=t\sum_{i=1}^LE_i,\quad C=A+D.
$$
池的对称占据正交基为 $u_0,\ldots,u_L$，并置
$$
a_j=t\sqrt{j(L-j+1)},\qquad
p_0=1,\quad p_j=\prod_{\nu=1}^ja_\nu.
$$
这里的 $p_j$ 不等于 bosonic 分母，故以下使用真正池 Gram
$$
H_{\rm pool}=\sum_{j<d}\frac{(A^*)^jA^j}{p_j^2},\qquad
h=H_{\rm pool}^{-1}f.
\tag{5.1}
$$
$f$ 是任意完整头 forcing，不要求低孔。已付完整最小列
$g_f=(C^*)^\dagger(f\otimes u_0)$ 为
$$
(g_f)_{j-1}
=(-1)^{j+1}p_{j-1}\sum_{k=j}^{d-1}
\frac{(A^*)^{k-j}A^kh}{p_k^2},
\qquad1\le j<d,
\tag{5.2}
$$
更高池层为零。其来源保持
$$
C^*g_f=(I-P_{\ker C})(f\otimes u_0),\qquad
g_f\perp\ker C^*.
$$
尤其不能把右侧换成未经完整核投影的 forcing。

令 $v_k=A^kh/p_k$。同一真实投影的能量是
$$
\sum_{k<d}\|v_k\|^2
=\langle H_{\rm pool}^{-1}f,f\rangle.
\tag{5.3}
$$
现在仅在输出头施加 $P_{\le s}$。每个卷积项准确满足
$$
\|P_{\le s}(A^*)^\ell\|=\|A^\ell P_{\le s}\|.
\tag{5.4}
$$
又 $L\ge2d$ 给 $a_\nu^2\ge S\nu/2$，故 (5.2) 的第 $\ell=k-j$ 个系数至多
$$
\sqrt{\frac2S}\,
\frac{\|A^\ell P_{\le s}\|(2/S)^{\ell/2}}{\sqrt{(\ell+1)!}}.
$$
在真实池层 Hilbert 直和中用移位的 $\ell^1$--$\ell^2$ 卷积界，再用一次 Cauchy--Schwarz，得到
$$
\begin{aligned}
\|(P_{\le s}\otimes I)g_f\|^2
&\le\frac4S
\left[\sum_{\ell<d}
\frac{\|A^\ell P_{\le s}\|^2(4/S)^\ell}{\ell!}\right]
\langle H_{\rm pool}^{-1}f,f\rangle\\
&\le\frac4S D_s(S/4)\,
\langle H_{\rm pool}^{-1}f,f\rangle.
\end{aligned}
\tag{5.5}
$$
因此
$$
\boxed{
\|(P_{\le s}\otimes I)(C^*)^\dagger(f\otimes\Omega)\|^2
\le
\frac4S
\exp[1+s\tau_4+\tau_4^{4/3}]
\,\langle H_{\rm pool}^{-1}f,f\rangle,
\quad
\tau_4=\max\{0,\log(144/S)\}.
}
\tag{5.6}
$$
右端也可用 $\|f\|^2$ 放大。

这是真正完整最小列的低孔输出界，且保留了任意 forcing 的全部 nuisance 和同一个 $H_{\rm pool}^{-1}$。证明从未假设 $h=H_{\rm pool}^{-1}f$ 低孔。因只投了输出，(5.6) 不给其余输出的范数，也不直接给原连续非等权尾的完整列界。把额外强位并入头时，还须另证该扩头的输入幂界，不能将扩头幂自动换为 $A_m$。

## 6. N 型的低孔测试与同一 bosonic 核反馈行

本节只对原 N 型主张孔数三角性。Y 型的 Cayley 伴随可以一次增加多个物理孔，不作相同断言。

在共同 Fock 空间中，令 $a_0$ 为原尾归一集体 annihilator，$P_0$ 为其零占据投影。沿用
$$
\mathcal R_mh
=\sum_{j<d}\frac{(-A_m)^j(a_0^*)^jh}{S_m^{j/2}j!},
\qquad
H_m=\mathcal R_m^*\mathcal R_m,
\qquad
P_m^{\rm B}=\mathcal R_mH_m^{-1}\mathcal R_m^*.
\tag{6.1}
$$
$h$ 位于集体零占据空间，所有横向占据均保留。

对 N 型，每个 $N_{i,m}^*$ 在整数头上加 $2^i$，因此至多增加一个二进位孔。故 $(A_m^*)^j$ 至多增加 $j$ 个头孔。另一方面，$a_0^j$ 恰降低尾总粒子数 $j$，$P_0$ 保持尾总粒子数。因此
$$
\mathcal R_m^*
=P_0\sum_{j<d}\frac{(-A_m^*)^ja_0^j}{S_m^{j/2}j!}
$$
把总物理孔数不超过 $s$ 的输入送到总孔数不超过 $s$ 的集体零占据源。此式可先在有限粒子核心上核对；$P_0a_0^j$ 只读取集体占据 $j$，有界，故所需投影身份延伸到整个相关 Hilbert 空间。

取任意总孔数不超过 $s$ 的真实物理测试 $f$，置
$$
u=\mathcal R_m^*f,\qquad v=P_m^{\rm B}f.
$$
于是 $u$ 的头孔数不超过 $s$，且 $N_{i,m}^*u$ 的头孔数不超过 $s+1$。由完整核伴随公式及核不变性，
$$
P_m^{\rm B}N_{i,m}^*f
=P_m^{\rm B}N_{i,m}^*v
=\mathcal R_mH_m^{-1}N_{i,m}^*u.
\tag{6.2}
$$
所有列保留同一 $u$ 和完整 $H_m^{-1}$。

原归一 bit 的无进位项还给比已有 $(I-P_{\rm top})$ 更精确的计数：
$$
\sum_{i<m}N_{i,m}N_{i,m}^*
\succeq mI-\mathcal N_{\rm head}.
\tag{6.3}
$$
确实，输入整数头每个零位都贡献一个系数恰为 $1$ 的创建；其余 carry 项非负。因此若 $m>s$，对低孔 $u$ 有
$$
\sum_{i<m}\|N_{i,m}^*u\|^2\ge(m-s)\|u\|^2.
$$
将 (4.5) 用于每个实际低孔 $N_{i,m}^*u$，横向空间只作恒等张量，得到
$$
\boxed{
\sum_{i<m}\|P_m^{\rm B}N_{i,m}^*f\|^2
\ge\frac{m-s}{D_{s+1}(S_m)}\|\mathcal R_m^*f\|^2
\ge\frac{m-s}{D_{s+1}(S_m)}\|P_m^{\rm B}f\|^2.
}
\tag{6.4}
$$
最后一步用 $H_m^{-1}\preceq I$，即
$\|P_m^{\rm B}f\|^2=\langle u,H_m^{-1}u\rangle\le\|u\|^2$。

(6.4) 是固定低孔测试的真实全行下界，成本不再使用整个环境 $C_m$。它仍不是原 $w\in W$ 的全行上界；一般 $w$ 的高孔尾可能没有足以与该系数相乘的速率。特别，不能仅用固定测试逼近 $w$，再省掉行长和压缩逆所产生的误差。

## 7. 当前可用范围

本文新增的是实际源孔数进入借位计数后的四次幂衰减。其后果分别保持了：
1. 原 N/Y 头及全局算子的真实低孔输入；
2. 完整 bosonic Gram 的低源压缩及先完整逆、再压缩的正确二次型方向；
3. 完整等权池最小 Green 列的低孔输出、原 forcing 和完整核反馈；
4. N 型固定低孔测试的同源归一 bit 反馈行。

原两费、连续尾强块的普通右费封口，以及原 $W$ 的移动整行统一上界，均未由这些结论自动支付。后续应用需要保留相应残差增加的真实孔数和完整 inverse/Schur，不能把本稿的低输入或低输出条件移过一个未控制的完整投影。
