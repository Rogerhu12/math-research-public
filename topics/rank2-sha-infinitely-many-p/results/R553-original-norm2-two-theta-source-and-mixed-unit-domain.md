# R553 — 原六 sigma 的完整 Norm2 双张量与实际四线单位域

日期：2026-11-14。**状态：已证明。**
在同一原六输入上作一个在所有当前素数处可逆的 Norm2 换元，
原两态 $\rho_0,\eta$ 及其反射偶部 $h$ 全部落在两个明确的
degree2 theta 张量中。这里是整个六变量测度的恒等式，
不只是一条第一输出边际，也没有取 principal 投影。

两条新坐标具有完整、相同且绝对定标的普通核心；
两个真实单位测试给出整的对偶基。原 R544 的唯一余域准确变成
两条单位条件，其中一条是 $U^3+V^3$。这些身份保留所有第一输出、
隐藏测试及对数单位 cut；不由张量单位推出原完整中央非零。

## 1. 原来源与同一个 Norm2 换元

保 R541、R544、R546、R551 的全部固定 ray、有限坏集及系数环。
特别 $p>19$ 是普通好素数，$\omega^2+\omega+1=0$，
$\delta=1+2\omega$，$b=17$。令
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda=\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2.
\tag{1}
$$
$\Omega=\Omega_p$ 是同一个 $E_b$ 形式群周期。
写
$$
\Sigma(z)=\sigma(z)^2,\qquad
\Theta(z)=x(z)\sigma(z)^2,
\tag{2}
$$
并以 $\nu_\sigma,\nu_\Sigma,\nu_\Theta$ 表示相同 Amice 规范下的整有界测度。
$\Sigma,\Theta$ 是完整标准偶 $S_2$ 的一组基，
分别有 CM 型 $2,0$：
$$
\Sigma(\zeta z)=\zeta^2\Sigma(z),\qquad
\Theta(\zeta z)=\Theta(z)\quad(\zeta\in\mu_6).
\tag{3}
$$

六个原输入是 $(\xi_1,\xi_2,\xi_3,x,c,d)$，
$$
\rho_0=-\frac1{84}\nu_\sigma^{\otimes6},\qquad
\eta=\omega^2H_*\rho_0,\qquad h=\eta+\frac12\rho_0.
\tag{4}
$$
$H$ 只作用于末两输入，真实矩阵为
$$
H=\frac12
\begin{pmatrix}
-1-\omega&-1-2\omega\\
2+\omega&-1-\omega
\end{pmatrix}.
\tag{5}
$$
设
$$
\boxed{U=c+\omega d,\qquad V=c-\omega d,}
\qquad
c=\frac{U+V}{2},\quad d=\frac{\omega^2(U-V)}2.
\tag{6}
$$
记整个六维换元为 $P$。末两行 Hermitian 范数皆为 $2$、相互正交，
行列式为 $-2\omega$；因此 $P$ 在原 $\mathbf Z_p^6$ 上是整可逆映射。
原 $c,d$ 同时落在 $p^n\mathbf Z_p$ 当且仅当 $U,V$ 同时如此；
单个原输入条件仍须按 (6) 转置。

令
$$
\mathcal X=\nu_\Theta\otimes\nu_\Sigma,\qquad
\mathcal Y=\nu_\Sigma\otimes\nu_\Theta
\tag{7}
$$
为真正的 $(U,V)$ 两变量测度。后文张量积均保前四个独立 sigma 输入。

## 2. 完整双张量身份

**定理1。** 在整个原六变量测度上准确有
$$
\boxed{
\begin{aligned}
P_*\rho_0&=\frac{\omega}{84}\nu_\sigma^{\otimes4}
 \otimes(\mathcal X-\mathcal Y),\\
P_*\eta&=\frac1{84}\nu_\sigma^{\otimes4}
 \otimes(\omega^2\mathcal X-\mathcal Y),\\
P_*h&=-\frac{2+\omega}{168}\nu_\sigma^{\otimes4}
 \otimes(\mathcal X+\mathcal Y).
\end{aligned}}
\tag{8}
$$

**证明。** 在 Amice 对偶坐标 $(u,v)$ 中，(6) 将末两原 sigma 变成
$\sigma(u+v)\sigma(\omega(u-v))$。原 sigma 加法公式及 CM 型给
$$
\sigma(u+v)\sigma(u-v)
=\sigma(u)^2\sigma(v)^2\bigl(x(v)-x(u)\bigr),
\qquad \sigma(\omega z)=\omega\sigma(z).
\tag{9}
$$
乘 (4) 的 $-1/84$ 正得到第一式，包括其符号和 $\omega$。

