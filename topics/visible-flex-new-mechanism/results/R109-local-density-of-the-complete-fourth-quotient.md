# R109：完整第四成本模可调响应的局部密度约简

日期：2026-11-14。**已证明。** 本稿只作原式纸面推导与小型自由对称代数核对，不进行新的 profile、几何或完整研究编译。依据 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 和 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)。

本稿把 R105 的有限商进一步化成一个**不含累计第二、第三历史的局部积分问题**。端点势并没有被设为零；它产生一个明确修正项。结论适用于完整相位算子，不只适用于纯第四谐波。局部密度的剩余商、真实成本半群、第四 ruling 及更高阶仍未支付。

## 1. 固定 canonical 对象

沿真实有限路径使用

$$
h>0,\qquad \omega_s=\frac{k_s}{2h},
$$

固定共同物理区间、右 collar 与右端原函数，保持 $\xi+\omega>0$ 的统一间隙。目标、第一 profile 和差记为

$$
F=f\odot f,\qquad
\phi=\cos\theta f+\sin\theta g,\qquad
D=F-\phi^2.
$$

第二、第三恢复及第四成本均采用 R105 的 canonical 选择，不加入任意新的齐次 profile gauge，不重置左尾或途中历史。

记 $E_8=\{\Phi_M:M\in\mathfrak{sl}_3(\mathbb R)\}$，$W$ 为 R80 的完整真实第三可调空间：

$$
W=W_{71}+V_3+W_1.
$$

所有空间都按真实 profile 函数身份定义。第三算子 $\tau(a;b,c)$ 只要求内两槽对称；不交换外槽和内槽。若 $D$ 是对称二次张量，按线性延拓写 $\tau(a;D)$。

对 $A\in E_8$、完整第三算子 $\tau$ 定义

$$
\begin{aligned}
\mathfrak F(A,\tau)
&=2\tau(AD;D)-4\tau(\phi;\phi,AD),\\
\mathcal B_A(\tau)
&=\mathfrak F(A,\tau)+4A\bigl(\phi,\tau(\phi;D)\bigr).
\end{aligned}\tag{1}
$$

这是 R83 的完整第四响应。记

$$
\mathcal R_8=\operatorname{span}
\{\mathcal B_A(\tau):A\in E_8,\ \tau\in W\}.
\tag{2}
$$

这里模掉的是已有真实控制方向的**函数线性空间**，不是把实际成本半群擅自允许取负。

## 2. 局部第三势：为什么余项逐点属于 W

用 $n(s)$ 表示 R73 的完整局部第三密度 $\mathcal C_s$。R77 与 R79 给的是以下原式分解：

$$
n=D_s(P_{\rm acc}+P_h)
+\mathcal A(S)(k_s h_{ss}-h_s k_{ss})
+\sum_{j=0}^3\mathcal C_j(S)h_s^{3-j}k_s^j
+k_s R(S),
\qquad S=(h,k,\omega).
\tag{3}
$$

$P_{\rm acc}$ 是速度二次式，$P_h$ 是权一项沿 $h$ 的真实原函数。R77 的 $V_3$ **定义为** $\mathcal A(S),\mathcal C_j(S)$ 的实际算子值的跨度，再证明这个空间可由真实路径实现。因此 (3) 的面积与三次速度部分在每个 $s$ 都属于 $V_3$。此处不是从“某个积分可实现”反推被积函数的逐点性质。

对最后的 $R$，取一个固定 $h_*>0$，令

$$
a_*(k,\omega)=
\left.(R+hR_h)\right|_{h=h_*},\qquad
b_*(k,\omega)=
\left.-h^2R_h\right|_{h=h_*}.
$$

R79 证明在真实商 $E_3/W_1$ 中，

$$
[R]=[a_*]+[b_*]/h,\qquad
\partial_\omega[a_*]=2\partial_k[b_*].
\tag{4}
$$

固定参考 $(k_*,\omega_*)$，取下面的**实际算子代表**，而不只写一个抽象商元素：

$$
F_*(k,\omega)=
\int_{k_*}^{k}a_*(v,\omega_*)\,dv
+2\int_{\omega_*}^{\omega}b_*(k,u)\,du.
\tag{5}
$$

积分只作用于几何系数，profile 右锚不变。由 (4)，

$$
R-(F_*)_k-\frac{(F_*)_\omega}{2h}\in W_1
\quad\text{在每个状态 }S\text{ 成立}.
\tag{6}
$$

这一步来自 R79 已证的原式相容性及实际函数商，不依赖任何不完备正规化报告。有限 Laurent/log 与多项式几何系数使 (5) 仍是有限局部算子表达式。

现在定义

$$
\boxed{N(s)=P_{\rm acc}(s)+P_h(S(s))+F_*(k(s),\omega(s)).}
\tag{7}
$$

它只依赖当前状态和有限 jets，不依赖从路径起点累计的二、三阶历史。真实关系 $\omega_s=k_s/(2h)$、(3) 与 (6) 给

