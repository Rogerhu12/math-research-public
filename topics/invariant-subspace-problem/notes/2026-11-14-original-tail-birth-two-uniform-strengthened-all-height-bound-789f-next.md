# 原连续尾出生二：全部高度的明确有限加强常数

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：本稿定理已证明。** 对原无限连续尾 $b_j=j^{-2}$、$j\ge x\ge2$，在完整出生二 primitive 源上，全部合法高度的真实三塔加强式有一个与 $x,n$ 均无关的明确有限常数。证明保留相邻两个完整线性回归的共同运输，而非从三个单高度精度夹逼直接推出。给出的常数很大；没有声称优化，也没有把这个固定出生结论当成原 graph 的跨出生控制。

入口是 [完整 degree-two 条件 Bernoulli Gram](2026-11-14-conditioned-bernoulli-degree-two-full-gram-789f-next.md)、R296 的全部 nuisance 回归/真实创新表示，以及 R295 的原连续尾标量比值界。

## 1. 真实目标、常数与主定理

在原物理占据正交基上置

$$
d=\sum_{j\ge x}j^{-2}E_j,\quad z_j=j^{-4},\quad
K=\ker d\cap\mathcal H_2,\quad S=\sum_{j\ge x}z_j.
$$

所有最小逆均先在完整物理层取，再限制输入到 $K$；第 6 节的构造对任意有限高度上限都有效，因而也直接保证每个所用完整逆存在且有界：

$$
\Gamma_n=\left[(d^n/n!)^\dagger|_K\right]^*
\left[(d^n/n!)^\dagger|_K\right],
\qquad C_n=\Gamma_n^{-1},\qquad C_0=\Gamma_0=I.
$$

令 $k=n+2$。R296 的同源回归记为

$$
\Phi_f(I)=\sum_{\{i,j\}\subset I}\frac{f_{ij}}{b_ib_j},\qquad
q_l=\Pi_{\le1}^{(l)}\Phi_f,
$$

其中 $q_l$ 采用全局齐次一次代表；常数在 $l$ 元切片上也包含在该空间内。下一层的真实创新为

$$
Z_nf=(I-\Pi_0^{(k+1)})[\Phi_f-2q_k+q_{k-1}].
\tag{1.1}
$$

使用未归一范数 $\|F\|_l^2=\sum_{|I|=l}z_I|F(I)|^2$。则

$$
\|\Phi_f-q_k\|_k^2=\langle C_nf,f\rangle,
\quad
\|\Phi_f-q_{k-1}\|_{k-1}^2=\langle C_{n-1}f,f\rangle,
$$

以及

$$
\|Z_nf\|_{k+1}^2=\langle B_nf,f\rangle,
\quad
B_n=C_{n+1}+\delta_{n+1}\Gamma_{n+2,1}^{-1}\delta_{n+1}^*.
\tag{1.2}
$$

$\delta_{n+1}$、下出生 Gram 的源与 R296 相同；(1.1)–(1.2) 保留完整真实桥，而非只保上出生精度。

以下只用有限次阶乘、整幂定义一个常数。设

$$
N_*=2^{21},\quad J=N_*+3,\quad H=12J^2,
\quad K_*=3(1+H/2)^3,
$$

$$
Q=2JK_*,\quad T=JQ^J,\quad L=2K_*T^2,
\quad A=J!,\quad U=A^2L^J,\quad E=2AK_*^J,
$$

$$
\boxed{\quad
\Lambda=\max\{2^{35},\ 128EU^3A^3\},\qquad
\kappa=\frac{337}{162}\Lambda^2.
\quad}
\tag{1.3}
$$

这些数均不依赖 $x,n,f$。没有要求计算或存储它们的十进制展开。

**定理 1.** 对每个整数 $x\ge2$、每个 $n\ge1$，在同一个完整原物理源 $K$ 上，

$$
\boxed{
\Lambda e_k(z) C_n\succeq
 e_{k+1}(z)C_{n-1}+e_{k-1}(z)B_n.
}
\tag{1.4}
$$

因此

