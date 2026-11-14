# R550 — 同预算垂直理想、完整 ramification 商与原 H3 核的真实像

日期：2026-11-14。**状态：已证明。** 本篇把 R547 的原垂直列接到
同预算的整个 \((F,\mathcal EF)\mathcal H_2\)。
其代数余商是长度 \(\kappa=C^2\) 的真实交概形；
原整个 \(\mathcal H_3\) 首核在该交概形上的像，
准确由 R524 的第二连接核给出，并且限制映射单射。
因此这里不是把 \(\kappa\) 个值当成任意修正参数。

对 R514 的完整清极 forcing，另构造一个长度
\(\kappa+9d_\infty\) 的有限商，保分歧交概形与固定边界的重叠。
其核是同一真实三层核的限制像。
简单分歧处的 forcing 单位仍不能独立推出原 Bockstein 非零：
完整 \(\mathcal H_3\) 已能给出任意分歧值，而物理相容由上述连接控制。

## 1. 同一实际窗口

保持 R495、R498、R517、R524、R547 的原对象。
令
$$
e=\mathcal EF,\qquad
N=\mathcal O_C(C),\qquad
\kappa=C^2,\quad\chi=-K_XC,\qquad
\mathcal H_j=H^0(X,\mathcal O_X(jC)).
$$
\(F,e\) 都是同一 \(\mathcal H_1\) 的真实截面，
且 \(e(P)\ne0\)、\(P=(0,1)\in C\)。

原来源前缀始终为 \(d^{-C_D}t^rQ\)。
相对 \(J\) 和整个原 \(M\) 分别保
$$
T=s-r,\qquad T=s-r-13.
\tag{1}
$$
沿用 R547 的强窗
$$
\boxed{h>\kappa,\qquad q:=T-h>\kappa,\qquad T\le2h.}
\tag{2}
$$
这特别给 \(T>2\kappa\)、\(0<h<T<p\)。
原高目标仍是
$$
\mathcal A_T=k[[t]][\epsilon]/(t^T,\epsilon^2),\quad
\zeta\mapsto\eta+a\epsilon,\quad
\operatorname{ord}\eta=h,\quad\eta^2=0\bmod t^T.
$$
其余原低行、\(P_{134}/U_0\)、十三自由行及两条 carry 全部保留。
只在这个已知高像中使用下文几何评价。

## 2. 真交概形与同预算理想

定义 \(X\) 上的实际零维交概形
$$
\boxed{Z=V(F,e).}
\tag{3}
$$
这里 \(F,e\) 作为 \(\mathcal O_X(C)\) 的截面读取，
不是未经角平凡化的仿射交点集合。
因为 \(C\) 整且 \(e(P)\ne0\)，\(e\) 不在整个 \(C\) 上为零。
所以 \(F,e\) 是一个正则序列，\(Z\) 为有限完全交，
并且
$$
\boxed{\operatorname{length}Z=\kappa,\qquad P\notin Z.}
\tag{4}
$$
它保所有固定角、重交点及非约化结构；
并不假定每个点都是光滑简单分歧。

令
$$
\boxed{
\mathcal I=F\mathcal H_2+e\mathcal H_2
\subset\mathcal H_3.
}
\tag{5}
$$
这整个空间都由 R495 返回同一原 \(\mathcal W_D\)，零新增 charge。
其原多项式呈示是 \((H,K)\mapsto FH+eK\)。

Koszul 序列准确给
$$
0\longrightarrow\mathcal O_X(C)
\xrightarrow{(-e,F)}
\mathcal O_X(2C)^2
\longrightarrow\mathscr I_Z(3C)\longrightarrow0.
$$
R495 已付全部正倍数的一、二阶所需上同调消失，所以
$$
\boxed{
\mathcal I=H^0(X,\mathscr I_Z(3C)),\qquad
\mathcal H_3/\mathcal I
\simeq H^0(Z,\mathcal O_Z(3C)).
}
\tag{6}
$$
特别
$$
\dim\mathcal I
=1+\frac{7\kappa+3\chi}{2},
\tag{7}
$$
且整个 \(\mathcal H_3\to H^0(Z,\mathcal O_Z(3C))\) 满射。
这最后的满射不能省略：一个在 \(Z\) 上非零的候选，
未必在加入全部原 \(\mathcal H_3\) 列后仍有缺陷。

## 3. 理想块的物理核准确回到同一个镜轴

