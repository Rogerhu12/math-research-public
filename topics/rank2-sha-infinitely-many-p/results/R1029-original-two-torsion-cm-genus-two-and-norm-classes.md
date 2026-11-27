# R1029 — 原二挠谱盖的 CM 亏格二与四曲线、真实同源及固定 Norm 类

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明。** 本篇从原 $I_9/I_3$ 曲面自身的非零二挠点出发，
给出一条实际亏格二曲线及其 degree3 基映射、两个 degree2
椭圆商、到 $E_{27}^2$ 的准确 degree3 Jacobian 同源，以及
三次谱域中两个独立的固定平方 Norm 类。所有微分、push/pull
及 CM 符号先在特征零确定，再由同一个好模型约化。

这不是原 $S$ 与一个 K3 或 $E_{27}^2$ 的 Chow 同构。
这里分裂的是明确的亏格二 Jacobian；它为原2-descent及
Frobenius 构造提供实际输入，尚不等于一般新截面或原27对
带权评价已经求出。

## 1. 从原非零二挠点逐式取得谱曲线

保持原模型
$$
 B:\quad v^3=t(1-27t),\qquad
 S/B:\quad y^2+xy+ty=x^3,
$$
$$
 X=-3v,\quad Y=-27t,\qquad B:\ Y^2+Y=X^3.
 \tag{1}
$$
纤维反演为 $(x,y)\mapsto(x,-y-x-t)$，所以非零二挠点满足
$$
 2y+x+t=0,\qquad 4x^3+(x+t)^2=0.
 \tag{2}
$$
在相应稠密开集置
$$
 u=\frac{x+t}{2x}.
$$
则(2)准确给
$$
 x=-u^2,\qquad t=u^2(1-2u),\qquad
 1-27t=(1-3u)^2(1+6u).
 \tag{3}
$$
进一步定义
$$
 z=\frac{v}{u(1-3u)}.
$$
由(1)、(3)，
$$
 z^3=\frac{(1-2u)(1+6u)}{u(1-3u)},\qquad
 (z^3-4)u(1-3u)=1.
$$
令 $w=(1-6u)(z^3-4)$，即得到同一谱域的光滑完备化
$$
 \boxed{\mathscr C:\quad w^2=(z^3-4)(z^3-16).}
 \tag{4}
$$
其六个有限分支根互异，无穷有两个点，所以 $\mathscr C$ 的
亏格是2。对全部 $q\ge5$，六根仍互异，故这个同一模型有好约化。

原基映射 $f:\mathscr C\to B=A=E_{27}$ 为
$$
 \boxed{
 X=-\frac{3z}{z^3-4},\qquad
 2Y+1=\frac{w(z^3+2)}{(z^3-4)^2}.
 }
 \tag{5}
$$
直接代入(4)验证 $(2Y+1)^2=1+4X^3$。
原二挠点也完全恢复：
$$
 u=\frac{1-w/(z^3-4)}6,\qquad
 x_2=-u^2,\qquad y_2=-\frac{x_2+t}{2}.
 \tag{6}
$$
有理式(3)、(5)、(6)互逆于原谱曲线的函数域；
没有用同一个 $j$ 代替原三次域。

$X$ 作为 $\mathscr C$ 上的函数次数为6，而作为 $B$ 上的函数
次数为2，故 $\deg f=3$。等价地，三次谱域有实际生成元 z，
满足
$$
 \boxed{z^3+\frac3Xz-4=0.}
 \tag{7}
$$
它不是任意另选的三次 Kummer 扩张。

在 $z=0$ 的两点 $w=\pm8$，映射分别到 $T,-T$，且不分歧。
$\mathscr C$ 的两个无穷点分别也到 $T,-T$，此时
$X\sim-3z^{-2}$，所以分歧指数为2。Riemann–Hurwitz 的总分歧
次数恰为2，故这就是全部分歧。它正对应原奇数 $I_9,I_3$
单值在二挠点上的两个 transposition。

## 2. 两个实际 degree2 椭圆商

$\mathscr C$ 有明确的非超椭圆对合
$$
 \iota:(z,w)\longmapsto(4/z,\,8w/z^3).
 \tag{8}
$$
它的平方为恒等，且直接保持(4)。
相应不变量为
$$
 U=z+4/z,\qquad V_+=w(z+2)/z^2,
$$
给出实际 degree2 商
$$
 \boxed{E_+:\quad V_+^2=(U+4)(U^3-12U-20).}
 \tag{9}
$$
与超椭圆对合复合后，取 $V_-=w(z-2)/z^2$，得到另一商
$$
 \boxed{E_-:\quad V_-^2=(U-4)(U^3-12U-20).}
 \tag{10}
