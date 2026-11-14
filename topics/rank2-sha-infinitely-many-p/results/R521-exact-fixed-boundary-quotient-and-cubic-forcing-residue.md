# R521 — 准确固定边界商与三次 forcing 残数

日期：2026-11-14。**状态：已证明。** R514、R517 的固定清极返回位于
$3C+c\pi^*S_\infty$。本篇将它们在完整 $3C$ 来源以外的附加空间，
准确识别为一个长度 $3c(u+4b)$ 的有限边界商；来源维数中另有的
$2c^2+3c$ 项全被真实 $F^3$ 核消掉。

原几何真行的作用可准确转到这个边界的残数配对。
在任一非固定角的 $Y=\infty$ 交点，还得到一个显示边界泛函：
它杀全部同乘子的切向来源，对三次 forcing 却给
$b^2m(4t_0-1)$。因而在明确条件下，forcing 的边界类不在切向边界像内。

最后保留从边界商到原有限高 jet 的准确核。
没有把边界类的非零冒称原 $J$ 或 $M$ 余核的非零；
这一步需要同一个真实 $\mathscr I_\eta$ 的全局截面相容性。

## 1. 同一固定角曲面和正截面

保 R495、R498、R514、R517 的实际立方
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,
\qquad b=\deg_YF,\qquad
u=\max_i(\deg F_i-4i)\ge0.
\tag{1}
$$
$X$ 是同一十九次普通吹起，$C$ 是 $F=0$ 的严格变换。
写
$$
E_\infty=\pi^*S_\infty,\qquad
d_\infty=C\cdot E_\infty=u+4b.
\tag{2}
$$
这里 $S_\infty=S_0+4F_0$ 是 $\mathbb F_4$ 的正截面。
准确有
$$
E_\infty^2=4,\qquad K_XE_\infty=-6.
\tag{3}
$$
$E_\infty$ 与原点 $P=(0,1)$ 不相交。

注意 $E_\infty$ 是完整拉回除子。
除 $S_\infty$ 的严格变换外，它还含 $0$、两个 $h_7$ 根、
$1$ 的四条 $Y=\infty$ 链中的十五个素例外分量，
每个系数为一。$d$ 处和 $(T,Z)=(0,0)$ 处的两条二步链不在
$E_\infty$ 中，但它们的四个原角条件仍在 $C$ 和所有截面格中。
因此下文的边界不能只用最高几条 $Y$ 系数代替。

为免和目标长度混淆，$c\ge0$ 始终是固定增权整数，记
$$
V_c=H^0(X,\mathcal O_X(3C+cE_\infty)),\qquad
Y_3=3C,\qquad L_c=\mathcal O_{Y_3}(3C+cE_\infty).
\tag{4}
$$
所有来源在原仿射多项式框中读取。

## 2. 所需上同调与来源维数完全可算

**引理 1。** 对每个 $c\ge0$，
$$
H^1(X,\mathcal O_X(cE_\infty))=
H^1(X,\mathcal O_X(3C+cE_\infty))=0,
\tag{5}
$$
相应 $H^2$ 也为零，并且
$$
h^0(X,\mathcal O_X(cE_\infty))=1+2c^2+3c,
\tag{6}
$$
$$
\boxed{\dim V_c-\dim V_0=3c\,d_\infty+2c^2+3c.}
\tag{7}
$$

**证明。** 正截面的线性系无基点。
在代数闭包上选一个同类的光滑有理截面 $E$，
避开全部十九个吹起中心；其拉回仍是光滑 $\mathbf P^1$。
这仅用于证明上同调，不改变真正边界 $E_\infty$。
必要时扩域后证明，有限维上同调随后下降。

有理曲面给 $H^1(\mathcal O_X)=0$；
R495 给 $H^1(\mathcal O_X(3C))=0$。
沿 $E$ 逐次使用限制序列，限制线束的次数分别是
$4j$ 和 $3d_\infty+4j$，均非负，
所以归纳得到 (5)。
因为相应除子有效，
$H^0(K_X-cE)=H^0(K_X-3C-cE)=0$，
Serre 对偶给 $H^2=0$。
用 (3) 和 Riemann–Roch 得 (6)、(7)。$\square$