记
$$
K_0=\ker(\mathcal H_3\to\mathcal A_T),\qquad
K_{\rm mir}=
\ker\bigl(\mathcal H_2
 \xrightarrow{H\mapsto H(t,\psi e^{2\eta})}
 k[t]/t^T\bigr).
\tag{8}
$$
这些均为原有限评价的约化，不是自由截面模型。

**定理 1。**
$$
\boxed{K_0\cap\mathcal I=F K_{\rm mir}.}
\tag{9}
$$

**证明。** 取同一 \(G=FH+eK\in\mathcal I\)，
并假定其原两 Gaussian 行为零。
由 \(\eta^2=0\bmod t^T\)，
\(G|_C=0\bmod t^T\)。
但 \(G|_C=eK|_C\)，且 \(e(P)\) 是单位。
\(K|_C\) 是次数 \(2\kappa\) 的截面；
\(T>2\kappa\) 迫 \(K|_C=0\)，故 \(K=FK_1\)，\(K_1\in\mathcal H_1\)。
于是
$$
G=F(H+eK_1).
$$
括号仍属于同一个 \(\mathcal H_2\)。
按 R511/R547 的实际二层展开，
\(F(H+eK_1)\) 物理为零准确等价于括号在正镜轴
\(\psi e^{2\eta}\) 消到 \(T\)。
这证明正向。反向是同一个镜轴身份。证毕。

本定理不是仅对某个较小试验修正格成立：
(5) 的整个真实理想块都被包括。
但它也没有把 \(K_{\rm mir}\) 宣称为零；
其值层与 R524 的第一连接继续保留。

## 4. 整个 H3 首核在 Z 上的准确像

按当前 \(T,h,q=T-h\)，R524 的两条实际连接为
$$
\alpha_\eta:
H^0(C,N^2(-hP))\longrightarrow
\operatorname{coker}E_q,
$$
$$
\beta_\eta:
V_T:=H^0(C,N^3(-TP))
\longrightarrow\operatorname{coker}E_{\rm mir}.
\tag{10}
$$
\(E_q,E_{\rm mir}\) 都用原 \(\mathcal H_1,\mathcal H_2\) 的真实列，
单位 \(e+f_2\eta\)、同一 normal 系数及全部正镜轴高尾照 R524 读取。

这里 \(q>\kappa\)，所以最内层 \(N(-qP)\) 负度。
在原 \(X\) 上的来源表示中，准确有
$$
\boxed{
0\to kF^2\to K_{\rm mir}\to\ker\alpha_\eta\to0,
}
\tag{11}
$$
$$
\boxed{
0\to F K_{\rm mir}\to K_0
\to\ker\beta_\eta\to0.
}
\tag{12}
$$
(12) 的最后一映射就是取同一个 \(G|_C\)，
其高值先消到 \(T\)，再由 R524 的真实第二连接判定能否提升。
\(F^3\) 已在前一项中，未在从 \(X\) 到 \(3C\) 时重复计数。

**引理 1。** 限制映射
$$
\boxed{
\operatorname{ev}_Z:V_T\longrightarrow
H^0(Z,\mathcal O_Z(3C))
}
\tag{13}
$$
单射。

**证明。** \(Z\) 在 \(C\) 上是 \(e|_C\) 的 Cartier 零除子，
其线束是 \(N\)，并且与 \(P\) 不交。
(13) 的核为
$$
H^0(C,N^3(-TP-Z))
=H^0(C,N^2(-TP)).
$$
其次数 \(2\kappa-T<0\)，故为零。证毕。

由 (9)、(12)、(13)，得到本篇对整个原首核的准确识别：

**定理 2。**
$$
\boxed{
\operatorname{res}_Z K_0
=\operatorname{ev}_Z(\ker\beta_\eta),\qquad
K_0/(F K_{\rm mir})
\xrightarrow{\sim}\operatorname{ev}_Z(\ker\beta_\eta).
}
\tag{14}
$$
所以这些分歧值不是可独立指定的 \(\kappa\) 个参数；
它们是同一个实际第二连接核的单射像。
第一连接也没有消失，它准确控制 (14) 映射前的
\(F K_{\rm mir}\)。

## 5. 原实际像之间的完整商，而非环境维数

令 \(\varepsilon\) 表示同一 \(\mathcal H_3\to\mathcal A_T\) 评价。
(6)、(14) 给
$$
\boxed{
\frac{\varepsilon(\mathcal H_3)}{\varepsilon(\mathcal I)}
\simeq
\frac{H^0(Z,\mathcal O_Z(3C))}
{\operatorname{ev}_Z(\ker\beta_\eta)} .
}
\tag{15}
$$
证明是直接对
\(\mathcal H_3/\mathcal I\to
\varepsilon(\mathcal H_3)/\varepsilon(\mathcal I)\)
取核；核是 \((K_0+\mathcal I)/\mathcal I\)，
由 (14) 准确识别。
这是真实物理像之商，已通过全部显示来源列。

