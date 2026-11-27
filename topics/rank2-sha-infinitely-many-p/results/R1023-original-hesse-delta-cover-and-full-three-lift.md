# R1023 — 原 Hesse 公共盖的准确 [δ] 身份、Frobenius 符号与全 [3] 补盖

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：完整代数证明。** 本篇把同一个原曲面的 Hesse 公共盖写成明确的
$[\delta]$ 同源，固定甲板和 Frobenius 的方向，并支付 $\alpha_q$ 拉回
Kummer 类时实际改变的三型及其常数。两条 q=11 固定极除子均已被完整
公开计算否定；本篇不重跑它们，也不把新的盖身份当成已构造截面或
原 ordinary 最高配对非零。

## 1. 固定同一基曲线与真正 Hesse 方程

令
$$
K=\mathbf Q(\delta),\qquad\delta^2=-3,\quad\omega=(-1+\delta)/2.
$$
所有下述有理函数首先在 K 上成立，也在特征不为2、3的相应光滑模型上成立。
原模型仍是
$$
B:\ Y^2+Y=X^3,\quad X=-3v,\ Y=-27t,
\qquad
\mathscr S:\ y^2+xy+ty=x^3.
\tag{1}
$$
有序坏基点为 $T=(0,0)$、$-T=(0,-1)$。

取 Fermat 曲线
$$
B':\quad w^3=\lambda^3-1
\tag{2}
$$
并定义
$$
t=\frac{\lambda^3-1}{27\lambda^3},\qquad
v=\frac{w}{3\lambda^2},
\quad
X=-\frac w{\lambda^2},\qquad Y=-\frac{w^3}{\lambda^3}.
\tag{3}
$$
直接算得 $v^3=t(1-27t)$，所以这是原 B 的覆盖，而非只相同的 j 值。

在 B' 上取 Hesse 三次曲线
$$
\mathcal H_\lambda:\quad A^3+B_1^3+C^3=3\lambda AB_1C,
\tag{4}
$$
原点是 $(1:-1:0)$。在 $u=A+B_1+\lambda C\ne0$ 的图中令
$$
z=C/u,\qquad h=(A-B_1)/u.
$$
由(4)逐项展开，
$$
3h^2=-1+6\lambda z-9\lambda^2z^2-4(1-\lambda^3)z^3.
\tag{5}
$$
因此
$$
\boxed{
x=-3\lambda t z,\qquad
2y+x+t=\delta t h
}
\tag{6}
$$
准确给(1)的原方程。反向是
$$
z=-x/(3\lambda t),\quad
h=(2y+x+t)/(\delta t),\quad
(A:B_1:C)=
\left(\frac{1-\lambda z+h}{2}:
      \frac{1-\lambda z-h}{2}:z\right).
\tag{7}
$$
它们在泛点互逆。直线 $u=0$ 是所选 Hesse 原点的挠切线；
z、h 在该点的极阶分别为2、3，故(6)保原点。
这给的是实际椭圆曲线同构，包含原三次扭曲规范。
在最小正则模型上按泛纤维同构的唯一延拓理解分母为零的图。

(6)还记录了一个真实有限符号：
对固定的 Q 模型 B' 和 Hesse 曲线共轭 K/Q 后，$\delta$ 变负，
该同构变为原纤维的 $[-1]$。等价地，在 Hesse 端交换 A、B_1。
不许只保同一个 j 而忘记这次有限扭曲。

## 2. $B'\to B$ 恰为 $[\delta]$，带显式逆同构

以 $(r,s)$ 表示一份源曲线
$$
B_{\rm src}:\quad s^2+s=r^3.
$$
定义
$$
\boxed{
\phi(r,s)=
\left(
\lambda=\frac{\delta r}{s-\omega},
\quad
w=-\frac{s-\omega^2}{s-\omega}
\right).
}
\tag{8}
$$
恒等式
$$
(s-\omega)^3-(s-\omega^2)^3
=\delta^3(s^2+s)
$$
证明 $w^3=\lambda^3-1$。
其有理逆为
$$
\boxed{
r=-\frac{\lambda}{w+1},\qquad
s=\frac{\omega w+\omega^2}{w+1}.
}
\tag{9}
$$
所以 $\phi:B_{\rm src}\simeq B'$ 是 K 上的真正同构。
源原点 O 对应 B' 的 $(\lambda,w)=(0,-1)$。

