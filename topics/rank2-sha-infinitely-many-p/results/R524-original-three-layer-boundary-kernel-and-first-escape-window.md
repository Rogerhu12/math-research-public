# R524 — 原三层边界核与第一逃逸层的准确范围

日期：2026-11-14。**状态：已证明。** 本篇继续 R521 的显示边界残数，
准确分解它还必须穿过的
$H^0(3C,\mathscr I_\eta L_c)$。
这个核具有三层，但不是三个截面空间的直和；
两个全局连接映射给出同一个实际修正的相容条件。
两个连接均写成原有限 jet 矩阵的显示类。

最内层是 $N_C(cE_\infty)(-qP)$，完全不随实际 $\eta$ 的高轴参数变化。
对 R521 的非固定角根，该层在一个明确的小 $q$ 范围已能改变显示残数，
故该残数不能扩成原真行；而在
$q>\kappa+c d_\infty$ 时该层严格为零。
低 $\ell$ 的二次临界窗最终落在后一范围，
因此剩余边界逃逸必须经过两个仍保留的全局连接，不能再归给任意 $F^2$ 修正。

## 1. 原对象与完整比较空间

保 R495、R498、R511、R514、R517、R521 的同一曲面、因子和原目标：
$$
\kappa=C^2,\qquad \chi=-K_XC\ge2b,\qquad
E_\infty=\pi^*S_\infty,\qquad
d_\infty=C E_\infty=u+4b,\qquad N=\mathcal O_C(C).
$$
低 $\ell$ 范围为
$$
1\le\ell\le r<h<s,\qquad
0\le k=2h+r-s<\ell,\qquad
S=s-r=2h-k,\qquad q=h-k.
\tag{1}
$$
特别 $q+h=S$、$\eta_0^2=0\bmod t^S$，其中
$
\eta_0=t^h v,\qquad v(0)\ne0.
$
它来自同一个原 regularized 轴和同一个 $F$，不是自由函数。
$d_\infty$ 中的 $u$ 始终是 R495 的次数参数。

对 $j\ge1,c\ge0$ 置
$$
L_{j,c}=\mathcal O_{jC}(jC+cE_\infty),\qquad
\mathcal H_{j,c}=H^0(X,\mathcal O_X(jC+cE_\infty)).
\tag{2}
$$
这些空间保全部十九个角和准确次数帽。
逐 charge 的角整除给相应有限自由整格，约化准确为 (2)；
不从特征零维数推断物理像饱和。

R521 的边界商为
$$
\mathcal Q_c=H^0(3C,L_{3,c})/H^0(3C,L_{3,0}),
\qquad
D_c=(3C)\cap(cE_\infty),
$$
$$
\mathcal Q_c\simeq H^0(D_c,L_{3,c}|_{D_c}),\qquad
\dim\mathcal Q_c=3c d_\infty .
\tag{3}
$$
只有 R514/R517 证明返回原格的列才是新增原来源。
$\mathcal H_{j,c}$ 在本篇用作同一实际因子曲面的完整比较空间，
不被自动赋予原来源预算或中央零。

## 2. 三个层之间的准确短正合列

在 $3C$ 上用 R498 的原正规坐标
$\zeta=\log(Y/\psi)\bmod F^3$。
置
$$
\mathscr I_\eta=(t^S,(\zeta-\eta_0)^2)
\subset\mathcal O_{3C,P}^{\wedge}.
$$
在 $P$ 外取整个结构层。
在 $2C$ 上，同一镜轴理想为
$$
\mathscr I_{\rm mir}=(t^S,\zeta-2\eta_0)
\subset\mathcal O_{2C,P}^{\wedge}.
$$
定义
$$
\mathcal K_{3,c}=\mathscr I_\eta L_{3,c},\qquad
\mathcal K_{2,c}=\mathscr I_{\rm mir}L_{2,c},
$$
以及 $C$ 上三条真实线束
$$
\boxed{
A_c=N(cE_\infty)(-qP),\quad
B_c=N^2(cE_\infty)(-hP),\quad
C_c=N^3(cE_\infty)(-SP).
}
\tag{4}
$$

