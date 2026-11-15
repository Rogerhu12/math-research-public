# R237：例外端芽主能量消去后的完整下一 mixed 层

日期：2026-11-15。完整纸面推导；未运行新的 profile 积分、符号目标或几何计算。

本稿沿用 [R231](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md) 的真实例外偶端芽，在其两个领先能量均为零后，确定整个第四 ruling 的下一非平凡增长层。所有第二、第三累计 history、局部恢复和变化 profile 的链式项都保留。结论是两个新的准确必要能量条件；本稿不预填它们在 [R235](R235-nonseparable-complete-third-order-circles-with-zero-exceptional-leading-energies.md) 新圆上的值。

主要来源：[R56 原分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 逐点八矩与真实链式项](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R224 中心化与偶部商](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R227 例外 germ](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R229 同锚能量身份](R229-p2-energy-boundary-identity-for-exceptional-germs.md)及 R231。

## 1. 结论与固定约定

本稿固定 R231 的 $b=0$ 分支：

$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=\frac{k_e}{h},
\qquad \varepsilon>0,\ h_e>0,\ k_e\ne0.
\tag{1}
$$

共同 profile 区间 $I=[\ell,r]\Subset(0,\infty)$ 满足
$x+k_e/h_e>0$。因此解析模型上 $z=x+k_e/h$ 对全部实 $\sigma$ 为正。这里只用模型的解析延续检验实际局部 germ 的身份，不将原闭路径延长到无穷。

取双 collar 为零的实光滑三矩圆 $(f,g)$，即

$$
\mathbf m(f,f)=\mathbf m(g,g),\qquad \mathbf m(f,g)=0.
$$

设

$$
\phi_\theta=\cos\theta f+\sin\theta g,\qquad
D_\theta=f^2-\phi_\theta^2.
\tag{2}
$$

二次算子作用于 $D_\theta$ 时按对称双线性槽解释。三矩使每个八矩算子作用于 $D_\theta$ 后都在两个 collar 为零。

令 $Jq(x)=\int_x^r q$，并用 R73 的八基记

$$
\mathcal G=-\frac12\Phi_{p_2},\qquad
\mathcal P=\Phi_{p_1},\qquad
\mathcal T=\Phi_{t_1},\qquad
\mathcal D=\mathcal P-\frac18\mathcal T.
\tag{3}
$$

这里 $\mathcal G=G_0$ 正是 R231 的算子；$\mathcal D$ 与二次槽 $D_\theta$ 不同。为固定全部符号，

$$
\mathcal P(u,v)=-\frac12uv+\frac x2(uv'+u'v)
-\frac{x^2}{2}u'v'-\frac{x^2}{4}J(xu''v''),
$$

$$
\mathcal T(u,v)=x^2u'v'+xJ(x^2u''v''+2u'v').
\tag{4}
$$

能量始终按真实原函数定义：

$$
E(U,V)=\frac14\int_I(x^2U''V''+2U'V').
\tag{5}
$$

记 $A_f=\mathcal G(f,f)$。它一般有真实左二次尾，不称紧支撑。假设 R231 的两个领先条件已经成立：

$$
L_c=E\{A_f,\mathcal G(g,g)-\mathcal G(f,f)\}=0,
\qquad L_s=E\{A_f,\mathcal G(f,g)\}=0.
\tag{6}
$$

**定理。** 对 R224/R231 的中心化完整第四 ruling $\widehat{\mathscr K}_\theta$，有

$$
\boxed{
\lim_{\sigma\to+\infty}
\frac{\widehat{\mathscr K}_\theta(\sigma)}{h(\sigma)^2\sigma^6}
=\frac{8\varepsilon^2 k_e^3}{5}
 E\{A_f,\mathcal D D_\theta\}.
}
\tag{7}
$$

因此若实际完整第四 ruling 可由任意允许的第二、第三 homogeneous gauge 支付，还必须有

$$
\boxed{
M_c:=E\{A_f,\mathcal D(g,g)-\mathcal D(f,f)\}=0,
\qquad
M_s:=E\{A_f,\mathcal D(f,g)\}=0.
}
\tag{8}
$$

定理没有声称 (8) 非零，也没有声称 (6)、(8) 足以支付完整 ruling、period 或 joint 系统。

