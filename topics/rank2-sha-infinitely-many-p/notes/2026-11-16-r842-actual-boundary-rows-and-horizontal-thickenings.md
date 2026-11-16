# 原 R842 指定两行的完整边界读取与水平厚化条件

日期：2026-11-16。**状态：下列同源边界恒等式、两水平完整系数式和十九角运输已证明；原联合延拓的剩余类是否为零仍未判定。**

接 [R842](../results/R842-original-gres-double-ramification-transpose-and-joint-prefix-extension.md)、
[第一层满射及实际受限类](2026-11-16-r842-first-layer-surjectivity-and-actual-restricted-class.md)
和 [R822](../results/R822-original-cartier-residue-descent-and-actual-ramification-trace.md)。
本注把其指定 $\lambda_0,\lambda_1$ 的剩余类写成原全部边界与同一个原点项；
再给能逐系数读取的真实公式。
没有用一个局部系数非零代替该全局类非零，也没有把因子倍来源的边界消去搬到一般来源。

## 1. 同一个提升及完整边界类

沿 R842，令
$$
C=(F=0),\quad P=(0,1),\quad
N=\mathcal O_C(C),\quad e=\mathcal EF,\quad f_2=\mathcal E^2F,
\quad \mathcal E=Y\partial_Y,\quad Z=(e|_C),
$$
$$
\mathscr V_T=H^0(C,N^3(-TP)),\qquad
\mathcal Q_T=H^0(C,\omega_CN^{-1}(TP)),
\qquad T>2\kappa,\quad\kappa=C^2.
\tag{1}
$$
物理窗口为 $T=s-r-13$；长相对窗口如另行使用则为 $T=s-r$。
原 $q=q_{\rm src}$、$t^r\mathcal H_3$ 返回、全部低行高尾及十三行带不变。

第一层满射允许选取同一个真正
$\omega_1\in\mathcal Q_T$，使其在 $Z$ 上等于 $\lambda_1$ 的第一层。
于是唯一的 $\nu_0\in\mathscr Z^\vee$ 由
$$
\iota^\vee\nu_0=e\nu_0
=\mathrm{res}_{2Z}\omega_1-\lambda_1
\tag{2}
$$
定义。记这个选择对应的实际泛函为
$$
b_0=j_T^\vee(\lambda_0-\mathfrak d^\vee\nu_0)
\quad\text{于 }\mathscr V_T.
\tag{3}
$$
更改 $\omega_1$ 的允许范围及 $[b_0]$ 的商已由第一层注支付；
本注不扩大它。

对 $V_0\in\mathscr V_T$，取原
$G_V\in\mathcal H_3$ 满足 $G_V|_C=V_0$，并置
$$
V_1=(\mathcal EG_V)|_C,\qquad R_V=qt^rG_V.
$$
这里的 $G_V$ 不是原物理单位 $G_0=w^{13}U_0$。
$V_1$ 不被额外假定有 $T$ 阶前缀。

由 R842 的同一个有限配对和全局留数，准确有
$$
\boxed{
b_0(V_0)=
\mathfrak G_F(R_V)
+\operatorname{Res}_P\frac{V_1\omega_1}{e^2}.
}
\tag{4}
$$
确实，(2) 给
$$
\langle D_3V_0,\nu_0\rangle
=\sum_{Z}\operatorname{Res}^C
\frac{V_1(\omega_1-\lambda_1)}{e^2}.
$$
将它代入 (3)，前两项是原 $\mathfrak G_F(R_V)$。
余下 $V_1\omega_1/e^2$ 是真正全局对偶化微分，
仅在 $Z$ 和 $P$ 可能不正则，故得到 (4)。
所有奇点处均取全部正规化分支与剩余域迹，使用同一个 conductor 下降条件。
若改提升 $G_V\mapsto G_V+FH$，则 $V_1$ 改为 $V_1+eH$。
(2) 的第一层相同使其有限差可用 $\omega_1$ 代 $\lambda_1$；
再对 $H\omega_1/e$ 使用同一全局留数，(4) 的总差准确为零。
所以这里没有通过选择提升改变边界行。

