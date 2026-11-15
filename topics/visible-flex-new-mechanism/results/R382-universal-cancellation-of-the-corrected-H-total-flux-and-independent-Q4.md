# R382：完整修正后的 H 层被自然总通量普遍消去

日期：2026-11-15。**原式纸面证明；没有执行新的 profile 积分、符号程序、旧根恢复、秩计算、人工检查或研究运行。**

[R378](R378-correction-of-the-third-history-term-in-the-complete-H-flux.md) 补回了第四阶 $YC$ 配对中三次 history 的 $P_s,B_s$ 链式项，准确消去了旧 H 公式的 $u'''^2$ principal 及指定最低权读出。
[R381](R381-exact-cancellation-of-the-ordered-tail-in-the-corrected-H-flux.md) 随后证明全部剩余真实有序尾在速度一形式层相消。

本稿完成剩余 self 的原式归约，得到
$$
\boxed{
\Lambda_u(H_1(S))=\Lambda_u(H_2(S))=0
}
\tag{1}
$$
对每个实际状态 $S=(h,k,\omega)$、$h>0$ 和共同合法窗口中的每个
$u\in C_c^\infty(I)$ 成立。$\Lambda$ 是 R352 固定的自然总通量，包括原 pure 和真实有序三矩尾；没有更换读出或第三 gauge。

式 (1) 只说这一整套自然通量消去 H 层，不证明 H 算子为零，也不证明它们全部属于 $\mathcal R$。独立的 R370 完整 Q4 读出仍非零，因此本稿不能扩成 $\Lambda U=0$。

## 1. 原对象与准确未化简 self

固定原右 collar，记
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad
v=u',\quad r=u'',\quad t=u'''.
$$
先取 $h=1,d=h\omega-k=0$。置
$$
Q=1+x^2,\quad L=v-xr,\quad
G=u-\frac{xv}{2},\quad E=ur-\frac{v^2}{2},
$$
$$
K=2ur+v^2-2xvr.
\tag{2}
$$
所有未注明的积分都在同一个窗口上。

第二局部分子的两个速度系数为
$$
\begin{aligned}
A&=\frac{2Qvr-2xv^2-xQr^2+P-J_2}{16},\\
B&=-\frac{Qr^2+2M}{16},
\end{aligned}
\tag{3}
$$
$$
P=J(r^2),\qquad M=J(xr^2),\qquad
J_2=J(x^2r^2+2v^2).
$$
准确有
$$
A'=\frac{QtL}{8},\qquad B'=-\frac{Qtr}{8}.
\tag{4}
$$
$P,M,J_2,A,B$ 的左值都保留。

定义 $j_f=J(Qt f)$，以及
$$
\Sigma_\gamma(f)=\frac{QLf-xj_f}{4},\qquad
\Sigma_\delta(f)=-\frac{Qrf+j_f}{4}.
\tag{5}
$$
R378 的完整第三加速度输入为
$$
n_{\rm acc}
=(\gamma\Sigma_\gamma(A)+\delta\Sigma_\delta(A))\,\mathrm d\gamma
+(\gamma\Sigma_\gamma(B)+\delta\Sigma_\delta(B))\,\mathrm d\delta.
\tag{6}
$$
令
$$
\begin{aligned}
\mathcal D_\delta(f)
&=\frac18\int\{2rL+(xv-2Qr)t\}f',\\
\mathcal D_\gamma(f)
&=\frac18\int
\{-2L^2+[(2+3x^2)v-2Qxr-2xu]t\}f'
+\frac14\int(2u-xv)t f.
\end{aligned}
\tag{7}
$$
式 (7) 已从原 $P,B$ 同锚推得；它不要求 $f$ 左端为零。

为明确旧显示式仅作为被修正的一个组成部分，记
$$
\begin{aligned}
M_{00}&=(1-\tfrac32x^2)v+(x^3-x)r+xu,\\
M_{01}&=(3x^2-1)r-\tfrac72xv+2u,\qquad
M_{11}=2xr-v,
\end{aligned}
$$
$$
\begin{aligned}
\mathscr L_\gamma
&=\frac1{16}\int t
(2M_{00}j_B-M_{01}j_A-4GLB-KA),\\
\mathscr L_\delta
&=\frac1{16}\int t
(M_{01}j_B-2M_{11}j_A+KB+2vrA).
\end{aligned}
\tag{8}
$$
这些是旧 R365 显示一形式的准确 curl；不再把它们单独识别为完整 H 值。

