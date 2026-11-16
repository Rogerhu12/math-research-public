# R843 — 原最低属四来源的真实椭圆商、次数三同源与 CM 参数

日期：2026-11-16。**状态：下列商映射、同源、参数和条件性 CM 结论已证明。**
本篇只处理 R841 附录 B 所得原有限曲线表达中，像正规化确为亏格四的项。
它不假定这种项已经出现或非零，也不把一般参数的曲线换作原端点类。

## 1. 从同一个原曲线项出发

R841 B 保整个有理 Hecke packet、原三个权一对应及其 Artin 系数，
用真实 Hom 双线性与对称性把原类展开成
$$
\sum_i c_i\Pi\,\Phi_{F_i,a_i,*}[X],
\qquad \Phi_{F,a}=(F,a q_0,a q_2).
\tag{1}
$$
对其中一个生成 $E_0^3$ 的实际像，取正规化 $D$。
若 $g(D)=4$，同一 $R_N$ 和半平移 $S$ 给
$$
D:\quad y^3=x(x^4+a x^2+b),\qquad
b(a^2-4b)\ne0,
\tag{2}
$$
$$
v(x,y)=(x,\omega y),\qquad s(x,y)=(-x,-y),
\quad \omega^2+\omega+1=0.
\tag{3}
$$
全部坐标变换只需一个先于目标素数 $p$ 固定的有限扩域。
R841 A 已证明此实际来源还满足
$$
J(D)\sim E_0^4,\qquad \operatorname{End}^0(E_0)=K=\mathbf Q(\sqrt{-3}).
\tag{4}
$$
一般 (2) 不满足 (4)；本篇的 CM 结论确实使用这一额外限制。

记 $d=a^2-4b$。原二阶商的准确不变量
$$
z=y/x,\qquad w=x^2-b/x^2
$$
给
$$
H=D/\langle s\rangle:\quad
w^2=z^6-2az^3+d .
\tag{5}
$$
因为 $z^3=x^2+a+b/x^2$，式 (5) 逐项成立，且
$x^2=(z^3-a+w)/2$、$y=xz$，所以函数域指数恰为2。
右侧重根只能满足 $z=0$ 或 $z^3=a$；
分别迫 $d=0$ 或 $b=0$，已被 (2) 排除。
故 $H$ 平滑、亏格2，且由实际 norm/pullback
$$
J(H)\sim E_0^2.
\tag{6}
$$

选择固定的 $c$ 满足 $c^6=d$，置
$$
X=z/c,\qquad Y=w/c^3,\qquad \mu=-2a/c^3.
$$
则同一个曲线商变为
$$
\boxed{H_\mu:\ Y^2=X^6+\mu X^3+1,\qquad
\mu^2-4=16b/d\ne0.}
\tag{7}
$$
$\mu$ 是本篇的曲线参数，不能与原 Hecke 角色 $\lambda_\nu$ 混同。

## 2. 两个实际 degree-two 椭圆商

在 (7) 上有真实自同构
$$
r(X,Y)=(\omega X,Y),\qquad
t(X,Y)=(X^{-1},Y/X^3),\qquad
\iota(X,Y)=(X,-Y).
\tag{8}
$$
它们延拓到光滑射影曲线，满足
$$
r^3=t^2=\iota^2=1,\quad trt=r^{-1},\quad
\iota r=r\iota,\quad \iota t=t\iota .
\tag{9}
$$
$t$ 的固定点恰为 $X=1$ 的两个点；
$X=-1$ 若固定则须 $Y=0$，将迫 $\mu=2$。
同样 $\iota t$ 恰有 $X=-1$ 的两个固定点。
Riemann–Hurwitz 因而给两个 genus-one 商。

显式令
$$
u=X+X^{-1},\qquad
v_+=Y(X+1)/X^2,\qquad v_-=Y(X-1)/X^2.
$$
由于 $X^3+X^{-3}=u^3-3u$，有
$$
\boxed{
E_+:\ v_+^2=(u+2)(u^3-3u+\mu),\qquad
E_-:\ v_-^2=(u-2)(u^3-3u+\mu).
}
\tag{10}
$$
$v_+$ 由 $t$ 固定，$v_-$ 由 $\iota t$ 固定。
又 $X$ 满足 $X^2-uX+1=0$，并可由 $v_\pm$ 恢复 $Y$，
所以两个函数子域指数准确为2，所显示的映射就是完整商
$$
q_+:H_\mu\to E_+=H_\mu/\langle t\rangle,\qquad
q_-:H_\mu\to E_-=H_\mu/\langle\iota t\rangle.
\tag{11}
$$
分别以 $(-2,0)$、$(2,0)$ 为椭圆曲线原点。
这些点确为光滑点，因为 $\mu\ne\pm2$。

