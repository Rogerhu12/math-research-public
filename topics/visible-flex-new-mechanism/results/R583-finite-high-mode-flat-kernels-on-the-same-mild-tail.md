# R583 同一温和尾上 j≤8 的真实全平端模

状态：严格有限频率补证，供 R576 的有限高度表示使用。没有证明全频 tame 逆、非线性分支或闭面完成。
本条不重做 R571 的二阶模数值计算；它补足此前 j=4,6,8 仅作数值 probe 的端部存在性。

## 1. 同一个固定输入

沿用 [R571](../results/R571-milder-phase-tail-flat-kernel-and-core-shooting-zero.md) 的 $r_c=11/50$、$\ell=1/5$、$A=4/5$，
$$
w_\varphi(r)=A e^{-u(2-\sin(u+\varphi))},\qquad u=\ell/(r-r_c),\quad 0\le\varphi\le2\pi.
$$
固定整数 $2\le j\le8$，记 $\mu=j^2$。准确角模方程为
$$
(wf')'-\mu\frac{w'}r f=0. \tag{1}
$$
置 $f=r^\mu y$，链式法则给
$$
(py_u)'+\varepsilon p y=0,\quad p=4u^2r(u)^{2\mu}e^{-u(2-\sin(u+\varphi))},\quad
\varepsilon=\frac{\mu(\mu-1)\ell^2}{r(u)^2u^4}. \tag{2}
$$
这里 $r(u)=r_c+\ell/u$，没有固定半径替代。

## 2. 相同单谷区间仍准确适用

有
$$
(\log p)'=u(\cos(u+\varphi)-\eta(u)),\qquad
\eta=\frac{2-\sin(u+\varphi)}u-\frac2{u^2}+\frac{2\mu\ell}{r u^3}. \tag{3}
$$
在 $u\ge100$、$4\le\mu\le64$，
$$
0<\eta<\frac3{100}+\frac{128/5}{(11/50)10^6}<.031,
$$
且
$$
|\eta'|\le\frac1u+\frac3{u^2}+\frac4{u^3}
 +\frac{2\mu\ell^2}{r_c^2u^5}+\frac{6\mu\ell}{r_cu^4}<.011. \tag{4}
$$
因此 R571 的 stationary-point 论证原样成立：对每个 $n\ge17$，唯一最大点 $\alpha_n$ 位于
$$
\pi/2+2\pi n-\varphi-.04<\alpha_n<\pi/2+2\pi n-\varphi,
$$
唯一谷点位于对应 $3\pi/2$ 中心右侧 .04 内；相邻最大点距离在6与7之间，权先降后升。全部这些区间均在 $u>100$。

固定一 cell 左端 $a=\alpha_n$，令 $C_a=4r_c^{2\mu}a^2$。在 $a\le u<a+7$，
$$
1\le \frac{u^2r(u)^{2\mu}}{a^2r_c^{2\mu}}
 \le(107/100)^2e^{64/55}<4.
$$
最后一不等式例如由 $(107/100)^2<6/5$、$e^{64/55}<e^{6/5}<10/3$ 得到；后者可直接用指数级数的有限和及几何尾上界核验。
从而
$$
e^{-21}C_a e^{-a(2-\sin(u+\varphi))}\le p(u)
 \le4C_a e^{-a(2-\sin(u+\varphi))}. \tag{5}
$$
同时
$$
a^{-4}\le\varepsilon(u)\le3400a^{-4}. \tag{6}
$$
上界使用 $\mu(\mu-1)\le4032$、$r\ge.22$；下界使用 $\mu(\mu-1)\ge12$、$r\le.222$、$u\le1.07a$。
因此 $(49/2)\varepsilon_{\max}<.001<1/2$。R569 已证的单谷 Dirichlet/Green 引理仍适用，其常数不依赖权的 contrast。

## 3. DtN 对角占优与实际端模

记 $R_* =\int p^{-1}$、$K=1/R_*$。仍用两端各长1/2的窗及中间长1的谷窗，(5) 给
$$
K\le4C_a e^{-11a/4},\qquad
\int pH_L^2,\ \int pH_R^2\ge\frac{e^{-21}C_a}{16}e^{-5a/4}. \tag{7}
$$
端窗的电阻占比至多 $2e^{21}e^{-3a/2}<1/2$，所以其中对应零势插值 $H_i\ge1/2$；这支付了第二个估计中的端值控制。
由含势 Green domination 及 (6)，准确 DtN 满足
$$
0<-D_{LR}\le2K,\qquad
D_{LL},D_{RR}\le-\frac{e^{-21}C_a}{32a^4}e^{-5a/4}<0. \tag{8}
$$
把 $K$ 项吸收进势能项所需的不等式是 $128e^{21}a^4e^{-3a/2}<1$，在 $a\ge100$ 直接成立。

写 $k_n=-D_{n,LR}$、$V_n=-(D_{n-1,RR}+D_{n,LL})$。
前一 cell 左端与 $a=\alpha_n$ 相差小于7，且对应 $C_{a_-}\le C_a$。(7)--(8) 因此给共同的保守界
$$
\frac{k_{n-1}}{V_n},\frac{k_n}{V_n}
 \le1024e^{42}a^4e^{-3a/2}<1/64. \tag{9}
$$
例如前一耦合的直接系数为 $256e^{21+77/4}$，小于 (9) 的系数。最后一不等式在100处可用 $1024\cdot10^8e^{-108}<1024\cdot10^8 2^{-108}<1/64$ 核验，并由 $a^4e^{-3a/2}$ 递减延伸。

准确通量匹配与交替符号变换给
$$
\rho_n=\frac{k_{n-1}}{V_n-k_n\rho_{n+1}}.
$$
在 $0\le\rho\le1/32$ 上，映像仍位于 $(0,1/32)$，导数不超过
$$
\frac{(1/64)^2}{(1-1/2048)^2}<10^{-3}.
$$
从有限 $\rho_{M+1}=0$ 反推并取极限，得到唯一的正比值链。对应每 cell 的准确 ODE 解全通量匹配，且
$$
|\rho_n-\rho_n^{(M)}|\le\frac1{32}10^{-3(M-n+1)}. \tag{10}
$$
令 $y(\alpha_{17})=1$，则此真实解非零。
由 (9)，足够大的 $n$ 有 $\rho_n\le e^{-\alpha_n}$，故节点幅度衰减如 $e^{-c\alpha_n^2}$。
各固定阶 ODE 系数导数只有 $u$ 的多项式增长；cell 内的 Gronwall 损失至多 $e^{C_k u}$。
因此所有固定阶 $r$ 导数都全平，$f$ 在 $r=r_c$ 向零光滑延拓。全部估计对有限集合 $2\le j\le8$ 和紧相位区间一致。

两个全平解的 $w(f_1f_2'-f_1'f_2)$ 在平端为零且沿区间恒定，所以全平解空间一维。
有限 DtN 与端点连续性及一致收缩亦给归一种子对相位的连续依赖。
这证明了每个 $j=2,4,6,8$ 都有同一固定尾上的实际全平端模，而不再只是有限积分试探。

## 4. 向量场与数值范围

令
$$
A_j=\frac{w(\mu f-rf')}{\mu-1},\qquad
V_j=A_j\cos(j\theta)e_r-\frac{A_j}{j}\sin(j\theta)e_\theta+f\cos(j\theta)e_z.
$$
(1) 给 $A_j'=wf'$。对背景 $X=(re_r,h)$、$h'=-w$ 直接微分，
$$
\delta E=2(A_j'-wf')\cos(j\theta)=0,
$$
$$
\delta F=-\frac{rA_j'+(\mu-1)A_j-\mu wf}{j}\sin(j\theta)=0,
\qquad \delta G=0.
$$
因此这些是实际全平无穷小场，可作为非线性表示中的准确端部基。

本条没有给各模在整个连接头的核心 shooting 零，也没有说这些零可同时发生。
数值实现须报告实际核心 trace，并把为满足外端边界而作的校正放回完整残差。
(10) 仅约束准确 DtN 的有限截断；它不控制浮点 ODE 误差。
现有较高模 probe 可引用其原数值身份，但本条不补记任何未执行的精化。
超过8的所有频率、角向无限谱非线性解及固定度量收敛仍须继续支付。
