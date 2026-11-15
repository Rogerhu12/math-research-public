# R301：完整 self 的五维平移轮廓、有限多包真实联调与兼容边界

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、秩计算、人工检查或科学运行。**

[R298](R298-zero-platform-matrix-with-nonzero-self-response-and-ten-observation-control.md) 已用一个完整响应支付固定单个 profile 的 self 数值。本稿把它扩成一个准确的五维完整平移轮廓：对任意先选定的非零真实紧母包，五个明确的 pure-zero、三矩矩阵零响应，在母包的所有允许平移上恰给全部四次以下多项式。这里控制的是完整 self，包含全部原右尾及低阶余项，不只是最高 profile jet 符号。

因此，任意不超过五个不同中心、同母同宽的真实包，其 self 值可与整 universal pure、整个九维平台矩阵真实同时指定。对更多包，本稿给这五维响应模块的准确插值兼容条件，不把五个方向冒成整个响应空间，也不把换母包后的同一结论冒成旧几何仍然有效。

## 1. 真实观测和固定母包

沿用真实成本空间 U、完整响应空间 $\mathcal R$、pure 投影 $\pi$。令

$$
\mathcal R_{\mathrm p0}=\mathcal R\cap\ker\pi.
$$

采用 [R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md) 的全 U 线性矩阵查询

$$
\mathsf T:U\longrightarrow\operatorname{Mat}_3(\mathbb R).
\tag{1}
$$

它在真实 R292 几何上正好等于原二阶 history 构造的三矩型，而不是另外指定的九个参数。

对任意固定真实紧 profile u，定义

$$
\mathfrak q_u(V)
=\frac14[x^2]_{\rm left}V(u\odot u,0).
\tag{2}
$$

这是同一右锚原函数在共同左 collar 的真实二次系数。式 (2) 在整个 U 上线性有定义；在 R292 的 actual whole-pure 零背景上，它就是该文的单包自 history $q_B(u)$。

固定非零实光滑紧母包 u。对允许中心 c 置

$$
u_c(x)=u(x-c).
\tag{3}
$$

所有允许平移的支撑都位于一个共同合法 I 内，并与左右 collar 留正距离。共同右锚始终是同一个 $r_*$。若要把这些查询同时用作某个实际圆中的微包，还须按原圆构造保持其支撑不交；下面的代数行列式只要求中心互异，不替代这项几何条件。

同宽包括任意先固定的正宽度：可以先把该宽度吸收到 u 的定义。不同宽度、不同母形不能未经证明直接套用本稿的 Vandermonde 矩阵。

## 2. 五条原二次方向及完整平移链

采用 [R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md) 的原二次算子记号

$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U_1=\Phi_{s_1},
\quad V_1=\Phi_{p_1},\quad T_1=\Phi_{t_1},\quad E_+=\Phi_{p_2}.
$$

此处 $U_1,V_1,T_1$ 是二次算子，不是成本空间 U、成本 V 或三矩型 $\mathsf T$。

真实平移导子 $N=\mathscr L_{\partial_x}$ 的完整表是

$$
\begin{aligned}
NP&=0,& NR&=NS=P,& NL&=-\tfrac12(R-S),\\
NU_1&=R+2S,& NV_1&=L-\tfrac12U_1,& NT_1&=2U_1,\\
NE_+&=2V_1-\tfrac12T_1.
\end{aligned}
\tag{4}
$$

R255 的原证明保同右积分及移动重标后的实际上锚，不是只比较显式局部项。

定义五个原八矩方向

$$
\boxed{
\begin{aligned}
A_0&=P,\\
A_1&=(R+S)/2,\\
A_2&=(U_1-L)/3,\\
A_3&=T_1/12-V_1/3,\\
A_4&=-E_+/6.
\end{aligned}}
\tag{5}
$$

逐项使用 (4)，准确得到

$$
\boxed{NA_0=0,\qquad NA_l=A_{l-1}\quad(1\le l\le4).}
\tag{6}
$$