以下 $q_\pm^*$、$q_{\pm,*}$ 均表示实际 Jacobian pullback 和 norm，
不将曲线上的非原点保持复合误写成群同态。
在 $J=J(H_\mu)$ 上，超椭圆 involution 诱导 $[-1]$，
故
$$
q_+^*q_{+,*}=1+t,\qquad q_-^*q_{-,*}=1-t,
\qquad q_{\pm,*}q_\pm^*=[2].
\tag{12}
$$
这里的 $r,t$ 也表示它们在 $J$ 上的真实协变同态。

## 3. 一个准确的 Jacobian 恒等式

$r$ 的曲线商由 $U=X^3,Y$ 给出
$$
H_\mu/\langle r\rangle:\quad Y^2=U^2+\mu U+1.
$$
这是 genus-zero 曲线。因此商的 norm/pullback 在 $J$ 上为零，
严格得到
$$
\boxed{1+r+r^2=0\quad\text{于 }\operatorname{End}(J).}
\tag{13}
$$
这不是由全纯微分的特征猜出的高余维 Chow 等式；
它是完整曲线商在 Jacobian 上的等式。

令
$$
A=q_{+,*}r q_+^*\in\operatorname{End}(E_+).
$$
因 $tq_+^*=q_+^*$、$q_{+,*}t=q_{+,*}$ 及 (9)，
$$
q_{+,*}r^{-1}q_+^*=q_{+,*}trtq_+^*=A.
$$
把 (13) 左右复合 $q_{+,*},q_+^*$，得到 $[2]+2A=0$。
椭圆曲线同态群无整数挠元，故
$$
\boxed{A=-[1].}
\tag{14}
$$

现在定义原两个椭圆商之间的实际同态
$$
\boxed{
\alpha=q_{-,*}r q_+^*:E_+\longrightarrow E_-,
\qquad
\beta=q_{+,*}r^{-1}q_-^*:E_-\longrightarrow E_+.
}
\tag{15}
$$
用 $r^{-1}tr=rt$、(12)、(14)，逐项计算
$$
\begin{aligned}
\beta\alpha
 &=q_{+,*}r^{-1}(1-t)r q_+^*\\
 &=q_{+,*}(1-rt)q_+^*\\
 &=[2]-q_{+,*}r q_+^*\\
 &=[3].
\end{aligned}
\tag{16}
$$
曲线自同构 $r$ 保持 Jacobian 的主极化，
其 Rosati 对偶是 $r^{-1}$；norm 与 pullback 互为极化对偶。
所以 (15) 中 $\beta=\alpha^\vee$。式 (16) 因而严格给
$$
\boxed{\deg\alpha=3,\qquad
\alpha^\vee\alpha=[3],\qquad
\alpha\alpha^\vee=[3].}
\tag{17}
$$
特征零下 $\ker\alpha$ 是阶3的循环子群。
这里的次数由真实对应复合支付，不以“两个 $j$ 满足模块方程”
替代同源构造。

为说明选择 $\omega$ 不改变循环子群，注意
$q_{-,*}q_+^*=0$：它同时等于自身与自身的负数，这是 (12)
中 $t$ 的两种特征给出的。
再由 (13)，
$$
q_{-,*}r^{-1}q_+^*=-\alpha .
\tag{18}
$$
故把 $\omega$ 共轭成 $\omega^2$ 只将 $\alpha$ 改为 $-\alpha$，
保持同一个核。特别在以 $\mu$ 为变量的 (7)–(10) 家族中，
$(E_+,\ker\alpha)$ 的模点已经在 $\mathbf Q(\mu)$ 上定义。

## 4. 全常数的 Weierstrass 变换与 $j$-参数

