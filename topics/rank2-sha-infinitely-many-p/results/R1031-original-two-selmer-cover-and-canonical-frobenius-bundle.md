# R1031 — 原二 Selmer 的固定生成元、真正两二次式覆盖与规范 Frobenius 束

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明。** 对每个惰性素数 $q\ge5$，原 $I_9/I_3$ 曲线及其
常数 $-3$ 扭曲的完整二 Selmer 群均为一维，并有下面明确的
固定 Norm 类作生成元。对 R1014 已付的全部充分大 $q$，它正是
实际最短反 Frobenius 截面的非零模二类。本篇给出这个类的
真正两二次式覆盖、坐标返回，并把后继所需的稳定束同构和
Frobenius 映射落实到固定三同源盖上的准确除子及原谱域乘法。

这里的 Selmer 定位不等于已经求出该覆盖的一般有理点，也不
等于 R1027 的原27对评价或普通 $p$ 局部 AJ 已非零。后两项
仍须继续，不能由二 Selmer 维数或 Frobenius 束同构代替。

## 1. 原对象、常数扭曲与准确二下降方向

固定
$$
 B:\ Y^2+Y=X^3,\qquad t=-Y/27,\qquad
 E/\mathbf F_q(B):\ y^2+xy+ty=x^3.
 \tag{1}
$$
令 $k=\mathbf F_q(B)$，$q\equiv-1\pmod6$，并令
$\delta^2=-3$、$\omega=(-1+\delta)/2$。原二挠谱曲线及映射
保持 R1029 的实际模型
$$
 C:\ w^2=(z^3-4)(z^3-16),\qquad
 f:C\longrightarrow B,
$$
$$
 X=-\frac{3z}{z^3-4},\qquad
 2Y+1=\frac{w(z^3+2)}{(z^3-4)^2}.
 \tag{2}
$$
其谱域 $K_C=k(z)$ 具有固定基 $1,z,z^2$，满足
$$
 z^3+\frac3Xz-4=0.
 \tag{3}
$$
原非零二挠点的 $x$ 坐标是
$$
 \beta=-u^2
 =-\frac{(Yz+X)^2}{9(z-2X)^2}.
 \tag{4}
$$
例如由 R1029 的 $u=(1-w/(z^3-4))/6$ 及(2)，直接得到
$u=-(Yz+X)/(3(z-2X))$，所以(4)未换二挠谱域。

写
$$
 F(x)=x^3+\frac{(x+t)^2}{4}.
$$
反 Frobenius 的实际常数扭曲取为
$$
 E^-:\quad -3(W/2)^2=F(x),\qquad
 y=\frac{\delta W-x-t}{2}.
 \tag{5}
$$
$E^-(k)$ 与原 $E(\mathbf F_{q^2}(B))$ 中满足
$\sigma Q=-Q$ 的点逐点对应；这里 $\sigma(\delta)=-\delta$。

对一般常数扭曲 $E^{(d)}:d\,w_0^2=F(x)$，二 Kummer 映射
在谱域中的准确代表是
$$
 d(x-\beta)\quad \bmod K_C^{\times2}.
 \tag{6}
$$
证明是把模型改成 $x'=dx,\ y'=d^2w_0$；其二挠根为 $d\beta$，
通常的 $x'-d\beta$ 正是(6)。因而(5)必须使用
$-3(x-\beta)$，不能漏掉 $-3$ 而仅取 $x-\beta$。

三个非零二挠点给出精确的有限 Galois 模列
$$
 1\longrightarrow E[2]\longrightarrow
 \operatorname{Res}_{K_C/k}\mu_2
 \xrightarrow{\operatorname{Nm}}\mu_2\longrightarrow1.
 \tag{7}
$$
其中一个非零二挠点对应的三个符号在自身坐标为 $+1$，
另两处为 $-1$。Norm 的对角截面在次数三时确为截面，因此
$$
 H^1(k,E[2])=
 \ker\{K_C^\times/K_C^{\times2}
              \xrightarrow{\operatorname{Nm}} k^\times/k^{\times2}\}.
 \tag{8}