**定理 1。** 在相应厚化曲线上，准确有
$$
\boxed{
0\longrightarrow A_c
\xrightarrow{\ F\ }
\mathcal K_{2,c}
\longrightarrow B_c\longrightarrow0,
}
\tag{5}
$$
$$
\boxed{
0\longrightarrow\mathcal K_{2,c}
\xrightarrow{\ F\ }
\mathcal K_{3,c}
\longrightarrow C_c\longrightarrow0 .
}
\tag{6}
$$
将 $C$、$2C$ 的层推前到 $3C$ 后理解这些式子。

**证明。** 先对 (5) 写一个二层截面
$H=h_0+\zeta h_1$。
镜轴条件准确为
$$
h_0+2\eta_0h_1=0\bmod t^S .
$$
于是 $h_0$ 必须被 $t^h$ 整除；
反过来对任何这样的局部 $h_0$，
可解 $h_1=-h_0/(2\eta_0)\bmod t^q$。
所以值层正是 $B_c$。
若 $h_0=0$，则 $h_1$ 须被 $t^q$ 整除，
给最内层 $A_c$。
$F/\zeta$ 是同一个单位，故以 $F$ 而不是形式 $\zeta$ 表示嵌入时，
只运输这个原单位，不改变线束和消失阶。

再取 $G=g_0+\zeta g_1+\zeta^2g_2$。
原高块条件为
$$
g_0+\eta_0g_1=0\bmod t^S,\qquad
g_1+2\eta_0g_2=0\bmod t^S.
\tag{7}
$$
因 $\eta_0^2=0$，第一式等价于 $g_0=0\bmod t^S$。
因此值层是 $C_c$，且局部任意被 $t^S$ 整除的值都可提升。
核是 $F H$。在高块中 $F=\zeta(e+f_2\eta_0)$，
其中 $e=(\mathcal EF)|_C$、$f_2=(\mathcal E^2F)|_C$，
括号是单位。故 $FH$ 的消失准确等价于同一镜轴
$H(t,\psi e^{2\eta_0})=0\bmod t^S$，即 (5) 中的理想。
这证明 (6)，包括两个局部生成元的全部条件。$\square$

三个层的次数准确为
$$
\boxed{
\deg A_c=\kappa+c d_\infty-q,\quad
\deg B_c=2\kappa+c d_\infty-h,\quad
\deg C_c=3\kappa+c d_\infty-S.
}
\tag{8}
$$

## 3. 全局核不是这三个空间的直和

记
$$
K^{(0)}_c=H^0(3C,\mathcal K_{3,c}),\quad
K^{(1)}_c=H^0(2C,\mathcal K_{2,c}),\quad
K^{(2)}_c=H^0(C,A_c).
$$
由 (5)、(6)，完整全局条件是
$$
\boxed{
0\to K^{(2)}_c\to K^{(1)}_c\to
H^0(C,B_c)\xrightarrow{\alpha_\eta}H^1(C,A_c),
}
\tag{9}
$$
$$
\boxed{
0\to K^{(1)}_c\to K^{(0)}_c\to
H^0(C,C_c)\xrightarrow{\beta_\eta}
H^1(2C,\mathcal K_{2,c}).
}
\tag{10}
$$
$\alpha_\eta,\beta_\eta$ 依赖同一个真实 $\eta_0$；
不能把两个值层独立选取后称为同一个原修正。

作为长度核对，伴随公式给
$2p_a(C)-2=\kappa-\chi$。
由 (8)，
$$
\chi(\mathcal K_{3,c})
=\frac{9\kappa+3\chi}{2}+3c d_\infty-2S.
\tag{11}
$$
它恰等于 $h^0(3C,L_{3,c})$ 减去原高目标长度 $2S$。
(11) 只核 Euler 特征；并不假定 (9)、(10) 的连接具有最大秩。

## 4. 两个连接都能在同一个原有限矩阵中准确读取

R521 的上同调证明同时给
$$
H^1(X,\mathcal O_X(jC+cE_\infty))=0
\quad(j,c\ge0).
\tag{12}
$$
确实，从 R495 的 $H^1(jC)=0$ 开始沿一般正截面逐步限制，
其限制次数是 $j d_\infty+4c\ge0$。
同时
$$
H^1(C,N^j(cE_\infty))=0\quad(j\ge1),
$$
因为其对偶次数为
$(1-j)\kappa-\chi-cd_\infty<0$。
所以以下全局提升和有限 jet 余核识别均有支付。