(7) 是全来源的维数差。
例如 $c=2$ 得 $6u+24b+14$，$c=3$ 得 $9u+36b+27$。
下一节说明这些常数在真正 $3C$ 输出中全部消失。

## 3. 除去完整 F³ 核后的准确有限边界

令
$$
D_c=Y_3\cap cE_\infty .
\tag{8}
$$
$E_\infty$ 不含 $C$，故它在 $Y_3$ 上是有效 Cartier 除子。
$D_c$ 是有限局部完全交，不要求交点横截或各分支光滑。
其准确长度为
$$
\boxed{\operatorname{length}D_c=3c\,d_\infty.}
\tag{9}
$$

R498 已付
$H^1(Y_3,L_0)=0$。
由
$$
0\longrightarrow L_0\longrightarrow L_c
\longrightarrow L_c|_{D_c}\longrightarrow0
$$
得到

**定理 2。**
$$
\boxed{
\mathcal Q_c:=
H^0(Y_3,L_c)/H^0(Y_3,L_0)
\ \simeq\
H^0(D_c,L_c|_{D_c}),
\qquad
\dim\mathcal Q_c=3c\,d_\infty.
}
\tag{10}
$$

来源端同样完全准确。由 (5)，
$$
0\longrightarrow F^3H^0(X,\mathcal O_X(cE_\infty))
\longrightarrow V_c
\longrightarrow H^0(Y_3,L_c)\longrightarrow0 .
$$
因此
$$
\boxed{
\mathcal Q_c
=
V_c/
\left(V_0+F^3H^0(X,\mathcal O_X(cE_\infty))\right).
}
\tag{11}
$$
两个被商去的来源交集为 $kF^3$。
确实，$E_\infty$ 不含 $C$；
若一个只允许在 $E_\infty$ 有极的函数乘 $F^3$ 后已在 $V_0$，
则该函数在 $E_\infty$ 泛点没有极，因而是 $X$ 上的常数。

所以 (7) 中的
$2c^2+3c=h^0(cE_\infty)-1$
恰被真实 $F^3$ 核消去。这是实际限制核，不是维数上的猜测。

### 对真实新高列的统一上界

R517 的两 charge 切向来源、R514 的三 charge forcing 来源
分别属于 $V_2,V_3$，且仍乘同一个 $t^rQ/d^{C_D}$。
在原低 $\ell$ 高块中 $F^3=0$，
所以它们在显示的完整 $\mathcal H_3$ 首像以外新增的秩至多
$$
\boxed{
c=2:\ 6u+24b,\qquad
c=3:\ 9u+36b.
}
\tag{12}
$$
(12) 是上界，不宣称它被达到。
这些新列还必须满足 R514/R517 已付的实际同预算条件。
本篇没有将整个 $V_c$ 自动加入原 $\mathcal W_D$：
$V_c$ 是用于限制和比较的几何空间，只有已返回的列是原来源。

如果 $u=O(b)$、$c$ 固定，则 (12) 仅为 $O(b)$。
因此在 $D\asymp\sqrt p$、二次主阶为 $b^2$ 的临界窗，
固定清极的额外来源容量本身不能支付一个非零二次主阶缺口。
这不排除一条特殊 forcing 非零已经足以解决某个实际障碍；
容量上界与特殊非零配对是两个不同的结论。

## 4. 原真行的边界限制就是准确对偶

保 R498 的实际高目标子概形 $Z_\eta\subset Y_3$，
支撑在 $P$。在低 $\ell$ 范围
$1\le\ell\le r<h$、$k=2h+r-s$、$0\le k<\ell$ 中可写成
$
\mathscr I_\eta=(t^S,(\zeta-\eta_0)^2)
\subset k[[t]][\zeta]/(\zeta^3),
\qquad S=s-r,\quad 2h\ge S.
\tag{13}
$$
$Z_\eta$ 的长度是 $2S$。
完整目标单位仍使用同一个 $t^rQ_{\rm phys}/d^{C_D}$。
取几何真行
$$
\Phi\in
H^0\!\left(Y_3,\operatorname{Hom}
(\mathscr I_\eta,K_X|_{Y_3})\right).
\tag{14}
$$
若要称它为整个原 $J$ 的真行，仍须通过 R498 的全部原列测试。

