# R119 续篇：尾标签与长段联合消元的完整空间及1850角宽费用

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇给实际原点 Schur 行从内端完整两迹残差回到
真实内部尾标签的统一全频界，明确支付1850的角宽差。它与已证真实
nonlinear outer forcing 接合后，给一个可实际消费的 $\ell^1_{128}$
标签列。这个较弱权列不属于已安装全 nonlinear chart 的
$\ell^1_{8192}$ 同一闭球，因此没有将它说成完整非线性逆。

## 1. 三个空间及准确 Schur 行

实际内部标签仍在 R115 (115.2)–(115.3) 的层 $b_m$ 上定义，
$$
 \|a\|_{\ell^1_\beta}=\sum_{m\in4\mathbb Z\setminus\{0\}}
 e^{\beta|m|}|a_m|.
 \tag{Q.1}
$$
在真正 $u=B$，正参考高度的完整相对两迹是
$$
 f_B=v_\perp/(a_Bw_B),\qquad k_B=(v_a)_\perp/w_B.
$$
记 $M=|m|$，两迹强 norm 和残差强 norm 为
$$
 \|(f,k)\|_{\mathfrak C_\sigma}
 =\sum_{m\ne0}e^{\sigma M}M^2
       (|f_m|^2+|k_m/M|^2)^{1/2},\qquad
 \|g\|_{\mathfrak Z_\sigma}
 =\sum_{m\ne0}e^{\sigma M}M|g_m|.
 \tag{Q.2}
$$
长段用 R119 的实际 $\mathcal Y_\sigma$ 或变化角宽的 $\mathcal Y_{W_0}$；
它包含径向二 jet 与完整角频率，不将两个端点 norm 当作内部强 norm。
mean 高度、mean flux/holonomy 负荷及平盘平移 $\lambda$ 都另列。

在原点，实际联合 Schur 行是
$$
 \mathsf D_0 a:=k_B^{lin}(a)+\mathsf C_L f_B^{lin}(a),
 \quad (\mathsf C_L f)_m=M\coth(ML)f_m,
 \quad L=\omega B.
 \tag{Q.3}
$$
双 bump 续篇 (B.17) 已逐频证明，对于 $g=\mathsf D_0a$，
$$
 (|f_m|^2+|k_m/M|^2)^{1/2}
 \le2^{40}|g_m|/M.
 \tag{Q.4}
$$
它包含高度为0的模，没有除以一个未知高度分量。

## 2. 从同一真实两迹回到 $u=B$ 的物理状态

令 $Y=(y,y_u/M)$，沿用真实 R74 (74.14) 的北帽高度和同一实际半径。
本篇的正参考高度是其相反数，故
$$
 \binom f{k/M}
 =-16\omega h(B)^2\,
 \mathsf J_M Y,
 \qquad
 \mathsf J_M=\begin{pmatrix}\omega&-1/M\\\omega/M&-1\end{pmatrix}.
 \tag{Q.5}
$$
其逆的无穷 norm 满足
$$
 \|\mathsf J_M^{-1}\|_\infty
 \le\max\left\{\frac1{\omega(1-1/M)},\frac1{1-1/M}\right\}
 \le4/3.
$$
由 $\omega>7/5$，$\|(f,k/M)\|_\infty\le|(f,k/M)|_2$，得到
$$
 h(B)^2\|Y\|_\infty
 \le\frac5{84}|(f,k/M)|_2
 <\frac1{16}|(f,k/M)|_2
 \le2^{36}|g_m|/M.
 \tag{Q.6}
$$
极小半径 $a_B$ 在这里准确抵消，不能单独丢掉其逆幂。

## 3. 消费实际双 bump、connector 和真内部标签权

R74 §5 的同一真实流给：双 bump 在 $u$ 的总长度
$L_u=25/8$ 上的状态费用至多 $e^{4ML_u}$；完整 connector 费用
至多 $e^{1143M}$。在 $u=T$ 从 $y_u/M$ 换到 $y_{\log h}/M$ 只乘
$1/\omega<1$。R74 (74.32) 的真 cut128 转换是
$$
 \zeta_{128}^{-1}\|V_{m,128}^{ref}\|_\infty
 \le16\delta_{tail}^{-15/4}
       \frac{H^2\omega_e^2}{b_{tail}^{10}}M^4\|Z_m\|_\infty.
 \tag{Q.7}
$$
使用同一几何门
$H^2\omega_e^2<8\Omega^3h(T)^2$、$\Omega=2^{360}$、
$h(T)^2/h(B)^2\le e^{3L_u}$、$b_{tail}>1$，并消费 R15 新已证的
真实 raw 标签费用 $e^{404M}$，代入 (Q.6) 得
$$
 |a_m|
 \le2^{1618}M^4
     e^{(3119/2)M+75/8}\,|g_m|/M.
 \tag{Q.8}
$$
常数来自 $7+495+1080+36=1618$：
$\delta_{tail}=(2/25)2^{-128}>2^{-132}$，故
$\delta_{tail}^{-15/4}<2^{495}$。
频率线性项是 $1143+4(25/8)+404=3119/2$。