把(8)代入(3)，得到
$$
X=-\frac{r^3+1}{3r^2},\qquad
Y=\left(\frac{s-\omega^2}{\delta r}\right)^3.
\tag{10}
$$
这正是 R1019(29)已逐式支付的 $[\delta]$。因此
$$
\boxed{\pi\circ\phi=[\delta],\qquad \deg\pi=3.}
\tag{11}
$$
该同源可分且无分歧，核为 $\langle T\rangle$；
(3)不是另一条只有同构纯表示的三次覆盖。

固定
$$
\rho(\lambda,w)=(\omega\lambda,\omega^2w).
$$
由基曲线加法公式
$$
X(P+T)=-Y/X^2,\qquad Y(P+T)=-1/(Y+1)
$$
代入(8)，得到
$$
\phi(P+T)=(\omega^2\lambda,\omega w).
$$
所以
$$
\boxed{\rho\text{ 在 }B_{\rm src}\text{ 上准确对应平移 }-T.}
\tag{12}
$$
它与原 $B\to\mathbf P^1_t$ 的甲板
$\tau:(X,Y)\mapsto(\omega X,Y)$ 是两个不同的自同构。
完整三项迹在 $\rho$、$\rho^{-1}$ 下相同，但单个三次 character 的标签不同。

## 3. 惰性 q 的真正 Frobenius 符号