$$
常数扭曲不改变这个二挠模及其三个标号。

## 2. 所有局部条件都是 unramified，并给完整 Selmer 核

以下论证既用于 $E$，也用于 $E^-$。原光滑模型在好处有好约化，
仅有两个乘法约化处，几何分量阶分别为 $9$、$3$；常数扭曲
只改变分裂型，不改变这两个奇数。

令 $K$ 是任一基曲线完备局部域，$K^{\mathrm{nr}}$ 是最大
非分歧扩张。在好处，约化后的椭圆曲线在代数闭剩余域上
二可除；在乘法处，恒等分量为 $\mathbf G_m$，也二可除，
而分量群阶为奇数。形式群因 $q\ne2$ 而乘二可逆。因此
$$
 E^{(d)}(K^{\mathrm{nr}})/2=0.
 \tag{9}
$$
局部 Kummer 像遂包含于 $H^1_{\mathrm{nr}}(K,E[2])$。
两者维数也相同：前者的阶等于 $E^{(d)}(K)[2]$ 的阶，
因为局部点群具有乘二可逆的开形式子群和有限商；
后者是
$E[2]^I/(\mathrm{Frob}-1)E[2]^I$，其维数等于
$\dim E[2]^{G_K}$。故准确有
$$
 \operatorname{im}\bigl(E^{(d)}(K)/2\to H^1(K,E[2])\bigr)
      =H^1_{\mathrm{nr}}(K,E[2]).
 \tag{10}
$$

通过(8)，一个类在此处非分歧，等价于它在谱曲线各个上方点的
赋值均为偶数。确实，转到 $K^{\mathrm{nr}}$ 后，各谱域因子的
剩余域均代数闭，单位皆为平方，而非分歧基扩张不改变这些
赋值；这也涵盖两个分歧谱点，不能只检查原谱盖的 étale 开集。

对任意光滑射影曲线 $D/\mathbf F_q$，全部赋值为偶数的函数
平方类有精确列
$$
 0\longrightarrow\mathbf F_q^\times/\mathbf F_q^{\times2}
 \longrightarrow H^1(D,\mu_2)
 \longrightarrow\operatorname{Pic}(D)[2](\mathbf F_q)
 \longrightarrow0.
 \tag{11}
$$
这里可直接由 $\operatorname{div}(h)=2D_h$ 证明；有限域的
Brauer 群为零，保证有理的二挠线丛有这样的有理代表。
Norm 在常数平方类上是三次幂，因而是同构。
若 Picard 类的 Norm 为零，其函数 Norm 为常数乘一个平方；
用唯一的常数平方类即可把这个常数消掉。这给出准确而无额外
常数核的同构
$$
 \boxed{\quad
 \operatorname{Sel}_2(E^{(d)}/k)
 \simeq
 \ker\{\operatorname{Nm}_f:\operatorname{Pic}(C)[2](\mathbf F_q)
                          \to\operatorname{Pic}(B)[2](\mathbf F_q)\}.
 \quad}
 \tag{12}
$$
此处 $d=1$ 或 $-3$；证明使用全部局部条件，不是只给必要条件。

## 3. 固定生成元与实际最短截面的模二定位

令 $a=a_0\in\mathbf F_q$ 为唯一的 $a^3=4$ 的根，并令
$a_1=\omega a,\ a_2=\omega^2a$。在 $C$ 上写
$P_i=(a_i,0)$。R1029 已逐式证明
$$
 \ker(\operatorname{Nm}_f:\operatorname{Pic}(C)[2]\to
                         \operatorname{Pic}(B)[2])
       =\{0,[P_0-P_1],[P_0-P_2],[P_1-P_2]\}.
 \tag{13}
