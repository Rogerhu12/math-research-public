# 加权 Bernstein–Walsh 与双尺度截断：原临界核的完整排除正文

日期：2026-11-12。张量/文献子代理提出加权外域多项式估计，根会话与本代理同时补出保留真实低位的双尺度搬运；`critical_kernel` 补齐唯一数值常数的严格区间证书。本文为 R60 的主体推导。负指数常数的完整解析证明、有理表见 [常数证书](2026-11-12-critical-negative-integral-certificate-0c.md)，有限区间核算见 [证书脚本](2026-11-12-critical-negative-integral-certificate-0c.py)。

**结论范围。** 下文针对 R28/R36/R43 的原多项式尾临界算子 $D=I-Q$，证明 $\ker D=\ker L=\{0\}$、$\overline{DH}=\overline{LH}=H$，从而原临界向量 $D1$ 循环。它解决这一具体临界核缺口，不决定该 odometer 的全部普通不变子空间，更不解决一般 Hilbert 不变子空间问题。

## 1. 区间外的加权多项式估计

设 $0<a<b$，定义

$$
 g_0=\log\frac{\sqrt b+\sqrt a}{\sqrt b-\sqrt a},
 \qquad
 d\omega_0(u)=
 \frac{\sqrt{ab}}{\pi u\sqrt{(u-a)(b-u)}}\,du,
 \quad a<u<b.
 \tag{1.1}
$$

$\omega_0$ 是概率测度。对任意次数不超过 $n$ 的复多项式 $p$，有

$$
 \boxed{
 \log|p(0)|
 \le n g_0+\int_a^b\log|p(u)|\,d\omega_0(u).
 }
 \tag{1.2}
$$

约定 $p(0)=0$ 时左边为 $-\infty$，恒零多项式无需讨论。

**自含证明。** 置 $c=(a+b)/2$、$d=(b-a)/2$，以及

$$
 r=\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a}\in(0,1).
$$

有 $c=\frac d2(r+r^{-1})$。函数

$$
 F(\zeta)=\zeta^n p\!\left(c+\frac d2(\zeta+\zeta^{-1})\right)
$$

在单位圆盘内解析：$p$ 的次数不超过 $n$，所以 $\zeta=0$ 的表面极点已被消掉。它连续延伸到闭圆盘。在 $\zeta=-r$ 处，其多项式参数恰等于零，故

$$
 \log|F(-r)|=n\log r+\log|p(0)|.
$$

对解析函数使用对数模的 Poisson 上界，得到

$$
 n\log r+\log|p(0)|
 \le\frac1{2\pi}\int_0^{2\pi}
 \frac{1-r^2}{1+2r\cos\theta+r^2}
 \log|p(c+d\cos\theta)|\,d\theta.
 \tag{1.3}
$$

这里可以先把圆盘内的零点用有限 Blaschke 因子消掉，再对其余非零解析函数的对数模用 Poisson 公式；Blaschke 因子在边界模为一、在内点模不超过一，正好给出不等号。边界零点的对数奇点可积，可从半径小于一的圆或连续截断取极限，因此没有假设 $p$ 在区间上无零点。

令 $u=c+d\cos\theta$。由

$$
 1+2r\cos\theta+r^2=\frac{2r}{d}u,
 \qquad 1-r^2=\frac{2r}{d}\sqrt{ab},
$$

Poisson 权变成 $\sqrt{ab}/u$；再把余弦的两条分支合并，式 (1.3) 右边即为式 (1.1) 的积分。取常数 $p=1$，或直接对 Poisson 核积分，可知 $\omega_0$ 质量为一。由于 $-\log r=g_0$，得到式 (1.2)。证毕。

特别地，若 $W>0$ 在 $[a,b]$ 上连续，且 $|p(u)|\le K W(u)$，则

$$
 |p(0)|\le K\exp\!\left(n g_0+
               \int_a^b\log W(u)\,d\omega_0(u)\right).
 \tag{1.4}
