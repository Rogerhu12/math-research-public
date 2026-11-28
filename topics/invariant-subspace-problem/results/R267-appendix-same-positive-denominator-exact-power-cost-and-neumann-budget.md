# R267 附录：同一定量正分母的精确非线性幂费用与全尺度 Neumann 预算

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整实际来源定理。** 对[定量共同分母稿](R267-appendix-quantitative-positive-common-denominator-and-strict-superquartic-inverse-cost.md)的同一个 $P$，本文证明

$$
\lim_{n\to\infty}
\frac{\log(-\log\|P^n\|)}{n^{3/2}}=\frac{\log16}{48}.
$$

证明保留实际正项、完整尾源和实现原权范数的同一个柱。由此得到 $P$ 的任意接近一次对数增长的 Neumann 预算，可用于真正联合的 $\sum P^j f_j(C^{-1})$ 来源。未知普通子商只继承上界；本文不把全空间真空下界搬到它们。

## 1. 固定来源及整数边界

沿用同一个原 Haar 尾 $C=A^{(m_0)}$、正权 $a_j=\alpha_{m_0+j}$，以及

$$
q_\nu=256\nu^2,\qquad
m_\nu=1+256\sum_{i<\nu}i^2,\qquad
F_\nu=[m_\nu,m_\nu+q_\nu),
$$

$$
T_\nu^+=\frac2{q_\nu+2}\sum_{j\in F_\nu}N_j,\qquad
T_\nu^0=\frac2{q_\nu+2}\sum_{j\in F_\nu}E_j,\qquad
P=\operatorname*{SOT-lim}_{K\to\infty}\prod_{\nu\le K}T_\nu^+.
\tag{1.1}
$$

所有因子及其实际尾积 $Q_N$ 都是正锥保持收缩，并且

$$
P=\left(\prod_{\nu\le N}T_\nu^+\right)Q_N,\qquad
N_j\ge_{\mathrm{cone}}E_j,\qquad
\|T_\nu^+-T_\nu^0\|
\le\frac4{q_\nu+2}e^{-770\,16^{m_\nu}}.
\tag{1.2}
$$

$P$ 单射、稠密值域，故所有 $\|P^n\|$ 严格正。

对整数 $n\ge257$，定义

$$
N=N(n)=\left\lfloor\sqrt{\frac{n-1}{256}}\right\rfloor.
\tag{1.3}
$$

于是准确有

$$
q_N<n,\qquad q_{N+1}\ge n.
\tag{1.4}
$$

若 $n=q_\nu$，该块归入尾部；若 $n=q_\nu+1$，它才归入前部。后面两侧都使用这个同一边界。

## 2. 一个真实进位给整个 $P^n$ 的上界

纯块 $T_N^0$ 只包含 $q_N$ 个交换的平方零下降算子，所以

$$
(T_N^0)^{q_N+1}=0.
$$

两算子均为收缩，由有限差幂望远镜和 (1.2)，

$$
\|(T_N^+)^{q_N+1}\|
\le(q_N+1)\|T_N^+-T_N^0\|
<4e^{-770\,16^{m_N}}.
\tag{2.1}
$$

从原强乘积中单独提出第 $N$ 个因子，余下乘积仍是与它交换的收缩。再用 $n\ge q_N+1$，得到

$$
\boxed{\|P^n\|\le4e^{-770\,16^{m_N}}.}
\tag{2.2}
$$

这里没有把真实 $T_N^+$ 当作 nilpotent；(2.1) 完整保留使它非零的实际 carry。

## 3. 同一正来源的尾乘积下界

记 $c_\nu=2/(q_\nu+2)$、$k_N=\sum_{\nu\le N}2^{m_\nu}$。由于
$N_{m_\nu}=C^{2^{m_\nu}}/d_{m_\nu}$ 且 $0<d_{m_\nu}\le1$，按函数锥序有

$$
T_\nu^+\ge_{\mathrm{cone}}c_\nu C^{2^{m_\nu}}.
$$

保正算子的乘法和幂保持这样的比较；不需要被比较的两个算子彼此交换。因此

$$
\boxed{
P^n\Omega
\ge_{\mathrm{cone}}
\left(\prod_{\nu\le N}c_\nu\right)^n
C^{n k_N}Q_N^n\Omega.}
\tag{3.1}
$$

下一步保留同一个尾源，而非换成任意单位向量。

对 $\nu>N$，$q_\nu\ge n$，定义纯尾向量
$s_{\nu,n}=(T_\nu^0)^n\Omega$。有限不交位块的真空计算给

$$
\mu_{\nu,n}:=\langle s_{\nu,n},\Omega\rangle
=\frac{(q_\nu)_n}{(q_\nu+2)^n}>0,
\qquad (q)_n=q(q-1)\cdots(q-n+1).
\tag{3.2}
$$

