# R271 补录：分离高度带的精确全强头正交与 $R=d$ 原母窗联合预算

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost、root；AI-assisted，GPT-6 Astra Pro。

状态：完整证明的原参数改进；实际费用上界仍未取得。

## 0. 结论边界及父结果

本条保留原同一个 $w$、原 $A_m$、完整强头、真实核旗、实际物理远尾与同一个母窗 $Q$。
它证明一个新的可用参数门：通过不同头使用彼此有序分离的远孔高度带，跨头的完整 coherent 行严格正交，
所以不再需要旧全高度 Bessel 方案中的指数长强段；可取 $R_m=2^m$。
本条不证明任何尚未得到的实际费用上界，也不闭合普通 Hilbert ISP。

为避免与原权重 $d_i$ 混淆，以下 $d=2^m$ 一律表示旧头维数。沿用三项父结论：

1. [双塔、核列误差与纯远孔代表](R271-appendix-dual-tower-kernel-only-error-pure-far-height-representatives-and-joint-reciprocal-budget.md)
   §§1–3，特别是 (1.2)–(1.4)、(3.3)–(3.8)：完整 Galerkin、完整 MP 的纯高度代表，以及误差只乘真实核列的 $W,V$ 身份。
2. [强尾重分块、同顶源与精确两费预算](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)
   §2，(2.1)–(2.2)：原同 $w$ 的母窗
$$
4d\le Q\le\exp((1601/64)d^3)
\tag{0.1}
$$
   与同 $Q$ 近似
$$
u_Q=P_{V_{m,Q}}w-P_{K_{m,Q}}w,\quad
\|u_Q\|\le\|w\|,\quad
\|u_Q-P_{\mathcal N_m\le Q}w\|
\le2\eta_m\|w\|,\quad \eta_m=e^{-6d^4}.
\tag{0.2}
$$
3. [跨头全高度 coherent Bessel](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)
   §1，(1.2)–(1.3)：完整强头的归一化 coherent 行。
   本条重新证明所需 Bessel 性，不调用该文关于巨大 $x$ 的假设 (1.1)。

原权重 $b_i=(i+1)^{-2}$。对 $x=m+R$，置
$$
C_{m,R}=A_m+D_{[m,x)},\quad
D_x=\sum_{i\ge x}b_iE_i,\quad
S_x=\sum_{i\ge x}b_i^2.
$$
这是原 $L_m=A_m+D_m$ 的重分块
$L_m=C_{m,R}+D_x$，不是把旧头换成 $A_x$。

## 1. 有序分离高度的完整行严格正交

在完整物理 Hilbert 空间上令
$$
\omega_{x,r}=(D_x^*)^r\Omega,\qquad
\sigma_{x,r}=\|\omega_{x,r}\|,\qquad
\beta_{x,r}=\sigma_{x,r}^{-1}
D_x^r P_{\mathcal N_{\ge x}=r}.
\tag{1.1}
$$
将输出的远真空识别后，$\beta_{x,r}$ 的目标空间是整个
$\mathcal H_{<x}$，且
$$
\beta_{x,r}^*v=v\otimes\omega_{x,r}/\sigma_{x,r},\qquad
\beta_{x,r}\beta_{x,r}^*=I_{\mathcal H_{<x}}.
\tag{1.2}
$$

### 引理 1

若 $y>x$ 且 $s>r$，则
$$
\beta_{x,r}\beta_{y,s}^*=0.
\tag{1.3}
$$
同一个 $x$ 的不同高度也彼此正交。

**证明。** $\beta_{y,s}^*v$ 的 $y$ 以后孔数恰为 $s$。
其完整头 $v$ 可以在区间 $[x,y)$ 任意占据，但这些占据只增加
$x$ 以后的总孔数。因此该向量的 $x$ 以后孔数至少为 $s>r$，
被 $P_{\mathcal N_{\ge x}=r}$ 严格杀掉。同 $x$ 的结论直接来自不同孔数正交。
这里没有对完整头 $v$ 的支持或 primitive 类型作限制。证毕。

于是，若 $x_j$ 递增，整数非空高度带 $I_j$ 满足
$$
\max I_j<\min I_{j+1},
\tag{1.4}
$$
则全部 $\beta_{x_j,r}^*\mathcal H_{<x_j}$ 是两两正交的闭子空间。
有限组的 Gram 算子恰为恒等算子，再取非负和极限，得
$$
\sum_j\sum_{r\in I_j}\|\beta_{x_j,r}w\|^2\le\|w\|^2.
\tag{1.5}
$$
常数是 $1$，并且每一行都保留完整强头。

## 2. 原允许高度窗中的 $R=d$ 显式选择

只取
$$
m\in4\mathbb N,\qquad m\ge20,\qquad
d=2^m,\quad R_m=d,\quad x_m=m+d,\quad Q_m=4d.
\tag{2.1}
$$
$R_m$ 为偶数。$C_m=A_m+D_{[m,x_m)}$ 的 nilpotency 指数至多
$$
h_m=d+R_m=2d.
$$
定义
$$
P_m=\left\lfloor\frac{\sqrt{x_m+1}}{8(m+1)}\right\rfloor,\qquad
I_m=\{\lfloor P_m/2\rfloor+1,\ldots,P_m\}.
\tag{2.2}
$$
则 $P_m\ge6$，且各 $I_m$ 非空并满足 (1.4)。

