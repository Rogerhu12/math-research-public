# R759 — 原 S34 的 CM13 连接修正与非零 primitive 型五分量

日期：2026-11-15。**状态：已证明。** 本篇在同一原 sigma 规范中支付协变导数穿过完整 CM13 迹的修正，证明该修正在原 S 上是非零的全纯型五截面，并证明原 S 的协变伙伴确有两条已识别曲线线之外的 primitive 三维分量。所有结论由已付来源恒等式作符号推导，不新增数值执行。

这里的“非零”指完整截面。它不代替该截面的原 unit 负一 Mellin 值非零；完整连接项、CM 分支、单位域和原中央行在第 5 节同时保留。

## 1. 原来源、连接与绝对 CM 规范

沿用 [R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、[R728](R728-frozen-type-five-connection-and-complete-near-cancellation.md) 和 [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md) 的规范。

置
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\gamma=4+\omega,\quad \gamma\bar\gamma=13,\quad b=17,
$$
$$
x'=2y,\qquad y^2=x^3+b,\qquad
\sigma=z+\cdots,\quad \zeta=\sigma'/\sigma .
\tag{1}
$$
本篇的连接是准确的原亚纯连接
$$
\nabla_{34}=\partial_z-34\zeta(z),\qquad
\mathcal D(P)=-\frac1{34}\nabla_{34}P
             =\zeta P-\frac1{34}P'.
\tag{2}
$$
没有将其替换成另一个 Gaussian 或拟周期规范，也没有事先假定它与 CM 交换。

令
$$
F_j=b^j\sigma^{34}x^{14-3j},\qquad
\Xi_j=-b^j\sigma^{34}x^{13-3j}y,\quad 0\le j\le4.
\tag{3}
$$
这些分别是原型零零质量空间及整个型五空间的基。原 S 为
$$
S=F_0-\frac{53}{7}F_1-\frac{12}{7}F_2
       -\frac{80}{7}F_3-\frac{128}{7}F_4.
\tag{4}
$$
它首项为 $z^6$，且真实全十三纤维迹满足
$$
M_\gamma=[\gamma]_*[\bar\gamma]^*,\qquad
M_\gamma S=-\gamma S.
\tag{5}
$$
这里不除以 13，不添加另一个 Weil 标量。

R732 已付整个型五空间上的
$$
N_\gamma=\gamma^{-1}M_\gamma,\qquad
\det(T-N_\gamma)=(T+1)(T+\omega^2)(T^3+\omega),\qquad
N_\gamma^{18}=1.
\tag{6}
$$
本文使用的是这个完整算子，包含原两个一次因子和整个三次因子。

## 2. division-log 修正的全纤维定义

原真实 division 多项式是
$$
Q_\gamma(x)
 =\frac{\sigma(\gamma t)}{\sigma(t)^{13}}
 =\gamma\left(
 x^6+(8+12\omega)b x^3+\frac{64+48\omega}{13}b^2
 \right).
\tag{7}
$$
$Q_{\bar\gamma}$ 为其系数共轭。前导因子 $\gamma$ 及 $\bar\gamma$ 都保留。将它们无证首一化，会改变下面原迹的绝对常数。

定义两个实际椭圆函数
$$
R_\gamma(t)=\left(\frac{Q_{\bar\gamma}(x(t))}
                         {Q_\gamma(x(t))}\right)^{34},
$$
$$
\begin{aligned}
b_\gamma(t)
 &=\partial_t\log\frac{Q_{\bar\gamma}(x(t))}{Q_\gamma(x(t))}\\
 &=\bar\gamma\,\zeta(\bar\gamma t)-\gamma\,\zeta(\gamma t)\\
 &=2y(t)\left(
 \frac{\partial_xQ_{\bar\gamma}}{Q_{\bar\gamma}}
 -\frac{\partial_xQ_\gamma}{Q_\gamma}\right)(x(t)).
\end{aligned}
\tag{8}
$$
第二行的两个 $13\zeta(t)$ 准确抵消。因此 $b_\gamma$ 是由同一 division 来源确定的有理函数；它不是任意选择的连接补偿。

若 $P=\sigma^{34}\phi$，令
$$
\mathcal C_\gamma(P)(z)
 =\sigma(z)^{34}
   \operatorname{Tr}_{\gamma t=z}
       \left(R_\gamma(t)b_\gamma(t)\phi(\bar\gamma t)\right).
\tag{9}
$$
该迹在每个非分歧局部图中是全部十三个逆像的和，并按原 sigma frame 延拓。它没有选出单个纤维，也没有把 kernel 点附近的单项极点先行删掉。

同一 frame 中 R297 的真实迹公式正是
$$
M_\gamma P(z)
 =\sigma(z)^{34}
   \operatorname{Tr}_{\gamma t=z}
      \left(R_\gamma(t)\phi(\bar\gamma t)\right).
\tag{10}
$$
公式 (9) 与 (10) 使用完全相同的纤维、半特征和除法多项式比。

## 3. 完整连接—CM 恒等式

在没有极点的局部图中，每一逆像都有 $dt/dz=\gamma^{-1}$，而
$$
R_\gamma'(t)=34b_\gamma(t)R_\gamma(t).
$$
先将 (10) 除以 $\sigma(z)^{34}$，逐项求导，再乘回同一 frame，即得
$$
\boxed{
\nabla_{34}M_\gamma P
 =\frac{\bar\gamma}{\gamma}M_\gamma\nabla_{34}P
  +\frac{34}{\gamma}\mathcal C_\gamma(P).
}
\tag{11}
$$
双方都是同一曲线上的亚纯截面，故 (11) 延拓为全局恒等式。这个证明支付了全部分支，不涉及局部样本拟合。

等价地，
$$
\boxed{
\mathcal D(M_\gamma P)
 =\frac{\bar\gamma}{\gamma}M_\gamma\mathcal D(P)
  -\frac1{\gamma}\mathcal C_\gamma(P).
}
\tag{12}
$$
一般 P 的连接像可能有原点极点，必须保留。例如 $P(0)\ne0$ 时，$\zeta P$ 有简单极点。本篇不将 (11) 无条件解释为两个全纯有限维空间间的算子。

现在取原 S，记
$$
D_S=\mathcal D(S).
$$
S 在每个格点有六阶零，所以 $D_S$ 是真正全纯的标准 degree34 型五截面。由 (5)、(12)，
$$
\boxed{
\mathcal C_\gamma(S)=\bar\gamma M_\gamma D_S+\gamma^2D_S
 =\gamma(\gamma+\bar\gamma N_\gamma)D_S.
}
\tag{13}
$$
于是 (9) 中所有单项可能出现的极点，在完整迹中准确相消；(13) 本身给出该相消的全纯来源证明。

而且 $\mathcal C_\gamma(S)\ne0$。事实上 $D_S$ 的首项是
$$
D_S(z)=\frac{14}{17}z^5+\cdots\ne0.
\tag{14}
$$
若 (13) 为零，则 $N_\gamma D_S=-(\gamma/\bar\gamma)D_S$。但 (6) 的全部特征值为十八次单位根，而 $\gamma/\bar\gamma$ 在素理想 $(\gamma)$ 的赋值为 1，在 $(\bar\gamma)$ 的赋值为 $-1$，不可能为单位根。

更强地，$\gamma+\bar\gamma N_\gamma$ 在整个五维空间上可逆。因此对 (6) 的每个实际谱投影 $\Pi$，
$$
\Pi\mathcal C_\gamma(S)=0
 \quad\Longleftrightarrow\quad
\Pi D_S=0.
\tag{15}
$$
这是固定特征零来源的等价，不声明任一相应 Mellin 泛函保非零，也不声明该逆在未经删坏素的任意整格上为单位。

## 4. 原 D_S 的 primitive 三维分量严格非零

由 $F_j'=34\zeta F_j-2(14-3j)\Xi_j$，
(4) 给出完整坐标
$$
\boxed{
D_S=\frac{14}{17}\Xi_0-\frac{583}{119}\Xi_1
       -\frac{96}{119}\Xi_2-\frac{400}{119}\Xi_3
       -\frac{256}{119}\Xi_4.
}
\tag{16}
$$
R732 的两条首项一特征线，在同一 $(\Xi_0,\ldots,\Xi_4)$ 基中为
$$
D_-=(1,13,-156,-104,64),\qquad
D_\omega=\left(1,-\frac{109}{11},\frac{120}{11},
                       \frac{368}{11},\frac{128}{11}\right).
\tag{17}
$$
取明确的有理线性行
$$
\mathscr L(v)=429v_0+51v_1+7v_2.
\tag{18}
$$
直接代入 (17)，两个值均为零；代入 (16) 则准确得到
$$
\boxed{\mathscr L(D_S)=\frac{11637}{119}\ne0.}
\tag{19}
$$
因此 $D_S$ 不属于两条一次特征线之和。

为明确这是完整谱结论，使用 R732 的原投影
$$
\Pi_6=\frac{N_\gamma^3+\omega}{\omega-1},\qquad
\Pi_{\rm prim}=1-\Pi_6 .
\tag{20}
$$
前者的像就是 (17) 的两线，后者是 $T^3+\omega$ 的整个三维块。由 (19)，
$$
\boxed{
\Pi_{\rm prim}D_S\ne0,\qquad
\Pi_{\rm prim}\mathcal C_\gamma(S)\ne0.
}
\tag{21}
$$
第二式由 (15) 得到。这保留了原 S 经实际连接产生的非算术二线余块；不能把该完整连接源直接放进已付的两条原 rank-one 曲线点空间。

这里“余块”不是指没有算术解释。它的完整坏处角色、可能的 CM 系数域及负一分支仍可另外识别；(21) 没有以型五、零质量或一个 CM 样本替代该识别，也没有假设其解析秩。

## 5. 原 unit 负一 Mellin 与 S 中央同时保留

固定原普通射线、同一周期 $\Omega$，按 R728 使用
$$
\int e^{Yz/\Omega}\,d\nu_F(Y)=F(z),\qquad
\nu_{F'}=(Y/\Omega)\nu_F.
\tag{22}
$$
对有限角色 $\chi$ 定义完整原单位域上的
$$
I_F(\chi,w)=\Omega\int_{Y\ {\rm unit}}
     \chi(Y)Y^{-1}\langle Y\rangle^{d_pw}\,d\nu_F(Y),
$$
$$
J_S(\chi,w)=\int_{Y\ {\rm unit}}
     \chi(Y)\langle Y\rangle^{d_pw}\,d\nu_S(Y).
\tag{23}
$$
对 $\mathcal C_\gamma(S)$ 和 $M_\gamma D_S$，(23) 使用 (9)、(10) 的完整实际来源。不将 CM pull/trace 与单位指示、有限角色或原其他伙伴门无证交换。

令 $H_S=S/\sigma$，则 $H_S$ 是真实全纯 odd degree33 截面，
$$
G_S=\zeta S=\sigma'H_S,\qquad
D_S=G_S-S'/34.
\tag{24}
$$
原有界卷积
$$
\mu_{H_S}=\nu_\sigma(c)\otimes\nu_{H_S}(v),\qquad Y=c+v
$$
给出整个一变量来源
$$
\nu_{D_S}
=Y_*\left(\frac{c-Y/34}{\Omega}\,\mu_{H_S}\right).
\tag{25}
$$
因此
$$
I_{D_S}(\chi,w)=I_{G_S}(\chi,w)-\frac1{34}J_S(\chi,w),
\tag{26}
$$
其中连接项是准确的有理测试
$$
I_{G_S}(\chi,w)=
\int_{\{c+v\ {\rm unit}\}}
   \frac{c}{c+v}\,
   \chi(c+v)\langle c+v\rangle^{d_pw}\,d\mu_{H_S}.
\tag{27}
$$
原两输入深浅和近消部分没有从 (27) 中删掉。若另加 mixed cut，必须在 (25) 的完整来源中保留该 cut；不能在忘却伙伴后再把新门解释成裸 $D_S$。

由 (13)、(26)，对整个 Mellin 变量准确有
$$
\boxed{
I_{\mathcal C_\gamma(S)}(\chi,w)
 =\bar\gamma I_{M_\gamma D_S}(\chi,w)
   +\gamma^2I_{G_S}(\chi,w)
   -\frac{\gamma^2}{34}J_S(\chi,w).
}
\tag{28}
$$
特别在原平凡 tame 分支，
$J_S(1,0)=0$，所以零权处
$$
I_{\mathcal C_\gamma(S)}(1,0)
 =\bar\gamma I_{M_\gamma D_S}(1,0)
   +\gamma^2I_{G_S}(1,0).
\tag{29}
$$
完整中央导数则是
$$
\boxed{
I_{\mathcal C_\gamma(S)}'(1,0)
 -\bar\gamma I_{M_\gamma D_S}'(1,0)
 -\gamma^2I_{G_S}'(1,0)
 =-\frac{\gamma^2}{34}J_S'(1,0).
}
\tag{30}
$$
这里的撇号只对 $w$ 求导。若原 $J_S'(1,0)=0$，所得正是 (30) 左边的完整相消，不是把其任一单项或 (21) 的某个负一值赋零。

## 6. 对实际 raising/connection 接口的范围

原 physical shear 的 first jet 读 first-Y 型五、partner 型一的 off-diagonal 块；见 [原剪切 note](../notes/2026-11-15-actual-central-shear-and-fixed-representation-gate.md) 附录 A。若试图用 (2) 把该块与原型零 toric 来源相接，(11) 是必须一起运输的真实 CM 修正。

(13)、(21) 证明修正不能在原 S 上省略，并且它保有完整 primitive 三维分量。(28)–(30) 给出在同一原单位测试下能够合法代回的中央关系。任何进一步的固定表示平方、双线性 period 或 point-log 公式，都还必须识别这些实际分量的全角色、周期和原 mixed gate；不能由连接同型或截面非零跳过这些条件。

本篇没有增加第三个中央零假设，没有把 $I_{\mathcal C_\gamma(S)}$ 或 $I_{D_S}$ 认作已知非零，也没有把 R732 的有限矩阵投影直接穿过未运输的原 W/E 门。新增结论是原 S 的完整 CM–connection 恒等式、不可删除的全纯修正，以及该实际修正所携带的非零 primitive 分量。
