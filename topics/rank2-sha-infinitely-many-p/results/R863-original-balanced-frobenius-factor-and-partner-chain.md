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


## 附录 A. 原第二列的算术交、唯一连接伴随与完整除 p 行

本附录固定原 $J_S$，不把四个不同伙伴相认。所有 $b$ 尺度都保留；
$q_F$ 表示下面固定 frame 的对数导数，不是另一个可选择的来源。
引用 [R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)
的完整原 CM13 三线及其(18)–(25)的连接规范。

### A.1 三个实际乘积与恰为二维的算术交

令
$$
Z_j=E_jJ_S,\qquad P_c(X)=(X+b)(X-8b)=X^2-7bX-8b^2.
$$
由本篇(1)及共同 C24 注(6)，准确有
$$
\boxed{Z_j=\sigma^{34}x^2\,b^jX^{2-j}P_c(X),\qquad j=0,1,2.}
\tag{A1}
$$
特别 $Z_2=b^2\sigma^{34}x^2P_c$，其首项为 $b^2z^{18}$。
它属于原 whole degree34 型零格，原点质量严格为零。

为使算术范围明确，R307 的三条原线在同一个 $b$ 模型中为
$S=\sigma^{34}x^2P_{1,b}$、$H_3=\sigma^{34}x^2P_{3,b}$、
$H_5=\sigma^{34}x^2P_{5,b}$，其中
$$
\begin{aligned}
P_{1,b}&=X^4-\frac{53b}{7}X^3-\frac{12b^2}{7}X^2
-\frac{80b^3}{7}X-\frac{128b^4}{7},\\
P_{3,b}&=X^5-208bX^4+400b^2X^3+8128b^3X^2
+12032b^4X-2048b^5,\\
P_{5,b}&=X^5+272bX^4-272b^2X^3-14912b^3X^2
-6784b^4X+1024b^5 .
\end{aligned}
\tag{A2}
$$
在原 $b=17$ 算术框，它们分别是 $E_{17},E_{17^3},E_{17^5}$
的已识别来源；R307 已支付后两者移到共同微分尺度的全部倍率。
本附录只使用它们在同一框中的完整截面，不改变各自的 Hecke 角色。

将(A2)与(A1)逐项比较，得到
$$
\boxed{
S=Z_0-\frac47Z_1+\frac{16}{7}Z_2,\qquad
D_{\rm ref}:=-\frac{H_3-H_5}{96b}=5Z_0+28Z_1-4Z_2 .
}
\tag{A3}
$$
因此，若
$$
\mathcal Z=\langle Z_0,Z_1,Z_2\rangle,\qquad
\mathcal A=\langle S,H_3,H_5\rangle,
$$
则
$$
\boxed{\mathcal Z\cap\mathcal A=\langle S,D_{\rm ref}\rangle.}
\tag{A4}
$$
证明不依赖一个未计算的谱投影：$\mathcal Z$ 全部质量零；
$S(0)=0$、$H_3(0)=H_5(0)=1$，
故 $\mathcal A$ 中质量零部分恰为右边的二维空间。
(A3)把它包含在 $\mathcal Z$ 中，且两向量线性独立。

准确的剩余坐标是
$$
\ell(c_0,c_1,c_2)=-4c_0+c_1+2c_2 .
\tag{A5}
$$
它同时杀掉 $(1,-4/7,16/7)$ 和 $(5,28,-4)$，
而 $\ell(0,0,1)=2$。更完整地，
$$
\boxed{
\sum_{j=0}^2c_jZ_j
=\frac{7(28c_0-5c_1)}{216}S
+\frac{4c_0+7c_1}{216}D_{\rm ref}
+\frac{\ell(c)}2Z_2 .
}
\tag{A6}
$$
所以 $Z_2$ 是此实际商的一条代表；没有说它本身已是纯 CM 谱线。

