# R324：完整有理九门、十九维真实主空间与同一圆的全部中心偶 germ

日期：2026-11-15。**完整纸面原式与有限频率存在性证明；没有执行求积、符号程序、人工测试、数值秩或研究计算。**

本稿接 [R312](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md)、[R315](R315-full-angle-arctangent-square-gates-and-ordered-history-cancellation.md)、[R318](R318-complete-local-log-residue-and-a-first-single-arctangent-gate.md)与 [R321](R321-complete-single-arctangent-gates-and-ten-dimensional-joint-control.md)。此前非有理的平方、对数和全部单反正切系数已能共同支付，但纯有理余式尚不能仅凭 principal 宣称清零。

下面首先从 R56 完整恢复逐层证明：**整个**有理余式只含 $h^{-7},\ldots,h^4$，没有范围外的纯 $C^2$ 系数。除去原允许的 $1,h,h^{-1}$ 后恰有九个真实门。其主项与 R321 的十行联合恰十九维。新的真实 pure-self 补偿保持全角结构，有限正幅锥和同纤维有限频率根则支付全部十九个完整值，包括所有低阶基线。

结论是同一个实际新圆的完整**中心偶 germ**属于 $\mathcal W_e$，并经 R312 的真实比较成为原偶部的商结论。不由此宣整个闭路径 ruling、canonical period、同一二阶 gauge 的 joint 问题或主课题已解。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、[R296](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)、[R299](R299-complete-centered-ruling-angular-reduction-by-corrected-pure-self-fibers.md)和上述新端芽原稿。

## 1. 实际端芽与完整待解向量

沿 R321 的约定，
$$
h=H(1+\varepsilon\sigma^2),\quad H=h_e>0,\quad
\kappa\ne0,\quad\varepsilon>0,\quad \omega=0,\quad k=\kappa,
$$
$$
K=1+\kappa^2,\quad e_{\rm g}=hx-\kappa,\quad
Q_{\rm g}=1+e_{\rm g}^2,\quad
\gamma=2H\varepsilon\sigma,\quad
\gamma^2=4H\varepsilon(h-H),\quad\gamma_\sigma=2H\varepsilon.
\tag{1}
$$
几何仍按 R312 从最初在实际安装邻域内选择，不在已固定度量上改变这些参数。原共同正 profile 区间和右锚一直保留。

完整中心式为
$$
\widehat{\mathscr K}_\theta
=\mathscr R_{{\rm rat},\theta}
+E\,\mathscr R_{E,\theta}
+E^2\,\mathscr R_{2,\theta}
+\log(h/H)\,\mathscr R_{L,\theta},
$$
$$
E=\frac{\arctan(\sqrt\varepsilon\,\sigma)}{\sqrt\varepsilon}.
\tag{2}
$$
R312 的两复 pole monodromy 已证明这四类在有理函数域上线性独立，不能用相互抵消代替单独支付。

本稿首先证明
$$
\boxed{\mathscr R_{{\rm rat},\theta}
=\sum_{m=-7}^{4}h^m Z_m(\theta)}
\tag{3}
$$
对完整原式成立。$\mathcal W_e=\operatorname{span}\{1,h,h^{-1}\}$，故新增九个真正系数为
$$
Z_m,\qquad m\in\mathcal J=\{-7,-6,-5,-4,-3,-2,2,3,4\}.
\tag{4}
$$
与 R321 的三个 $q_j$ 和七个 $\rho_\ell$ 合起来，
$$
\mathcal V_{19}=
(q_0,q_1,q_2,\rho_{-4},\ldots,\rho_2,(Z_m)_{m\in\mathcal J}).
\tag{5}
$$
每一项始终定义为完整实际值。以下 principal 仅用来构造改变这些值的方向。

## 2. 原二阶与局部第三恢复给准确 pole 封口

用 $\mathscr L[p,q]$ 表示几何系数为有限 Laurent 和，h 次数位于整数区间 $[p,q]$。系数是原固定 profile 表达，包括真正的 J；这个记号不把任何系数设成零。