$$
例如(9)只需使用
$z^3+64/z^3=U^3-12U$ 及 $(z+2)^2/z=U+4$。
反向 z 满足 $z^2-Uz+4=0$，继而恢复 w，故次数准确为2。

对二元四次式 $aU^4+bU^3+cU^2+dU+e$，采用
$$
 I=12ae-3bd+c^2,\quad
 J=72ace+9bcd-27ad^2-27b^2e-2c^3,\quad
 j=\frac{6912I^3}{4I^3-J^2}.
$$
(9)、(10)分别给
$$
 \begin{array}{c|ccc}
 &I&J&j\\ \hline
 E_+&0&11664&0\\
 E_-&1440&-109296&-12288000 .
 \end{array}
 \tag{11}
$$
第二行 $4I^3-J^2=-1296^2$。
这些数值由四次式的完整系数直接代入得到，未用近似 CM 识别。

(9)还有完全有理的短 Weierstrass 模型。以其点
$(U,V_+)=(-4,0)$ 为零点，令
$$
 k=(U+4)^{-1},\qquad \ell=V_+/(U+4)^2.
$$
则
$$
 \ell^2=1-12k+36k^2-36k^3
       =-36(k-1/3)^3-1/3.
$$
所以
$$
 X_+=-36(k-1/3),\quad Y_+=36\ell,\qquad
 \boxed{Y_+^2=X_+^3-432.}
 \tag{12}
$$
原 $A$ 经 $X_B=4X,Y_B=8Y+4$ 为
$Y_B^2=X_B^3+16$，二者之间的实际 degree3 同源是
$$
 (X_B,Y_B)\longmapsto
 \left(\frac{X_B^3+64}{X_B^2},
       \frac{Y_B(X_B^3-128)}{X_B^3}\right).
 \tag{13}
$$
代入方程即核(12)，核为 $O,(0,4),(0,-4)$；
微分保持由两个显示坐标的直接求导也可核定。

## 3. 固定 $K$ 同构、原微分与交叉迹的符号

令 $\delta^2=-3$、$\delta=1+2\omega$，仍用
$A:Y^2+Y=X^3$ 及 $\omega_A=dX/(2Y+1)$。
(9)的指定 $K$ 同构到 A 给实际 degree2 映射
$r:\mathscr C\to A$：
$$
 \boxed{
 X_r=-\frac{U+1}{U+4},\qquad
 2Y_r+1=\frac{\delta V_+}{(U+4)^2}.
 }
 \tag{14}
$$
(12)的计算已逐式验证此同构。固定此处的 $\delta$ 后不再
任添另一二次扭曲。

从(5)、(14)直接求导，准确得到
$$
 \boxed{
 f^*\omega_A=6\frac{dz}{w},\qquad
 r^*\omega_A=\delta(z-2)\frac{dz}{w}.
 }
 \tag{15}
$$
这两条是 $\mathscr C$ 的一形式基，故不是只给一个相同的
纯表示标签。

记 $J=\operatorname{Jac}(\mathscr C)$，并以星号下标表示 Jacobian
之间的真正推前同态。令
$$
 F=f_*:J\to A,\qquad R=r_*:J\to A.
$$
其相对于标准主极化的对偶分别为 $f^*,r^*$。
有限曲线映射的 pull 后 push 给
$$
 FF^\dagger=[3],\qquad RR^\dagger=[2].
 \tag{16}
$$
为定交叉项，(7)给 $\operatorname{Tr}_{\mathscr C/B}(z)=0$。
由(15)，
$$
 f_*(r^*\omega_A)
  =\operatorname{Tr}_{\mathscr C/B}
       \left(\frac{\delta(z-2)}6\right)\omega_A
  =-\delta\,\omega_A.
 \tag{17}
$$
左边正是同态 $R F^\dagger:A\to A$ 的 pullback 微分。
在特征零中，椭圆曲线同态的微分表示单射，因此
$$
 \boxed{RF^\dagger=[-\delta],\qquad
        FR^\dagger=[\delta].}
 \tag{18}
$$
第二式是第一式的主极化对偶，使用 $[-\delta]^\vee=[\delta]$。
它没有把两次 trace 的方向混为同一个负号。

于是对实际同态
$$
 \Phi=(F,R):J\longrightarrow A^2
$$
有完整的极化 Gram 矩阵
$$
 \boxed{
 \Phi\Phi^\dagger
   =\begin{pmatrix}3&\delta\\-\delta&2\end{pmatrix},
 \qquad \det_K(\Phi\Phi^\dagger)=3.
 }
 \tag{19}
