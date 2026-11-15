# R259：全部 Gaussian 面积的三外矩与不交微包的有序有限接口

日期：2026-11-15。**完整纸面结论。** 没有执行新的积分、规范化、参数扫描、矩阵消元或几何实际计算。

本稿把当前例外端芽的全部六个 Gaussian 面积同时写成准确有限条件。对于原三矩圆，保留不同的 outer profile $\phi_\theta$ 与 inner 二次槽 $D_\theta$；不会用对角变分的交叉抵消替代完整圆。对于不交实微包，真实跨包 history 准确归入三类有序双线性核，单包部分仍用原算子自矩，不把单包二次尾假称紧支撑。

六面积、三外矩、四个角系数共给 **72 条方程**。它们可以冗余；本稿不声称其独立，不声称已能联调，也不把全部面积为零当作整个第四 ruling 或 period 可解。

来源：[R73 原八矩](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R217 同锚代数导子](R217-two-left-tail-invariants-independent-on-pure-zero-responses.md)、[R245 完整 Gaussian history](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R249 真实词独立性](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)、[R250 整圆面积](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R251 非共振系数](R251-nonresonant-Gaussian-area-obstruction-and-two-exceptional-curves.md)、[R252 原交叉矩](R252-two-further-Gaussian-areas-exclude-the-even-packet-exceptional-family.md)及 [R257 累计 primitive 门](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)。

## 1. 固定原问题与六个面积

采用同一共同右锚 $r$，

$$
J(F)(x)=\int_x^rF(t)\,dt,\qquad (J(F))'=-F.
$$

所有 profile 位于同一物理区间的双零 collar 内；本稿不改变目标度量或已选几何。

取真实例外端芽

$$
H=e^{\varepsilon\sigma^2},\quad h=h_eH,\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\qquad
h_e>0,\ \varepsilon>0,\ \kappa\ne0.
\tag{1}
$$

对实三矩圆 $(f,g)$ 定义

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{2}
$$

$\odot$ 始终是对称二次算子槽。三矩为

$$
\begin{aligned}
I_0(u,v)&=\int_Iu''v'',\\
I_1(u,v)&=\int_Ixu''v'',\\
I_2(u,v)&=\int_I(x^2u''v''+2u'v').
\end{aligned}
\tag{3}
$$

这里 $I_2$ 就是先前的 $I_2^*$，不省略一阶导项。圆条件为
$\mathbf I(f,f)=\mathbf I(g,g)$、$\mathbf I(f,g)=0$。

用 $\Phi_X$ 表示八矩方向 $X$ 的原二次算子；写

$$
[X,Y](u;B)=
\Phi_X(u,\Phi_YB)-\Phi_Y(u,\Phi_XB).
\tag{4}
$$

以下也把 $X$ 简写为 $\Phi_X$。四个 Gaussian 剩余方向是

$$
\begin{aligned}
B_1&=\zeta\Phi_{p_2},&
B_{-1}&=d\Phi_{p_0}+e\Phi_{s_1},\\
B_{-2}&=a\Phi_{r_1}+b\Phi_{s_0},&
B_{-3}&=c\Phi_{r_0},
\end{aligned}
\tag{5}
$$

其中

$$
\zeta=-\kappa h_e,\qquad d=6\kappa^3/h_e,\qquad
e=-\frac{\kappa(14\kappa^2+1+4\varepsilon)}{4h_e},
$$

$$
a=\frac{\varepsilon(16-36\kappa^2)-93\kappa^4-8\kappa^2-16}{128h_e^2},
\qquad
b=-\frac{\kappa^2(9\kappa^2+4+32\varepsilon)}{32h_e^2},
$$

$$
c=\frac{\kappa\{\varepsilon(36-84\kappa^2)-20\kappa^4-9\kappa^2-27\}}{216h_e^3}.
\tag{6}
$$

各值允许发生已经识别的退化；本稿不除以它们。

沿用原 $E_r,K_{r,s}$ 及 $A_{r,s}=K_{r,s}-K_{s,r}$。R245/R249/R250 的完整三槽恢复给：

