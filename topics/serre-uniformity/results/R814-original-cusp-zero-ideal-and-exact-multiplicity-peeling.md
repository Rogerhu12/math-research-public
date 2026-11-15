# R814：原导子的约化 cusp 零理想与准确降重数

日期：2026-11-15。状态：**本篇证明原正规环中的零理想和降重数接口；尚未计算新的导子矩阵、极理想、radical、Jacobian 或高度。**
首个实际消费者是 R805 的三重数提取。它可直接复用原导子矩阵，因而不要求先生成一个 ambient 场迹配对全表。

本篇接 [R805](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)、
R806 的真实 primitive 乘法、
[R809](R809-original-normal-vectors-for-function-and-Hodge-inputs.md)、
[R811](R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md)、
[R813](R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md)。
所有坐标仍在原 $Y/K$、$K=\mathbb Q(\zeta)$ 及其 $L=K(b)$ 基变换中。
原函数、$\tau,\sigma,c_0,c_1,\rho,\kappa$ 和三同源主函数规范均不改变。

## 1. 两种迹不能混用，当前真正需要什么

在 R805 中，完整非零整理想 $I\subset\mathcal R$ 给有限 $k$ 代数
$\mathcal R/I$，其中 $k=K$ 或 $L$。
求 $\sqrt I$ 时原可用的配对是
$$
(\bar a,\bar b)\longmapsto
\operatorname{Tr}_{k}\bigl(m_{\bar a\bar b}\mid\mathcal R/I\bigr).
\tag{814.1}
$$
其核为该有限代数的 nilradical。

它不同于
$$
(a,b)\longmapsto
\operatorname{Tr}_{k(Y)/k(z)}(ab)
\tag{814.2}
$$
在有限自由环 $\mathcal R/k[z]$ 上的场迹配对。
把(814.2)的矩阵模掉一个理想，不能直接替代(814.1)；
分歧纤维和非平坦的有限商尤其不能略过。
本篇不使用“ambient trace 矩阵的核就是 $\sqrt I$”这一错误替换。

R813 已为真实函数微分和 R804 加法 DAG 给出同一原导子的恢复接口。
一旦其实际 $M_g,\Gamma$ 返回，下文只用两个 $272\times544$
多项式列生成矩阵及整理想商，便可替代(814.1)的 radical 步骤。
这正是此次的实际消费者桥；无需先生成场迹配对全表。

## 2. 固定原整基、导子及完整列约定

取 R805 的真实无基点铅笔和正规整基
$$
z=\sigma/\tau,\qquad
\mathcal R_\tau=\mathcal O(Y_k\setminus H_\tau)
=\bigoplus_{a=0}^{271}k[z]\beta_a,\qquad
\beta_a=d_a/\tau^{\epsilon_a},
$$
$$
H_\tau=\operatorname{div}\tau,\qquad
\epsilon=(0,1^{144},2^{127}),\qquad\beta_0=1.
\tag{814.3}
$$
这里是完整正规环，不是可能非正规的 $k[z,w]$。

写 $\mathcal D_{\rm cusp}$ 为原约化二十 cusp 除子。
原线丛是 $\mathcal H=K_Y+\mathcal D_{\rm cusp}$。
R813 的准确原导子为
$$
D_0=\frac{q_Y}{82}\frac d{dq_Y},\qquad
\delta_\tau=\tau^{-1}D_0,\qquad
g=\delta_\tau z.
\tag{814.4}
$$
$\delta_\tau$ 在 $U_\tau=Y_k\setminus H_\tau$ 上正则，且在 $k$ 上线性。
它非零，而 $k(Y)/k(z)$ 可分，所以 $g\ne0$。

固定列向量约定
$$
\delta_\tau\beta_a=\sum_b\Gamma_{ba}(z)\beta_b,\qquad
g\beta_a=\sum_b(M_g)_{ba}(z)\beta_b.
\tag{814.5}
$$
对任意多项式坐标列 $v(z)$，
$$
\operatorname{coord}(\delta_\tau(\beta v))
=\Gamma v+M_gv'.
\tag{814.6}
$$
$M_g$ 是乘法矩阵，$\Gamma$ 是导子对基的矩阵；不能互换这两个角色。
两者必须是经过 R813/R809 完整准确认证的实际输出。
仅有两个 Wronskian 的 normal 向量，尚不等于已经有这些矩阵。