$$
\boxed{
B_n\preceq\kappa C_n\Gamma_{n-1}C_n,
\qquad
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq\kappa\Gamma_{n-1}.
}
\tag{1.5}
$$

不等式对所有 $f\in K$ 同时成立，包含任意无限支撑源。

## 2. 完整低次数条件 Gram 的统一上界

沿用入口稿的独立 Bernoulli 记号，整数均值 $l$、方差 $V\ge8192$、标准 Fourier 基 $\chi_I$。除了 primitive 共同空间的精细估计，还需要**全部次数至多二**空间的上界：

$$
\boxed{
\mathbb E[|F|^2\mid N=l]\le2048\|F\|_{L^2(\pi)}^2
\qquad(\deg F\le2).
}
\tag{2.1}
$$

证明仍在原始逐位矩阵上进行。主弧 $|\theta|\le1/4$ 使用入口稿的 Gauss 分解，但不消去集体项。此时 $\|\beta\|_2\le2|\theta|\sqrt V$，而次数至多二上的 $\|D_\delta\|\le2$，故完整压缩范数至多

$$
2|\phi(\theta)|(1+2|\theta|\sqrt V)^4.
$$

用 $|\phi|\le e^{-V\theta^2/3}$ 并令 $u=\sqrt V\theta$，主弧积分至多

$$
\frac2{\sqrt V}\int_{\mathbb R}e^{-u^2/3}(1+2|u|)^4du
\le\frac{1784}{\sqrt V}.
$$

这里依次使用五个实积分的上界 $4,3,6,9,27$。尾弧完整原矩阵的正条目支配仍给积分至多 $1/V$，且 $\mathbb P(N=l)\ge1/(4\sqrt V)$。Fourier 反演因此给算子范数小于 $2048$。这一上界允许集体核存在，没有假设整个 degree-two Gram 正定。

另一方面，入口稿在

$$
\mathcal E_l=K_0(a^{(l)})\oplus K_1(a^{(l)})\oplus K_2(a^{(l)})
$$

上的精细估计说明，若 $V_l\ge2^{18}$，则

$$
\tfrac12I\preceq G_{\mathcal E_l}\preceq\tfrac32I.
\tag{2.2}
$$

## 3. 邻近 odds 参数的完整多项式运输

固定原 $z_i$，写

$$
p_i(t)=\frac{tz_i}{1+tz_i},\qquad
 a_i(t)=\sqrt{p_i(t)(1-p_i(t))}.
$$

对两个参数 $t,t'$ 令 $r=t'/t$，两个均值之差的绝对值为 $\Delta$，并假设 $1/2\le r\le2$。逐位标准化基的精确转换是