$$
\boxed{w(s):=n(s)-N'(s)\in W\quad\text{逐点成立}.}
\tag{8}
$$

$N$ 的初值一般不为零；即使路径首末是常值 germs，也只保证 $P_{\rm acc}$ 的端值为零，不能删掉 $P_h,F_*$ 的端值。后文保留这些常势。

## 3. 完整真实历史的微分系统

把从路径起点到 $s$ 的零传入 second、third、fourth 数据分别记作

$$
A(s),\qquad T(s),\qquad V(s),
\qquad A(0)=T(0)=V(0)=0.
$$

R73 的逐点八矩给

$$
m(s):=A'(s)\in E_8.
$$

这里 $m$ 是点态密度，$A$ 才是累计算子；这与 R73 对矩阵积分的字母命名有所不同。

由 R83 的真实 composition 对末段长度求导，得到

$$
\boxed{
\begin{aligned}
A'&=m,\\
T'&=n-m\circ A,\\
V'&=v+\mathfrak F(A,n)
-m(AD,AD)-4m\bigl(\phi,T(\phi;D)\bigr),
\end{aligned}}
\tag{9}
$$

其中

$$
(m\circ A)(a;b,c)=m\bigl(a,A(b,c)\bigr).
$$

$v(s)$ 是完整第四局部生成元，其定义次序非常重要：

1. 先按 R56 对物理第二、第三场及其 forcing 求**全部真实 $s$ 导数**；
2. 代入真实 history 微分方程；
3. 最后才把累计 second、third scalar 值设为零。

这不把这些历史的导数也设为零。它等价于 (9) 中一段无累计传入值的无穷小路径第四增量。因而 $v$ 仍包含全部 normal、mixed 与局部 drift 项，并非单独取某个静态 forcing。

(9) 不要求在每个切点造一个常值 germ，也没有在切点重锚。它是同一条真实路径的原式演化；R83 的输入历史差恒等式在任意光滑切点成立。

## 4. 第一轮消去：保留端点势的常数

令

$$
Q(s)=N(s)-N(0),\qquad
\bar T=T-Q,\qquad
\bar V=V-\mathfrak F(A,Q).
\tag{10}
$$

于是 $Q(0)=0$，$Q'=n-w$，由 (9) 得

$$
\bar T'=w-m\circ A,
\tag{11}
$$

以及

$$
\boxed{
\bar V'=v-\mathcal B_m(Q)
+\mathfrak F(A,w)-m(AD,AD)
-4m\bigl(\phi,\bar T(\phi;D)\bigr).
}
\tag{12}
$$

例如 $-\mathcal B_m(Q)$ 中的最后一项来自
$T=\bar T+Q$ 的真实第三历史，而不是任意补入的修正。只保留
$-\mathfrak F(m,Q)$ 会漏掉这项。

定义内对称三线性交换子

$$
\tau_{A,m}=A\circ m-m\circ A.
$$

因为 $A,m\in E_8$，它属于 $W_{71}\subset W$。再令

$$
\boxed{H=\bar T+\frac12A\circ A.}
\tag{13}
$$

则

$$
\boxed{H'=w+\frac12\tau_{A,m}\in W,\qquad H(0)=0.}
\tag{14}
$$

有限维真实函数空间 $W$ 对积分封闭，所以 $H(s)\in W$ 对整条路径成立。原累计第三算子 $T(s)$ 未必在 $W$；(13) 中的局部势和对称二阶历史正是使这一结论合法所需的修正。

## 5. 第二轮消去及六分之一系数

记 $a=AD$、$b=mD$。定义三次于 $A$ 的第四表达式

$$
\mathfrak C(A)=
-\frac13A(a,a)
+\frac23A\bigl(\phi,A(\phi,a)\bigr),
\tag{15}
$$

以及

$$
\boxed{
Z=V-\mathfrak F(A,Q)-\mathfrak F(A,H)-\mathfrak C(A).
}
\tag{16}
$$

逐项求导给准确恒等式

$$
\boxed{
Z'=v-\mathcal B_m(Q)-\mathcal B_m(H)
-\frac16\mathcal B_A(\tau_{A,m}).
}
\tag{17}
$$

以下把唯一较易漏项的自由代数部分展开。先由 (12)–(14) 消掉
$\mathfrak F(A,w)$，余下除 $v-\mathcal B_m(Q)-\mathcal B_m(H)$ 外为

$$
R=-A(a,b)+2A\bigl(\phi,m(\phi,a)\bigr).
$$

另一方面，

$$
\begin{aligned}
\mathfrak C'(A)
={}&-\frac13\{m(a,a)+2A(a,b)\}\\
&+\frac23\{
m(\phi,A(\phi,a))
+A(\phi,m(\phi,a))
+A(\phi,A(\phi,b))\}.
\end{aligned}
$$

而 (1) 直接给

$$
\begin{aligned}
\mathcal B_A(\tau_{A,m})
={}&2A(a,b)-2m(a,a)
-8A(\phi,m(\phi,a))\\
&+4m(\phi,A(\phi,a))
+4A(\phi,A(\phi,b)).
\end{aligned}
$$

故 $R-\mathfrak C'(A)=-\mathcal B_A(\tau_{A,m})/6$。这里仅使用 $A,m$ 的双线性与对称性，没有假设算子复合可交换或可结合，也没有只核对角 profile。

## 6. 零矩路径的完整商公式

现假设整条路径的二阶矩阵为零，即

$$
A(L)=0.
$$

不必先假设 $T(L)=0$。由于 (16) 中三个端点修正都含 $A$，

$$
Z(0)=0,\qquad Z(L)=V(L).
$$

又 $m,A\in E_8$、$H,\tau_{A,m}\in W$，所以

$$
\int_0^L\mathcal B_m(H)\,ds,\qquad
\int_0^L\mathcal B_A(\tau_{A,m})\,ds
\in\mathcal R_8.
$$

最后保留 (10) 中的常势：

$$
\int_0^L\mathcal B_m(Q)\,ds
=\int_0^L\mathcal B_m(N)\,ds
-\mathcal B_{A(L)-A(0)}(N(0)).
$$

末项由实际零总矩阵准确为零；不是把 $N(0)$ 设成零。于是得到主结论

$$
\boxed{
[V_B]_{\mathcal R_8}
=
\left[\int_0^L
\bigl\{v(s)-\mathcal B_{m(s)}(N(s))\bigr\}\,ds
\right]_{\mathcal R_8}.
}
\tag{18}
$$

等价的未取商身份是

$$
\boxed{
V_B=
\int_0^L\bigl(v-\mathcal B_mN\bigr)\,ds
-\int_0^L\mathcal B_mH\,ds
-\frac16\int_0^L\mathcal B_A(\tau_{A,m})\,ds.
}
\tag{19}
$$

(19) 明确保留了两个历史修正，只是证明它们的完整函数值落在已知 $\mathcal R_8$。没有把它们在物理路径上无成本地删除。

若改选另一个局部势 $\widetilde N$，且仍有
$n-\widetilde N'\in W$，则沿给定路径
$\widetilde N-N=C_0+W_s^*$，其中 $C_0$ 为常算子、$W_s^*\in W$。
常项的积分由 $A(L)=0$ 消掉，另一项落在 $\mathcal R_8$。因此 (18) 的商类不依赖势代表、参考状态或势原函数锚的选择；这些变化必须连同其真实端差一起作，不能只改某一项。

## 7. 有限且局部的下一计算对象

定义真实局部第四密度

$$
\boxed{\mathscr L_4(s)=v(s)-\mathcal B_{m(s)}(N(s)).}
\tag{20}
$$

R105 的分子恢复式保证 $v$ 的 profile 部分不含随 $\omega$ 移动的 $\xi$ 极点。$m$ 是 R73 的同一八矩算子；$N$ 是第 2 节的有限局部 profile 表达式。把三者作 (20) 中有限次双线性代入后，仍只需要：

- 固定坐标 $\xi$ 的多项式；
- $f,g$ 的有限 jets；
- 同一右端锚、严格正 profile 次数的有限 Volterra 原函数；
- 依赖当前几何状态与有限 jets 的系数，包括可能的 $\log h$。

因此存在一个独立于路径取值的有限模板表，使

$$
\mathscr L_4(s)=\sum_{\alpha=1}^{N_{\rm loc}}
c_\alpha(j^rS(s))\,\Psi_\alpha(f,g).
\tag{21}
$$

这里没有累计矩阵 $A(s)$ 或累计第三算子 $T(s)$。当前没有计算
$N_{\rm loc}$，没有把模板数当成真实维数，也没有把每个几何系数当作可独立调节。

R105 已证明 $\mathcal U_4$ 可由同端口、frame 恒等的真实 $M=0$ 路径成本张成。因此 (18) 准确给

$$
\boxed{
\mathcal U_4/\mathcal R_8
=
\operatorname{span}
\left\{
\left[\int_B\mathscr L_4\,ds\right]:
B\text{ 为同端口真实零矩路径}
\right\}.
}
\tag{22}
$$

若个别局部模板本身不在 $\mathcal U_4$，可先在有限环境空间
$\mathcal U_4+\operatorname{span}\{\Psi_\alpha\}$ 中取商；(18) 保证实际路径积分的类属于左端的自然嵌入。不把单个局部形式系数未经证明称为真实成本。

下一实际 consumer 因而可以先编译 (20)，按真实 $\mathcal R_8$ 原式关系取商，再处理局部积分的路径约束；不必重跑完整长路径的所有 second/third histories。正结论仍须从原式复核；不完备正规化的非零余项仍不能当作非成员定理。

## 8. 已付与未付

已付：完整第三局部势的逐点 $W$ 余项、两层真实历史的全部交叉项、端口常势的准确抵消，以及完整第四成本模 $\mathcal R_8$ 的有限局部积分公式。此结论覆盖两个复相位模式及其共轭、常数项，不只覆盖纯模式。

未付：$\mathscr L_4$ 的商是否为零、零总矩阵约束下的真实局部积分锥、$\mathcal U_4=\mathcal R_8$、实际零第四基准或任意完整 $P_0$ 的抵消。更不能由本稿推出第四逐 $s$ ruling、双 collar、无限阶收敛、有限等距族、闭嵌入、reach 或主课题的宏观运动指标。
