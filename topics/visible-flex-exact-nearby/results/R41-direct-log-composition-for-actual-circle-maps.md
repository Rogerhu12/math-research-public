# R41：实际非近恒等角图的直接 log 权复合与差量

2026-11-12，independent-audit。

**状态：已证明的角变量定理。** 对一个实际实解析、保向圆周
微分同胚，只用其正导数下界、导数上界、真实复条带及二阶导数界，
证明同一直接 log 权中的复合估计。映射不必接近恒等。代价为任意
预先选定的 $\varepsilon>0$ 阶导数以及下面明确的有限常数。
反向复合、差量、半密度和有限阶算子的共轭费用也全部列出。

本篇只处理 $\theta\mapsto H(\theta)$ 这样的真实角图。它不能证明
mixed Tricomi 逆坐标中的非解析径向函数获得正解析或 log 角宽；
该区别见 [R39](R39-finite-component-airy-transfer-input.md) §1。
也不将当前有限样条或浮点返回图自动授予这里的解析输入。

## 1. 范数与实际解析输入

在 $2\pi$ 圆周上使用平均测度和全部整数 Fourier 模，记
$$
\langle j\rangle=(1+j^2)^{1/2},\qquad
\omega(t)=\bigl(\log(e+t)\bigr)^{3/2}-1\quad(t\ge0),
$$
$$
W_\rho(j)=e^{\rho\omega(|j|)},\qquad
\|u\|_{s,\rho}^2=\sum_{j\in\mathbb Z}
       \langle j\rangle^{2s}W_\rho(j)^2|u_j|^2.
\tag{1.1}
$$
这里 $s,\rho\in\mathbb R$；相反符号权也包含在定理中。
直接微分可得 $\omega(0)=0$、$\omega'>0$、$\omega''<0$，因此
$\omega$ 次可加，并且
$$
|\omega(|j|)-\omega(|k|)|\le\omega(|j-k|).
\tag{1.2}
$$

设 $H:\mathbb R\to\mathbb R$ 为保向提升，
$$
H(x+2\pi)=H(x)+2\pi,\qquad
0<m\le H'(x)\le M.
\tag{1.3}
$$
由于一周期平均导数为 $1$，可以且以下总取 $m\le1\le M$。
要求 $H(z)-z$ 在实际条带 $|\operatorname{Im}z|<b_0$ 全纯，
并已给出
$$
\sup_{|\operatorname{Im}z|<b_0}|H''(z)|\le L_2<\infty.
\tag{1.4}
$$
这组量是实际输入，不是以“光滑”代替的存在性假设。定义
$$
b=\min\{1,b_0/2,m/(2L_2)\}>0,
\tag{1.5}
$$
$L_2=0$ 时第三项视为 $+\infty$。
由沿竖线积分，整个闭条带 $|\operatorname{Im}z|\le b$ 上
$$
\frac m2\le\operatorname{Re}H'(z)\le\frac{3M}{2},
\qquad |H'(z)|\le\frac{3M}{2}.
\tag{1.6}
$$
所以 $\operatorname{Im}H(x+iy)$ 与 $y$ 同号，且其绝对值夹在
$m|y|/2$ 与 $3M|y|/2$ 之间。

设 $\mathcal C_Hu=u\circ H$。实变量换元已经给
$$
\|\mathcal C_H\|_{L^2\to L^2}\le m^{-1/2}.
\tag{1.7}
$$
下面把它提升到同一 $W_\rho$，而不要求 $H-\mathrm{id}$ 小。

## 2. 显式复合常数与主定理

定义实际锥常数
$$
R=\max\{4M,4/m,2\},\qquad
c=\frac{bm}{8},\qquad
J=\lceil\log_2R\rceil+1,
$$
$$
R_b=2^{J+1},\qquad d=\log R_b,\qquad
F_0=\coth(c/2).
\tag{2.1}
$$
对给定 $s\in\mathbb R$、$\rho\in\mathbb R$、$\varepsilon>0$，置
$$
\begin{aligned}
B_{\rm near}&=4^\varepsilon(\sqrt2R_b)^{|s|}
 \exp\left[\frac{9\rho^2d^2}{16\varepsilon}
             +\frac{3|\rho|}{2}d^{3/2}\right],\\
