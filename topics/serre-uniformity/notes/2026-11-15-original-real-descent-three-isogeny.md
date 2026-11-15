# 原第4号映射的次数1206实下降与原正目标的明确比较

日期：2026-11-15。状态：**从 R791 实际共轭关系作出的纸面推论；没有新 Hom 计算，没有更换原 q、基点或高度规范。**

本记录给 R792/R793 的一个可选模型接口。当前 R792 仍直接输出原
$C_b:y^2=x^3+b$ 上的 $\beta_C$ 及原实映射 $f_R$ 的像；
本记录不改变其冻结算法或已认证生产者。

## 1. 一个次数一的目标同构使原 f 本身实下降

保留 $f=f_4$、$f(c_0)=O$、$\deg f=1206$，以及

$$
K=\mathbf Q(\zeta),\quad F_b=\mathbf Q(b),\quad L=F_bK,
\quad \varsigma=1+2\zeta,\quad
\alpha_3=1-\zeta^2,\quad a_3=1-\zeta.
$$

$F_b$ 使用原实嵌入，不额外声称全实。R791 已准确证明
$c(f)=-[\zeta^2]f$。定义

$$
C'/F_b:\quad Y^2=X^3-27b,
\qquad
\iota=D_{a_3}:C_{b,L}\xrightarrow{\ \sim\ }C'_L.
\tag{1}
$$

因为 $a_3^2=-3\zeta$、$a_3^3=-3\varsigma$、$a_3^6=-27$，
其坐标和实际不变微分的比较是

$$
X=-3\zeta x,\qquad Y=-3\varsigma y,
\qquad
\iota^*\frac{dX}{2Y}=a_3^{-1}\frac{dx}{2y}.
\tag{2}
$$

于是 $f'=\iota f$ 定义在 $F_b$ 上。证明只用实际共轭关系：
$-[\zeta^2]=D_{-\zeta}$，且
$(-\zeta)c(a_3)=(-\zeta)(1-\zeta^2)=a_3$，所以

$$
c(f')=D_{c(a_3)}c(f)=D_{a_3}f=f'.
\tag{3}
$$

$\iota$ 的次数为一，故 $\deg f'=1206$、$f'(c_0)=O$；
其实际微分是 $h'=h/a_3$。这两个标量不能省去。
这不是把原正目标凭同一 $j=0$ 替换为一个未比较的扭曲：
(1)–(3) 给明确的原映射、字段和微分运输。

## 2. 返回原正目标的三同源

定义 $F_b$ 上的有理映射

$$
\boxed{
\psi:C'\longrightarrow C_b,\quad
(X,Y)\longmapsto
\left(\frac{X^3-108b}{9X^2},
      \frac{Y(X^3+216b)}{27X^3}\right).}
\tag{4}
$$

在稠密开集上将 (2) 代入，恰得到 R791 的原公式

$$
x_R=-\frac{\zeta x(y^2+3b)}{3(y^2-b)},\qquad
y_R=\frac{y(y^2-9b)}{3\varsigma(y^2-b)}.
$$

因此 (4) 延拓为三次同源，且准确满足

$$
\psi\iota=[\alpha_3],\qquad
\psi f'=f_R,
\qquad
\psi^*\frac{dx}{2y}=3\frac{dX}{2Y}.
\tag{5}
$$

最后一式也由 $\alpha_3a_3=3$ 与 (2) 直接推出。
(4) 的分母9、27与 (5) 的微分倍数3都是原规范的一部分。

R792 若写有限原点为 $x_0=\zeta^2u_0$、
$y_0=\varsigma v_0$，则 $f'(c_1)$ 的实坐标就是

$$
(X_0,Y_0)=(-3u_0,9v_0)\in C'(F_b).
\tag{6}
$$

原 $\beta_C=O$ 时这两条实下降路径也都给 $O$。

## 3. 原有理商和极化尺度没有被消去

令

$$
B'=\operatorname{Res}_{F_b/\mathbf Q}C',\qquad
B=\operatorname{Res}_{F_b/\mathbf Q}C_b,\qquad
\Psi=\operatorname{Res}_{F_b/\mathbf Q}\psi.
$$

两者各用 R728 的共轭椭圆标准极化的外积极化。
Weil adjunction 给实际有理同态 $q'_R:J_X\to B'$，且

$$
q_R=\Psi q'_R.
\tag{7}
$$

在原 primitive 因子的有理同态范畴中写
$q'_R=v'q$、$q_R=vq$。R791 的原 $q$、$\lambda_A$ 保持不动；
(7) 给 $v=\Psi v'$。因每个椭圆分量的 $\psi$ 是三同源，

$$
\Psi^\dagger\Psi=[3]_{B'},\qquad
v^\dagger v=3(v')^\dagger v',\qquad
e':=\kappa(v')^\dagger v'=\frac e3,
\quad \kappa=qq^\dagger.
\tag{8}
$$

这里 $e$ 是 R791 实际求得的 $\kappa v^\dagger v$，不是一。
若在 $B'$ 的自然 theta 极化中使用 $e'$，原五个方向仍必须写成

$$
h_j=3\kappa^{-1}e'(s_j-r_j).
\tag{9}
$$

不能改用 $h_j/3$ 而仍称原高度方向不变。$v'$ 的任何整数化分母
也不能由本记录推定为一。$q'_R([c_1-c_0])$ 是原点经已知同源比较
后的像；本记录没有选择或恢复原抽象 $A$ 上某个未认证的同源核原像。

## 4. 极除子相同，主函数常数仍须保留

$Y'=-3\varsigma y$ 只是乘非零常数，故在原商曲线 $Y=X/\mu_3$ 上

$$
(Y')_\infty=(y)_\infty.
\tag{10}
$$

所以 $f'$ 的单个极除子次数仍为1206。
另一方面，(4) 的极点给

$$
P_{\psi g'}=3P_{g'}+\operatorname{div}\bigl((Y_{g'})^2+27b\bigr)
\tag{11}
$$

对任一同靶等变映射 $g'$ 成立；这与原 R791 的三同源除子公式一致。
若 $g'=D_{a_3}g$，则其主函数准确为

$$
(Y_{g'})^2+27b=-27(y_g^2-b).
\tag{12}
$$

两者的除子相等，但函数并不逐字相等。
若对 R791 的整数化组合使用 $r_j=a_j/b_j$，令 $\mathcal R'_j$
表示使用新因子 $(Y_{g'})^2+27\sigma b$ 的同一乘积/商，则准确有
$$
\mathcal R'_j=(-27)^{-7(b_j+a_j)}\mathcal R_j.
$$
如果要把旧的 $\mathcal R_j$ 用新因子乘积表示，则必须使用反向常数：
$\mathcal R_j=(-27)^{7(b_j+a_j)}\mathcal R'_j$。
这个常数在主除子层面不可见，却必须进入原 $c_0$ 刚性化、
Poincaré 函数或局部高度的运输。
因此使用 $B'$ 模型不会自动消掉 R791/R793 已保留的主函数修正。

依据：[R725](../results/R725-original-CM-elliptic-model-and-splitting-field.md)、
[R728](../results/R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md)、
[R764](../results/R764-certified-original-cusp-images-and-base-translation.md)、
[R791](../results/R791-certified-original-Hom-descent-and-eta-inputs.md)及
[R792](../results/R792-original-beta-composition-and-Galois-cube-root.md)。