## 2. 原二阶密度的准确零次 h 层

置

$$
v=2\varepsilon\sigma,\qquad j=2\varepsilon k_e\sigma^2,
\qquad e=hx+j,\qquad z=x+k_e/h.
\tag{9}
$$

于是 $k=k_e-j$、$h_s=vh$、$j_s=2k_ev$，且

$$
K_0=kx^2+\frac{a}{h}x+\frac{b_0}{h^2},\qquad
a=k_e^2-j^2-1,\quad b_0=k_e(kj-1).
\tag{10}
$$

R73 的原八坐标中

$$
p_1=-kj,\qquad p_2=-kh/2,\qquad
t_1=(a-v^2)/8.
\tag{11}
$$

其余五个独立坐标全部是 $h^{-1},h^{-2},h^{-3}$ 乘 $\sigma$ 多项式的有限和。例如 $p_0=-k(1+j^2)/(2h)$；由 R73 的 $B_1$ 公式，$s_1=(aj-2k_ev^2)/(4h)$。$t_0=p_0/4+s_1/2$ 也没有零次 h 部分。

故点态真实密度准确为

$$
\boxed{
r_\sigma=hk\,\mathcal G-kj\,\mathcal P
+\frac{k_e^2-j^2-1-v^2}{8}\mathcal T+\mathcal N_\sigma,
\qquad
\mathcal N_\sigma=\sum_{m=1}^3h^{-m}\mathcal Q_m(\sigma),
}
\tag{12}
$$

其中每个 $\mathcal Q_m$ 是取值于固定八维算子空间的有限多项式。这不是只积分后成立的关系，也没有把局部加速度或速度项删去。

令

$$
\beta(\sigma)=\int_0^\sigma hk
=2k_e\int_0^\sigma h-k_e\sigma h.
\tag{13}
$$

R231 已付 $\beta/(h\sigma)\to-k_e$。完整中心第二 history 写成

$$
O=\int_0^\sigma r_\tau\,d\tau=\beta\mathcal G+C.
\tag{14}
$$

直接积分 (12) 给更精确的准确式

$$
\begin{aligned}
C(\sigma)={}&\frac{4\varepsilon^2k_e^2}{5}\sigma^5\mathcal D
-\frac{2\varepsilon k_e^2}{3}\sigma^3\mathcal P
-\frac{\varepsilon^2}{6}\sigma^3\mathcal T
+\frac{k_e^2-1}{8}\sigma\mathcal T
+\int_0^\sigma\mathcal N_\tau\,d\tau.
\end{aligned}
\tag{15}
$$

最后一项及其所需导数在正无穷有多项式界，而且该积分本身有有限极限。它是实际负 h 层的完整 history，不重置为零。特别地，设 $c_5=4\varepsilon^2k_e^2/5$，则

$$
C=c_5\sigma^5\mathcal D+O(\sigma^3),\qquad
C'=5c_5\sigma^4\mathcal D+O(\sigma^2).
\tag{16}
$$

这些估计在固定八维算子空间上成立；对任一固定光滑输入，可同时用于本稿所需的有限个 x 导数范数。

## 3. 控制幂次的记号与积分界

以下 $\operatorname{poly}$ 表示有某个有限多项式增长界的余项，阶数可以随表达式改变；它不包含任何正指数 h 因子。所需有限个 x 导数以及明确使用的 s 导数均取同类界。

写 $h^aO(\sigma^d)+\operatorname{poly}$ 时，$h^a$ 层的 d 是明确的，不能把该层任意提高到未指明的多项式阶。所有原局部表达式都来自 R56 的有限 Laurent 多项式，因此下文求导时使用原表达式，不从一个抽象 O 界推导其导数。

对固定整数 $d\ge0$，

$$
\int_0^\sigma h(\tau)(1+\tau)^d\,d\tau
=O\{h(\sigma)\sigma^{d-1}\}
\quad(\sigma\to+\infty).
\tag{17}
$$

这是正高斯指数的直接分部积分估计；对 $d=0$ 右边解释为 $h/\sigma$。有限起始区间只贡献常数。负 h 层乘任意固定多项式可积，实际原函数至多为 $\operatorname{poly}$。

## 4. 局部第三密度与 chain 项的真实界