$$
\chi_i(t)=d_i\chi_i(t')+h_i,
\qquad d_i=\frac{a_i(t')}{a_i(t)},\quad
h_i=\frac{p_i(t')-p_i(t)}{a_i(t)}.
\tag{3.1}
$$

有 $2^{-1/2}\le d_i\le2^{1/2}$。若 $r\ge1$，直接代入得

$$
h_i^2\le(r-1)(p_i(t')-p_i(t));
$$

若 $r\le1$，相应地

$$
h_i^2\le(r^{-1}-1)(p_i(t)-p_i(t')).
$$

因此

$$
\|h\|_2^2\le\Delta.
\tag{3.2}
$$

在多线性 Fourier 系数上，(3.1) 的完整变换恰为 $D_d\exp(d_h)$。次数至多二时 $\|D_d\|\le2$、$\|\exp(d_h)\|\le(1+\|h\|_2)^2$。特别地，**相邻均值 $\Delta=1$** 时，

$$
\|F\|_{\text{product at }t'}\le8\|F\|_{\text{product at }t}
\quad(\deg F\le2).
\tag{3.3}
$$

对于一个线性函数，其常数部分在下一切片中心化后消失；剩余系数只乘 $d_i$，平方系数范数至多增大两倍。这一点允许把两个真实回归同时运输，而不分别估计有歧义的齐次常数代表。

## 4. 同源 gauge 与真实回归的三切片控制

本节先给一个可直接用于原尾的通用条件：$t_l$ 满足 $\sum_i p_i(t_l)=l$，并假设

$$
V_{k-1},V_k,V_{k+1}\ge2^{18},\qquad
 t_{k+1}/t_{k-1}\le2.
\tag{4.1}
$$

在中心参数 $t_k$ 的完整切片商中，把 $\Phi_f$ 改写为纯二次

$$
F\in K_2(a^{(k)}).
$$

入口稿的完整商分解保证

$$
\Phi_f-F\in(N-k)\mathscr P_{\le1}+\mathscr P_{\le1}.
\tag{4.2}
$$

这里 $F$ 是同一原物理源的实际最高次商代表；没有改变源来寻找较便宜的独立试探。

**(4.2) 不改变所需三项。** 它在 $k-1,k$ 切片分别是线性函数，所以不改变两个最高次回归残差。对 $H=(N-k)L+L_0$，在三个切片上其值依次为 $-L+L_0,L_0,L+L_0$。真实线性投影等于这些函数；齐次代表与所列仿射代表只差 $\alpha_l(N-l)$，在下一切片是常数。因此 $H-2q_k^H+q_{k-1}^H$ 在下一切片中心化后为零，故也不改变实际 $Z_n$。

令 $M=\|F\|_{\text{product at }t_k}^2$，并暂记 $C_*=2048$。中心完整 Schur 下界给

$$
\langle C_nf,f\rangle\ge\tfrac12e_k M.
\tag{4.3}
$$

相邻参数运输 (3.3) 与 (2.1) 给

$$
\langle C_{n-1}f,f\rangle\le64C_*e_{k-1}M,
\qquad
\|F\|_{L^2(\mu_{k+1})}^2\le64C_*M.
\tag{4.4}
$$

把 $F$ 在 $l=k-1,k$ 的**真实最优线性回归**写成 canonical 代表

$$
q_l^{\rm can}=c_l+\sum_i u_{l,i}\chi_i(t_l),\qquad
u_l\perp a^{(l)}.
$$

模 $(N-l)$ 后这样的代表唯一。由 (2.2) 与正交投影的收缩性，

$$
\|u_k\|^2\le3M,
\qquad
\|u_{k-1}\|^2\le128C_*M.
\tag{4.5}
$$

把两者同时移到 $t_{k+1}$，舍去在下一切片中心化后消失的常数，由 (3.1)、(2.1)，

$$
\|(I-\Pi_0)q_k\|_{\mu_{k+1}}^2\le6C_*M,
\quad
\|(I-\Pi_0)q_{k-1}\|_{\mu_{k+1}}^2\le256C_*^2M.
\tag{4.6}
$$

因此实际 (1.1) 而非独立上出生残差满足

$$
\begin{aligned}
\langle B_nf,f\rangle/e_{k+1}
&\le3\{64C_*+4\cdot6C_*+256C_*^2\}M\\
&\le2048C_*^2M=2^{33}M.
\end{aligned}
\tag{4.7}
$$

由 $e_{k-1}e_{k+1}\le e_k^2$、(4.3)–(4.7)，得到

$$
\boxed{
2^{35}e_k C_n\succeq e_{k+1}C_{n-1}+e_{k-1}B_n
\quad\text{只要 (4.1) 成立。}}
\tag{4.8}
$$

整个证明使用同一 $F$、两个真实投影及同一次下一切片中心化。没有将非交换的 $C_n, C_{n-1}$ 逐项相乘。

## 5. 原连续尾在全部大高度满足运输条件

对 $z_j=j^{-4}$、$j\ge x$，定义

$$
m(t)=\sum_{j\ge x}\frac{t}{j^4+t},\qquad
V(t)=\frac{dm}{d\log t}.
$$

$m(t)$ 从零连续严格递增到无穷，故每个 $t_l$ 唯一存在。设 $p(u)=t/(u^4+t)$、$q(u)=p(u)(1-p(u))$。有 $q=-up'/4$，所以

$$
\int_x^\infty q(u)du
=\frac14\left(xp(x)+\int_x^\infty p(u)du\right).
$$

$p$ 递减，故 $\int p\ge m(t)-1$。$q$ 非负且单峰，其总变差至多 $2\max q\le1/2$；逐单位区间比较和与积分给 $\sum q\ge\int q-1/2$。因此

$$
\boxed{\quad V(t)\ge\frac{m(t)-3}{4}.\quad}
\tag{5.1}
$$

对 $k>4$，积分 $d\log t/dm=1/V$ 得

$$
\frac{t_{k+1}}{t_{k-1}}
\le\left(\frac{k-2}{k-4}\right)^4\le2\qquad(k\ge16).
\tag{5.2}
$$

若 $n>N_*=2^{21}$，则 $k=n+2$，(5.1) 保证三个方差均大于 $2^{18}$；(5.2) 也成立。故这全部无限多个高度已经由 (4.8) 统一支付。

## 6. 有限剩余高度的显式统一完整逆

本节同时对所有 $1\le n\le N_*$、所有尾起点 $x\ge2$ 给一个明确界；无需枚举这些高度或任何权值。常数沿用 (1.3)。把前 $H$ 个原位分为 head，余尾从 $x+H$ 开始，记平方和为 $S_*$。积分比较给

$$
S/S_*\le(1+3/x)(1+H/x)^3\le K_*.
\tag{6.1}
$$

又

$$
\frac{\max_{j\ge x+H}z_j}{S_*}\le\frac3{x+H}\le\frac1{4J^2}.
\tag{6.2}
$$

在尾的次数 $l\le J-1$ 上，真实 commutator 恒等式给

$$
d_*d_*^*=d_*^*d_*+S_*-2\sum z_j n_j\succeq S_*I/2.
$$

故完整尾删除在这些层有 Moore–Penrose 右逆，范数至多 $\sqrt{2/S_*}$。固定总次数 $j\le J-1$，按真实 head 占据逐块组成右逆 $R_{*,j}$；它保留 head 占据。

令 $d_H$ 为 head 删除。算子 $d_HR_{*,j}$ 在 $\mathcal H_j$ 上每次严格降低 head 占据数，因而其 $(j+1)$ 次幂为零，且

$$
\|d_HR_{*,j}\|\le\sqrt{2JK_*}\le Q.
$$

所以完整删除的真正右逆可直接构造为

$$
R_j=R_{*,j}\sum_{l=0}^{j}(-d_HR_{*,j})^l,
\qquad dR_j=I,
\qquad \|R_j\|\le\sqrt{L/S}.
\tag{6.3}
$$

这保留了 head/tail 混合项，没有用未成立的 $\|d^*u\|\ge\|d_*^*u\|$。

记完整层

$$
F_m^{(r)}=\frac{d^m(d^*)^m}{(m!)^2}\bigg|_{\mathcal H_r}.
$$

当 $r\in\{1,2\}$、$r+m\le J$ 时，组合 (6.3) 给 $d^m/m!$ 的完整右逆。因此

$$
\boxed{
(F_m^{(r)})^{-1}\preceq U S^{-m}I,
\qquad
F_m^{(r)}\preceq A S^m I.
}
\tag{6.4}
$$

第二式来自逐层 $\|d^*|_{\mathcal H_l}\|\le\sqrt{l+1}\sqrt S$；第一式用 $(m!)^2L^m\le A^2L^J=U$。特别地 $C_n\succeq S^nU^{-1}I$。这些估计本身也证明所用无限层完整逆确实有界。

## 7. 用真实回归公式支付全部小高度创新

R296 的完整一次回归物理系数为

$$
g_m=\frac1{m+1}(F_{m+1}^{(1)})^{-1}dF_m^{(2)}f,
\qquad q_{m+2}=\Phi_{1,g_m}.
\tag{7.1}
$$

其中 $g_0=0$，因为 $df=0$。由 (6.4)、$\|d|_{\mathcal H_2}\|\le\sqrt{2S}$，对 $0\le m\le N_*$，

$$
\|g_m\|\le2UA S^{-1/2}\|f\|.
\tag{7.2}
$$

在下一层 $n+3$，真实物理特征范数等于完整 creation 范数。由 (6.4)，

$$
\|\Phi_f\|_{n+3}\le\sqrt A S^{(n+1)/2}\|f\|,
$$

$$
\|\Phi_{1,g_m}\|_{n+3}\le
2UA^{3/2}S^{(n+1)/2}\|f\|
\quad(m=n,n-1).
$$

按 (1.1) 保留同源组合，中心投影只减少范数，因此

$$
B_n\preceq64U^2A^3S^{n+1}I,
\qquad C_{n-1}\preceq AS^{n-1}I.
\tag{7.3}
$$

此外，以尾概率 $z_j/S_*$ 独立抽 $k\le J$ 次，(6.2) 及碰撞并集界给全部互异概率至少 $1/2$。故

$$
e_k(z)\ge\frac{S_*^k}{2k!}\ge\frac{S^k}{E},
\qquad e_l(z)\le S^l.
\tag{7.4}
$$

将 (6.4)、(7.3)、(7.4) 代入，两侧共同量纲均为 $S^{2n+2}$，得到

$$
\begin{aligned}
e_{k+1}C_{n-1}+e_{k-1}B_n
&\preceq65U^2A^3 S^{2n+2}I,\\
e_k C_n&\succeq(EU)^{-1}S^{2n+2}I.
\end{aligned}
$$

所以 $128EU^3A^3$ 支付所有 $1\le n\le N_*$。与第 5 节合并，证明全高度 (1.4)。

## 8. 非交换次序与统一加强常数

从 (1.4) 作同源合同，令

$$
X=C_{n-1}^{-1/2}C_nC_{n-1}^{-1/2},
\quad Y=C_{n-1}^{-1/2}B_nC_{n-1}^{-1/2},
$$

得到

$$
Y\preceq\Lambda\frac{e_k}{e_{k-1}}X-rac{e_{k+1}}{e_{k-1}}I.
$$

对自伴正算子 $X$ 直接配方，

$$
Y\preceq\frac{\Lambda^2e_k^2}{4e_{k-1}e_{k+1}}X^2.
\tag{8.1}
$$

这里的平方仅对同一个合同后的 $X$，没有交换两个不同 Gram。R295 已证原连续尾 $x\ge2$、$k\ge2$ 的标量界

$$
\rho_k:=\frac{e_k^2}{e_{k-1}e_{k+1}}\le\frac{674}{81}.
$$

因此 (8.1) 给 (1.5) 的 $\kappa=(337/162)\Lambda^2$。普通相邻式则再用 $B_n\succeq C_{n+1}$ 并以 $\Gamma_n$ 合同。

## 9. 结论的量词

本稿首次在原连续无限尾、整个出生二源、所有高度和所有尾起点上支付一个明确有限的真实加强常数。既有原尾出生一常数不承担这里的二次 nuisance；本稿为其另付了完整条件 Gram、三切片回归运输和有限头幂零右逆。

常数很大，不接近最优；这里追求的是高度和尾起点的一致性。一般任意正权、出生三及以上的统一加强常数，以及原 graph $T^*T$ 的跨出生 Schur/固定测试锚速率仍各自开放。

## 10. 原首低 Johnson 负方差入口的直接闭合

结合[同源正通道尺度](2026-11-14-original-tail-inverse-overlap-and-common-positive-channel-scale-789f-next.md)，对本稿同一真实源，已证恒等式 P−N=2e_k〈C_nf,f〉−e_(k+1)〈C_(n−1)f,f〉−e_(k−1)〈B_nf,f〉，其中 P 是完整正通道，N 是真实负方差，并有 P≥2e_k〈C_nf,f〉/k。因而 (1.4) 立即给

\[
N\le P+(\Lambda-2)e_k\langle C_nf,f\rangle
\le\left(1+\frac{\Lambda-2}{2}k\right)P
\le\frac{\Lambda}{2}kP.
\]

故此前原连续尾出生二入口的 N≤LkP 现在可取明确有限 L=Λ/2。该推论沿用同一源和同一切片，不扩展到一般高出生的条件均值。