$$
式(15)先给 $\Phi$ 是同源。矩阵(19)在 CM 乘积上的次数是
$\operatorname{Norm}_{K/\mathbf Q}(3)=9$；而
$\deg\Phi^\dagger=\deg\Phi$，所以
$$
 \boxed{\deg\Phi=3.}
 \tag{20}
$$
这里完整支付了次数，不把“Jacobian 分裂”当成一个未定 isogeny。

以上均在特征零由实际曲线映射证明。$A,\mathscr C$ 在所有
$q\ge5$ 有好约化，曲线映射诱导的 Jacobian 同态延拓到相应好
Néron 模型，故同一个(19)在约化中保留。(20)给 degree3 的核，
对 $q\ge5$ 为有限 étale。因而全部等式也在这些约化上成立；
没有在正特征仅凭相同微分猜同态。

## 4. 原三次谱域中两个独立的平方 Norm 类

在一个固定有限域或数域扩张中取 $a^3=b^3=4$、$a\ne b$，
并记
$$
 P_a=(a,0),\qquad P_b=(b,0)\quad\text{于 }\mathscr C.
$$
设 $\infty_+,\infty_-$ 是(4)的两个无穷点。则
$$
 \operatorname{div}(z-a)=2P_a-\infty_+-\infty_-,
$$
所以
$$
 D_{a,b}:=[P_a-P_b]\in J[2],\qquad
 \operatorname{div}\frac{z-a}{z-b}=2P_a-2P_b.
 \tag{21}
$$
这些非零二挠类不能是主类：若两个不同点之差为主除子，
就会有 degree1 的非常数函数，迫曲线亏格为0。
三个根产生的三个非零类中任意两个独立，其和是第三个。

由(5)，三个 $P_a$ 全部映到 $B$ 的原点 $O_B$，故
$$
 F(D_{a,b})=0.
 \tag{22}
$$
$J[2]$ 的维数为4，$A[2]$ 的维数为2，且
$FF^\dagger=[3]$ 在二挠点上为恒等。因此
$F:J[2]\to A[2]$ 满射，其核维数恰为2。
(21)的两个独立类遂是这个核的**全部**，而非两个未核的候选。

它们在(19)下的第二坐标也明确。对 $a^3=4$，(14)化简为
$$
 r(P_a)=\left(-\frac{a^2}{4},-\frac12\right)=:R_a\in A[2].
 \tag{23}
$$
三个 $R_a$ 恰为全部非零二挠点，故
$$
 \Phi(D_{a,b})=(0,R_a-R_b).
 \tag{24}
$$
这同时核定这些固定 Norm 类与实际 CM 椭圆二挠点的对应，
没有忽略 degree3 同源中的有限核。

最后在(7)的**原三次域**中直接取 Norm：
$$
 \operatorname{N}_{\mathscr C/B}(z-a)
   =-\left(a^3+\frac3X a-4\right)
   =-\frac{3a}{X}.
$$
因此
$$
 \boxed{
 \operatorname{N}_{\mathscr C/B}
    \left(\frac{z-a}{z-b}\right)=\frac ab.
 }
 \tag{25}
$$
$a/b\in\mu_3$ 是明确的平方；例如 $\omega=(\omega^2)^2$。
(21)、(25)是原2-descent所需的实际函数与 Norm 恒等式，
而不是只在 abstract Prym 上数维数。

## 5. 每个惰性 $q$ 的规范 Frobenius 固定类

现在令 $q\ge5$ 惰性。由于立方在 $\mathbf F_q$ 上为双射，
取其唯一的 $a_0\in\mathbf F_q$ 满足 $a_0^3=4$，并置
$a_1=\omega a_0,a_2=\omega^2a_0$。Frobenius 固定 $a_0$、
交换 $a_1,a_2$，因此在(22)的二维核中，其唯一非零固定类为
$D_{a_1,a_2}$。

该类无需通过非有理系数函数表示。准确取
$$
 \boxed{g_q(z)=(z-a_1)(z-a_2)=z^2+a_0z+a_0^2
                 \in\mathbf F_q(\mathscr C)^\times.}
 \tag{26}
$$
它与 $(z-a_1)/(z-a_2)$ 相差平方 $(z-a_2)^2$，所以是同一个
平方类。并且(25)直接给
$$
 \boxed{
 \operatorname{N}_{\mathscr C/B}(g_q)
       =\left(\frac{3a_0}{X}\right)^2.
 }
 \tag{27}
$$
所有零极阶都为偶数，其半除子类就是
$D_{a_1,a_2}$。这为一般惰性约化提供了一个无需选择猜测极除子
的规范2-descent输入；另两条非零类则在 Frobenius 下互换。