R822 的原全局式对这个实际 $R_V$ 给
$$
\boxed{
b_0(V_0)=
-\mathfrak B_F(R_V)
+\operatorname{Res}_P
\left(\frac{V_1\omega_1}{e^2}-\Xi_{R_V}\right).
}
\tag{5}
$$
这正是所需的全部边界读取。
(5) 的 $P$ 项沿原曲线分支 $Y=\psi(t)$，
不是沿实际 theta 轴 $g=\psi e^\eta$；
两者的 $\eta\mathcal E^2G_V$ 差不能在 $\omega_1$ 的极前删除。
任意本节 $G_V$ 的 $\operatorname{Res}_P\Xi_{R_V}$ 也不能代成
仅对原指定 forcing 已付的 $\gamma/6$。

## 2. 指定 GRes 的完整有理主部

以下所有 $F_t$、$F_{tt}$ 都是在固定原 $Y$ 下的偏导数。
置
$$
W=W_s=t^{r+1-s}(1-t)^{3s},\qquad
c_s=\frac{3(-1)^s}{17},
$$
$$
\Omega_C=\frac{dY}{YF_t}=-\frac{dt}{e},\qquad
H=WF_t^2,\qquad A=Hf_2-e\mathcal EH.
$$
在原函数域上有精确恒等式
$$
\boxed{
\frac{A\Omega_C}{e^2}
=-d\left(\frac{WF_t}{e}\right)
+\frac{W'F_t+WF_{tt}}e\,dt.
}
\tag{6}
$$
证明只用
$$
dY=-\frac{YF_t}{e}\,dt,\qquad
de=\left(\mathcal EF_t-\frac{f_2F_t}{e}\right)dt.
$$
展开右边后，其两项 $WF_t\mathcal EF_t/e^2$ 相加，
与 $A=WF_t^2f_2-2eWF_t\mathcal EF_t$ 及
$\Omega_C=-dt/e$ 完全吻合。
它是有理微分恒等式，在分母零点仍按同一亚纯微分解释。

对任何本注实际 $R$，定义
$$
X_R=(\mathcal ER)|_C,\qquad
\mathcal D_R=
c_sX_R
\left[
-d\left(\frac{WF_t}{e}\right)
+\frac{W'F_t+WF_{tt}}e\,dt
\right].
\tag{7}
$$
由 R842 的原转置，
$$
\sum_{Z^\circ}\operatorname{Res}\mathcal D_R
=\mathfrak G_F(R).
\tag{8}
$$
$Z^\circ$ 仍只含原非固定仿射分歧概形。
第二项在这个开集的原对偶化层中正则；
即使奇点正规化上出现 conductor 极，其全部分支残数和为零。
所以也可在这个开集写
$$
\mathfrak G_F(R)
=c_s\sum_{Z^\circ}\operatorname{Res}
\frac{WF_t}{e}\,dX_R.
\tag{9}
$$
(9) 只在指定开集删正则项，不能把 (7) 的第二项从全局边界删去。
特别 $R=qt^rG_V$ 时，$dX_R$ 保 $d(t^rq)$ 和其余全部余因子导数。

记 $\mathfrak B_{\mathcal D}(R)$ 为 (7) 在 $P$、$Z^\circ$ 之外的
全部分支残数和。非固定、非分歧的原仿射点没有额外残数；
其它位置包括两个水平、六个底纤维、全部十九角及边界奇点。
则 (4) 等价于
$$
\boxed{
b_0(V_0)=
-\mathfrak B_{\mathcal D}(R_V)
+\operatorname{Res}_P
\left(\frac{V_1\omega_1}{e^2}-\mathcal D_{R_V}\right).
}
\tag{10}
$$
这没有将两个不同的边界代表相认。它们的准确补偿为
$$
\boxed{
\mathfrak B_F(R_V)
=\mathfrak B_{\mathcal D}(R_V)
+\operatorname{Res}_P(\mathcal D_{R_V}-\Xi_{R_V}).
}
\tag{11}
$$
故可用后面的系数式实际读取 (10)，也可用 (11) 返回原 (5)。

另有
$$
\frac{W'}W=\frac{r+1-s}{t}-\frac{3s}{1-t}
=\frac{r+5/6}{t}-\frac1{2(1-t)}
\quad\text{于特征 }p=6s-1.
\tag{12}
$$
(12) 只化简导数；原 $W$ 自身仍须完整保留。

## 3. 非固定负水平：一般来源出现真实加权值

先取 $Y=0$ 上不在六个固定底纤维的光滑点 $Q$，并假设
$F_t(Q)\ne0$。令 $x=Y$，原曲线为 $t=t(x)$。
设 $m=\operatorname{ord}_Q(t-t(Q))<p$，则
$$
F_Y(t(x),x)=x^{m-1}v(x),\qquad v(0)\ne0.
$$
定义
$$
J(t,x)=q(t,x)G_V(t,x),\quad
A_-(x)=\frac{W(t(x))F_t(t(x),x)}{v(x)},\quad
K_-(x)=W'(t(x))+W(t(x))\frac{F_{tt}}{F_t}(t(x),x).
$$
$A_-$、$K_-$ 正则。原 $X_{R_V}$ 是
$t(x)^r x\,\partial_xJ(t(x),x)$，偏导保持固定 $t$。
由 (7) 得完整读取
$$
\boxed{
\operatorname{Res}_Q\mathcal D_{R_V}
=-c_s[x^{m-1}]
\left\{
t(x)^r\,\partial_xJ(t(x),x)
\bigl(xA_-'(x)-mA_-(x)\bigr)
\right\}.
}
\tag{13}
$$
这里 prime 是沿 $C$ 的全导数，
而 $\partial_xJ$ 是原固定 $t$ 偏导，二者不可互换。
$K_-$ 项为正则微分，故此处确实没有残数。
(13) 保全部 $m$ 阶分歧与同一个来源的高尾。

特别当 $F_t(Q)F_Y(Q)\ne0$，即 $m=1$，且
$q=Y\widetilde q$ 时，
$$
\boxed{
\operatorname{Res}_Q\mathcal D_{R_V}
=c_s\,t(Q)^rW(Q)\,
\frac{F_t(Q)}{F_Y(Q)}
\,\widetilde q(Q)\,G_V(Q).
}
\tag{14}
$$
符号为正：$WF_t/e$ 的首项是
$(WF_t/F_Y)(Q)x^{-1}$，其负微分的首项为正的 $x^{-2}dx$。

这项不能沿用旧因子倍来源的消去。
旧 $\Delta R=qt^rFH$ 在 $C$ 上的 $G_V=FH$ 为零，
因此其对应值为零；一般 $G_V\in\mathcal H_3$ 没有这个性质。

在 R792 的原 $r=2$ 分类中：

- $q(t,0)\ne0$ 时，$F(t,0)=\lambda d^c$，不存在本节非固定移动点。
- $q(t,0)=0$ 时，$q=Y\widetilde q$，
  $F(t,0)=\lambda d^cH_0$、$\deg H_0\le2$。
  (14) 是这些实际简单横截移动点的加权值。
- 若 $\deg H_0=2$，原
  $\lambda^3d^{3c}\widetilde q(t,0)=A_1$ 为非零常数。
  因此在 $H_0$ 的简单根且 $F_Y(Q)\ne0$ 时，
  (14) 中除 $G_V(Q)$ 外的各因子都是单位。
  这没有证明其加权总和或 $G_V(Q)$ 非零。
- 多重分歧使用 (13)，奇点则使用第6节，
  不能将其都改成一个约化值。

特别，原相对 Euler 在 $H_-$ 的权为零，
所以兼容对确有 $V_1|_{Z_-}=0$；
若第二值实现，也有 $V_2|_{Z_-}=0$。
这并不迫使 (14) 所读取的 $V_0|_{Z_-}$ 为零。
更细的
$\mathcal E^2G_V-\mathcal EG_V=Y^2(G_V)_{YY}$
是相对于 $2H_-$ 的同源关系；
只有在本节 $F_Y$ 单位情形才可对应这个局部 $2Z$ 因子，
不能换成全 $2Z$ 恒等式。

## 4. 非固定正水平的全长系数

取 $Q\in C\cap(Y=\infty)$，仍不在固定底纤维，
并在原正水平图取
$$
x=Y^{-1},\quad f(t,x)=x^bF(t,x^{-1}),\quad
\widehat q=x^c q,\quad \widehat G=x^{3b}G_V,
\qquad c=\deg_Yq,\quad N_*=3b+c.
$$
这些函数在该图正则；低于最大次数的列保其额外 $x$ 零。
假设 $f_t(Q)\ne0$，令
$$
f_x(t(x),x)=x^{m-1}v(x),\quad
m=\operatorname{ord}_Q(t-t(Q))<p,
$$
$$
J_+=\widehat q\,\widehat G,\qquad
L_{N_*}J_+=(N_*-x\partial_x)J_+,
$$
$$
A_+(x)=\frac{W(t(x))f_t(t(x),x)}{v(x)},\qquad
K_+(x)=W'(t(x))+W(t(x))\frac{f_{tt}}{f_t}(t(x),x).
$$
原物理 Euler 逐项给
$$
X_{R_V}=t(x)^r x^{-N_*}
(L_{N_*}J_+)(t(x),x).
$$
并且
$$
\frac{WF_t}{e}=-x^{-m}A_+,\qquad
\frac{W'F_t+WF_{tt}}e\,dt=\frac{K_+}{x}\,dx.
$$
故完整残数为
$$
\boxed{
\begin{aligned}
\operatorname{Res}_Q\mathcal D_{R_V}
=c_s\bigg\{&
[x^{N_*+m}]
\left[t(x)^r(L_{N_*}J_+)
 \bigl(xA_+'-mA_+\bigr)\right]\\
&+[x^{N_*}]
\left[t(x)^r(L_{N_*}J_+)K_+\right]\bigg\}.
\end{aligned}
}
\tag{15}
$$
两个项都需要保留。
即使 $m=1$，第一项仍可读到 $N_*+1$，不能只读最高 $Y$ 系数的值。
$L_{N_*}$ 中的偏导仍在固定 $t$ 下；
若改用沿曲线导数，必须加回
$x\,t'(x)\partial_tJ_+$ 的完整项。
这些局部高 jet 来自同一个原 $G_V$，不是自由的边界变量。

## 5. 十九角的全部实际运输

(7) 本身可在所有真框直接代入。以下给具体式，避免把
$F_t$ 错当成吹起后保持同一坐标的偏导。

### 5.1 全部有限链

写
$$
t=t_i+x^jz,\qquad Y=x^\epsilon,\qquad
\epsilon=-1\text{ 于负链},\quad
\epsilon=1\text{ 于正链},
$$
$$
F=x^\mu f(x,z),\qquad
D=\epsilon(x\partial_x-jz\partial_z),\qquad
a=\epsilon\mu,\qquad e_U=(D+a)f.
$$
负链 $\mu=V_j-b$，正链 $\mu=V_j$。
于是
$$
F_t=x^{\mu-j}f_z,\qquad
F_{tt}=x^{\mu-2j}f_{zz},\qquad
e=x^\mu e_U.
\tag{16}
$$
这是原固定 $Y$ 偏导的准确运输。
在 $f_z$ 单位的曲线图中可用 $x$ 作参数，
且
$$
dt=-\epsilon\,x^{j-1}\frac{e_U}{f_z}\,dx.
$$
因此
$$
\boxed{
\mathcal D_R
=c_sX_R\left[
-d\left(Wx^{-j}\frac{f_z}{e_U}\right)
-\epsilon\left(\frac{W'}x+
 Wx^{-j-1}\frac{f_{zz}}{f_z}\right)dx
\right].
}
\tag{17}
$$
三个四步负链、一个三步负链及有限两步正链全部由 (17) 包括。
$j=0$ 同时给两个未吹起水平图和有限底纤维的相应图。
$e_U$ 可能在边界为零，(17) 保其实际分歧极。
$f_z$ 非单位时不用这一约简，而使用 (7)、(16) 后在正规化逐支展开。

若实际物理 $R=x^\rho R_U$，其 Euler 输出必须取
$$
X_R=x^\rho(D+\epsilon\rho)R_U\big|_C.
\tag{18}
$$
没有把 $q$ 的 Euler 权或各原系数帽从 $X_R$ 中删去。

### 5.2 底无穷远的两步链

先取 $T=1/t,\ Z=t^4Y$，
$u_F=\max_i(\deg_tF_i-4i)$，
再取
$$
T=x^jz,\qquad Z=x,\qquad
F=T^{-u_F}x^{V_j}f(x,z),\quad j=1,2.
$$
置
$$
D=x\partial_x-jz\partial_z,\quad
e_U=(D+V_j)f,\quad
L=4x\partial_x-(4j+1)z\partial_z,\quad a_\infty=u_F+4V_j,
$$
$$
A_1=(L+a_\infty)f,\qquad
A_2=(L+a_\infty-1)(L+a_\infty)f.
$$
因为原固定 $Y$ 的 $t\partial_t$ 是
$-T\partial_T+4Z\partial_Z$，准确得到
$$
\boxed{
\frac{F_t}{e}=\frac{TA_1}{e_U},\qquad
\frac{F_{tt}}e=\frac{T^2A_2}{e_U}.
}
\tag{19}
$$
在 $f_z$ 单位图，
$$
dt=T^{-2}x^{j-1}\frac{e_U}{f_z}\,dx,
$$
故
$$
\boxed{
\mathcal D_R=c_sX_R\left[
-d\left(\frac{WTA_1}{e_U}\right)
+\left(\frac{W'A_1}{xz f_z}
 +\frac{Wx^{j-1}A_2}{f_z}\right)dx
\right].
}
\tag{20}
$$
两个零阶项 $a_\infty$ 和 $a_\infty-1$ 都是原微分运输的一部分。
不把 $\partial_t$ 换成只作用 $z$ 的导数。
若物理 $R=T^{-u_R}x^\rho R_U$，
则 $T$ 的 Euler 权为零，
$X_R=T^{-u_R}x^\rho(D+\rho)R_U|_C$。
其它交叠图用 (7) 的同一个有理微分运输；
没有额外选择一个边界来源。

## 6. 分歧和 conductor 与水平值必须分开

第3–4节的简式假设局部曲线光滑、所示 $F_t$ 或 $f_t$ 为单位。
它们不覆盖奇点，也不把高分歧改成横截值。

对任意边界点，使用 (7)、(16) 或 (19) 的原有理表达，
在每个正规化分支的一个实际局部参数 $v$ 中读取
$[v^{-1}](\mathcal D_R/dv)$，再作全部剩余域迹。
所有出现的函数来自同一个 $F,q,G_V$。
有限 pole cap 决定所需的 Laurent 截断；不存在可以另选的 jet。

检验 $\omega_0,\omega_1$ 是否为真正全局截面时，
则须使用不同但同样完整的下降条件。
在一个原局部单位二形式框 $\Omega_U$ 中写
$$
\Omega_{\log}=g_U\Omega_U,\qquad
\omega_i=B_i\Omega_{\log}|_C.
$$
准确要求 $g_UB_i\in\mathcal O_{C,Q}$，只在 $P$ 允许 $T$ 阶极。
有限链的 $g_U$ 为单位乘 $x^{j-1}$；
无穷远链为单位乘 $x^{-j-1}z^{-2}$，
两个水平为单位乘 $x^{-1}$，无穷远严格纤维另保 $T^{-2}$。
这与 R842 的完整 canonical 除子相同。

若 $C$ 在 $Q$ 奇异，先在全部正规化分支检查
$g_UB_i$ 正则，然后还要其模 conductor 的向量来自
$$
\mathcal O_{C,Q}/\mathfrak f_Q
\subset\widetilde{\mathcal O}_{C,Q}/\mathfrak f_Q.
\tag{21}
$$
仅各支阶非负不能代替 (21)。
普通微分经伴随同构可有 conductor 极；
不能将它们各支的残数分别赋零。

## 7. 固定补零支对同一两微分的真实限制

$\lambda_0,\lambda_1$ 在 $2(Z\setminus Z^\circ)$ 为零。
因此在一个真实单位框中，必须有同一个 $\nu$ 满足
$$
w_1=e_U\nu\pmod{e_U^2},\qquad
w_0=-\nu f_{2,U}
+e_U\bigl(D\nu+(c-a)\nu\bigr)\pmod{e_U^2},
\tag{22}
$$
其中 $w_i$ 是 $\omega_i$ 的真实系数，
$f_{2,U}=(D+a)e_U$，
$c$ 由 $\mathcal L_D\Omega_U=c\Omega_U$ 定义。
分母、单位框和 conductor 全按第6节。
这里的 $\nu$ 是原全有限向量的一部分，不能逐边界重选。

在不经过吹起中心的横截水平点，
即 $F_t,F_Y$ 或 $f_t,f_x$ 都为单位时，
(22) 可化成两个明确的厚化条件：

| 真边界 | 同一 $w_0,w_1$ 的必要且充分局部条件 |
|---|---|
| $Y=0$ | $w_1\in(e_U)$ 且 $w_0=0\bmod e_U^2$ |
| $Y=\infty$ | $w_1\in(e_U)$ 且 $w_0+3b\,w_1=0\bmod e_U^2$ |

证明如下。
在 $Y=0$ 的单位框中，$D=x\partial_x,a=0,c=1$，
$e_U=xf_x$，
$$
\mathfrak d^\vee\nu
=x^2(\nu f_{xx}-f_x\partial_x\nu)=0\bmod e_U^2.
$$
在 $Y=\infty$，$D=-x\partial_x,a=b,c=-1$，
$e_U=-xf_x$ 于 $C$，并有
$f_{2,U}=(2b-1)e_U+O(x^2)$。
于是 $\mathfrak d^\vee\nu=3b\,e_U\nu\bmod e_U^2$。
这正给上表。
其中 $3b$ 是原 $\mathcal H_3$ 的真框权，不是物理余因子 $q$ 的次数。

高分歧、非约化角或奇点必须回到 (22)，
不能把上表扩为全 $2Z$ 的公式。
尤其不允许先将 $w_1/e_U$ 视作任意有理函数，
再对不相容的 ambient 提升作裸 $D$ 微分；
R842 已付的 lift 独立性必须在同一个 $(F,e_U)$ 商中使用。

## 8. 当前得到的实际检验范围

(5) 或完全等价的 (10) 是原剩余类 $b_0$ 的全部同源边界式。
(13)–(20) 给其两个水平、全部有限链及无穷远链的指定系数读数；
(21)–(22) 保真正全局延拓的 conductor 和固定补零条件。

若再限制到 R842 的兼容高前缀对，$V_0,V_1$ 都有 $T$ 阶，
则原 (7) 在 $P$ 的阶至少
$$
2r+1-s+T=r-12
\quad(T=s-r-13).
\tag{23}
$$
所以 $r\ge12$ 时这个代表的 $P$ 残数为零。
这只是一项局部消去：
(10) 的另一个 $P$ 项、全部边界和同一 $\omega_1$ 仍须保留。
对定义于整个 $\mathscr V_T$ 的 $b_0$，
其提升的 $V_1$ 没有这个前缀，不能预用 (23)。

本注尚未证明这些实际边界可以由同一 $\omega_0,\omega_1$ 全部支付，
也未证明它们不相容。
新的横截负水平行 (14) 只是一个真实分量；
它与正水平高 jet、所有固定纤维及 (10) 的原点项可能补偿。
原三长核还是兼容高前缀对的更小受限子空间，
全部第二法向值、同一个 $cF^3$ 尾、第四短块和原 $\mathcal W_D$ 余列仍在。

没有新中央零，没有改 $q$ 或 $R$，
也没有将 $b_0$ 的任一局部单位当作主目标的非零证明。


## 9. 原全 $\mathcal H_3$ 来源的整 $t=1$ 纤维消去

本节使用原曲线的两个非恒定投影都为驯分歧的范围。
这由原次数门
$$
a=\deg_tF<p,\qquad b=\deg_YF<p
$$
保证：每个投影的非零分歧指数小于 $p$。
仍取同一 $R_V=qt^rG_V$，其中 $G_V\in\mathcal H_3$；
不要求 $G_V$ 为 $F$ 的倍数，不增加其前缀。
记
$$
c=\deg_Yq,\qquad N_*=3b+c,\qquad
h_1=\operatorname{ord}_{t=1}F_b(t),
\quad F_b(t)=[Y^b]F.
\tag{24}
$$
原 $q$ 仅有 $d$ 分母，而 $d(1)=9$ 是单位，故在此整纤维正则。

**整纤维结论。** 若
$$
\boxed{3s>(N_*+1)h_1,}
\tag{25}
$$
则 (7) 的 $\mathcal D_{R_V}$ 在整个 $t=1$ 纤维的全部边界残数和为零。
这里包括两个原水平、全部三步吹起链和每个奇点的全部正规化分支。
这是对同一个原 $q$ 和每个 $G_V\in\mathcal H_3$ 的结论。
若 $h_1=0$，没有 $Y=\infty$ 的点位于该纤维，(25) 自动满足。

证明分开处理两个真实项。逐正规化分支作一次有理分部，
$$
\operatorname{Res}\mathcal D_{R_V}
=c_s\operatorname{Res}
\left\{
\frac{WF_t}{e}\,dX_{R_V}
+
X_{R_V}\frac{W'F_t+WF_{tt}}e\,dt
\right\}.
\tag{26}
$$
这只使用一个全导数的残数为零，两个剩余项仍全部保留。

先取有限 $Y$ 的点。此处 $R_V$ 正则，
$X_{R_V}=Y\partial_YR_V$ 正则且可被 $Y$ 整除。
在正规化参数 $v$ 中，记
$m_t=\operatorname{ord}_v(t-1)$。
由
$$
\frac{F_t}{e}=-\frac{dY/Y}{dt}
\tag{27}
$$
可知：在 $Y$ 为单位的分支上，其阶至少 $1-m_t$；
在 $Y=0$ 的分支上，其阶为 $-m_t$。
后者 $dX_{R_V}$ 的阶至少 $\operatorname{ord}_vY-1$。
$W$ 的阶为 $3s\,m_t$，所以 (26) 第一项在每个有限分支正则。

(26) 的第二项可写成
$$
\frac{X_{R_V}}Y\,(W'F_t+WF_{tt})\,\frac{dt}{F_Y}.
\tag{28}
$$
其系数在原平面曲线的局部环正则，
而 $dt/F_Y$ 是该平面完整交的对偶化生成元。
所以此项属于原对偶化层：光滑点残数零，
奇点的全部正规化分支残数和为零。
这里没有把各奇点分支残数分别设为零。

再取 $Y=\infty$ 的点，令
$$
x=Y^{-1},\qquad f=x^bF,\qquad
J_+=x^{N_*}qG_V,\qquad
H_{N_*}=(N_*-x\partial_x)J_+ .
$$
$J_+$ 和 $H_{N_*}$ 在原图正则，且
$X_{R_V}=t^rx^{-N_*}H_{N_*}$。
在这个原平面曲线的局部环，
$$
f(t,0)=F_b(t)=(t-1)^{h_1}a_1(t),\qquad a_1(1)\ne0,
$$
以及 $f=0$ 给出真正的环内整除
$$
\boxed{(t-1)^{h_1}\in (x)\subset\mathcal O_{C,Q}.}
\tag{29}
$$
这比逐正规化支的阶不等式更强，因而保留 conductor 下降。

由 (25)，整数指数满足
$3s-1\ge(N_*+1)h_1$。
于是 $W/x^{N_*+1}$ 和 $W'/x^{N_*+1}$
都在该原局部环正则。
(26) 第二项现在是
$$
-t^rx^{-N_*-1}H_{N_*}
(W'f_t+Wf_{tt})\,\frac{dt}{f_x}.
\tag{30}
$$
其系数正则，故再次属于原对偶化层；
其全部分支残数和准确为零。

对第一项，记
$m_x=\operatorname{ord}_v x$。
(29) 给 $m_x\le h_1m_t$。
因为 $m_x,m_t<p$，(27) 在 $Y=x^{-1}$ 时的阶为 $-m_t$；
又有
$\operatorname{ord}_v(dX_{R_V})\ge-N_*m_x-1$。
所以
$$
\begin{aligned}
\operatorname{ord}_v\left(\frac{WF_t}{e}\,dX_{R_V}\right)
&\ge(3s-1)m_t-N_*m_x-1\\
&\ge(3s-1-N_*h_1)m_t-1\\
&\ge h_1m_t-1\ge0.
\end{aligned}
\tag{31}
$$
它在每支正则。吹起不改变这些正规化分支及其残数，
故整条三步链和 conductor 残数已一起处理，(25) 得证。

本条件也有一个直接可检查的原来源充分门。
由原完整返回
$$
3a+r+\deg_tQ\le M_D,\quad N_*\le D,\quad h_1\le a,
\qquad q=d^{-C_D}Q,
$$
可用
$$
\boxed{9s>(D+1)(M_D-r-\deg_tQ)}
\tag{32}
$$
推出 (25)。
(32) 是充分条件，不是在所有现有窗口上自动成立的假设。
没有用渐近主项替代这一实际有限不等式。

## 10. $h_7$ 纤维的有限 $Y$ 部分无条件消去

本节使用当前 R842 继承的真实三次幂来源
$$
t^rF^3q\in\mathcal W_D,
\tag{33}
$$
不是只使用一般的 $qt^r\mathcal H_3$ 包含。
设 $\alpha$ 为原 $h_7$ 的任一根。
它不在 $0,1,d=0$ 上，所有分母在此为单位；
如 $\alpha$ 不在基域，以下先在其剩余域证明，再作原剩余域迹。

原 $\mathcal W_D$ 的第 $n$ 个 charge 列含
$$
h_7^{A_n},\qquad A_n=\left\lfloor\frac{n+1}{4}\right\rfloor.
$$
所以将 (33) 在 $t=\alpha$ 特化，其非零 $Y$ 次数至多为 $2$。
$F$ 原始且定义当前非垂直不可约曲线，故 $F(\alpha,Y)$ 不恒零。
由此有精确二择：

- 若 $q(\alpha,Y)\ne0$，则
  $3\deg_YF(\alpha,Y)+\deg_Yq(\alpha,Y)\le2$。
  因而 $F(\alpha,Y)$ 是非零常数，此纤维没有有限 $Y$ 曲线点。
- 若 $q(\alpha,Y)=0$，则在同一原局部多项式环
  $q\in(t-\alpha)$。
  对每个当前 $G_V$，
  $X_{R_V}=\mathcal E(qt^rG_V)$ 同时含 $t-\alpha$ 和 $Y$。

第二种情形中，(26) 可继续逐原分支使用。
$W,W'$ 在此正则且 $W$ 为单位。
在 $Y$ 为单位的分支，
$\operatorname{ord}(F_t/e)\ge1-m_t$、
$\operatorname{ord}dX_{R_V}\ge m_t-1$，
所以第一项正则。
在 $Y=0$ 的分支，记 $m_Y=\operatorname{ord}Y$，
则
$$
\operatorname{ord}(F_t/e)=-m_t,\qquad
\operatorname{ord}dX_{R_V}\ge m_t+m_Y-1,
$$
第一项仍正则。
第二项仍有 (28) 的形式，其系数在原局部环正则，
故每个原有限点的全部 conductor 分支残数和为零。

因此得到同源完整消去
$$
\boxed{
\sum_{\substack{Q\text{ 在 }t=\alpha\\Y(Q)\ne\infty}}
\operatorname{Res}_Q\mathcal D_{R_V}=0
\qquad(\alpha\mid h_7),
}
\tag{34}
$$
对同一个原 $q$ 和所有 $G_V\in\mathcal H_3$ 成立。
这里不要求 $G_V=FH$，也没有高前缀或额外长窗口条件。

(34) **不包括** $h_7$ 纤维在 $Y=\infty$ 的点及其四步链。
它也不删去第4节的其它移动正水平。
这些部分仍用 (15)、(17) 和全部 conductor 条件。

最后，(25)、(34) 删除的是 (10) 的
$\mathfrak B_{\mathcal D}$ 中相应的整块；
(11) 的原 $P$ 点补偿逐字保留。
它们没有声称 $\Xi_R$ 与 $\mathcal D_R$ 在每个固定纤维分别有相同残数，
也没有直接将原 $\mathfrak B_F$ 的同名子和设零。
原剩余类仍是同一个 (5)/(10)，全部未消边界和同一 $\omega_1$ 未变。