对固定 profile $u$，记

$$
a_u=-u'/2,\qquad F_u=u-xu'/2.
$$

R56/R73 原分子及完整协变导数准确为

$$
V_u=(a_u,0,hF_u+ja_u),
\qquad
\nabla_sV_u=(0,hF_u+k_ea_u,vhF_u+2k_ev a_u).
\tag{18}
$$

第二局部恢复 $K$ 采用 R56 的 $W=0$ 分子，不能同时将 normal 与 eta 置零。直接由 (18) 的配对及 R56 (2)、(6)，得到

$$
P_2,\ B_2=hO(1)+\operatorname{poly},\qquad
\eta_2=hO(\sigma)+\operatorname{poly}.
\tag{19}
$$

更细地，零次 h 层中 $P_2,B_2$ 至多为二次多项式，$\eta_2$ 至多三次；剩余为负 h 层。代入 $V_K=(\eta_2/h,zP_2+B_2,e\eta_2/h)$ 及框架连接后，所需准确层级如下：

| 分量 | $V_K$ | $\nabla_s V_K$ |
|---|---|---|
| T | $O(\sigma)+$ 负 h 层 | $hO(\sigma^2)+\operatorname{poly}$ |
| N | $hO(1)+\operatorname{poly}$ | $hO(\sigma)+\operatorname{poly}$ |
| B | $hO(\sigma)+\operatorname{poly}$ | $hO(\sigma^2)+\operatorname{poly}$ |

表中 T 导数的 $h\sigma^2$ 来自真实 $-k(V_K)_N$，没有忽略 frame 导数。

在 $\ell=R[H(Y_\phi,K_D)]$ 中，P、B 为
$hO(\sigma)+\operatorname{poly}$，其 s 导数为
$hO(\sigma^2)+\operatorname{poly}$。$T_s/(2h^2)$ 至多
$O(\sigma^3)+$ 负 h 层；$K_0P$ 和 $(K_0/z)B$ 各至多
$hO(\sigma^3)+\operatorname{poly}$。另外
$\lambda=e_s/h^2=h^{-1}O(\sigma)+h^{-2}O(\sigma)$，故完整
$-\lambda P_s-\gamma B_s/h^2$ 不产生更高正 h 层。于是

$$
\boxed{\ell=hO(\sigma^3)+\operatorname{poly}.}
\tag{20}
$$

R73 的链式项也保留。其原式的零次 h 层恰为

$$
\Psi_\sigma(u,w)=-\frac{v(\sigma)}8\mathcal T(u,w)
+\sum_{m\ge1}h^{-m}\mathcal Q_m^\Psi(\sigma)(u,w).
\tag{21}
$$

这里 $v(\sigma)=2\varepsilon\sigma$ 是几何量；$\mathcal Q_m^\Psi$ 是有限多项式系数双线性算子，不要求对称。式 (21) 同时使用
$\nu-\gamma k/h^2=-(j/h)_s$ 的准确抵消。结合 (12)，

$$
\boxed{\Psi_\sigma(\phi,r_\sigma D_\theta)
=hO(\sigma^3)+\operatorname{poly}.}
\tag{22}
$$

因此本次更精细的层级没有把变化 profile 的 s 导数漏掉。

## 5. 第三 history 的两项准确抽取

设 $A=\mathcal G D_\theta$，并记 $C_D=C D_\theta$。中心第三 characteristic 满足 R231 的完整方程

$$
W_3'=-2\ell+2r_\sigma(\phi,\beta A+C_D)
+2\Psi_\sigma(\phi,r_\sigma D_\theta).
\tag{23}
$$

令 $r_0=r_\sigma-\beta'\mathcal G=C'$。抽取两个已指明 history，写

$$
W_3=\beta^2\mathcal G(\phi,A)
+2\beta\mathcal G(\phi,C_D)+V.
\tag{24}
$$

逐项求导后余项准确满足

$$
\begin{aligned}
V'={}&2\beta\{r_0(\phi,A)-\mathcal G(\phi,r_0D_\theta)\}
+2r_0(\phi,C_D)-2\ell
+2\Psi_\sigma(\phi,r_\sigma D_\theta).
\end{aligned}
\tag{25}
$$

