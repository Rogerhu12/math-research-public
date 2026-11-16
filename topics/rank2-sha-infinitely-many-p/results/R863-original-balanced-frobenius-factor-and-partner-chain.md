# R863 — 原三差的平衡 Frobenius 因式与完整法向伙伴链

日期：2026-11-16。**状态：已证明。** 本注对 [R860](R860-original-common-odd-cross-and-balanced-partners.md) 的同一交叉算子作准确因式分解，并逐项返回原三差矩阵。它不证明该矩阵杀不掉原指定向量，也不为其伙伴添加中央零。全部证明为符号恒等，没有数学数值运行或目标素数扫描。

原来源、完整二挠规范和列符号均保持[共同 C24 注](../notes/2026-11-16-original-common-odd-degree24-and-three-row-pairing.md)。特别
$$
m=24,\quad n=n_\nu\in\{10,48,112,42\},\quad M=m+n,\qquad
E_j=-b^j\sigma^{24}x^{8-3j}y,\quad j=0,1,2,
$$
$$
C_{24}=\sum_jc_{*,j}E_j,\qquad c_*=(1,-4/7,16/7)^t,\qquad
A_\nu=C_{24}J_\nu .
\tag{1}
$$
四个 $J_\nu$ 始终是该注(6)的实际 whole 来源；$p=6s-1>211$，并保原固定坏集。$m,n,M$ 都为单位。

## 1. 同一 Witt 多项式的真实平衡坐标

在两个独立物理变量上记
$$
\mathcal D=D_1+D_2,\qquad
\mathcal N=nD_1-mD_2,\qquad
\mathcal K=\frac{\mathcal N^2}{2mnM}.
\tag{2}
$$
所以
$$
D_1=\frac{m\mathcal D+\mathcal N}{M},\qquad
D_2=\frac{n\mathcal D-\mathcal N}{M}.
$$
所有这些是互相交换的常系数微分算子；这里不对某个函数或导数作除法。

保持 R860 的整多项式
$$
\mathfrak C_p(X_1,X_2)=\frac{(X_1+X_2)^p-X_1^p-X_2^p}{p}.
$$
定义真正的整常数
$$
c_{m,n,p}=\frac{M^p-m^p-n^p}{pM^p}\in\mathbf Z_{(p)}.
\tag{3}
$$
它的整数分子被 $p$ 整除，并没有将它视为一个自由参数。

在剩余域中有完整恒等式
$$
\boxed{
\overline{\mathfrak C_p(D_1,D_2)}
=\bar c_{m,n,p}\mathcal D^p
+\frac1M\sum_{k=2}^{p-1}
 \frac{(-1)^km^{1-k}+n^{1-k}}{k}
 \mathcal D^{p-k}\mathcal N^k .
}
\tag{4}
$$
证明从(2)代回整多项式开始。$k=p$ 的两项因 $p$ 为奇数准确相消。
$k=1$ 的系数是
$-(m^{p-1}-n^{p-1})/M^p$，约化后为零。
对 $2\le k\le p-1$，使用
$\binom pk/p\equiv(-1)^{k-1}/k$、
$M^p=M$、$m^{p-k}=m^{1-k}$ 和 $n^{p-k}=n^{1-k}$，
得到(4)。没有省略任何奇数 $k$。

于是定义以下完全显示的齐次多项式：
$$
\mathcal Q_{m,n,p}(D,R)
=2mn\sum_{k=2}^{p-1}
 \frac{(-1)^km^{1-k}+n^{1-k}}{k}
 D^{p-k-1}R^{k-2}.
\tag{5}
$$
它的总次数是 $p-3$，且
$$
\boxed{
\overline{\mathfrak C_p(D_1,D_2)}
-\bar c_{m,n,p}\mathcal D^p
=\mathcal D\,\mathcal K\,
 \mathcal Q_{m,n,p}(\mathcal D,\mathcal N).
}
\tag{6}
$$
首尾系数分别为
$$
[D^{p-3}]\mathcal Q=M,\qquad
[R^{p-3}]\mathcal Q=-2mnM.
\tag{7}
$$
它们都是单位。不过(7)不是对某个指定来源的非零结论。

尤其不能把(5)换成一个只含 $R^2$ 的多项式。
它的第一个奇 $R$ 系数为
$$
[D^{p-4}R]\mathcal Q=\frac{2(m^2-n^2)}{3mn}.
\tag{8}
$$
对本注四个原伙伴，这个系数依次是
$$
\frac{119}{90},\qquad -1,\qquad-\frac{187}{63},\qquad-\frac{11}{14}.
\tag{9}
$$
四者均为原好素数处的单位，奇法向项不能因原两输入均为奇函数而删除。

### 1.1 有限核的准确一变量导数