定义实际约化接触和镜轴矩阵
$$
E_q^{(c)}:\mathcal H_{1,c}\to k[t]/t^q,\quad
H\mapsto H(t,\psi)\bmod t^q,
$$
$$
E_{\rm mir}^{(c)}:\mathcal H_{2,c}\to k[t]/t^S,\quad
H\mapsto H(t,\psi e^{2\eta_0})\bmod t^S.
\tag{13}
$$
它们使用 (2) 的真正有限列；没有补独立法向数据。
因 $q\le h$，第一式也等于同一原 $\bar g$ 的该长度评价。
准确有
$$
\operatorname{coker}E_q^{(c)}=H^1(C,A_c),\qquad
\operatorname{coker}E_{\rm mir}^{(c)}
=H^1(2C,\mathcal K_{2,c}).
\tag{14}
$$

### 第一连接

给定 $v_2\in H^0(C,B_c)$，
用 (12) 选择同一 $\mathcal H_{2,c}$ 中的 $H_2$ 提升它。
其镜轴值被 $t^h$ 整除。
则
$$
\boxed{
\alpha_\eta(v_2)
=
\left[
\frac{E_{\rm mir}^{(c)}(H_2)}{2e\eta_0}
\right]\in\operatorname{coker}E_q^{(c)} .
}
\tag{15}
$$
除法只在已知的 $t^h$ 像中进行，读长 $q=S-h$。
不同提升差一个 $F H_1$，而
$$
E_{\rm mir}^{(c)}(F H_1)
=2e\eta_0 E_q^{(c)}(H_1)\pmod{t^S}.
$$
因此 (15) 良定义并恰是 (9) 的连接。

### 第二连接

给定 $v_3\in H^0(C,C_c)$，
用 (12) 取 $G\in\mathcal H_{3,c}$ 提升它。
在原正规框中写
$$
G=g_0+\zeta g_1+\zeta^2g_2,\qquad
g_0=0\bmod t^S .
$$
由于
$$
F=\zeta(e+f_2\eta_0)
$$
于同一高目标中，(7) 的整个目标可准确除去这个指定的 $F$ 像，
得到长度 $S$ 的向量
$$
f_G=\frac{g_1+2\eta_0g_2}{e+f_2\eta_0}\pmod{t^S}.
$$
所以
$$
\boxed{
\beta_\eta(v_3)
=
[f_G]\in\operatorname{coker}E_{\rm mir}^{(c)} .
}
\tag{16}
$$
不同提升差一个 $F H_2$，故 $f_G$ 改变同一个
$E_{\rm mir}^{(c)}(H_2)$，证明良定义。

(15)、(16) 保同一 $\eta_0$、完整分母单位和同一列格。
尤其 (16) 不能只读 $g_1$ 或只读 $g_2$；
它们是同一个实际 $G$ 的正规展开。

## 5. 最内层与全部高轴参数无关

由 (5)、(6)，$K^{(2)}_c$ 在 $K^{(0)}_c$ 中的像是
$$
\boxed{F^2H,\qquad
H|_C\in H^0(C,N(cE_\infty)(-qP)).}
\tag{17}
$$
每个这样的 $H|_C$ 均可由 $\mathcal H_{1,c}$ 提升，因 (12) 保限制满射。

在原高块中，
$$
F^2H=2a\epsilon\,e^2\eta_0(H|_C).
$$
它为零恰因 $\operatorname{ord}_P(H|_C)\ge q$，
以及 $h+q=S$。
这个包含只使用 $\operatorname{ord}\eta_0=h$、$\eta_0^2=0$；
因此对保持这些数据的全部实际高轴参数一致。
没有为不同的完整中央参数另选来源或随意改变 $\xi$。

$K^{(2)}_c$ 的消失范围也完全准确：
$$
\boxed{
q>\kappa+c d_\infty
\quad\Longrightarrow\quad
K^{(2)}_c=0.
}
\tag{18}
$$
这是负度给出的消失。
等号时是零次线束，不能自动判定零。

(17) 是 R521 几何比较空间的实际限制核，
不声称每个 $\mathcal H_{1,c}$ 列均已成为原
$\mathcal W_D$ 的新列。
它之所以可以用于判断边界行能否延拓，
是因为这些截面的原有限高评价已经严格为零，
而非因为给了它们新的算术零。

