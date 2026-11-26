# R1041：原 r=2 bare 高系数与实际 Hodge graph 核的范数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
o2_high_coefficient / global_route / root。

**已证明：在原 $r=2$ 行，完整高权 supersingular 迹等于
R1037 实际核生成元的 $B$-范数乘一个明确单位。**
这里保留原 Cartier 的 $1/6$、原偶权 Hodge frame、所有细模
超奇异点、实际 oldform 相位和原 Serre 下降度数。特别地
$$
\boxed{\quad S^p=-36\rho\,B(c_0,c_0),\qquad \rho^3=2,\quad\rho\in\mathbf F_p.\quad}
\tag{1041.1}
$$
$S$ 是 R932/R936 的完整 fine supersingular 和，
$c_0$ 是 R1037 的准确归一化核向量，均在下文重述。
结合 R988 已证的原迹/bare 等价，
$$
\boxed{\quad
\overline{c_{p-2}^{+}}\ne0
\iff\overline{c_{p-2}^{-}}\ne0
\iff B(c_0,c_0)\ne0.
\quad}
\tag{1041.2}
$$
本篇不证明右端非零；也不把此范数等同于 R1037 的
$K_{\mathcal Q,p}$ 或任何指定 CM jet 的值。

## 1. 原对象及范数的准确归一化

只取原行
$$
p=12g-1\ge41,\qquad p\equiv2,5\pmod9,\qquad
w=p-1,\quad m=(p-1)/2,\quad d=6g-2.
$$
沿用 R1023/R1028 的实际族
$$
E_b:\ y^2=x^3+3brx+r(1-2b^3),\qquad
r=1-b^3,\qquad \omega=dx/(2y),
$$
$$
h_p=r^{2g}A,\qquad A=bQ_p(b^3)\text{ 单首},\quad
\deg A=d,\quad S_{\rm ss}=\{A=0\}.
\tag{1041.3}
$$
$A$ 的根简单，属于 $\mathbf F_{p^2}$，且避开 $r=0$。
原 Kodaira–Spencer 和平方 Igusa 根为
$$
\operatorname{KS}(\omega^2)=\frac{db}{2r},\qquad
u^m=h_p.
\tag{1041.4}
$$

定义
$$
f=r^{8g-2},\qquad
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b .
$$
R1037 已从该族证明
$$
\mathcal LA=0,\qquad
\mathcal LT_0=A,\quad T_0\in\mathbf F_p[b^3],\quad\deg T_0<d,
\tag{1041.5}
$$
其中第二式有唯一解。其次数为 $d-1=6g-3$，首系数为 $-1$：
$\mathcal L(b^e)=e(e-1)b^{e-2}-(e+3/2)^2b^{e+1}$，
在 $e=d-1$ 时最后一个系数为 $-1$。