$$
[A_{r,s}]\mathscr K_\theta
=2\mathcal E_\sigma
\{\phi_\theta,[B_r,B_s](\phi_\theta;D_\theta)\}.
\tag{7}
$$

这里固定 $r>s$，$r,s\in\{1,-1,-2,-3\}$。二阶平方只产生对称 history，所有真实中心常数和其余恢复项已保在原分解，不能另生一个反对称面积。

外能量完整为

$$
\mathcal E_\sigma(u,v)
=\frac{1+j^2}{4h}I_0(u,v)+\frac j2I_1(u,v)+\frac h4I_2(u,v),
\quad j=2\varepsilon\kappa\sigma^2.
\tag{8}
$$

$H$ 对 $\mathbb R(\sigma)$ 超越，且 $j$ 非常数。因此对固定 $\theta$，式 (7) 恒零等价于

$$
\boxed{
I_\ell\{\phi_\theta,[B_r,B_s](\phi_\theta;D_\theta)\}=0,
\quad \ell=0,1,2.
}
\tag{9}
$$

真实 Gaussian 词独立性保证六面积之间以及它们与零、一层 history 不能互相抵消。所以下文给出的 72 方程是**六个完整面积都消失**的必要充分条件；它们仍只是完整 ruling 的一部分。原完整第三 period/ruling、允许 gauge 与同一目标度量的其他要求仍须按原构造支付。

## 2. 八个 local cubic 密度

令 $u$ 为任意紧 profile，$v=u'$、$\rho=u''$，并记

$$
J_0=J(\rho^2),\quad
J_1=J(x\rho^2),\quad
J_2=J(x^2\rho^2+2v^2).
$$

全部原二次对角式为：

| $X$ | $\Phi_X(u,u)$ |
|---|---|
| $r_0$ | $J_0$ |
| $r_1$ | $v^2+xJ_0$ |
| $s_0$ | $J_1$ |
| $p_0$ | $uv-xv^2/2-x^2J_0/4+J_2/4$ |
| $s_1$ | $xv^2+xJ_1+J_2/2$ |
| $p_1$ | $-u^2/2+xuv-x^2v^2/2-x^2J_1/4$ |
| $t_1$ | $x^2v^2+xJ_2$ |
| $p_2$ | $-xu^2+x^2uv-x^3v^2/2-x^2J_2/4$ |

不要求这些输出单独紧支撑。定义

$$
F_{X,\ell}(u)=I_\ell(u,\Phi_X(u,u)).
$$

对 $\ell=0$，真实同锚 IBP 给 $F_{X,0}=\int f_{X,0}$，其中：

| $X$ | $f_{X,0}(x,u,v,\rho)$ |
|---|---|
| $r_0$ | $0$ |
| $r_1$ | $-\rho^3/3$ |
| $s_0$ | $-\rho^3/3$ |
| $p_0$ | $-v\rho^2/2$ |
| $s_1$ | $v\rho^2-x\rho^3$ |
| $p_1$ | $u\rho^2/2-xv\rho^2+x^2\rho^3/4$ |
| $t_1$ | $2xv\rho^2-x^2\rho^3$ |
| $p_2$ | $xu\rho^2-3x^2v\rho^2/2+x^3\rho^3/3-v^3/3$ |

式中所有 primitive 已按原右锚消去，外 collar 端项均含紧 $u$ 的导数；没有把 $J_i$ 的真实左常尾置零。

例如 $p_1$ 的原二导为

$$
(\Phi_{p_1}(u,u))''
=u\rho-xv\rho+xu\rho'-x^2v\rho'
+\frac{x^2}{4}\rho^2-\frac{J_1}{2}
+\frac{x^3}{2}\rho\rho'.
$$

与 $\rho$ 配对，并用 $\int\rho J_1=\int xv\rho^2$，得到表中系数。$p_2$ 的全部原二导及端项已经在 R257 逐项列出；其余六项由同样的 $J_i'$ 和一次 IBP 直接得到。

## 3. 不重新展开原算子的全部三外矩

R217 的代数导子

$$
\mathscr Du=x^2u'-2xu
$$

只用于算子身份，不冒作允许的几何变换。令