$$

这一步使用的是对数权的调和平均。把它换成区间上权的最大值，会失去下面所需的负指数。

## 2. 平方尾部的指数乘积与统一 Riemann 和误差

在公平乘积 Hilbert 空间上令 $E_j=e_{10}^{(j)}$，参考向量为 $1=\bigotimes_j(e_0+e_1)/\sqrt2$。取原临界例的系数

$$
 \delta_j=\frac{2}{(j+2)^2+1},\qquad
 C_m=\sum_{j\ge m}\delta_jE_j.
 \tag{2.1}
$$

对实 $t\ge0$，因各位交换且 $E_j^2=0$，

$$
 e^{-tC_m^*}1=\bigotimes_{j\ge m}(I-t\delta_jE_j^*)1.
$$

无限乘积按范数收敛，因 $\sum_jt\delta_j<\infty$。单个位上，$E_j^*1=1_{\{b_j=0\}}$，所以

$$
 F_m(t):=\|e^{-tC_m^*}1\|
 =\prod_{j\ge m}
 \left(1-t\delta_j+\frac{t^2\delta_j^2}{2}\right)^{1/2}.
 \tag{2.2}
$$

定义

$$
 P(q)=1-q+q^2/2=\frac{1+(q-1)^2}{2},
 \quad \ell(q)=\frac12\log P(q),
$$

$$
 h(u)=\int_1^\infty\ell(u/x^2)\,dx
 =\frac12\int_1^\infty
       \log\left(1-\frac{u}{x^2}+\frac{u^2}{2x^4}\right)\,dx.
 \tag{2.3}
$$

对 $q\ge0$，

$$
 |\ell'(q)|=
 \frac{|q-1|}{1+(q-1)^2}\le\frac12.
 \tag{2.4}
$$

由 $\ell(0)=0$，特别有 $|\ell(q)|\le q/2$，积分绝对收敛且

$$
 |h(u)|\le u/2,\qquad |h'(u)|\le1/2. \tag{2.5}
$$

置 $M=m+2$、$t=uM^2/2$。对 $j=m+l$，令 $x_l=1+l/M$，则

$$
 t\delta_j=\frac{u}{x_l^2+M^{-2}}.
$$

记 $f_{M,u}(x)=\ell(u/(x^2+M^{-2}))$。由式 (2.4)，

$$
 |\partial_x f_{M,u}(x)|\le\frac{u}{x^3},\qquad x\ge1.
$$

在每个长度 $1/M$ 的网格区间上用积分形式的中值界，然后求和，得到

$$
 \left|\frac1M\sum_{l\ge0}f_{M,u}(x_l)
       -\int_1^\infty f_{M,u}(x)\,dx\right|
 \le\frac1M\int_1^\infty|\partial_xf_{M,u}(x)|\,dx
 \le\frac{u}{2M}. \tag{2.6}
$$

另一方面，式 (2.4) 给

$$
 \left|f_{M,u}(x)-\ell(u/x^2)\right|
 \le\frac{u}{2M^2x^4},
$$

其积分不超过 $u/(6M^2)$。结合式 (2.2)，得到显式统一误差

$$
 \boxed{
 \left|\log F_m(uM^2/2)-M h(u)\right|
 \le\frac u2+\frac{u}{6M}.
 } \tag{2.7}
$$

因此对 $u\in[1,20]$ 和 $M\ge1$，可统一使用

$$
 e^{M h(u)-14}\le F_m(uM^2/2)\le e^{M h(u)+14},
 \qquad F_m(uM^2/2)\ge e^{-10M-14}.
 \tag{2.8}
$$

这些是有明确余项的界，不需要核投影或谱测度的截断极限。

## 3. 唯一需要的严格负常数

固定 $a=1$、$b=20$，$g_0,\omega_0$ 由式 (1.1) 定义。设

$$
 J=g_0+\int_1^{20}h(u)\,d\omega_0(u).
 \tag{3.1}