$$
Frobenius 固定 $P_0$、交换 $P_1,P_2$，所以(13)的固定部分
准确为一维，非零元为
$$
 L=[P_1-P_2],\qquad
 g(z)=(z-a_1)(z-a_2)=z^2+az+a^2.
 \tag{14}
$$
若 $\infty_+,\infty_-$ 是 $C$ 的两无穷点，则
$$
 \operatorname{div}(g)=
 2(P_1+P_2-\infty_+-\infty_-).
$$
因为 $2P_2\sim\infty_++\infty_-$，半除子的类正是 $L$。
它非零，故 $g$ 甚至在几何谱域中也不是平方。其精确 Norm 为
$$
 \operatorname{Nm}(g)=\left(\frac{3a}{X}\right)^2.
 \tag{15}
$$
例如在(3)中
$(z-a)g=-3z/X$，
$\operatorname{Nm}(z)=4$，
$\operatorname{Nm}(z-a)=-3a/X$，立即给(15)。
这同时确定了后文使用的 Norm 平方根。

由(12)--(15)，对每个惰性 $q\ge5$，
$$
 \boxed{\operatorname{Sel}_2(E/k)=
 \operatorname{Sel}_2(E^-/k)=\langle[g]\rangle\simeq\mathbf F_2.}
 \tag{16}
$$
这本身不把一个二 Selmer 类自动变成有理点。

现在限于 R1014 已证明 Tate 的全部充分大惰性 $q$。
R1014、R1027§8 已给实际反 Frobenius 点群的自由秩一，
其最短生成元高度为 $2q/3$。其挠点为零：几何挠群是原
$\mathbf Z/3$，全部被 Frobenius 固定，不能同时满足
$\sigma P=-P$。于是
$E^-(k)/2E^-(k)$ 一维，注入(16)便是同构。因此
$$
 \delta_2(Q_{\min})=[g],\qquad
 \Sha(E^-/k)[2]=0.
 \tag{17}
$$
这里没有把原曲面的 Brauer 消失未经处理地外推到常数扭曲；
(17)来自已付的实际秩与完整 Selmer 维数。

## 4. 真正的两二次式覆盖、所有返回坐标及分母

保持 $c=3/X$，在固定谱基中置
$$
 R=A+B_1z+C_1z^2,
$$
$$
 U_0=A^2+8B_1C_1,\quad
 U_1=2AB_1-2cB_1C_1+4C_1^2,\quad
 U_2=B_1^2+2AC_1-cC_1^2,
$$
$$
 \begin{aligned}
 G_0&=a^2U_0+4U_1+4aU_2,\\
 G_1&=aU_0+(a^2-c)U_1+(4-ac)U_2,\\
 G_2&=U_0+aU_1+(a^2-c)U_2.
 \end{aligned}
 \tag{18}
$$
由 $z^3=4-cz,\ z^4=4z-cz^2$，
$U_i$ 是 $R^2$ 的三个系数，$G_i$ 是 $gR^2$ 的三个系数。

在 $\mathbf P^3_k$ 的坐标 $(A:B_1:C_1:s)$ 中取
$$
 \begin{aligned}
 3G_0-12X^2G_2-X^2(4Y^2-1)s^2&=0,\\
 3G_1+12XG_2+2XY(2Y+1)s^2&=0.
 \end{aligned}
 \tag{19}
$$
这是类 $[g]$ 对应的真正二覆盖。直接证明如下。令 $k_0=xs^2$，
(19)等价于存在 $k_0$ 满足谱域恒等式
$$
 -9k_0(z-2X)^2-(Yz+X)^2s^2=3gR^2.
 \tag{20}
$$
在 $s\ne0$ 时，(20)就是
$$
 -3(x-\beta)
       =g\left(\frac{R}{s(z-2X)}\right)^2,
 \tag{21}
$$
并给
$$
 x=-\frac{G_2}{3s^2}-\frac{Y^2}{9}.
 \tag{22}