## 3. 一个 272×544 列像恰给导子的完整零理想

记原导子的零理想为
$$
\mathcal C_\tau=\delta_\tau(\Omega^1_{\mathcal R_\tau/k})
\subset\mathcal R_\tau.
\tag{814.7}
$$
这是把一形式与原向量场配对的像。
在离散赋值参数 $u$ 下若
$\delta_\tau=a(u)\,\partial_u$，则局部
$\mathcal C_\tau=a(u)\mathcal R_\tau$。

**定理814.1。** 在(814.3)的原整基中，
$$
\boxed{\quad
\mathcal C_\tau=
\operatorname{im}_{k[z]}\,[\,\Gamma\ \ M_g\,].
\quad}
\tag{814.8}
$$
右侧虽然初始只是 $k[z]$ 子模，其准确像本身已经是
$\mathcal R_\tau$ 理想。无需先生成272个基元素的全部乘法表来闭包它。

**证明。**
$\Gamma$ 的列是 $\delta_\tau\beta_a$；
$M_g$ 的列是 $\beta_a\delta_\tau z$。
它们属于(814.7)，故右侧 $N$ 包含于 $\mathcal C_\tau$。
同时 $N$ 包含 $g\mathcal R_\tau$。
因为 $g\ne0$，$\mathcal R_\tau/g\mathcal R_\tau$ 是有限 $k$ 代数，
所以只需在有限支撑上的完成化中证明相等。

为说明局部证明，可作忠实平坦的代数闭包基变换；
这只用于证明，不要求实际算法拆分闭点。
先在基环的一个点 $z=z_0$ 完成，而不是只分别投影到各因子：
$$
\widehat{\mathcal R}
=\mathcal R_{\bar k}\otimes_{\bar k[z]}\bar k[[z-z_0]]
=\prod_{P\mid z_0}\bar k[[u_P]].
$$
$\widehat N$ 此时只是这个完整乘积中的
$\bar k[[z-z_0]]$ 子模；本段不预先假定它对各因子的幂等元稳定。
每个因子上有
$$
z-z_0=u_P^{e_P}b_P(u_P),\quad b_P(0)\ne0,\qquad
\delta_\tau=a_P(u_P)\partial_{u_P}.
$$
于是 $g_P=a_Pz'_P$，且在特征零下
$\operatorname{ord}_{u_P}z'_P=e_P-1$。

对乘积中的任意 tuple $(a_Pv_P)_P$，逐因子用截断积分选 $r_P$ 满足
$$
r'_P(u_P)\equiv v_P(u_P)\pmod{z'_P(u_P)}.
\tag{814.9}
$$
当 $e_P=1$ 时商为零；当 $e_P>1$ 时只需积分至 $u_P^{e_P-2}$，
每个整数 $1,\ldots,e_P-1$ 在特征零中均可逆。
把这些选择合成同一个 $r=(r_P)_P\in\widehat{\mathcal R}$。
原自由基在基环完成后仍是整个乘积的自由基，
所以有一个完整系数列 $v\in\bar k[[z-z_0]]^{272}$ 使 $r=\beta v$。
由(814.6)，
$\delta_\tau r=\Gamma v+M_gv'\in\widehat N$。
且 $(a_Pv_P)_P-\delta_\tau r\in g\widehat{\mathcal R}\subseteq\widehat N$。
于是整个乘积中的 $\widehat{\mathcal C_\tau}$ 包含于 $\widehat N$，
而非仅仅在每个投影中像相等。
有限商在这些基环完成化中全零即为零；再忠实下降，得到(814.8)。$\square$

这个论证同时处理 $\pi:Y\to\mathbb P^1$ 的分歧点。
不能把未经证明的集合 $\delta_\tau(\mathcal R_\tau)$ 本身先叫作理想；
真正使用的是含 $g\mathcal R_\tau$ 的有限列像及上述局部证明。

## 4. 本题的零理想恰是约化 cusp，不能换成任意高重零导子