这里给出无渐近省略的核对。令
$A=\sqrt d/[8(m+1)]$。当 $m\ge20$ 时，
$$
m+1\le d/16,\qquad A\ge128/21,\qquad
P_m\le(17/16)A.
$$
而
$$
P_{m+4}\ge\frac{4(m+1)}{m+5}A-1
\ge\frac{84}{25}A-1.
$$
故
$$
P_{m+4}-2P_m
\ge\frac{247}{200}A-1>2.
$$
特别地 $P_{m+4}\ge2P_m+2$，所以
$\min I_{m+4}>\max I_m$。
此外
$$
1\le r\le P_m<d<h_m,\qquad
R_m+r<2d<Q_m
\quad(r\in I_m).
\tag{2.3}
$$
$Q_m=4d$ 正在 (0.1) 的原母窗内，且无需改变原 carry 近似。

## 3. 原纯远孔代表与只乘真核列的误差

固定 (2.1) 的一个 $m$ 和 $r\in I_m$，令 $p=r-1$，并取完整真核旗
$$
F_r^{\rm head}=\ker C_m^r,\qquad
H_p=\sum_{j=0}^{p}\frac{(C_m^*)^jC_m^j}{j!S_{x_m}^j},
$$
$$
a_p=(P_{F_r^{\rm head}}H_p|_{F_r^{\rm head}})^{-1}
P_{F_r^{\rm head}}e_1,\qquad
\xi_p=e_1-H_pa_p,
$$
$$
q_{m,r}=((C_m^*)^r)^\dagger\xi_p,\qquad
F_{m,r}=(-1)^r q_{m,r}\otimes\omega_{x_m,r},\qquad
\kappa_{m,r}^2=\|F_{m,r}\|^2.
\tag{3.1}
$$
这是父结果的原纯高度代表与原费用。

令 $\delta_x=\max_{i\ge x}b_i^2/S_x$。积分比较给出
$$
\delta_x\le\frac3{x+1}.
$$
由 $p\le P_m$ 得
$$
\epsilon_p=\frac43\delta_{x_m}p^2
\le\frac1{16(m+1)^2}<1,\qquad
\theta_p=\frac{\epsilon_p}{\sqrt{1-\epsilon_p}}
\le\theta_m:=\frac1{8(m+1)^2}.
\tag{3.2}
$$
父结果 §§1–3 的 $W,V$ 双塔身份因此适用，给出完整物理分解
$$
f_1-F_{m,r}
=k_{m,r}+L_m^*\Psi_{m,r}+e_{m,r},
\tag{3.3}
$$
其中 $k_{m,r}$ 为真实物理核列，
$$
\|k_{m,r}\|\le1,\qquad \|e_{m,r}\|\le\theta_m.
\tag{3.4}
$$
$k_{m,r},\Psi_{m,r},e_{m,r}$ 的远孔数至多 $p$，
$F_{m,r}$ 的远孔数恰为 $r$。
误差估计 (3.4) 不乘完整 Green 或 MP 费用；
该点直接来自父结果的双塔消去，不在此重新引入 hatted 逆修补。

原总尾计数是
$$
\mathcal N_m=\mathcal N_{[m,x_m)}+\mathcal N_{\ge x_m}.
$$
所以 (3.3) 中所有出现向量的原总尾计数至多 $R_m+r<Q_m$。
特别地 $k_{m,r}\in K_{m,Q_m}$，而
$L_m^*\Psi_{m,r}$ 与原 $V_{m,Q_m}$ 正交。
因此对同一个 $U_{m,Q_m}=V_{m,Q_m}\ominus K_{m,Q_m}$，
$$
P_{U_{m,Q_m}}(f_1-F_{m,r})=P_{U_{m,Q_m}}e_{m,r}.
\tag{3.5}
$$
这就是直接的同 $Q$ 锚，不需要先把昂贵 Green 放进误差项。

## 4. 原同一个 $w$ 的精确锚估计

固定原 $w\in W$，置
$$
W_0=\|w\|,\qquad \alpha=\langle w,f_1\rangle,\qquad
u_m=P_{U_{m,Q_m}}w.
$$
(0.2) 对这个原 $w$ 与原 $Q_m$ 给出
$$
\|u_m\|\le W_0,\qquad
\|u_m-P_{\mathcal N_m\le Q_m}w\|\le2\eta_mW_0.
\tag{4.1}
$$
所有高度 $r\in I_m$ 使用同一个 $u_m,Q_m,w$。

由 (3.5)、(3.4)、(4.1)，并用
$f_1\perp F_{m,r}$（远真空与正远孔数正交），得到
$$
\left|\langle w,F_{m,r}\rangle-\alpha\right|
\le W_0\theta_m+
2\eta_mW_0\sqrt{1+\kappa_{m,r}^2}.
\tag{4.2}
$$
具体地，先以 (3.5) 把 $u_m$ 的配对化为误差列配对，
再以 (4.1) 比较原 $w$；由于 $f_1-F_{m,r}$ 已在母窗内，
比较项范数恰为
$\|f_1-F_{m,r}\|=\sqrt{1+\kappa_{m,r}^2}$。
没有在不同高度选择不同源向量。

