# R226 — 实际双倍下降、对称整参考与二挠运输的完整中央卷积

日期：2026-11-13。**状态：以下实际 theta 恒等式、同一原两权的整比较、完整中央运输公式和新的有限局部向量已证明。尚未证明原 $K$ 无穷次非零；二挠运输没有免费产生另一个固定秩零曲线的中央单位。**

本篇延续 [R222](R222-actual-theta-torsion-cocycle-and-integral-two-frame-completion.md)，
始终使用原 $A,B$、原 $c=68k_r$ 和原 degree-$p$ 参数 $Z$。
新的对称有限参考直接从原双倍恒等式构造，不把任意插值在另一端的值认成实际 theta。
完整 Mellin 运输保留乘子 $X/2$ 及全部余类；第一行先保留模 $p^2$，
确实可除 $p$ 后才定义 $K$。

## 1. 同一实际 theta 的双倍下降

保持 R207–R222 的记号，特别
$$
E_0:y^2=x_0^3-x_0,\quad
E_+:Y^2=X^3+4X,\quad
q=\frac1{X^2+4},\quad
\nu=-X/Y,\quad
\rho=\frac{1-s}{1+s}.
$$
为了不混淆曲线坐标，以下另记
$$
\xi=q(1-4q)=\nu^4,\qquad v=16\xi.
$$
原双倍公式给
$$
s(2z)=16q(1-4q)=v,\qquad
\Theta(z)=\vartheta(2z)^{17}.
$$
若 $L(s)=\log\vartheta(z(s))^{68}$，则有特征零准确形式恒等式
$$
\boxed{\quad
\mathcal L(q)=\log\Theta=\frac14L(16\xi),\qquad
F_+(q)=(1-4q)^{1/4}F(16\xi).
\quad}                                                     \tag{1}
$$
这里各根在原点取首项一。

证明：原曲线倍点公式为
$$
x_0(2z)=\frac{(x_0^2+1)^2}{4x_0(x_0^2-1)}.
$$
取倒数平方即得 $s(2z)=16\xi$。又
$2z=(16\xi)^{1/4}F(16\xi)$，而
$z=q^{1/4}F_+(q)$；首项确定四次根，证明第二式。
第一式就是同一 $\Theta=\vartheta(2z)^{17}$，没有换周期或换 theta 截面。

原第一列的有理因子准确下降为
$$
\boxed{\quad
a_0(q)=
\xi+\frac{48}{5}\xi^2-\frac{256}{5}\xi^3+\frac{4096}{5}\xi^4
=\frac1{16}P_4(16\xi),
\quad}                                                     \tag{2}
$$
其中 $P_4(t)=t+3t^2/5-t^3/5+t^4/5$。
所以 $a_0(1/4-q)=a_0(q)$，且这正是原 $A=A_{17}(2z)/16$ 的实际下降。

## 2. 原坏 primitive 的准确 Frobenius 完成

令 $p=4r-1>19$、$d=2r-1$。R211、R219 的两个原多项式满足
$$
h(s)+4sh'(s)=(1-s)^d,\qquad
g(q)+4qg'(q)=(1-4q)^{r-1}.
$$
置
$$
t(q)=q^rg(q),\qquad C=t(1/4)=-\frac1{2\kappa}.
$$
则同一原 $h$ 给出真正对称的有限完成：
$$
\boxed{\quad
\xi^rh(16\xi)
=(1-8q)^p\,t(q)+4Cq^p.
\quad}                                                     \tag{3}
$$
左边在 $q\mapsto1/4-q$ 下不变。右边的 $q^p$ 项不能省略；
它准确支付 R222 的非零反射常数。

证明：因为 $r=1/4$ 于 $\mathbf F_p$，
$$
\frac d{dq}\bigl(\xi^rh(16\xi)\bigr)
=\frac14\xi^{r-1}(1-8q)(1-16\xi)^d
=\frac14\xi^{r-1}(1-8q)^p.
$$
这也是 $(1-8q)^pt(q)$ 的导数。
两者次数至多 $6r-2<2p$，原点值均零，故差为 $Aq^p$。
代入 $q=1/4$，左边零、右边的第一项为 $-C$，
得到 $A=4C$。这证明全多项式恒等式。