K_{\rm far}&=|\rho|(3/e)^{3/2}+2(|s|+\varepsilon)/e,\\
E_{\rm far}&=\exp\left[K_{\rm far}\sqrt e
                      +\frac{K_{\rm far}^2}{2c}\right],\\
\mathfrak C_H(s,\rho,\varepsilon)
&=(2J+1)(m^{-1/2}+F_0)B_{\rm near}
                  +E_{\rm far}^{\,2}\coth(c/4).
\end{aligned}
\tag{2.2}
$$
所有常数只读 (1.3)–(1.5)，没有读 $H-\mathrm{id}$ 的小量。

**定理 2.1。** 满足 §1 的实际角图有唯一连续延拓
$$
\boxed{\quad
\mathcal C_H:H^{s+\varepsilon}_\rho\longrightarrow H^s_\rho,
\qquad
\|\mathcal C_Hu\|_{s,\rho}
\le\mathfrak C_H(s,\rho,\varepsilon)
                    \|u\|_{s+\varepsilon,\rho}.\quad}
\tag{2.3}
$$
该延拓在定义域内的平滑函数上等于真实复合，且包含均值、正负频率及其
所有混合。$\rho=0$ 时本界不是普通 Sobolev 复合的最优估计；
它的用途是同一正 log 权及反向权中的统一费用。
当 $\rho<0$ 时，(1.1) 还允许超多项式增长的 Fourier 序列；
对这些不一定是分布的输入，“复合”准确指由三角多项式得到的
有界 Fourier 延拓，不附加一个未经定义的分布复合声称。

## 3. 傅里叶矩阵的锥外指数界

矩阵元为
$$
C_{kj}=\frac1{2\pi}\int_0^{2\pi}
                  e^{ijH(x)-ikx}\,dx.
\tag{3.1}
$$
称下列集合为近锥：$(j,k)=(0,0)$，或
$$
jk>0,\qquad R^{-1}\le |k|/|j|\le R.
\tag{3.2}
$$
令 $C^{\rm far}$ 为将 (3.1) 限于其补集的矩阵，其他元取零。
则
$$
\boxed{\quad |C^{\rm far}_{kj}|
           \le e^{-c(|j|+|k|)}.\quad}
\tag{3.3}
$$

**证明。** 先设 $j>0$。因为被积函数全纯且一周期相容，可把
积分线平移到 $x+ib$ 或 $x-ib$。前者的绝对值由
$\exp[-bmj/2+bk]$ 控制，后者由
$\exp[3bMj/2-bk]$ 控制。

若 $k\le0$，取前者；若 $0<k<j/R$，由 $R\ge4/m$ 得指数
至多 $-bmj/4$。若 $k>Rj$，取后者，由 $R\ge4M$ 得指数
至多 $-5bk/8$。在每种情形，这都不超过
$-bm(j+|k|)/8$。$j<0$ 用实映射的共轭对称性，$j=0$ 则
$C_{k0}=\delta_{k0}$。得到 (3.3)。证毕。

因
$$
\sum_{n\in\mathbb Z}e^{-a|n|}=\coth(a/2),
\tag{3.4}
$$
Schur 检验给 $\|C^{\rm far}\|_{\ell^2\to\ell^2}\le F_0$。
故 $C^{\rm near}=C-C^{\rm far}$ 满足
$$
\|C^{\rm near}\|_{\ell^2\to\ell^2}
\le m^{-1/2}+F_0.
\tag{3.5}
$$
这里没有声称任意逐元删去矩阵的操作都保持算子 norm；(3.5)
来自完整复合减去已经单独证明有界的锥外矩阵。

## 4. 近锥的同 log 权费用