$$
\delta X=\mathscr D\circ\Phi_X
-\Phi_X(\mathscr D\,\cdot,\cdot)
-\Phi_X(\cdot,\mathscr D\,\cdot).
$$

其准确八维表是：

| $X$ | $\delta X$ |
|---|---|
| $r_0$ | $-2r_1-2s_0$ |
| $r_1$ | $4p_0-2s_1$ |
| $s_0$ | $-2s_1$ |
| $p_0$ | $-2p_1-t_1/2$ |
| $s_1$ | $4p_1-2t_1$ |
| $p_1$ | $-p_2$ |
| $t_1$ | $4p_2$ |
| $p_2$ | $0$ |

对 local 密度 $f(x,u,v,\rho)$ 定义显式多项式运算

$$
\mathscr Vf
=-x^2f_x-2xf-2xu f_u-2u f_v
+(2x\rho-2v)f_\rho.
\tag{10}
$$

这是 $\int f$ 沿 $\delta u=\mathscr Du$ 的真实变分密度。它由一次完整总导数
$\int x^2D_xf=-2\int xf$ 得到；不是新原函数。

全部其余 16 个 cubic 密度可直接定义为

$$
\boxed{
f_{X,1}=\frac{\mathscr V f_{X,0}+f_{\delta X,0}}2,
\qquad
f_{X,2}=\mathscr V f_{X,1}+f_{\delta X,1}.
}
\tag{11}
$$

方向线性组合按表线性解释。于是

$$
F_{X,\ell}(u)=\int_If_{X,\ell},
\qquad \ell=0,1,2.
\tag{12}
$$

**证明。** 对一槽紧的配对，完整 IBP 给

$$
I_0(\mathscr Du,w)+I_0(u,\mathscr Dw)=2I_1(u,w),
$$

$$
I_1(\mathscr Du,w)+I_1(u,\mathscr Dw)=I_2(u,w),
$$

$$
I_2(\mathscr Du,w)+I_2(u,\mathscr Dw)=0.
\tag{13}
$$

允许 $w=\Phi_X(u,u)$ 有左尾，因为另一槽 $u$ 的全部端导数为零。将
$2\Phi_X(u,\mathscr Du)=\mathscr D\Phi_X(u,u)-\Phi_{\delta X}(u,u)$
代入真实变分，便得到 (11)。

这给出完整、可直接消费的 24 个 local cubic 密度。没有只计算 $I_0$ 后宣称其他两矩同理，也没有删去 $I_2$ 的 $2u'v'$。

## 4. Full outer/inner 的准确变分，不能用 diagonal 抵消

令

$$
L_0=\partial_x^4,\qquad
L_1=x\partial_x^4+2\partial_x^3,\qquad
L_2=x^2\partial_x^4+4x\partial_x^3.
\tag{14}
$$

它们满足一槽紧时 $I_\ell(u,w)=\int wL_\ell u$。定义 Euler 密度

$$
\operatorname{EL}(f)=f_u-D_xf_v+D_x^2f_\rho
$$

及 local quadratic 函数

$$
\boxed{
Q_{X,\ell}(u)
=\operatorname{EL}(f_{X,\ell})(u)
-L_\ell[\Phi_X(u,u)].
}
\tag{15}
$$

虽然右边显示原二次算子，$Q_{X,\ell}$ **确为 local**：所有 $J_i$ 的外系数次数不超过 2，而 $L_\ell$ 至少含三阶导数，故每个 primitive 都被真正求导；没有余 Volterra 变量。它的支撑包含于 $u$ 的支撑。

对任意光滑 $w$，即使 $w$ 有左多项式尾，

$$
\boxed{
2I_\ell\{u,\Phi_X(u,w)\}=\int_I Q_{X,\ell}(u)\,w.
}
\tag{16}
$$

先对紧 $w$ 由 (12) 求变分：

$$
DF_{X,\ell}(u)[w]
=I_\ell(w,\Phi_X(u,u))
+2I_\ell(u,\Phi_X(u,w)).
$$