以下门覆盖全部 $M\ge4$，不是有限模式测试。由 $\log2<7/10$ 和
$\log M/M$ 在 $M\ge4$ 单调递减，
$$
 \frac{1618\log2+4\log M+75/8}{M}
 <\frac{1618(7/10)}4+\frac75+\frac{75}{32}.
$$
准确有理和为
$$
 \frac{3119}{2}+\frac{5663}{20}+\frac75+\frac{75}{32}
 =\frac{295423}{160}<1850.
$$
因此
$$
 \boxed{\quad |a_m|\le e^{1850M}|g_m|/M.\quad}              \tag{Q.9}
$$
全部内部层和全部真实流都保留；无 mean 量被乘非零模指数。

## 4. 原点强逆的准确范围与一条真实非线性输入列

对任意 $\beta\ge0$，逐频求和 (Q.9) 给
$$
 \boxed{\quad
 \|\mathsf D_0^{-1}g\|_{\ell^1_\beta}
 \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}}.
 \quad}                                                     \tag{Q.10}
$$
这里是明确的角宽损失1850。若要输出进入现有整个 nonlinear chart
的 $\ell^1_{8192}$ 域，输入残差必须在 $\mathfrak Z_{10042}$ 上控制；
不能只用已给的 $\mathfrak Z_{\tau+1968}$。

另一方面，R119 nonlinear screening 的真实结论是
$$
 \|\mathcal F(a,f)-\mathcal F(a,g)\|_{\mathfrak Z_{\tau+1968}}
 <17e^{-L/2}\|f-g\|_{\sigma_o,2},\qquad\sigma_o=1/512.
$$
因 $128+1850=1978<\tau+1968$，它与 (Q.10) **确实**接合，给
$$
 \boxed{\quad
 \|\mathsf D_0^{-1}[\mathcal F(a,f)-\mathcal F(a,g)]\|_{\ell^1_{128}}
 <2e^{-L/2}\|f-g\|_{\sigma_o,2}.
 \quad}                                                     \tag{Q.11}
$$
这是实际 nonlinear outer forcing 的基态预条件列，包含所有输入和
输出高频。它的标签权为128，不是8192；本篇不以 (Q.11) 冒充一个
在已许 nonlinear 标签球内闭合的 Newton map。

## 5. 普通源与 mean 在联合消元中的位置

为明确源合同，若实际非mean长段 Jacobi 源为 $e$，完整 Dirichlet
Green 给真实内端 Neumann particular $q_D=(\mathcal G_De)_t(0)$。
若尾侧另有已经构造、单位匹配的真实 particular 两迹 $(f^p,k^p)$，
原点标签方程准确为
$$
 \mathsf D_0 a
 =\mathsf S_L f_*+q_D-(k^p+\mathsf C_L f^p),
 \qquad (\mathsf S_L f)_m=M e^{2L}\operatorname{csch}(ML)f_m.
 \tag{Q.12}
$$
若还有外部界面负荷，按其真实符号加入同一右端。
这个公式不宣称任意尾源已经完成 connector 传播；对应 particular
必须使用真正的连续源 realization 和足够角宽，不能直接置成0。

mean 不通过 (Q.10) 处理。更新后 scalar Darboux 源的准确独立行已由
上一续篇证明为
$$
 (\delta M/w^2)_t=-2\delta M/w^2+\langle\rho J e\rangle,
 \qquad
 \delta K_0=D K_0(h)[\xi]+\langle\rho J\rangle^{-1}\delta M/w^2.
 \tag{Q.13}
$$
实际尾给初始 holonomy 负荷和 mean 高度；另保留平盘平移 $\lambda$。
平均高度的另一端及 mean 通量均是积分输出，必须与主体的增广行接合。
grounded density source 使用真 normal/shear 转换；本篇没有删除其源端点项。

## 6. 与实际更新后 Schur 行的关系

更新后长段的真相对误差已证明小于 $2^{-8390}$，所以
$$
 D_a\mathcal F=DT_k+\mathsf C_LDT_f-\mathcal R_BDT_f,
 \quad\|\mathcal R_B\|_{\sigma_i,2\to\sigma_i,1}<2^{-8390}.
$$
尚缺的是同一空间中对真实混合尾 $DT_k+\mathsf C_LDT_f$ 的相对逆。
已有 actual angle/density 共轭将该问题精确化到真实
$\nu,a_k,q_k$ 框架，但未支付其全 return。角宽损失 (Q.10) 和
域差 (Q.11) 说明为何绝对 $D^2X$ 小量及巨大 $e^{-L/2}$ 不能单独
完成所需的闭合。这是空间合同的明确结论，不是把未付门隐藏在一个
“存在常数”的假设中。

[准确有理程序](../scripts/fourfold_joint_tail_schur_weights_20261113.py) 与
[报告](../notes/2026-11-13-R119-joint-tail-schur-weights-budget.json)
核真实两迹换算、全部标签费用和 nonlinear 列的实际宽度接合。