例如 $N(U_1-L)=\tfrac32(R+S)$，
$N(T_1/12-V_1/3)=(U_1-L)/3$。
等价地，$A_l=-N^{4-l}E_+/6$，而 $N^4E_+=-6P$。这是真二次算子身份，未新增原式计算。

## 3. 五条响应的完整 self 和整三矩核

令 $\chi=\chi_{30}$ 为 R254/R261 已付的完整第三对角核方向，$\Delta\chi=0$。记

$$
G_l=\mathcal B_{A_l}(\chi),\qquad 0\le l\le4,
\tag{7}
$$

其中 $\mathcal B$ 是 R83/R255 的完整第四响应规范，保外槽、内槽和全部第三 history。

R261 的零阶局部系数准确为

$$
c_{\chi,u}=\frac3{512}D^3\bigl((u'')^2\bigr).
\tag{8}
$$

R298 已由完整右三常数证明

$$
\pi\mathcal B_E(\chi)=0,\qquad
\mathsf T(\mathcal B_E(\chi))=0
\quad\text{对全部 }E\in E_8.
\tag{9}
$$

因此五条 (7) 都在 $\mathcal R_{\mathrm p0}\cap\ker\mathsf T$。这里没有假定整个 $Z$ 的响应都在矩阵核；R297 的另外三条 $\chi$ 恰有非零矩阵作用。

完整 self 是

$$
\boxed{
\mathfrak q_u(\mathcal B_E(\chi))
=-\frac14\int c_{\chi,u}(x)\,\Phi_E(u,u)(x)\,dx
=\frac3{2048}\int (u'')^2D^3\Phi_E(u,u)\,dx.
}
\tag{10}
$$

三个积分号换位的边项由 $(u'')^2$ 的真实 compact 支撑支付，不要求 $\Phi_E(u,u)$ 的左多项式尾为零。还可写为

$$
\mathfrak q_u(\mathcal B_E(\chi))
=-\frac3{2048}\int D((u'')^2)\,D^2\Phi_E(u,u)\,dx.
\tag{11}
$$

原 $D^2\Phi_E$ 只含至多三阶局部 jets 与已知原右积分，故 (11) 同时给该完整泛函的 $C^3$ 连续多项式性质。

定义五个准确母包常数

$$
d_l(u)=\mathfrak q_u(G_l).
\tag{12}
$$

它们由完整 (10) 或 (11) 定义，没有将原尾独立赋值，也不需要在本稿求出其数值。只有首个常数的严格值必须用到：