$$

所需且已由[完整常数证书](2026-11-12-critical-negative-integral-certificate-0c.md)证明的界为

$$
 \boxed{J\le-\frac{51746665241}{375000000000}<-13/100.} \tag{3.2}
$$

以下列出该证书的解析结构，避免把普通浮点值当作引理。由

$$
 (\log P)''(q)=
 \frac{2(1-(q-1)^2)}{(1+(q-1)^2)^2},
$$

有 $|h''(u)|\le\int_1^\infty x^{-4}\,dx=1/3$。所以整数区间 $[i,i+1]$ 上，$h$ 不超过其端点线性插值加 $1/24$。谐测质量与一阶矩的原函数分别为

$$
 W(u)=\frac2\pi\arctan\sqrt{\frac{20(u-1)}{20-u}},
 \qquad
 M_1(u)=\frac{2\sqrt{20}}\pi
          \arcsin\sqrt{\frac{u-1}{19}},
 \tag{3.3}
$$

端点取连续极限。这使 19 段线性插值的积分成为只有 20 个 $h(i)$ 的有限表达式。令 $\alpha=(1+\mathrm i)/2$，对 $u>0$ 取主分支，有

$$
 h(u)=\operatorname{Re}
 \left[-\log(1-\alpha u)
 -2\sqrt{\alpha u}\,\operatorname{atanh}\sqrt{\alpha u}\right].
 \tag{3.4}
$$

该式来自对式 (2.3) 分部积分；$\alpha u$ 在严格上半平面，因此连续选取的平方根、对数、反双曲正切分支无歧义。详细分支与严格区间求值见上述常数证书。证书列出 20 个负有理数 $H_i/10^6$，分别严格大于 $h(i)$；列出 20 个正有理数 $W_i/10^6$，分别严格小于帽函数的谐测积分权重；再用 $g_0<454900/10^6$。因为所有 $H_i<0$，用权重下界相乘的方向仍是上界。41 个界经 256-bit Arb/Acb 的完整球端点比较核实，最后仅用整数分数算术得

$$
 J\le\frac{454900}{10^6}
      +\sum_{i=1}^{20}\frac{H_iW_i}{10^{12}}+\frac1{24}
   =-\frac{51746665241}{375000000000}
   <-\frac{13}{100}.
$$

本文后续只使用有理界 (3.2)。

## 4. 纯张量模型先说明机制

令 $B=\sum_{j\ge0}\delta_jE_j$，$H_m=\sum_{j<m}\delta_jE_j$。二者的头尾分解 $B=H_m+C_m$ 中各项交换，且 $H_m^{m+1}=0$。

若 $Bf=0$，则 $C_m^qf=(-H_m)^qf$，所以对实 $t$，

$$
 \langle f,e^{-tC_m^*}1\rangle
 =\langle e^{tH_m}f,1\rangle.
$$

右边是次数不超过 $m$ 的多项式。令

$$
 p_m(u)=\langle e^{uM^2H_m/2}f,1\rangle,
 \qquad M=m+2.
$$

则 $p_m(0)=\langle f,1\rangle$，而式 (2.8) 给

$$
 |p_m(u)|\le\|f\|e^{M h(u)+14},\qquad 1\le u\le20.
$$

应用式 (1.4)，

$$
 |\langle f,1\rangle|
 \le\|f\|\exp\left(14+m g_0+M\int h\,d\omega_0\right)
 \le\|f\|\exp(14-13M/100).
$$

令 $m\to\infty$，得到 $\ker B\perp1$。又 $\ker B$ 对所有 $E_j$ 不变，而
$E_F^*1=\prod_{j\in F}1_{\{b_j=0\}}$ 的张成稠密，故 $\ker B=\{0\}$。全位互补酉算子把 $B$ 变为 $B^*$，所以纯模型也有稠密值域。

这一步没有使用尚未证明的有限正则化逆状态比较，也没有从有限截断核投影取极限。下一节保留真实进位误差，证明原 $L$。