R318 的准确二阶局部分子是
$$
V_K=(\gamma F,N,e_{\rm g}\gamma F),\qquad
F\in\mathscr L[-3,-1],\quad N\in\mathscr L[-1,1].
\tag{6}
$$
elementary 第二 history 是
$$
\mathsf Q=\sigma\mathsf A(h),\qquad
\mathsf A\in\mathscr L[-3,1],\qquad
\mathsf Q'=\mathsf A+2(h-H)\mathsf A_h\in\mathscr L[-4,1].
$$
因此 $Z_0=K(D)-Y_{\mathsf QD}$ 的 T、B 分量分别为
$\sigma\mathscr L[-3,1]$、$\sigma\mathscr L[-3,2]$，N 分量为
$\mathscr L[-1,1]$。原 ruling 配对是 $h^{-1}\int V_x\cdot V_x$；对合法 whole D 它与 physical 配对相同。由
$\sigma^2=(h-H)/(H\varepsilon)$，
$$
\mathfrak b(Z_0,Z_0)\in\mathscr L[-7,4].
\tag{7}
$$

考虑第三的局部 forcing $H(Y_\phi,K(D))$。R56 的两个原恢复量满足
$$
P_C=\gamma\overline P,\quad B_C=\gamma\overline B,
\qquad \overline P,\overline B\in\mathscr L[-4,0].
\tag{8}
$$
这是原 $P_C=(2h)^{-1}J(V_\phi'\cdot V_K')$、
$B_C=(2h)^{-1}V_\phi\cdot V_K$ 的次数，非对其左尾作假设。

原联络与(6)给 $T_{\sigma x,C}\in\mathscr L[-4,2]$。代 R56(6)，全部项为
$$
\eta_C^{(0)}
=-\frac{T_{\sigma x,C}}{2h}
+\frac{\gamma x}{2h}(P_C)_x
+\frac{\gamma}{2h}(B_C)_x-\frac12(P_C)_\sigma
\in\mathscr L[-5,1].
\tag{9}
$$
特别 $(P_C)_\sigma=\gamma_\sigma\overline P+
\gamma^2\overline P_h$ 中可能的最低 $h^{-5}$ 不能删掉。