使用对称配对即得 (16)。对一般 $w$，取在 $\operatorname{supp}u$ 邻域等于 1 的紧 cutoff。所有原二次 integrand 都含 $u$ 或其导数，故 $\Phi_X(u,w)$ 不变；local $Q$ 也不变。这完整支付了非紧方向，未延伸局部密度身份到未经许可的非紧输入族。

因此对于任意原二次槽 $B$，

$$
\boxed{
2I_\ell\{u,[X,Y](u;B)\}
=\int_I Q_{X,\ell}(u)\,\Phi_YB
-Q_{Y,\ell}(u)\,\Phi_XB.
}
\tag{17}
$$

特别，对 $B=D_\theta$，三矩使 $\Phi_YB,\Phi_XB$ 真正紧支撑；此时直接用 cubic 变分写 (17)，它包含

$$
\begin{aligned}
2I_\ell\{u,[X,Y](u;B)\}
={}&DF_{X,\ell}(u)[\Phi_YB]
-DF_{Y,\ell}(u)[\Phi_XB]\\
&-I_\ell(\Phi_YB,\Phi_X(u,u))
+I_\ell(\Phi_XB,\Phi_Y(u,u)).
\end{aligned}
\tag{18}
$$

末行两项一般不抵消；只在相应变分方向也已合法的特殊 diagonal $B=u\odot u$ 时才有对称抵消。式 (15) 中的两个 $-L_\ell$ 项正是保住了这对完整 quadratic cross 配对。后文非紧单包方向只使用已由 cutoff 证明的 (17)，不把 (18) 越界套到两个同时带尾的配对。

## 5. 微包左尾与精确 sl2 作用

对一个实紧微包 $u$ 记

$$
\mathbf m(u)=(m_0,m_1,m_2)
=(I_0(u,u),I_1(u,u),I_2(u,u)).
$$

原 $\Phi_X(u,u)$ 在该微包左侧的完整多项式尾为
$A_Xx^2+B_Xx+C_X$：

| $X$ | $A_X$ | $B_X$ | $C_X$ |
|---|---:|---:|---:|
| $r_0$ | $0$ | $0$ | $m_0$ |
| $r_1$ | $0$ | $m_0$ | $0$ |
| $s_0$ | $0$ | $0$ | $m_1$ |
| $p_0$ | $-m_0/4$ | $0$ | $m_2/4$ |
| $s_1$ | $0$ | $m_1$ | $m_2/2$ |
| $p_1$ | $-m_1/4$ | $0$ | $0$ |
| $t_1$ | $0$ | $m_2$ | $0$ |
| $p_2$ | $-m_2/4$ | $0$ | $0$ |

右侧准确为零。没有假定某个单包 $m_i=0$。

令 $p=Ax^2+Bx+C$，并记

$$
D_-u=u',\qquad D_0u=xu'-u,\qquad D_+u=x^2u'-2xu.
$$

同一个右锚直接给：

| $X$ | $\Phi_X(u,p)$ |
|---|---|
| $r_0$ | $-2A D_-u$ |
| $r_1$ | $B D_-u$ |
| $s_0$ | $-2A D_0u$ |
| $p_0$ | $(C/2)D_-u-(A/2)D_+u$ |
| $s_1$ | $B D_0u-A D_+u$ |
| $p_1$ | $(C/2)D_0u$ |
| $t_1$ | $B D_+u$ |
| $p_2$ | $(C/2)D_+u$ |

这些是原函数身份，不是单纯尾匹配。其原 primitive 计算为