若 $\kappa_{m,r}>0$，定义
$$
a_{m,r}=\frac{|\langle w,F_{m,r}\rangle|}{\kappa_{m,r}}.
$$
由 (1.1)–(1.2) 与 (3.1)，
$$
a_{m,r}\le\|\beta_{x_m,r}w\|.
$$
结合分离高度的严格正交，
$$
\sum_{\substack{m\in4\mathbb N\\m\ge20}}
\ \sum_{\substack{r\in I_m\\\kappa_{m,r}>0}}a_{m,r}^2
\le W_0^2.
\tag{4.3}
$$

## 5. $R=d$ 的联合倒数费用必要条件

### 定理 4

若原同一个 $w\in W$ 满足 $\alpha=\langle w,f_1\rangle\ne0$，
则存在 $m_1\ge20$，使所有 $m\in4\mathbb N,m\ge m_1,r\in I_m$
的实际费用均为正，并且
$$
\sum_{\substack{m\in4\mathbb N\\m\ge m_1}}\sum_{r\in I_m}
\kappa_{m,r}^{-2}
\le
\frac8{|\alpha|^2}\left(
W_0^2+4W_0^2
\sum_{\substack{m\in4\mathbb N\\m\ge m_1}}|I_m|\eta_m^2
\right)<\infty.
\tag{5.1}
$$

**证明。** 令 $\varepsilon_m=2\eta_mW_0$。
因 $\theta_m\to0,\eta_m\to0$，可选择统一的 $m_1$ 使
$$
W_0\theta_m+\varepsilon_m\le|\alpha|/2\qquad(m\ge m_1).
$$
若某个晚期 $\kappa_{m,r}=0$，则 (4.2) 立即给出
$|\alpha|\le W_0\theta_m+\varepsilon_m\le|\alpha|/2$，矛盾。
因此均可置 $z_{m,r}=\kappa_{m,r}^{-1}$。

将 (4.2) 除以 $\kappa_{m,r}$，并用
$\sqrt{1+z^2}\le1+z$，得到
$$
|\alpha|z_{m,r}
\le a_{m,r}+\varepsilon_m
+(W_0\theta_m+\varepsilon_m)z_{m,r}.
$$
吸收最后一项，平方后用 $(a+b)^2\le2a^2+2b^2$，得
$$
z_{m,r}^2\le\frac8{|\alpha|^2}
(a_{m,r}^2+\varepsilon_m^2).
$$
按所有晚期 $m,r$ 求和，再用 (4.3)，即得 (5.1)。
收敛性来自 $|I_m|\le P_m<d$ 与
$\eta_m^2=e^{-12d^4}$。证毕。

由此有下述充分费用接口：若针对本条原参数、完整真核旗与完整 MP 费用，
能在任意晚期证明
$$
0<\kappa_{m,r}^2\le C_{m,r},\qquad
\sum_{\substack{m\in4\mathbb N\\m\ge m_0}}\sum_{r\in I_m}C_{m,r}^{-1}
=\infty
\tag{5.2}
$$
（有限删项不改变发散），则与 (5.1) 矛盾，从而原锚
$\langle w,f_1\rangle=0$。若存在趋于无穷的 $m$ 子列，使每个这样的 $m$ 至少有一个所选高度的费用为零，
则由 (4.2) 取极限同样迫使原锚为零。
这是费用的条件接口；本条没有证明 (5.2) 的实际 $C_{m,r}$。

## 6. 参数收益及保留的未闭项

- 原强段从旧全高度跨头方案的 $x\asymp e^{c d^3}$ 缩短为
  $R=d,\ x=m+d$，同时保留原母窗 $Q=4d$。
  这来自高度带的精确正交，不是声称旧全高度方案在该尺度仍然有效。
- 每个带的高度数
$$
|I_m|=P_m-\lfloor P_m/2\rfloor\ge P_m/2
\asymp\frac{\sqrt d}{m};
$$
  所有高度仍在原双塔允许窗内。
- 若把强 Boolean 权重化为未加权模型，其整个对角相似的对数条件数为
$$
\log\!\left(\prod_{i=m}^{m+d-1}b_i^{-1}\right)
=2\sum_{i=m}^{m+d-1}\log(i+1)
\le2d\log(m+d)=O(d\log d).
$$
  这只给出一个以后必须实际支付的成本量级；没有由此推出 Galerkin/MP 费用。
- 本条没有转用旧巨大强段下的 Riordan、hatted 或逆修补结论，
  也没有把固定 $m=2$ 的小 carry 消奇性代入原所有 $A_m$。
- 下一未闭量仍是 (3.1) 的原实际费用：必须同时控制多层 carry、
  全强头真核旗、可变高度以及随 $m$ 增长的常数。
  任何局部预算门都不等于普通 Hilbert ISP 的完成。