其余两个真实第三 local 项分别满足
$$
\eta_K(\phi,\mathsf QD)\in\mathscr L[-5,2],
\qquad
\eta^{\rm ch}(\phi,\mathsf MD)\in\mathscr L[-5,2].
\tag{10}
$$
第一式使用 $\gamma\sigma=2(h-H)$。第二式直接用 R296(6)：
$$
\eta^{\rm ch}(\phi,w)
=\frac{2he_{\rm g}\phi''w-2h^2\phi'w
-Q_{\rm g}\phi''w'-J_e(\phi,w)}{16h},
\quad
\mathsf M\in\mathscr L[-4,1].
$$
这里 $w=\mathsf MD$，不能换为 $\mathsf Q'D$。

与紧 outer $Y_\phi$ 配对再乘 $Q_{\rm g}/(2h^2)$，(9)—(10)均不出
$\mathscr L[-7,2]$。等价地可直接用分子配对；这也保住单包 self 的 formal 边项，而不偷用其第一槽紧性。

## 3. 完整第三原函数及真实中心常数也不越界

R312 的原式为
$$
U'=\mathscr C_\sigma(\phi;D)
-\mathsf Q'(\phi,\mathsf QD)
+E'[\mathsf Q,B](\phi;D),\quad U(0)=0,
$$
其中 $\mathscr C_\sigma=\ell_\sigma-\Psi_\sigma(\phi,\mathsf MD)$，且 $E'=H/h$。

将整个式子除以 $\gamma$，就是对 h 的准确导数。由 R56(5)及(8)，
$$
\ell_\sigma/\gamma\in\mathscr L[-7,0].
\tag{11}
$$
最低幂来自
$-x(\gamma_\sigma\overline P+\gamma^2\overline P_h)/h^2$
及相同的 $\overline B$ 项，必须先保留。
R318 的完整 $T_{\sigma,C}/\gamma$ 在 $\mathscr L[-4,1]$ 内，再除 $2h^2$ 不越(11)。

原 chain
$$
\Psi_\sigma(\phi,w)/\gamma
=-\frac{\kappa}{4h^2}\phi'w
-\frac{Q_{\rm g}}{8h^3}\phi'w'
-\frac{x}{8h^3}J_e(\phi,w)
$$
对 $w=\mathsf MD$ 同样在 $\mathscr L[-7,0]$。其余两项准确是
$$
-\frac{\mathsf Q'(\phi,\mathsf QD)}{\gamma}
=-\frac{(\mathsf A+2(h-H)\mathsf A_h)(\phi,\mathsf AD)}
{2H\varepsilon}\in\mathscr L[-7,2],
$$
$$
\frac{E'[\mathsf Q,B]}{\gamma}
=\frac{[\mathsf A,B]}{2\varepsilon h}\in\mathscr L[-4,0].
$$
故
$$
\boxed{U'/\gamma\in\mathscr L[-7,2].}
\tag{12}
$$
准确积分每个幂：
- $h^{-1}$ 产生 R318 已完整识别的 $\log(h/H)\mathscr D$；
- 其余项产生 $h^{-6},\ldots,h^3$；
- 为使 $U(0)=0$，必须减去在 $h=H$ 的真实常数。

因此
$$
U_{\rm rat}\in\mathscr L[-6,3].
$$
原能量系数为 $(K/(4h),-\kappa/2,h/4)$，从而
$$
\mathcal E_h(\phi,U_{\rm rat})\in\mathscr L[-7,4].
\tag{13}
$$
这个中心常数只经原三个能量权进入，未被事先设零。

(7)、(9)—(13)放回 R312(23)的整个 $\mathscr R_{\rm rat}$，即证明(3)。这是全恢复的次数界；所以(4)以外确实没有未计入的 $C^2$-only 商系数。

## 4. 九个真实有理 principal

沿 R321 定义
$$
W=v-xr,\quad C=u-xv+x^2r/2,\quad
b(x)=a+ex+tx^2,\quad
\alpha_B=2(bW-eC),
$$
$$
a=\frac{K(\varepsilon-2K)}{32H^2},\quad
e=\frac{\kappa K}{4H},\quad t=-\varepsilon/4.
$$
令 $\Psi_h=p(h,x)W+q(h,x)C$，p、q 正是 R321(8)。

R296 的**完整**共同主平方给
$$
Z_m(\pi/2)\equiv_2
\sum_i\lambda_i\int\mathcal Z_m(x,W,C)(u_i''')^2,\quad
\lambda_i=-a_i^2R_i,
$$
$$
\boxed{
\sum_{m=-7}^{4}h^m\mathcal Z_m
=\frac{(h-H)Q_{\rm g}}{4H\varepsilon h}\Psi_h^2.}
\tag{14}
$$
真实 $C^2$ 余项并未删除；它包含(9)—(13)刚封住的所有系数。由于原 finite geometry 函数分解唯一，主项抽取与各原幂系数的有限线性抽取可交换。

R321 已证另外十行是
$$
\alpha_B\cdot
\operatorname{span}\{x^jW,x^jC:0\le j\le4\}
$$
的一组基。现在核九个(14)在这个十维空间之外真正增加九维。

## 5. 一个可直接手核的九余式表

若某些(14)的线性组合落在上述 $\alpha_B$ 倍数空间，将
$$
C=\frac{b(x)}eW
\tag{15}
$$
代入，所得必须为零。$e\ne0$，这个代数代入合法；不是改变任何真实 profile。

令 $\zeta_m(x)$ 是(15)后 $\mathcal Z_m/W^2$。为少写共同正分母，下面全部先乘 $4H\varepsilon$。低六个余式的次数与最高系数如下：

| $m$ | 次数 | $[x^{\deg}](4H\varepsilon\zeta_m)$ |
|---:|---:|---|
| $-7$ | $0$ | $-K^3\varepsilon^2H^3/9$ |
| $-6$ | $1$ | $8\kappa K^2\varepsilon^2H^3/9$ |
| $-5$ | $2$ | $-7K\varepsilon^2H^3(1+4\kappa^2)/9$ |
| $-4$ | $4$ | $2\kappa K^2\varepsilon H^3t/(9e)$ |
| $-3$ | $5$ | $-10\kappa^2K\varepsilon H^3t/(9e)$ |
| $-2$ | $6$ | $4\kappa(2+5\kappa^2)\varepsilon H^3t/(9e)$ |

每项非零。前三条只用 $\Psi_h$ 的 $W^2$ 部分；后三条最高次来自其真正 $WC$ 部分乘 $b/e$，不能把它漏掉后误报次数3、4、5。

为核高三条，置
$$
y=-\frac{\kappa x^2b}{6e},\qquad
z=\frac{\kappa^2xb}e-\frac K4x^2,\qquad
p=2Ha+\varepsilon Hx^2.
$$
在同一共同分母下，它们准确为
$$
\begin{aligned}
r_4&=x^2y^2,\\
r_3&=3Hr_4-2\kappa xy^2+2x^2zy,\\
r_2&=(K-6\kappa Hx)y^2+(-4\kappa x+2Hx^2)zy
+x^2z^2+2x^2py,
\end{aligned}
\tag{16}
$$
其中 $r_m=4H\varepsilon\zeta_m$。进行两个明确的常数行变换：
$$
r_3^*=r_3-3Hr_4,\qquad
r_2^*=r_2-\frac{9H}{7}r_3+\frac{27H^2}{7}r_4.
$$
其准确最高系数是
$$
\begin{array}{c|c|c}
 &\deg&\text{最高系数}\\ \hline
r_4&10&\kappa^2t^2/(36e^2)\\
r_3^*&9&-7\kappa^3t^2/(18e^2)\\
r_2^*&8&
\displaystyle\frac{\kappa^2t^2(1+61\kappa^2)}{36e^2}
-\frac{\kappa Ht(K+14\varepsilon)}{42e}
\end{array}
\tag{17}
$$
最后一项严格正：$t<0$、$\kappa/e=4H/K>0$，它的两个显示部分均正。

所以九个余式经上述可逆行变换的次数为
$$
0,1,2,4,5,6,8,9,10,
$$
均有非零首项，因而线性独立。任何落入 $\alpha_B$ 倍数空间的九行组合只能全零，再用 R321 十行的独立性，得到
$$
\boxed{\text{十九个原 principal 在自由 jet 多项式空间中恰独立。}}
\tag{18}
$$
没有执行消元程序，也没有按行数授秩。

## 6. 真偶配对、同一个母包与全部原副本

十九个多项式全是 x、W、C 的二次式。R321 的偶点分离说明：若一个二次 jet 多项式对所有偶母包、偶 $\chi$ 及平移都零，它必须为
$Auv+Bvr$，其中 A、B 是常数。

本次甚至不需共同 $\alpha_B$ 因子。写
$$
v=W+xr,\qquad u=C+xW+x^2r/2 .
$$
若 $Auv+Bvr$ 只依赖 x、W、C，那么其关于独立 r 的系数都零。$r^2$ 系数是 $Ax^3/2+Bx$，故 A=B=0。因此(18)在真实偶主观察中仍为十九维。

有限维分离、有限点 Hermite 见证和保非零 minor 的解析逼近，可在一个正解析母包
$u_0=\psi P_0,\ P_0>0$ 上用有限个
$\chi_\alpha=\psi Q_\alpha$ 达到这十九维。至多十九个形状足够。

各 principal 的位置次数至多十：(14)中 $\Psi_h$ 至多四次，$Q_{\rm g}$ 再加二次；R321 十行的次数更低。所有原复制共同作用
$P(X)\mapsto\sum_cw_cP(X+d_c)$，仍是在次数十空间上的可逆三角算子。故全套真实正四次权、八/十二副本和最后五块都不减(18)的主空间。

## 7. 完整中心角余项：须把 R299 的原证明重新接到本芽

R299 正文以 Gaussian 安装为背景。本节不用其特殊标量微分式，而逐项说明同一真尾证明在(1)上的适用依据。

在本中心、同右锚的原恢复上，定义
$$
K_\sigma(u)=\mathfrak b_\sigma(Z(u^2),Z(u^2))
+4\mathfrak b_\sigma(Y_u,C(u;u^2)).
\tag{19}
$$
单包用原分子配对 $h^{-1}\int V_x\cdot W_x$；不能假其尾紧。R296 的原主恒等只依赖 R56/R73 逐点式，故在这里仍成立。其幅度多项式中取 $a=0,d=-c^2$，整个三阶平方准确抵消，留下可按真 J/Green 降阶的四次 $C^2$ 泛函。由此(19)是**完整真实** $C^2$ self，不是只抽取零 principal。

对左、右两包的原三矩 $\mu,\nu$，写真实二阶左尾
$$
\Pi_\mu(x)=xU_\mu+V_\mu.
$$
R56 的同中心恢复给跨包第三
$W=\beta_\nu u'-\beta_{\nu,x}u$，$\beta_\nu$ 二次。它由真实二阶尾确定，仍满足 R299(16)，没有新增自由初值。令
$$
\mathcal A_{\beta_\nu}=he_{\rm g}\beta_\nu
-\frac{Q_{\rm g}}2\beta_{\nu,x},
\qquad
\mathbf a_{\beta_\nu}=([x^0],[x^1],[x^2])\mathcal A_{\beta_\nu}.
$$
最高三次项准确消掉。原积分端差和原 cross 恢复依次给
$$
\mathfrak b(Z_\mu,Z_\nu)
=-\Pi_\mu(\ell)\cdot U_\nu/h,\qquad
\mathfrak b(Y_u,C(u;v^2))
=\mu\cdot\mathbf a_{\beta_\nu}/(4h).
$$
这两条只用原联络和右锚，不用 Gaussian 方程。因此本芽的准确 whole 有序核和校正 self 仍是
$$
\boxed{
\Gamma_\sigma(\mu,\nu)
=-2\Pi_\mu(\ell)\cdot U_\nu/h
+\mu\cdot\mathbf a_{\beta_\nu}/h,\qquad
\widehat K_\sigma=K_\sigma-\Gamma_\sigma(\mu,\mu)/2.
}
\tag{20}
$$
它含原局部项、完整中心二/三 history、两真实左尾。补偿后与任选左零 collar 的位置无关；可以在证明平移次数时同步移动该端点，而不改实际锚。

R56 的有限运算及原分子次数界给
$$
\widehat K_\sigma(u_\tau)=\sum_{d=0}^{10}\tau^d\widehat K_{\sigma,d}(u).
\tag{21}
$$
(3)及 R312/R318 的其他三类界同时用于这些形式 self 与 cross，故其真实几何函数在
$$
\mathscr E=
\operatorname{span}\{
h^m:-7\le m\le4;\
\sigma E h^\ell:-4\le\ell\le2;\
E^2h^j,\log(h/H)h^j:-1\le j\le1
\}
\tag{22}
$$
内。单包 Green 补偿只含同原恢复的系数，不增这些范围。R312 的双 pole monodromy与各 Laurent 幂独立性给 $\dim\mathscr E=25$。也可仅用此有限生成空间，不先求其坐标。

选其真实有限点评价基。于是从起点在 R321 的 $\mathcal F_{\rm one}$ 中加入
$$
[\tau^d]\widehat K_{\sigma_\alpha}(u_\tau),
\qquad 1\le\alpha\le25,\quad0\le d\le10
\tag{23}
$$
即可保持整个(21)。这是至多275条额外明确生成观察，不称其控制秩为275。各项是四次 $C^2$；平移系数可用十一固定合法平移的值插值，不需 profile 十阶导数。

## 8. 全角还原与整个完整基线

以 $\mathcal F_{\rm rat}$ 记从起点加入(23)后的整个有限映射。原二次槽恒等和(20)给
$$
\widehat{\mathscr K}_\theta
=\sin^2\theta\,\widehat{\mathscr K}_{\pi/2}
+\sin^2\theta\cos^2\theta\,\Xi_\sigma,
$$
$$
\Xi_\sigma
=\sum_i(R_i^2-4T_i^2)\widehat K_\sigma(u_i)
+\sum_{r<s}\gamma_{rs}(\sigma)\mathcal A_{rs}.
\tag{24}
$$
这里 $T_i=a_ib_i$，三个 $\mathcal A_{rs}$ 是含原 $I_2$ 的真正 ordered wedge。

同 $\mathcal F_{\rm rat}$ 使第一项保持同母平移值，等背景的
$R_i^2-4T_i^2=(7B_0/2)R_i$ 及十次矩消去将其准确清零；第二项由原五个最终完整 block 正权清掉。十二完整副本消全部 odd 角。故
$$
\boxed{\widehat{\mathscr K}_\theta
=\sin^2\theta\,\widehat{\mathscr K}_{\pi/2}}
\tag{25}
$$
对本芽完整中心函数成立，包含所有四类(2)，不只一个系数或 principal。

(23)必须先选，再选真最大秩母包和纠正方向。R293 的有限多项式 prefactor 直线方法使它与第6节十九阶 principal minor 同时非零；不存在在冻结旧母包上暗增275个数值的步骤。

## 9. 十二真实列的正核与有限 N 的十九门真零

每个选中的 $\chi_\alpha$ 占用原等背景编码的不同第二层，使用十二个真实交替索引
$$
0,1,33,34,49,50,65,66,81,82,97,98 .
$$
真实位置递增，$\lambda_i=-a_i^2R_i$ 交替。次数十的十二点 Vandermonde 核同样交替；除以 $\lambda_i$ 后给每一形状组严格正核。十二点评价张成其整个位置多项式系数空间。十九维分离于是给联合所有列的正锥恰为 $\mathbb R^{19}$。

对每个选中基本包用
$$
u_{i,N,z}=u_0+z_iN^{-3}\chi_{\alpha(i)}\cos(Ny)
+\text{同整个 }\mathcal F_{\rm rat}\text{ 的有限纠正},
$$
所有实际副本同步。固定有限正幅盒上，真实完整映射满足
$$
\mathcal V_{19,N}(\pi/2)
=b+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{26}
$$
v 包含全部真实 copy 权和振荡平均 $1/2$；b 含原全部 local、chain、非紧 self、跨尾和低阶有理系数。由 §§2—3，没有 b 以外被丢掉的未知商幂。

联合正锥给严格正幅 $z_i^*$ 使极限为零。选择十九条独立列、固定其余正幅后，Jacobian 可逆。因此足够大但有限的 N 上有真零
$$
\boxed{\mathcal V_{19,N}(\pi/2)=0.}
\tag{27}
$$
原有限纤维保持了完整 log 门及所有原三矩、E8 面积、第三条件、角 self 和 ordered wedges。没有要求余项自行小于某个数值容差，而是对完整原方程使用有限 N 的准确隐函数定理。

五个最后 block 在各自已经选定的真实位置和正幅权下分别作此操作，取有限个阈值的最大值。所有后续混合仅用已定正幅，不再移动已求出的圆。解析版本仍可取 $\psi$ 乘全区正 prefactor，有限 N 后保持真实平端与内解析结构。

## 10. 新结论的准确范围

在同一个从起点构造的实际有限圆上，由(25)、(27)和 R318 的完整 log 支付，
$$
\boxed{
\mathscr R_{E,\theta}=\mathscr R_{2,\theta}
=\mathscr R_{L,\theta}=0,\qquad
\mathscr R_{{\rm rat},\theta}\in
\operatorname{span}\{1,h,h^{-1}\}
\quad\text{对全部 }\theta .
}
\tag{28}
$$
这一次支付了 R312 完整四类分解的全部局部函数成员条件，而非只其主空间或有限 Taylor 层。

R312 §3.1 保原 history 入值、任意允许第二 gauge 与同一第三常量的比较已经给
$$
[\operatorname{Ev}\mathscr K_\theta^0]
=[\widehat{\mathscr K}_\theta]\pmod{\mathcal W_e}.
$$
故(28)确实消掉该实际端芽的完整**偶部商**，不需要重锚全路径，也不从 Gaussian 的特殊公式借用比较。

仍须支付实际闭路径其余段、可能的奇部、canonical 整个 period、平台/flux、内部 range、同一允许第二 gauge 的 joint 匹配。更高阶收敛、固定目标度量的有限连续等距族、闭面嵌入、reach 及宏观握持条件也不由本稿推出。新进展是：旧 Gaussian 正余量所排的 rank-one profile 类，在这个从头安装的合法有理端芽上，已经不存在同类的**完整局部偶 germ**障碍；这不宣该类已完成主课题。
