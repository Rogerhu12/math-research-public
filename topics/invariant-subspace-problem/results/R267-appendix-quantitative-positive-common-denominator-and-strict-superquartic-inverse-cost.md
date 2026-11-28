# R267 附录：定量正锥共同分母与每个实际平坦向量的严格超四次逆幂费用

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整原算子结论。** 本文选定一个新的、明确的正锥共同分母 $P$，同时支付全部实际 $C^{-r}P$ 的 $r^{4+o(1)}$ 对数费用。反向，对每个固定非零 $p\in\bigcap_r\operatorname{Ran}C^r$，证明完整极限 $\log\|C^{-r}p\|/r^4\to+\infty$。因此幂指数 $4$ 可以达到，但任何固定 $\exp(Kr^4)$ 来源预算都不可能。这里始终是原 Haar 尾；没有把负整数边界模型的逆运回原空间。

## 1. 原权及明确的新块

固定原 Haar 尾 $C=A^{(m_0)}$，局部坐标为 $y\in\mathbb Z_2$：

$$
(Cf)(y)=a_{v_2(y)}f(y-1),\qquad a_j=\alpha_{m_0+j},\qquad
-\log\alpha_\ell=\frac{280}{3}16^\ell-90\,8^\ell+300\,2^\ell-\frac{850}{3}.
\tag{1.1}
$$

$C$ 单射、稠密值域、拟幂零，且 $\|C\|=a_0<1$。记实际归一化幂

$$
d_j=\|C^{2^j}\|,\qquad N_j=C^{2^j}/d_j,\qquad
Y_j=N_j(I+N_j)^{-1}.
$$

原权的一个整周期给准确公式

$$
d_j=a_j\prod_{i<j}a_i^{\,2^{j-1-i}}.
\tag{1.2}
$$

因为 $0<-\log\alpha_\ell\le400\,16^\ell$，所以

$$
0<-\log d_j
\le400\,16^{m_0+j}\left(1+\sum_{h=1}^j2^{h-1}16^{-h}\right)
\le500\,16^{m_0+j}.
\tag{1.3}
$$

沿用[正锥共同分母稿](R267-appendix-positivity-preserving-common-powers-and-no-compact-domination.md)的真实关系

$$
\|N_j-E_j\|\le\eta_j,\qquad
\|Y_j-E_j\|\le4\eta_j,\qquad
\|N_j-Y_j\|\le3\eta_j,\qquad
\sum_{j\ge m}\eta_j\le2e^{-770\,16^m}.
\tag{1.4}
$$

本稿重新选块；不改变先前已经构造的分母。明确取

$$
q_\nu=256\nu^2,\qquad
m_\nu=1+256\sum_{i<\nu}i^2,\qquad
F_\nu=[m_\nu,m_\nu+q_\nu),\qquad
b_\nu=m_\nu+q_\nu-1=256\sum_{i\le\nu}i^2.
\tag{1.5}
$$

这些连续块互不交，且

$$
\sum_{\nu\ge1}q_\nu^{-1}<\frac1{128}.
\tag{1.6}
$$

定义同一组实际因子

$$
T_\nu=\frac2{q_\nu+2}\sum_{j\in F_\nu}Y_j,\qquad
T_\nu^+=\frac2{q_\nu+2}\sum_{j\in F_\nu}N_j.
\tag{1.7}
$$

这里“正锥保持”指函数 $f\ge0\Rightarrow Tf\ge0$，不是正自伴。

## 2. 新块确有非零强乘积及同一强单位

纯局部范数 $\|\sum_{F_\nu}E_j\|\le(q_\nu+1)/2$ 与 (1.4) 直接给

$$
\|T_\nu\|\le
\frac{q_\nu+1+8\sum_{F_\nu}\eta_j}{q_\nu+2}<1,\qquad
\|T_\nu^+\|\le
\frac{q_\nu+1+2\sum_{F_\nu}\eta_j}{q_\nu+2}<1.
\tag{2.1}
$$

因此无需把新 $q_\nu$ 填进旧稿较粗的块长条件。全部因子仍是收缩且互相交换。

为完整支付新参数的强极限，使用[原共同分母稿 §§2–3](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)的准确真空列，而非仅引用旧参数的结论：

$$
T_\nu\Omega=t_\nu=\frac{q_\nu-\sum_{j\in F_\nu}\chi_j}{q_\nu+2},\qquad
\mu_\nu=\langle t_\nu,\Omega\rangle=\frac{q_\nu}{q_\nu+2},\qquad
\alpha_\nu=\|t_\nu\|^2=\frac{q_\nu^2+q_\nu}{(q_\nu+2)^2}.
$$

不交块的有限乘积真空列准确等于 $\prod t_\nu$。对 $k>n$，其差平方为

$$
\left(\prod_{\nu\le n}\alpha_\nu\right)
\left(\prod_{n<\nu\le k}\alpha_\nu+1-2\prod_{n<\nu\le k}\mu_\nu\right).
\tag{2.2}
$$