对真实矩阵 (5) 直接乘行，得到
$$
UH=-U,\qquad VH=-\omega V.
\tag{10}
$$
由 (3)，(10) 在 $\mathcal X,\mathcal Y$ 上分别乘
$\omega^2,1$。再乘 (4) 的 $\omega^2$ 即第二式。
最后 $2\omega^2+\omega=-2-\omega$，两系数相加得到第三式。
这些是完整 Amice 幂级数恒等式；整有界 Amice 对应的单射性
将其提升为整个测度身份，故所有连续六变量测试同时成立。证毕。

两张量确实独立：它们的总质量皆零，但
$$
\int U^2\,d\mathcal X=0,\quad
\int V^2\,d\mathcal X=2\Omega^2,\qquad
\int U^2\,d\mathcal Y=2\Omega^2,\quad
\int V^2\,d\mathcal Y=0.
\tag{11}
$$
两原态的系数矩阵行列式为 $1-\omega$，
在当前系数环中是单位。第三式是完整对称张量，非两个边际的猜测。

原输入反射 $R_c:(c,d)\mapsto(-c,d)$ 准确给
$$
R_c:(U,V)\mapsto(-V,-U).
\tag{12}
$$
$\Theta,\Sigma$ 都偶，故 $R_{c,*}h=h$，
$R_{c,*}\rho_0=-\rho_0$，与 R544 的整个两态矩阵一致。

## 3. 完整 degree2 核心的绝对符号

**定理2。** 在同一个 (1) 规范中，
$$
\boxed{
\nu_\Theta|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_\Theta,\qquad
\nu_\Sigma|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_\Sigma.
}
\tag{13}
$$
因此 (8) 的整个六变量来源在 $U$ 和 $V$ 两方向分别都有标量核心
$\beta=-\lambda$；任意独立深度 $(n,m)$ 的真实矩形给
$$
\boxed{
(P_*\mu)|_{\{U\in p^n\mathbf Z_p,\ V\in p^m\mathbf Z_p\}}
=\beta^{n+m}[\,U\mapsto\kappa^nU,\ V\mapsto\kappa^mV\,]_*
(P_*\mu),
}
\tag{14}
$$
其中 $\mu=\rho_0,\eta,h$，前四坐标及其全部测试保持。

**证明。** R316 第3节已由同一 division trace 和真实正权锚确定
$\nu_\Theta$ 的完整核心。改用 $E_0$ 的 $\pi_0$ 及 (1) 的 $\kappa$ 后，
其标量准确为 $\bar\pi_0^{-1}=\beta$。
实际 $E_b$ 与 $E_0$ 的形式群同构是
$\Theta_b(z)=\Theta_0(b^{1/6}z)$、
$\Omega_{p,0}=b^{1/6}\Omega_p$，故此处并未任意缩放测度变量。

为支付整个 $S_2$ 而不只使用 $\Theta$ 一条线，
保 R300/R506 的完整标准 theta 群 lift。
当前原 ray 在模 $4$ 下有
$$
\pi_0\equiv3+2\omega,\qquad
\bar\pi_0\equiv1+2\omega,\qquad
g_\pi=\pi_0/\bar\pi_0\equiv-1\pmod4.
\tag{15}
$$
在标准二维 theta 表示的基 $e_j$（$j\in\mathbf Z/2$）上，
取 $Xe_j=e_{j+1}$、$Ze_j=(-1)^je_j$。
完整 canonical lift 可写
$T(s,r)=i^{-sr}Z^sX^r$。
(15) 在 lift 上送 $T(s,r)$ 到 $T(-s,-r)$，
而二阶时后者与前者相等。这里模 $4$ 保证中心相位亦相同，
不只是模 $2$ 标签相同。
故完整普通 trace 核心与 $X,Z$ 都交换。
二者生成完整二阶矩阵代数，核心必在整个 $S_2$ 上为同一个标量。
用已付的 $\Theta$ 锚定标即 $\beta$，得到 $\Sigma$ 的同一核心。
(8) 两张量的每个因子皆属这一整个 $S_2$；
两方向相互独立，迭代 (13) 得 (14)。证毕。

前四条 $\nu_\sigma$ 在同一 (1) 规范中也都有核心 $\beta$，
见 R316 的实际形式群同构。因此 (8) 现在有六个各自独立、
均已绝对定标的标量方向；这不等于原六个输入在 $H$ 后仍独立。

## 4. 真单位区间上的整对偶与完整连续逆

