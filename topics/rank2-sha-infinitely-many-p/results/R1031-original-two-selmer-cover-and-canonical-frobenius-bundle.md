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

## 9. 原 maximal Frobenius 线性系确实落在同一个三盖拉回

仍取 $P_0=(a,0)$。原映射(2)给
$$
 f^*(O)=P_0+P_1+P_2.
$$
每个 $P_i$ 都是 Weierstrass 点，故 $2P_i\sim K_C$，
从而
$$
 \mathcal O_C(f^*O-3P_0)=L.
 \tag{44}
$$
惰性 $q$ 的 $d_q=(q+1)/3$ 为偶数，(44)中的二挠误差准确消掉：
$$
 f^*\mathcal O_B(d_qO)=\mathcal O_C((q+1)P_0).
 \tag{45}
$$
R1029 已证明同一 $J(C)$ 上的实际
$\operatorname{Frob}_q^2=[-q]$。$P_0$ 在 $\mathbf F_q$ 上有理，
所以对每个几何点 $P$，
$$
 qP+\operatorname{Frob}_q^2(P)\sim(q+1)P_0\sim f^*(d_qO).
 \tag{46}
$$
这给原 $f$ 上的真正 Frobenius 线性系；它仍不把该线性系中的
一个函数自动改成(19)的有理点。

## 10. 同构的显式迹核与原谱基中的固定矩阵

为避免把(34)仅留成一个除子存在结论，现把相应截面写成原
函数域中的公式。以下的 $\xi$ 是三同源的 Kummer 坐标，
不与(4)的二挠参数 $u$ 混用。

在(29)的 $b$ 椭圆曲线坐标 $(r_b,s_b)$ 上定义
$$
 \xi=-\frac{\delta(2s_b+1+\delta)}{6r_b},
 \qquad
 \xi'=-\frac{\delta(2s_b+1-\delta)}{6r_b}.
$$
原三同源公式直接给
$$
 \xi^3=Y,\qquad \xi'^3=Y+1,\qquad
 \xi\xi'=X,\qquad r_b=\frac1{\xi-\xi'}.
 \tag{47}
$$
例如把 $(2s_b+1)^2=4r_b^3+1$ 展开三次，便得这些等式。
这也是(29)的实际 $\mathbf F_q$ 下降模型；
在 $\delta$ 共轭及定义域 $[-1]$ 同时作用下，$\xi,\xi'$ 不变。

置 $k_z=z^3$，并保持 $g=z^2+az+a^2$。定义
$$
 \begin{aligned}
 H_1&=\frac g z\bigl(w+k_z+8-3a^2z\bigr),\\
 H_2&=\frac{k_z-4}{z^2}
       \left((2z^2-az-a^2)(w+k_z+8)-36z^2\right),\\
 h&=-18a^2g+3a\,\xi H_1+\xi^2H_2.
 \end{aligned}
 \tag{48}
$$
它是(34)所需截面的准确有理函数系数。为证明这个陈述，选
$\omega_C=dz/w$，其除子是 $\infty_++\infty_-$。
采用(41)中的 $L=\mathcal O_C(D_g)$，则需要证明
$$
 \operatorname{div}(h)+
 g_C^*(2\infty_++2\infty_- -P_1-P_2)-b^*O
       \ \text{有效}.
 \tag{49}
$$
这里 $g_C:C_\delta\to C$ 是(29)的盖映射，避免与函数 $g$ 混淆。

先核全部可能极点。(47)使 $\xi$ 在每个 $P_i$ 上方有一阶极，
在 $\infty_+$ 上方有二阶零，在 $z=0,w=8$ 上方有一阶零，
余处无零极。(48)三项在两无穷点上方的极阶均至多二。
在 $z=0$ 两支，$w+z^3+8$ 分别有常数项16及三阶零；
因此 $\xi H_1$、$\xi^2H_2$ 的表观 $z,z^2$ 分母全部消掉。
在 $P_i$ 处，$z^3-4$ 有二阶零而 $w$ 有一阶零，
所以这些项均正则。没有删除任何分母支。

再核要求的零。取局部参数 $s=w$。在 $P_i$ 附近有
$$
 z=a_i-\frac{s^2}{36a_i^2}+O(s^4),\qquad
 Y=\frac{432}{s^3}-\frac12+O(s).
$$
三条盖支为
$$
 \xi=\frac{3a_i^2\omega^j}{s}+O(s^2),\qquad j=0,1,2;
 \tag{50}