在原点的 $q<p$ 窗口，(3) 与 $t(q)$ 相同；
但它在另一端为零，而 $t(1/4)=C$ 是单位。
这不是把特征零形式原函数宣称为全局有理函数。
(3) 是明确的特征 $p$ 多项式完成，且全部新增极点仍在
$q=\infty$ 的 $P_\pm$，即原 $Z=0$ 的点。

## 3. 一份真正双端对称的实际整参考

记
$$
\ell=[s^r]L,\qquad
\mu=\frac{16^r}{4}\ell.
$$
由 $16^r\equiv4\pmod p$，
$$
p\mu\bmod p=\alpha=68\kappa,\qquad
c-\mu\in O,\qquad O=\mathbf Z_p.                            \tag{4}
$$
第二个断言也可直接由 (1) 的第 $r$ 次项看出：
除 $\mu$ 外，该系数只读 $L$ 的低于 $r$ 次整系数；
再用 R222 的 $c-[q^r]\mathcal L\in O$。

用 R213 已付的实际整 log 定义
$$
Y(s)=
\exp\!\left(\frac14\bigl(L(s)-\ell s^rF(s)\bigr)\right)
       \pmod{s^{2r}},
$$
$$
\boxed{\quad
\Xi_{\rm sym}(q)=
\sum_{j=0}^{2r-1}[s^j]Y(s)\,16^j\xi^j\in O[q].
\quad}                                                     \tag{5}
$$
因此 $\deg_q\Xi_{\rm sym}\le p-1$，并且
$$
\Xi_{\rm sym}(q)=\Xi_{\rm sym}(1/4-q)
$$
是特征零准确多项式恒等式。

其在两个端点的有限 jet 都由原 $\Theta$ 得到。
在原点，
$$
\Xi_{\rm sym}
=\exp\!\left(\mathcal L(q)-\mu\,\xi^rF(16\xi)\right)
       \pmod{q^{2r}}.                                      \tag{6}
$$
另一端沿原双倍映射的 Mumford 运输使用同一 $\xi$，
所以得到同一个有限表达。整性只用 R213 的整 log 和次数小于 $p$ 的阶乘；
不使用 $\exp(\text{单位}/p)$，也不声称完整无限 theta 已由一个全局整函数平凡化。

准确比较原 $w=z^4$ 参数时，(1) 给
$$
\xi^rF(16\xi)
=q^rF_+(q)(1-4q)^{p/4}
=w^rF(16\xi)^{-p}.                                       \tag{7}
$$
这保留了原来的第一 Frobenius 修正。

对于任一固定的原正次有理因子 $R(q)\in qO[[q]]$，
令 $F=\Theta R$。定义
$$
R_1(F)=[w^r]F,\qquad
\widehat R_2(F)=[w^{2r}]e^{-cw^r}F,
$$
$$
D_{2,{\rm sym}}(F)=[w^{2r}]\Xi_{\rm sym}R,
\qquad
L_{\rm dual}(F)=
[w^r]\Xi_{\rm sym}R\log F(16\xi)\pmod p.
$$
右边 $F(16\xi)$ 表示原椭圆对数级数，不是截面 $F$；
这个标准重名在公式中仅此一处。

第一行准确不变；第二行的整比较为
$$
\boxed{\quad
\overline{D_{2,{\rm sym}}(F)}
=\overline{\widehat R_2(F)}
 +\overline{c-\mu}\,\overline{R_1(F)}
 +\alpha L_{\rm dual}(F).
\quad}                                                     \tag{8}
$$
证明：在所需窗口，
$$
F(16\xi)^{-p}=1-p\log F(16\xi)\pmod{p^2}.
$$
把 (7) 代入 (6)，和原 $e^{-cw^r}F$ 比较。
共同额外指数从 $w^r$ 开始，原因子从正次开始，
故第二权只读一次线性项；得到 (8)。所有待约化的第二行已由 (5) 整化。

若原第一行确实被 $p$ 整除，令 $u_F=\overline{R_1(F)/p}$，
则同一原后继坐标准确是
$$
\boxed{\quad
K_F=\overline{D_{2,{\rm sym}}(F)}
       -\alpha u_F-\alpha L_{\rm dual}(F).
\quad}                                                     \tag{9}
$$
本式没有用模 $p$ 的首行冒充 $u_F$。

