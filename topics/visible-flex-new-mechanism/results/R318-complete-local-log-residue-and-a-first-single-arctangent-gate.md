# R318：二次高度端芽的完整 local residue、全角对数门与首个单字门

日期：2026-11-15。**完整纸面推导与有限频率存在性证明；没有运行求积、符号程序、人工测试或研究计算。**

本稿接 [R312](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md) 与 [R315](R315-full-angle-arctangent-square-gates-and-ordered-history-cancellation.md)。R315 已支付完整反正切平方门，并将 log 的有序 history 部分准确化为已清的原交换子。但这不删除 local-third 和 chain。

下面从 R56/R73 原式计算其剩余 residue。结论是一个完整三次算子 $\kappa^2\mathcal L$。它有真实右积分和可能的二次左尾，但不同微包的内外槽作用准确为零；其三个自矩是有限平移次数的 $C^2$ 观测。因而从起点增加明确的27条低阶观测后，可以在同一个实际有限频率圆上清掉**整个 log 系数**，同时保留 R315 已付门。

单反正切系数另有七个原有理幂。本稿将其最高 $h^2$ 行化为准确 mixed 能量，并用第五个真实交替微包同时支付该行。其余六幂与纯有理余式仍不宣称为零。

来源：[R56 完整分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 原八矩与 chain](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R221 完整局部配对](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R259 原 self/tail](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R291 原 $p_2$ 三次恒等](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、[R293 初选有限纤维](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、[R296 原局部主恒等](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)以及 R312/R315。

## 1. 固定原式与 residue 的含义

沿 R312 同一个从设计起点安装的真实端芽，在共同平移后的 profile 坐标中，
$$
h=h_e(1+\varepsilon\sigma^2),\quad
k=\kappa\ne0,\quad \omega=0,\quad
e_{\rm g}=hx-\kappa,\quad
Q_{\rm g}=1+e_{\rm g}^2,\quad K=1+\kappa^2.
$$
置
$$
\gamma=h_\sigma=2h_e\varepsilon\sigma,\qquad
\gamma^2=4h_e\varepsilon(h-h_e),\qquad
\gamma_\sigma=2h_e\varepsilon.
\tag{1}
$$
$x$ 始终是原 profile 坐标，不把移动 $s$ 导数换成固定 physical $u$ 导数。

令 $\mathscr C_\sigma(f;D)=\ell_\sigma(f;D)-\Psi_\sigma(f,\mathsf M D)$，其中 $\ell$ 对整个原局部二阶场求导，$\Psi$ 是 R73 的变化 profile chain。R315 的剩余对数算子是
$$
\boxed{\mathscr D_{\rm loc}(f;D)
=\operatorname{Res}_{h=0}\{\mathscr C_\sigma(f;D)/\gamma\}.}
\tag{2}
$$
$\mathscr C_\sigma$ 奇，故 $\sigma=0$ 的商可去；(1)使该商为 h 的有理算子。这个 residue 是原 $\log(h/h_e)$ 的系数，不是对实际路径作复延长，也不是任意新的三阶初值。

采用原 E8 名称 $R=\Phi_{r_1},P_1=\Phi_{p_1},T=\Phi_{t_1},V=\Phi_{p_2}$。对 $D=b\odot c$ 定义并线性延拓
$$
\Omega_D=(b'-xb'')(c'-xc''),\quad
\tau=T(D),\quad \xi=P_1(D),\quad \nu=V(D),
$$
$$
b_D=\frac{\tau'-2\tau/x}{16}.
\tag{3}
$$
$\tau/x=xb'c'+J_2^*(b,c)$ 是原 polynomial/primitive 表达；(3)没有添加隐藏的 $x=0$ 奇点。物理 I 仍在正坐标支上。

对外槽 f 另记
$$
A_f=f-xf'/2,\quad W_f=f'-xf'',\quad
C_f=f-xf'+x^2f''/2.
\tag{4}
$$

## 2. 完整 residue 的准确公式

**命题。** 对任意原同 collar profiles 和对称内槽 D，
$$
\boxed{\mathscr D_{\rm loc}(f;D)=\kappa^2\mathcal L(f;D),}
\tag{5}
$$
其中
$$
\boxed{
\begin{aligned}
\mathcal L(f;D)={}&
\frac{x^2C_f\Omega_D}{16}-xC_fb_D
+\frac{x^2}{32}J(x^2f'''\Omega_D)
-\frac{x^2}{2}J(xf'''b_D)\\
&-\frac{f'\nu}{8}+\frac{xf'\nu'}8
+\frac x8J(xf''\nu'')\\
&+\frac{x^2f'\xi'}8
+\frac x8J(x^2f''\xi''+2f'\xi').
\end{aligned}}
\tag{6}
$$
所有 J 都是同一个真实右锚，式中的 $\tau,\xi,\nu$ 可以有左尾。结论与 $\varepsilon,h_e$ 无关是原 residue 抵消的结果，不能预先删掉其速度项来猜得。

### 2.1 二阶局部场的完整 Laurent 分层

R221(14)直接给
$$
\frac{\eta_D}{\gamma}
=\frac{K(RD)'}{16h^2}
+\frac{\kappa\Omega_D}{8h}+b_D.
\tag{7}
$$
因此其分子准确为
$$
V_{K_D}=(\gamma F_D,N_D,e_{\rm g}\gamma F_D),
$$
$$
F_D=\frac{K(RD)'}{16h^3}
+\frac{\kappa\Omega_D}{8h^2}+\frac{b_D}{h},
\qquad N_D=N_{-1}/h+N_0+hN_1.
\tag{8}
$$
$N_D=xP_D+B_D$ 仍为原 normal 分子，三个系数都是实际 profile 表达。它的三个 h 次数由 R221(13)直接读取，不要求单包三矩为零。

对 forcing $H(Y_f,K_D)$ 写
$P_C=\gamma\overline P,\ B_C=\gamma\overline B$。
由原 $V_f=(-f'/2,0,hA_f+\kappa f'/2)$ 及(8)，
$\overline P,\overline B$ 的最高 h 次数均为0。令
$q_D=\kappa\Omega_D/8$，准确的四个所需系数是
$$
\begin{aligned}
\overline P_0&=-xW_fb_D/4+\tfrac14J(x^2f'''b_D),\\
\overline P_{-1}&=-xW_fq_D/4
-\tfrac\kappa2(xf''-f'/2)b_D
+\tfrac14J(x^2f'''q_D)
-\tfrac\kappa2J(xf'''b_D),\\
\overline B_0&=xA_fb_D/2,\\
\overline B_{-1}&=xA_fq_D/2+\kappa(xf'-f)b_D/2.
\end{aligned}
\tag{9}
$$
例如(9)中的 J 项由原 $P_C=(2h)^{-1}J(V_f'\cdot V_{K_D}')$ 一次真实 IBP 得到；右端为零，左值没有改写。

### 2.2 哪些原速度项确实没有 residue

使用原联络
$\nabla_s(a,n,b)=(a_s-\kappa n,n_s+\kappa a+b,b_s-n)$，
完整 $T_{s,C}$ 为
$$
\gamma A_f\{h(N_D)_h-N_D
+(h^2+\gamma^2)xF_D
+e_{\rm g}\gamma_\sigma F_D
+e_{\rm g}\gamma^2(F_D)_h\}.
$$
将它和(9)代 R56(5)，先保全部速度项。在除以 $\gamma$ 后：
- $(h(N_D)_h-N_D)/(2h^2)$ 只有 $h^{-3},h^{-2}$；
- 含 $\gamma^2$ 或 $\gamma_\sigma$ 的三个 $F_D$ 项最高次数为 $h^{-2}$；
- 原 $-\lambda(P_C)_s-\gamma(B_C)_s/h^2$ 由 $\overline P,\overline B$ 最高次数0，亦没有 $h^{-1}$ 项。

最后一项使用 $\partial_s=\gamma\partial_h$ 和(1)，不是删除 $\sigma$ 总导数。故
$$
\operatorname{Res}_{h=0}\frac{\ell_\sigma}{\gamma}
=\frac{xA_fb_D}{2}
+\kappa x^2\overline P_{-1}-Kx\overline P_0
+\kappa x\overline B_{-1}-K\overline B_0.
\tag{10}
$$

### 2.3 原 chain 必须同时保留

R73(15)在 $\omega=0$ 为
$$
\Psi_\sigma(f,w)/\gamma
=-\frac{\kappa}{4h^2}f'w
-\frac{Q_{\rm g}}{8h^3}f'w'
-\frac{x}{8h^3}J_e(f,w).
$$
原瞬时矩阵的非负 h 部分是
$$
\mathsf M_0=\kappa^2P_1-KT/8,\qquad
\mathsf M_1=-\kappa V/2.
$$
因此其完整 residue 为
$$
\begin{aligned}
\operatorname{Res}_{h=0}\frac{\Psi_\sigma(f,\mathsf MD)}{\gamma}
={}&\frac K{64}\{x^2f'\tau'+xJ_2^*(f,\tau)\}\\
&+\frac{\kappa^2}{8}
\{f'\nu-xf'\nu'-xJ_1(f,\nu)
-x^2f'\xi'-xJ_2^*(f,\xi)\}.
\end{aligned}
\tag{11}
$$

(10)中的 K 部分恰为
$$
K\{x^2W_fb_D/4-xJ(x^2f'''b_D)/4\}.
$$
将(3)代入，它与(11)第一行严格相等。所用原恒等为
$$
(x^2f''\tau'+2W_f\tau)'
=x^2f'''\tau'+x^2f''\tau''
-2xf'''\tau+2f'\tau'.
\tag{12}
$$
共同右端的乘积零使 $J(D_xF)=-F$；不要求 $\tau$ 的左尾零。余下 $\kappa^2$ 部分正是(6)，证明(5)。

## 3. 不交微包：全 cross 算子为零，不是假设 primitive 局域

设 outer $f_i$ 在 inner $D_j=u_j^2$ 的左侧。原八表在整个 outer 支撑上给
$$
\Omega_{D_j}=0,\quad b_{D_j}=-m_{2,j}/16,\quad
\tau=m_{2,j}x,\quad
\xi=-m_{1,j}x^2/4,\quad
\nu=-m_{2,j}x^2/4.
\tag{13}
$$
全部带 outer 导数的 J 密度也只在这个真实区域取值。

(6)首行按 $J(xf_i''')=-xf_i''+f_i'$ 化为
$$
m_{2,j}(xf_i/16-x^2f_i'/32).
$$
其中三个 $\nu$ 项准确为相反数。最后两个 $\xi$ 项为
$T(f_i,-m_{1,j}x^2/4)/8=0$，使用原 sl2 表中 $T(f,Ax^2)=0$。
所以
$$
\boxed{\mathcal L(f_i;u_j^2)\equiv0\quad(i\ne j).}
\tag{14}
$$
若 inner 在左侧，则它在 outer 支撑和其右方已为真实零尾，(14)直接成立。以上是全原函数身份，不只在 outer 区间取零。

单包 self $\mathcal L(u_i;u_i^2)$ 的右尾零，左尾由(6)明确至多二次。原三个 $I_j$ 都与另一不交紧 profile 正交，因为
$I_j(v,p)=0$ 对任意二次 p 和紧 v 成立；$I_2$ 的 $2v'p'$ 必须保留才有这个准确零。因此
$$
\boxed{
I_j\{\phi_\theta,\mathscr D_{\rm loc}(\phi_\theta;D_\theta)\}
=\kappa^2\sum_i c_i(\theta)^2d_i(\theta)S_j(u_i),
}
\tag{15}
$$
$$
S_j(u)=I_j\{u,\mathcal L(u;u^2)\},\qquad
c_i=a_i\cos\theta+b_i\sin\theta,\quad d_i=a_i^2-c_i^2.
$$
这一步没有把 self 第三尾本身称为紧支撑。

## 4. S_j 的真实 C² 性与有限平移系数

R296(22)从 R56/R73 原系数逐项证明的恒等为
$$
(\mathscr C_\sigma(u;u^2))_r^{\rm loc}
=(\beta_{\rm g}^2)_\sigma,\qquad
r=u'',\quad
\beta_{\rm g}=\frac{Q_{\rm g}\gamma(u'-xu'')}{8h^3}.
\tag{16}
$$
这里的 local-r 导数采用该原稿明确的真 J 降阶表达；所有 primitive 变量独立保留。该恒等的证明只用原逐点系数，不用 Gaussian 微分方程，所以适用于(1)。

除以 $\gamma$ 后，对 h 取 residue。由于
$$
\beta_{\rm g}^2
=\frac{h_e\varepsilon(h-h_e)Q_{\rm g}^2(u'-xu'')^2}{16h^6}
$$
是 h 的有理式，而有理函数导数的 residue 为零，得到
$$
\boxed{(\mathscr D_{\rm loc}(u;u^2))_r^{\rm loc}=0.}
\tag{17}
$$
profile 微分与有限系数抽取可交换；这里没有把未知 residue 设为某个自由常数。

原(6)经同一真 J 降阶后，只含 $u,u'$ 和有限个 $C^2$ primitive。再对其求两个 x 导数，三阶导至多线性出现，且其系数是低阶 jet 与原 primitives 的多项式。对 r 取多项式原函数作一次 IBP，primitive 的导数仍为 $C^2$ 密度，边界因 r=0 消失。由此外矩(15)是连续四次 polynomial/$C^2$ 泛函。I2 的额外一阶导配对亦在此类中。

从(6)逐项看，同步平移的 $\mathcal L$ 次数至多6；原 $I_j$ 再至多加2。所以
$$
S_j(u(\cdot-\tau))\quad\text{为 }\tau\text{ 的次数至多8的真实多项式}.
\tag{18}
$$
其中所有右锚均留在共同零 collar。用九个固定合法小平移插值读系数，也只需要 $C^2$ 数据，不要求多八阶导数。

## 5. 新的初选低阶纤维确实支付整个 log

从构造之初将 R315 的 $\mathcal F_{\rm new}$ 明确扩大为
$$
\boxed{
\mathcal F_{\log}
=\left(\mathcal F_{\rm new},\
[\tau^k]S_j(u(\cdot-\tau)):
j=0,1,2,\ 0\le k\le8\right).
}
\tag{19}
$$
这是27个额外所列标量，不称其实际秩为27；也不称它们原本已包含在旧 F 中。

在每个等背景实际布局内，$b_i^2=B_0$，
$R_i=a_i^2-b_i^2\in\{-B_0/2,8B_0\}$，并有
$$
\sum_iR_it_i^k=0\ (k\le10),\qquad
R_i^2-4a_i^2b_i^2=\tfrac{7B_0}{2}R_i.
$$
纤维使每个 $S_j(u_i)$ 恰等于原母包在该位置的值。因此(15)的两个 even 角系数分别为
$$
B_0\sum_iR_iS_j(u_i)=0,\qquad
\tfrac{9B_0}{2}\sum_iR_iS_j(u_i)=0.
$$
odd 系数由原十二完整副本消去，(18)保证所需次数。全部副本和最终正幅混合均按原共享实际包执行。因此
$$
I_j\{\phi_\theta,\mathscr D_{\rm loc}(\phi_\theta;D_\theta)\}=0
\quad\text{对全部 }\theta.
\tag{20}
$$

R315 的有序部分 $\mathscr D_{\rm hist}$ 是原 E8 交换子组合，仍由(19)的旧部分清掉。故在同一新构造上，
$$
\boxed{I_j\{\phi_\theta,\mathscr D(\phi_\theta;D_\theta)\}=0
\quad(j=0,1,2),}
\tag{21}
$$
即**整个 log 系数**为零。

R315 的三个平方 principal 仍有次数6、7、8与非零共同首系数；从起点加有限 $C^2$ 观测不改变这一事实。对(19)重新选真最大秩母包与纠正方向，原四包正锥和有限 N IFT 因而仍同时支付整角 E²。这是从起点选择的同一个新圆，不是把已产生圆的任意新低阶数据当作可自由指定。

## 6. 单 E 的七个原幂及最高行

此处保留 R315 的 $\mathsf Q=\sigma\mathsf A(h)$，
$\mathsf A=\sum_{p=-3}^1A_ph^p$，五个 $A_p$ 仍为该稿原(28)。
令
$$
\mathcal T_h^\#=\mathcal T_\sigma/\gamma,\qquad
H_{X,j}(\theta)=-I_j(XD,BD)+2I_j\{\phi,X(\phi,BD)\}.
\tag{22}
$$
原 R221 完整局部式直接给
$$
\begin{aligned}
\mathcal T_h^\#(c;a,b)=\frac1{32h^4}\int\Big[
&Q_{\rm g}^2c'''(a'b''+a''b'-xa''b'')
-2he_{\rm g}Q_{\rm g}c'''a'b'\\
&+(Q_{\rm g}c''-2he_{\rm g}c'+2h^2c)
\{(Q_{\rm g}-2he_{\rm g}x)a''b''-2h^2a'b'\}\Big].
\end{aligned}
\tag{23}
$$
这是原 right-tail 转置后的全式；不能只保第一项。其 h 次数为 $-4,\ldots,0$。

由 R312 的完整单 E 系数，
$$
\boxed{
\begin{aligned}
\frac{\mathscr R_E}{2\sigma}
={}&2h_e\varepsilon
\{\mathcal T_h^\#(BD;D)-2\mathcal T_h^\#(\phi;\phi,BD)\}\\
&+\sum_{p=-3}^{1}\left\{
\frac K4h^{p-1}H_{A_p,0}
-\frac\kappa2h^pH_{A_p,1}
+\frac14h^{p+1}H_{A_p,2}\right\}.
\end{aligned}}
\tag{24}
$$
因此它准确是 h 的七幂 Laurent 式 $h^{-4},\ldots,h^2$；不是只看有限 Taylor 近似。

最高行只有 $A_1=-\kappa V/6$ 的贡献：
$$
[h^2]\frac{\mathscr R_E}{2\sigma}
=-\frac\kappa{24}H_{V,2}(\theta).
\tag{25}
$$
R291 的原恒等 $I_2(u,V(u,u))\equiv0$ 及真紧方向 $BD$ 给
$$
2I_2\{\phi,V(\phi,BD)\}=-I_2(BD,V\phi^2).
$$
所以
$$
\boxed{H_{V,2}(\theta)=-I_2(BD_\theta,Vf^2).}
\tag{26}
$$
$Vf^2$ 可以有真实左尾；另一槽 $BD_\theta$ 因原三矩真紧，变分与配对合法。(26)保整个源 f，不偷换为当前 $\phi$。

这是一条新的 mixed 能量门。它不能由 B² 三门简单线性推出。其全角只含 $\sin^2\theta$ 与 $\sin\theta\cos\theta$；后一项由原完整十二复制消去，所用真实平移次数仍至多10。

## 7. 第五个实际包可同付这条真实新行

对(26)仍用原完整主项，而不删 C² 基线：
$$
H_{V,2}(\pi/2)
\equiv_2 \sum_i(-a_i^2R_i)
\int x^2\alpha_V\alpha_B(u_i''')^2.
$$
原
$$
\alpha_V=x^2u-x^3u'+x^4u''/2
$$
与 R315 的 $\alpha_B$ 使该位置多项式的次数准确为9，首系数
$$
A_+=-t\Big(\sum_cw_c\Big)\int(u_0'')^2\chi^2>0,
\quad t=-\varepsilon/4.
\tag{27}
$$
全部真实 copy 权已包含；不是单个未包装母包的形式次数。

于是四个主位置多项式的次数是 $6,7,8,9$，首系数为
$A,A,A,A_+$。共同大正 C 下四点 evaluation minor 的首项为
$$
A^3A_+C^{24}\prod_{i<k}(\xi_k-\xi_i)>0.
\tag{28}
$$
对应 Wronskian 系数12，正好被 $0!1!2!3!$ 除去。

取真实交替索引 $0,1,33,34,49$，其
$\lambda_i=-a_i^2R_i$ 号为 $-,+,-,+,-$。四阶 minors 同正给五列严格正核与整个 $\mathbb R^4$ 正锥。按 R315 同一有限频率证明，只将四个目标换为
$$
(q_0,q_1,q_2,H_{V,2})(\pi/2),
$$
在固定有限正幅盒上保全部实际基线与 $C^1$ 极限。选四个独立幅度，固定第五个，足够大的有限 N 给准确四零。

整个过程中保持(19)，故(21)、原三矩、完整第三与全部 E8 面积均不动。由 R315 全角公式和(26)，同一个最终有限圆准确支付
$$
\boxed{
\mathscr R_2\equiv0,\qquad
\mathscr R_L\equiv0,\qquad
[h^2](\mathscr R_E/(2\sigma))\equiv0
\quad\text{于全部 }\theta.
}
\tag{29}
$$
没有增加任何新实际运行；这是有限参数存在性证明。

## 8. 下一门必须继续用完整原式

仍欠(24)的其余六个 h 幂以及 R312 纯有理余式在同一个
$\operatorname{span}\{1,h,h^{-1}\}$ 中的成员条件。其 principal 之间可能有真实低阶兼容，不能仅按条目数增加振荡幅度。当前也没有支付全路径的 canonical period、同一二阶 gauge 的 joint 门或有限等距几何。

本稿的新推进是原 local+chain residue 的确切(6)，及由它推出的真实 cross0、C² self、初选有限纤维全角支付。下一分析可直接用完整(23)–(24)和 R312 的有理项；不再将 log 的整个局部残余当作“以后检查”的黑箱，也不把已付一行当作整个单 E 已解。