令 $\alpha=m/M,\ \beta=n/M$，所以 $\alpha+\beta=1$，并在剩余域定义
$$
F_{m,n,p}(u)=\overline{\mathfrak C_p(\alpha+u,\beta-u)}.
$$
则
$$
\boxed{
F_{m,n,p}'(u)
=(\beta-u)^{p-1}-(\alpha+u)^{p-1}
=\frac{u^p-u}{(u-\beta)(u+\alpha)}.
}
\tag{10}
$$
最后一个商是多项式：$\beta$ 和 $-\alpha$ 是两个不同的剩余域元素，
都为 $u^p-u$ 的根。它不是一个新引入的有极函数。
准确地，
$$
F(0)=\bar c_{m,n,p},\quad F'(0)=0,\quad
[u^2](F-F(0))=\frac1{2\alpha\beta}.
\tag{11}
$$
并且 $F$ 次数恰为 $p-1$，最高系数为 $-1$。
式(10)与(4)是同一个有限多项式的两种表达。

## 2. 原除 p 行确实消去(3)，而不消去伙伴链

令 $\mu$ 表示 $z_1=z_2=z$。对每一原输入
$$
\Phi_{\nu j}=E_j(z_1)J_\nu(z_2)
$$
定义
$$
X_{\nu j}
=\left.D_z\mu\mathfrak C_p(D_1,D_2)\Phi_{\nu j}\right|_{z=0}
\pmod p .
\tag{12}
$$
R860(40)和原 $E_j(0)=j_1(E_j)=J_\nu(0)=0,\ j_1(J_\nu)=1$
准确给
$$
\mathfrak B(E_jJ_\nu)=O_j+X_{\nu j},
\qquad O_j=j_p(E_j)/p\bmod p .
\tag{13}
$$
整性只使用 R856 的相应 whole 格；不声称 $\mathscr D_m=P_m/p$
在任意 Hurwitz 级数上整。

(4)中的第一项在(12)贡献
$\bar c_{m,n,p}j_{p+1}(E_jJ_\nu)$。
原乘积是质量零的 whole degree $M$ 截面，所以 R856 给
$$
j_{p+1}(E_jJ_\nu)
\equiv H\,j_2(E_jJ_\nu)+MC\,j_0(E_jJ_\nu)=0
$$
于原 CM 纤维，其中 $H(P)=0$。
因此这一项在这里确实消失，不需要设 $c_{m,n,p}=0$。
得到
$$
\boxed{
X_{\nu j}
=\left.D_z^2\mu\mathcal K
 \mathcal Q_{24,n_\nu,p}(\mathcal D,\mathcal N)
 \Phi_{\nu j}\right|_{z=0}.
}
\tag{14}
$$
$D_z\mu=\mu\mathcal D$ 和各常系数算子交换，故(14)没有把
法向微分换成已限制到对角之后的微分。

原三差仍逐项是
$$
\boxed{M_{\nu j}=X_{\nu j}-X_{Sj}\quad(\nu=T,U,V).}
\tag{15}
$$
不同 $\nu$ 使用各自的 $n_\nu,M_\nu,\mathcal N,\mathcal K,\mathcal Q$；
不能在(14)中给 $J_\nu-J_S$ 选一个共同的未定义 degree。

## 3. 全部法向读数是原固定来源，而非自由列

为把(14)的内容写明，置
$$
\mathcal V_{\nu j,r}
=\left.\mathcal N^r\Phi_{\nu j}\right|_{z_1=z_2=z}
=\sum_{a=0}^r\binom ra n_\nu^a(-24)^{r-a}
 D_z^aE_j\,D_z^{r-a}J_\nu .
\tag{16}
$$
对每个 $r\ge0$，它是 whole degree $M_\nu$ 截面。
证明可在原 sigma 准周期中直接作：两个输入同时平移一个周期时，
其乘法指数的线性部分是
$\eta_\Omega(mz_1+nz_2)$；$\mathcal N$ 杀掉这个线性部分。
因此每次法向微分保持同一总 degree 的半特征与指数，
对角限制后仍全纯。等价地，所有含 $\zeta$ 的非椭圆项在(16)中相消，
余下是原 $\sigma^{M_\nu}$ 乘 $x,y$ 的多项式。
这也说明(16)没有换掉 R636 原 Frobenius 初值或 CM frame。

于是(14)可以逐项写成
$$
\boxed{
X_{\nu j}
=\frac1{M_\nu}\sum_{r=2}^{p-1}
\frac{(-1)^r24^{1-r}+n_\nu^{1-r}}r\,
 j_{p+1-r}(\mathcal V_{\nu j,r}).
}
\tag{17}
$$
所有物理读数的阶都小于 $p$；其法向来源则由(16)完整确定。
该式保留奇数 $r$。特别 $r=2$ 项准确为
$$
M_\nu\,j_{p-1}(K_{\nu j}),\qquad
K_{\nu j}=\mu\mathcal K\Phi_{\nu j}.
\tag{18}
$$
因此 R860(56) 给它的实际分解
$$
M_\nu\left\{
k_\nu(-1)^j j_{p-1}(\Xi_\nu)
+\frac14j_{p-1}\big(\sigma(2z)^2L_{\nu j}\big)
\right\}.
\tag{19}
$$
$\Xi_\nu,L_{\nu j},k_\nu$ 全取 R860(50)、(54)。
式(19)不把两项分别赋零，也没有删除(17)中 $r\ge3$ 的其余真实项。