因为 $D_c$ 与 $P$ 不相交，(14) 在 $D_c$ 上是一个正则的
$K_X$ 截面，故有真实限制
$$
\operatorname{res}_{D_c}\Phi\in H^0(D_c,K_X|_{D_c}).
\tag{15}
$$
局部完全交的伴随公式给
$$
\omega_{D_c}
=\mathcal O_{D_c}(K_X+3C+cE_\infty).
$$
因此
$$
\boxed{
\mathcal Q_c^*
=
H^0\!\left(D_c,
\omega_{D_c}\otimes(L_c|_{D_c})^{-1}\right)
=
H^0(D_c,K_X|_{D_c}).
}
\tag{16}
$$
这是准确的有限残数对偶，包含全部重交点和例外分量。

**定理 3。** 对任何 $G\in V_c$，在原框中取其在 $P$ 的高 jet，
则
$$
\boxed{
\lambda_\Phi(G)
=
-\operatorname{TrRes}_{D_c}
\left((G|_{D_c})(\Phi|_{D_c})\right).
}
\tag{17}
$$
乘积按 (16) 取值于 $\omega_{D_c}$。
因此其配对只依赖 (11) 中的边界类。

**证明。** $G\Phi$ 是 $Y_3$ 上的对偶化微分，
允许的极仅在 $P$ 和 $D_c$。
全局残数定理把 $P$ 处原 R498 配对的残数，
变成其余边界残数的负和。
也可直接对
$0\to L_0\to L_c\to L_c|_{D_c}\to0$
作 Serre 对偶，所得边界迹正是 (17)。
该论证适用于非约化的 Gorenstein 曲线 $Y_3$；
不能只对其约化正规化作普通残数后漏掉 normal 两层。$\square$

例如 R517 的切向行条件可准确改写为：
$\Phi|_{D_2}$ 杀所有
$(\mathfrak m_2\mathcal V_FH)|_{D_2}$，$H\in\mathcal H_2$。
这与 R517 的三层转置是同一个实际列测试，
但全局所需的角与 normal 相容现在集中在一个确定的有限边界上。

## 5. 边界非零到原高 jet 之间仍有一个准确核

(10) 不能直接当原余核。
定义两个真实局部评价
$$
\varepsilon_0:H^0(Y_3,L_0)\to H^0(Z_\eta,L_0|_{Z_\eta}),
\qquad
\varepsilon_c:H^0(Y_3,L_c)\to H^0(Z_\eta,L_0|_{Z_\eta}).
$$
因为 $E_\infty$ 与 $P$ 不相交，两个局部线束使用同一个原框。
于是有有定义的映射
$$
\tau_c:\mathcal Q_c\longrightarrow\operatorname{coker}\varepsilon_0.
$$
完整蛇形序列给
$$
\boxed{
H^0(Y_3,\mathscr I_\eta L_c)
\longrightarrow\mathcal Q_c
\xrightarrow{\tau_c}\operatorname{coker}\varepsilon_0
\longrightarrow\operatorname{coker}\varepsilon_c
\longrightarrow0.
}
\tag{18}
$$
特别
$$
\boxed{
\ker\tau_c
=
\operatorname{res}_{D_c}
H^0(Y_3,\mathscr I_\eta L_c).
}
\tag{19}
$$
右边是按 (10) 的边界类读取；不是任意有限边界值。

设 $\mathcal B_c\subset\mathcal Q_c$ 是某族**已付原来源**
的边界像，$v\in\mathcal Q_c$ 是一个新的实际候选。
它在原高目标中被显示的 $\mathcal H_3$ 和这族来源吸收，
准确当且仅当
$$
\boxed{v\in\mathcal B_c+\ker\tau_c.}
\tag{20}
$$
如果还允许其余原 $\mathcal W_D$ 列，则须把它们真实低行消元后的像继续加入。
因此 (20) 也未将显示来源的余核冒称整个 $J$ 的余核。