整原 Taylor 首项给
$$
\nu_\Theta(1)=1,\quad\nu_\Sigma(1)=0,\qquad
\int z^2d\nu_\Theta=0,\quad\int z^2d\nu_\Sigma=2\Omega^2.
\tag{16}
$$
结合 (13)，
$$
\boxed{
\begin{array}{c|cc}
&\nu_\Theta^\times&\nu_\Sigma^\times\\ \hline
1&1-\beta&0\\
z^2&0&2\Omega^2(1-\beta\kappa^2)
\end{array}}
\tag{17}
$$
全部分母均为单位。$1-\beta\kappa^2$ 显然是单位；
$1-\beta$ 的单位性保 R316 的真实 $E_0$ 参数：
$E_0$ 有有理二挠，Frobenius trace 为偶数；
Hasse 界在 $p>7$ 下把 $a_p\equiv1\bmod p$ 的唯一可能代表压到 $1$，
再由偶性排除它。因此 $\bar\pi_0\not\equiv1\bmod p$。

于是两个明确整连续测试
$$
e_0(z)=\frac{\mathbf1_{\mathbf Z_p^\times}(z)}{1-\beta},
\qquad
e_2(z)=
\frac{\mathbf1_{\mathbf Z_p^\times}(z)z^2}
 {2\Omega^2(1-\beta\kappa^2)}
\tag{18}
$$
在整个 $S_2$ 上是准确对偶基：
$$
\begin{pmatrix}
\nu_\Theta(e_0)&\nu_\Sigma(e_0)\\
\nu_\Theta(e_2)&\nu_\Sigma(e_2)
\end{pmatrix}=I_2.
\tag{19}
$$
例如在 (8) 中对 $V$ 用 $e_0$ 或 $e_2$ 积分，
$h$ 分别返回
$-(2+\omega)\nu_\sigma^{\otimes4}\otimes\nu_\Sigma/168$
和
$-(2+\omega)\nu_\sigma^{\otimes4}\otimes\nu_\Theta/168$。

这也是一个完整六输入单位见证。令
$$
e_1(z)=\frac{\mathbf1_{\mathbf Z_p^\times}(z)z}
 {\Omega(1-\beta\kappa)}.
$$
前四独立 sigma 各给 $\nu_\sigma(e_1)=1$，故
$$
\boxed{
(P_*h)(e_1^{\otimes4}\otimes e_2\otimes e_0)
=(P_*h)(e_1^{\otimes4}\otimes e_0\otimes e_2)
=-\frac{2+\omega}{168}\in\mathcal O^\times.
}
\tag{20}
$$
这个单位属于明确的原来源单位测试，不被称作原中央导数。

所有连续混合测试也有同一完整单位逆。
对 $Z=U$ 或 $V$，令 $S_Zf$ 表示只把该变量替为 $\kappa Z$，
$f_{Z,0}=f|_{Z=0}$，并定义
$$
\boxed{
\mathcal U_Zf
=\frac{f_{Z,0}}{1-\beta}
+\sum_{n\ge0}\beta^n
 \bigl(S_Z^nf-f_{Z,0}\bigr).
}
\tag{21}
$$
在全部其余变量组成的紧空间上一致连续，保证级数按测试范数一致收敛；
每项整且 $1-\beta$ 是单位，所以 $\|\mathcal U_Zf\|\le\|f\|$。
望远镜计算给
$$
(I-\beta S_Z)\mathcal U_Zf=f.
\tag{22}
$$
由 (13)–(14)，对每个 $\mu$ 有
$$
\boxed{
(P_*\mu)(f)
=(P_*\mu)|_{\{Z\ {\rm unit}\}}(\mathcal U_Zf)
=(P_*\mu)|_{\{U,V\ {\rm unit}\}}
(\mathcal U_U\mathcal U_V f).
}
\tag{23}
$$
两逆交换，因它们只缩放不同坐标。
(21) 的常数项不能省略；本篇不把质量一的 $\Theta$ 写成没有边界项的
环带无穷和。原混合 $Y,W$、所有指示函数和 $q_n$ 在 (21) 每一项内都随坐标变化。

## 5. 原观察量与 R544 唯一余域

为避免把新的整张量当成原观察分离，以下列出真实所有线性输出。
保 R539 的记号
$$
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x,\qquad
\gamma=3+\omega,\quad\bar\gamma=2-\omega.
\tag{24}
$$
原第一输出 $Y=A+c+2d$ 及第二输出 $W$ 准确为
$$
\boxed{
\begin{aligned}
Y&=A-\frac{\delta}{2}U+\frac{3+2\omega}{2}V,\\
W&=A+\frac{-1+2\omega}{2}U+\frac{7+10\omega}{2}V,\\
L=\frac{W-Y}{2}&=\omega U+\delta V,\\
M&=(1-\omega)U+\omega V.
\end{aligned}}
\tag{25}
$$
这里 $Y$ 的 $V$ 系数也等于 $-\omega^2\bar\gamma/2$。
原 $C$ 不含 $c,d$，原 $F$ 的末两输入部分是 $M$，
原 $G_{\rm hid}$ 的末两输入部分是 $(3-2\omega)M$；
所以原 $q_n$ 直接按 (25) 替换，其他部分逐字保持。
$U$ 或 $V$ 单独缩放一般改变 $Y,W,M$，不得只把 Mellin 因子提出。