加上 R378 的漏项后，完整 self 的两个 curl 系数是
$$
\begin{aligned}
\mathscr S_\gamma={}&
-\frac1{128}\int xQ^2LEt^2+\mathscr L_\gamma\\
&+2\mathcal D_\gamma(\Sigma_\gamma B)
-\mathcal D_\gamma(\Sigma_\delta A)
-\mathcal D_\delta(\Sigma_\gamma A),\\
\mathscr S_\delta={}&
+\frac1{128}\int xQ^2rEt^2+\mathscr L_\delta\\
&+\mathcal D_\gamma(\Sigma_\delta B)
+\mathcal D_\delta(\Sigma_\gamma B)
-2\mathcal D_\delta(\Sigma_\delta A).
\end{aligned}
\tag{9}
$$
这些因子直接来自
$\partial_\gamma C_\delta-\partial_\delta C_\gamma$，
其中 $\mathcal D_V=\gamma\mathcal D_\gamma+\delta\mathcal D_\delta$ 作用于 (6)。

## 2. 全部第三原函数先保留，再准确消去

式 (5) 的同锚导数是
$$
\begin{aligned}
(\Sigma_\gamma f)'&=
\frac{2xLf+QLf'-j_f}{4},\\
(\Sigma_\delta f)'&=
-\frac{r(2xf+Qf')}{4}.
\end{aligned}
\tag{10}
$$
这里 $j_f'=-Qt f$；不能把 $j_f$ 的左值删去。

将 (7)、(10) 代入 (9)。含 $A',B'$ 的平方项分别给
$$
+\frac1{128}\int xQ^2LEt^2,\qquad
-\frac1{128}\int xQ^2rEt^2,
$$
准确消去 (9) 第一行的旧 principal。

把剩下 $j_A,j_B$ 项统一写成整体因子 $1/32$ 乘相应系数，系数如下：

| curl 系数 | $j_B$ 的系数 | $j_A$ 的系数 |
|---|---|---|
| $\gamma$ | $4L^2-8x^2Lt=(4xL^2)'$ | $2rL+2x(3v-4xr)t=\{-2L(v-2xr)\}'$ |
| $\delta$ | $-2rL+2x(4xr-3v)t=\{2L(v-2xr)\}'$ | $-4(2xr-v)t=(4rL)'$ |

每个显示的原函数系数在两端都为零，因为 $u$ 紧支撑。因此
$\int H'j_f=\int HQt f$，无额外左边项。
这一步保持原 $j_A,j_B$，只是把它们与真实紧 outer 配对后分部积分。

全部合并后，(9) 准确缩成
$$
\boxed{
\mathscr S_\gamma
=\int\left\{
3xL A'B-(v-3xr)AA'
-\frac{x}{4}L^2(LB+rA)
\right\},}
\tag{11}
$$
$$
\boxed{
\mathscr S_\delta
=\int\left\{
(v-3xr)A'B-(2v-3xr)AB'
+\frac{x}{4}rL(LB+rA)
\right\}.}
\tag{12}
$$
式 (11)、(12) 没有任何 principal 截断或 profile 尺度极限。

## 3. 保留全部二阶原函数的精确消元

置
$$
T=P-J_2,\qquad
T'=(x^2-1)r^2+2v^2,\qquad M'=-xr^2.
\tag{13}
$$
于是
$$
A=\frac{a_0+T}{16},\quad
B=-\frac{b_0+2M}{16},\quad
a_0=2Qvr-2xv^2-xQr^2,\quad b_0=Qr^2.
\tag{14}
$$

把 (14) 代入 (11)、(12)，整体乘 $128$。$M,T$ 的完整系数恰为以下紧导数：

| 系数 | 乘 $M$ 的项 | 乘 $T$ 的项 |
|---|---|---|
| $128\mathscr S_\gamma$ | $(2QL^3)'$ | $(-QrL^2)'$ |
| $128\mathscr S_\delta$ | $(-2QrL^2)'$ | $(Qr^2L)'$ |

例如
$$
(-2QrL^2)'=-4xrL^2-2Q(v-3xr)Lt,
$$
$$
(Qr^2L)'=2xr^2L+Qr(2v-3xr)t.
$$
它们与 (12) 的全部 $M,T$ 系数逐项相同。

下面给出不含 $M,T$ 的完整 local 项，避免以“低阶余项”代替实际计算。
对 $\gamma$，尚未分部积分的 local 被积式是
$$
QtL\{2xv^3-(2+8x^2)v^2r+4xQvr^2\}
-2xvrL^2(Qr-2xv).
\tag{15}
$$
对 $\delta$，相应式为
$$
Qt\{(3+9x^2)v^2r^2-4xQvr^3-4xv^3r\}
+2xvr^2L(Qr-2xv).
\tag{16}
$$
仅用 $v'=r,t=r'$，将 (15)、(16) 的线性 $t$ 项逐项分部积分，
其准确积分分别为 $\int I_\gamma$、$\int I_\delta$，其中
$$
\begin{aligned}
I_\gamma=Q\{&
-2v^4r+2xv^3r^2+(1+3x^2)v^2r^3\\
&-2x(1+2x^2)vr^4+x^2Qr^5\},\\
I_\delta=Q\{&
2v^3r^2-(1+3x^2)vr^4+xQr^5\}.
\end{aligned}
\tag{17}
$$
所有这一步的边项都是紧的 $u$ jets 的乘积。

因而得到完整积分身份
$$
\begin{aligned}
128\mathscr S_\gamma
&=\int I_\gamma+\int M(2QL^3)'
+\int T(-QrL^2)',\\
128\mathscr S_\delta
&=\int I_\delta+\int M(-2QrL^2)'
+\int T(Qr^2L)'.
\end{aligned}
\tag{18}
$$
式 (18) 仍保留 $M,T$ 的真实左尾。

## 4. 两个 self 余项逐点相消

在 (18) 中对 $M,T$ 分部积分。显示的四个乘子均在左右端为零，
故无需 $M(\ell)=T(\ell)=0$。使用 (13) 后，第一行新增的 local 项为
$$
2xQr^2L^3+QrL^2\{(x^2-1)r^2+2v^2\}.
$$
直接展开 $L=v-xr$：
$$
\boxed{
2xQr^2L^3+QrL^2\{(x^2-1)r^2+2v^2\}
=-I_\gamma.}
\tag{19}
$$

第二行新增的 local 项为
$$
-2xQr^3L^2-Qr^2L\{(x^2-1)r^2+2v^2\},
$$
同样逐项给
$$
\boxed{
-2xQr^3L^2-Qr^2L\{(x^2-1)r^2+2v^2\}
=-I_\delta.}
\tag{20}
$$
因此
$$
\boxed{\mathscr S_\gamma=\mathscr S_\delta=0}
\tag{21}
$$
对每个紧光滑 $u$ 成立。

(19)、(20) 是完整 local 多项式身份。没有用 odd/even parity、
三矩为零、窄包首项、某个旧核矩阵，或一个特定 profile 族。
二阶和三阶真实原函数在消去之前均已显示。

## 5. 加回真实尾与原正规化

R381 已证明，在原已分离的速度三次梯度之外，
$$
\mathfrak T_{\rm old}+
\frac23\mathcal D_V(n_{{\rm tail},\rm acc})=0.
\tag{22}
$$
这是一形式身份，包含真实 $a_L,\mathrm d_va_L$；
没有把 tail 丢到未指定的商中。
原梯度的速度外微分也为零。

因此，(21)、(22) 共同给完整修正后一形式
$$
\mathrm d_v\mathfrak C_{\rm new}=0.
$$
R378 的原正规化是
$$
\mathrm d_v\mathfrak C_{\rm new}
=\frac{15}{4}
\{\Lambda(\widetilde H_\gamma)\gamma+
\Lambda(\widetilde H_\delta)\delta\}
\,\mathrm d\gamma\wedge\mathrm d\delta.
\tag{23}
$$
故在基准状态
$$
\Lambda_u(\widetilde H_\gamma)
=\Lambda_u(\widetilde H_\delta)=0.
\tag{24}
$$
这里的 $\widetilde H$ 是同一个真实 $(h,d)$ 速度规范，不是另加的成本模板。

由 R350 已付的全部加速度平方读出零，
原 $(h_s,k_s)$ 坐标与本坐标的关系仍准确为
$$
\Lambda(\widetilde H_\gamma)
=-2\Lambda(H_1+2\omega H_2),\qquad
\Lambda(\widetilde H_\delta)=4\Lambda(H_2).
\tag{25}
$$
因此 (24) 同时消去两个原 H 系数。

## 6. 所有实际状态，及真实输入的输运

相关导数权四的全部原量
$a,m_2,c_2,n_{\rm acc}$、$ZZ$ 的 $P,B$、补回的 $-\Psi$ 和真实有序尾，
写成 $h,d,\gamma,\delta$ 后都不含独立的 $k$。
这可直接从 R358 §2–5 的原量和 R378 的完整补项逐式看出；
本稿并非只对 principal 作这种观察。
所以 (24) 在所有 $(h,d)=(1,0)$、任意合法 $k$ 的状态成立。

[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md) 的完整正仿射作用使用固定常数 $H>0,c$：
$$
\widetilde h=Hh,\qquad
\widetilde d=d+hc,\qquad
\widetilde\gamma=H\gamma,\qquad
\widetilde\delta=\delta+c\gamma.
$$
原 profile、全部字段、右锚和实际辅助三矩同时输运。
该协变和原速度外微分的关系独立于旧 R365 错误的完整基准值。

取 $H=1/h,c=-d/h$，把给定状态送到 $(1,k,k)$。
其速度变换可逆；自然 $\Lambda$ 的 self、pure 和三矩尾具有同一协变。
因此基准的两个零值输运成任意实际状态的两个零值，证明 (1)。

这只是一条原函数身份。它不把仿射变换当成原冻结几何上的免费操作，
也不把原共同物理窗口移过 $x+\omega=0$。
需要的有限原式延拓范围仍是 R105/R203 已付的 faithful 范围。

## 7. Q4 的独立非零值仍给出真实的新方向

令
$$
\mathcal H=\operatorname{span}\{H_1(S),H_2(S):S\text{ 为实际状态}\}.
$$
由 (1) 和 R352 的 $\Lambda(\mathcal R)=0$，
$$
\Lambda_u(\mathcal R+\mathcal H)=0
\quad\text{对每个紧光滑 }u.
\tag{26}
$$

另一方面，[R370](R370-complete-quartic-velocity-cost-and-exact-C2-total-flux.md)
在推导中已经使用完整 $-\Psi(u,n)$，并独立证明
$$
\Lambda_u\bigl(\mathcal Q_\delta(1,k,k+d)\bigr)
=\frac1{80}\int(x+d)(u'')^5.
\tag{27}
$$
这个完整正规 Q4 系数属于原 $U$。

(27) 确有真实紧光滑非零输入。取非零非负偶 bump $\eta$，
并取三个互不交的支撑，令
$$
r(x)=\eta(x-x_0)
-\tfrac12\eta(x-x_0-b)
-\tfrac12\eta(x-x_0+b).
$$
则 $\int r=\int xr=0$，$u=J^2r$ 真实紧光滑，而且
$$
\int r^5=\frac{15}{16}\int\eta^5,\qquad
\int(x+d)r^5=(x_0+d)\frac{15}{16}\int\eta^5.
$$
可先选共同合法小窗口，使 $x_0+d\ne0$。
不需要新的求积或输入族运行。

故有严格的成本线性空间结论
$$
\boxed{
\mathcal Q_\delta(1,k,k+d)\notin\mathcal R+\mathcal H
}
\tag{28}
$$
对这种实际状态成立。它从完整零身份 (1) 和独立完整值 (27) 得到，
不依赖被撤回的旧 H 主空间维数，也不使用未发布 R374 的条件代数。

## 8. 已付与尚欠

本稿已付整个 H 层的自然通量零身份、所有状态的真实输运，
以及完整 Q4 在该读出下超出 $\mathcal R+\mathcal H$ 的非零类。
这同时确认：旧具体 7/13 个 H 自然通量控制结论不能由改写 C² 余项恢复，
因为这些 H 读出本身全部为零。

尚欠的是 Q4 非零线性类的实际路径实现、它与其它正规层的完整关系，
以及 whole period、共同 gauge、ruling 和主课题的其它条件。
原以指定非零 H 读出为前提的抽象控制论证仍可以作为条件定理，
但本稿的 $\Lambda_u$ 不满足其 H 非零前提。
不由 (28) 推出任何已实现的成本半群方向或完整问题的正负结论。