从 (10) 的 $E_+$ 出发，令
$$
U=(u+2)^{-1},\qquad V=v_+/(u+2)^2.
$$
则
$$
V^2=1-6U+9U^2+(\mu-2)U^3.
$$
再置 $x_1=(\mu-2)U,\ y_1=(\mu-2)V,\ x_2=x_1+3$，得到
$$
\boxed{
E_+:\ y_1^2=x_2^3-3(2\mu+5)x_2+(\mu^2+14\mu+22).
}
\tag{19}
$$
原点 $(-2,0)$ 正是该三次模型的无穷远点。
写右侧系数为 $A_+=-3(2\mu+5)$、$B_+=\mu^2+14\mu+22$，
直接展开有
$$
4A_+^3+27B_+^2=27(\mu-2)^3(\mu+2).
$$
因此
$$
\boxed{
j_+=-\frac{6912(2\mu+5)^3}{(\mu-2)^3(\mu+2)}.
}
\tag{20}
$$
变换 $X\mapsto-X$ 将 $H_\mu$ 送到 $H_{-\mu}$，
同时把两种 involution 商交换；于是
$$
\boxed{
j_-=j_+(-\mu)
=-\frac{6912(5-2\mu)^3}{(\mu+2)^3(\mu-2)}.
}
\tag{21}
$$

令
$$
\boxed{T=-27\frac{\mu+2}{\mu-2}.}
\tag{22}
$$
对当前平滑有限 $\mu$，$T\ne0,-27$，且不是无穷远。
代入 (20)、(21)，严格得到
$$
\boxed{
j_+=\frac{(T+27)(T+3)^3}{T},\qquad
j_-=\frac{(T+27)(T+243)^3}{T^3}.
}
\tag{23}
$$
这正是 $X_0(3)$ 的标准有序两个 $j$-映射的一种规范，
Fricke 对换为 $T\mapsto729/T$。
在当前参数中 $\mu\mapsto-\mu$ 正好实现这个对换。
可与 González–Jiménez–Lario 作者所载补充材料 §2.1 的
$T=3^6(\eta(3\tau)/\eta(\tau))^{12}$ 规范逐项核对；
这里只用其显示的两个有理函数，不使用其后关于有理同源图或概率的结论。

还可把 (23) 与 (15) 的**指定核**相认，而不仅是无序的 $j$ 对。
对几何泛型 $\mu$，$E_+$ 无 CM，两个 degree3 同态
$E_+\to E_-$ 必相差一个符号：
其 Hom 群为秩1自由群，同一次数限制只容许两个相反的生成倍数。
故泛型有序 $j$ 对唯一决定核。
(15) 与 (23) 的模点在泛型一致，
由分离的模块曲线及平滑族中的有限 étale 核延拓，
它们在所有 $\mu\ne\pm2$ 的当前家族中一致。
这同时保留特殊 CM 参数处可能出现的其它同源，
而不在这些特殊点重新任选核。

## 5. 原几何迫出的 CM 条件，以及仍未支付的比较

本篇到 (23) 的全部构造对任意 $\mu\ne\pm2$ 都成立。
若它来自本篇开头的原最低属四项，则额外使用 (6)：
$E_\pm$ 是 $J(H)$ 的实际非零椭圆商，而 $J(H)\sim E_0^2$。
所以
$$
E_\pm\sim E_0,\qquad
\operatorname{End}^0(E_\pm)=K.
\tag{24}
$$
由此
$$
\boxed{(E_+,\ker\alpha)\text{ 是 }X_0(3)\text{ 上的一个实际 }K\text{-CM 点。}}
\tag{25}
$$
它是从原曲线项的两次商与 Jacobian 同态得到的；
不是先选择一个 $K$-CM 点后声称它就是原来源。

(24) 不固定整数 endomorphism order。
两个端点的 CM order 也不能仅凭 (17) 就视作相同；
三同源可改变 order 的3部分。
本篇没有从 $\eta_\nu$ 的阶18直接推定 conductor34，
没有算出原具体 $a,b$ 或 $T$，
没有识别这个 CM 点的 Galois 轨道及原17处角色。

同样，(25) 本身不把
$\Pi\Phi_{F,a,*}[X]$ 变成 R814 的指定 canonical cycle。
尚须给实际 cycle 对应、原有限角色提取、非零系数及全部
局部/Euler/period 规范；同一 CM 域或同一个 $j$-轨道不能替代它们。
这正是下一接续问题。

原 (1) 的系数、$X\to D$ 的有限推前次数、R841 的
$1/2$ polarization 及三个 $1/3$ 平均系数一直保留。
本篇的 degree2、degree3 均在同一个曲线项内部，未擅自乘回原类；
R831 的 $6^{-2}$、$X_1$ 遗忘 $1632/816$ 和 $12^{-2}$ 仍原样保持。
没有证明原端点、其 AJ 或某个指定局部化非零，
更没有由此推出无穷多个 $p$ 的全 $\Sha[p^\infty]$ 有限。

## 6. 依赖与核对来源

- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)，
  附录 A、B：同一个原有限 Hom 表达、最低属四模型和全部有限系数。
- [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  原最高投影、平移不变性和实际曲线像；本篇只在权一 Jacobian 上作同态计算。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  原两个退化、唯一端点与完整 $X_0/X_1$ 倍率。
- Enrique González–Jiménez and Joan Carles Lario,
  *Faltings elliptic curves in twisted Q-isogeny classes — Supplementary Material*,
  作者网页稿，§2.1（所载 PDF 第13页）：
  <https://web.mat.upc.edu/joan.carles.lario/types.pdf>。
  此项仅核对 (23) 的参数规范；(5)–(22) 与实际同源次数均已在本文自含证明。

本篇没有执行数值计算、目标素数扫描或生成可重算数据。


## 附录 A. 同一 genus-four 曲线的实际纤维积与全部同源次数

本附录补出 (2) 中一直存在的固定 $j=0$ 部分。
只要 $b(a^2-4b)\ne0$ 即成立；无需先假定原来源的 (4)。

### A.1. 两个非奇异 $j=0$ 商及真实逆式

在固定有限扩域中取 $\beta^2=b$，$\beta\ne0$，令
$$
\delta(x,y)=(\beta/x,\beta y/x^2).
\tag{A1}
$$
将右侧代入 (2)，利用
$$
(\beta/x)\big((\beta/x)^4+a(\beta/x)^2+b\big)
=\frac{\beta^3}{x^6}\,x(x^4+a x^2+b),
$$
可见 $\delta$ 是曲线自同构。
它满足 $\delta^2=1$，并与原 $s,v$ 交换。
本附录的 $\delta$ **不是**正文 (8) 在 $H_\mu$ 上的 $t$。

令
$$
z=y/x,\qquad U_+=x+\beta/x,\qquad U_-=x-\beta/x.
$$
同一曲线函数严格满足
$$
\boxed{
\mathcal E_+:\ U_+^2=z^3-a+2\beta,\qquad
\mathcal E_-:\ U_-^2=z^3-a-2\beta.
}
\tag{A2}
$$
由 $a^2-4b\ne0$，两条三次方程的常数均非零，
所以是非奇异的 $j=0$ 椭圆曲线。
以各自无穷远为原点。这里用 $\mathcal E_\pm$，
与正文的三同源端点 $E_\pm$ 严格区分。

这些坐标不是只构造了一个映射：
$$
\boxed{
x=(U_++U_-)/2,\qquad y=xz,\qquad
\beta/x=(U_+-U_-)/2.
}
\tag{A3}
$$
最后一式由 $U_+^2-U_-^2=4\beta$ 得到。
因此 $D$ 准确是下面实际纤维积的光滑正规化：
$$
\boxed{
D=\operatorname{Norm}
\bigl(\mathcal E_+\times_{\mathbf P^1_z}\mathcal E_-\bigr).
}
\tag{A4}
$$
(A3) 支付了整个函数域，未丢失一个隐藏的有限覆盖次数。

各自的泛型次数恰为2。事实上 $(z,U_+)$ 的非平凡 deck 变换为
$\delta$，而 $(z,U_-)$ 的非平凡 deck 变换为 $s\delta$；
$x$ 满足相应二次方程并可恢复 $y$。记这两个真实商为
$$
p_+:D\to\mathcal E_+=D/\langle\delta\rangle,\qquad
p_-:D\to\mathcal E_-=D/\langle s\delta\rangle.
\tag{A5}
$$
$r_D:=v$ 在两条椭圆商上均作用为
$(z,U_\pm)\mapsto(\omega z,U_\pm)$，在原点保持阶3，
微分 $dz/(2U_\pm)$ 上的特征均为 $\omega$。

### A.2. 原 genus-two 商与 Klein 四群

$s$、$\delta$ 在这套真实坐标上的作用为
$$
s:(z,U_+,U_-)\mapsto(z,-U_+,-U_-),
$$
$$
\delta:(z,U_+,U_-)\mapsto(z,U_+,-U_-).
\tag{A6}
$$
两者生成真正的 Klein 四群 $V_4$。
全部不变量域为固定的 $k(z)$，故
$$
D/V_4=\mathbf P^1_z.
\tag{A7}
$$
乘积
$$
w=U_+U_-=x^2-b/x^2
$$
恢复正文的同一个 $H=D/\langle s\rangle$，以及
$$
w^2=(z^3-a+2\beta)(z^3-a-2\beta)
=z^6-2az^3+a^2-4b.
\tag{A8}
$$
$\delta$ 下降到 $H$ 正是超椭圆 involution $(z,w)\mapsto(z,-w)$。
这也逐式说明三个非平凡 $V_4$ 特征的维数分别为 $2,1,1$，
没有平凡特征：
$H$ 对应 $s=+1,\delta=-1$，
$\mathcal E_+$ 对应 $s=-1,\delta=+1$，
$\mathcal E_-$ 对应 $s=-1,\delta=-1$。

### A.3. 实际次数16同源与极化

写 $p_s:D\to H$ 为原二重商，定义真实 norm 同态
$$
\Phi=(p_{s,*},p_{+,*},p_{-,*}):
J(D)\longrightarrow J(H)\times\mathcal E_+\times\mathcal E_-.
\tag{A9}
$$
以右侧的乘积极化和左侧的 canonical 主极化识别对偶，
其极化对偶为
$$
\Phi^\vee=p_s^*+p_+^*+p_-^*.
$$
曲线商恒等式给
$$
\Phi^\vee\Phi
=(1+s)+(1+\delta)+(1+s\delta).
\tag{A10}
$$
另一方面，(A7) 的 norm/pullback 经过 $J(\mathbf P^1)=0$，
所以在实际 $\operatorname{End}J(D)$ 中
$$
1+s+\delta+s\delta=0.
$$
将其代入 (A10)，得到
$$
\boxed{\Phi^\vee\Phi=[2].}
\tag{A11}
$$
因此 $\Phi$ 是同源。左右维数均为4，极化对偶与原同源次数相等，
$\deg[2]=2^8$，故
$$
\boxed{\deg\Phi=16.}
\tag{A12}
$$
也可直接由不同 $V_4$ 特征使所有交叉 norm/pullback 为零，
得到 $\Phi\Phi^\vee=[2]$。
其核包含于 $J(D)[2]$；没有把 (A12) 误写成 degree8 或任意未定幂。

正文两个椭圆商还给真实同态
$$
Q=(q_{+,*},q_{-,*}):J(H)\longrightarrow E_+\times E_-.
$$
(12) 使 $Q^\vee Q=(1+t)+(1-t)=[2]$，
所以
$$
\boxed{\deg Q=4.}
\tag{A13}
$$
(A9) 后接 $Q\times1\times1$ 的总次数准确为 $64$。
正文 (15) 另给 $E_+\to E_-$ 的 degree3 同源；
这三个数是不同实际映射的次数，不能混为同一个系数。

### A.4. 对原最低亏格条件的精确加强

(A2) 的两个固定 $j=0$ 椭圆因子在一个固定有限扩域上
均与 $E_0$ 同构。由 (A9)、(A13) 和正文的三同源，
对任意当前参数均有
$$
\boxed{J(D)\sim E_0^2\times E_+^2.}
\tag{A14}
$$
故在几何同源意义下，
$$
\boxed{
J(D)\sim E_0^4
\ \Longleftrightarrow\
E_+\sim E_0
\ \Longleftrightarrow\
\operatorname{End}^0(E_+)=K.
}
\tag{A15}
$$
最后一条使用特征零 CM 椭圆曲线的格描述：
同一虚二次域中的秩二格在乘一个非零复常数后彼此可公度，
所以有相同 CM 域的椭圆曲线几何同源；整数 order 可以不同。

(A15) 将 R841 属四来源的几何同源条件准确集中到
正文 (22)–(25) 的一个 $X_0(3)$ 模点。
它仍未计算原 Hom 表达中的实际模点或其整数 order，
也没有给指定 Artin 角色的 cycle 比较。
一般参数的两个 $j=0$ 因子本身不能支付这些缺口。

为防止从新对称性得到错误消失结论，可核同一个最高全纯空间：
$H^0(D,\Omega^1)_\omega$ 的维数为3，
$s$ 在其上特征为 $(-1,+1,-1)$；
$\delta$ 的特征为 $(+1,-1,-1)$。
两者的 determinant 都为 $+1$。
所以这里的 $V_4$ 不给原最高因子额外的负号，
没有由此证明原类为零或非零。

本附录只分解同一个实际曲线项的 Jacobian。
原 (1) 的全部有限系数、$\deg(X\to D)$ 与 $X_0/X_1$ 尺度不变；
(16)、(A12)、(A13) 没有被无依据地乘入原端点类。
所有等式均为显示的函数域或 Jacobian 同态推导，无新增数值运行。