## 4. 第一个奇法向伙伴的完整多项式

将 R860 的 $E_j=\sigma^mR_j,\ J_\nu=\sigma^nS_\nu$ 代入。
在本节 $D=2y\partial_x+3x^2\partial_y$，不是热方向 $L$。
准确有
$$
\mathcal V_{\nu j,1}
=\sigma^M\big(n(DR_j)S_\nu-mR_jDS_\nu\big),
\tag{20}
$$
以及
$$
\boxed{
\begin{aligned}
\sigma^{-M}\mathcal V_{\nu j,3}
={}&n^3(D^3R_j)S_\nu-3mn^2(D^2R_j)(DS_\nu)\\
&+3m^2n(DR_j)(D^2S_\nu)-m^3R_jD^3S_\nu\\
&-3mnM x\big(n(DR_j)S_\nu-mR_jDS_\nu\big)\\
&-2mnM(n-m)yR_jS_\nu .
\end{aligned}}
\tag{21}
$$
证明把 conjugated 法向导子写为
$$
nD_1-mD_2+mn(\zeta(z_1)-\zeta(z_2)).
$$
对角上最后一项为零，其第一次法向导数为 $-mnM x$，
第二次为 $-2mnM(n-m)y$。
非交换三次展开即给(21)，包括两个必要的连接修正。

$R_j,S_\nu$ 都是 $y$ 乘 $x$ 多项式。
所以(21)的右边是 $y$ 乘完整多项式，定义
$$
\widetilde L_{\nu j}
=\sigma^{M_\nu-4}\,
 \frac{\sigma^{-M_\nu}\mathcal V_{\nu j,3}}y .
$$
这是全纯 degree $M_\nu-4$、型二来源，且
$$
\boxed{
\mathcal V_{\nu j,3}=-\frac{\sigma(2z)}2\,\widetilde L_{\nu j},
\qquad \operatorname{ord}_O\widetilde L_{\nu j}\ge2 .
}
\tag{22}
$$
商在这里为多项式，不是未处理的有限极。

原指定组合由 $C_{24}=z^5+\cdots,\ J_\nu=z+\cdots$ 准确给
$$
\mathcal V_{\nu,*,1}=(5n_\nu-24)z^5+O(z^{11}),\qquad
\mathcal V_{\nu,*,3}=60n_\nu^2(n_\nu-24)z^3+O(z^9),
\tag{23}
$$
$$
\widetilde L_{\nu,*}
=-60n_\nu^2(n_\nu-24)z^2+O(z^8).
$$
这些系数在原范围都是单位。它们说明(8)的奇项有一个实际非零来源，
不能只以“平衡平方”之名把整条奇链省掉；
不从其正 jet 推出(17)这个全和非零。

## 5. 同一 whole Frobenius 还给完整法向递推

R856 分别作用于两个原 whole 输入，模 $p$ 得
$$
\mathcal N^p\Phi_{\nu j}
=H\mathcal N\Phi_{\nu j}
+mnC(z_1-z_2)\Phi_{\nu j}.
$$
因 $\mathcal N(z_1-z_2)=M$，再作用 $\mathcal N^r$ 并取对角，
准确有
$$
\boxed{
\mathcal V_{\nu j,p+r}
=H\mathcal V_{\nu j,r+1}
+mnM C\,r\,\mathcal V_{\nu j,r-1}\pmod p
\qquad(r\ge0),
}
\tag{24}
$$
$r=0$ 的后一项解释为零。CM 纤维上尤其
$$
\mathcal V_{\nu j,p}=0,\qquad
\mathcal V_{\nu j,p+1}=mnM c_p\,E_jJ_\nu .
\tag{25}
$$
(24)是一条在原 total degree $M$ whole 格中的法向 jet 身份；
没有把每个 $\mathcal V_r$ 另认成 degree $mnM$ 的一变量来源。

原(17)仍读取 $2\le r\le p-1$ 这一完整前缀。
(24)没有免费确定该前缀，也没有给(25)的除 $p$ 行。
需要使用二挠、CM13 或原算术中央时，须将(16)的整个来源一并运输。

最终，四个原首必要零条件仍准确是
$$
O_*+X_{S,*}=0,\qquad
X_{T,*}-X_{S,*}=X_{U,*}-X_{S,*}
=X_{V,*}-X_{S,*}=0.
\tag{26}
$$
本注把每个 $X$ 写成同一明确有限核作用的真实平衡链，
并保了 R860 已发现的所有 $\Xi,L$ 以及第一个奇伙伴。
它没有将首尾单位、多项式非零或(23)的来源非零
替代(26)中指定读数的非零。