$1-\mu_\nu\le2/q_\nu$、$1-\alpha_\nu\le3/q_\nu$ 与 (1.6) 使 (2.2) 一致趋零。真空循环性及 (2.1) 将真空收敛延到全 $H$。故旧型因子在这些新块上有实际收缩乘积 $P^Y$ 和尾积 $Q_n^Y$，且

$$
\langle P^Y\Omega,\Omega\rangle>63/64,\qquad Q_n^Y\longrightarrow I\ \text{强*}.
\tag{2.3}
$$

又令 $\delta_\nu=\|T_\nu^+-T_\nu\|$，则

$$
\delta_\nu\le\frac6{q_\nu+2}\sum_{j\in F_\nu}\eta_j,\qquad
\Delta:=\sum_\nu\delta_\nu<12e^{-770}<1/64.
$$

有限乘积差的望远镜展开

$$
\prod_{\nu\le n}T_\nu^+-\prod_{\nu\le n}T_\nu
=\sum_{\nu\le n}
\left(\prod_{i<\nu}T_i^+\right)(T_\nu^+-T_\nu)
\left(\prod_{\nu<i\le n}T_i\right)
\tag{2.4}
$$

逐个固定 $\nu$ 取旧尾强极限，再用可和的 $\delta_\nu$，给

$$
P=\operatorname*{SOT-lim}_{n\to\infty}P_n,\qquad
P_n=\prod_{\nu\le n}T_\nu^+,\qquad
\|P\|\le1,\qquad \langle P\Omega,\Omega\rangle>31/32.
\tag{2.5}
$$

所以 $P\ne0$，且保持函数正锥。相同论证给收缩尾积 $Q_n$，满足

$$
P=P_nQ_n,\qquad
\|Q_n-Q_n^Y\|\le\sum_{\nu>n}\delta_\nu,\qquad Q_n\to I\ \text{强*}.
\tag{2.6}
$$

令 $k_n=\sum_{\nu\le n}2^{m_\nu}$。真实有限多项式分解为

$$
T_\nu^+=C^{2^{m_\nu}}U_\nu(C),\qquad
U_\nu(z)=\frac2{q_\nu+2}
\sum_{j\in F_\nu}\frac{z^{\,2^j-2^{m_\nu}}}{d_j},\qquad
U^{[n]}=\prod_{\nu\le n}U_\nu(C).
\tag{2.7}
$$

$U_\nu(0)>0$，所以 $U_\nu(C)$ 是有界交换单位。对任意整数 $r\ge0$，选 $k_n\ge r$，定义

$$
R_r=C^{k_n-r}U^{[n]}Q_n.
\tag{2.8}
$$

这是全 $H$ 上有界且正锥保持的实际算子，满足

$$
C^rR_r=P,\qquad R_r=C^{-r}P.
\tag{2.9}
$$

$C$ 单射保证它与所选 $n$ 无关。特别 $R_0=P$。

同一个 $P$ 仍有原强单位：取 R23 的收缩多项式 $E_{\ell(n)}=C^{k_n}B_n(C)$，其中 $\ell(n)\ge n$ 且最低次数至少 $k_n$，置

$$
W_n=(U^{[n]})^{-1}B_n(C)\in\mathcal A.
$$

便有

$$
PW_n=Q_nE_{\ell(n)},\qquad \|PW_n\|\le1,\qquad PW_n\to I\ \text{强*}.
\tag{2.10}
$$

每个 $R_r$ 用右因子 $C^rW_n$ 得到同一单位。由原有界强多项式闭包，这些因子保持全部有限放大中的原闭不变旗。因此 $P$ 及每个 $R_r$ 在每个非零这样的子商上都单射、稠密值域。这个结论来自 (2.10)，没有从环境空间稠密像推到任意限制。

## 3. 同一分母的明确逆幂费用

因为 $\|C\|<1$ 且 $d_j$ 随 $j$ 递减，(2.7) 给

$$
\|U_\nu(C)\|\le2d_{b_\nu}^{-1}.
$$

对给定 $r\ge1$，取最小的 $n$ 使 $k_n\ge r$。由 (1.3)、(2.8) 及 $b_\nu$ 的严格递增，

$$
\log^+\|R_r\|
\le n\log2+\sum_{\nu\le n}(-\log d_{b_\nu})
\le1000\,16^{m_0+b_n}.
\tag{3.1}
$$

若 $n\ge2$，置 $t=\log_2r$。最小性给 $r>k_{n-1}\ge2^{m_{n-1}}$，所以

$$
n\le2+(3t/256)^{1/3},\qquad
b_n-t\le q_{n-1}+q_n-1\le512n^2\le4096+64t^{2/3}.
\tag{3.2}
$$

$n=1$ 时 $r\le2$、$b_1=256$，同一最后界亦成立。将 (3.2) 代入 (3.1)，并用
$64\log16/(\log2)^{2/3}<300$，得到一个统一明确预算：

$$
\boxed{\displaystyle
\log^+\|C^{-r}P\|
\le K_{m_0}\,r^4
\exp\!\left(300[\log(2+r)]^{2/3}\right),\qquad
K_{m_0}=1000\,16^{m_0+4096}.}
\tag{3.3}
$$