## 5. 原临界对数与已有的真实低位近似

保持 R43 的记号

$$
 N_j=\frac{A^{2^j}}{\|A^{2^j}\|},\qquad
 \eta_j=\frac{a_{j+1}}{a_j},\qquad r_j=1-\delta_j,
$$

$$
 L=\sum_{j\ge0}h_j(N_j),\qquad
 h_j(T)=\log(I+T)-\log(I+r_jT).
 \tag{5.1}
$$

这里只把函数 $h_j$ 与第 2 节的实函数 $h(u)$ 以自变量区分，二者没有等同关系。实际的

$$
 -\log\eta_j=1400\,16^j-630\,8^j+300\,2^j
 \ge770\,16^j. \tag{5.2}
$$

设 $A_k$ 为删除 $v_2(y)\ge k$ 权的有限链截断，只作用于前 $k$ 位，$A_k^{2^k}=0$。对 $j<k$ 置

$$
 N_j^{[k]}=\frac{A_k^{2^j}}{\|A^{2^j}\|},\qquad
 G_k=\sum_{j<k}h_j(N_j^{[k]}).
 \tag{5.3}
$$

$G_k$ 是 $A_k$ 的无常数项多项式，因此

$$
 G_k^{2^k}=0. \tag{5.4}
$$

R50 §2 已完整证明以下近似，现列出需要的全部常数：

$$
 T_k=G_k+\sum_{j\ge k}\delta_jE_j,
 \qquad \|L-T_k\|\le22\eta_{k-1},\quad k\ge1,
 \tag{5.5}
$$

$$
 \Delta:=\sum_j\delta_j\le2,\qquad
 \|G_k\|\le\tfrac83\Delta.
 \tag{5.6}
$$

为明确 (5.5) 是真实模型估计，其证明所用精确事实为

$$
 \|N_j-N_j^{[k]}\|=a_k/a_j\quad(j<k),\qquad
 \|N_j-E_j\|=\eta_j,
$$

以及

$$
 \|h_j(T)-h_j(S)\|\le\tfrac{64}{9}\delta_j\|T-S\|,
 \qquad
 \|h_j(N_j)-\delta_jE_j\|\le\tfrac{11}{3}\delta_j\eta_j.
$$

前者由 $h_j(T)=\int_{r_j}^1T(I+sT)^{-1}ds$ 和
$\|(I+sT)^{-1}\|\le8/3$ 推出，适用于本处原幂和截断幂；后者由 $N_j^2$ 的范数至多 $\eta_j$ 后直接求幂级数尾和得到。再用 $\eta_j$ 递减、$a_k/a_j\le\eta_{k-1}$、$\Delta\le2$，总误差不超过
$\frac{64}{9}\Delta\eta_{k-1}+\frac{11}{3}\Delta\eta_k<22\eta_{k-1}$。

## 6. 两个尺度分开：真实头部只占 $o(m)$ 个多项式次数

给定大整数 $m$，仍记 $M=m+2$，并选

$$
 k=k(m)=\left\lfloor\frac34\log_2M\right\rfloor.
 \tag{6.1}
$$

当 $M\ge32$ 时，$1\le k<m$，且

$$
 \frac12M^{3/4}\le2^k\le M^{3/4},
 \qquad16^{k-1}\ge\frac{M^3}{256}.
 \tag{6.2}
$$

把近似算子 (5.5) 再拆成

$$
 T_k=H_{k,m}+C_m,\qquad
 H_{k,m}=G_k+\sum_{j=k}^{m-1}\delta_jE_j.
 \tag{6.3}
$$

$G_k$ 作用于前 $k$ 位；中间段的 $E_j$ 和 $C_m$ 都作用于不相交的位。因此这些头、中、尾算子彼此交换，中间段的幂零阶至多 $m-k+1$。由二项展开和 (5.4)，

$$
 H_{k,m}^{,2^k+m-k}=0. \tag{6.4}