R544 的三个真实第一轴现在是
$$
\boxed{
u_0=\frac{U+V}{2},\qquad
u_1=-\frac{U+\omega^2V}{2},\qquad
u_2=\frac{U+\omega V}{2}.
}
\tag{26}
$$
由
$$
(U+V)(U+\omega V)(U+\omega^2V)=U^3+V^3
\tag{27}
$$
及整数环中乘积为单位当且仅当每个因子为单位，得到

**定理3。** R544 的同一个唯一余域准确为
$$
\boxed{
P(\mathcal V)=
\{\,\omega U+\delta V\in\mathbf Z_p^\times,\ 
U^3+V^3\in\mathbf Z_p^\times\,\},
}
\tag{28}
$$
前四输入仍自由，测试保持 (25)。没有把它换成 $\{U,V\ {\rm unit}\}$。

特别，$U$ 深、$V$ 单位以及 $V$ 深、$U$ 单位两个真不交区域
都完整包含于 (28)。在 $U,V$ 皆单位部分，只保同时避开
(28) 两条零模 $p$ 条件的点。这给四条明确线
$$
U+V,\quad U+\omega V,\quad U+\omega^2V,\quad\omega U+\delta V
\tag{29}
$$
的实际有限剩余域。它不包含 $U,V$ 同时深的点。
各线的原输入 cut 和任何追加的 $\mathcal D_n$ 条件仍按 (6) 保持。

## 6. 原中央比较在新张量中的准确形式

保 R544 的同一个
$$
f=\mathbf1_{L\ {\rm unit}}\,
q_n\left(
\mathbf1_{Y\ {\rm unit}}\,d\log_pY
-\mathbf1_{W\ {\rm unit}}\,d\log_pW
\right),\qquad
\Phi_j=f\circ P_{u_j,\kappa}.
\tag{30}
$$
$d=p-1$ 在 (30) 中是 Mellin 微分因子，不是第六输入。
按 $h=\eta+\rho_0/2$，原两态项准确为
$$
\boxed{
\rho_0(\Phi_1-\Phi_0)+\eta(\Phi_1-\Phi_2)
=\rho_0\!\left(\frac{\Phi_1+\Phi_2}{2}-\Phi_0\right)
+h(\Phi_1-\Phi_2).
}
\tag{31}
$$
最后一项现在有完整来源表达
$$
\boxed{
h(\Phi_1-\Phi_2)=
-\frac{2+\omega}{168}
\int
\bigl((\Phi_1-\Phi_2)\circ P^{-1}\bigr)\,
d\!\left(\nu_\sigma^{\otimes4}
\otimes(\mathcal X+\mathcal Y)\right).
}
\tag{32}
$$
(25)–(26) 给出 (32) 中全部实际代入。
结合原两中央假设时 R544 的准确式，得到
$$
\boxed{
\rho_0|_{\mathcal V}(f)=
\lambda\left[
J-
\rho_0\!\left(\frac{\Phi_1+\Phi_2}{2}-\Phi_0\right)
-h(\Phi_1-\Phi_2)
\right].
}
\tag{33}
$$
$J$ 仍是原共同单位域上的完整对数比积分；未改成单独常数。
(8)、(23)、(25)、(28)、(32) 对其全部补域和测试都可直接使用。

(19) 允许对一个**独立**的 $V$ 测试作精确收缩；
它不允许在含 $Y(U,V)$、$W(U,V)$ 或 $q_n(M)$ 的测试中
直接把 $V$ 积掉并仍保原权不变。同样，(23) 的完整逆是合法的，
只取其中的未移动 $n=0$ 项则不是。
因此本篇的两个低度张量、整对偶和四线区域均已支付，
尚未支付的是 (33) 上这个实际混合行的非消失或完整消去。
不由 (20) 的单位见证、第一边际或部分区域非零关闭主目标。

## 依赖

- [R316：原低度核心及四因子 carry](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)，第3–5节；其中绝对 $\Theta$ 核心与完整质量项在此保留。
- R300 的完整 division trace 及 R506 的 canonical theta 中心规范；
  本篇第3节已在实际二阶表示中付清所需中心。
- [R541](R541-original-degree8-second-state-and-exact-sigma-transport.md)，原第三支和实际 $H$。
- [R544](R544-original-s3-and-exact-mixed-unit-complement.md)，全部三轴、原余域和中央式。
- [R546](R546-original-third-sigma-full-five-companion-cm-transfer.md)，完整六输入框架。
- [R551](R551-original-norm5-two-state-core-and-complete-unit-inverse.md)，连续测试逆的同一范数方法；本篇 (21)–(23) 已给标量情形完整证明。