若同时使用 R219 的原下降列 $B\rho^{-p}$，
其第一行仍须保留
$$
D_{1,{\rm sym}}\equiv R_1-p\eta\pmod{p^2},\qquad
\eta=(0,L_{\rho,B}).
$$
于是 (9) 对两原列写成
$$
K=\overline{D_{2,{\rm sym}}}
  -\alpha\left(\overline{D_{1,{\rm sym}}/p}
              +\eta+L_{\rm dual}\right).                  \tag{10}
$$
只有在聚合首行可除 $p$ 后使用这条式子。

## 4. 实际对称参考的全迹常数

使用 R219 的同一个 degree-$p$ 覆盖及其特征零提升 $\widehat Z$。
因为 (5) 在 $T'$ 正则，$a_0(T')=0$，
而原下降 $b$ 在 $T'$ 的极阶仍为 $2p-2$，
完整迹继续只有常数和负四倍幂。两条正中央全迹仍准确为零。

对称性让其常数项成为一个明确的实际低 jet。
记 $q^\tau=1/4-q$，则
$$
\boxed{\quad
C_{{\rm sym},B}
=\frac1C[q^{r-1}]
 \overline{E_p^{\rm low}(q)}\,b_0(q^\tau)(1-4q)^{r-1}.
\quad}                                                     \tag{11}
$$
这里 $E_p^{\rm low}$ 正是 R222 的实际低 log 指数，不是可自由选择的参考。