$$
J(u''p'')=-2Au',\qquad
J(xu''p'')=-2A(xu'-u),
$$

$$
J(x^2u''p''+2u'p')=-2Ax^2u'-2Bu.
\tag{19}
$$

$u$ 的右 collar 消掉所有右端边项，左侧没有重锚。代入原八式即得表。

三个外矩对这些真实一阶作用是

$$
\begin{aligned}
2\mathbf I(u,D_-u)&=(0,-m_0,-2m_1)=:\mathbf t_-(\mathbf m),\\
2\mathbf I(u,D_0u)&=(m_0,0,-m_2)=:\mathbf t_0(\mathbf m),\\
2\mathbf I(u,D_+u)&=(2m_1,m_2,0)=:\mathbf t_+(\mathbf m).
\end{aligned}
\tag{20}
$$

每式由普通 IBP 得到；这里的 $D_+$ 仍只是用于原算子计算，未赋予新的实际几何控制权限。

## 6. 只有三类跨包 history 核

令 $\mathbf m=(m_0,m_1,m_2)$ 对应左侧 outer 微包，$\mathbf n=(n_0,n_1,n_2)$ 对应右侧 inner 微包。定义

$$
\mathbf\Gamma_{X,Y}(\mathbf m,\mathbf n)
=
2\mathbf I\{u,\Phi_X(u,\operatorname{tail}_Y(\mathbf n))
-\Phi_Y(u,\operatorname{tail}_X(\mathbf n))\}.
\tag{21}
$$

式 (19)、(20) 表明它只依赖两组三矩。需要的三个核准确为

$$
\boxed{
\mathbf K_1(\mathbf m,\mathbf n)
=\left(-m_1n_0,\
-\frac{m_0n_2+m_2n_0}{2},\
-m_1n_2\right),
}
$$

$$
\boxed{
\mathbf K_2(\mathbf m,\mathbf n)
=\left(-m_0n_0,\
-m_0n_1,\
m_2n_0-2m_1n_1\right),
}
$$

$$
\boxed{
\mathbf K_3(\mathbf m,\mathbf n)
=\left(\frac{m_0n_2}{2}-m_1n_1,\
-\frac{m_2n_1}{2},\
-\frac{m_2n_2}{2}\right).
}
\tag{22}
$$

对式 (5) 使用的六个方向
$\{r_0,r_1,s_0,p_0,s_1,p_2\}$，全部非零基本核为

| ordered operator pair $(X,Y)$ | $\mathbf\Gamma_{X,Y}$ |
|---|---|
| $(r_0,p_2)$ | $\mathbf K_1$ |
| $(r_1,s_1)$ | $\mathbf K_2$ |
| $(s_0,p_0)$ | $-\mathbf K_2/2$ |
| $(s_0,p_2)$ | $\mathbf K_3$ |
| $(p_0,s_1)$ | $\mathbf K_1/2$ |

其余基本 pair 的核为零；交换 $X,Y$ 取负，但不交换 $\mathbf m,\mathbf n$。特别，这些核一般不对称，不能把有序求和改成无序平均。

按原六 Gaussian pair，完整结果为：

| $(r,s)$ | $\mathbf\Gamma_{B_r,B_s}$ |
|---|---|
| $(1,-1)$ | $0$ |
| $(1,-2)$ | $-\zeta b\,\mathbf K_3$ |
| $(1,-3)$ | $-\zeta c\,\mathbf K_1$ |
| $(-1,-2)$ | $(db/2-ea)\mathbf K_2$ |
| $(-1,-3)$ | $0$ |
| $(-2,-3)$ | $0$ |

“核为零”只表示该 pair 的**跨不交微包尾贡献**为零，不表示完整交换子、自微包贡献或真实面积为零。

## 7. 完整圆的 72 方程

设实微包 $u_i$ 支撑严格不交，从左到右编号，且

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i.
\tag{23}
$$

形状、宽度、中心都可以不同。先准确支付三矩圆：

$$
\sum_i(a_i^2-b_i^2)\mathbf m_i=0,\qquad
\sum_i a_i b_i\mathbf m_i=0.
\tag{24}
$$

记

$$
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,\qquad
d_i(\theta)=a_i^2-c_i(\theta)^2.
$$

定义原 self 向量

$$
\mathbf S_{X,Y}(u_i)
=2\mathbf I\{u_i,[X,Y](u_i;u_i\odot u_i)\}.
\tag{25}
$$

这一定义允许二次 inner 输出有真实左尾；其准确评价可直接用 (17) 的 local $Q$ 和两条原二次输出。**不得**将 R257 对合法整体 $q$ 的 compact 变分公式，逐包套到不合法的单个 $u_i$。

由于原二次 integrand 局部，而 (15) 的 $Q$ 为 local quadratic，完整三矩准确为

$$
\boxed{
\begin{aligned}
2\mathbf I\{\phi_\theta,[X,Y](\phi_\theta;D_\theta)\}
={}&\sum_i c_i(\theta)^2d_i(\theta)\mathbf S_{X,Y}(u_i)\\
&+\sum_{i<k}c_i(\theta)^2d_k(\theta)
\mathbf\Gamma_{X,Y}(\mathbf m_i,\mathbf m_k).
\end{aligned}}
\tag{26}
$$

**次序证明。** 在第 i 个 outer 支撑上，来自左方 $k<i$ 的 inner 二次场已经处于其准确右零 collar，贡献为零；来自右方 $k>i$ 的场恰为原二次多项式左尾，贡献正是 (21)。同包使用完整 (25)。原 $Q$ 中的平方系数是 $c_i^2$，inner 槽系数是 $d_k$，不能换成对称的 $c_i^2d_k+c_k^2d_i$。

对固定 Gaussian pair、固定外矩分量，定义上三角标量阵

$$
\Omega_{ik}=
\begin{cases}
S_{B_r,B_s,\ell}(u_i),&i=k,\\
\Gamma_{B_r,B_s,\ell}(\mathbf m_i,\mathbf m_k),&i<k,\\
0,&i>k.
\end{cases}
\tag{27}
$$

式 (26) 为 $\sum_{i,k}\Omega_{ik}c_i^2d_k$。其完整 $\theta$ 恒零恰等价于

$$
\boxed{
\begin{aligned}
0={}&-2\sum_{i,k}\Omega_{ik}a_i^2a_kb_k,\\
0={}&\sum_{i,k}\Omega_{ik}
\{a_i^2(a_k^2-b_k^2)-4a_ib_i a_kb_k\},\\
0={}&2\sum_{i,k}\Omega_{ik}
\{a_ib_i(a_k^2-b_k^2)-b_i^2a_kb_k\},\\
0={}&\sum_{i,k}\Omega_{ik}b_i^2(a_k^2-b_k^2).
\end{aligned}}
\tag{28}
$$

它们依次是 $\cos^3\theta\sin\theta$、
$\cos^2\theta\sin^2\theta$、
$\cos\theta\sin^3\theta$、$\sin^4\theta$ 的系数。
没有 $\cos^4\theta$ 项，因为原 $D_0=0$。
四个 homogeneous monomial 在单位圆上独立；例如在 $\cos\theta\ne0$ 上除以 $\cos^4\theta$ 后得到一个一元多项式。因此 (28) 是准确 iff，不是有限角采样。

对六个 pair 和三个 $\ell$ 全部使用 (28)，便得到宣称的 72 方程。参数退化、已知原身份或三矩可能使它们相依，本稿不预填其真实秩。

## 8. 为混宽度构造保留的实际数据与范围

本接口不恢复第四 forcing，也不需重新求 Gaussian histories。它需要的 profile 数据仅为：

1. 每个实际微包的三个原矩 $\mathbf m_i$；
2. 六个 Gaussian pair 的原 self 三向量，或由 (10)—(17) 给出的固定形状积分；
3. 严格真实左右次序及实幅度 $(a_i,b_i)$。

跨包项已由 (22) 全部显式支付。对固定基本形状的正宽度缩放和平移，self 数据是有限个形状积分的 Laurent/多项式组合；不能把这些常数当作独立可调坐标。

还可给一个不依赖未证消项的有限次数界：原二次表的每项总坐标次数至多 4；$f_{X,0}$ 至多 3，递推 (10) 每次至多加 1；式 (15) 的 local 项坐标次数至多 6。故 (25) 用 local $Q$ 乘原二次输出时，平移参数次数至多 10。同步搬移输入时，右锚上限始终位于零 collar，原 $J$ 的全部展开均是有限多项式，不产生另一个未记的锚常数。宽度正缩放只引入有限整数幂；例如 $w^{3/2}$ 的归一化在四次 self 项中给 $w^6$。

这不是把 R257 的累计量消掉。相反，其 $[r_0,p_2]$ 正对应 $\mathbf K_1$；原有序条件会自然进入 (28)。只有对完整合法 profile 使用全部式子以后，才允许进一步用零三矩合并为 R257 的 $\int(Jq''^2)^2$ 形式。

在共振参数下，一般微包的 R241 能量层确可由整体紧目标和逐包 bulk 身份归为 $N_c=6M_c,N_s=6M_s$；这不消本稿三类有序核。新的两斜率、不同宽度或符号排列构造必须同时支付这些真实有限关系，不能只配平局部四次张量及 $S/C$。

本稿没有执行或安排新的实际计算，没有赋予任意 self 常数独立控制权，也没有证明这 72 方程与所有其他第四项可同时解。它完成的是原三外矩、整圆相位与全部跨微包 history 的统一准确接口。

## 9. 十二个完整副本同时清掉全部 odd 角系数

这个推论给一个真实可用的缩减，但不清 even 系数。

取已经完成三矩与完整第三阶的 base circle，**并窄定它具有 R183 的八复制结构**：第三完整槽的平移系数次数至多 6，由八项有限差分准确消去。再对整个 base 作一次共同平移，原有限差分仍消掉任意次数至多 6 的多项式，故其完整第三闭合在每个合法共同平移后都保持。原支持/同锚性质按 R183/R245 的完整 block 范围使用。这一前提强于“只知道当前某一 geometry、某一平移处的第三 forcing 为零”，本推论不从后者擅推平移稳定。

先共同正缩放，使十二个不交 base 平移副本可以在所选物理 I 内留有严格 collar。令

$$
d_j=d_0+j\Delta,\quad 0\le j\le11,\qquad
\epsilon_j=(-1)^j,\qquad
\gamma_j=\binom{11}{j}^{1/4}>0.
\tag{29}
$$

在第 j 个完整副本中，取 $(\gamma_j f_j,\epsilon_j\gamma_j g_j)$。每个副本的三矩只乘 $\gamma_j^2$，仍为圆；已经为零的完整第三槽只乘 $\gamma_j^3$。$g\mapsto-g$ 是固定正交作用，保 R183 已付的完整三槽零张量。第三闭合按上述精确平移稳定范围保留，不以局部连续性代替。

不同完整副本之间，式 (26) 的交叉项准确为零：对位于右方的完整副本，

$$
\sum_{k\ {\rm in\ that\ block}}d_k(\theta)\mathbf m_k=0,
$$

而 $\mathbf\Gamma$ 对其 inner 三矩线性。等价地，原 $\Phi_XD_\theta$ 在该完整副本左侧真正为零。共同副本幅度不影响这个零。因此不能把这一步偷换为“每个微包的左尾都为零”；每个 base 内部的全部有序项仍保留。

对固定 pair/外矩，两个 odd 系数 $\cos^3\theta\sin\theta$ 与
$\cos\theta\sin^3\theta$ 在翻转 $g$ 后反号；两个 even 系数不变。
完整面积是 profile 四次齐次的，所以第 j 个 odd 系数准确乘 $\epsilon_j\gamma_j^4=(-1)^j\binom{11}{j}$。未经幅度缩放的系数是 $d_j$ 的次数至多 10 的真实多项式，已由第 8 节逐原槽界支付。十一阶有限差分给

$$
\sum_{j=0}^{11}(-1)^j\binom{11}{j}d_j^k=0,\qquad 0\le k\le10.
\tag{30}
$$

于是全部六 Gaussian 面积、三个外矩的 **36 个 odd 方程同时准确为零**。这里只作十二个 profile 副本的纸面构造，没有执行新求积。若需整体实归一化，所有第四量只乘同一正四次因子。

剩余 36 个 even 方程一般仍非零，且内部累计 primitive 不消失。这个包装也不保持一条仅在原平移处碰巧为零的 even 能量；例如若要与 $L_c=0$ 联调，应把全部十二副本纳入原准确参数方程以后再求解，不能先解单个 base 再宣任意平移保持该零。

本推论不证明这些 even 方程与其余 ruling 函数可同时支付。所得是新选择的完整圆及 seed，一般改变原来的目标 seed；不宣称沿旧固定 seed 作了允许的变形。