这个等式保留了两个嵌套次序的差；未假定 $\mathcal G$ 与 $r_0$ 对易。由 (12)、(16)、(20)、(22)，第一项至多 $hO(\sigma^5)+\operatorname{poly}$，其余无更高正 h 层。用 (17) 和中心初值，得到

$$
\boxed{V=hO(\sigma^4)+\operatorname{poly}.}
\tag{26}
$$

式 (24) 的第二项是本稿不能省掉的 history；它为 $h\sigma^6$ 阶，进入 ruling 后正产生 $h^2\sigma^6$。

## 6. 完整局部第四部分没有同阶遗漏

这里检查 R56 恢复的全部局部项，而不只检查 (23)。完整第二场为

$$
Z_D=K_D-Y_{\beta A}-Y_{C_D}.
\tag{27}
$$

先看唯一含指数 history 的 $\beta$ 部分。其原分子 T 分量为
$hO(\sigma)$，B 分量为 $h^2O(\sigma)+h\operatorname{poly}$。
真正 s 导数必须包含 $\beta'Y_A$；其 T 分量为
$hO(\sigma^2)$，B 分量为
$h^2O(\sigma^2)+h\operatorname{poly}$。N 协变分量也完整保留。

将它与第一场 (18) 放入第三 forcing，再用 R56 (2)、(6)，其局部恢复满足

$$
P_3^{\beta},B_3^{\beta}
=h^2O(\sigma)+h\operatorname{poly}+\operatorname{poly},
$$

$$
\eta_3^{\beta}
=h^2O(\sigma^2)+h\operatorname{poly}+\operatorname{poly}.
\tag{28}
$$

尤其 $\eta_3$ 中的 $P_{3,s}$、$T_{s\xi}$ 和真实 $\beta'$ 均在该界内。恢复出的第三局部 TB 分量分别为
$hO(\sigma^2)+\operatorname{poly}$ 与
$h^2O(\sigma^2)+h\operatorname{poly}+\operatorname{poly}$。

来自 $Y_{C_D}$ 的分子仅为 $h\operatorname{poly}+\operatorname{poly}$；因为 C 及其导数均为多项式增长，它的第三局部恢复也只给这个指数级。来自 $K_D$ 的第三局部恢复更低，仍包含在该界内。

第四 ruling 用 $T_\xi/h$，而不是未经除 h 的物理猜测。故第一场与第三局部场的完整交叉至多

$$
h^2O(\sigma^2)+h\operatorname{poly}+\operatorname{poly}.
$$

同样，第二局部平方 $K_D^2$ 至多 $h\operatorname{poly}+\operatorname{poly}$；$K_D$ 与 $Y_{\beta A}$ 的交叉至多 $h^2O(\sigma^2)+h\operatorname{poly}+\operatorname{poly}$；$K_D$ 与 $Y_{C_D}$ 的交叉只给后两类。因此完整非 history 部分满足

$$
\boxed{\mathscr K_{\rm loc}
=h^2O(\sigma^2)+h\operatorname{poly}+\operatorname{poly}.}
\tag{29}
$$

这也解释为何只知道 R231 的粗 $O(h^2\operatorname{poly})$ 不足以推出本稿：必须把同指数 h² 层的次数明确压到二次。

## 7. 整个 ruling 的次层系数

R231 的第一场能量准确分为

$$
\mathcal E_\sigma(u,w)
=hE(u,w)+\frac j2\int_Ix u''w''
+\frac{1+j^2}{4h}\int_Iu''w''.
\tag{30}
$$

完整 history ruling 为

$$
-\mathcal E_\sigma(\beta A+C_D,\beta A+C_D)
+2\mathcal E_\sigma(\phi,W_3).
\tag{31}
$$

其中 $h\beta^2$ 项是 R231 的 $C_\theta$，由 (6) 对全部相位准确为零。不是只将其最高渐近系数设零。

式 (31) 的下一项来自 (24) 的 $2\beta$ 部分，恰为

$$
-2h\beta E(A,C_D)+4h\beta E\{\phi,\mathcal G(\phi,C_D)\}.
\tag{32}
$$

每个 $C_D$ 是真正双 collar 为零的固定八矩算子像。R229 三个紧槽的循环身份因而合法，给