证明可直接用原 cocycle
$Z\circ\tau=Z-C\nu^{-p}$。
完整迹常数是
$$
-\operatorname{res}_{T'}
 \frac{\Xi_{\rm sym}\,b_0(q)(1-4q)^{-d}\omega}{Z}.
$$
运输回原点，用 $\Xi_{\rm sym}\circ\tau=\Xi_{\rm sym}$，
以及
$$
\frac1{Z\circ\tau}
=-\frac{\nu^p}{C}\frac1{1-q^rg/C},
$$
得到 (11)。具体地，$\omega=\tfrac14q^{-3/4}(1-4q)^{-3/4}dq$；
$q$ 在原点的分歧指数四抵消前面的 $1/4$，
$(4q)^{-d}\nu^p\omega$ 的 $q$ 指数是 $-r$。
$4^{-d}=1$ 于 $\mathbf F_p$，而 $q^rg$ 从 $q^r$ 开始，
故最后的几何级数不影响 $[q^{r-1}]$。这个系数也不见 gauge 的第 $r$ 次项，
所以 $\Xi_{\rm sym}$ 可换成同一实际 $E_p^{\rm low}$。

本式没有把 (11) 认成裸单位 $\kappa2261/81920$。
对原点和非原点聚合仍有 $N_j=-D_j$，
所以 (10) 等价于
$$
K=-\overline{N_2-\mu N_1}
  -\alpha(\eta+L_{\rm dual}).                              \tag{12}
$$
原反射也不配对消去这些非原点项：一般 $Z(P)=0$ 时
$Z(\tau P)=-C\nu(P)^{-p}\ne0$，所以 $\tau$ 不保原 $Z=0$ 纤维。
(11) 是一个新的实际常数泛函，(12) 才是原目标所需的聚合。

## 5. 原第二列的准确运输与一个固定挠点截面

在 $E_0$ 取 $R=(1,0)$。其像是 $E_+$ 的 $T'$；
$\tau_R$ 的坐标公式给
$$
q\circ\tau_R=1/4-q,\quad
\rho\circ\tau_R=\phi,\quad
\phi=2\sqrt q=\frac{2x_0}{x_0^2+1},\quad
\frac{\rho}{\phi}=\frac X2.
$$
因为 $\Theta=[2]^*\vartheta^{17}$，
使用双倍映射的实际 Mumford 线性化时 $\mathcal T_R\Theta=\Theta$。
于是原两列的运输准确为
$$
\boxed{\quad
\mathcal T_R A=A,\qquad
\mathcal T_R B=\Theta\phi\,b_0(1/4-q).
\quad}                                                     \tag{13}
$$
这保留全部 theta 自动因子，不能改成未正规化的普通函数平移。

原多项式 $b_0$ 的偶部和奇部精确为
$$
\frac{b_0(q)+b_0(q^\tau)}2
=\frac{8192\xi^3-256\xi^2+64\xi-1}{40},
$$
$$
\frac{b_0(q)-b_0(q^\tau)}2
=-\frac{(8q-1)(1-16\xi)^2(1+16\xi)}{40}.                    \tag{14}
$$
所以
$$
b_0(q^\tau)-b_0(q)=\frac{(8q-1)^5(1+16\xi)}{20}.
$$
令
$$
S=\vartheta(z)^{68}(1-s)(1+s)^2
       (s^2-6s+1)^5 H_2(s),\qquad S(0)=1.
$$
从 $8q-1=-(s^2-6s+1)/(1+s)^2$ 和
$1+16\xi=H_2(s)/(1+s)^4$ 立即得到完整截面恒等式
$$
\boxed{\quad
B^\sharp:=\frac X2\,\mathcal T_RB=B-\frac1{20}S.
\quad}                                                     \tag{15}
$$
此处 $X/2$ 在原点有二阶极点；
$\mathcal T_RB=-z^2/10+\cdots$ 正好支付它，
而 $B^\sharp(0)=-1/20$。这个质量不能省略。

$S$ 的全部零点都在 $E_0[8]$。
还可用两个正规二挠 theta $\vartheta_\pm$ 写出
$$
\boxed{\quad
S=
[\vartheta_+(z)\vartheta_-(z)]^2\,\vartheta(2z)^2\,
[\vartheta_+(2z)\vartheta_-(2z)]^5\,\vartheta(4z).
\quad}                                                     \tag{16}
$$
证明：取首项一的平方根，有
$\vartheta_+\vartheta_-=\vartheta^2\sqrt{1-s}$，
$\sqrt{1-s(2z)}=(s^2-6s+1)/(1+s)^2$，
$\vartheta(4z)=\vartheta(z)^{16}H_2(s)$。
代入即得 (16)，也证明挠点范围。
只有挠点除子并不自动把它识别成已知秩零的 Mellin 行。

## 6. 完整中央泛函的真实运输：所有余类都保留

固定 $w=z^4$、$v=w^r$，使用原共同规范
$$
\mathcal J_p(F;u)
=\sum_{h\ge0}[w^{rh}](e^{-cv}F)\,
       c^{-h}(u)_h,\qquad
(u)_h=u(u-1)\cdots(u-h+1).                                  \tag{17}
$$
这是 R54、R185 的同一完整轴；它对实际固定 theta 截面线性，
并保留原尾界。对 $\Theta,S$ 等非零质量截面，其常数为 $F(0)$。
本篇只对相同次数六十八的固定截面使用这一定义；
它们都是 $\vartheta^{68}$ 乘固定 $O[s]$ 多项式，已有 gauge 及尾界证明逐项适用。

由 (13)，$\mathcal T_RB$ 只含 $z^{4n+2}$；
所以其原 $\mu_4=1$ 中央投影恒为零。这与原 $B$ 的完整中央失败无关，
也不支付 (15) 中乘 $X/2$ 后的中央值。

为给出乘后的完整公式，置
$$
H(w)=z^2X(z),\qquad C_B(w)=z^{-2}\mathcal T_RB(z).
$$
它们都是实际形式级数，$H(0)=1$、$C_B(0)=-1/10$。
按同一原余类分解
$$
H(w)=\sum_{l=0}^{r-1}w^lH_l(v),\qquad
e^{-cv}C_B(w)=\sum_{l=0}^{r-1}w^lC_l(v).
$$
则 (15) 的完整 gauged 中央部分准确是
$$
\boxed{\quad
\bigl(e^{-cv}B^\sharp\bigr)_{\rm central}
=\frac12\left(
H_0(v)C_0(v)+v\sum_{l=1}^{r-1}H_l(v)C_{r-l}(v)
\right).
\quad}                                                     \tag{18}
$$
对右边的第 $h$ 系数乘 $c^{-h}(u)_h$ 并求和，就是
$\mathcal J_p(B^\sharp;u)$。每个系数只作有限卷积；
整体收敛由 (15) 的实际截面及已有尾界保证。
没有另行假设各因子有独立单位测度。

这正是原二挠运输的完整中央协变式。它读取相邻字符中全部 $r$ 个余类，
所以不能从 $\mathcal T_RB$ 的恒零中央轴直接得到 (18) 为零。

为回到质量零的原型，定义实际截面
$$
D=S-\Theta,\qquad
U=B^\sharp+\frac{\Theta}{20}
  =B-\frac D{20}.
$$
于是
$$
\boxed{\quad
\mathcal J_p(U;u)=\mathcal J_p(B;u)-\frac1{20}
       \bigl(\mathcal J_p(S;u)-\mathcal J_p(\Theta;u)\bigr).
\quad}                                                     \tag{19}
$$
特别其中央导数也满足这个完整等式。
原 $B$ 中央导数为零，尚不意味着 $U$ 的中央导数为零；
这个剩余项就是 (18) 中的实际相邻字符卷积，而不是省略的常数。

## 7. 质量、第一行 p² 和 K 同时运输

$D$、$U$ 的原 $q$ 因子分别为
$$
R_D=-20\rho\bigl(b_0(q^\tau)-b_0(q)\bigr)-1,\qquad
R_U=\rho b_0(q^\tau)+1/20.
$$
两者常数均为零。因此 R213/R222 以及本篇 (8)–(10)
适用于它们与原 $A,B$ 的同一整化，不另选原点或参考。

特征零准确有
$$
R_1(U)=R_1(B)-R_1(D)/20,\qquad
\widehat R_2(U)=\widehat R_2(B)-\widehat R_2(D)/20.           \tag{20}
$$
第一式必须保留模 $p^2$。$R_1(S)$ 和 $R_1(\Theta)$ 各自可能有同一负 $p$ 层；
必须先形成实际 $D=S-\Theta$，不能分别当成整行约化。

若 $R_1(B)\in pO$，则
$$
R_1(U)\in pO\quad\Longleftrightarrow\quad R_1(D)\in pO.
$$
在这个条件满足后才有
$$
\boxed{\quad K_U=K_B-K_D/20.\quad}                           \tag{21}
$$
所以 (19) 若要成为新的中央约束，
仍须实际控制 $U$ 的完整行或 (18) 的卷积；
单独运输 $B$ 的消失并未完成这一步。

这里只说明原正次源的真实比较。
$S$ 的常数项一还表明它不是原两列的线性组合；
不能将 (15) 新增的固定方向预先作为原 $A,B$ 的另一个已知中央零行。

## 8. 实际有限 dyadic 向量：同一 E34 的另一组权

这一部分识别真正的 $\mathcal T_RB$，尚不把乘 $X/2$ 后的 $U,D$
认成另外一条曲线的完整行。

沿用 R112、R115 的实际高斯生成式，$L=34$、
$\beta=4-i$，
$$
a_n^+=\varepsilon_n\lambda(n)^2\zeta_{289}^{77n^2},
\quad
(\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3)=(1,1,-1,1),
$$
以及相同的 $h_0$ 和首项归一。
则真正的 Mumford 运输准确把它变成
$$
\boxed{\quad
a_n^-=(-1)^n a_n^+,\qquad
\phi_2^-=\frac{e_0-e_1-e_2-e_3}{\sqrt2}.
\quad}                                                     \tag{22}
$$
特别，十七处的原 tame 角色 $\lambda^2$ 完全没有改变。

证明：在 Hermite 变量 $t=h_0z$ 中，$R=\Omega_0/2$ 对应
$\delta=\sqrt{\pi/2}(4+i)$。
将高斯和中的下标移 $136=34\cdot4$，得到
$$
B_+(t+\delta)
=e^{2\bar\delta t+|\delta|^2}B_-(t),
$$
新系数是
$a_{n+136}^+e^{2\pi i n/34}$。
因为 $136\equiv0\pmod{17}$、$136\equiv0\pmod4$、
$136^2=64\cdot289$，交叉相位和最后的指数合成
$$
\zeta_{289}^{136n}e^{2\pi i n/34}=(-1)^n.
$$
而
$2\bar\delta h_0z+|\delta|^2=34\pi z/\Omega_0+17\pi/2$，
正是 $\Theta(z+R)/\Theta(z)$ 的实际自动因子。
Mumford 运输准确消去这个因子，证明 (22)，没有遗留未知归一常数。

在 R112 的原 E34 splitting 矩阵 $I,-G_0$ 上，
$$
I\phi_2^-=-\phi_2^-,\qquad -G_0\phi_2^-=\phi_2^-.
$$
现在保留同一 E34 的完整 Hecke 参数
$$
\chi_m=\psi_{34}^{2m+1}N^{-m-1/2}.
$$
R46 所核统一化元公式给
$\chi_m(1+i)/\chi_0(1+i)=i^{-m}$。
所以当 $m\equiv2\pmod4$ 时，二处多出的是 $K_2$ 的未分歧二次字符，
在统一化元 $1+i$ 上取 $-1$，在单位上平凡。
其 splitting 修正对 $i$、$g_*=(-3+4i)/5$ 分别为 $-1,+1$：
这里 $v_{1+i}(i-1)=1$，$v_{1+i}(g_*-1)=4$。
新的两个矩阵是 $-I,-G_0$，恰固定 $\phi_2^-$。

十七处单位角色、其 Fourier 向量及范数均不变；
其他有限处仍使用相同的未分歧向量。
无穷处相应 Hermite 阶是 $m\equiv2\pmod4$。
因此 Yang 的同一局部—全局平方公式把 (22) 识别为
**同一 E34 的 $m\equiv2\pmod4$ 权值行**，
对应 $L_f(\psi_{34}^{2m+1},m+1)$，不是新固定秩零曲线。
有限导子和各向量范数不变；这里不借此省略在中心比较所需的 Euler 因子。

对目标惰性 $p$，原中央权为 $m=(p+1)h$，恒为四的倍数。
(22) 的非零权属于另一个剩余字符。
把该行接回原中央支仍必须支付 (18) 的乘法卷积、
实际单位边界与质量校正。单凭已知非中心临界值或权值平移，
不能推出原中央导数非零。

这一识别使用 Yang，*Theta liftings and Hecke L-functions*，
J. reine angew. Math. 485 (1997)，Theorem 2.6、式 (2.19)、
Theorem 2.15，以及 R46/R112 已核的 splitting 规范；
[作者原文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)
本轮重新核对。未上传或逐页渲染 PDF。

## 9. 原 p43 校准与继续的实际问题

只复用已有 $p=43$，不增加素数扫描。
[准确脚本](../scripts/check-original-double-descent-and-torsion-transport.py)
已执行通过；它还核对 (3) 的整条多项式、(14) 及两个有限 dyadic 矩阵。
[输出](../scripts/check-original-double-descent-and-torsion-transport.json)
保留了本节的全部原系数。
准确有
$$
\alpha=19,\quad c-\mu=9,\quad [q^r]\mathcal L-\mu=20\pmod{43}.
$$
按 $(A,B,D,U)$ 次序，实际行分别为
$$
R_1\bmod43^2=(899,1683,930,712),
$$
$$
\widehat R_2\bmod43=(22,2,42,30),
$$
$$
D_{2,{\rm sym}}\bmod43=(20,26,15,36),\qquad
L_{\rm dual}=(38,12,22,41).
$$
(8)、(20) 全部准确相容。
原行列式一列 $B-20A$ 仍有 $u=8$，由 (9)
$$
K=(26-20\cdot20)-19\cdot8-19(12-20\cdot38)=12\pmod{43}.
$$
实际对称参考的 (11) 给 $C_{{\rm sym},B}=24$；
它不同于原裸常数 $21$，也不同于 R219 那份有限参考的常数 $8$。
这三个常数的差没有改变原 $K$。

本篇支付了原双倍下降、真实对称有限参考、二挠完整运输、
相邻字符卷积和首行下一位。仍待证明的是：
(18) 是否有保原 theta 连接的二阶协变微分或完整算术比较，
从而控制实际 $U$、$D$ 的中央行；或直接证明 (9)/(12) 的原向量非零。
不能把普通二阶导数的矩移位当成省略连接项后的协变恒等式。