$$
其中 $j=0$ 正是 $b=O$ 支，因为
$\xi'=X/\xi$ 且 $\xi-\xi'$ 仅在该支消掉其极，
于是 $r_b=1/(\xi-\xi')$ 有极。

在 $i=1,2$，(48)三项都至少消一次，且
$$
 (\xi H_1)'=\frac{3a^2a_i}{4}\omega^j,\qquad
 (\xi^2H_2)'=-9a_i\omega^{2j}.
 \tag{51}
$$
因此 $h'=9a_i(\omega^j-\omega^{2j})$，
在 $j=0$ 进一步消一次。这正是
$g_C^*(P_1+P_2)+b^*O$ 在这些点要求的全部重数。
在 $P_0$ 的 $j=0$ 支，
$g=3a^2+O(s^2)$，
$\xi H_1=36+O(s^2)$，
$\xi^2H_2=108a+O(s^2)$；
(48)的常数和一次项同时为零。它在另外两支的值为
$-324a\ne0$，故 $h$ 不是零函数。

于是(49)成立；§6 已证明这个 Hom 空间一维，
所以其有效除子准确等于 $v^*O$，即
$$
 \operatorname{div}(h)=
 v^*O+b^*O+g_C^*(P_1+P_2-2\infty_+-2\infty_-).
 \tag{52}
$$
这也独立固定了(36)中的另外两个零，未对任何 $q$ 扫点。

有限映射的微分迹伴随现在把同构写成
$$
 \boxed{\quad
 \phi_0(s)=\operatorname{Tr}_{C_\delta/B_b}(h\,s).
 \quad}
 \tag{53}
$$
(53)与按 $\omega_C/\omega_B$ 写出的伴随仅差一个非零固定
标量：$f^*\omega_B=6\,dz/w$，$\delta^*\omega_B=\delta\omega_B$，
所以原比为 $\delta/6$；再乘 $\delta$ 下降后为 $-1/2$。
(53)因此确实定义在 $\mathbf F_q$ 上。这里仅去掉一个
$\mathbf F_q^\times$ 的固定标量，它在 Frobenius 运输中的
$b/b^q$ 为一；没有重定义原(41)的 $j$。

更具体地，在 $V$ 的原有理基 $1,z,z^2$ 与 $W$ 的
$1,\xi,\xi^2$ 基中，(53)的固定矩阵是
$$
 M_{0j}=-18a^2\operatorname{Tr}(g z^j),\quad
 M_{1j}=3a\operatorname{Tr}(H_1 z^j),\quad
 M_{2j}=\operatorname{Tr}(H_2 z^j),\quad 0\le j\le2.
 \tag{54}
$$
所有迹都在原(3)的三次谱代数中；$w$ 由(2)返回。
(52)--(53)已证明 $\det M\ne0$，不是数值猜测。
若 $N_q$ 是(42)的实际矩阵，则真实运输严格是
$$
 j_W=M\,N_q\,\bigl(M^{(q)}\bigr)^{-1},
 \tag{55}
$$
其中 $M^{(q)}$ 对基域函数及系数取 $q$ 次幂。
(54)--(55)连同(18)--(24)提供完整固定有限源接线；
仍需由它产生(19)的实际点，不能把矩阵可写当成点已经取得。

## 11. 原迹核的准确 Norm 与常数

保持(47)--(48)，令 $r=X_b$，而 $X=X(\delta b)$ 仍是原基坐标。
则有完整函数恒等式
$$
 \boxed{\quad
 \operatorname{Nm}_{C_\delta/B_b}(h)
       =-2^7\,3^{10}\,
          \frac{r+a/2}{r^2X^2}.
 \quad}
 \tag{56}
$$
先不猜常数而比较完整除子。由(36)--(37)，
$$
 b_*(v^*O)=O+B_++B_-,
 \qquad B_\pm:\ r=-a/2,\ 2s_b+1=\pm\sqrt{-1}.
$$
此外
$b_*(b^*O)=3O$，
$b_*g_C^*(P_1+P_2)=2\ker\delta$，
$b_*g_C^*(\infty_++\infty_-)=\delta^{-1}(T+(-T))$。
所以(52)的 Norm 除子为
$$
 6O+2T+2(-T)+B_++B_-
                  -2\delta^{-1}(T+(-T)).
 \tag{57}
$$
另一方面
$\operatorname{div}r=T+(-T)-2O$，
$\operatorname{div}(r+a/2)=B_++B_--2O$，
$\operatorname{div}X=\delta^{-1}(T+(-T))-2\ker\delta$，
逐项给出同一个(57)。故(56)尚只差一个非零常数 $C_0$。

在 $b$ 上取 $\xi\to0$ 的支，并令
$\xi'\to\varepsilon$、$\varepsilon^3=1$。这是
$\delta b=T$ 的三个真实支之一，且
$$
 r\longrightarrow-\varepsilon^2,\qquad
 X\sim\varepsilon\xi,\qquad
 \frac{r+a/2}{r^2X^2}
       \sim\frac{a-2\varepsilon^2}{2\xi^2}.
 \tag{58}
$$
$f^{-1}(T)$ 有一个不分歧点 $(z,w)=(0,8)$，另一个点
$\infty_+$ 的分歧阶为二；这三条局部分支全部进入 Norm。

在不分歧支，
$z\sim4\varepsilon\xi/3$，由(48)得
$$
 h\longrightarrow
 U_0=-72a+\frac{144}{\varepsilon}
                     +\frac{36a^2}{\varepsilon^2}.
 \tag{59}
$$
在另两支，$w\sim z^3$、
$z^2\sim-3/(\varepsilon\xi)$，且
$$
 \frac h{z^2}\longrightarrow
 L_0=-18a^2-\frac{18a}{\varepsilon}
                       +\frac{36}{\varepsilon^2}.
 \tag{60}
$$
因此三支乘积的首项为
$$
 \operatorname{Nm}(h)
       \sim\frac{9L_0^2U_0}{\varepsilon^2\xi^2}.
 \tag{61}
$$
置 $b_0=a\varepsilon$，则 $b_0^3=4$，并有
$$
 U_0=36\varepsilon^{-1}(b_0^2-2b_0+4),\qquad
 L_0=-18\varepsilon^{-2}(b_0^2+b_0-2).
$$
把(58)--(61)相除，
$$
 C_0=2^5\,3^8\,
 \frac{(b_0-1)^2(b_0+2)^2(b_0^2-2b_0+4)}{b_0-2}.
$$
最后准确使用
$$
 b_0^2-2b_0+4=\frac{12}{b_0+2},\qquad
 (b_0-1)^2(b_0+2)=-3(b_0-2),
$$
得到 $C_0=-2^7\,3^{10}$。这些分母在 $q\ne2,3$ 时均非零。
常数既未以数值拟合，也未只保其平方类。

(56)为原矩阵运输付清了真实 Norm 因子。
其线性因子 $r+a/2$ 有两个单零点，不能未经处理把它当平方，
更不能从(56)直接宣称(19)已经有一个明确返回点。

## 12. 同一个 $C_\delta$ 的真实 $(3,3)$ 模型与另一亏格二商

现在把(29)进一步写成低次数平面乘积模型。
保持原二挠参数
$$
 u_2=\frac{1-w/(z^3-4)}6,\qquad
 z^3=\frac{(1-2u_2)(1+6u_2)}{u_2(1-3u_2)},\qquad
 Y=-27u_2^2(1-2u_2).
$$
在(47)的同一三盖上，令
$$
 A=-\frac{\xi}{3u_2},\qquad B=\frac zA.
$$
则
$$
 A^3=\frac{1-2u_2}{u_2},\quad
 u_2=\frac1{A^3+2},\quad
 \xi=-\frac{3A}{A^3+2},\quad
 B^3=\frac{A^3+8}{A^3-1}.
$$
所以同一个光滑射影 $C_\delta$ 的稠密开集恰为
$$
 \boxed{(A^3-1)(B^3-1)=9.}
 \tag{62}
$$
所有反向坐标也保持：
$$
 z=AB,\qquad
 w=\frac{(A^3-4)(A^3+2)}{A^3-1},\qquad
 \xi'=\frac{B(A^3-1)}{A^3+2}.
 \tag{63}
$$
由此直接核
$z^3-4=(A^3+2)^2/(A^3-1)$、
$z^3-16=(A^3-4)^2/(A^3-1)$，
以及 $\xi'^3-\xi^3=1$、$\xi\xi'=X$。
因此(62)没有只凭 genus 或 CM 型替换原盖；它与(29)在原
$C$、原三同源及原二挠参数上逐项双向相接。
在 $q\ne2,3$，六个分歧点互异，光滑射影模型仍为 genus4。
而且这正是原 $\kappa=[-1]$ 的下降：
$\sigma(\delta)=-\delta$、$\sigma(b)=-b$ 时，
(47) 的 $\xi,\xi'$ 均固定；$u_2,z,w$ 原定义于 $\mathbf F_q$，
故 $A=-\xi/(3u_2)$、$B=z/A$ 也固定。
因此(62)的有理系数模型模 $q$ 就是原谱盖，未漏常数二次扭曲。

两坐标的独立三次单位作用给群 $G=(\mathbf Z/3)^2$。
其子群
$$
 \kappa:(A,B)\longmapsto(\omega A,\omega^2B)
$$
的商由(63)给原 $C$；它就是原 étale 三盖的甲板群。
另一个子群
$$
 \lambda:(A,B)\longmapsto(\omega A,\omega B)
$$
也自由，给另一条实际 genus2 曲线。置
$$
 r=A/B,\qquad c_0=2A^3-(r^3+1).
$$
由 $(A^3-1)(B^3-1)=9$，准确得到
$$
 \boxed{C_{\mathrm{alt}}:\ c_0^2=r^6+34r^3+1.}
 \tag{64}
$$
反向取
$B^3=(c_0+r^3+1)/(2r^3)$、$A=rB$，便返回(62)。
这两个 degree3 商都定义在 $\mathbf Q$ 上；
无需把 $\omega$ 选为有理数。

两条商的 Jacobian 映射给实际同源
$$
 J(C_\delta)\longrightarrow J(C)\times J(C_{\mathrm{alt}})
 \quad\text{次数 }3^4.
 \tag{65}
$$
为付清而不只数维数，两个 pull/push 的自身复合都是 $[3]$；
交叉复合为零，因为另一子群在商上的进一步商是
$C_\delta/G\simeq\mathbf P^1$。两个不变 $H^1_{\mathrm{\acute et}}$ 空间各四维，
交为零、合为全部八维；于是映射是同源。
其与极化伴随的复合为 $\operatorname{diag}([3],[3])$，
次数 $3^8$，故(65)次数准确为 $3^4$。

(62)还给原 degree2 商 involution 的明确提升：
$$
 (A,B)\longmapsto(-2/A,-2/B).
 \tag{66}
$$
它在(63)上给 $(z,w)\mapsto(4/z,8w/z^3)$。
其在 $b$ 椭圆坐标上的作用是
$b\mapsto r(P)-b=v+R_0$；在 $P_0,b=O$ 处返回 $R_0$，
固定了这个常数。不能把它写成 $v$ 而漏掉 $R_0$。

## 13. 另一个商的真实非 CM 椭圆因子及整个盖的 Frobenius

(64)有 involution
$(r,c_0)\mapsto(1/r,c_0/r^3)$ 及其双曲共轭。
准确两个 degree2 商为
$$
 U=r+1/r,\qquad
 V_\pm=c_0(r\pm1)/r^2,
$$
$$
 V_\pm^2=(U\pm2)(U^3-3U+34).
 \tag{67}
$$
它们的真实 $\mathbf Q$ 模型必须保二次扭曲：

对于加号，取
$k=1/(U+2)$、$\ell=V_+/(U+2)^2$，
则 $\ell^2=32k^3+9k^2-6k+1$。
再取 $x=32k+3,\ y=32\ell$，得到
$$
 E_+:\quad y^2=x^3-219x+1654,\qquad
 j(E_+)=-\frac{3\cdot73^3}{512}.
 \tag{68}
$$
对于减号，取
$k=1/(U-2)$、$\ell=V_-/(U-2)^2$，
则 $\ell^2=36k^3+9k^2+6k+1$。
再取 $x=36k+3,\ y=36\ell$，得到
$$
 E_-:\quad y^2=x^3+189x+702,\qquad
 j(E_-)=\frac{9261}{8}.
 \tag{69}
$$
两个有理 $j$ 均非代数整数，故两曲线均非 CM。
(67)的 push/pull 交叉为零，自身复合为 $[2]$，
因此
$$
 J(C_{\mathrm{alt}})\longrightarrow E_+\times E_-
 \quad\text{为次数4的实际同源。}
 \tag{70}
$$

若使用较小系数模型
$$
 E_*:\ y^2=x^3+21x+26,
$$
则 $E_-$ 是它的二次 $3$ 扭曲，不是同一条 $\mathbf Q$ 曲线。
$E_*$ 的三同源核是 $x=1,y=\pm4\sqrt3$；
斜率 $\sqrt3$ 直接核实这些点的阶三。
Vélu 公式给其真正商
$$
 E_*':\quad y^2=x^3-219x-1654.
 \tag{71}
$$
例如核对两点的
$3x^2+21=24$ 及
$5x^3+3\cdot21x+2\cdot26=120$ 求和，
即得 $21-5\cdot48=-219$ 与 $26-7\cdot240=-1654$。
所以 $E_+$ 是 $E_*'$ 的二次 $-1$ 扭曲。
特别是 $E_-$ 有真正的有理三挠点 $(3,36)$；
不能把 $E_*$ 的核角色免费改成平凡。

三条实际模型的坏素数只在 $2,3$；
例如 $E_*,E_-,E_+$ 的显示 Weierstrass 判别式依次为
$-2^{15}3^3,-2^{15}3^9,-2^{21}3^5$。
若 $q\ge5$ 是 $E_-$ 的超奇异素数，则 Hasse 界及
$q\mid a_q(E_-)$ 给 $a_q(E_-)=0$。
由有理三挠点，
$q+1-a_q(E_-)$ 被三整除，故
$$
 q\equiv-1\pmod3.
 \tag{72}
$$
又由(71)与两个准确扭曲，
在这些惰性 $q$ 有
$$
 a_q(E_+)=-a_q(E_-).
 \tag{73}
$$
一般惰性 $q$ 的(73)只消总迹，不能推出平方为 $-q$。
必须再使用 $a_q(E_-)=0$，才由
$F^2-a_qF+q=0$ 得两个因子的真正 $F^2=[-q]$。

因此对每个 $E_-$ 的好超奇异素数，
R1029 的原 $J(C)$ Frobenius 恒等式、
(65)、(70)及同态在 Tate 模上的单射共同给
$$
 \boxed{
 \operatorname{Frob}_{q,J(C_\delta)}^2=[-q].
 }
 \tag{74}
$$
这里没有把纯表示等式当成 $S$ 的 Chow 分解：
(74)发生在已明确写出全部映射的同一个 genus4 曲线 Jacobian。

(74)为原谱盖增加了完整 Frobenius 图输入。
即使进一步用非 CM 椭圆曲线的超奇异素数定理取得无穷多个
这样的 $q$，仍须真正把该图接到(19)的有理点或原27对带权和；
它不自动产生原普通 $p$ 局部非零，也不自动保证 $q+1$
含有无穷多个不同的所需普通素因子。

### 13.1 固定原盖的无穷辅助惰性素数

这里可无条件消费已经发表的确切外部定理。
Elkies, *Supersingular primes for elliptic curves over real number fields*,
Compositio Math. **72** (1989), 165–172，p.165 的 Theorem
（[原文](https://www.numdam.org/item/CM_1989__72_2_165_0.pdf)，证明见§4）：
固定数域上的固定椭圆曲线，只要底域有实嵌入，
任意有限素位排除集之外仍有超奇异素位。
这里只取底域 $\mathbf Q$ 与(69)中固定的 $E_-$，满足全部假设；
没有使用 GRH、Lang–Trotter 或一个未证明的指定算术级数分布。

任取有限有理素数集合 $\Sigma$，将 $2,3$、原固定模型的有限坏集
和 R1014 的有限小素数范围一起并入。
定理给 $q\notin\Sigma$ 的 $E_-$ 好超奇异素数；
(72)使其自动惰性，(65)、(70)和(74)遂给同一个原盖
$\operatorname{Frob}_{q,J(C_\delta)}^2=[-q]$。
因此这些原谱盖具有上述完整 Frobenius 等式的惰性素数 $q$
**无穷多**，且可同时处在已付 Tate 的大 $q$ 范围。

此处量词只属于辅助 $q$。定理没有附带
$q\equiv-1\pmod{6p}$ 对任意指定 ordinary $p$ 的结论，
也没有给 $q+1$ 的 ordinary 素因子无穷性。
原两 quadric 点与完整27项带权评价仍须消费真正 Frobenius 图；
本节不将辅助素数无穷性改记成通常全 $\Sha[p^\infty]$ 的完成。

## 14. 同一个覆盖的实际九挠点及辅助超奇异素数的模九约束

(62)的坐标交换 $\sigma:(A,B)\mapsto(B,A)$ 给一个实际 degree2
椭圆商。令 $S=A+B,\ P=AB$，则其射影模型为
$$
 \mathcal E_F:\quad P^3+3PSZ-S^3-8Z^3=0,\qquad
 O_F=(S:P:Z)=(1:1:0).
 \tag{75}
$$
这里商函数域就是交换不变域：$A,B$ 为
$T^2-ST+P=0$ 的两个根，而(62)准确等价于(75)。
这不是仅凭 $j$ 值认定的另一条椭圆曲线。

令 $u=P-S+Z$。逐项代入(75)得到双向有理变换
$$
 x=\frac{12Z}{u}-1,\qquad
 y=\frac{12(P+S)}u,
 \qquad
 E_F:\quad y^2=x^3+21x-26,
 \tag{76}
$$
$$
 (S:P:Z)=(x+y-11:y-x+11:2x+2).
 \tag{77}
$$
例如写 $k=Z/u,\ v=(P+S)/u$，(75)直接给
$v^2=12k^3-3k^2+2k-1/3$，再取
$x=12k-1,\ y=12v$ 即为(76)。
$u=0$ 在(75)上的交为 $-9Z^3=0$，所以 $O_F$ 为 flex，
并由(76)延拓到 Weierstrass 模型的无穷点。
两条光滑射影曲线的有理双射因而给带原点的同构。
$E_F$ 的判别式为 $-2^{15}3^3$，故所有 $q\ge5$ 均好约化，
上述同构在相应光滑模型上仍成立。

群逆元的准确射影公式是
$$
 -(S:P:Z)=(P:S:-Z).
 \tag{78}
$$
这由(76)立即核为 $(x,y)\mapsto(x,-y)$，没有更换原点或暗加平移。

现在取任意特征不为 $2,3$ 的域及一个 $\alpha^3=-2$。
交换固定点 $A=B=\alpha$ 给实际点
$$
 R=(S:P:Z)=(2\alpha:\alpha^2:1).
 \tag{79}
$$
它的切线为 $S=2\alpha Z$；取 $Z=1$ 后，交方程准确分解成
$$
 P^3+6\alpha P+8=(P-\alpha^2)^2(P+2\alpha^2).
 \tag{80}
$$
因此第三个交点为 $(2\alpha:-2\alpha^2:1)$，由(78)
$$
 2R=(2\alpha^2:-2\alpha:1).
$$
$\alpha\ne1$，因为 $\alpha^3=-2$ 且特征不为 $3$。
连接 $R$ 与 $2R$ 的直线为
$$
 P=2Z-\frac{\alpha+2}{2(\alpha-1)}S.
 \tag{81}
$$
其第三个交点准确为 $(0:2:1)$，所以
$$
 3R=(-2:0:1).
 \tag{82}
$$
为确认阶数而不只报告三倍点，(76)把(82)送到
$(x,y)=(3,-8)$。该点的切线斜率为 $-3$，二倍点为
$(3,8)$，故它是非零三挠点。
于是(79)具有准确阶数九；所有切线分母及所用非零点在
$q\ge5$ 均无例外。也可在(75)上直接核：
(82)处切线为 $2S+P+4Z=0$，代入后得到
$-9(S+2Z)^3$，所以它是不同于 $O_F$ 的 flex。

若 $q\equiv-1\pmod3$，立方在 $\mathbf F_q^\times$ 上为自同构，
$\alpha^3=-2$ 有唯一 $\mathbf F_q$ 根。因此(79)给
$$
 \mathbf Z/9\ \subset E_F(\mathbf F_q).
 \tag{83}
$$
这里的九挠点来自原 $C_\delta$ 的交换固定点，未使用任意新曲线
或一个只在代数闭包存在的九挠点。

最后，把这个商与(69)的真实 $\mathbf Q$ 模型比较：
$$
 E_- = E_F^{(-3)}.
 \tag{84}
$$
确切地说，在 $\mathbf Q(\delta)$ 上
$(x,y)\mapsto(-3x,-3\delta y)$ 把(76)送到(69)；
所以(84)是准确的二次扭曲关系。
对于每个惰性 $q\ge5$，$(-3/q)=-1$，故
$a_q(E_-)=-a_q(E_F)$。结合(83)，得到更强的全惰性等式
$$
 9\ \mid\ q+1+a_q(E_-).
 \tag{85}
$$
特别地，§13所取的 $E_-$ 好超奇异素数先由(72)确定为惰性，
再由 $a_q(E_-)=0$ 和(85)得到
$$
 \boxed{q\equiv-1\pmod9.}
 \tag{86}
$$
因此上一节实际超奇异素数定理给出的无穷辅助素数，
在删除任何固定有限例外集之后，全部仍满足(86)及(74)。

这加强的是同一个谱盖的辅助 Frobenius 输入。
(83)--(86)本身仍没有求出(19)的原有理点，
没有给原27对带权评价非零，
也没有证明 $q+1$ 有无穷多个不同的所需普通素因子。
这些原目标不因九挠点存在而自动完成。

## 15. 原三盖的另一个实际纤维积图：九挠分歧点与固定二次尺度

本节把§§12–14的两个商放进同一个实际函数域图，
以保留下一步 Frobenius 图所需的平移及二次尺度。
它不把新的椭圆商当成原(19)的有理点。

首先，(68)的同一条曲线有准确九阶有理点
$$
 Q_+=(11,24)\in E_+(\mathbf Q).
 \tag{87}
$$
直接群律给
$$
 2Q_+=(-13,48),\quad
 3Q_+=(3,-32),\quad
 4Q_+=(35,-192).
 \tag{88}
$$
$3Q_+$ 的切线斜率为3，二倍点为 $(3,32)$，
故它是非零三挠点。这同时证明(87)的阶恰为九；
在全部 $q\ge5$ 的好约化处，九挠的阶仍为九。

(76)上的两个点 $S_\pm=(-1,\pm4\delta)$ 生成一个真正的三次同源核。
其商同源 $\phi:E_F\to E_+$ 由
$$
 \begin{aligned}
 \phi_x(x,y)
   &=x+\frac{48}{x+1}-\frac{192}{(x+1)^2},\\
 \phi_y(x,y)
   &=y\left(1-\frac{48}{(x+1)^2}
                    +\frac{384}{(x+1)^3}\right)
 \end{aligned}
 \tag{89}
$$
给出。可以直接代入(68)核验；其微分尺度为1，极点恰为
$O_F,S_+,S_-$，所以它是 degree3 的同源。
也可从两核点逐项核 Vélu 系数：
$3(-1)^2+21=24$，
$5(-1)^3+3\cdot21(-1)+2(-26)=-120$，
于是商系数为 $21-5\cdot48=-219$、
$-26-7(-240)=1654$。

保持(64)与(67)–(68)的原坐标，记
$$
 \pi_+:C_{\mathrm{alt}}\longrightarrow E_+,
 \qquad
 x_+=\frac{32}{U+2}+3,\quad
 y_+=\frac{32V_+}{(U+2)^2}.
$$
记 $\pi_F:C_\delta\to E_F$ 为(75)–(76)的交换商，
$\pi_\lambda:C_\delta\to C_{\mathrm{alt}}$ 为(64)的三盖。
则准确的交换关系是
$$
 \boxed{
 \pi_+\circ\pi_\lambda
   =\Psi\circ\pi_F,\qquad
 \Psi(P)=-\phi(P)-3Q_+.
 }
 \tag{90}
$$
这里的负号与 $-3Q_+$ 均不可删掉。

以下付清这两个常数。$\lambda:(A,B)\mapsto(\omega A,\omega B)$
与交换 $\sigma:(A,B)\mapsto(B,A)$ 对易，因此在 $E_F$ 上诱导
一个三次平移；它把 $O_F=(1:1:0)$ 送到 $(1:\omega:0)$，
由(76)识别为 $S_+$ 或 $S_-$，所以其平移核就是(89)的核。
于是 $\pi_+\pi_\lambda$ 在 $E_F$ 上的商映射，
必为 $\phi$ 后接一个带平移的椭圆曲线同构。

在 $O_F$ 上取 $A\to\infty,\ B\to1$ 的原分支，则
$r=A/B\to\infty$、$c_0\sim A^3$；(67)–(68)给
$$
 (\pi_+\pi_\lambda)(O_F)=(3,32)=-3Q_+.
 \tag{91}
$$
剩下的保原点自同构只有 $\pm1$，
因为(68)的 $j$ 值既非0也非1728。
取(79)的 $\alpha^3=-2$。原 $r=1,c_0=-6$ 给
$(\pi_+\pi_\lambda)(R_\alpha)=-Q_+$，而(89)准确给
$\phi(R_\alpha)=(-13,-48)=-2Q_+$。
因此保原点方向是 $-\phi$，证明(90)。
为使这个代入完全可回查，置 $u=(\alpha-1)^2$，则
$$
 u^2=6\alpha^2-6\alpha+9,\qquad
 u^3=27\alpha^2-36\alpha+45;
$$
把(79)的
$x=12/u-1,\ y=12\alpha(\alpha+2)/u$ 代入(89)，
即得上述 $(-13,-48)$。

两个对易商次数为2和3，故其函数域的合成是全部
$\mathbf Q(C_\delta)$，交是 $\mathbf Q(E_+)$。
所以(90)不只交换，而给同一个光滑射影曲线的准确识别
$$
 \boxed{
 C_\delta \simeq
 \operatorname{Norm}\!
 \left(C_{\mathrm{alt}}\times_{E_+,\Psi}E_F\right).
 }
 \tag{92}
$$
右侧为纤维积的正规化。三同源在特征不为3时 étale，
而下面二盖的分歧点互异，因此全部好约化处仍为这个实际图；
无需由 Jacobian 同源猜测曲线的纤维积身份。

二盖 $\pi_+$ 的平方根函数也有固定有理尺度。令
$$
 T=\frac{4(r-1)}{r+1}.
$$
由(67)–(68)直接得到
$$
 \boxed{
 T^2=-2(x_+-11),\qquad
 r=\frac{4+T}{4-T},\qquad
 c_0=\frac{y_+(r+1)^3}{32}.
 }
 \tag{93}
$$
故 $C_{\mathrm{alt}}/E_+$ 的分歧点恰为 $Q_+,-Q_+$。
$x_+-11$ 在无穷点的极阶为2，那里不分歧。
(93)的 $-2$ 是原双盖的真实二次尺度；
只列分歧点而省去它，会改变原 $\mathbf Q$ 模型。

相应地，$C_\delta/E_F$ 的六个分歧点正是
$A=B=\alpha$、$\alpha^3=-2$，以及
$A=B=\beta$、$\beta^3=4$。
前一组三点在 $\phi$ 下均为 $-2Q_+$，在 $\Psi$ 下均为 $-Q_+$；
后一组三点在 $\phi$ 下均为 $-4Q_+$，在 $\Psi$ 下均为 $Q_+$。
后一断言也可直接代入：若 $u=(\beta-1)^2$，则
$$
 u^2=6\beta^2-15,\quad
 u^3=-9\beta^2+54\beta-63,
$$
(89)给 $(35,192)=-4Q_+$。
这同时把全部分歧分支逐点接回原(62)，没有漏掉其中一组三根。

所有这些图在 $\mathbf Q$ 上定义，并按§12的原
$\delta\mapsto-\delta,\ b\mapsto-b$ 下降返回原 $C_\delta$。
在§13的辅助超奇异 $q$ 上，$Q_+$ 仍为固定九挠，
$q\equiv-1\pmod9$，各有理图与真正的 $q$ 次 Frobenius 对易。
因此(92)–(93)给的是可直接用于原函数域的 Frobenius 图，
而不是仅在 Tate 模上存在的某个同源。

下一步仍须用这些准确函数和(54)的原谱乘法，
真正求出(19)的点或计算原27对带权值；
(87)的九挠点不是原椭圆曲面上的非挠截面。

## 16. 原谱平方根的精确乘法运输及其真实 CM 二同源

保持原 $a^3=4$、$R_0=(-a^2/4,-1/2)$，
$p_C:C_\delta\to C$，
以及§§8–10的实际映射
$$
 b,\qquad v=r(P)-R_0-b:C_\delta\longrightarrow B.
$$
本节的 $g=z^2+az+a^2$ 与 $h$ 始终是(10)、(49)的原函数；
没有更换其平方类或乘上一个未定的常数。

**精确乘法恒等式。** 在同一个 $C_\delta$ 的函数域中，
$$
 \boxed{
 g=-\frac{h^2}{2916\,a(A-B)^2}
       \left(X(v)+\frac{a^2}{4}\right).
 }
 \tag{94}
$$
因而令 $e=-a^2/4$，原平方根被准确运输为
$$
 s=\frac{54(A-B)\sqrt g}{h},\qquad
 \boxed{s^2=-\frac{X(v)-e}{a}.}
 \tag{95}
$$
包括 $-1/a$ 在内的全部系数已经固定。

**证明。**
先核函数除子，随后在一个明确分支求常数。
由(62)微分及(63)，
$$
 \frac{dz}{w}=\frac{dA}{B^2(A^3-1)}.
$$
另一方面，用(75)的 $S=A+B,P=AB$，
(76)给
$$
 \pi_F^*\frac{dx}{2y}
   =\frac{dS}{2(P^2+S)}
   =\frac{A-B}{2}\frac{dz}{w}.
 \tag{96}
$$
最后一个等式可不作展开地检查：
$$
 \frac{dS}{dA}
 =1-\frac{A^2(B^3-1)}{B^2(A^3-1)}
 =\frac{(A-B)(A^2B^2+A+B)}{B^2(A^3-1)}.
$$

交换二盖 $\pi_F$ 的六个分歧点正是§15的两组三点。
其中 $A=B,\ A^3=-2$ 的三个点准确组成 $b^*O$。
确实此处 $\xi,\xi'$ 同有一阶极，$\xi'/\xi\to1$；
由 $\xi'^3-\xi^3=1$，
$\xi-\xi'$ 有二阶零，故 $X(b)=1/(\xi-\xi')$ 有二阶极。
另三点 $A=B=\beta,\ \beta^3=4$ 满足
$$
 \xi=-\beta/2,\quad \xi'=\beta/2,\quad
 b=(-1/\beta,-1/2)=(-\beta^2/4,-1/2)=R_i.
$$
原 $r\circ\iota=r$，所以这些点的 $r(P)$ 也等于 $R_i$；
由 $v=r(P)-R_0-b$，它们准确组成 $v^*R_0$。
两种纤维各三点，与全部分歧次数六相等，故没有余下的分支。
由于 $dz/w$ 在原 $C$ 上的除子为 $\infty_++\infty_-$，
(96)给
$$
 \operatorname{div}(A-B)
 =b^*O+v^*R_0-p_C^*(\infty_++\infty_-).
 \tag{97}
$$

令
$$
 D_g=p_C^*(P_1+P_2-\infty_+-\infty_-),
 \qquad \operatorname{div}g=2D_g.
$$
§10已经逐点支付的原 $h$ 除子是
$$
 \operatorname{div}h
 =v^*O+b^*O+D_g-p_C^*(\infty_++\infty_-).
$$
与(97)相减得到
$$
 \operatorname{div}\frac{h}{A-B}
   =D_g+v^*O-v^*R_0.
 \tag{98}
$$
而 $X-e$ 在 $B$ 上的除子是 $2R_0-2O$。
所以(94)两边之比确为常数；
这一步只使用已经固定的实际映射及除子，没有把线丛同构当作
函数相等。

现在在(62)的明确点 $A=0,B=-2$ 求该常数。
这里
$$
 z=0,\quad w=8,\quad \xi=0,\quad \xi'=1,\quad
 A-B=2,\quad g=a^2.
$$
按(49)的原表达式取极限，三项分别给
$$
 -72a,\qquad144,\qquad36a^2;
 \quad
 h=36(a^2-2a+4).
 \tag{99}
$$
例如 $\xi\sim-3A/2,\ z\sim-2A$，
$H_1\sim16a^2/z,\ H_2\sim64a^2/z^2$，
故(99)包含了两个不能直接按 $\xi=0$ 删掉的有限项。

原群律给 $r(P)=(-1,\omega)$、$b=(-1,\omega^2)=-r(P)$；
$r(P)$ 为三挠点，因此 $v=b+R_0$。
其相加斜率为 $-2\delta/(a^2-4)$，所以
$$
 X(v)+\frac{a^2}{4}
 =1+\frac{a^2}{2}-\frac{12}{(a^2-4)^2}
 =-\frac3{a(a-1)}.
$$
又由 $a^3=4$，
$$
 (a^2-2a+4)^2=12a(a-1).
$$
将这些值代入(98)所得的常数比例，准确为
$-1/(2916a)$，证明(94)。
对所有 $q\ge5$，这里 $a\ne0,1$、$a^2\ne4$，
(99)非零；所以求常数的分支没有未处理的小特征例外。
其余零点、极点按函数域恒等式及光滑射影模型延拓。
$\square$

### 16.1. 半线性下降不丢失 $-1/a$

先在含 $\delta$ 的原域上，把(95)看成 $B_v$ 的 étale 二盖。
设 $y_v=Y(v)+1/2$，则
$$
 y_v^2=X(v)^3+\frac14.
$$
原 $\delta\mapsto-\delta$ 的下降同时给
$b\mapsto-b$、$r(P)\mapsto-r(P)$，
而 $R_0=-R_0$，所以 $v\mapsto-v$。
$A,B,a,h,g$ 保持固定；对原形式平方根 $\sqrt g$ 取其定义的
下降作用，(95)中的 $s$ 也保持固定。
因此 $y_v/s$ 变号，不能把它直接叫作 $\mathbf F_q$ 坐标。

准确的下降坐标是
$$
 U=\frac{y_v}{\delta s}.
$$
由 $X(v)=e-as^2$、$e^3=-1/4$，得到实际模型
$$
 \boxed{
 D_2^-:\quad U^2=\frac43s^4+as^2+\frac{a^2}{4},
 \qquad
 X(v)=e-as^2,\quad
 \frac{y_v}{\delta}=sU.
 }
 \tag{100}
$$
全部系数在 $\mathbf Q(a)$ 中；
对惰性 $q$，$a$ 为 $\mathbf F_q$ 中唯一的立方根，
所以这就是原 $\mathbf F_q$ 下降模型。
其目标准确是
$$
 B^-:\quad -3V^2=X^3+\frac14,\qquad
 (X,V)=(e-as^2,sU).
 \tag{101}
$$
在 $\mathbf F_{q^2}$ 上再以 $y_v=\delta V$
返回原 $B$，并保留该指定方向。

(100)有两个明确的 $\mathbf F_q$ 点
$$
 O_2=(0,a/2),\qquad T_2=(0,-a/2).
 \tag{102}
$$
二者在(101)都送到 $R_0=(e,0)$。
因此给 $D_2^-$ 选原点 $O_2$，再在目标作真实平移 $+R_0$，
才得到保原点的 degree2 同源
$$
 I:D_2^-\longrightarrow B^-,
 \quad
 \begin{cases}
 X_I=-a^2/4-3/(4s^2),\\
 V_I=-3U/(4as^3).
 \end{cases}
 \tag{103}
$$
这些式子就是(101)与 $(e,0)$ 的实际群律相加；
它们在(102)的两点延拓到 $O$。
二盖的甲板作用为 $(s,U)\mapsto(-s,-U)$，
交换(102)的两点；其核为 $\{O_2,T_2\}$。
群逆元则是 $(s,U)\mapsto(-s,U)$。
这区分了平方根的符号、群逆元和目标平移三种不同操作。

为确认这确实是 CM 椭圆二同源而不只一张四次式，
(100)有双向 Weierstrass 变换
$$
 \begin{aligned}
 x_2&=\frac{a(U+a/2)}{s^2},\\
 y_2&=\frac{a^2(s^2+U+a/2)}{s^3},\\
 s&=\frac{a(x_2+a)}{y_2},\qquad
 U=\frac{x_2s^2}{a}-\frac a2,
 \end{aligned}
$$
$$
 \boxed{
 y_2^2=(x_2+a)\left(x_2^2-\frac43a^2\right).
 }
 \tag{104}
$$
$O_2$ 送到无穷点，$T_2$ 送到 $(-a,0)$。
平移 $x_2$ 消去平方项后，短模型系数为
$-5a^2/3$、$-88/27$；故其判别式为 $2^{12}/27$，
$j=54000$。它在 $q\ge5$ 光滑，并由(103)实际同源于
$j=0$ 的 $B^-$。尤其其 CM 身份来自这条已给出的同源，
不依赖只认一个 $j$ 标签。

最后，(95)、(100)给同一个平方根盖的实际纤维积识别
$$
 \boxed{
 \operatorname{Norm}\bigl(C_\delta(\sqrt g)\bigr)
 \simeq
 \operatorname{Norm}
 \left(C_\delta\times_{B^-,\,v^-}D_2^-\right),
 }
 \tag{105}
$$
其中右侧用的是未平移的(101)，
$v^-=(X(v),y_v/\delta)$。
若改用保原点的(103)，同时必须把底映射改成 $v^-+R_0$。
这两个表示不能混用。
原平方根盖连通：$p_C$ 的次数为三，而原 $L$ 是非零二挠；
若 $p_C^*L$ 为零，取 norm 得 $L^3=L=0$，矛盾。
因此(105)没有偷偷丢掉一支或改为平凡平方类。

本节已经把原 $g$ 的谱平方根及其下降真正接到一个固定 CM
二同源，且给出了所有函数和原点。
这仍不是(19)的有理点：还必须让该实际平方根运输满足
(19)中同时保留的两条二次式。
特别是这里的 $O_2$ 是常曲线二盖的原点，不能把它当作原
椭圆曲面上的非挠截面或原27对的非零值。