写
$$
a_\eta=\dim\ker\alpha_\eta,\qquad
b_\eta=\dim\ker\beta_\eta.
$$
同一个有限矩阵的准确约化秩因此为
$$
\boxed{
\begin{aligned}
\dim\varepsilon(\mathcal I)&=\frac{7\kappa+3\chi}{2}-a_\eta,\\
\dim\varepsilon(\mathcal H_3)&=\frac{9\kappa+3\chi}{2}-a_\eta-b_\eta .
\end{aligned}}
\tag{16}
$$
对应整限制具有这么多个单位 Smith 因子。
这保原整个 \(M\) 时必须使用 (1) 的 \(T_M\)；
没有把相对 \(J\) 的连接或秩直接搬过去。

若需要显式上界，可用 R543 已证明的整 Gorenstein 曲线 Clifford 函数
\(\mathfrak b_g\)：
$$
a_\eta\le\mathfrak b_{g_C}(2\kappa-h),\qquad
b_\eta\le\mathfrak b_{g_C}(3\kappa-T),
\quad g_C=1+\frac{\kappa-\chi}{2}.
\tag{17}
$$
在满主阶低 \(\ell\) 窗
\(h/\kappa\to9/8,\ T/\kappa\to9/4,\ \chi=o(\kappa)\)，
这些最多为 \(7\kappa/16+o(\kappa)\)、\(3\kappa/8+o(\kappa)\)。
所以整个实际 \(\mathcal H_3\) 至少有
\(59\kappa/16+o(\kappa)\) 个单位因子。
但 (16) 的完整未知量仍是两条真正连接，不能用这个上界把它们置零。

## 6. forcing 的固定边界和 Z 必须作为一个有限扩张保留

R514/R521 的
$$
G_K=\mathfrak m_3K_F,\qquad
\mathfrak m_3=Y^3t(t-1)^2h_7^3d^2
$$
属于 \(H^0(X,\mathcal O_X(3C+3E_\infty))\)；
它不被免费视为 \(\mathcal H_3\) 的截面。
为同时保 \(Z\) 和这个固定边界，置
$$
Y_3=3C,\qquad L_0=\mathcal O_{Y_3}(3C),\qquad
L_c=L_0(cE_\infty),\qquad D_c=Y_3\cap cE_\infty.
$$
此节的 \(c\ge0\) 是边界厚度，和 R545 的角整数不同；
forcing 使用 \(c=3\)。

令 \(\mathscr I_Z^{Y_3}=(F,e)\subset\mathcal O_{Y_3}\)
为真正的像理想，定义有限子概形
$$
\boxed{
Z_c\subset Y_3,\qquad
\mathscr I_{Z_c}=
\mathscr I_Z^{Y_3}\,\mathcal O_{Y_3}(-cE_\infty).
}
\tag{18}
$$
这是乘积理想；即使 \(Z\) 与 \(D_c\) 重叠，也不把它们当不交并。
边界局部方程在 \(3C\) 上是非零因子，所以有准确序列
$$
0\to\mathcal O_Z(-cE_\infty)
\to\mathcal O_{Z_c}
\to\mathcal O_{D_c}\to0.
$$
扭 \(L_c\) 后给
$$
\boxed{
0\to H^0(Z,L_0|_Z)
\to H^0(Z_c,L_c|_{Z_c})
\to H^0(D_c,L_c|_{D_c})\to0,
}
\tag{19}
$$
且
$$
\boxed{\operatorname{length}Z_c=\kappa+3c\,d_\infty.}
\tag{20}
$$

Koszul 消失还给
\(H^1(Y_3,\mathscr I_Z^{Y_3}L_0)=0\)。
可由第2节的 \(X\) 序列再商去 \(F^3\mathcal O_X\) 得到，
其核是 \(\mathcal O_X\)，一、二阶上同调均为零。
因此
$$
\boxed{
H^0(Y_3,L_c)/
H^0(Y_3,\mathscr I_Z^{Y_3}L_0)
\simeq H^0(Z_c,L_c|_{Z_c}).
}
\tag{21}
$$
左边的分母就是同预算理想块 \(\mathcal I\) 的真实限制像；
它已包含原 \(F^3\) 的零限制。