按 $1+|j|$ 分成 dyadic 块
$$
I_n=\{j:2^n\le1+|j|<2^{n+1}\},\qquad n=0,1,\ldots.
$$
近锥矩阵只连接 $|n-m|\le J$ 的块。对于这样的一对块内的
任意输入 $j$、输出 $k$，即使两者本身不在近锥，也有
$$
R_b^{-1}\le\frac{1+|k|}{1+|j|}\le R_b,\qquad
R_b^{-1}\le\frac{e+|k|}{e+|j|}\le R_b,
$$
$$
\max\left\{\frac{\langle k\rangle}{\langle j\rangle},
            \frac{\langle j\rangle}{\langle k\rangle}\right\}
\le\sqrt2R_b.
\tag{4.1}
$$
令 $x=\log(e+|j|)\ge1$，则
$$
|\omega(|k|)-\omega(|j|)|
\le\tfrac32d\sqrt{x+d}
\le\tfrac32d\sqrt x+\tfrac32d^{3/2}.
$$
对 $a\sqrt x\le\varepsilon x+a^2/(4\varepsilon)$ 取
$a=3|\rho|d/2$，得到
$$
\frac{W_\rho(k)}{W_\rho(j)}
\le(e+|j|)^\varepsilon
 \exp\left[\frac{9\rho^2d^2}{16\varepsilon}
               +\frac{3|\rho|}{2}d^{3/2}\right].
\tag{4.2}
$$
再用 $(e+|j|)/\langle j\rangle<4$，可得这两个完整块之间的
输出、输入权比至多 $B_{\rm near}$：
$$
\frac{\langle k\rangle^s W_\rho(k)}
     {\langle j\rangle^{s+\varepsilon}W_\rho(j)}
\le B_{\rm near}.
\tag{4.3}
$$
因此每个加权 block 的 norm 至多
$B_{\rm near}(m^{-1/2}+F_0)$，这里是先取输出权上确界和输入
逆权上确界，再用 (3.5)；没有逐元绝对值化近锥矩阵。块矩阵的
每行、列最多 $2J+1$ 个非零块，离散 Schur 检验遂给
$$
\|C^{\rm near}\|_{H^{s+\varepsilon}_\rho\to H^s_\rho}
\le(2J+1)B_{\rm near}(m^{-1/2}+F_0).
\tag{4.4}
$$

## 5. 锥外的完整加权 bound

对 $x>0$，初等最大值计算给
$$
\log x\le(3/e)x^{1/3},\qquad
\log x\le(2/e)x^{1/2}.
$$
所以对任意 $n\ge0$，
$$
|\rho|\omega(n)+(|s|+\varepsilon)\log\langle n\rangle
\le K_{\rm far}\sqrt{e+n}
\le K_{\rm far}\sqrt e+K_{\rm far}\sqrt n.
\tag{5.1}
$$
再用
$K_{\rm far}\sqrt n\le(c/2)n+K_{\rm far}^2/(2c)$，得到
$$
e^{|\rho|\omega(n)}\langle n\rangle^{|s|+\varepsilon}
                         e^{-cn}
\le E_{\rm far}e^{-cn/2}.
\tag{5.2}
$$
对输入、输出分别使用该式，(3.3) 的加权矩阵元至多
$E_{\rm far}^2e^{-(c/2)(|j|+|k|)}$。由 (3.4)，
$$
\|C^{\rm far}\|_{H^{s+\varepsilon}_\rho\to H^s_\rho}
\le E_{\rm far}^2\coth(c/4).
\tag{5.3}
$$
(4.4) 与 (5.3) 合并即为定理 2.1 的完整证明。
由于三角多项式在所有 (1.1) 空间中稠密，该有界矩阵唯一延拓。
对定义域内平滑函数，其 Fourier 部分和在每个固定有限光滑档
收敛，真实复合亦收敛；与加权矩阵极限逐个 Fourier 系数比较，
便得到所声称的一致性。一般负权输入只使用前述有界延拓。

## 6. 反向角图也有显式实际输入