常数很大但固定，且全部作用于同一个 $P$。尤其对每个 $\varepsilon>0$ 都有有限 $K_{\varepsilon,m_0}$ 使

$$
\log^+\|C^{-r}P\|\le K_{\varepsilon,m_0}r^{4+\varepsilon}
\qquad(r\ge1).
\tag{3.4}
$$

没有宣称 $\varepsilon=0$ 的固定常数预算；下一节证明这种预算对任何非零实际平坦来源都不可能。

## 4. 每个固定平坦向量的严格超四次下界

**定理 4.1。** 对任意固定

$$
0\ne p\in\bigcap_{r\ge1}\operatorname{Ran}C^r,
$$

其唯一实际原像满足完整极限

$$
\boxed{\displaystyle
\lim_{r\to\infty}\frac{\log\|C^{-r}p\|}{r^4}=+\infty.}
\tag{4.1}
$$

**证明。** 固定整数 $L\ge1$。对 $k\ge0$ 取随 $k$ 后移的真实柱窗

$$
U_{k,L}=\{y:y\bmod2^{k+L}<2^k\}
=\{b_k(y)=\cdots=b_{k+L-1}(y)=0\}.
\tag{4.2}
$$

其测度为 $2^{-L}$。对固定低位柱函数，充分大的 $k$ 使该窗与测试坐标独立。因此乘法投影满足

$$
\mathbf1_{U_{k,L}}\xrightarrow{\mathrm{WOT}}2^{-L}I,\qquad
\|\mathbf1_{U_{k,L}}p\|^2\longrightarrow2^{-L}\|p\|^2.
\tag{4.3}
$$

记 $r=2^k$，$C^rf(y)=w_r(y)f(y-r)$，其中
$w_r(y)=\prod_{s=0}^{r-1}a_{v_2(y-s)}$。对 $y\in U_{k,L}$，
在 $0\le s<r$ 中取 $s=y\bmod2^{k+L}$，便有
$2^{k+L}\mid(y-s)$。故该乘积有一个因子至多 $a_{k+L}$，其余因子不超过 $1$：

$$
w_{2^k}(y)\le a_{k+L}\quad(y\in U_{k,L})\quad\text{几乎处处}.
$$

原平移保 Haar 测度，且 $p\in\operatorname{Ran}C^{2^k}$，于是

$$
\|C^{-2^k}p\|
=\|p/w_{2^k}\|
\ge a_{k+L}^{-1}\|\mathbf1_{U_{k,L}}p\|.
\tag{4.4}
$$

这里是真实唯一逆，不是形式系数。由 (1.1)、(4.3)–(4.4)，对这个固定 $L$，

$$
\liminf_{k\to\infty}
\frac{\log\|C^{-2^k}p\|}{16^k}
\ge\frac{280}{3}16^{m_0+L}.
\tag{4.5}
$$

$L$ 可以任意大，故 dyadic 左侧趋于 $+\infty$，而不只是有一个发散子列。最后 $C$ 为收缩且各逆存在，所以 $\|C^{-r}p\|$ 随 $r$ 不减。若 $2^k\le r<2^{k+1}$，则 $r^4\le16\cdot16^k$。对充分大 $k$，相关对数为正，(4.5) 因而给所有整数 $r$ 的 (4.1)。证毕。

该证明对复向量同样成立，不要求 $p$ 保持函数正号；也没有要求一个未知子空间具有柱函数核心。关键是对同一个固定 $p$ 先固定 $L$，再令 $k\to\infty$，最后利用 $L$ 任意。

## 5. 达到的准确指数及用途边界

把定理 4.1 用于 (2.5) 的 $p=Px$。因 $P$ 单射，每个 $x\ne0$ 都有 $p\ne0$，而 (2.9) 给 $C^{-r}p=R_rx$。结合 (3.3) 得

$$
\frac{\log\|R_rx\|}{r^4}\longrightarrow+\infty,\qquad
\boxed{\displaystyle
\lim_{r\to\infty}
\frac{\log\log(e+\|R_rx\|)}{\log r}=4
\quad(x\ne0).}
\tag{5.1}
$$

算子范数也满足同样的两个结论。特别任意非零有界共同分母 $\widetilde P$，只要 $C^{-r}\widetilde P$ 对每个 $r$ 全域有界，就不可能有固定 $K$ 使
$\|C^{-r}\widetilde P\|\le e^{Kr^4}$ 对全部充分大 $r$ 成立：任取 $\widetilde Px\ne0$，(4.1) 已反证它。

这与[旧 R44 §5](R44-critical-schur-division-and-kernel-regularity.md)的平坦向量交稠密性相容。新内容是逐个固定非零向量的完整严格超四次下界，以及 (1.5) 选出的同一实际有界分母所达到的 $r^{4+o(1)}$ 上界。原强单位、每个实际整数逆及全部原旗仍保留。

这些预算可用于有明确系数衰减的同分母级数。它们本身没有解出 $Y^2=CP^2$，也没有把共同整数逆改成分数次根。普通 ISP 及实际非局部闭根来源继续开放。