(17) 中来自 (14) 的边界行自动杀 (19)。
反之，一个随意指定的边界残数未必能扩成 (14)：
这正是边界非零还不能直接推出原 jet 非零的地方。

## 6. 同一个三 charge 乘子的切向来源确实已付

为与 R514 forcing 使用同一边界，取
$$
\mathfrak m_3=Y^3\,M(t),\qquad
M(t)=t(t-1)^2h_7^3d^2.
\tag{21}
$$
R514 的 forcing 是
$$
G_K=\mathfrak m_3K_F\in V_3.
$$
对任意 $H\in\mathcal H_2$，还准确有
$$
\boxed{
G_H=\mathfrak m_3\mathcal V_FH\in V_3,\qquad
d^{-C_D}t^rQG_H\in\mathcal W_{D_0+3}.
}
\tag{22}
$$
证明直接用 R517 (7)：
$\mathfrak m_3$ 的角值
$(1,9,3,7,5)$ 补齐
$(0,-4,-3,-2,0)$ 的全部损失。
每个中间有限 $Y=\infty$ 链也保非负余量，
$d$ 链余量至少 $j+3$，无穷远链至少 $j+3$；
ambient 帽为 $(3b+3,3u)$。
所以 (22) 保完整十九角和原列帽。
若要使用同 $D$ 的原行，须保 $D_0+3\le D$；
否则只对扩大后的原矩阵成立。

以下记 $\mathcal B_{\rm tan}\subset\mathcal Q_3$
为 (22) 的实际边界像。
它未被赋新的中央零。

## 7. 一个杀全部切向来源的显示边界残数

写原多项式
$$
F(t,Y)=f(t)Y^b+\text{较低 }Y\text{ 次数},\qquad f\ne0.
$$
在代数闭包中取 $f$ 的一个有限根 $t_0$，其重数为 $m\ge1$，
并假设
$$
t_0\notin\{0,1,-1/8\},\qquad h_7(t_0)\ne0.
\tag{23}
$$
这对应未吹起固定角以外的 $C$ 与 $Y=\infty$ 的交点。
允许交点重切；不要求 $f'(t_0)\ne0$。

对 $G\in V_3$，记 $G_{3b+3}(t)$ 为其最高允许 $Y$ 系数。
定义
$$
\boxed{
\rho_{t_0}([G])=
\operatorname{Res}_{t=t_0}
\frac{G_{3b+3}(t)}
{t\,M(t)\,f(t)^3}\,dt.
}
\tag{24}
$$
这是 $\mathcal Q_3$ 上有定义的线性泛函。

确实，$V_0$ 的 $Y$ 次数不超过 $3b$，故对它为零。
若 $G=F^3B$、$B\in H^0(X,\mathcal O_X(3E_\infty))$，
则最高系数是 $f^3B_3(t)$；
$B_3$ 在所有有限 $t$ 正则。
由 (23)，$tM(t)$ 在 $t_0$ 为单位，
所以 (24) 同样为零。由 (11) 即得所称的良定义性。
这个泛函是 (16) 某条有限边界行的显示表达，
但没有预先假定它能扩成 (14)。

若 $h(t)$ 是 $H\in\mathcal H_2$ 的 $Y^{2b}$ 系数，
则
$$
(\mathcal V_FH)_{3b}
=b\left(f\delta_t h-2(\delta_t f)h\right).
$$
所以
$$
\frac{(G_H)_{3b+3}}{tM f^3}\,dt
=b\,d(h/f^2).
$$
一个有理函数的微分在每点留数为零。因此

**定理 4。**
$$
\boxed{\rho_{t_0}(\mathcal B_{\rm tan})=0.}
\tag{25}
$$
这对同一真实 $\mathcal H_2$ 的全部截面成立，
不是只检其中的最高 charge 单列，也没有增加自由边界数据。

## 8. 同一残数对三次 forcing 的准确值