每个 $s_{\nu,n}\ge0$、范数不超过 $1$。固定 $n$ 时，

$$
1-\mu_{\nu,n}\le\frac{n(n+3)}{2(q_\nu+2)},\qquad
0\le1-\|s_{\nu,n}\|^2\le2(1-\mu_{\nu,n}).
$$

这些亏损对 $\nu>N$ 可和。独立块的均值与平方范数乘积公式，和前稿相同的 Cauchy 论证，因而给实际 $L^2$ 极限

$$
g_{N,n}=\lim_{K\to\infty}
\left(\prod_{N<\nu\le K}(T_\nu^0)^n\right)\Omega\ge0,
\qquad
\|g_{N,n}\|\ge\prod_{\nu>N}\mu_{\nu,n}>0.
\tag{3.3}
$$

它只依赖编号至少为 $m_{N+1}$ 的物理位。

由 $T_\nu^+\ge_{\mathrm{cone}}T_\nu^0$，先对每个有限尾乘积取第 $n$ 次幂再比较；其强极限仍保持锥序，故

$$
Q_N^n\Omega\ge_{\mathrm{cone}}g_{N,n}.
\tag{3.4}
$$

这里尾的强极限与固定整数 $n$ 的乘法可交换，因为全部有限尾均为收缩。

还需控制 (3.3) 的实际费用。若 $q\ge2n$，

$$
-\log\frac{(q)_n}{(q+2)^n}
=\sum_{k=0}^{n-1}-\log\left(1-\frac{k+2}{q+2}\right)
\le\frac{n(n+3)}{q+2}.
\tag{3.5}
$$

$n\le q<2n$ 的块只有 $O(\sqrt n)$ 个；每个可粗界为
$n\log(2n+2)$。其余块用 (3.5) 及
$\sum_{\nu\ge c\sqrt n}\nu^{-2}=O(n^{-1/2})$。因此

$$
-\sum_{\nu>N}\log\mu_{\nu,n}
=O(n^{3/2}\log(2+n)).
\tag{3.6}
$$

所有隐常数为固定的绝对常数；没有丢掉碰到 $q_\nu=n$ 的整块。

## 4. 原 $C^r$ 范数在同一柱上确实实现

对任意整数 $r\ge1$，原权的准确范数为

$$
W_r:=\|C^r\|
=\prod_{t=1}^{r}a_{v_2(t)}
=\prod_{j:b_j(r)=1}d_j.
\tag{4.1}
$$