## 6. 显示边界残数在第一层上的真实值

现在取 R521 的 $c=3$ 与
$$
F=f(t)Y^b+\cdots,\qquad
M(t)=t(t-1)^2h_7^3d^2 .
$$
令 $t_0$ 是 $f$ 的一个有限根，重数 $m$，
并继续保
$$
t_0\notin\{0,1,-1/8\},\quad h_7(t_0)\ne0,\quad
p\nmid bm,\quad t_0\ne1/4 .
\tag{19}
$$
R521 的边界泛函为
$$
\rho_{t_0}([G])
=\operatorname{Res}_{t_0}
\frac{G_{3b+3}(t)}{tM(t)f(t)^3}\,dt .
\tag{20}
$$
它杀同一乘子的切向来源，且
$\rho_{t_0}([G_K])=b^2m(4t_0-1)\ne0$。

对 (17) 的 $G=F^2H$，
令 $h(t)$ 为 $H$ 的最高 $Y^{b+3}$ 系数。则
$$
\boxed{
\rho_{t_0}([F^2H])
=\operatorname{Res}_{t_0}\frac{h(t)}{tM(t)f(t)}\,dt.
}
\tag{21}
$$
这是一个真实边界 jet，而不是任意指定的值。

若 $Q=(t_0,Y=\infty)$ 在 $C$ 上光滑，
则 $E_\infty$ 与 $C$ 在 $Q$ 的交数为 $m$。
(21) 通过线束
$A_3=N(3E_\infty)(-qP)$ 在 $mQ$ 上的限制因子化，
并是该长度 $m$ jet 的一个非零线性泛函。

证明如下。设 $x=1/Y$，则曲线的局部方程为
$f(t)+x f_{b-1}(t)+\cdots=0$。
$m=1$ 时 (21) 只读点值。
$m>1$ 且 $Q$ 光滑时必有 $f_{b-1}(t_0)\ne0$，
所以 $t-t_0$ 是 $C$ 的局部参数、$x$ 的阶准确为 $m$。
$H$ 的原线束框内的值为 $h(t)+x(\cdots)$，
故模 $mQ$ 正是 $h(t)$。
又 $tM$ 在 $Q$ 是单位，$f$ 有 $m$ 重零，
所以 (21) 读到长度 $m$ jet 的最高系数乘单位，确为非零泛函。

若 $C$ 在该边界点奇异，本段的光滑点 jet 结论不自动适用；
R521 的完整局部完全交残数仍保持有效。

## 7. 显示残数不能延拓为真行的统一小 q 范围

**定理 2。** 在 (19) 且 $Q$ 光滑的条件下，若
$$
\boxed{q\le\chi+3d_\infty-m-1,}
\tag{22}
$$
则
$$
\boxed{
\rho_{t_0}\!\left(
\operatorname{res}_{D_3}K^{(2)}_3
\right)=\bar k .
}
\tag{23}
$$
本节将全部空间同时扩到包含 $Q$ 的代数闭剩余域上读取。
特别该显示边界行不杀同一扩域后 R521 的 $\ker\tau_3$，
因此不能延拓为同一扩域后 R498 的原高 jet 真行。
若要使用原域定义的迹或线性组合，仍须测试那个组合；
不能从单点残数非零推断其域迹非零。

**证明。** 在 $C$ 上
$$
\deg\bigl(\omega_C\otimes A_3^{-1}(mQ)\bigr)
=q-\chi-3d_\infty+m .
$$
(22) 使此次数严格为负。
所以 $H^1(C,A_3(-mQ))=0$，
评价
$H^0(C,A_3)\to A_3|_{mQ}$ 满射。
第6节证明 (21) 是该 jet 上的非零线性泛函，
故得到 (23)。
(17) 给这些截面确在 $K^{(0)}_3$ 中，
R521 (19) 再给其边界像在 $\ker\tau_3$ 中。$\square$

当 $m=1$，条件是
$q\le\chi+3d_\infty-2$。
这并不证明整个 forcing 边界类已被吸收：
只证明这个单独的显示残数无法区分它和真实有限 jet 核。
若取 (21) 的值等于 $b^2m(4t_0-1)$，
仍须比较完整边界向量，而不是只比较一个标量。