在 $b=1$ 的原 $W_D$ 规范，写 $\rho=d(t)\Theta^{17}$、$d(t)=1+8t$。
三个固定列 $f_j=(-1)^jt^{j+1}(t-1)$ 满足
$$
\rho f_j=Z_j,\qquad
\sum_jc_{*,j}f_j=t(t-1)h_7(t)/7 .
\tag{A7}
$$
一般 $b$ 时第一式为 $b^{-1}\rho f_j=Z_j$。
特别深层接口实际出现的 $f_2=t^3(t-1)$
并不在(A3)的两个已识别方向之内。
(A7)只是同一个原输入的准确运输，不把整个 $K_1$ 尾像变成这三列，
也不对相应整目标单位的高位 carry 作截断。

### A.2 固定 Θ17 frame 下的唯一全纯伴随

保持 R307 的
$$
F=\Theta^{17}=\sigma^{34}x^{17},\qquad
\nabla_F=\partial_z-\frac{F'}F,\qquad X=x^3 .
$$
对 $C_R=\sigma^{34}x^3yR(X)$、$\deg R\le4$，
$$
\nabla_FC_R=\sigma^{34}x^2\mathcal L_bR,\qquad
\mathcal L_bR=6X(X+b)R'-(25X+28b)R .
\tag{A8}
$$
这是完整原点连接；一般 $\sigma^{34}yP(X)$
在 $x=0$ 的两个点会留下 R307(21)的极，不能免费扩大全纯域。

定义
$$
\begin{aligned}
R_b(X)
={}&\frac{2b^3}{7}-\frac{b^2X}{154}
-\frac{135bX^2}{2464}
+\frac{351X^3}{4928}
-\frac{351X^4}{2816b},\\
c_b&=-\frac{351}{2816b},\qquad
C_2=\sigma^{34}x^3yR_b(X).
\end{aligned}
\tag{A9}
$$
则有完整来源恒等式
$$
\boxed{Z_2=\nabla_FC_2+c_bF,\qquad C_2'(0)=-c_b.}
\tag{A10}
$$
证明可直接按
$$
\mathcal L_bX^j=b(6j-28)X^j+(6j-25)X^{j+1}
$$
计算：$\mathcal L_bR_b=b^2P_c-c_bX^5$。
这个两项带状矩阵的五个首 pivot 均非零，
故在 $\deg R\le4$、余项为 $cX^5$ 的原规范中，$(R_b,c_b)$ 唯一。
这也可由 R307 的原余行
$(-6175,6916,-8008,9856,-14080,56320)$
对 $X^2-7X-8$ 的值 $-7020$ 复核。
没有将“存在一个 meromorphic primitive”代替这枚明确全纯伴随。

$C_2$ 是原 whole degree34 型一截面，首阶为一；
它在 $x=0$ 至少三阶零，全部有限连接极已经支付。
(A9)分母只含 $2,7,11$ 和固定 $b$；
$c_b=-3^3\cdot13/(2^8\cdot11b)$ 在本文原好素数处为单位。
$F$ 的质量为一并原样保留，尚未被认作另一条已知算术中央来源。

### A.3 同一伴随的 whole 除 p 行和不能删除的连接商

以下所有 Hurwitz 读数都取原 CM 纤维，写
$j_k(A)=\partial_z^kA(0)$，并记
$c_p=(L_2H)(P)$ 为 R856 的实际 Hasse 导数。
为避免混淆，$c_b$ 始终是(A9)的固定连接系数。

R856 对原 whole degree34 截面 $A$ 给整量
$$
\mathcal D_{34,p,k}(A)
=\frac{j_{p+k}(A)-34c_p\,k\,j_{k-1}(A)}p ,
\tag{A11}
$$
这是原全参数定义在 $H(P)=0$ 的纤维值。
尤其(A10)的两个 whole 输入准确满足
$$
j_{p+2}(C_2)=-68c_pc_b+p\mathcal D_{34,p,2}(C_2),
\qquad
j_{p+1}(F)=34c_p+p\mathcal D_{34,p,1}(F).
\tag{A12}
$$
现在固定
$$
q_F=\frac{F'}F=34\left(\zeta+\frac yx\right).
$$
它是原点处的整 Hurwitz 级数，从五阶起；
全局的准周期和有限连接极均仍在。
特别不把 $q_FC_2$ 称为 whole degree34 输入。

对(A10)取 $p+1$ 阶，使用 $Z_2(0)=0$ 的准确整性，
得到
$$
\boxed{
\mathcal K_{2,p}
:=\frac{j_{p+1}(q_FC_2)+34c_pc_b}{p}\in\mathcal O_p,
}
\tag{A13}
$$
以及
$$
\boxed{
\mathfrak B(Z_2)
=\mathcal D_{34,p,2}(C_2)
+c_b\mathcal D_{34,p,1}(F)
-\mathcal K_{2,p}\pmod p .
}
\tag{A14}
$$
(A13)的整性是(A10)、(A12)和原 $Z_2$ 的质量零共同推出的；
没有对非 whole 乘积套用 R856。
这显示 $c_b$ 是单位也不能单独决定 $\mathfrak B(Z_2)$。

连接商还可把全部低卷积写明。因为 $F(0)=1$，$F'=q_FF$，
Leibniz 式在第 $p$ 阶给
$j_p(q_F)\equiv j_{p+1}(F)\equiv34c_p\pmod p$。
定义原固定 frame 的整量
$$
\mathcal L_p(F)=\frac{j_p(q_F)-34c_p}{p}.
$$
由 $q_F$ 型五、$C_2$ 型一及 $j_1(C_2)=-c_b$，
准确得到
$$
\boxed{
\mathcal K_{2,p}\equiv
-c_b\bigl(34c_p+\mathcal L_p(F)\bigr)
-\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
\frac{j_r(q_F)\,j_{p+1-r}(C_2)}{r(r-1)}
\pmod p .
}
\tag{A15}
$$
这里先保端项
$-(p+1)c_bj_p(q_F)$，再用
$\binom{p+1}{r}/p\equiv-1/(r(r-1))$；
原端项的下一位不能在除 $p$ 前删除。
和式所有读数严格低于 $p$，而 $\mathcal L_p(F)$
仍是同一个实际 $\Theta^{17}$ 的首对数商，不是可自由指定的数。

最后，(A3)在原 canonical 行上的参考项准确为
$$
\mathfrak B(D_{\rm ref})
=-\frac{\mathcal D_{34,p,1}(H_3)
-\mathcal D_{34,p,1}(H_5)}{96b}\pmod p .
\tag{A16}
$$
两个质量一来源的 Hasse 修正相消；没有分别对 $H_3,H_5$
使用质量零的定义。R307 的秩零和非零复中央值
不将这两条原中央导数赋零。
因此(A6)、(A14)–(A16)保留了原第二列的全部实际算术参考和连接商，
没有给四条原中央条件以外的附加零。


### A.4 用原 S 精确消去 Θ17 高商

(A10)可用原 $S$ 的同一个 R307 伴随进一步消元。
R307(26)–(27)给
$$
S=\nabla_FC_1+c_{1,b}F,\qquad
c_{1,b}=-\frac{8991}{12320b}.
$$
这里保原 $C_1$ 的全多项式，不以其算术名字代替来源。
两固定常数的准确比为
$$
a_0=\frac{c_b}{c_{1,b}}=\frac{455}{2664}.
$$
令 $C_0=C_2-a_0C_1$，直接相减 R307 的系数得到
$$
\boxed{
C_0=\frac{\sigma^{34}x^3y}{2664}
 (X+b)(65X^2-380bX+464b^2).
}
\tag{A17}
$$
尤其原四次多项式的最高项准确抵消；没有删除一个尚未确定的首项。
完整来源恒等式是
$$
\boxed{
Z_2-\frac{455}{2664}S=\nabla_FC_0,\qquad
C_0=-\frac{65}{2664}z^7+O(z^{13}).
}
\tag{A18}
$$
也可独立用(A8)验证：在分母 $2664$ 下，
$R=(65X^3-315bX^2+84b^2X+464b^3)/2664$，
其 $\mathcal L_b$ 像准确为
$b^2P_c-(455/2664)P_{1,b}$。

因为 $j_1(C_0)=j_3(C_0)=0$，R856 的 whole 行在这里没有质量修正：
$$
\mathcal D_{34,p,2}(C_0)=j_{p+2}(C_0)/p\in\mathcal O_p.
$$
$q_FC_0$ 的第 $p+1$ 阶 Leibniz 式也没有 $j_p(q_F)j_1(C_0)$
或其它高端项。因此(A18)给
$$
\boxed{
\begin{aligned}
\mathfrak B(Z_2)-\frac{455}{2664}\mathfrak B(S)
={}&\mathcal D_{34,p,2}(C_0)\\
&+\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
 \frac{j_r(q_F)\,j_{p+1-r}(C_0)}{r(r-1)}
 \pmod p .
\end{aligned}}
\tag{A19}
$$
这里不再有(A14)的 $\mathcal D_{34,p,1}(F)$
或(A15)的 $\mathcal L_p(F)$。
这个消去使用的是同一原 $S$，所以原中央首必要条件
$\mathfrak B(S)=0$ 可以真实代入(A19)；它不使
$\mathfrak B(Z_2)$ 或右边的任一项自动为零。

### A.5 同一七阶伴随的 degree12 × degree22 低卷积

进一步定义两个固定 whole 来源
$$
A_{12}=\sigma(2z)^3,\qquad
H_{22}=\sigma^{22}x^3(65X^2-380bX+464b^2).
$$
原绝对恒等式 $\sigma(2z)=-2y\sigma^4$ 给
$$
\boxed{
C_0=-\frac{A_{12}H_{22}}{21312},\qquad
A_{12}=8z^3+O(z^9),\quad H_{22}=65z^4+O(z^{10}).
}
\tag{A20}
$$
degree 分别为 $12,22$，型分别为三和四。
$H_{22}$ 在有限点没有极，最高函数极阶为十八，
故确为 whole degree22 截面。
这里的 degree22 并不识别其全部 $2/3/11$ Schwartz 角色，
也不把它当作原 $V_{66}$ 的一个已付算术因子。

取(A20)的第 $p+2$ 阶。所有不被 $p$ 整除的
二端系数只能出现在
$r=0,1,2,p,p+1,p+2$；
它们全被 $A_{12}$ 的三阶零和 $H_{22}$ 的四阶零准确杀掉。
其余真实非零项恰为
$3\le r\le p-2$、$r\equiv3\pmod6$，两输入的读数都严格小于 $p$。
并且
$$
\frac1p\binom{p+2}{r}
\equiv\frac{2}{r(r-1)(r-2)}\pmod p
\quad(r\equiv3\pmod6).
$$
于是
$$
\boxed{
\mathcal D_{34,p,2}(C_0)
=-\frac1{10656}
\sum_{\substack{3\le r\le p-2\\r\equiv3\ (6)}}
\frac{j_r(A_{12})\,j_{p+2-r}(H_{22})}
     {r(r-1)(r-2)}
\pmod p .
}
\tag{A21}
$$
分母 $10656=4\cdot2664$ 与所有显示的 $r,r-1,r-2$
均为原好素数处的单位。式(A21)也独立给该指定商的整性，
不需要把 $A_{12}$ 或 $H_{22}$ 各自的除 $p$ 行赋值。

将(A21)代入(A19)，得到原第二列的完整有限式
$$
\boxed{
\begin{aligned}
\mathfrak B(Z_2)-\frac{455}{2664}\mathfrak B(S)
={}&-\frac1{10656}
\sum_{\substack{3\le r\le p-2\\r\equiv3\ (6)}}
\frac{j_r(A_{12})j_{p+2-r}(H_{22})}{r(r-1)(r-2)}\\
&+\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
\frac{j_r(q_F)j_{p+1-r}(C_0)}{r(r-1)}
\pmod p .
\end{aligned}}
\tag{A22}
$$
两和全部是同一原 sigma/frame 的严格低于 $p$ 的系数。
$q_F$ 的低前缀由固定 $F=\Theta^{17}$ 的真实除法唯一确定；
没有替换 R636 的 Frobenius 初值、CM13 frame 或 Gaussian 高位。
(A22)不依赖(A13)里待保的高端连接商，却仍完整保留低连接配对。

这是一条指定原输入的消元，不是整个三差矩阵的新零行：
它尚未证明右边非零，也未给 $H_{22}$ 一个可以免费调用的中央条件。
对 R872 的全部 $K_1$ 末三尾，仍须连同同一个原向量、
其余 charge 列和完整目标单位的 carry 运输。