可直接证明第一式：任意 $r$ 个连续整数中，$2^\ell$ 的倍数至少有
$\lfloor r/2^\ell\rfloor$ 个。将权积写成
$a_0^r\prod_{\ell\ge1}(a_\ell/a_{\ell-1})^{\#\{2^\ell\text{ 的倍数}\}}$，
因各比率小于 $1$，前缀 $1,\ldots,r$ 同时达到所有这些计数下界，因而实现最大权积。相应柱具有正 Haar 测度。

现在取 (3.1) 中的 $r=n k_N$，并置

$$
H=m_N+\lceil\log_2 n\rceil+2.
$$

$k_N\le2^{m_N+1}$，所以 $r<2^H$；由 $q_N\asymp n$，充分大 $n$ 时还有

$$
H<m_{N+1}=m_N+q_N.
\tag{4.2}
$$

在明确的同一个柱

$$
E=\{y:y\equiv r\pmod {2^H}\}
\tag{4.3}
$$

上，$y-r=2^H z$，而 $y,y-1,\ldots,y-r+1$ 的低 $H$ 位恰为
$r,r-1,\ldots,1$。所以原实际权积准确等于 $W_r$；没有遇到需要无限尾赋值的零余类。

同时 $g_{N,n}$ 只依赖位 $\ge m_{N+1}>H$，平移 $y\mapsto y-r$ 在 (4.3) 上不改变这些位，且该尾函数与柱事件独立。因此

$$
\boxed{\|\mathbf1_E C^r g_{N,n}\|
=2^{-H/2}W_r\|g_{N,n}\|.}
\tag{4.4}
$$

这是指定同源尾函数的真下界，不是以另一个达到范数的输入代替它。

由定量稿的 $-\log d_j\le500\,16^{m_0+j}$ 及 (4.1)，

$$
-\log W_r\le1000\,16^{m_0}r^4.
\tag{4.5}
$$

把 (3.1)、(3.3)–(3.4)、(4.4) 合起来，得到

$$
\|P^n\|
\ge
\left(\prod_{\nu\le N}c_\nu\right)^n
2^{-H/2}W_{n k_N}\prod_{\nu>N}\mu_{\nu,n}.
\tag{4.6}
$$

其中
$-n\sum_{\nu\le N}\log c_\nu=O(n^{3/2}\log(2+n))$。
再用 (3.6)、(4.5) 及 $n k_N\le2n\,2^{m_N}$，得

$$
\boxed{
-\log\|P^n\|
\le16000\,16^{m_0}n^4\,16^{m_N}
+O(n^{3/2}\log(2+n)+H).}
\tag{4.7}
$$

## 5. 精确阶梯及混合幂

(2.2) 与 (4.7) 给精确到对数误差的原阶梯：

$$
\boxed{
\log(-\log\|P^n\|)
=m_{N(n)}\log16+O_{m_0}(\log n).}
\tag{5.1}
$$

而

$$
N(n)\sim\frac{\sqrt n}{16},\qquad
m_{N(n)}=1+\frac{256}{6}(N-1)N(2N-1)
\sim\frac{n^{3/2}}{48}.
$$

故

$$
\boxed{
\lim_{n\to\infty}
\frac{\log(-\log\|P^n\|)}{n^{3/2}}
=\frac{\log16}{48}.}
\tag{5.2}
$$

同一方法还支付原混合输入。固定整数 $a\ge0,b\ge1$，以 $p=bn$ 取
$N=N(p)$；(3.1) 的前缀变成
$C^{p k_N+an}$，纯尾均值仍是同一个 $g_{N,p}$。取
$H=m_N+\lceil\log_2((2b+a)n)\rceil+2$，充分大 $n$ 时仍有
$p k_N+an<2^H$ 及 $H<m_{N+1}$。原同柱论证完整保留，给

$$
\log(-\log\|C^{an}P^{bn}\|)
=m_{N(bn)}\log16+O_{a,b,m_0}(\log n),
$$

从而

$$
\boxed{
\lim_{n\to\infty}
\frac{\log(-\log\|C^{an}P^{bn}\|)}{n^{3/2}}
=\frac{\log16}{48}\,b^{3/2}.}
\tag{5.3}
$$

上界使用 $\|C^{an}P^{bn}\|\le\|P^{bn}\|$；下界确实在同一个原正乘积中增加了 $C^{an}$，没有用压缩逆或未知子商的真空。

## 6. 可直接用于联合来源的 Neumann 预算

定义非负标量函数

$$
\mathcal R_P(t)=\sum_{n\ge0}t^n\|P^n\|,\qquad t\ge0.
$$

由 (5.2)，对每个 $s>1$，存在有限 $A_s$ 使
$\|P^n\|\le A_s e^{-n^s}$。有限极大化
$n\log^+t-\tfrac12n^s$ 因而给：对每个 $\varepsilon>0$，存在固定 $K_\varepsilon$ 使

$$
\boxed{
\log^+\mathcal R_P(t)
\le K_\varepsilon[1+\log(2+t)]^{1+\varepsilon}.}
\tag{6.1}
$$

这是同一个 $P$ 的全参数预算，不为每个 $t$ 更换分母。

例如 $V$ 是与 $P$ 交换的任意有界算子，则
$(PV)^n=P^nV^n$，Neumann 级数绝对收敛并准确乘回：

$$
(I+PV)^{-1}=\sum_{n\ge0}(-PV)^n,\qquad
\|(I+PV)^{-1}\|\le\mathcal R_P(\|V\|).
\tag{6.2}
$$

特别对任意 $\rho>0$，定义有限常数

$$
L_\rho=\sum_{j\ge1}\rho^{-j}\|P^{j-1}\|.
$$

若标量系数 $|c_j|\le t\rho^{-j}$，则
$B=\sum_{j\ge1}c_jP^j=PV$ 在范数中绝对收敛，
$\|V\|\le tL_\rho$，故

$$
\boxed{
\left\|\left(I+\sum_{j\ge1}c_jP^j\right)^{-1}\right\|
\le\mathcal R_P(tL_\rho).}
\tag{6.3}
$$

这已经包括任意有限多项式及任意在正半径圆盘内收敛的同一 $P$ 芽，没有把 $\|B\|<1$ 当成必要条件。

## 7. 原旗及下一实际输入

任何有限放大原旗商 $Q$ 上，
$\|P_Q^n\|\le\|P^n\|$，所以 (2.2)、(6.1)–(6.3) 的上界及逆级数原样适用。本文没有为未知 $Q$ 构造 (3.3) 的正真空，因此不声称其幂范数也满足 (5.2) 的等式。

前稿的 $C^{-r}P$ 预算支付一个变量的快速整逆源。本稿的 (6.3) 进一步控制另一个真实变量 $P$ 的解析逆，这正是联合级数 $\sum_jP^j f_j(C^{-1})$ 所需要的非线性分母费用。联合类的忠实性及是否严格超出旧场须另证，不能仅凭这个预算宣称；本稿也没有把 (5.2) 或 (6.3) 当作 $Y^2=CP^2$ 的解。