$$

故 $e^{tH_{k,m}}$ 是 $t$ 的次数至多

$$
 d_m=2^k+m-k-1\le M+M^{3/4} \tag{6.5}
$$

的算子多项式。此外

$$
 \|H_{k,m}\|+\|C_m\|
 \le\tfrac83\Delta+\sum_{j\ge k}\delta_j
 \le\tfrac{22}{3}<8.
 \tag{6.6}
$$

这里没有把整个前 $m$ 位真实链当成次数 $m$ 的幂零算子。真实有限链仅截到 $k\asymp\log m$ 位，其阶 $2^k=O(m^{3/4})=o(m)$；其余 $m-k$ 位采用独立矩阵单位，并把替换误差保留在 (5.5) 中。

## 7. Duhamel 误差远小于尾部指数权

取任意 $f\in\ker L$。由 (5.5)，

$$
 \|T_kf\|\le22\eta_{k-1}\|f\|.
 \tag{7.1}
$$

$H_{k,m}$ 与 $C_m$ 交换，因此对实 $t\ge0$ 有精确积分公式

$$
 e^{tH_{k,m}}f-e^{-tC_m}f
 =\int_0^t e^{(t-s)H_{k,m}}e^{-sC_m}T_kf\,ds.
 \tag{7.2}
$$

这也可直接对 $e^{(t-s)H_{k,m}}e^{-sC_m}$ 求导得到。注意它不要求 $L$ 与 $T_k$ 交换；这里只使用 $Lf=0$ 后的范数误差 (7.1)。结合 (6.6)，

$$
 \|e^{tH_{k,m}}f-e^{-tC_m}f\|
 \le22t e^{8t}\eta_{k-1}\|f\|.
 \tag{7.3}
$$

在后续的整个区间 $t=uM^2/2$、$1\le u\le20$ 上，$t\le10M^2$。由 (5.2)、(6.2)，

$$
 \eta_{k-1}\le
 e^{-770M^3/256}\le e^{-3M^3}.
$$

故 (7.3) 除以 $\|f\|$ 后不超过

$$
 220M^2\exp(80M^2-3M^3).
 \tag{7.4}
$$

当 $M\ge32$ 时，$220M^2\le e^{M^2}$、$3M-81\ge15$，因此

$$
 220M^2e^{80M^2-3M^3}
 \le e^{-15M^2}\le e^{-20M}.
 \tag{7.5}
$$

现在定义次数至多 $d_m$ 的复多项式

$$
 p_m(u)=\left\langle e^{uM^2H_{k,m}/2}f,1\right\rangle.
 \tag{7.6}
$$

它满足 $p_m(0)=\langle f,1\rangle$。另一方面，

$$
 \left|\left\langle e^{-uM^2C_m/2}f,1\right\rangle\right|
 \le\|f\|F_m(uM^2/2).
$$

将此式与 (7.5)、(2.8) 合并。由于
$e^{-20M}\le e^{-10M-14}\le F_m(uM^2/2)$ 对 $M\ge32$ 成立，得到

$$
 \boxed{
 |p_m(u)|\le2\|f\|F_m(uM^2/2)
 \le2\|f\|e^{M h(u)+14},
 \quad1\le u\le20.
 } \tag{7.7}
$$

## 8. 原临界核均值为零，再由循环性排除全核

若某个 $p_m$ 恒为零，已经有 $\langle f,1\rangle=0$。其余情形对 (7.7) 使用 (1.4)，并代入 (3.2)、(6.5)，得到

$$
 \begin{aligned}
 |\langle f,1\rangle|
 &\le2\|f\|\exp\left(
       14+d_m g_0+M\int_1^{20}h\,d\omega_0\right)\\
 &\le2\|f\|\exp\left(
       14-\frac{13}{100}M+g_0M^{3/4}\right).
 \end{aligned}
 \tag{8.1}
$$

由于 $g_0$ 为固定有限常数，右边随 $m\to\infty$ 趋零。因此