$$
2E\{\phi,\mathcal G(\phi,C_D)\}
=-E\{C_D,\mathcal G(\phi,\phi)\}.
$$

由于 $A+\mathcal G(\phi,\phi)=A_f$，(32) 准确合为

$$
\boxed{-2h\beta E(A_f,C_D).}
\tag{33}
$$

这里 $A_f$ 的真实左尾仍在能量中；只用 $C_D$ 的紧性使循环身份成立。

其余部分逐类如下：

| 剩余来源 | 足够的完整上界 |
|---|---|
| $-hE(C_D,C_D)$ | $h\operatorname{poly}$ |
| $2hE(\phi,V)$ | $h^2O(\sigma^4)+h\operatorname{poly}$ |
| (30) 的 j 项作用于 $\beta^2$ 主项 | $h^2O(\sigma^4)$ |
| j 项的其余交叉与余项 | $h\operatorname{poly}+\operatorname{poly}$ |
| (30) 的 $(1+j^2)/h$ 项 | $h\operatorname{poly}+\operatorname{poly}$ |
| 全部局部项 | (29) |

于是

$$
\widehat{\mathscr K}_\theta
=-2h\beta E(A_f,C_D)
+h^2O(\sigma^4)+h\operatorname{poly}+\operatorname{poly}.
\tag{34}
$$

最后用 (13)、(16)，除以 $h^2\sigma^6$：

$$
\frac{-2h\beta E(A_f,C_D)}{h^2\sigma^6}
\longrightarrow 2k_ec_5 E(A_f,\mathcal D D_\theta)
=\frac{8\varepsilon^2k_e^3}{5}E(A_f,\mathcal D D_\theta).
$$

表中其余各项都趋零，证明 (7)。

## 8. 真实 gauge 商与两个相位条件

R224/R231 已经准确比较全部传入第二、第三 histories。其结论是

$$
[\operatorname{Ev}\mathscr K^0_\theta]
=[\widehat{\mathscr K}_\theta]\pmod{\mathcal W_e},
\qquad
\mathcal W_e=\operatorname{span}
\left\{h,\ \sigma^2,\ \frac{1+4\varepsilon^2k_e^2\sigma^4}{h}\right\}.
\tag{35}
$$

中心化没有删除未知 prefix；完整二阶初值对应一个合法紧 profile，任意二阶 gauge 的偶响应、其平方和第三初值的偶影响都按该已证身份处理。

$\mathcal W_e$ 的每个函数除以 $h^2\sigma^6$ 都趋零。若 (7) 某相位的值非零，则中心 ruling 不可能在 germ 中属于 $\mathcal W_e$。理由仍是同一真实正支上的解析延续：所有 s 系数及其有限真实 history 构成解析有限分离系统；固定 x-profile 可以只是光滑，不需关于 x 解析。没有沿实际闭几何作不允许的延长。

由 (2)，

$$
E(A_f,\mathcal D D_\theta)
=-\sin^2\theta\,M_c-\sin(2\theta)\,M_s.
\tag{36}
$$

这两个独立相位函数同时消失当且仅当 (8) 成立。因此 (8) 是全部允许 gauge 共同必须通过的完整下一层门，不是从单一 pure 或 mixed Fourier 项推测的障碍。

## 9. 可继续使用的范围

本稿覆盖任意满足 (2)、(6) 的固定三矩圆。特别可用于 R233 或 R235 的新圆，但仅靠它们已经支付 $L_c=L_s=0$，不能预先推断 $M_c$、$M_s$ 的值。

对两个支撑区间不交的完整三矩 block，(8) 的两个能量也准确相加：$\mathcal D(g,g)-\mathcal D(f,f)$ 与 $\mathcal D(f,g)$ 在各 block 两端为零，右方 block 的 $A_f$ 在左方 block 上是 $cx^2$，而 $E(x^2,Z)=0$ 对紧 Z 成立。这个加法保留所有原左尾；不允许在未满足三矩的微包级随意删除边界项。

若需要判断某个新圆，应另固定其完整 smooth profiles、幅度、放置及共同锚，准确计算或纸证 (8)，再决定是否进入更低层。任何新研究计算只在公开 Actions 执行。本稿没有重算旧四系数或 R232 的两领先能量，也没有把尚未评价的新必要门称为非零障碍。