$$
\boxed{
d_0(u)=\frac3{512}\int (u'')^2(u''')^2>0.
}
\tag{13}
$$

这正是 R298 的完整正 identity；其严格性只要求非零实紧母包。

## 4. 全部允许平移上的准确四次轮廓

### 4.1 同锚平移，没有丢右常数

把 $x=y+c$ 代入原二次算子。右积分变成

$$
\int_x^{r_*}F(\xi)\,d\xi
=\int_y^{r_*-c}F(c+\eta)\,d\eta.
$$

对所有允许 c，$r_*-c$ 仍在未平移母包的共同右零区间中。把该上锚在这段零 collar 内移动，不改变任何原二次算子。由完整表 (4)，

$$
\Phi_E(u_c,u_c)(y+c)
=\Phi_{\exp(cN)E}(u,u)(y).
\tag{14}
$$

而 (8) 没有显式 x，故

$$
c_{\chi,u_c}(y+c)=c_{\chi,u}(y).
$$

将这两个准确身份代入 (10)，得到

$$
\mathfrak q_{u_c}(\mathcal B_E(\chi))
=\mathfrak q_u(\mathcal B_{\exp(cN)E}(\chi)).
\tag{15}
$$

这里只平移评价输入并作同锚重标，不把平移当作已经实际执行的几何控制。左二次多项式的最高系数在坐标重标下保持，也没有在 (15) 中添加新的左基准。

### 4.2 完整轮廓是一个可逆三角族

由 (6)、(15)，五个函数

$$
s_l(c)=\mathfrak q_{u_c}(G_l)
$$

准确满足

$$
\boxed{
s_l(c)=\sum_{r=0}^{l}\frac{c^r}{r!}\,d_{l-r}(u),
\qquad 0\le l\le4.
}
\tag{16}
$$

其最高项是 $d_0c^l/l!$。于是

$$
\boxed{
\left\{c\longmapsto
\mathfrak q_{u_c}(K):
K\in\operatorname{span}(G_0,\ldots,G_4)\right\}
=\operatorname{Pol}_{\le4}.
}
\tag{17}
$$

并且从该五维响应模块到右端的映射是同构。独立性来自 $d_0>0$ 及不同最高次数；没有作新的求秩或采样。

式 (17) 是**完整 self 的原函数身份**。它不只是 $u'''$ 主项的多项式，也不只是五个点上的数值匹配。改变 c 时，所有随平移变化的 $C^2$ 余项及真实 Volterra 尾都已经包含在 $d_l$ 和 (16) 中。

给定任意四次以下目标多项式，可从最高次起三角求出唯一 $t_0,\ldots,t_4$，使 $\sum t_ls_l(c)$ 等于该多项式。每步除数都是某个非零 $d_0/l!$，其余 $d_j$ 保准确定义。没有用高 jet 主符号代替完整目标。

## 5. 不超过五个完整 self 的联合矩阵

取 $1\le m\le5$ 个互异允许中心 $c_1,\ldots,c_m$。允许实际包另带非零实幅度 $\rho_j$：

$$
u_j(x)=\rho_j u(x-c_j).
\tag{18}
$$

由原成本四次齐次性，

$$
\mathfrak q_{u_j}(V)=\rho_j^4\mathfrak q_{u_{c_j}}(V).
\tag{19}
$$

对列 $G_0,\ldots,G_{m-1}$，完整 self 矩阵是

$$
S_{jl}=\rho_j^4s_l(c_j),
\qquad 1\le j\le m,\quad0\le l\le m-1.
$$

由 (16) 及 Vandermonde 行列式，

$$
\boxed{
\det S=
\left(\prod_{j=1}^m\rho_j^4\right)
\frac{d_0(u)^m}{\prod_{l=0}^{m-1}l!}
\prod_{1\le i<j\le m}(c_j-c_i)\ne0.
}
\tag{20}
$$

所以这 m 个**完整** self 值在矩阵零的真实 pure-zero 响应上独立。即使这些包属于同一高阶编码母族，(20) 仍不是它们所有数量的自动满射；这里只用了不超过五个节点。

### 5.1 加上 R297 九矩，准确三角化

令 $R_{ab}$ 是 R297 的九条矩阵单位响应：

$$
\pi R_{ab}=0,\qquad \mathsf T(R_{ab})=e_{ab}.
$$

记 $\mathbf q(V)=(\mathfrak q_{u_1}(V),\ldots,\mathfrak q_{u_m}(V))$。
用 (20) 的准确逆，定义

$$
\widehat R_{ab}
=R_{ab}-\sum_{l=0}^{m-1}
\bigl(S^{-1}\mathbf q(R_{ab})\bigr)_lG_l.
\tag{21}
$$

则

$$
(\mathsf T,\mathbf q)(\widehat R_{ab})=(e_{ab},0).
$$

五模块的适当 S 逆组合则给 $(0,e_j)$。所有列的 pure 都为零。因此

$$
\boxed{
(\mathsf T,\mathbf q)(\mathcal R_{\mathrm p0})
=\operatorname{Mat}_3(\mathbb R)\oplus\mathbb R^m.
}
\tag{22}
$$

式 (21) 中的旧列 self 数值没有在本稿重新评价。它们是准确有限实数；三角存在性不需要把它们伪写成已计算的有理常数。

## 6. 真正的有限几何支付

令 $P_{\rm univ}=\pi U$。固定上述真实包、查询及共同 I 后，R222 的一般有限观测定理可取

$$
F=(\mathsf T,\mathbf q),\qquad \dim F=9+m.
$$

其响应矩阵由 (20)–(22) 准确可逆。故对任意

$$
p\in P_{\rm univ},\quad
A\in\operatorname{Mat}_3(\mathbb R),\quad
z\in\mathbb R^m,
$$

存在有限真实同端口、frame $I\to I$ 块 D，使

$$
\boxed{
M_D=\mathbf T_D=0,\quad
\pi V_D=p,\quad
\mathsf T(V_D)=A,\quad
\mathbf q(V_D)=z.
}
\tag{23}
$$

这里 $\mathbf T_D$ 指整个第三算子，不是平台矩阵。

这一步保 R222 的完整控制顺序：有限原第三 prototypes 先补 whole-pure 基准；全部 mixed 基准留在复制词；最后一个实际 full-pure 截面的全部新 self/矩阵值留在有界 $C^1$ 误差中；最后才选择有限复制数，以 Brouwer 或统一收缩同时支付 $9+m$ 个实数。没有负路径，没有把基准归零，也没有略去 pure 校正改变 self 的部分。

对一个先纳入生成库的真实闭 hook 背景，给 D 指定四份成本的四分之一校正，再按 R222/R297 的真实 Klein 词闭合，得到

$$
\boxed{
M_X=0,\quad
\mathbf T_X=\kappa\mathfrak H,\quad
\pi V_X=0,\quad
\mathsf T_X=A,\quad
q_X(u_j)=z_j\ (1\le j\le m).
}
\tag{24}
$$

取 $A=0,z=0$，即同时支付至多五个指定完整 self 及整九矩。R196 的严格正字符仍保留；本稿不把这些有限观测等同于完整 period。

共同 I 的顺序与 R298 一致：先固定 full-pure 库、九条 R297 原响应、五条 (7)、背景和桥的小参数包络，再选 I 及母包/中心；最后选实系数、目标盒与有限重复。大系数只增加固定小族的重复，不扩原 scalar 包络。

一般结论不保持预先冻结的总长、位移、度量、Gaussian 共振 germ 或全域 Morse。若另有已证明的联合结构保持族，可在那个族上使用本稿的有限观测；但 (22) 本身不提供这些额外自由度。

## 7. 任意多包时，这五维模块的准确兼容条件

本节只讨论 $\mathcal G=\operatorname{span}(G_0,\ldots,G_4)$ 的作用，不把它当作整个 $\mathcal R_{\mathrm p0}\cap\ker\mathsf T$。

取任意有限个不同允许中心 $c_1,\ldots,c_n$，$n>5$，以及非零幅度。把原 self 数值正规化为

$$
y_j(V)=\rho_j^{-4}\mathfrak q_{\rho_ju_{c_j}}(V)
=\mathfrak q_{u_{c_j}}(V).
$$

令 $\ell_1(c),\ldots,\ell_5(c)$ 为前五个节点的准确四次 Lagrange 基。由 (17)，存在一个 $K\in\mathcal G$ 使全部 $y_j(V+K)=0$，当且仅当

$$
\boxed{
y_j(V)-\sum_{a=1}^5\ell_a(c_j)y_a(V)=0,
\qquad 6\le j\le n.
}
\tag{25}
$$

证明只需取唯一四次多项式
$P(c)=-\sum_a\ell_a(c)y_a(V)$，用 (17) 实现它，再检查剩余节点。式 (25) 是完整 self 值的兼容式，包含所有低阶余项。

这些残差杀 $\mathcal G$，但不据此声称它们杀整个真实响应空间，也不预报它们在 U 上独立。其他 $\chi$、其他第三槽及第四 pure 核分支仍可能改变它们。

若要求同一母包的整个开放平移区间上都清零，则本模块准确能做到，当且仅当原函数

$$
c\longmapsto\mathfrak q_{u_c}(V)
$$

本身属于 $\operatorname{Pol}_{\le4}$。不能只因它是某个有限次数的多项式，就把次数大于四的系数删去。

同样，(25) 是给定线性成本 V 后加入这一五模块的兼容条件。R222 的实际纯校正会产生自己的完整 self 基准，所以没有把 (25) 直接冒作一个未知实际校正后的不变量；真正的实际联调仍应对最终所需观测用同一有限响应矩阵支付。

## 8. 母 shape 改变时可以说什么

### 8.1 对每个非零母包重新成立

(13)、(16)、(20) 对每个非零实紧母包都成立。因此不必为另一个母包重新运行五个科学目标。

但母包变为 $\widetilde u$ 后，全部 $d_l$、S、(21) 的系数、原控制的 mixed 基准及最后解出的几何参数一般都会变化。不能把“对每个母包存在控制”写成“原来那条固定几何仍清全部新 self”。

尤其，R293/R294 的同一有限 $C^2$ 观测纤维并不固定 $d_0$；R298 已明确给其非 $C^2$ 连续的高频通道。因此同 $\mathcal F^\star$ 或同 $\mathcal F^+$ 本身不够继承一个旧 self 控制系数。

### 8.2 有界光滑母族的参数化接口

有一个严格而有限的可用增强。设 $\zeta$ 位于一个固定紧的有限维参数集，全部真实 profiles $u_\zeta$ 光滑、非零且支撑在固定内部包络。假设

$$
\zeta\longmapsto \rho_j(\zeta)\,
u_\zeta(\,\cdot-c_j(\zeta))
$$

为 $C^1$ 的 $C^3$ 值映射；中心互异且非零幅度在紧集上留正间隔。这里可以直接取一个光滑有限参数族，不要求只凭 $C^2$ 接近就推出这项假设。

由 (11) 及 R295 对完整 self 的 $C^3$ 分裂，所有相关原查询关于 $\zeta$ 为 $C^1$。式 (13) 在该紧集上有正下界，(20) 使 S 的逆及其一阶导有统一界。原九矩与五条 G 的生成库始终不变。

因此 R222 的有限控制证明可以同时带参数 $\zeta$：其可逆观测矩阵写为 $\mathsf K(\zeta)$，真实基准中心为

$$
t^0(\zeta)=-2\mathsf K(\zeta)^{-1}v_\Sigma(\zeta).
$$

先固定覆盖这些中心及目标的紧参数盒与 full-pure 截面，再选统一有限 n，解

$$
t=t^0(\zeta)+n^{-1}\mathsf K(\zeta)^{-1}
\{(A,z)-\mathcal E(t,p,\zeta)\}.
\tag{26}
$$

统一收缩给一个关于 $\zeta,p,A,z$ 的实际 $C^1$ 控制截面。所有未知 mixed 基准仍包含在 $\mathcal E$ 中，原共同 I 先于最后有限计数固定。

这允许在一个已经明确给定的有限光滑 shape 族中重新调几何以保有限 self 目标。它不授无限高频全族的统一预算或一个固定控制字，不授仅由 $C^2$ 纤维约束产生的统一 $C^3$ 界，也不同时自动保其他无限族 profile 或所有编码包。

## 9. 本稿推进到的位置

已经完成的是：

- 五个明确真实方向 (5)、(7)，全部在 pure 与三矩矩阵的共同核；
- 完整 self 的全平移原身份 (16)，准确产生整个四次以下轮廓；
- 至多五个同母同宽不同中心的完整 Vandermonde 非退化式 (20)；
- 整 pure、九矩、这些完整 self 的实际有限同时支付 (23)–(24)；
- 对任意多包的五模块准确兼容式 (25)，以及有界光滑 shape 族的真实参数接口 (26)。

还没有完成当前巨量编码模板的全部 $q_i$，没有证明全部 canonical self 平移轮廓次数不超过四，没有证明全函数观测
$V\mapsto[u\mapsto\mathfrak q_u(V)]$
在 $\mathcal R_{\mathrm p0}$ 上覆盖其在 U 上的全部像。

后续若要扩展，应比较更多真实响应对完整 self 的作用，或消费原函数的完整主项加 $C^2$ 余项；不能只把 principal 满秩当成完整 self 满射。本文不重算已付三矩、八个 hook、旧 pure 分类或完整第四 forcing，也不把这五维新接口冒成主课题完成。