保原
$$
A_0=6(1-t),\qquad B_0=-(1+2t),\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2}.
$$
R514 的三次表达的最高 $Y$ 系数准确为
$$
\begin{aligned}
(K_F)_{3b}
={}&b^3f^3\mathcal R\\
&+b^2A_0\left(f^2\delta_t^2f
-f(\delta_tf)^2\right)
+b^2B_0f^2\delta_tf .
\end{aligned}
\tag{26}
$$
只使用原 $\mathcal E$ 对 charge $b$ 的真实作用。

下式的 $d\log f=f^{-1}df$、$\delta_t\log f=t f'/f$ 只是有理微分，未调用正特征完整 log。将 (26) 代入 (24)，得到
$$
\rho_{t_0}([G_K])
=b^2\operatorname{Res}_{t_0}
\left[
\frac{b\mathcal R}{t}\,dt
+A_0\,d(\delta_t\log f)
+B_0\,d\log f
\right].
$$
(23) 使第一项正则。
对第二项分部积分，
$$
\operatorname{Res}A_0\,d(\delta_t\log f)
=-\operatorname{Res}(\delta_tA_0)\,d\log f.
$$
而 $B_0-\delta_tA_0=-1+4t$。
故得到

**定理 5。**
$$
\boxed{
\rho_{t_0}([G_K])=b^2m(4t_0-1).
}
\tag{27}
$$
重数 $m$ 在剩余域中读取。
特别若
$$
p\nmid bm,\qquad t_0\ne1/4,
\tag{28}
$$
则
$$
\boxed{[G_K]\notin\mathcal B_{\rm tan}\subset\mathcal Q_3.}
\tag{29}
$$
这是一个全参数、可直接检验的非零边界类。
若 $t_0$ 只在有限扩域中出现，(29) 经忠实平坦下降仍是原域的非包含。
没有用有限素数样本证明其存在；
也没有假定每个实际候选的最高系数都必有满足 (23)、(28) 的根。

(27) 与 R517 的垂直分歧结论不同。
这里在 $Y=\infty$ 的固定全局边界上读相对切向像，
并将 R514 同一三次多项式真正代入；
R517 则证明有限分歧处 $e^2\mathcal F_F$ 的标量极不能免费除去。
两者都不把一个形式微分认作新的算术来源。

## 9. (27) 仍须穿过同一个原有限 jet 核

将
$$
v_K=[G_K]\in\mathcal Q_3
$$
代入 (20)。在已付的显示来源范围内，
原 forcing 高输出是否被 $\mathcal H_3$ 与切向来源吸收，
准确判据是
$$
\boxed{
v_K\in\mathcal B_{\rm tan}+
\operatorname{res}_{D_3}
H^0(Y_3,\mathscr I_\eta L_3).
}
\tag{30}
$$
(27) 已把第一项上的泛函严格算成零，
并把 $v_K$ 上的值算成显示非零量。
剩下的准确问题是：
同一真实 $\mathscr I_\eta$ 的截面能否在边界上提供这个值，
以及其余原列是否继续吸收。

例如若另有证明
$$
\rho_{t_0}\!\left(
\operatorname{res}_{D_3}
H^0(Y_3,\mathscr I_\eta L_3)
\right)=0,
\tag{31}
$$
则 (27)、(28) 会排除 (30)。
本篇没有把 (31) 当成自动成立：
它等价于这个边界行能通过原高 jet 的兼容核，
还需要原低行高尾及其余来源测试才能成为整个 $J$ 的真行。

恢复 $M=c_*U_0m_{13}J$ 时继续按 R517 的整拉回，
保全部 $P_{134}$、十三自由行、两条十三行 carry 和原第三精度。
(27) 是约化的边界非零，不是已经计算完原首次 Bockstein，
也不将目标 Euler 共振替换为新的中央导数非零。

本篇完成了准确有限边界、全局残数转置及原三次 forcing 的一个显示非零类。
下一未付接口已具体化为 (30) 的同一全局截面边界像；
三条原完整中央仍没有传播到这些返回源。