$$
在谱域分裂后，对三个根分别取平方根，可把(20)变为通常的
三个对角平方式，消去 $x$ 正是光滑的两二次式交。
三个二挠根互异；这个模型的光滑射影曲线是 genus1，
到(5)的映射为 degree4 的二覆盖，而不是仅清分母得到的必要条件。

Norm 计算也完全保留：
$$
 \operatorname{Nm}(z-2X)=-2(2Y+1)^2,
$$
$$
 \operatorname{Nm}(R)=
 \det\begin{pmatrix}
 A&4C_1&4B_1\\
 B_1&A-cC_1&4C_1-cB_1\\
 C_1&B_1&A-cC_1
 \end{pmatrix}.
 \tag{23}
$$
使用(15)确定的平方根，可选择返回为
$$
 W=-\frac{a\,\operatorname{Nm}(R)}
            {3X(2Y+1)^2s^3},\qquad
 y=\frac{\delta W-x-t}{2}.
 \tag{24}
$$
把(20)取 Norm，逐项得到 $-3W^2=4x^3+(x+t)^2$；
另一个 Norm 符号只把原截面改成其负元。

这里没有漏掉 $s=0$ 的有理点。若(19)在 $s=0$ 有 $k$ 点，
(20)迫 $g$ 等于一个 $k^\times$ 常数乘谱域平方。
(15)再迫这个常数本身是 $k$ 中的平方（次数为三），从而
$g$ 为谱域平方，矛盾。故每个 $k$ 点均可用(22)--(24)返回。

$X=0$ 或 $2Y+1=0$ 是这些有理坐标的分母位置，不是可以删除
的基点；全程采用(19)的光滑射影模型及返回有理映射的延拓。
相同地，谱基公式在 $z=2X$ 的表观分母不能被当作额外局部
不满足条件。局部条件已在§2对全部点支付。

(17)证明(19)对全部充分大惰性 $q$ 有 $k$ 点。
它尚未给出这些点的统一公式；后继必须真正解(19)，不能
把这个存在断言记作已经构造一般截面。

## 5. 实际稳定束及固定三同源模型

以下先在包含 $\delta,a$ 的特征零域证明几何恒等式，再沿同一
好模型约化到 $q\ge5$。也可在约化后的代数闭域逐式证明。

把 $L$ 看作(14)的二挠线丛，令
$$
 V=f_*L,\qquad W=[\delta]_*\mathcal O_B(-O).
 \tag{25}
$$
两者秩三、次数 $-1$，并且
$$
 \det V=\det W=\mathcal O_B(-O).
 \tag{26}
$$
对 $V$，Norm $L$ 为零，故只需确定 $\det f_*\mathcal O_C$。
(3)的判别式为
$-108(2Y+1)^2/X^3$，其符号二盖具有平方类 $-3X$。
由于 $\operatorname{div}X=T+(-T)-2O$，其反不变线为
$\mathcal O_B(-O)$，这就是三盖的行列式线。
常数 $-3$ 改变二盖的乘法而不改变该线丛。
对 $W$，étale 三同源的 $\delta_*\mathcal O_B$ 分成
$\mathcal O,L_3,L_3^2$，其行列式平凡；推前 $-O$ 的 Norm
正是 $-O$，所以(26)成立。

$V$ 稳定可以直接证明，不用一个未注明的 Frobenius 稳定性
断言。若它有次数非负的线子丛 $M$，有限映射伴随给
$H^0(C,L\otimes f^*M^{-1})\ne0$。次数迫 $\deg M=0$，
继而 $L=f^*M$。取 Norm 得 $M^3=1$，所以 $L^3=1$，
与非零二挠 $L$ 矛盾。若有破坏稳定性的秩二子丛，商线 $N$
次数至多 $-1$；有限映射对偶伴随给
$$
 \operatorname{Hom}(V,N)
 =H^0(C,L^{-1}\omega_C\otimes f^*N)=0
$$
因为次数至多 $2-3=-1$。这排除全部真子丛。