## 7. 同一真实三层核决定这个有限商的物理核

仍用原
$$
\mathscr I_\eta=(t^T,(\zeta-\eta)^2)
$$
及同一高目标 \(\mathcal A_T\)。
因为固定边界不经过 \(P\)，所有 \(L_c\) 在该高目标用同一个原框。
(21) 因而给实际映射
$$
\tau_{\mathcal I,c}:
H^0(Z_c,L_c|_{Z_c})
\longrightarrow\operatorname{coker}\varepsilon(\mathcal I).
$$
准确有
$$
\boxed{
\ker\tau_{\mathcal I,c}
=
\operatorname{res}_{Z_c}
H^0(Y_3,\mathscr I_\eta L_c).
}
\tag{22}
$$
证明与 R521 一样由实际两评价的蛇形序列得到；
但本篇分母是整个真理想块，有限商是 (18) 的乘积厚化。
\(Z_c\) 的所有重叠和 normal 条件均在同一式中保留。

在 (19) 的首子空间 \(H^0(Z,L_0|_Z)\) 上，
(22) 的核准确退化为 (14)：
$$
\ker\tau_{\mathcal I,c}\cap H^0(Z,L_0|_Z)
=\operatorname{ev}_Z(\ker\beta_\eta).
\tag{23}
$$
因为该子空间来自真正的 \(\mathcal H_3\) 列，
其物理核就是同一 \(K_0\)。
这明确说明两份有限数据之间不是独立选择。

对一个已经支付来源成本的候选 \(G\in H^0(Y_3,L_c)\)，
它在物理目标中被理想块 \(\mathcal I\) 吸收，当且仅当
$$
\boxed{G|_{Z_c}\in
\operatorname{res}_{Z_c}H^0(Y_3,\mathscr I_\eta L_c).}
\tag{24}
$$
若再加入整个原 \(\mathcal H_3\)，还须商去 (19) 的首子空间；
这准确恢复 R521 的固定边界商，不能把分歧值当成一份额外障碍。
其余原 \(\mathcal W_D\) 列继续经过同一个实际消元。

## 8. 原 forcing 的分歧单位与必须保留的相容性

在非固定角的光滑简单分歧点 \(Q\in Z\)，假设
$$
t(Q)\notin\{0,1,-1/8\},\quad h_7(t(Q))\ne0,\quad
Y(Q)\ne0,\quad F_t(Q)F_{YY}(Q)\ne0.
$$
R517 的同一原三次 forcing 给
$$
\boxed{
G_K(Q)=
\mathfrak m_3(Q)\,6(1-t(Q))\,t(Q)^2F_t(Q)^2
Y(Q)^2F_{YY}(Q)\ne0.
}
\tag{25}
$$
这是 (18) 有限商中的一个真实局部值，
不是在别的曲线或任意分歧模型上生成的输入。
若没有满足这些条件的点，不额外假定它存在。

但 (25) 不能直接用来排除原完整像。
第2节已证明整 \(\mathcal H_3\to H^0(Z,L_0|_Z)\) 满射。
第4、7节准确说明：实现这些分歧值时产生的物理相容问题，
由 \(\operatorname{ev}_Z(\ker\beta_\eta)\) 和
同一 \(H^0(\mathscr I_\eta L_3)\) 的完整限制像控制。

forcing 自身是已付返回列；当所用预算含它时，原真左行必须杀它。
(25) 的意义是在比较子格中提供一个具体非零条件，
不是说这个已加入的来源列在整个原余核中仍非零。
要把它接到 R502 的 \(\xi\) 和完整首 Bockstein，
必须使用 (22)–(24) 的同一有限数据与全部原列。

## 9. 原 M、同一修正与接续范围

本篇给了整个原 \(\mathcal H_3\) 首核在 \(Z\) 的准确像，
并支付了 forcing 的有限 ramification/固定边界联合商。
它没有仅报告 Koszul 维数后把所有局部值视为自由；
两条真实连接、重叠点、完整三层核均明确保留。

原 \(M\) 使用 (1) 的准确较短 \(T\)，
其 \(P_{134}/U_0\)、十三自由行、两条十三行 carry
和 R479/R481 的同一修正第三精度保持。
来源返回的预算与实际像也没有混同。

下一实质比较是 (14)、(22) 中的实际核像是否支付原 forcing，
以及与 R547 单列余项、R545 平衡切向列和全部原剩余列的联合。
原三条完整中央并未给这些新比较空间额外的中央零，
跨素数非零及主目标仍未得到。