实际 $k$-线性 graph 首算子是
$$
\overline{\mathcal Q}(a)
=\operatorname{quo}\bigl(f\,a(b^p),A^2\bigr)\pmod A,
\tag{1041.6}
$$
其中 $a(b^p)$ 保持 $a$ 的系数不变。
令 $c_0$ 为唯一的次数 $<d$ 多项式，使
$$
\frac{f\,c_0(b^p)}{A'}\equiv T_0\pmod A .
\tag{1041.7}
$$
此映射由 $S_{\rm ss}$ 上 Frobenius 置换和单位乘法组成，故可逆。
它在 $\mathbf F_p$ 上定义，所以 $c_0\in\mathbf F_p[b]$；
R1037 证明它生成 $\ker\overline{\mathcal Q}$。
特别地在各根处
$$
c_0(s)^p=\frac{T_0(s)A'(s)}{f(s)}.
\tag{1041.8}
$$

原 Lie 基 $e_s=\theta_sf_s$ 及 R1036 完美对称型满足
$$
q_s=-\frac{f(s)}{A'(s)^2}\in\mathbf F_p^\times,\qquad
B(e_s,e_t)=\frac{q_s}{2}\,\mathbf1_{t=s^p}.
\tag{1041.9}
$$
故本文的范数准确是
$$
B(c_0,c_0)=\frac12\sum_{s\in S_{\rm ss}}
q_s c_0(s)c_0(s^p).
\tag{1041.10}
$$
这是原双线性 $B$；其算术 Frobenius 已包含于 $t=s^p$，
不能再对外部系数任加一次 $p$ 次方。

## 2. 整个原 weight $p-1$ 空间的 $b$-frame

原 $H_6$ 曲线是 $\mathbf P^1_b$，只有一个 cusp $\infty$，
三个 order-three elliptic 点为 $r=0$。在 (1041.3) 的 frame 中，
整个 cusp 空间准确写成
$$
\boxed{\quad
S_{p-1}(H_6,k)
=\{\,r^{2g}T(b)\,\omega^{p-1}:\ T\in k[b],\ \deg T<d\,\}.
\quad}
\tag{1041.11}
$$
这里没有只取正 deck 角色或删除旧角色。

为证明它，先在有限 $r\ne0$ 的点使用 (1041.3) 的好模型；
标量只能正则。在 $r=0$ 的点，取辅助六次参数 $r=t^6$。
以 $x=t^2x_0,y=t^3y_0$ 取得好模型后，$\omega=t^{-1}\omega_0$。
因此标量 $F$ 的正则条件是
$6\operatorname{ord}_rF-w\ge0$，即
$\operatorname{ord}_rF\ge\lceil w/6\rceil=2g$。
原 fine 参数仅满足 $r=v^3$；必要的二次 twist 须同步运输。
因为 $w$ 偶，以上偶权截面下降，在该 fine 参数的阶为
$3\operatorname{ord}_rF-w/2$。所以最低阶是 **1**，
而辅助六次参数中是 **2**，两者不混同。

在 $\infty$，置 $x=b^2x_0,y=b^3y_0$，则
$\omega=b^{-1}\omega_0$；$\omega_0$ 是原半稳定 cusp 的单位 frame。
$b^{-1}$ 是该宽度六 cusp 的参数到一个单位。
因而 cuspidality 准确要求 $\deg F\le w-1$。
除去 $r^{2g}$ 后即 $\deg T\le6g-3=d-1$。
反向这些条件在所有点都保证正则和 cusp 零，证明 (1041.11)。

## 3. 原 Cartier 算子的完整有限点公式

用 R932/R952 的固定规范
$$
\Phi_w(H)=\frac16\operatorname{KS}(H/\mathfrak a^{w-2}),
\qquad \mathfrak a^2=u,\quad\mathfrak a^{p-1}=h_p.
$$
因此 (1041.11) 的截面对应
$$
\Phi_w(r^{2g}T)=\frac{T\,u}{12rA}\,db.
\tag{1041.12}
$$
这里的 $12=6\cdot2$ 同时保留原 Fourier $1/6$ 和
(1041.4) 的 KS 因子。由于
$$
u^p=u\,h_p^2=u\,r^{4g}A^2,
$$
(1041.12) 等于
$$
u^p\,\frac{T\,db}{12r^{4g+1}A^3}.
\tag{1041.13}
$$

逐个根 $s\in S_{\rm ss}$ 展开三阶极部。
记 $\vartheta=4b^2/r$，则
$$
\frac{(r^{-(4g+1)})'}{r^{-(4g+1)}}=\vartheta,\qquad
\frac{A''}{A'}=\vartheta,\qquad
\frac{A'''}{A'}=\vartheta'+\vartheta^2+\frac{9b}{4r}
\quad(A=0).
$$
若 $z=b-s$，则
$A=A'(s)z(1+\vartheta(s)z/2+
(\vartheta'+\vartheta^2+9b/(4r))(s)z^2/6+\cdots)$。
完整展开给
$$
\begin{aligned}
\operatorname{Res}_s
 \frac{T\,db}{12r^{4g+1}A^3}
&=\frac{1}{12r_s^{4g+1}A'(s)^3}
 \left(\frac{T''}2-\frac{\vartheta T'}2-\frac{9bT}{8r}\right)(s)\\
&=\frac{\mathcal LT(s)}
 {24r_s^{4g+2}A'(s)^3}.
\end{aligned}
\tag{1041.14}
$$

Cartier 杀二阶和三阶的局部极部，把简单极部的系数取
$p$ 次根。R952 的实际 holomorphic Cartier 对应保证输出仍在
同一个整个空间 (1041.11)。若输出多项式写为
$\mathscr U_b(T)$，(1041.12)–(1041.14) 因而给
$$
\boxed{\quad
\mathscr U_b(T)(s)^p
=\frac12r_s^{8g-3}A'(s)^{p-3}\mathcal LT(s),
\qquad s\in S_{\rm ss}.
\quad}
\tag{1041.15}
$$
所有根均保留。取值在 $d$ 个简单根上对次数 $<d$ 的多项式
是单射；故即使在 $r=0$ 的 rational expression 还出现极部，
也没有通过删去它们推断输出为零：
$$
\mathscr U_b(T)=0
\iff\mathcal LT\equiv0\pmod A
\iff\mathcal LT=cA .
\tag{1041.16}
$$
最后一步使用 $\deg\mathcal LT\le d$。
(1041.5) 及 R1037 的单射性给其核恰为 $kT_0$。

$r=2$ 的整个 Cartier 核一维亦可从 R955 的已登记低权论证取得；
这里的新内容是原 $b$-frame 中的完整公式 (1041.15)，
以及它同实际 $B$-范数的以下比较。

## 4. 指定原 CM form 的尺度

保持原 named form，而不是另选同 Hecke 系统的向量：
$$
F=V_{p-1}^{\dagger}(Q)
 =F_{p-1}(Q)-2^{p-1}\zeta^2F_{p-1}(Q^4).
\tag{1041.17}
$$
R947/R952 已证其实际 Cartier 为零，其首 Fourier 系数为一。
因此 (1041.16) 迫
$$
F(E_b,\omega)=\xi_p\,r^{2g}T_0(b),\qquad \xi_p\ne0.
\tag{1041.18}
$$

可以从 R936 的原 monic companion 直接求出这个尺度。
置
$$
N=2g-1,\qquad s_0=\sqrt{-3},\qquad
\rho^3=2,\quad c=\rho^2,\quad c^3=4,\qquad \lambda^2=\rho .
$$
$\rho,c$ 是 $\mathbf F_p$ 中唯一相应立方根。
用 R936 的粗坐标 $u_{\rm old}$，原正 cubic transport 为
$b=c\,u_{\rm old}$。其 (ET15) 模型经
$x_b=\lambda^2x_{\rm old},\,y_b=\lambda^3y_{\rm old}$
正好成为 (1041.3)，且
$\omega_b$ 的 pullback 是 $\lambda^{-1}\omega_{\rm old}$；
$\lambda^6=2$。偶权值不依赖 $\lambda$ 的正负。

R936 (ET6)、(ET17) 的原单首 $P_N$ 因而给
$$
F(E_b,\omega)
=-\lambda^w r^{2g}\,12s_0(6s_0)^N
 P_N\bigl(24s_0(1-2b^3)\bigr).
\tag{1041.19}
$$
负号是 $(-1)^N=-1$，没有重选 $\eta^{12}$ 的 Tate 相位。
除去 $r^{2g}$，首项准确为
$-\lambda^w12s_0\,864^N b^{3N}$。
与 $T_0$ 的首系数 $-1$ 比较得到
$$
\xi_p=\lambda^w12s_0\,864^N
     =\rho^m12s_0\,864^N.
\tag{1041.20}
$$

$\rho^m\in\{\pm1\}$，而 $s_0^p=-s_0$，所以
$$
\xi_p^{p+1}=432\cdot864^{2N}\in\mathbf F_p^\times.
$$
又 $6N=p-5$，故这个数的立方为
$$
432^3\,864^{p-5}=\frac1{6912}
 =\left(\frac{c^2}{48}\right)^3 .
$$
$p\equiv2\bmod3$ 使立方在 $\mathbf F_p$ 上为双射，因此
$$
\boxed{\quad \xi_p^{p+1}=\frac{c^2}{48}=\frac{\rho}{24}.\quad}
\tag{1041.21}
$$
若将原 Frobenius 侧的同一标记写成共轭表达，尺度成为
$\xi_p^p$，(1041.21) 不变；这不是任意删掉标记相位。

## 5. 完整高 diagonal 等于实际核范数

在 $S_{\rm ss}$ 的好 frame，原 Hasse derivative 的连接项
被 $h_p=0$ 杀掉。由 (1041.4) 得准确值
$$
\mathcal B=2r\,h_p'=2r^{2g+1}A'.
\tag{1041.22}
$$
于是原高 weight $w=p-1$ 的 modular function 在每个根的值是
$$
\frac{F(s)^{p+1}}{\mathcal B(s)^{p-1}}
=\xi_p^{p+1}
 \frac{T_0(s)^{p+1}}{f(s)A'(s)^{p-1}}.
\tag{1041.23}
$$
此处 $2^{p-1}=1$，$r$ 的指数是
$2g(p+1)-(2g+1)(p-1)=-(8g-2)$。

(1041.9) 的 $q_s\in\mathbf F_p$ 给
$$
f(s)^p=f(s)A'(s)^{2p-2}.
$$
再用 (1041.8) 及其 $p$ 次方，逐点得到
$$
q_s c_0(s)c_0(s^p)
=-\frac{T_0(s)^{p+1}}{f(s)A'(s)^{p-1}} .
\tag{1041.24}
$$
因此完整粗根集的和为
$$
\sum_{s\in S_{\rm ss}}
 \frac{F(s)^{p+1}}{\mathcal B(s)^{p-1}}
=-2\xi_p^{p+1}B(c_0,c_0).
\tag{1041.25}
$$

原标准/exotic 两侧满足 $a=b^p$。这里原 weight-zero 函数定义于
$\mathbf F_p$：$\xi_p^{p+1}\in\mathbf F_p$，而 $r,A,T_0$
及原 Hasse derivative 都在同一个 $\mathbf F_p$ 标架中定义。
在完整超奇异根集上 Frobenius 是双射；以上使用的是
frame-独立的这个原函数的全和。因此从 $a$ 侧到 $b$ 侧只是这个实际双射的重标，
不是以一个同 character 的函数替换原 form。

仍须加回细模曲线上的全部点。R936 §4 已精确计算
$X(6)\to X'(6)$ 的有效度数为 $12$。
每个 $A=0$ 的点上方有十二个不分歧点。
三个 $r=0$ 的 elliptic 点上方各有四点，分歧指数为三；
它们全都 supersingular。第2节证明 $F$ 在每个这类 fine 点
至少有一阶零，$\mathcal B$ 在好 Hodge frame 为单位。
所以这些 $3\cdot4$ 个点仍在完整和中，贡献准确为零。
fine Igusa cover 在每个 SS 点上只有一个全分歧点，
故没有额外乘 $p-1$。得到
$$
\sum_{P\in\operatorname{SS}(\widetilde C_1)}
 \frac{F_P^{p+1}}{\mathcal B_P^{p-1}}
=-24\xi_p^{p+1}B(c_0,c_0).
\tag{1041.26}
$$

R932/R936 的完整和是
$$
S=\sum_{P\in\operatorname{SS}(\widetilde C_1)}
       \frac{g_P^{1+1/p}}{\mathcal B_P^2},\qquad
g_P=-6\mathcal B_PF_P .
$$
R936 (ET12) 因而给
$$
S^p=36\sum_P\frac{F_P^{p+1}}{\mathcal B_P^{p-1}}
=-864\xi_p^{p+1}B(c_0,c_0)
=-36\rho B(c_0,c_0),
$$
证明 (1041.1)。

## 6. 原 bare 等价、保留的下降度数与剩余问题

R932 的原功能值仍是
$$
\lambda_h\bigl(\Phi_{p-1}(F)_{\rm full}\bigr)
=\frac{m_{\rm I}(c_h^{\rm F})^{1/p}}{d_1\,6^2}\,S .
\tag{1041.27}
$$
$r=2$ 行 $m_{\rm I}=1$；$d_1$ 是原完整 fine Igusa cover 的度数，
并不因此等于上一节粗 tame cover 的 $12$。
原 $c_h^{\rm F}$、$d_1$ 和全部 norm transport 均未改动。
(1041.27) 外因子全为非零，故保留原非零判据。

R978 的原 Robert 坐标比较和 R988 (988.22)–(988.23)
已证明这同一个原完整迹非零，当且仅当
$\overline{c_{p-2}^+}\ne0$，亦当且仅当
$\overline{c_{p-2}^-}\ne0$；其 $\eta$、$\chi(\sigma)-1$、
$\beta$ 与阶乘都是原单位。结合 (1041.1) 得 (1041.2)，
没有除去一个未经证明为单位的 CM period。

若需只以多项式读取同一范数，(1041.8) 及单首 $A$ 的
Lagrange 部分分式还给
$$
B(c_0,c_0)
=-\frac12[b^{d-1}]\bigl(c_0T_0\bmod A\bigr).
\tag{1041.28}
$$
这里仍是完整剩余类，不能删去其低项。

待证问题仍为这个指定自配对不为零。
核一维、$B$ 完美、R1037 的 $B(c_0,J)=-1/8$，
均不能推出 $B(c_0,c_0)\ne0$。
即使后者成立，也不自动确定
$K_{\mathcal Q,p}=B((1-\overline{\mathcal Q})\lambda,
                   \overline{\mathcal Q}DJ)$，
更不删除其完整 $\overline{\mathcal Q}^2\lambda$ 项。
本篇只接通原 $r=2$ bare 标量；没有声称 $r=8$ 同一结论，
没有解决原指定 CM jet 或整个 Serre 一致性。

## 来源与计算范围

- [R932](R932-original-Igusa-Frobenius-line-and-supersingular-residue-pairing.md)，(932.7)、(932.31)、(932.37a)：原 $1/6$、完整细模和与所有下降因子。
- [R936](R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md)，(ET6)、(ET12)、(ET15)–(ET18) 及 §4：原 oldform 标架、正确 Tate 符号、全部 SS 点和实际度数。
- [R952](R952-exact-Cartier-formula-for-the-last-Hasse-obstruction.md)，(952.12)–(952.13)：原 whole-space Cartier 对应。
- [R955](R955-original-Cartier-nilpotent-packet-is-a-single-odd-chain.md)：原 CM 向量、实际 Cartier 核和未解决的长奇链。
- [R978](R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md) 与 [R988](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：同一个原 high trace 与 bare 系数的完整单位等价。
- [R1028](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md)：原 $E_b$、Hasse 根及 KS 标架。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)：原 $B$、$q_s\in\mathbf F_p$ 及算术下降。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：实际 $\overline{\mathcal Q}$、唯一 $T_0$、核及系数固定规范。

所有新恒等式来自上述原模型的纸面代数、局部留数和完整全和。
没有数学程序执行，没有重复有限窗口；工具仅传输本文小文本。