本篇只声称(21)–(27)的真实非平凡 Norm 类。
把它用于原反 Frobenius 截面时，还要保留二次 twist $-3$、
确切的局部条件，以及从相应覆盖方程恢复 $(x,W,y)$ 的步骤。
不能仅由一个 Norm 为平方的函数宣布已经得到一个有理截面。


## 6. 原完整二挠谱域的显式 S3 闭包

上述非 Galois 三次域还具有完全显示的 Galois 闭包。取
$$
 \boxed{\mathscr D:\quad 4H^3=A^6-1}
 \tag{28}
$$
的光滑完备化。它是到 $A$ 直线的三次盖，在六个 $A^6=1$
点全分歧，在无穷有三个不分歧点。因此
$2g(\mathscr D)-2=-6+6\cdot2=6$，即 $g(\mathscr D)=4$。
对所有特征不为2、3的同一模型，这些点及分歧仍保留。

到原基曲线的映射准确为
$$
 \boxed{
 X=\frac{H^2}{A^2},\qquad
 Y=\frac{(A^3-1)^2}{4A^3},\qquad
 t=-\frac{(A^3-1)^2}{108A^3}.
 }
 \tag{29}
$$
由 $(A^6-1)^2=16H^6$ 直接得 $Y^2+Y=X^3$。
到前述原三次谱盖的映射则为
$$
 \boxed{
 z=\frac{A^2-1}{H},\qquad
 w=\frac{3A(A^4-1)}{H^3}.
 }
 \tag{30}
$$
逐式代回给
$$
 z^3-4=-\frac{3A^2(A^2-1)}{H^3},\qquad
 w^2=(z^3-4)(z^3-16),
$$
且(5)恰恢复(29)，不是更换了原基映射。

函数 $X$ 在 $\mathscr D$ 上有12个计重极：$A=0$ 的三个点和
无穷的三个点各为二阶。故(29)的次数为6。保持同一个
$\omega$，六个实际自同构由
$$
 \boxed{
 \sigma:(A,H)\mapsto(\omega A,\omega H),\qquad
 \tau:(A,H)\mapsto(A^{-1},-H/A^2)
 }
 \tag{31}
$$
生成。二者均固定(29)，并满足
$\sigma^3=\tau^2=1$、$\tau\sigma\tau=\sigma^{-1}$。
它们给六个不同自同构，所以(29)确为 $S_3$ Galois 盖。
(30)被 $\tau$ 固定；由原三次次数，$\mathscr C$ 恰是
$\mathscr D/\langle\tau\rangle$。

更直接地，原曲面三个非零二挠点的全部坐标为
$$
 \boxed{
 u_j=\frac{1+\omega^jA+\omega^{-j}A^{-1}}6,\qquad
 x_j=-u_j^2,\qquad y_j=-\frac{x_j+t}{2},
 \quad j=0,1,2.
 }
 \tag{32}
$$
令 $v_j=6u_j-1$，则
$v_j^3-3v_j=A^3+A^{-3}$，因而
$u_j^2(1-2u_j)=t$。这逐点核定(2)。
$\sigma$ 循环三个标号，$\tau$ 交换 $j=1,2$；
原函数 $u_j=(x_j+t)/(2x_j)$ 又能由二挠坐标恢复。
同时 $H=(A^6-1)/(4XA^2)$，故这些坐标生成的正是
原基域上的整个六次谱域，不是独立附加的 Fermat 扩张。

其二次 resolvent 也准确为
$$
 \boxed{
 S=H/A,\qquad S^2=X,\qquad
 (2Y+1)^2=1+4S^6.
 }
 \tag{33}
$$
这是 $\langle\sigma\rangle$ 的固定域。
(29)仅在原 $T,-T$ 上分歧：$A^3=1,H=0$ 的三个点到 $T$，
$A^3=-1,H=0$ 的三个点到 $-T$，各分歧指数2；
总分歧次数6已用尽 Riemann--Hurwitz。
所以原奇数 $I_9/I_3$ 的完整二挠单值也在这个同一盖中支付。

原基曲线的三次 deck 作用 $v\mapsto\omega v$ 有实际 lift
$$
 \boxed{\rho:(A,H)\mapsto(A,\omega^2H).}
 \tag{34}
$$
它保持 $t$，并使 $X$ 乘 $\omega$。因此只依赖 $A$ 的函数
在这个原三次方向上不变；不能把从 $A$ 直线取得的一个点
未经原 $\rho$ 投影就当作所需的新方向。

## 7. 该原谱盖的全 Frobenius 恒等式