(23) 对所有保持 $h,S$ 的实际高轴参数一致，
因为使用的是 (17) 中与 $\eta_0$ 参数无关的同一最内层。
因此不能用三条完整中央所确定的高参数，
免费删去这个已存在的边界逃逸。

## 8. 简单交点处三层各自读取什么

为显示剩余条件的真实内容，另取 $m=1$。
置
$$
T(t)=tM(t)f'(t),\qquad
D_f=(f'(t))^{-1}\partial_t .
$$
这些在 $t_0$ 均合法。对相应多项式的最高允许 $Y$ 系数，
有准确公式
$$
\boxed{
\begin{aligned}
\rho_{t_0}(F^2H_1)
&=\left.\frac{h_1}{T}\right|_{t_0},\\
\rho_{t_0}(F H_2)
&=\left.D_f\!\left(\frac{h_2}{T}\right)\right|_{t_0},\\
\rho_{t_0}(G)
&=\left.\frac12D_f^2\!\left(\frac{g}{T}\right)\right|_{t_0}.
\end{aligned}}
\tag{24}
$$
其中 $h_1,h_2,g$ 分别是 charge
$b+3,2b+3,3b+3$ 的系数。
证明是用 $z=f(t)$ 作局部变量，
$dt=dz/f'(t)$，逐一取 $z^{-1}$ 留数。

(24) 只说明同一个边界泛函在三层上的坐标读法。
这些点值、一阶和二阶值不是三个独立可选参数：
要进入 $K^{(0)}_3$，
$H_2$ 的值层必须通过 (15)，
$G$ 的值层必须通过 (16)，
而完整原列与低行高尾仍须继续保留。
(9)、(10) 正是不能把 (24) 独立解开的全局约束。

## 9. 二次临界窗中第一逃逸层确实消失

考虑每个已经存在的实际候选，
并明确假设
$$
\kappa\asymp b^2,\qquad \chi=O(b),\qquad
u=O(b),\qquad r,k=O(b),\qquad
h/\kappa\longrightarrow9/8 .
\tag{25}
$$
这是 R495 的低 $\ell$ 二次主阶接口；
本篇不从人工曲线族推断原 theta 必有这样的接触。

固定 $c$ 时，由 $q=h-k$、$S=2h-k$，
(8) 准确给主阶
$$
\boxed{
\deg A_c=-\tfrac18\kappa+O(b),\quad
\deg B_c=\tfrac78\kappa+O(b),\quad
\deg C_c=\tfrac34\kappa+O(b).
}
\tag{26}
$$
所以 (18) 最终成立，最内 $F^2$ 逃逸层为零。
剩余核必须经
$$
\ker\alpha_\eta\subset H^0(C,B_c),\qquad
\ker\beta_\eta\subset H^0(C,C_c)
$$
及同一全局提升产生。
它们的次数并没有变成负数，不能再用 (18) 把它们一起删除。

这给 R521 的显示非零边界类一个准确的下一比较对象：
在真正二次临界窗，只需继续判断两个已写成有限矩阵
(15)、(16) 的连接所产生的边界一阶、二阶值。
仍未证明这些值必须为零，也未证明能支付 forcing 的单位。

## 10. 原 J/M 与完整中央的范围

R521 的准确吸收判据继续是
$$
[G_K]\in\mathcal B_{\rm tan}+
\operatorname{res}_{D_3}K^{(0)}_3 .
$$
本篇把第二项分解为 (9)、(10)，并付清最内层的两个明确范围。
显示边界单位没有被冒称原 $J$ 余核非零；
显示残数不能延拓的范围也没有被冒称整个 forcing 已吸收。

恢复原矩阵时仍保
$M=c_*U_0m_{13}J$、R517 的整左行拉回、
全部 $P_{134}/U_0$、十三自由行、两条十三行 carry，
以及 R481 的同一个修正第三精度。
R502 的 $\xi$ 和活 $V_1$ 没有被 (5)–(16) 删掉。

三条原完整中央决定的实际参数必须代入同一个 $\eta_0$；
它们没有给 $\mathcal H_{j,c}$ 或切向返回源新的中央零。
下一实质问题是 (15)、(16) 的联合像能否在原预算与原完整中央下支付
R521 (27) 所需的真实边界值，不能停在 (26) 的阶段性负度结论。