把原 $\tau$ 视为 $\Omega_Y^1(\mathcal D_{\rm cusp})$ 的截面。
其原对数微分在 Fourier 图上是
$$
\omega_\tau=82\tau\,\frac{dq_Y}{q_Y},
\qquad
\omega_\tau(\delta_\tau)=1.
\tag{814.10}
$$
同一原 Tate 规范给
$$
\operatorname{div}\omega_\tau=H_\tau-\mathcal D_{\rm cusp},
\qquad
\operatorname{div}\delta_\tau=\mathcal D_{\rm cusp}-H_\tau.
\tag{814.11}
$$
所以在 $U_\tau$ 内，导子零阶只可能为0或1，而且
$$
\boxed{\mathcal C_\tau
=I_{\mathcal D_{\rm cusp}\cap U_\tau}.}
\tag{814.12}
$$

这不是 R805 的21点除子
$\mathcal B=\mathcal D_{\rm cusp}+P_0$。
$P_0=\phi(c_0)$ 和 $P_1=\phi(c_1)$ 都不是额外的导子零点：
若某点属于 $H_\tau$，它不在本图；否则原对数微分在内部点没有 cusp 极点。
不能把 $\phi$ 的三分歧、内部模椭圆点和 $\delta_\tau$ 的零除子混为一件事。

下节降重数公式的必要输入是
$\operatorname{ord}_P\mathcal C_\tau\in\{0,1\}$。
对一个有高重零的任意导子，原公式一般不成立。

## 5. 完整理想的导数像：不额外做乘法闭包

设 $0\ne I\subset\mathcal R_\tau$ 是一个**已经准确认证的整理想**，
原整基中的多项式列基为
$$
I=H_I\,k[z]^{272},\qquad \det H_I\ne0.
\tag{814.13}
$$
不能把任意同维子模未经理想认证就用作这里的 $I$。
R811 的原极点前像理想是允许的实际输入。