设 q≥5、$q\equiv2\pmod3$，$k=\mathbf F_{q^2}$。
记 F、F' 分别为 B、B' 的 q 次幂自同源；
$\sigma$ 表示对 K 系数作 $\delta\mapsto-\delta,\omega\mapsto\omega^2$。
直接共轭(8)给
$$
\sigma\phi=(\lambda/w,\,1/w)=\phi\circ[-1].
$$
于是
$$
\boxed{F'\circ\phi=\phi\circ(-F).}
\tag{13}
$$
因此在 Fermat 模型上写出的 Frobenius 图，返到这份 B 坐标后是 $-F$；
不能免费换成同号 F。式(13)也使
$F[\delta]=-[\delta]F$ 与 Q 上定义的覆盖 $\pi$ 完全交换。

下文沿 R1019 取真正的可分自同源
$$
\alpha_q[\delta]=F-1,\qquad
[\delta]\alpha_q=-F-1,\qquad
\alpha_q^2=[-d],\quad d=(q+1)/3.
\tag{14}
$$
同一 Hesse 盖的两侧复合因此分别是 $F-1$、$-F-1$；
这两个符号不能在取图和完整迹时合并。

## 4. $\alpha_q$ 精确改变了原三型

置
$$
S_3=(-1,\omega^2).
\tag{15}
$$
原加法公式或(10)立即给
$$
[\delta]S_3=T,\qquad FS_3=-S_3.
$$
又 $\sigma(\alpha_q)=-\alpha_q$，所以
$F\alpha_q=-\alpha_qF$。因此 $\alpha_qT$ 是反 Frobenius 的
$[\delta]$ 原像 T。该原像唯一：任意两个相差一个固定的三挠点，
反固定又迫其被2杀掉。由此
$$
\boxed{\alpha_qT=S_3.}
\tag{16}
$$
特别 $\alpha_q$ 不保持原 $\langle T\rangle$。
由 $\alpha_q^2=[-d]$，
$$
\alpha_qS_3=-dT.
\tag{17}
$$
这些式子也保留 $3\mid d$ 的情形，没有假定 $\alpha_q$ 在完整3挠上可逆。

原 $[\delta]$ 盖的 Kummer 类是
$$
\frac1{Y+1}=\frac{Y}{X^3},
\tag{18}
$$
因此其 divisor/3 的 Picard 类为 T。
在标准主极化下 $\alpha_q^\dagger=-\alpha_q$，故拉回的 Picard 类准确变为
$$
\boxed{\alpha_q^*T=-S_3.}
\tag{19}
$$
实际代表函数是
$$
\boxed{\ell_{-S_3}=Y+\delta X-\omega^2.}
\tag{20}
$$
令该线为零，代 $Y=-\delta X+\omega^2$ 入基曲线，得到
$(X+1)^3=0$；故
$$
\operatorname{div}(\ell_{-S_3})=3[-S_3]-3[O].
$$
这确认了切线及点的符号，而不只是抽象3挠标签。

**常数三次扭曲也已经支付。**
令 $G_\alpha$ 为以下主除子的函数，并以 $G_\alpha(O)=1$ 正规化：
$$
\operatorname{div}(G_\alpha)
=\alpha_q^*([T]-[O])-([-S_3]-[O]).
\tag{21}
$$
(19)使该除子为主除子；其在 O 的系数为0。
整个除子定义于 k，上述 O 处正规化使函数也定义于 k。
在 $z=-X/Y$ 的无穷局部参数中，$\alpha_q'(0)=-1/\delta$，
而 $Y\sim-z^{-3}$、$\ell_{-S_3}\sim Y$。比较首项便给
$$
\boxed{
Y\circ\alpha_q
=3\delta\,\ell_{-S_3}G_\alpha^3
=\ell_{-S_3}(-\delta G_\alpha)^3.
}
\tag{22}
$$
所以拉回的实际 cube 类确是(20)，没有遗漏一个非立方的有限常数。
结合(18)，原 $\lambda^3=(Y+1)^{-1}$ 的拉回准确通过
$\lambda X(\alpha_qP)/(-\delta G_\alpha(P))$ 变成
$\ell_{-S_3}$ 的三次根。

也可直接排除原盖的自提升。若存在 $\beta$ 使
$[\delta]\beta=\alpha_q[\delta]$，将 $\beta(O)\in\ker[\delta]$ 平移掉后可设
$\beta$ 为同源。取对偶得到
$-\beta^\dagger[\delta]=[\delta]\alpha_q$；
在 T 上左边为0，右边为 T，矛盾。
同理 $\beta[\delta]=[\delta]\alpha_q$ 直接在 T 上矛盾。
因此不能把 $\alpha_q$ 当成同一个固定 Hesse 三型上的自映射。

## 5. 两个独立 cube 类的全 $[3]$ 补盖

T 与 $S_3$ 是 $B[3]$ 的一组有序基：若 $aT+bS_3=0$，
施 $[\delta]$ 得 bT=0，再得 a=0。
所以 Y 与 $\ell_{-S_3}$ 在 $k(B)^\times/k(B)^{\times3}$ 中独立。
对应的两个循环 étale 三次盖的公共盖是连通的 degree9 盖。
下面用函数把它明确认作 $[3]:B\to B$，不只给一个几何同构类。

对一份 B 上的点 P，记
$$
R=[\delta]P,\quad (X_R,Y_R)=(X(R),Y(R)),
$$
并置
$$
g_+(P)=1-\frac1X-\frac{Y+1}{X^2},\qquad
g_-(P)=1-\frac1X+\frac{Y}{X^2},
$$
$$
\ell_{S_3}=Y-\delta X-\omega.
$$
将(10)代入、只用 $Y^2+Y=X^3$ 约简，得到两个完整恒等式
$$
\boxed{
\ell_{-S_3}([\delta]P)=\delta^{-3}Y(P)\,g_+(P)^3,
\qquad
\ell_{S_3}([\delta]P)=\delta^{-3}(Y(P)+1)\,g_-(P)^3.
}
\tag{23}
$$
第二式也可由第一式施 $P\mapsto-P$ 得出；
这里 $Y(-P)=-Y(P)-1$、$\ell_{-S_3}(-P)=-\ell_{S_3}(P)$。
这些都是函数域恒等式，分母零的点用光滑模型延拓。

定义显式函数
$$
\boxed{
\mathcal U(P)=-\frac{Y_R-\omega}{\delta X_R},
\qquad
\mathcal V(P)=\frac{Y(P)-\omega}{3X(P)}\,g_-(R).
}
\tag{24}
$$
由于 $[3]=[-1][\delta]^2$，(10)、(23)准确给
$$
\boxed{
\mathcal U^3=Y([3]P),\qquad
\mathcal V^3=\ell_{-S_3}([3]P).
}
\tag{25}
$$
例如 $(Y_R+1)=((Y-\omega)/(\delta X))^3$，
代入第二个(23)并施负号便得到 $\mathcal V$；
第一式同样由 $Y(-[\delta]R)=-(Y([\delta]R)+1)$ 得到。

故两个 cube 根同时位于 $[3]$ 的实际源函数域中。
该源域相对目标域次数为9，而独立两类的复合也为9，
所以
$$
\boxed{
k(B)\bigl(\sqrt[3]{Y},\sqrt[3]{\ell_{-S_3}}\bigr)
\ \text{准确由 }[3]:B\to B\text{ 给出，立方根由(24)固定。}
}
\tag{26}
$$
不需要再附一个未指定的常数域扭曲。
在 O，$\mathcal U$、$\mathcal V$ 的首项均为 $-1/(3z)$，
也固定了两个 cube 根的正规化。

有序 deck character 亦可读出：
$$
\boxed{\begin{array}{c|cc}
\text{源上的平移}&\mathcal U&\mathcal V\\ \hline
T&\mathcal U&\omega\mathcal V\\
S_3&\omega\mathcal U&\mathcal V
\end{array}}
\tag{27}
$$
第一列用 $[\delta]T=O$、$[\delta]S_3=T$ 及加法公式直接得到。
$\mathcal V(P+T)=\omega\mathcal V(P)$ 也由同一加法式得到。
余下的比值 $\mathcal V(P+S_3)/\mathcal V(P)$ 的立方为1，所以为常数；
在 O 比较主项即可定为1：
$g_-(R+T)\sim-1/(\delta z)$，
$(Y(S_3)-\omega)/(3X(S_3))=\delta/3$，
乘积仍是 $-1/(3z)$。
因此(27)保留了两个真正的方向，不靠交换三次根后再改标签。

原 Hesse 子盖在这个全盖上由
$$
\lambda=\mathcal U/X([3]P),\qquad
w=-\mathcal U^2/X([3]P)
\tag{28}
$$
给出。其 deck $\rho$ 对应完整源上平移 $S_3$，
与(12)在中间 $[\delta]$ 源上的平移 $-T$ 相容。

## 6. 对原曲面和54图允许做什么

以 $[\delta]$ 或 $[3]$ 对原光滑最小曲面作基变，得到有限 étale 映射，
次数分别为3或9。所有拉回均保持原 t、原纤维方程及原有限角色，
再在显示的 Hesse 坐标中改写。
对与 A 的乘积上的 Chow 群，完整推拉分别是乘3、乘9；
对原不除3的 ordinary p，这些次数是单位。

这允许在明确全盖中构造图或截面，再携带所有 deck 分支作真实迹。
它没有说一个新构造在推前后必非零，也没有把 $\alpha_q$ 的核、
一个切线 cube 类或某个单分量直接当作原 Q。
原 $\eta_j^{-1}$、$P_-$、full9 和 $\operatorname{Cor}_{L/H}$ 仍须全保。
若借助(26)后的构造，只能在完成全部 degree9 / degree3 迹与对应比较后
判断是否回到原最高目标。

截至本篇，尚未得到一般 q 的实际新截面，也未支付原54图非零值或
原指定 ordinary 局部配对非零。后续工作继续沿(23)–(28)的实际
Frobenius 图及全迹进行；本篇的完成结论是严格的公共盖、有限扭曲和方向。

## 内部来源

- R991、R1011：原曲面、原 full9 和未 depletion 的54图对象。
- [R1019](R1019-original-full-trace-and-inert-kernel-divisor.md)：原反 Frobenius 方向、真正 $\alpha_q$、$[\delta]$ 的公式及完整 trace 后的 q+1 限制。
- [原固定核除子降维笔记](../notes/2026-11-27-original-kernel-section-finite-equations.md)：已执行 q=11 核除子的完整阴性检验。
- [三重六挠极点笔记](../notes/2026-11-27-original-six-torsion-polar-divisor.md)：另一个实际除子的完整分支与重数证明；其 q=11 公开结果也为阴性。

本篇全部新增式子都在正文给出代数证明，不把纯动机身份或未认可的预印本作为循环运输。