这里可以直接确定 $\operatorname{Jac}(\mathscr D)$ 的 Frobenius，
但结论仍只针对(28)的实际 Jacobian。其全纯一形式的完整基为
$$
 \boxed{
 \frac{dA}{H},\qquad
 \frac{dA}{H^2},\qquad
 \frac{A\,dA}{H^2},\qquad
 \frac{A^2\,dA}{H^2}.
 }
 \tag{35}
$$
在有限分支点用 $H$ 作参数、在无穷用 $A^{-1}$ 作参数，
可逐项核正则性；四条独立且等于亏格，故没有漏掉另一个角色。

让 $\mu_6\times\mu_3$ 按 $(A,H)\mapsto(\zeta A,\xi H)$ 作用。
式(35)的角色依次为
$$
 \boxed{(1,2),\quad(1,1),\quad(2,1),\quad(3,1)
          \quad\text{于 }\mathbf Z/6\times\mathbf Z/3.}
 \tag{36}
$$
它们与各自的逆角色给 $H^1$ 的八个不同一维角色。
每对角色的有理幂等元是
$$
 e_\chi=\frac1{18}\sum_{g\in\mu_6\times\mu_3}
        \{\chi(g)^{-1}+\chi(g)\}\,g .
 \tag{37}
$$
系数为有理数，Galois 同时对角色及自同构取逆，故(37)在
$\mathbf Q$ 上定义实际有理自同态。四个像分别为一维
阿贝尔子簇，给四个在 $\mathbf Q$ 上定义、具有 $K$ 乘法的
椭圆因子及其乘积到该 Jacobian 的同源。这里不需要另定四个
因子的 twist，也不把同源改成主极化直积同构。

现在令 $q\ge5$ 为惰性素数，故 $q\equiv-1\pmod6$。
$\mathscr D$ 在 $q$ 好约化，(35)--(37)的角色分解通过同一好
模型保留。取一个不为 $2,3,q$ 的辅助 $\ell$，扩充系数使
这些有限角色分裂。以下使用 Jacobian 的 Tate 模及其实际
$q$ 次幂 Frobenius 同态，避免把 Galois 的两种 Frobenius 约定混用。
该同态将每个 $\chi$ 角色与 $\chi^{-1}$ 角色交换，所以每个
二维块上的迹为零。主极化的 Weil 交替配对只配对互逆角色，
且在此块上非退化；Frobenius 将配对乘 $q$，故该块的
行列式准确为 $q$。Cayley--Hamilton 遂给每块的平方均为 $-q$。

阿贝尔簇同态到其 $\ell$-进 Tate 模的表示是单射：
若像子簇非零，其 $\ell$-进 Tate 模不可能为零。
由此从上述完整八维表示返回同一个 Jacobian，得到真正的
同态恒等式
$$
 \boxed{
 \operatorname{Frob}_{q,\operatorname{Jac}(\mathscr D)}^2=[-q].
 }
 \tag{38}
$$
这一推论只用表示的单射，不用 Tate 猜想的满射。
例如由迹立即得
$$
 \#\mathscr D(\mathbf F_q)=q+1,\qquad
 \#\mathscr D(\mathbf F_{q^2})=q^2+1+8q.
 \tag{39}
$$
这些是由(38)证明的统一等式，未作有限域点扫描。

$\mathscr C$ 本身的相同 Frobenius 平方也可由(19)--(20)及
原 $A$ 的平方 $[-q]$ 返回。这里更付的是全部原二挠谱域、
其六度 Galois 标号和(34)的实际三次角色。Frobenius 的图
可据此进入原 Norm/2-descent；还不能由(38)把其推成 $S$ 的
Chow 比较、实际截面或原最高循环的非零。

## 8. 对后继工作的准确作用范围

(4)不是另造一个仅有同 CM 型的辅助曲线，而是原 $S$ 的非零
二挠三次谱盖，(6)给回原二挠坐标。(14)、(18)–(20)则是真实
Jacobian 映射及其完全确定的符号和次数。
因此可以继续在这个固定谱域中写原2-descent覆盖，或把
Frobenius 对固定 $\mathscr C$ 的图与(24)的有限核相接。

原最高循环仍是 R1011 的完整54图及其
$\eta/P_-/\operatorname{Cor}_{L/H}$，R1027(38)给其准确27对
表达。本篇没有从 $J\simeq_{\rm isog}A^2$ 推出 $t_2(S)$ 的
Chow 比较，更没有推出原普通 $p$ 局部 AJ 的非零。
下一步是使用(26)–(27)写出并解实际覆盖，随后对真实截面使用
该27对原公式。