不必假定一个未知的逆解析半径。由 (1.6)，$H$ 在条带 $|y|<b$
单叶：若 $z_1\ne z_2$，沿线段积分得到
$$
H(z_1)-H(z_2)
=(z_1-z_2)\int_0^1H'(z_2+t(z_1-z_2))dt\ne0,
$$
因为后一个积分的实部至少 $m/2$。

对任意实中心 $x$，给定 $|w-H(x)|<mb/4$，在 $|\eta|\le b/2$
上求
$$
\eta=\frac{w-H(x)-[H(x+\eta)-H(x)-H'(x)\eta]}{H'(x)}.
\tag{6.1}
$$
右端导数绝对值至多 $L_2b/(2m)\le1/4$，且其值绝对值至多
$b/4+L_2b^2/(8m)\le5b/16<b/2$。压缩映射与复隐函数定理给
唯一解析逆；这些实中心圆盘的并包含 $|\operatorname{Im}w|<mb/4$，
单叶性保证各片一致。记 $K=H^{-1}$，则可直接供应
$$
b_{0,K}=mb/4,\qquad
m_K=1/M,\quad M_K=1/m,\qquad
L_{2,K}=8L_2/m^3.
\tag{6.2}
$$
最后一式来自 $K''=-(H''\circ K)/(H'\circ K)^3$ 与
$|H'\circ K|\ge m/2$。$K(w)-w$ 同样 $2\pi$ 周期。
用 (6.2) 代入 §2 便得到
$$
\mathcal C_{H^{-1}}:H^{s+\varepsilon}_\rho\to H^s_\rho
\tag{6.3}
$$
的全部显式常数。

$\mathcal C_H$ 与 $\mathcal C_{H^{-1}}$ 在平滑数据上准确互逆。
延拓到上述带损失的空间时，恒等式在具有两次所需导数预算的输入上
由稠密性成立；不是声称 (2.3) 的两个不同 Sobolev 档自动构成
同档 Banach 同构。

## 7. 乘法、半密度及真实相位 frame

为明确使用复合时的 Jacobian 费用，定义
$$
\mathfrak M_{s,\rho}(a)
=2^{|s|/2}\sum_{k\in\mathbb Z}
 \langle k\rangle^{|s|}e^{|\rho|\omega(|k|)}|a_k|.
\tag{7.1}
$$
由 (1.2)、离散 Young 不等式与
$\langle j\rangle/\langle j-k\rangle\le\sqrt2\langle k\rangle$，
$$
\|au\|_{s,\rho}\le\mathfrak M_{s,\rho}(a)\|u\|_{s,\rho},
\qquad
\mathfrak M_{s,\rho}(ab)
\le\mathfrak M_{s,\rho}(a)\mathfrak M_{s,\rho}(b).
\tag{7.2}
$$
这也可以从一个实际解析上界有限地估计。若周期 $a$ 在条带
$|y|<\beta$ 上有 $|a|\le A_\beta$，则令
$$
L_a=|\rho|(3/e)^{3/2}+2|s|/e,
$$
利用 $|a_k|\le A_\beta e^{-\beta|k|}$ 和 §5 同一计算，得到
$$
\boxed{\quad
\mathfrak M_{s,\rho}(a)
\le2^{|s|/2}A_\beta
 \exp[L_a\sqrt e+L_a^2/(2\beta)]\coth(\beta/4).\quad}
\tag{7.3}
$$

真实半密度变换为
$$
\mathcal U_Hu=\sqrt{H'}\,(u\circ H).
\tag{7.4}
$$
它在 $L^2$ 上准确酉，逆为 $\mathcal U_{H^{-1}}$，因为实换元
精确抵消 $H'$。其同 log 权 bound 是
$$
\|\mathcal U_H\|_{H^{s+\varepsilon}_\rho\to H^s_\rho}
\le\mathfrak U_H(s,\rho,\varepsilon)
:=\mathfrak M_{s,\rho}(\sqrt{H'})
                                  \mathfrak C_H(s,\rho,\varepsilon).
\tag{7.5}
$$
由 (1.6)，$H'$ 在 $|y|<b$ 落于右半平面，其正平方根是实际
全纯分支，并满足 $|\sqrt{H'}|\le\sqrt{3M/2}$。
因此 (7.3) 用 $\beta=b$ 就付清 (7.5) 的乘法常数。
完整 conormal 密度若要求 $H'\mathcal C_H$，则把该乘子换为
$H'$，以 $A_b=3M/2$ 同样计算。

因此可以在真实 height、conormal 与半密度 frame 间列出费用；
不能省略其中任何一个，再把不同 frame 的低阶相位常数认作相同。

## 8. 实际两个角图的差量与参数导数

设 $H,G$ 有相容实提升，并在同一个实际条带上满足共同的
$m,M,L_2,b_0$ 门。置 $d=H-G$，$H_t=G+td$。
所有 $H_t$ 都保向，保持同一解析条带和这些共同界。
对平滑 $u$，完整恒等式为
$$
u\circ H-u\circ G
=d\int_0^1u'\circ H_t\,dt.
\tag{8.1}
$$
由定理 2.1、(7.2) 及 $\|u'\|_{r,\rho}\le\|u\|_{r+1,\rho}$，
$$
\boxed{\quad
\|\mathcal C_H-\mathcal C_G\|_
 {H^{s+\varepsilon+1}_\rho\to H^s_\rho}
\le\mathfrak M_{s,\rho}(H-G)
             \mathfrak C(s,\rho,\varepsilon;m,M,L_2,b_0).\quad}
\tag{8.2}
$$
这额外的一阶导数是实际差量费用，没有把 moving composition
声称为同档 norm 连续。$\mathfrak M(H-G)$ 可直接使用真实 Fourier
数据，或以 (7.3) 的条带差量计算。

若实际参数族 $H_a$ 具有共同门和真实前两阶参数导数，则
$$
\partial_a\mathcal C_{H_a}u=(\partial_aH_a)(u'\circ H_a),
$$
$$
\partial_a^2\mathcal C_{H_a}u
=(\partial_a^2H_a)(u'\circ H_a)
 +(\partial_aH_a)^2(u''\circ H_a).
\tag{8.3}
$$
故其 $H^{s+\varepsilon+1}_\rho\to H^s_\rho$ 一阶 norm 不超过
$\mathfrak C\mathfrak M(\partial_aH_a)$，二阶的
$H^{s+\varepsilon+2}_\rho\to H^s_\rho$ norm 不超过
$$
\mathfrak C\left[
\mathfrak M_{s,\rho}(\partial_a^2H_a)
+\mathfrak M_{s,\rho}(\partial_aH_a)^2\right].
\tag{8.4}
$$
只要求估计而没有供应实际参数导数的族，不能引用 (8.3)–(8.4)。

### 8.1 半密度的完整差量

记 $a_H=\sqrt{H'}$、$a_G=\sqrt{G'}$。在同一条带 $|y|<b$，
两平方根的实部都至少 $\sqrt{m/2}$，所以
$$
a_H-a_G=d' b_{HG},\qquad
b_{HG}=\frac1{\sqrt{H'}+\sqrt{G'}},\qquad
|b_{HG}|\le(2m)^{-1/2}.
\tag{8.5}
$$
这是实际全纯 reciprocal；其 $\mathfrak M$ 由 (7.3) 支付。
准确分解
$$
\mathcal U_H-\mathcal U_G
=a_H(\mathcal C_H-\mathcal C_G)
 +(a_H-a_G)\mathcal C_G
$$
给
$$
\begin{aligned}
\|\mathcal U_H-\mathcal U_G\|_
 {H^{s+\varepsilon+1}_\rho\to H^s_\rho}
\le\mathfrak C\,[&\mathfrak M(a_H)\mathfrak M(d)\\
                 &+\mathfrak M(d')\mathfrak M(b_{HG})].
\end{aligned}
\tag{8.6}
$$
右端的 $\mathfrak M$ 均在同一个 $s,\rho$ 档，不隐藏角导数差量。

对实际参数族，令 $A=\sqrt{H_a'}$，用点表示参数导数，则
$$
\dot A=\frac{\dot H_a'}{2\sqrt{H_a'}},\qquad
\ddot A=\frac{\ddot H_a'}{2\sqrt{H_a'}}
       -\frac{(\dot H_a')^2}{4(H_a')^{3/2}}.
\tag{8.7}
$$
所有 reciprocal 的分支和条带下界均由 (1.6) 给出。准确有
$$
\partial_a\mathcal U_{H_a}u
=\dot A(u\circ H_a)+A\dot H_a(u'\circ H_a),
$$
$$
\partial_a^2\mathcal U_{H_a}u
=\ddot A(u\circ H_a)
 +(2\dot A\dot H_a+A\ddot H_a)(u'\circ H_a)
 +A(\dot H_a)^2(u''\circ H_a).
\tag{8.8}
$$
因此一阶、二阶 norm 分别以 $\mathfrak C$ 乘
$$
\mathfrak M(\dot A)+\mathfrak M(A)\mathfrak M(\dot H_a),
$$
$$
\mathfrak M(\ddot A)+2\mathfrak M(\dot A)\mathfrak M(\dot H_a)
+\mathfrak M(A)\mathfrak M(\ddot H_a)
+\mathfrak M(A)\mathfrak M(\dot H_a)^2
\tag{8.9}
$$
控制，输入分别是 $H^{s+\varepsilon+1}_\rho$ 与
$H^{s+\varepsilon+2}_\rho$。所需角导数与参数导数必须由实际族
提供，而不是从单个角图的界自动推出。

## 9. 共轭真实逆与 smoothing 的有限损失

以下说明如何把本篇放进
[R31](R31-actual-parameter-circle-normalization.md) 的实际解析
共轭与 [R40](R40-finite-unitary-two-order-normal-form.md) 的
加权算子之间。设一个实际 $T$ 已在相应有限窗口满足
$$
\|T:H^{r+d}_\rho\to H^r_\rho\|\le M_r.
\tag{9.1}
$$
$d$ 可以为正，也可以为负。由两次 (7.5)，准确有
$$
\boxed{\quad
\|\mathcal U_H^{-1}T\mathcal U_H:
 H^{s+d+2\varepsilon}_\rho\to H^s_\rho\|
\le\mathfrak U_{H^{-1}}(s,\rho,\varepsilon)
 M_{s+\varepsilon}
 \mathfrak U_H(s+d+\varepsilon,\rho,\varepsilon).
\quad}
\tag{9.2}
$$
每个中间档都在式中显示。普通复合用 $\mathfrak C$ 代替
$\mathfrak U$ 得同样结论。

例如，若 $T$ 是损失一阶的反馈逆，新的明确损失为
$1+2\varepsilon$。若 $T$ 原有三阶 smoothing，则只从本篇
推出共轭后增益 $3-2\varepsilon$；要以恰好三阶余项使用 R40，
须在前面的实际有限 columns 中多预付至少 $2\varepsilon$ 阶。
多预留一个整数阶并取 $0<\varepsilon<1/2$ 是一个充分做法，
不是把导数损失略去。

常数可能很大，但全部有限且可由实际输入计算。低阶系数的非小
振幅不能被这种 norm 转移消除；它们仍进入 R40 的 $Q,K$，
完整相位、真实有限低块与全网 Schur 也仍分别验证。

## 10. 对当前曲面工作的准确使用范围

本篇证明：若真实返回共轭已经供应了实际解析角图和导数、逆导数
预算，就不必再要求它接近恒等，仍可进入同一直接 log 权，支付
任意固定小量的有限导数损失。证明只用了固定实角的解析延拓、
真实 Fourier 矩阵、实 $L^2$ 换元与有限 dyadic 分块。

本篇未证明当前 Cauchy/返回算子具有 R40 的完整标量符号，未消掉
外侧负组件，也未赋予 mixed-radial 坐标中的样条正角权。R39 的
有限实际 jet、正组件 contact、多组件全网、完整低阶相位及本题
最终精确等距与几何预算仍是各自的实际输入。