$$
 \ker L\perp1. \tag{8.2}
$$

最后一步使用实际模型的已证循环性，而不使用纯模型的局部交换子。$L$ 是 $A$ 的多项式范数极限，故与 $A$ 交换；因此若 $f\in\ker L$，则每个 $A^nf\in\ker L$。对这些向量逐个应用 (8.2)，

$$
 \langle f,(A^*)^n1\rangle
 =\langle A^nf,1\rangle=0,
 \qquad n\ge0.
$$

R11 证明 $1$ 对 $A$ 循环；R24/R33 的共轭
$\mathcal C f(y)=\overline{f(-1-y)}$ 满足 $\mathcal C1=1$、$\mathcal C A\mathcal C=A^*$，故 $1$ 对 $A^*$ 也循环。这些矩分离全 $H$，所以

$$
 \boxed{\ker L=\{0\}.} \tag{8.3}
$$

同一共轭把 $L$ 变为 $L^*$，因为 $L$ 是 $A$ 的多项式范数极限。因此 $\ker L^*=\mathcal C(\ker L)=0$，得到

$$
 \boxed{\overline{\operatorname{Ran}L}=H.} \tag{8.4}
$$

R43 的精确因式分解

$$
 D=L\Psi(L),\qquad
 \Psi(z)=\frac{1-e^{-z}}z,\quad\Psi(0)=1,
$$

其中 $\Psi(L)$ 有界可逆且与 $L$ 交换，因而

$$
 \boxed{
 \ker D=0,\qquad
 \overline{\operatorname{Ran}D}=H.
 } \tag{8.5}
$$

特别地，每个正整数 $q$ 都有 $\ker L^q=\ker D^q=0$。又由 $1$ 对 $A$ 循环、$D$ 有界且与 $A$ 交换，

$$
 \overline{\operatorname{span}}\{A^nD1:n\ge0\}
 =\overline{D H}=H.
 \tag{8.6}
$$

因此原临界向量

$$
 f_*=D1=1-\prod_{j\ge0}r_j^{b_j}
$$

确实循环。这关闭了该原临界乘积差的核/闭值域缺口。

进一步，对每个整数 $q\ge1$，$D^q$ 与 $L^q$ 仍然单射、稠密值域并与 $A$ 交换，所以 $D^q1$、$L^q1$ 全部循环。更一般地，这些算子把任何已知的 $A$-循环向量送到循环向量：将该向量的多项式轨道先取闭包，再作用以有界算子，其轨道闭包就是对应的稠密闭值域。

原二维空间 $\operatorname{span}\{1,Q1\}$ 的每个非零向量也循环。确实，若 $\alpha+\beta\ne0$，由 R36 已证的 $\sigma(Q)=\{1\}$，算子 $\alpha I+\beta Q$ 可逆且与 $A$ 交换，故 $(\alpha I+\beta Q)1$ 循环；若 $\alpha+\beta=0$ 且系数不全零，则该向量是 $D1$ 的非零标量倍。$1$ 和 $Q1$ 本身线性无关，因为若 $Q1=c1$，则 $c\in\sigma(Q)$ 迫使 $c=1$，与 $D1\ne0$ 矛盾。

## 9. 适用边界

证明全程处理任意 $L^2$ 核向量，不假设连续、有限 Walsh 次数、有限乘积和、整数点迹或条件期望的逼近速度。真实进位没有删掉：先在 $k$ 位保留真实有限链，再把全部替换误差通过 (7.2) 传到最终多项式界。

这里也没有使用有限核投影的收敛、把稠密核心结论推广到全空间、或者把有限迹表示结论转给纯表示。有限迹状态比较与最大头系数角度不等式可以继续作为独立问题，但原临界核的排除不再依赖它们。

本结论只表明这一个临界向量不能提供该 odometer 的普通不变子空间；它没有证明该算子的每个非零向量循环。一般 ISP 的课题完成标准保持不变。