定义
$$
N(I)=I+\operatorname{span}_{\mathcal R_\tau}\delta_\tau(I).
$$
则有准确的更小列式
$$
\boxed{
N(I)=\operatorname{im}_{k[z]}
[\,H_I,\ \Gamma H_I+M_gH_I'\,].
}
\tag{814.14}
$$

**证明。**
对 $x\in k[z]^{272}$，
$$
\delta_\tau(H_Ix)
=(\Gamma H_I+M_gH_I')x+M_gH_Ix'.
$$
最后一项属于 $I$，因为 $M_g$ 是环内乘 $g$ 且 $I$ 是理想。
故右侧列像恰为 $I+\operatorname{span}_{k[z]}\delta_\tau(I)$。
它已经对任意 $b\in\mathcal R_\tau$ 稳定，因为
$$
b\,\delta_\tau i=\delta_\tau(bi)-(\delta_\tau b)i
\quad(i\in I),
$$
且 $bi\in I$、$\delta_\tau b\in\mathcal R_\tau$。
所以该列像就是完整理想 $N(I)$。$\square$

这里没有计算全部 $\beta_a\delta_\tau i$ 的单独乘法矩阵。
HNF须保存完整的列生成/包含见证，不能只给一个预计秩。
因为它包含 $I$，列像实际是满秩272的非零整理想。

## 6. 必须使用整理想商；零重数不能被变成负数

本文始终区分整理想商与不交环的分式商：
$$
(J:_\mathcal R Q)
:=\{r\in\mathcal R:rQ\subseteq J\}
=\mathcal R\cap JQ^{-1}.
\tag{814.15}
$$
在指数记号中，它给
$\max(v_P(J)-v_P(Q),0)$。
不允许删掉右侧的 $\mathcal R\cap$。

**定理814.2。** 对(814.13)，定义
$$
\boxed{
\mathsf P(I)=
\bigl(N(I):_{\mathcal R_\tau}\mathcal C_\tau\bigr)
=\mathcal R_\tau\cap N(I)\mathcal C_\tau^{-1}.
}
\tag{814.16}
$$
则逐个闭点有
$$
v_P(\mathsf P(I))=\max(v_P(I)-1,0).
\tag{814.17}
$$
特别地
$$
\boxed{\sqrt I=(I:_{\mathcal R_\tau}\mathsf P(I)),\qquad
I=\mathsf P(I)\sqrt I.}
\tag{814.18}
$$

**证明。**
完成化后写 $I=(u^m)$、
$\delta_\tau=a(u)\partial_u$、$c=v_u(a)\in\{0,1\}$。
若 $m=0$，$I=\widehat{\mathcal R}$，所以
$N(I)=\widehat{\mathcal R}$，
整理想商仍是 $\widehat{\mathcal R}$。
这一步不能误写成指数 $-c$。

若 $m>0$，特征零保证
$\delta_\tau(u^m)$ 的首系数 $m$ 非零。
所有 $I$ 中元素的导数都至少具有阶 $m-1+c$，
并有达到该阶的元素，故
$$
v_u(N(I))=\min(m,m-1+c).
$$
整理想商的指数是
$$
\max\bigl(\min(m,m-1+c)-c,0\bigr)=m-1
$$
，因为 $c=0$ 或1。得到(814.17)。
再逐点取整理想商便给(814.18)。正规一维环中这些逐点理想恒等式
即为原全局理想恒等式。$\square$

例如若换成 $u^2\partial_u$，$c=2$，直接套(814.16)会过度降重；
本篇从不作这个泛化。
整个证明和算法均在原闭点/剩余域上有效，不需要拆分几何支撑。

## 7. 第二图必须显式改用它的正则导子

置 $t=1/z$、$\beta^\sigma_a=t^{\epsilon_a}\beta_a$，
以及坐标运输
$$
D(t)=\operatorname{diag}(t^{-\epsilon_a}).
$$
R813 已给“同一个 $\delta_\tau$”在第二基中的连接。
为了在整个 $U_\sigma$ 上使用上述正则零理想，现**明确改用**
$$
\delta_\sigma=\sigma^{-1}D_0=t\,\delta_\tau.
\tag{814.19}
$$
于是
$$
\widetilde M_g(t)=D(t)M_g(1/t)D(t)^{-1},
$$
$$
M_{\delta_\sigma t}(t)=-t^3\widetilde M_g(t),
\tag{814.20}
$$
$$
\Gamma_\sigma(t)=
tD(t)\Gamma(1/t)D(t)^{-1}
-t^2\widetilde M_g(t)\operatorname{diag}(\epsilon).
\tag{814.21}
$$
这些矩阵的最终条目是多项式；必须准确核全部负幂系数消失。
不能把(814.21)误当成没有改导子的 R813 过渡，
也不能漏掉 $M_g\operatorname{diag}(\epsilon)$ 项。

按(814.8)、(814.14)、(814.16)在第二图使用
$\Gamma_\sigma,M_{\delta_\sigma t}$。
由
$\operatorname{div}\delta_\sigma=\mathcal D_{\rm cusp}-H_\sigma$，
其零理想也是本图的约化 cusp 理想。

在重叠区域 $t$ 是单位，
$\delta_\sigma=t\delta_\tau$。
故两个零理想只相差一个单位倍数，而
$I+\delta_\sigma I=I+\delta_\tau I$；
整理想商给相同的降重数理想。
HNF输出须通过 R811 的双向 Laurent 格包含核对交叠。
实际全球次数仍用“第一图全部加第二图 $t=0$ 部分”，
不能把重叠支撑加两次。

## 8. 直接接 R805 的原三重数和主函数运输

对原 $f_4$ 及 R794 的五个最终映射，原极除子满足
$$
E_g=\mathcal D_{\rm cusp}+P_0+3D_g.
\tag{814.22}
$$
原 cusp 的局部次数1来自 R793 的完整原 Hom 结论；
因此这六个 $E_g$ 在每个 cusp 的重数恰为1。
$p=41$ 的原实际次数及其理论校验值为：

| 原映射 | $\deg E_g$ | $\deg D_g$ |
|---|---:|---:|
| $f_4$ | 1206 | 395 |
| candidate0 | 1485 | 488 |
| candidate3 | 1521 | 500 |
| candidate1 | 1602 | 527 |
| candidate21 | 1674 | 551 |
| candidate15 | 1728 | 569 |

表中不是新求得的理想坐标。

在每图令 $I^{(0)}=I_{E_g}$。依次计算
$$
I^{(k)}=\mathsf P(I^{(k-1)}),\qquad
J_k=(I^{(k-1)}:_{\mathcal R}I^{(k)}).
\tag{814.23}
$$
于是 $J_k=\sqrt{I^{(k-1)}}$，与 R805 的逐层算法完全相同。
只把原 finite-quotient trace-radical 步骤换成了(814.14)–(814.18)。
仍有
$$
I_{D_g}=\prod_{3\mid k}J_k,\qquad
I_{\mathcal B}=(I_{E_g}:_{\mathcal R}I_{D_g}^{\,3}),
\quad\mathcal B=\mathcal D_{\rm cusp}+P_0.
\tag{814.24}
$$
全部理想乘回、约化性、全球次数及两个图的相容性仍须准确认证。

第一次降重后，$I^{(1)}$ 的支撑不含 cusp。
可准确核
$I^{(1)}+\mathcal C_\tau=\mathcal R_\tau$，第二图同理。
以后该等式保持，故对 $k\ge2$，无需再作对 $\mathcal C$ 的商：
$$
I^{(k)}=N(I^{(k-1)}).
\tag{814.25}
$$
这里省掉的是后续 cusp 商，不是
$J_k=(I^{(k-1)}:_{\mathcal R}I^{(k)})$ 或三重数理想的乘回。

执行到单位理想即停止。实际层数应记录；
不能把 degree395等总次数当作最大局部重数。
有限上界可用原 $\deg E_g$，本表最大1728，但不预跑这个最坏上界。

下游 R805 的两次 $V_3$ flip、$G_g=u_g/v_g$、
原 norm、$\mathcal G_g^9\mathcal R_g$ 和原 R794 基变换均不改。
HNF首一化只是理想生成矩阵的变换，不能被解释成主函数常数1；
实际截面坐标和每个刚性化标量仍须原样运输。
本篇没有消去 Picard 二挠、第二类周期、原 $c_0$ 刚性化或真实高度输入。

## 9. 执行边界、证明见证与实际成本

首次实际输入至少包括：

- R805 的同一272维完整正规基和两图过渡；
- R813 后继实际认证的 $M_g,\Gamma$，以及它们的原源身份；
- R811 或等价完整认证的原非零整理想 $I$，不是任意低阶前缀；
- 精确多项式格的 HNF、交、整理想商、乘回和双向包含见证。

先构造一次(814.8)的零理想。
在两个图上分别计算，核对重叠并记录其全球约化 degree20；
这个degree是几何目标校验，只有真实计算后才可写 computed=true。
它与21点 $\mathcal B$ 必须分别命名、分别认证。

对每个实际需要的 $I$，每层仅新增
$\Gamma H_I+M_gH_I'$ 和相应列 HNF；
已经完成的层、当前理想和已提取的 $J_k$ 全部源绑定保存。
整理想商仍须在完整正规环中执行，不能偷偷改到 $k[z,w]$；
它的成本没有被(814.14)抹去。
多项式矩阵系数可很大，HNF及商都可能需要独立的断点预算。

R813 首次两 RHS 任务尚不提供 $\Gamma$。
本篇不让一个只有 $g,h$ normal 向量的 producer
伪装成已经完成(814.8)或(814.23)。
也不因本算法存在，就填写 $D_g$、$\eta$ 或高度已算。

## 来源与原执行规范

- 本仓库 R762、R764、R793、R794、R805（2026）：原 cusp/固定点、
  全部非零原 Hom 的 cusp 次数、六个实际映射次数、三重数和主函数运输。
- R806、R809、R811、R813（2026）：原 primitive 乘法、cyclic 认证、
  有界 normal 坐标、完整正规极理想与原导子规范。
- 新的有限列像、分歧完成化、整理想商和逐层理想恒等式均在本文给出证明；
  未把算法存在登记成实际高度输入。

所有新算术仅在本公开仓库 Actions。
可重算矩阵、理想、证书只作一日活跃传输；仓库保脚本、参数、run、SHA与结论。