对 $W$，étale 拉回给
$$
 \delta^*W\simeq\bigoplus_{T'\in\ker\delta}
                    \mathcal O_B(-T').
$$
右侧是同斜率 $-1$ 的线丛直和，故半稳定；于是 $W$ 半稳定。
秩三与次数 $-1$ 互素，所以 $W$ 稳定。
下面直接构造非零的 $V\to W$，从而得到实际同构，
不把同秩同行列式分类的存在性当最后一步。

## 6. 固定 Hom 截面的准确 theta 平移及三个零点

令 $J=\operatorname{Jac}(C)$，
$P_0=(a,0)$，$R_0=r(P_0)\in B[2]$。
保持 R1029 的实际 degree2 映射
$$
 U=z+4/z,\quad V_+=w(z+2)/z^2,\qquad
 X_r=-\frac{U+1}{U+4},\quad
 2Y_r+1=\frac{\delta V_+}{(U+4)^2}.
 \tag{27}
$$
Abel 嵌入取 $i(P)=[P-P_0]$，其像为对称 theta 除子 $\Theta$。
设 $\Phi=(f_*,r_*):J\to B^2$。原来已付的伴随关系是
$$
 \Phi\Phi^\dagger=
 \begin{pmatrix}3&\delta\\-\delta&2\end{pmatrix},
 \qquad \deg\Phi=\deg\Phi^\dagger=3.
 \tag{28}
$$

定义实际 étale 三盖
$$
 C_\delta=C\times_{B,[\delta]}B,\qquad
 g:C_\delta\to C,\quad b:C_\delta\to B.
 \tag{29}
$$
它为 genus4。整个拉回阿贝尔簇
$J\times_{f_*,B,\delta}B$ 与 $B_u\times B_v$ 的同构为
$$
 (u,v)\longmapsto
 \bigl(\Phi^\dagger(u,v),\ b=-\delta u+v\bigr).
 \tag{30}
$$
这不是只在表示上的同构。其核中 $v=\delta u$，
再用(28)得 $\delta u=0$；于是 $v=0$、$f^*u=0$。
$f^*$ 单射：否则三盖 $f$ 会经一个非平凡 étale 三同源分解，
余下 degree1 映射会把 genus2 的 $C$ 同构到椭圆曲线，矛盾。
故(30)的核为零，结合次数三便是同构。

在(30)下，$C_\delta=(\Phi^\dagger)^{-1}\Theta$，并准确有
$$
 v=r(P)-R_0-b,\qquad
 \delta u=r(P)-R_0-2b.
 \tag{31}
$$
特别是不能把 $R_0$ 平移省掉。

现证明线丛的精确式，而不只比较第一 Chern 类：
$$
 (\Phi^\dagger)^*\mathcal O_J(\Theta)
   \simeq b^*\mathcal O_B(O)\otimes
          v^*\mathcal O_B(R_0).
 \tag{32}
$$
(28)的 Hermitian 矩阵减去 $b=(-\delta,1)$ 的矩阵，
恰为 $\operatorname{diag}(0,1)$，所以两边的差属于
$\operatorname{Pic}^0(B^2)$。准确平移由两轴决定。

在 $v$ 轴，theta 交为 $O+R_0$。确实 $r^{-1}(O)$ 是
$z=-2$ 的一对双曲共轭点，因而是规范除子；
$r^{-1}(R_0)=P_0+\iota P_0$，其中
$\iota(z,w)=(4/z,8w/z^3)$。所以
$r^*R_0=[\iota P_0-P_0]$，theta 上有这两个交点；
总次数为二，已穷尽全部交。

在 $u$ 轴，限制次数三且对称，唯一落入 theta 的二挠点为零。
为核后一句，三点 $P_i=(a_i,0)$ 与三点
$Q_i=\iota P_i=(a_i^2,0)$ 是全部 Weierstrass 点，且
$$
 \Phi i(P_i)=(0,R_i-R_0),\qquad
 \Phi i(Q_i)=(R_i,R_i-R_0),
$$
其中 $R_i=(-a_i^2/4,-1/2)$ 是三非零二挠点。
而(28)把 $(u,0)$、$u\in B[2]$ 送到 $(u,u)$，
因为 $\delta=1+2\omega$ 在 $B[2]$ 上恒为一。
上述六点只有 $P_0$ 匹配；余交成正负对，故限制为
$\mathcal O_B(3O)$。这正是(32)右侧的两个轴限制。
$\operatorname{Pic}^0(B^2)$ 由两轴限制确定，(32)遂无剩余平移。

由(13)--(14)，$\Phi(L)=(0,R_1-R_2)=(0,R_0)$，所以
$$
 g^*L=v^*\mathcal O_B(R_0-O).
 \tag{33}
$$
有限映射对偶伴随、étale 基变和 adjunction 给
$$
 \operatorname{Hom}_B(V,W)=
 H^0\!\left(C_\delta,\,
   g^*L^{-1}\otimes\omega_{C_\delta}
                    \otimes b^*\mathcal O_B(-O)\right).
$$
用(32)--(33)准确化为
$$
 \boxed{\quad
 \operatorname{Hom}_B(V,W)=H^0(C_\delta,v^*\mathcal O_B(O)).
 \quad}
 \tag{34}
$$
从 $B$ 拉回零点除子的规范截面，给一个非零 Hom。
§5 的稳定性使它是同构；两束几何稳定，故 Hom 一维。
这里已提供实际截面，而不是只引用一维空间中存在某元。

其零除子也完全明确。逐式由(2)、(27)可得
$$
 f(P)+f(\iota P)=\delta r(P).
 \tag{35}
$$
两边微分与常数可分别核；在 $P_0$ 处，
$f(P_0)=O,\ f(\iota P_0)=R_0=\delta R_0$。
故 $v=0$ 在 $C_\delta$ 上等价于
$b=r(P)-R_0$ 且 $f(\iota P)=R_0$。
这三个不同的点投到 $C$ 上恰为
$$
 P_0,\qquad (z,w)=(-2a,\ 24\sqrt3),\
                  (-2a,\ -24\sqrt3).
 \tag{36}
$$
例如 $f^{-1}(R_0)$ 的 $z$ 为 $a^2$ 及 $-a^2/2$；
后一 $z$ 对应两个不同点 $w=\pm6\sqrt3$。
它不是谱盖在 $R_0$ 的分歧；应用 $\iota$ 后得到(36)。

对应的 $b$ 坐标分别为 $O$ 及
$$
 X_b=-a/2,\qquad 2Y_b+1=\pm\sqrt{-1}.
 \tag{37}
$$
这可由(27)及二挠平移公式
$x(P+R_0)=x(R_0)+3x(R_0)^2/(x(P)-x(R_0))$
直接得到。两个根总按完整共轭对保留，不为选一支扩大或删改
原有限基域。它们只固定(34)的截面，不是一般 $q$ 的原 $Q$。

## 7. 规范 Frobenius 关系及不可省掉的原乘法

以下回到惰性特征 $q$，并令 $d_q=(q+1)/3$。
Frobenius 将 $\delta$ 共轭为 $-\delta$。étale 笛卡尔基变
及 $[-1]$ 保持 $O$ 给
$$
 F_B^*W
  \simeq(-\delta)_*\mathcal O_B(-qO)
  \simeq\delta_*\mathcal O_B(-qO).
 \tag{38}
$$
另一方面 trace 对偶与投影公式给
$$
 W^\vee\otimes\mathcal O_B(-d_qO)
 =\delta_*\mathcal O_B(O-d_q\,\ker\delta)
 \simeq\delta_*\mathcal O_B(-qO).
 \tag{39}
$$
最后一步不是未定的 Picard 类比较：
$\ker\delta=O+T+(-T)$ 且
$\operatorname{div}X=T+(-T)-2O$；
相应有理平凡化由 $X^{-d_q}$ 明确给出。
通过(34)的固定同构，遂有
$$
 F_B^*V\simeq V^\vee\otimes\mathcal O_B(-d_qO).
 \tag{40}
$$

这里的常数域下降也明确固定。在 $\mathbf F_{q^2}$ 上，
$\sigma W=(-\delta)_*\mathcal O(-O)$；用 $[-1]$ 对理想线
$\mathcal O(-O)\subset\mathcal O$ 的天然作用
$h\mapsto h\circ[-1]$，得到 $\kappa:\sigma W\to W$。
因为 $[-1]^2=1$，准确有 $\kappa\sigma(\kappa)=1$，故 $W$
下降为 $\mathbf F_q$ 束。$V$ 的 $D_g$ 本来就在 $\mathbf F_q$
上。一维 Hom 中，若(34)的固定截面 $\phi$ 满足
$\sigma\phi=c\phi$，则 $c\sigma(c)=1$。当 $c\ne-1$ 取
$b=1+c$，当 $c=-1$ 取 $b=\delta$，均有 $b/\sigma(b)=c$；
因此 $\phi_0=b\phi$ 是同一个实际同构的 $\mathbf F_q$ 下降。
运输下面的原映射时必须使用
$\phi_0\circ j\circ F_B^*(\phi_0^{-1})$。任意改变比例 $b$
会在 Frobenius 矩阵中产生 $b/b^q$，不允许丢掉这个因子或
反过来改变原 $j$。

真正需要保留的另一个映射是原谱盖的 Frobenius，而不是
任取(40)的一个矩阵。取
$D_g=P_1+P_2-\infty_+-\infty_-$，
$L=\mathcal O_C(D_g)$，$\operatorname{div}g=2D_g$。
相对 Frobenius 给规范单射
$$
 j:F_B^*V\longrightarrow V,\qquad
             h\longmapsto g^{(q-1)/2}h^q.
 \tag{41}
$$
因 $L^q\to L$ 的准确平凡化是乘 $g^{(q-1)/2}$，
这个因子不能省掉。其余核长度在两个实际分歧点各为
$(q-1)/2$，总长 $q-1$：局部谱盖为 $u^2=v$，
Frobenius 在基 $1,u$ 上的非单位因子就是
$v^{(q-1)/2}$，第三个不分歧分量为单位。
这也与 $\deg V-\deg F_B^*V=q-1$ 相合。

在固定有理谱基中，(41)的全部三列就是
$$
 \left[g(z)^{(q-1)/2}z^{jq}\right]_
          {\bmod\, (z^3+3z/X-4)},\qquad j=0,1,2.
 \tag{42}
$$
该式给原乘法上的实际矩阵，不需要有限素数扫描。
例如原 trace 配对必须同样保留为
$$
 \langle h_1,h_2\rangle=\operatorname{Tr}_{K_C/k}(g h_1h_2),
 \qquad
 \langle jF^*h_1,jF^*h_2\rangle
                   =F^*\langle h_1,h_2\rangle.
 \tag{43}
$$
仅把秩三束替换成一个同构模型却不运输(18)、(21)、(41)--(43)，
不会构造原两二次式覆盖的点。

## 8. 本篇付清与仍需实际完成的门

(16)给所有惰性 $q\ge5$ 的完整原二 Selmer 群；
(17)只在已付 Tate 的全部充分大 $q$ 使用实际秩，
将固定类定位到最短反 Frobenius 截面。
(19)--(24)是其原二覆盖及无遗漏的返回坐标，
(34)--(37)是后继束同构的真正固定截面，
(38)--(43)保留了原谱盖、Norm 与 Frobenius 的乘法数据。

下一项仍是据这些固定输入求出(19)的实际一般点，或直接确定
其对应截面在 R1027(38)全部27对中的带权评价。
原54图、$\eta_j$、$P_-$ 与完整 $\operatorname{Cor}_{L/H}$
没有被二 Selmer 群、一个 Frobenius 矩阵或一个存在定理替代。
