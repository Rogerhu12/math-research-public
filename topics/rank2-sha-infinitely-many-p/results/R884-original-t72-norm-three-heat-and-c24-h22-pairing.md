# R884 — 原 T72 的范数三热返回与同一 C24/H22 低配对

日期：2026-11-16。**状态：以下完整来源身份与指定读数等式已证明。** 全文只使用原四来源中的 $T_{72}$、原共同 $C_{24}$、R863 的实际 $H_{22}$ 伴随以及同一个原参考行。没有数学数值执行或目标素数扫描。本文不从 $\mathfrak B(T)=0$ 推出其热伴随或 trace 的读数为零，也不把原参考来源的秩零解释成中央导数零。

## 1. 原六 sigma 来源的准确范数三分解

保持原
$$
y^2=x^3+b,\quad D_zx=2y,\quad X=x^3,\quad
\delta=1+2\omega,\quad\delta^2=-3,\quad\gamma=3+\omega,
$$
以及 R398 的绝对来源
$$
T=-\frac{\sigma(\delta z)\sigma(2\delta z)\sigma(3\delta z)
                \sigma(4z)\sigma(\gamma z)\sigma(\bar\gamma z)}
              {504\delta}.
\tag{1}
$$
所有 sigma 都在同一个原 $b$ 模型上；$b$ 是原固定单位。记
$$
Q_7=7X^2-4bX+16b^2,\qquad A_2=X^2+20bX-8b^2,
$$
$$
K_{30}=\frac{\sigma(4z)\sigma(\gamma z)\sigma(\bar\gamma z)}{28}
       =-\frac{\sigma^{30}yQ_7A_2}{7},\qquad
A_{14}=\sigma^{14}xy(X+4b).
\tag{2}
$$
由原 $\sigma(4z)=-4yA_2\sigma^{16}$、
$\sigma_\gamma\sigma_{\bar\gamma}=\sigma^{14}Q_7$ 和
$\sigma(z)\sigma(2z)\sigma(3z)=-6A_{14}$，准确有
$$
\boxed{T=\frac1{3\delta}K_{30}[\delta]^*A_{14}.}
\tag{3}
$$
这里 $K_{30}=z^3+O(z^9)$、$A_{14}=-z^3+O(z^9)$，而
$\delta^3=-3\delta$，所以(3)的首项确为 $z^6$。
两因子的 degree 为 $30$ 和 $3\cdot14=42$。

原 canonical trace 始终取 R877 的同一规范
$$
\mathrm T_{\delta,m}(\sigma^{3m}R)
=\sigma^m\operatorname{Tr}\frac{R}{(\delta x)^m}.
\tag{4}
$$
目标坐标记为
$$
a=x(\delta z)=-\frac{x^3+4b}{3x^2},\qquad
c=y(\delta z)=-\frac{y(X-8b)}{3\delta X},\qquad c^2=a^3+b .
\tag{5}
$$
因此完整三个源 $x$ 坐标满足
$$
P_0(x)=x^3+3ax^2+4b=0.
\tag{6}
$$
式(4)保全部三个纤维和原 sigma 比，未作另一个平移相位归一化。

## 2. 完整三纤维计算：原 T 的 trace 确实为零

令以下固定有理函数只依赖原源坐标：
$$
C(x)=\frac{x^{-7}Q_7(x^3)A_2(x^3)}{x^3-8b}.
\tag{7}
$$
直接部分分式分解得
$$
\boxed{
C=7x^2+\frac{39b}{4x}-\frac{42b^2}{x^4}
+\frac{16b^3}{x^7}
+\frac{729b}{4}\frac{x^2}{x^3-8b}.
}
\tag{8}
$$
在(6)的完整代数中，Newton 公式给
$$
\operatorname{Tr}x^2=9a^2,\quad
\operatorname{Tr}x^{-1}=0,\quad
\operatorname{Tr}x^{-4}=\frac{9a^2}{8b^2},\quad
\operatorname{Tr}x^{-7}=-\frac{63a^2}{64b^3},
$$
$$
\operatorname{Tr}\frac{x^2}{x^3-8b}=0 .
\tag{9}
$$
最后一式也可直接在 $r^3=8b$ 的三个不同根上作部分分式：
$$
\operatorname{Tr}\frac{x^2}{x^3-8b}
=-\frac13\sum_{r^3=8b}\frac{P_0'(r)}{P_0(r)}
=-\frac23\sum_{r^3=8b}\frac1r=0.
$$
这些计算在 $a^3+b\ne0$ 的开集上形成，所得有理恒等式随后全局延拓。

于是
$$
\operatorname{Tr}C=63a^2-\frac{189a^2}{4}-\frac{63a^2}{4}=0.
\tag{10}
$$
另一方面由(2)、(5)，准确有
$$
\frac{-yQ_7A_2/7}{(\delta x)^{10}}
=\frac{3\delta^{-9}}7\,c\,C(x).
$$
因此不是仅凭环境型的猜测，而是由(10)得
$$
\boxed{\mathrm T_{\delta,10}K_{30}=0,\qquad
       \mathrm T_{\delta,24}T=0.}
\tag{11}
$$
第二式使用同一 canonical trace 的投影公式及(3)。
它未把 $K_{30}$ 或 $A_{14}$ 另赋算术中央零。

## 3. 原第一次热连接的完整 degree24 像

对原 $T=\sigma^{72}R_T(x,b)$ 使用 R855/R879 的完整热连接
$$
\mathcal H_M=\mathcal L-\frac{M-1}{2}x-\frac{D_z^2}{2M},
\qquad
\mathcal Lx=2x^2-\frac{g_2}{3},\quad
\mathcal Ly=3xy,\quad b=-g_3/4.
\tag{12}
$$
先在双参数中应用(12)，最后才令 $g_2=0$。原多项式按 $b$ 延拓，
没有另加 $g_2$ 项。记 $T^{[1]}=\sigma^{72}\mathcal H_{72}R_T|_{\rm CM}$。

置 $r_T=R_T/(\delta x)^{24}$。由(3)、(5)、(7)，
$$
r_T=\frac{\delta^{-10}}7 Q(a(x))C(x),\qquad
Q(a)=a(a^3+b)(a^3+4b).
\tag{13}
$$
这里 $a(x)=-(x^3+4b)/(3x^2)$ 是原有理函数。
R879(5)–(10)的实际共轭计算对本 $r_T(x,b)$ 逐字成立：
$$
\mathrm T_{\delta,24}T^{[1]}
=\sigma^{24}\operatorname{Tr}(\mathscr J r_T),\qquad
\mathscr J=\mathcal L-\frac23\frac yxD_z,
$$
$$
\operatorname{Tr}(\mathscr J r_T)
=12b\,\left.\partial_\rho\operatorname{Tr}_{P_\rho}r_T\right|_{\rho=0},
\qquad P_\rho=x^3+3ax^2+\rho x+4b .
\tag{14}
$$
已经消去的两项分别是完整 $\operatorname{Tr}r_T$ 及其目标导数，
由(11)为零；没有删除 $\mathscr J$ 的横向缺陷。
在 $P_\rho$ 中 $a(x)=a+\rho/(3x)$，所以
$$
\left.\partial_\rho\operatorname{Tr}r_T\right|_0
=\frac{\delta^{-10}}7
\left(Q(a)\left.\partial_\rho\operatorname{Tr}C\right|_0
+\frac{Q'(a)}3\operatorname{Tr}\frac Cx\right).
\tag{15}
$$

以下列出(15)的全部实际输入，方便逐项复核。
令逆根满足 $u^3+\rho u^2/(4b)+3au/(4b)+1/(4b)=0$；
Newton 递推给
$$
\begin{array}{c|c}
F(x)&\left.\partial_\rho\operatorname{Tr}F\right|_0\\ \hline
x^2&-2\\
x^{-1}&-1/(4b)\\
x^{-4}&1/(4b^2)\\
x^{-7}&189a^3/(256b^4)-7/(64b^3)\\
x^2/(x^3-8b)&1/(12(a^3+b)).
\end{array}
\tag{16}
$$
最后一项直接对
$-\frac13\sum_{r^3=8b}P_\rho'(r)/P_\rho(r)$ 求导；
在 $\rho=0$ 每个商的导数为 $-1/(3(ar^2+4b))$，
而三个倒数之和为 $3/(4(a^3+b))$。

同一递推还给
$$
\operatorname{Tr}x=-3a,\quad
\operatorname{Tr}x^{-2}=-\frac{3a}{2b},\quad
\operatorname{Tr}x^{-5}=\frac{15a}{16b^2},
$$
$$
\operatorname{Tr}x^{-8}=\frac{81a^4}{128b^4}-\frac{3a}{8b^3},
\qquad
\operatorname{Tr}\frac{x}{x^3-8b}=0.
$$
将这些值代入(8)，得到
$$
\boxed{
\operatorname{Tr}\frac Cx=\frac{81a(a^3-8b)}{8b},\qquad
\left.\partial_\rho\operatorname{Tr}C\right|_0
=\frac{27(7a^6-10ba^3-8b^2)}{16b(a^3+b)}.
}
\tag{17}
$$
(15)中 $Q$ 的因子 $a^3+b$ 准确消掉显示的分母；
未留下一个被忽略的二挠极。

由 $Q'=7a^6+20ba^3+4b^2$、$\delta^{10}=-243$，
(14)–(17)化为完整来源
$$
\boxed{
G_{24}:=\mathrm T_{\delta,24}T^{[1]}
=-\frac{\sigma^{24}x}{28}
  (7X^3-18bX^2-120b^2X-32b^3).
}
\tag{18}
$$
这里已经回到目标原坐标 $(x,y)$。
它是 whole degree24 型四来源，首项 $-z^4/4$。
本节是原 $T$ 的同一热缺陷，未把 trace 与热方向交换。

## 4. 在原三列上的准确连接与高端相消

固定共同 C24 注的原整基
$$
E_j=-b^j\sigma^{24}x^{8-3j}y,\quad j=0,1,2,\qquad
C_{24}=E_0-\frac47E_1+\frac{16}{7}E_2.
\tag{19}
$$
令 $F_{24}=\Theta^{12}$，并保持其真实连接
$$
q_{24}=F_{24}'/F_{24}=24(\zeta+y/x),\qquad
\nabla_{24}=\partial_z-q_{24}.
$$
直接求导给
$$
\boxed{
\nabla_{24}E_j
=b^j\sigma^{24}x^{7-3j}
  \big((5+6j)X+(8+6j)b\big).
}
\tag{20}
$$
最低 $x$ 幂为一，所以这里连接的所有有限极确已消去。

逐坐标比较(18)、(20)，得到
$$
G_{24}
=\nabla_{24}\left(-\frac1{20}E_0+
                  \frac{73}{770}E_1+\frac{67}{385}E_2\right)
 -\frac{180}{77}b^3\Xi_{24},
\qquad \Xi_{24}=\sigma^{24}x .
\tag{21}
$$
特别定义以下同一来源的确定组合：
$$
\boxed{
\begin{aligned}
\overline E&=\frac{51E_1+222E_2}{770},\\
\widehat G_{24}&=G_{24}+\frac1{20}\nabla_{24}C_{24}
=\frac{3b}{70}\sigma^{24}x(17X^2+136bX+80b^2).
\end{aligned}}
\tag{22}
$$
则完整式为
$$
\boxed{
\widehat G_{24}
=\nabla_{24}\overline E-\frac{180}{77}b^3\Xi_{24}.
}
\tag{23}
$$
$\overline E$ 首阶十一，$\widehat G_{24}$ 首阶十，
$\Xi_{24}$ 首阶二十二。因而此处已消掉原 $E_0$ 的首五阶高端，
不是在取商后无证丢掉它。式(22)的左边仍是原 $T$ 的热 trace
加原共同 $C_{24}$ 的确定连接项。

## 5. 指定 D5 的完整低配对

以下固定原 $p=6s-1>211$、原整模型及坏集。
$\mathcal D_{m,p,k}$ 取 R856 的固定特征零 $H_p,C_p=L_2H_p$ 提升；
不能在除 $p$ 前改换其提升。所有下式是在原 CM 纤维的模 $p$ 等式。

记
$$
O_p(\overline E)=j_p(\overline E)/p,\qquad
\mathcal S_p=
\sum_{\substack{11\le r\le p-6\\r\equiv5\pmod6}}
\frac{j_r(q_{24})\,j_{p+5-r}(\overline E)}
     {r(r-1)(r-2)(r-3)(r-4)(r-5)}.
\tag{24}
$$
$q_{24}=-48bz^5/5+\cdots$，故 $j_5(q_{24})=-1152b$。
在 $j_{p+5}(q_{24}\overline E)/p$ 中，
$r=p$ 的高端由 $j_5(\overline E)=0$ 消失；
$r=5$ 的高端恰是 $-1152b\,O_p(\overline E)$。
其余项全部为(24)，因为
$$
\frac1p\binom{p+5}{r}\equiv-\frac{120}{(r)_6}
\quad(5<r<p,\ r\equiv5\pmod6).
$$
所以(23)给
$$
\boxed{
\mathcal D_{24,p,5}(\widehat G_{24})
=\mathcal D_{24,p,6}(\overline E)
+1152b\,O_p(\overline E)+120\mathcal S_p
-\frac{180}{77}b^3\mathcal D_{24,p,5}(\Xi_{24}).
}
\tag{25}
$$
没有对非 whole 的 $q_{24}\overline E$ 套用 R856；
其商的整性与完整式直接由上述端项和低卷积证明。

这里的全部来源可以严格用低于 $p$ 的物理 jets 读取。
具体写 $F_2=\sigma^2,\ B_4=\sigma(2z)/2,\ \Theta=x\sigma^2$，
则
$$
E_1=b B_4F_2^5\Theta^5,\qquad
E_2=b^2B_4F_2^8\Theta^2,\qquad
\Xi_{24}=F_2^{11}\Theta .
\tag{26}
$$
读取 $j_p(\overline E)$、$j_{p+6}(\overline E)$ 或
$j_{p+5}(\Xi_{24})$ 时，每个非零多重 Leibniz 项的单因子
jet 阶都小于 $p$：在最小零阶的第一项中，
即使将一个因子分配最大阶，其余因子仍至少留九阶。
全部总阶介于 $p$ 与 $2p$ 之间，故多项式系数在除 $p$ 后整。
在本三个 $\mathcal D$ 行，低 Hasse 修正分别被
$j_5(\overline E)=j_4(\Xi_{24})=j_4(\widehat G_{24})=0$ 消去。
这支付了(25)的实际严格低窗口；没有替换原 sigma 的 Frobenius 初值。

## 6. 同一原 H22 两配对与算术参考逐项回入

保持原 $J_S=-\sigma^{10}y(X-8b)$，以及
$Z_j=E_jJ_S$、$D_{\rm ref}=-(H_3-H_5)/(96b)$。
R863(A3)、(A6) 的实际三列比较准确给
$$
\boxed{
\overline E J_S
=-\frac{17}{1584}S+\frac{17}{7920}D_{\rm ref}
+\frac9{28}Z_2.
}
\tag{27}
$$
没有把 $\overline E$ 换成三维空间中的一个任意输入。

定义同原 C24 注(15)的低配对
$$
\mathcal P_p(\overline E,J_S)=
\sum_{r=1}^{s-1}
\frac{j_{p-6r}(\overline E)j_{6r+1}(J_S)}
     {6r(6r+1)}.
\tag{28}
$$
则完整高端比较为
$$
O_p(\overline E)=\mathfrak B(\overline E J_S)
+\mathcal P_p(\overline E,J_S).
\tag{29}
$$

现在仍取 R863(A17)–(A22) 的同一
$$
C_0=-\frac{\sigma(2z)^3H_{22}}{21312},\qquad
H_{22}=\sigma^{22}X(65X^2-380bX+464b^2).
$$
其两个完整低配对定义为
$$
\begin{aligned}
\mathcal L_p(C_0)
={}&-\frac1{10656}
\sum_{\substack{3\le r\le p-2\\r\equiv3\ (6)}}
\frac{j_r(\sigma_2^3)j_{p+2-r}(H_{22})}{r(r-1)(r-2)}\\
&+\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
\frac{j_r(q_{34})j_{p+1-r}(C_0)}{r(r-1)},
\qquad q_{34}=34(\zeta+y/x).
\end{aligned}
\tag{30}
$$
全部 $\sigma_2$、$q_{34}$ 和原 CM frame 保留。
已付准确身份是
$$
\mathfrak B(Z_2)=\frac{455}{2664}\mathfrak B(S)+\mathcal L_p(C_0).
\tag{31}
$$

将(27)–(31)代入(25)，得到本注的同源交接式
$$
\boxed{
\begin{aligned}
\mathcal D_{24,p,5}(\widehat G_{24})
={}&\frac{20708}{407}b\,\mathfrak B(S)
+\frac{136}{55}b\,\mathfrak B(D_{\rm ref})
+\frac{2592}{7}b\,\mathcal L_p(C_0)
+\mathcal R_{T,p},
\\
\mathcal R_{T,p}
={}&\mathcal D_{24,p,6}(\overline E)
+1152b\,\mathcal P_p(\overline E,J_S)
+120\mathcal S_p
-\frac{180}{77}b^3\mathcal D_{24,p,5}(\Xi_{24}).
\end{aligned}}
\tag{32}
$$
所有显示分母在原 $p>211$ 与固定坏集范围内为单位；
$\mathcal R_{T,p}$ 的每一项由(24)、(26)、(28)在严格低于 $p$
的原物理输入上读取。没有新的 $\Theta^{12}$ 首对数商，
也没有将余配对设为零。

若采用原首必要条件 $\mathfrak B(S)=0$，可以在(32)中删除第一项。
另两个逻辑边界仍须保留：

- $\mathfrak B(D_{\rm ref})$ 是 R863(A16) 的完整两条质量一参考行之差，
  后两曲线的秩零不使它为零。
- 原 $\mathfrak B(T)=0$ 没有把(32)左边的热 trace／连接组合赋零。
  R879 已付的横向 trace 缺陷在这里具体表现为(18)。

因此(32)把原 $T_{72}$ 的实际 new/heat 接口送回了同一 C24 三列、
同一 H22 两配对及一个完全确定的低窗口余项。
它尚未证明原四个 $\mathfrak B$ 不能同时为零；后续必须在(32)
这同一左边与全部右边上取得额外的已识别关系，不能只用其单位系数。

## 依赖

- [R398 原 T72 六 sigma 与绝对规范](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)。
- [原 C24 三列与完整三差矩阵](../notes/2026-11-16-original-common-odd-degree24-and-three-row-pairing.md)。
- [R855 全热连接](R855-original-full-heat-connection-and-canonical-divided-jet.md)、
  [R856 原 whole Hurwitz 与固定除 p 行](R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)。
- [R863 原连接伴随及 H22 两低配对](R863-original-balanced-frobenius-factor-and-partner-chain.md)。
- [R877 原 canonical 范数三 trace](R877-original-norm-three-common-source-and-h22-partner.md)。
- [R879 实际热共轭与全部原 trace 缺陷](R879-original-v66-heat-and-degree22-trace-defect.md)。


## 附录 A. 原 V/T 两中央的同 degree68 搬运与真实带权 H22 行

本附录给原 $\mathfrak B(V)-\mathfrak B(T)$ 的完整同源搬运，而不把
§6 的热读者设为零。以下固定 $p=6s-1>211$ 和原坏集；
未标模 $p$ 的来源式均为原特征零全恒等式。
所有 $\sigma$、$\Theta=x\sigma^2$、$x,y,b$ 保正文的原绝对规范。

### A.1. 两个真实 whole degree68 来源

在正文的 $Q_7,A_2$ 之外记
$$
f=X+b,\quad d=X-8b,\quad
P_-=X^3-96bX^2+48b^2X+64b^3,\quad
P_+=X^3+228bX^2+48b^2X+64b^3 .
\tag{A1}
$$
原来源的完整式为
$$
S=\frac{\sigma^{34}x^2fdQ_7}{7},\quad
T=\frac{\sigma^{72}Xfd(X+4b)Q_7A_2P_-}{7},\quad
V=\frac{\sigma^{66}Xfd^2(X+4b)Q_7P_+}{7}.
\tag{A2}
$$
令
$$
W_{68}=\frac{T}{\Theta^2}
=\frac{\sigma^{68}xfd(X+4b)Q_7A_2P_-}{7}.
\tag{A3}
$$
(A3)是 whole 来源：原 $T$ 的 $x^3$ 因子被 $x^2$ 除后仍留下
$x$，没有新增有限极。它与 $V\Theta$ 都在原 degree68 格内、
型零且首项为 $z^6$。这里没有把 $W_{68}$ 单独赋中央零。

直接乘开原三个多项式得
$$
X(X-8b)P_+-A_2P_-
=8b(X+b)(37X^3-24bX^2-240b^2X+64b^3).
\tag{A4}
$$
定义确定的同模型来源
$$
\begin{aligned}
H'_{22}&=\sigma^{22}(37X^3-24bX^2-240b^2X+64b^3),\\
F_{12}&=\sigma^{12}(X+b)(X+4b),\\
K_{46}&=\frac SxF_{12}
=\frac{\sigma^{46}xf^2d(X+4b)Q_7}{7}.
\end{aligned}
\tag{A5}
$$
于是有完整同 degree 身份
$$
\boxed{\Delta_{68}:=V\Theta-W_{68}=8bK_{46}H'_{22}.}
\tag{A6}
$$
$F_{12}$ 的质量为一，$K_{46}=z^8+\cdots$，
$H'_{22}=37z^4+\cdots$，故 $\Delta_{68}=296bz^{12}+\cdots$。
各多项式仅在 $O$ 有极且极阶小于相应 sigma 次数：
$K_{46}$ 的最大极阶为 $38$，$H'_{22}$ 为 $18$。
因此(A6)没有用一个仅局部合法的除法替代 whole 格。

### A.2. 两个原中央条件的完整 cross 搬运

对本节实际型零来源 $A$ 及质量一型零伙伴 $B$，令
$$
\mathscr X_p(A,B)=
\sum_{\substack{6\le r\le p-5\\r\equiv0\ (6)}}
\frac{j_r(A)j_{p+1-r}(B)}{r(r-1)} .
\tag{A7}
$$
本节只用 $(A,B)=(V,\Theta)$、$(W_{68},\Theta^2)$。
其质量分别为 $(0,1)$，一次 jet 都为零。
真实 Leibniz 公式中的两个端项是 $j_{p+1}(A)$ 和零，
而 $2\le r\le p-1$ 时
$$
\frac1p\binom{p+1}{r}\equiv\frac{(-1)^r}{r(r-1)}\pmod p.
$$
非零项的 $r$ 都为六的倍数，所以没有额外负号。
这逐项证明
$$
\mathfrak B(V\Theta)=\mathfrak B(V)+\mathscr X_p(V,\Theta),
\qquad
\mathfrak B(T)=\mathfrak B(W_{68})
+\mathscr X_p(W_{68},\Theta^2).
\tag{A8}
$$
所有(A7)的单因子 jet 都严格低于 $p$；两个原
$\mathfrak B$ 的整性仍来自 R855/R856 的同一原 whole 格。

在(A6)右边，两个零阶分别为八和四，因此其完整首读数也是严格低窗：
$$
\mathscr W_p(H)=
\sum_{\substack{8\le r\le p-3\\r\equiv2\ (6)}}
\frac{j_r(K_{46})j_{p+1-r}(H)}{r(r-1)}
\quad
\left(H\in\sigma^{22}\langle X^3,bX^2,b^2X,b^3\rangle\right).
\tag{A9}
$$
每个这样的 $H$ 首阶至少四；(A9)正是
$\mathfrak B(K_{46}H)$，没有漏掉高端，也没有增添一个首
$\Theta$ 对数商。由(A6)、(A8)得
$$
\boxed{
8b\,\mathscr W_p(H'_{22})
=\mathfrak B(V)-\mathfrak B(T)
+\mathscr X_p(V,\Theta)+\mathscr X_p(W_{68},\Theta^2).
}
\tag{A10}
$$
因此两个原中央首必要条件确实给出
$$
8b\,\mathscr W_p(H'_{22})
=\mathscr X_p(V,\Theta)+\mathscr X_p(W_{68},\Theta^2),
\tag{A11}
$$
而不是 $\mathscr W_p(H'_{22})=0$。
(A11)使用原两个条件，未用热伴随的一个假零。

### A.3. 同一个 sigma2 三次因子与准确连接权

令 $\sigma_2=\sigma(2z)$。因为 $\sigma_2=-2y\sigma^4$，
(A5)准确分解为
$$
\boxed{
K_{46}=\sigma_2^3J_{34},\qquad
J_{34}=-\frac{\sigma^{34}xyQ_7(X-8b)(X+4b)}{56}.
}
\tag{A12}
$$
$J_{34}=z^5/8+\cdots$ 是 whole degree34 型五来源。
(A9)于是确与正文(30)共享同一个原 $\sigma_2^3$；
区别是这里仍有固定的非恒定权 $J_{34}$。

这个权有以下准确的原连接原函数。保持
$$
F=\Theta^{17},\qquad q_F=F'/F=34(\zeta+y/x),\qquad
\nabla_F=D_z-q_F,
$$
并定义
$$
A_{34}=\sigma^{34}x^2
\left(\frac{X^4}{48}-\frac{bX^3}{21}
-\frac{4b^2X^2}{21}+\frac{b^3X}{21}-\frac{32b^4}{105}\right).
\tag{A13}
$$
则
$$
\boxed{\nabla_FA_{34}=J_{34}.}
\tag{A14}
$$
完整核对如下：若 $A=\sigma^{34}x^2P(X)$，则
$$
\nabla_FA=6\sigma^{34}xy(XP'(X)-5P(X)).
$$
而
$$
Q_7(X-8b)(X+4b)
=7X^4-32bX^3-192b^2X^2+64b^3X-512b^4.
$$
将(A13)代入上一行即得(A14)，包括全部 $b$ 项。
此处 $A_{34}$ 首项 $z^6/48$，最大极阶为二十八；
连接产生的有限极已经由显示的 $x^2$ 因子消去。

对 $C_H=\sigma_2^3H$，完整乘积连接式为
$$
\boxed{
K_{46}H
=J_{34}C_H
=\nabla_{F^2}(A_{34}C_H)-A_{34}\nabla_FC_H.
}
\tag{A15}
$$
这里 $\nabla_{F^2}=D_z-2q_F$，不可省略第二项。
若 $H=H'_{22}$，其非零常数项 $64b^3$ 使
$\nabla_FC_H$ 自身在 $x=0$ 有真实极；该极在
$A_{34}\nabla_FC_H$ 中被 $A_{34}$ 的 $x^2$ 因子消去。
所以(A15)右边的实际 whole 乘积合法，却不能把裸
$\nabla_FC_H$ 当成一个已经支付的 whole 算术来源。

还可将(A15)直接写成原读者。$A_{34}C_H$ 首阶至少十三，
型一；其原 $\mathcal D_{68,p,2}$ 的两个低 Hasse 项均为零。
因为 $q_F$ 从第五阶起，所有下列卷积严格低于 $p$，
故(A15)给
$$
\boxed{
\begin{aligned}
\mathscr W_p(H)
={}&\mathcal D_{68,p,2}(A_{34}C_H)
+2\!\!\sum_{\substack{5\le r\le p-12\\r\equiv5\ (6)}}
 \frac{j_r(q_F)j_{p+1-r}(A_{34}C_H)}{r(r-1)}
-\mathfrak B(A_{34}\nabla_FC_H).
\end{aligned}}
\tag{A16}
$$
正号来自 $r$ 为奇数时
$\binom{p+1}{r}/p\equiv-1/[r(r-1)]$。
(A16)只是同一个实际(A9)的完整带权连接式；
没有将其中某个新伴随赋零。

这个权不能通过原三列的线性换基删去。
在特征零的三个非零二挠点 $X=-b$ 上，
(A13)的括号值为 $-797b^4/1680\ne0$，
而原 $Z_j=E_jJ_S$ 全带因子 $X+b$，均为零。
故 $A_{34}$ 不在原 $\langle Z_0,Z_1,Z_2\rangle$ 中。
此断言是显示来源的特征零比较，不把它升级成所有允许素数上的
指定读数非零；若约化该点值，还须保固定分子 $797$。

### A.4. 与原 H22 及本篇两低读者的准确联合

使用 R879 原
$$
G_{22}=-\frac{\sigma^{22}}{21}
(19X^3-119bX^2+56b^2X+32b^3),\qquad
B_{22}=\sigma^{22}X(X+b)(X-8b),
$$
则原四坐标的逐项恒等式为
$$
\boxed{
H'_{22}=\frac{69}{25}H_{22}-42G_{22}
-\frac{902}{5}B_{22}-\frac{76896}{25}b^2\sigma^{22}X.
}
\tag{A17}
$$
因此(A9)中可用(A17)线性展开，但全部四项都仍由同一
$K_{46}$ 读。R876 支付了这一整个 degree22 四维 CM 来源，
并未支付将有限 CM word 从带权读者中移走的交织。

联合正文(32)，原 $\mathfrak B(S)=\mathfrak B(T)=
\mathfrak B(V)=0$ 准确留下以下两条显示关系：
$$
\boxed{
\begin{aligned}
\mathcal D_{24,p,5}(\widehat G_{24})-\mathcal R_{T,p}
&=\frac{136}{55}b\,\mathfrak B(D_{\rm ref})
+\frac{2592}{7}b\,\mathcal L_p(C_0),\\
8b\,\mathscr W_p(H'_{22})
&=\mathscr X_p(V,\Theta)+\mathscr X_p(W_{68},\Theta^2).
\end{aligned}}
\tag{A18}
$$
第一条保持正文(30)的两项原低配对及完整参考；
第二条保持(A7)的两个原 cross。
$\mathcal L_p(C_0)$ 与 $\mathscr W_p$ 不是同一泛函：
前者为 degree34 的原未加权连接行，后者为(A12)–(A16)
显示的 degree68 带权行。
所以(A17)不能将(A18)第二条直接代成第一条的一个常数倍。
目前真实减少的是(A10)里的两个原中央首项，而非这些
固定的低卷积或连接伴随。这里没有宣称四原首行不可能同时为零。

### A.5. 原有理坐标的对数微分式及 R853 的同 P2 输入

(A12)还有一个不更换 sigma frame 的有理形式。令
$$
v=-\frac y{x^2}.
$$
由 $D_zy=3x^2$、$D_zx=2y$ 得
$$
D_z\log v=\frac{3x^2}{y}-\frac{4y}{x}
=-\frac{X+4b}{xy}.
$$
故
$$
\boxed{
\frac{J_{34}}S=\frac18D_z\log v,\qquad
\Delta_{68}=b\,S\,(\sigma_2^3H'_{22})\,D_z\log v.
}
\tag{A19}
$$
其全部有限极都由同一显示乘积抵消；不能将 $D\log v$ 单独删去。
在原 $t=-b/X$ 坐标上，
$$
v^6=-\frac{t(1-t)^3}{b},\qquad
d\log v=\frac{1-4t}{6t(1-t)}\,dt.
\tag{A20}
$$

具体接 R853 时固定其 $b=1$ 模型与同一个
$Z,G,\mathcal P_2$，不重新选择 Frobenius 初值。
对 degree $2n$ 的代数来源 $\sigma^{2n}R$，
记 $\widehat A=\mathcal P_2^nR$。则(A19)在这个实际有理模型中仍逐项为
$$
\boxed{
Z^{-p-2}\widehat\Delta_{68}\,\omega
=Z^{-p-2}\widehat S\,\widehat C_{H'_{22}}\,d\log v .
}
\tag{A21}
$$
左右的 $\mathcal P_2$ 总幂均为三十四。
没有由 $\widehat S$ 或 $\widehat C_H$ 中抽出一个未经支付的 $p$ 次幂。

R853 §§2–6 的完整极证明适用于(A21)：
$\widehat\Delta_{68}$ 在 $O$ 阶至少十二；
非原点 $Z$ 零点仍由同一指定 $\mathcal P_2$ 的至少 $p$ 阶零抵消；
三个二挠点的极帽可用 $n=34$ 的原上界。
型零不变性亦保持。因此若
$$
\alpha_\Delta=[z^{p+1}]\widehat\Delta_{68},
$$
则准确有
$$
\boxed{
\mathcal C^4\!\left(
 Z^{-p-2}\widehat S\,\widehat C_{H'_{22}}\,d\log v
\right)
=-\alpha_\Delta^{1/p^4}\frac{x^2}{y}\omega .
}
\tag{A22}
$$
原有限窗口给
$\mathfrak B(\Delta_{68})=U_p\alpha_\Delta$，
$U_p=(p+1)!/p\equiv-1\pmod p$。
所以在原 $V,T$ 两首必要行零时，
$$
\alpha_\Delta=
-\mathscr X_p(V,\Theta)-\mathscr X_p(W_{68},\Theta^2)
\pmod p.
\tag{A23}
$$
(A22)保同一原输入及其全部 Frobenius 资料；
$\mathcal C(d\log v)=d\log v$ 不会把(A21)的非 $p$ 次幂乘子消掉。
(A23)也明确：原两中央并不让这个新的加权 Cartier 输出为零。
若要由它排除四中央共同零，仍须对这里的实际完整乘子或
(A18)的两个 cross 证明额外关系，不能只依固定对数目标的一维性。


## 附录 B. 同 degree36 的实际 new 因子与两原差的减项

本附录继续附 A 的同一个原 $S,T,V$。其新增来源内容是：
两条不同 degree22 伙伴在完整原乘法中有一个确定的差，
准确回到 $S\Theta$；这把带权差减少成一个固定伙伴配对和
一个同 $S$ 的自配对。全部质量一 cross 仍保留。
它不把自配对设为零，也不替换正文(30)的未加权 $\mathcal L_p$。

### B.1. 原 STheta 的完整范数三分解

记
$$
A=S\Theta,\qquad
A_{12}=\sigma^{12}(X+b),\qquad
B_{12}=\Theta^3F_6=\sigma^{12}X(X-8b),\qquad
D_{36}=[\delta]^*B_{12}.
\tag{B1}
$$
$A$ 的 degree 为 $36$、首项为 $z^6$；
$A_{12}$ 首阶六；$B_{12}$ 与 $D_{36}$ 的质量为一。
由原
$$
J_S\Theta=-\sigma^{12}xy(X-8b)
=\frac{\sigma(2\delta z)}{2\delta}
=\frac1\delta[\delta]^*\frac{\sigma(2z)}2
$$
和 R877 的完整式
$\mathrm T_{\delta,8}C_{24}=-\sigma^8y/(7\delta)$，
使用同一个三点迹的投影公式，得到
$$
\boxed{\mathrm T_{\delta,12}A=-\frac1{21}A_{12}.}
\tag{B2}
$$
这里保 $\sigma(2z)/2=-y\sigma^4$ 以及 $\delta^2=-3$，
故显示的负号也已固定。

定义同一原来源的真实投影
$$
A^{\rm old}=\Pi_\delta^{(36)}A
=-\frac1{63}[\delta]^*A_{12},\qquad
N_{36}=A-A^{\rm old}.
$$
准确的多项式为
$$
\boxed{
A^{\rm old}=\frac37\sigma^{36}X^2(X+b)(X-8b)^2,\qquad
N_{36}=\frac47\sigma^{36}X(X+b)^2(X-8b)(X+4b).
}
\tag{B3}
$$
证明只需用原
$$
[\delta]^*A_{12}=-27\sigma^{36}X^2(X+b)(X-8b)^2
$$
以及
$$
Q_7=3X(X-8b)+4(X+b)(X+4b).
\tag{B4}
$$
所以 $\mathrm T_{\delta,12}N_{36}=0$ 是原完整投影的身份。
还有准确的既有伙伴表达
$$
N_{36}=C_{24}^{\rm new}\,\frac{\sigma(2\delta z)}{2\delta},
\qquad
C_{24}^{\rm new}=-\frac47\sigma^{24}x^2y(X+b)(X+4b).
\tag{B5}
$$
这里没有把 $C_{24}$ 的两个投影部分分别赋中央零。

### B.2. 两个 degree36 伙伴及其同源差

沿用附 A 的 $P_+,P_3=37X^3-24bX^2-240b^2X+64b^3$，定义
$$
J_{36}=\sigma^{36}Q_7P_+,\qquad
L_{36}=\sigma^{36}Q_7P_3 .
\tag{B6}
$$
二者均为原 whole degree36 型零来源，首阶至少六；
$J_{36}$ 首系数为七，$L_{36}$ 首系数为 $259$。
原 sigma 除法式逐项给
$$
[\delta]^*\Theta=\sigma^6(X+4b),\qquad
[\delta]^*F_6=\sigma^{18}P_+,
$$
因此
$$
\boxed{D_{36}=\sigma^{36}(X+4b)^3P_+.}
\tag{B7}
$$

现在在同一个 degree72 格中，有两个完整身份
$$
\boxed{
V\Theta^3=A D_{36}-4bN_{36}J_{36},\qquad
V\Theta^3-T=2bN_{36}L_{36}.
}
\tag{B8}
$$
第一式将(A2)、(B3)、(B7)代入后只剩
$(X+4b)^2-X(X-8b)=16b(X+b)$。
第二式即(A6)乘 $\Theta^2$，全部系数仍是原系数。

两个右伙伴不是独立的四谱输入。直接相减原三次多项式：
$$
P_3-P_+=36X(X+b)(X-8b),
$$
故
$$
\boxed{
L_{36}-J_{36}=252A.
}
\tag{B9}
$$
这是固定来源身份，不是对环境空间作维数计数。
在(B8)中消掉同一个 $N_{36}J_{36}$ 后得到
$$
\boxed{
3V\Theta^3-2T=A(D_{36}+1008bN_{36}).
}
\tag{B10}
$$
因而其中一个实际配对确回到了原 $A=S\Theta$ 自身。

### B.3. 全三点迹中的同一 old 项

为明确(B8)没有只保边际，以下给出其相关完整迹。
R877 原 $C_{30}$ 满足 $V=C_{30}[\delta]^*B_*$，其中
$$
B_*=\frac{\delta}{3}\sigma^{12}xy(X-8b).
$$
在正文(6)的三个根上，
$$
\operatorname{Tr}x^{-1}=0,\quad
\operatorname{Tr}x^{-4}=\frac{9a^2}{8b^2},\quad
\operatorname{Tr}x^{-7}=-\frac{63a^2}{64b^3}.
$$
而 $C_{30}\sigma^6$ 除以 $\sigma(\delta z)^{12}$ 后的完整商是
$$
\frac{3\delta^{-11}c}{7}
(7x^{-1}-4b x^{-4}+16b^2x^{-7}).
$$
括号的迹准确为 $-81a^2/(4b)$，于是
$$
\mathrm T_{\delta,12}(C_{30}\sigma^6)
=-\frac{\delta}{84b}\sigma^{12}x^2y,
\qquad
\mathrm T_{\delta,24}(V\sigma^6)
=\frac{\sigma^{24}X(X+b)(X-8b)}{84b}.
\tag{B11}
$$
再由
$\Theta^3=[\delta]^*\Theta-4b\sigma^6$、
$\mathrm T_{\delta,22}V=0$ 与正文(11)，得到
$$
\boxed{
\mathrm T_{\delta,24}(\Theta^2\Delta_{68})
=-\frac{\sigma^{24}X(X+b)(X-8b)}{21}
=B_{12}\,\mathrm T_{\delta,12}(A).
}
\tag{B12}
$$
所以这里的 old 项与(B2)确为同一原来源。
(B11)保全部三个纤维及绝对 sigma 商，没有将 $B_*$ 从错误的轴抽出。
(B12)也不让首除 $p$ 读者与迹无缺陷交换。

### B.4. 两原差变成同一个 new 因子的两个对称低配对

对本节实际两个 degree36、型零且从第六阶起的来源，定义
$$
\mathcal Q_p(F,G)=
\sum_{\substack{6\le r\le p-5\\r\equiv0\ (6)}}
\frac{j_r(F)j_{p+1-r}(G)}{r(r-1)}.
\tag{B13}
$$
完整 Leibniz 公式给
$\mathcal Q_p(F,G)=\mathfrak B(FG)$。
两个端项均由质量零和一次 jet 零消去，所有剩余 jet 严格小于 $p$。
在模 $p$ 中用 $r\mapsto p+1-r$，
其分母变为 $(1-r)(-r)=r(r-1)$，故
$\mathcal Q_p(F,G)=\mathcal Q_p(G,F)$。
这里的权始终是 $1/[r(r-1)]$，没有换成另一种 apolar 配对。

记以下两个确定值和三个完整质量一 cross：
$$
\begin{aligned}
Q_{1,p}&=\mathcal Q_p(N_{36},J_{36}),&
Q_{2,p}&=\mathcal Q_p(N_{36},A),\\
x_{S,p}&=\mathscr X_p(S,\Theta),&
x_{D,p}&=\mathscr X_p(A,D_{36}),&
x_{V,p}&=\mathscr X_p(V,\Theta^3).
\end{aligned}
\tag{B14}
$$
$\mathscr X_p$ 仍是(A7)的准确低卷积。
对(B8)、(B10)逐项应用同一原 $\mathfrak B$，得到
$$
\boxed{
\begin{aligned}
4bQ_{1,p}
&=\mathfrak B(S)-\mathfrak B(V)
+x_{S,p}+x_{D,p}-x_{V,p},\\
1008bQ_{2,p}
&=-\mathfrak B(S)+3\mathfrak B(V)-2\mathfrak B(T)
-x_{S,p}-x_{D,p}+3x_{V,p}.
\end{aligned}}
\tag{B15}
$$
没有对 $N_{36}$、$J_{36}$ 或 $A D_{36}$ 另设中央条件。
从原三条必要零条件只能删除(B15)中三个原
$\mathfrak B(S),\mathfrak B(T),\mathfrak B(V)$，其余五个显示低值原样保留。

第二个值具有更精确的“同 S”含义：
$$
\boxed{
N_{36}/A=\frac{4(X+b)(X+4b)}{Q_7},\qquad
A^{\rm old}/A=\frac{3X(X-8b)}{Q_7}.
}
\tag{B16}
$$
两个商相加为一，但它们的有限极不能在任意来源上删去。
在本节的实际 $A^2$ 上，$Q_7$ 因子充分，故
$$
Q_{2,p}=
\mathfrak B\!\left(
 A^2\,\frac{4(X+b)(X+4b)}{Q_7}
\right)
=\mathfrak B(AN_{36})
\tag{B17}
$$
确为 whole degree72 自配对。
原 $\mathfrak B(S)=0$ 并不使(B17)为零：
它是两因子低卷积，正是(B13)，而不是单一来源中央的乘方传播。

这给附 A 带权行一个真实减项：
$H'_{22}-\sigma^{22}P_+=36B_{22}$ 在完整乘法之后，
其中第二项准确回成(B17)的同原 $S$ 自配对。
正文(30)、(32)的未加权 $\mathcal L_p(C_0)$、
$\mathfrak B(D_{\rm ref})$ 和 $\mathcal R_{T,p}$ 仍然保留；
(B15)没有把它们认作这两个 degree72 配对。
原 $U$ 的二挠 new 行亦未改变。
后续若要排除共同零，须约束(B15)这同一五个低值，
或把(B17)与原 $U$ 的完整二挠伙伴实际相连。
单凭配对对称、同 degree 或 $N_{36}$ 的迹零都不足以完成该步。


## 附录 C. 原 U 的完整二挠伙伴及三个 degree36 来源之外的单位边界

本附录继续使用同一个原 $U_{136}$，并令
$$
A_8=\sigma^8x,\qquad
\mathcal H_{36}:=\mathrm T_{2,36}(UA_8).
\tag{C1}
$$
这里 $\mathrm T_{2,m}$ 是完整四纤维 canonical trace：
$$
\mathrm T_{2,m}(\sigma^{4m}R)
=\sigma^m\operatorname{Tr}_{[2]}
 \frac{R}{(-2y)^m}.
\tag{C2}
$$
绝对倍率由 $\sigma(2z)=-2y\sigma(z)^4$ 固定；本附录没有把完整迹改成选取两根或除以四的平均。

### C.1. 与原 U 的准确乘法关系

准确倍点式给
$$
x(2z)=\frac{x(X-8b)}{4(X+b)},\qquad
[2]^*\Theta=\sigma^8x(X-8b)=\Theta^4-8bA_8.
\tag{C3}
$$
原 R466 的二挠 new 身份为 $\mathrm T_{2,34}U=0$。
因此由(C2)的完整投影公式，
$$
\boxed{
\mathrm T_{2,36}(U\Theta^4)=8b\,\mathcal H_{36}.
}
\tag{C4}
$$
此式只消掉了与目标 $\Theta$ 对应的准确 old 乘积；
并未消掉 $UA_8$。

为固定输入，写
$$
U=\frac{\sigma^{136}x^2(X+b)}{91}
 Q_7A_2F_4G_4H_8,
\tag{C5}
$$
其中 $Q_7$、$A_2$ 与正文相同，而
$$
\begin{aligned}
F_4={}&X^4+40bX^3+2112b^2X^2+3136b^3X+1792b^4,\\
G_4={}&13X^4+52bX^3+1536b^2X^2+1024b^3X+256b^4,\\
H_8={}&X^8+1232bX^7-58688b^2X^6-49408b^3X^5
 -439040b^4X^4\\
&-2111488b^5X^3-1949696b^6X^2-851968b^7X-32768b^8.
\end{aligned}
\tag{C6}
$$
所有因子均为原 U 的定义，尤其不能把 $H_8$ 换成原 $S(2z)$ 的因子。

若目标坐标为 $a=x(2z)$，四个原输入 $x$ 满足
$$
x^4-4ax^3-8bx-4ab=0,\qquad
(x-4a)(x^3+b)=9bx.
\tag{C7}
$$
所以(C1)的有理系数准确是
$$
\frac{\mathcal H_{36}}{\sigma^{36}}
=\frac1{91\cdot2^{36}}
 \operatorname{Tr}_{(C7)}
 \frac{x^3Q_7(x^3)A_2(x^3)F_4(x^3)G_4(x^3)H_8(x^3)}
 {(x^3+b)^{17}}.
\tag{C8}
$$
原 U 自身的 trace 分母则是 $(x^3+b)^{16}$、分子带 $x^2$，
与(C8)不同。也可利用(C7)将(C8)写成
$\operatorname{Tr}(x\,r_U)/36$，其中
$r_U=R_U/(-2y)^{34}$，因为 $\operatorname{Tr}r_U=0$。
这保留同一四纤维的全部来源。

### C.2. Whole、角型与原两处边界

(C2)将 whole degree144 截面送到 whole degree36 截面。
$U$ 与 $A_8$ 均为 $\mu_6$ 型零，且 $[2]$ 与该作用交换，
所以 $\mathcal H_{36}$ 也为型零。

在目标原点的四个逆像中，$UA_8$ 在输入原点从第十二阶起；
在三个非零二挠点，(C5)的 $X+b$ 至少给二阶零。
canonical 线丛同构的局部倍率为单位，因此完整 trace
在目标原点至少二阶消失。
型零随即将其提高到至少六阶。
故存在准确多项式 $h_b$，使
$$
\boxed{
\mathcal H_{36}=\sigma^{36}h_b(X),\qquad
\deg_Xh_b\le5.
}
\tag{C9}
$$
齐次尺度为
$h_b(X)=\sum_{j=0}^5 h_jb^{4-j}X^j$；负的 $b$ 次数只表示原单位 $b$ 的分母。

原第四除法多项式是
$$
\psi_4/(4y)=A_2=X^2+20bX-8b^2.
$$
因此(C5)在全部本原四挠点消失。
每个非零二挠点的四个 $[2]$ 逆像恰是本原四挠点；
$A_8$ 不引入极，canonical 局部倍率仍为单位。
于是(C9)在三个非零二挠点均消失，给
$$
\boxed{h_b(-b)=0,\qquad X+b\mid h_b(X).}
\tag{C10}
$$
这一步使用完整四个逆像，不能从单一纤维的零点推出。

另一处边界可直接在(C8)计算，无需恢复其余系数。
当目标 $a=0$ 时，(C7)的根为 $x=0$ 和 $x^3=8b$ 的三个根；
它们在特征零及原好特征中均为简单根。
$x=0$ 项准确为零。其余三项相同，使用
$$
\begin{aligned}
Q_7(8b)&=2^4 3^3b^2,&
A_2(8b)&=2^3 3^3b^2,\\
F_4(8b)&=2^8 3^6b^4,&
G_4(8b)&=2^8 3^6b^4,\\
H_8(8b)&=-2^{15}3^{12}b^8.
\end{aligned}
\tag{C11}
$$
每一项为 $-32b^4/7371$，故
$$
\boxed{h_b(0)=-\frac{32}{2457}b^4.}
\tag{C12}
$$
例如(C11)最后一项可直接由原(C6)的 Horner 展开得到
$H_8(8)=-17414258688=-2^{15}3^{12}$；
它没有采用任何辅助素数或拟合数值。
(C10)、(C12)为同一个原 trace 的两个准确边界。

### C.3. 对三个实际来源的固定左行

对(C9)的全六维多项式空间，定义
$$
\Lambda_{36}(\sigma^{36}q(X))
=6561q(0)-1024q(-b).
\tag{C13}
$$
附录 B 的三个实际来源满足
$$
A(0)/\sigma^{36}=N_{36}(0)/\sigma^{36}=0,\qquad
A(-b)/\sigma^{36}=N_{36}(-b)/\sigma^{36}=0,
$$
这里写的是其有理系数的代入，不是把 $z=0$ 代入含极的 $x$。
同一原 $J_{36}$ 的系数则满足
$$
(Q_7P_+)(0)=1024b^5,\qquad
(Q_7P_+)(-b)=6561b^5.
$$
因此
$$
\boxed{
\Lambda_{36}(A)=\Lambda_{36}(N_{36})=\Lambda_{36}(J_{36})=0,
\qquad
\Lambda_{36}(\mathcal H_{36})=-\frac{7776}{91}b^4.
}
\tag{C14}
$$
右端在原 $p>211$、$b$ 为单位的范围内仍为单位。
所有 trace 和所示多项式在该范围内可整地约化：
(C5)的固定分母为 $91$，(C2)的核度为四，
(C7)展开只需另外倒置 $2,3,b$。
故(C14)不只排除特征零的 span；同一原好特征下也严格有
$$
\boxed{\mathcal H_{36}\notin
 \langle A,N_{36},J_{36}\rangle.}
\tag{C15}
$$
(C14)是完整固定左行；无需等待六坐标恢复或有限矩阵实验才成立。
它也不表示原四条算术中央互不相容：
此左行读取的是来源边界，并非原 $\mathfrak B$。

### C.4. 原除 p 行中的完整余项

为把(C4)放回真正读者，保留整个 canonical 投影，令
$$
\mathcal U_{144}^{\mathrm{new}}
=U\Theta^4-2b[2]^*\mathcal H_{36}.
\tag{C16}
$$
由于 $\mathrm T_{2,36}[2]^*=4I$，
(C4)准确给
$\mathrm T_{2,36}\mathcal U_{144}^{\mathrm{new}}=0$。
(C16)的两项都从第六阶起，故同一个
$\mathfrak B=j_{p+1}/p$ 在二者上合法。
完整 Leibniz 及真实倍点读数给
$$
\boxed{
\mathfrak B(U)+\mathscr X_p(U,\Theta^4)
=8b\,\mathfrak B(\mathcal H_{36})
+\mathfrak B(\mathcal U_{144}^{\mathrm{new}})
\pmod p.
}
\tag{C17}
$$
这里 $\mathscr X_p$ 仍为(A7)的全部严格低于 $p$ 卷积。
在约化以前，倍点项的准确系数是 $2b\,2^{p+1}$；
(C17)只在模 $p$ 后使用 $2^{p+1}\equiv4$。
更高精度不能据此省去 $q_p(2)$。
原 $\mathfrak B(U)=0$ 只删除(C17)左侧该一项；
trace 零不使右侧 new 余项的 $\mathfrak B$ 为零，
也不使 $\mathfrak B(\mathcal H_{36})$ 为零。

因此(C14)定位了原 U 必须携带的一个真实新增来源方向，
(C17)保留它与原中央及全 cross 的准确关系。
下一步可恢复(C9)的全部六系数，或对(C17)两个实际余项求同源关系；
不能用三个已知 degree36 来源的环境维数消掉此方向。

本附录所有结论均为固定四纤维、有理多项式及线丛局部零阶的手证。
公开 Fraction producer 只用于进一步恢复(C9)的全部坐标，
不是(C10)–(C17)的证明前提。


## 附录 D. 原 U 四纤维的全因式、同一 C8 返回及实际旧标量消元

### D.1. 完整特征零迹与准确剩余来源

对(C8)的原四纤维作全 Laurent Newton 迹，得到
$$
(h_0,h_1,h_2,h_3,h_4,h_5)
=\frac1{2457}(-32,-16,148,220,92,4).
\tag{D1}
$$
因此一般原单位 $b$ 的完整来源不是拟合值，而是
$$
\boxed{
\mathcal H_{36}
=\frac{4}{2457b}\sigma^{36}(X+b)^3
 (X^2+20bX-8b^2).
}
\tag{D2}
$$
展开右端的五次多项式，准确给
$$
(X+b)^3A_2
=X^5+23bX^4+55b^2X^3+37b^3X^2-4b^4X-8b^5,
$$
故(D2)同时恢复(C10)、(C12)，并进一步支付非零二挠点的六阶零。

为使(D1)可完整重算，固定 $b=1$，令 $p_j=\operatorname{Tr}x^j$。
由(C7)，其正幂初值为
$$
p_0=4,\quad p_1=4a,\quad p_2=16a^2,\quad
p_3=64a^3+24,\quad p_4=256a^4+144a,
$$
并有
$$
p_j=4ap_{j-1}+8p_{j-3}+4ap_{j-4}\quad(j\ge5).
$$
逆根满足
$u^4+(2/a)u^3+u-1/(4a)=0$，故负幂初值及递推为
$$
\begin{aligned}
p_{-1}&=-2/a,&p_{-2}&=4/a^2,\\
p_{-3}&=-8/a^3-3,&p_{-4}&=16/a^4+9/a,\\
p_{-j}&=-2p_{-(j-1)}/a-p_{-(j-3)}
       +p_{-(j-4)}/(4a)\quad(j\ge5).
\end{aligned}
$$
在(C8)中用
$(x^3+1)^{-17}=(x-4a)^{17}/(9x)^{17}$，
只需上述 $-14\le j\le63$ 的完整幂和。
逐项相加后所有负次及非 $3$ 倍次幂均消失，六个剩余系数恰为(D1)。
同一算法恢复原 $\mathrm T_{2,34}U=0$ 及
$\mathrm T_{2,2}A_8=-\Theta/3$，所以绝对倍率与原来源同时核定。

对附录 B 的三个实际列，完整六行还给
$$
\boxed{
\mathcal H_{36}
=\frac5{1248b}(A-N_{36})
-\frac{J_{36}}{78624b}
+\frac{243}{2912}\sigma^{36}X^4.
}
\tag{D3}
$$
三个原列的秩为三，附加本来源后秩为四。
最后一项不可删除；它正是(C14)检测到的实际剩余。

但这个剩余不是另一个待猜测的高 degree 来源。
原准确式
$\sigma(\delta z)=\delta x\sigma^3$、$\delta^{12}=729$
给
$$
[\delta]^*\sigma^{12}=729\sigma^{36}X^4.
$$
再用(B2)的 $A-N_{36}=-[\delta]^*A_{12}/63$，置
$$
K_{12}:=\sigma^{12}(4b-5X)=9b\sigma^{12}-5A_{12},
$$
便将(D3)化为
$$
\boxed{
J_{36}+78624b\,\mathcal H_{36}=[\delta]^*K_{12}.
}
\tag{D4}
$$
此式的右端保留原范数三拉回，不用任何新算术零。

### D.2. 原 C120 与已经出现的同一个 C8

设
$$
C_{120}
=-\frac{\sigma^{120}x^2yQ_7F_4G_4H_8}{91},
\qquad C_8=\sigma^8y,\qquad B_4=\sigma(2z)/2.
\tag{D5}
$$
$C_{120}$ 是 whole degree120、型五、首 $z^5$ 系数一的实际来源。
由
$\sigma(4z)=-4yA_2\sigma^{16}$，原(C5)准确给
$$
\boxed{
U=C_{120}\frac{\sigma(4z)}4
=\frac12C_{120}[2]^*B_4,\qquad
\mathrm T_{2,30}C_{120}=0.
}
\tag{D6}
$$
最后一式由 $\mathrm T_{2,34}U=0$ 和完整投影公式推出；
目标非零截面 $B_4$ 可在函数域中约消，不能把这步改成逐纤维消失。

对(C1)应用同一投影公式，得到
$$
\mathcal H_{36}
=\frac{B_4}{2}\,\mathrm T_{2,32}(C_{120}A_8).
$$
在(D2)中使用
$$
[2]^*C_8=32\sigma^{32}y^5A_2,
$$
遂有完整身份
$$
\boxed{
\mathrm T_{2,32}(C_{120}A_8)
=-\frac{[2]^*C_8}{9828b}.
}
\tag{D7}
$$
这里没有以 $C_{120}$ 的 trace 零删除乘法后的 trace。
(D7)是原 U 的全伙伴返回，而其目标 $C_8$ 正是
R877(16)–(19)已出现的 $C_{24}$ 范数三 old 伙伴：
$$
C_{24}^{\mathrm{old}}
=-\frac1{21\delta}[\delta]^*C_8,\qquad
C_{24}^{\mathrm{new}}=C_{24}-C_{24}^{\mathrm{old}}.
\tag{D8}
$$
两次返回用的是同一个 $\sigma^8y$，绝对倍率和原 $b$ 全部一致。

再令
$$
C_9=\sigma C_8=\sigma^9y.
$$
(D2)也准确等于
$$
\boxed{
\mathcal H_{36}
=\frac{\sigma(4z)\sigma(2z)^5}{78624b}
=-\frac{[2]^*C_9}{39312b}.
}
\tag{D9}
$$
$C_9$ 保留其实际奇 degree 的标准半特征；
这里只通过其真实倍点拉回使用它，
没有把它免费并入 R856 的偶 degree 整格。
结合(D4)，得到另一个可直接展开核对的原来源身份：
$$
\boxed{
J_{36}-2[2]^*C_9=[\delta]^*K_{12}.
}
\tag{D10}
$$
其共同 $\sigma^{36}$ 多项式为
$135X^5+4536bX^4+6480b^2X^3+8640b^3X^2$；
这还独立检查了所有符号与尺度。

### D.3. 同一 C8 在原 U 与原 S 中的合法消去

记
$$
O_{8,p}=j_p(C_8)/p,\qquad
O_{24,p}^{\mathrm{new}}=j_p(C_{24}^{\mathrm{new}})/p .
\tag{D11}
$$
这两个数的整性来自 R856 的原 whole degree8/24 递推及
$j_1(C_8)=j_1(C_{24}^{\mathrm{new}})=0$。
定义完整低卷积
$$
P_{8,p}=
\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
 \frac{j_r(C_8)j_{p+1-r}(\sigma)}{r(r-1)}.
\tag{D12}
$$
全部参与的 jet 指标严格小于 $p$。
对 $C_9=\sigma C_8$ 用完整 Leibniz：
唯一高端为 $(p+1)j_p(C_8)$，其余二项式除 $p$ 后，
因为 $r$ 为奇数，准确带负号。
故
$$
\boxed{\mathfrak B(C_9)=O_{8,p}-P_{8,p}\pmod p.}
\tag{D13}
$$
这里 $\mathfrak B(C_9)$ 的整性既可由该完整乘法式，
也可由(D9)及单位 $2^{p+1}$ 得到；
不需要一个未证明的奇 degree 普遍递推。

于是(C17)变成同一个实际旧标量的准确行：
$$
\boxed{
\mathfrak B(U)+\mathscr X_p(U,\Theta^4)
=\mathfrak B(\mathcal U_{144}^{\mathrm{new}})
-\frac2{2457}(O_{8,p}-P_{8,p})\pmod p.
}
\tag{D14}
$$
原 $\mathcal U_{144}^{\mathrm{new}}$ 也有完全显式表达
$$
\mathcal U_{144}^{\mathrm{new}}
=U\Theta^4+\frac{[4]^*C_9}{19656}.
$$
其 trace 零依旧不等于其中央读数为零。

另一方面，固定原 $S=C_{24}J_S$，
$J_S=-\sigma^{10}y(X-8b)$，$j_1(J_S)=1$，并置
$$
P_{S,p}^{24}=
\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
 \frac{j_r(C_{24})j_{p+1-r}(J_S)}{r(r-1)}.
$$
由(D8)，在模 $p$ 后
$$
j_p(C_{24}^{\mathrm{old}})/p
=-\delta^{p-1}O_{8,p}/21
\equiv O_{8,p}/21.
$$
完整 Leibniz 因而给
$$
\boxed{
\mathfrak B(S)=O_{24,p}^{\mathrm{new}}
+\frac1{21}O_{8,p}-P_{S,p}^{24}.
}
\tag{D15}
$$
(D14)、(D15)消去的是同一个已经支付来源的 $O_{8,p}$：
$$
\boxed{
\begin{aligned}
&2457\bigl(
\mathfrak B(U)+\mathscr X_p(U,\Theta^4)
-\mathfrak B(\mathcal U_{144}^{\mathrm{new}})\bigr)
+42\mathfrak B(S)\\
&\hspace{12mm}
=42O_{24,p}^{\mathrm{new}}+2P_{8,p}-42P_{S,p}^{24}
\pmod p.
\end{aligned}
}
\tag{D16}
$$
所以无需假设这枚旧标量非零。
在原 $S,U$ 两条必要中央零下，只删除(D16)中的
$\mathfrak B(S)$、$\mathfrak B(U)$；
所有 new 行和低卷积仍为所显示的实际值。

还有一个与附录 B 两个配对直接同源的写法。
(D10)的三个来源均质量零，因此其真实倍点读数在首位给
$$
\mathfrak B(J_{36})-8\mathfrak B(C_9)=3\mathfrak B(K_{12}).
$$
将它代入(D14)，便得
$$
\boxed{
9828\bigl(
\mathfrak B(U)+\mathscr X_p(U,\Theta^4)
-\mathfrak B(\mathcal U_{144}^{\mathrm{new}})\bigr)
=3\mathfrak B(K_{12})-\mathfrak B(J_{36}).
}
\tag{D17}
$$
约化前的倍率仍是 $2^{p+1}$、$\delta^{p+1}$；
这里不将高位 Fermat 缺陷省掉。
同一固定来源关系还可代入(B13)，准确给
$$
Q_{1,p}
=2\mathcal Q_p(N_{36},[2]^*C_9)
+\mathcal Q_p(N_{36},[\delta]^*K_{12}).
\tag{D18}
$$
没有把最后一项以“new 与 old 正交”为由删除：
(B13)的权是实际 $1/[r(r-1)]$，
尚未证明它与原范数三投影交换。
(D16)–(D18)也不把 $\mathfrak B(J_{36})$ 认成
$\mathcal Q_p(N_{36},J_{36})$。
这留下的都是同一原 $U,S,N_{36},J_{36}$ 的完整相应读者，
不是额外的算术假设。

### D.4. 公开精确执行来源

(D1)的完整 Laurent Newton 算法已在本仓库公开 Actions 实际执行：

- run 43862249339，job 133281755877；
- source commit 9dbad443f488c8cbba484ed58e7430b70e93abdf；
- 脚本：[check-r884-original-u-a8-two-division-trace.py](../scripts/check-r884-original-u-a8-two-division-trace.py)，无参数，Python 标准库 Fraction；
- script SHA256：53cfb87bcde3d8a350a54e6ea6107afe4c29d7f93482c713d51540c8d380c5b0；
- RANK2_U_A8_CM_RESULT 原完整结果 SHA256：f6e8722eb41fce6c246e92a2401e9698e3de7ccc5640ff693f36e91bb1e144e9。

原 U 的 trace 零、$A_8$ 的绝对 trace、全六坐标与三个实际列的
全部左余量均在同一次精确运行中验证。
本稿不另提交可重算输出文件，也没有目标素数扫描。
(D2)以后所有因式化、来源运输和首除 $p$ 消元为上述准确恒等式的手推。


## 附录 E. 原 N、T 的完整二挠 new 与同 S/T 旧标量的精确消去

本附录仍使用(C2)的全四纤维 trace，包括目标 degree 为奇数时
$(-2y)^m$ 的原符号。对所有固定整数倍点和 CM 倍点，均保标准
sigma 半特征及 canonical 线丛同构。以下结论是特征零来源身份；
原好特征下由相同整模型约化，不需要目标素数扫描。

### E.1. 同一个 N36 的真正二挠返回

原来源为
$$
N=N_{36}=\frac47\sigma^{36}X(X+b)^2(X-8b)(X+4b).
\tag{E1}
$$
它在输入原点从第六阶起，在三个非零二挠点至少四阶消失。
所以 $\mathrm T_{2,9}N$ 是 whole degree9、型零且在目标原点
至少四阶消失的截面。

这里不能把 degree9 换成偶 degree 格。
其准确表达是 $\sigma^9$ 乘一个在原点极阶至多九的椭圆函数。
型零只允许
$$
\sigma^9y(c_0+c_1X).
$$
第二项的原点值非零；上述零阶因此迫 $c_1=0$。
在目标 $a=x=0$ 的四个逆像中，原(C7)给输入 $X=0$ 或 $X=8b$；
(E1)的 $X(X-8b)$ 因子杀掉全部四项。
目标 $C_9=\sigma^9y$ 在此点不为零，故 $c_0=0$。
得到完整身份
$$
\boxed{\mathrm T_{2,9}N=0.}
\tag{E2}
$$
与(B2)的 $\mathrm T_{\delta,12}N=0$ 合用，
同一个 $N$ 同时具有二挠和范数三的 new 性。
这只是两个准确 trace 零，尚未给它的除 $p$ 行赋零。

### E.2. 原 T72 的全四纤维范围

记 $P_-=X^3-96bX^2+48b^2X+64b^3$。
本篇原 T 始终是
$$
T=\frac{\sigma^{72}}7
 X(X+b)(X-8b)(X+4b)Q_7A_2P_- .
\tag{E3}
$$
它在输入原点从第六阶起，在非零二挠点至少二阶消失。
因此 whole degree18、型零的迹可写成
$\sigma^{18}q(a^3)$，其中 $\deg q\le2$。

原 $A_2$ 因子又使(E3)在全部本原四挠点消失。
与(C10)完全相同的四纤维论证给 $q(-b)=0$。
当目标 $a=0$ 时，四个输入的 $X$ 仍为 $0$ 或 $8b$，
被(E3)的原 $X(X-8b)$ 因子全部杀掉，故 $q(0)=0$。
于是目前只可写
$$
\mathrm T_{2,18}T=c\,\sigma^{18}a^3(a^3+b).
\tag{E4}
$$
以下核定这个实际 $c$，不能仅由(E4)的环境一维性赋值。

### E.3. 完整逆根 Newton 对原最高系数的精确相消

置 $f=x^3+b$，并定义
$$
M(X)=X(X-8b)(X+4b)Q_7(X)A_2(X)P_-(X).
$$
(E3)除以准确 $\sigma(2z)^{18}$ 后的商为
$$
\frac{M(f-b)}{7\cdot2^{18}f^8}.
\tag{E5}
$$
原四次方程(C7)等价于
$$
f^4-(28b+64a^3)f^3+270b^2f^2-972b^3f+729b^4=0.
\tag{E6}
$$
四个倒数 $v_i=f_i^{-1}$ 的初等对称式准确是
$$
e_1=\frac4{3b},\quad
e_2=\frac{10}{27b^2},\quad
e_3=\frac{28b+64a^3}{729b^4},\quad
e_4=\frac1{729b^4}.
\tag{E7}
$$
令 $q_k=\sum_i v_i^k$。
从完整 Newton 递推，$q_k$ 对 $e_3$ 的次数至多 $\lfloor k/3\rfloor$，
并且
$$
[e_3^2]q_6=3,\qquad
[e_3^2]q_7=7e_1,\qquad
[e_3^2]q_8=12e_1^2-8e_2.
\tag{E8}
$$
例如 $q_3$ 的 $e_3$ 系数为三，
$q_4$ 为 $4e_1$，$q_5$ 为 $5(e_1^2-e_2)$；
(E8)随即逐项得出。因此没有省去任何倒数根。

原多项式在 $f=0$ 的前三项是
$$
M(f-b)=3^{13}b^{10}
 \left(1-\frac{46f}{9b}+\frac{9f^2}{b^2}\right)+O(f^3).
\tag{E9}
$$
这可直接由原因子核定：
$M(-b)=3^{13}b^{10}$，
$M'(-b)/M(-b)=-46/(9b)$，
$M''(-b)/(2M(-b))=9/b^2$。
同时 $M(f-b)$ 的最高项是 $7f^{10}$。

现在读取(E5)完整迹的 $a^6$ 系数。
所有 $f^{-k}$、$k\le5$ 的迹对 $a^3$ 至多一次，
故不能贡献这一系数。
常数及 $f$ 项也不能贡献。
正幂部分唯一贡献来自 $7f^2$；由(E6)，
$[a^6]\operatorname{Tr}f^2=64^2$，
在(E5)中的贡献恰为
$$
\frac{7\cdot64^2}{7\cdot2^{18}}=\frac1{64}.
$$
负幂部分只有(E9)所列的 $f^{-8},f^{-7},f^{-6}$ 贡献。
利用(E7)、(E8)，其完整贡献为
$$
\begin{aligned}
&\frac{3^{13}b^{10}}{7\cdot2^{18}}
\left(\frac{64}{729b^4}\right)^2
\left[
(12e_1^2-8e_2)-\frac{46}{9b}\,7e_1+\frac{27}{b^2}
\right]\\
&\quad=
\frac{3^{13}b^{10}}{7\cdot2^{18}}
\left(\frac{64}{729b^4}\right)^2
\left(-\frac7{3b^2}\right)
=-\frac1{64}.
\end{aligned}
\tag{E10}
$$
两部分精确相消，所以(E4)的 $c=0$：
$$
\boxed{\mathrm T_{2,18}T=0.}
\tag{E11}
$$
(E6)–(E10)是完整有理迹计算。
正、负幂部分分别给出的两项不是任意挑出的纤维，
也不是有限素数上的实验。

### E.4. 原参考乘积和两个核下的同一新乘积

先记
$$
R_{24}=A_{12}B_{12}
=\sigma^{24}X(X+b)(X-8b).
\tag{E12}
$$
其原点零阶至少六，非零二挠零阶至少二，
所以 $\mathrm T_{2,6}R_{24}$ 的型零目标只能是常数乘 $\sigma^6$。
目标 $a=0$ 的四个逆像再被 $X(X-8b)$ 全部杀掉。
因此
$$
\mathrm T_{2,6}R_{24}=0.
\tag{E13}
$$

对这里的原 canonical 标准线丛，二挠 trace 与 $[\delta]^*$ 准确交换：
$\delta$ 置换 $E[2]$，而
$\mathcal T_T([\delta]^*F)=[\delta]^*(\mathcal T_{\delta T}F)$
中的 theta 乘子由同一个 $\sigma(2\delta z)$ 固定。
对全部四个 $T$ 求和，再用 $[2]^*$ 的单射，即得
$$
\mathrm T_{2,3m}([\delta]^*F)
=[\delta]^*(\mathrm T_{2,m}F).
\tag{E14}
$$
没有只交换边际，或将未经核定的半特征删去。
因而(E13)也支付 $[\delta]^*R_{24}$ 的完整二挠 new 性。

置
$$
R_3=\sigma^3y,\qquad
D_9=\sigma^9y(X+4b)=[\delta]^*R_3+12bC_9.
\tag{E15}
$$
第二式用的是准确 $[\delta]^*R_3=C_9(X-8b)$。
$D_9$ 的质量为 $-1$，其奇 degree 标准半特征保留；
只有 $[2]^*D_9$ 才在下式作为 whole degree36 伙伴使用。

由(B8)–(B10)，原 T 可先写成
$$
T=A[\delta]^*B_{12}-6bNJ_{36}-504bNA.
$$
代入(B2)、(D10)，再用
$$
B_{12}+38bA_{12}-54b^2\sigma^{12}
=-[2]^*R_3-2bK_{12},
$$
得到完整来源身份
$$
\boxed{
T=-N[2]^*D_9-2b\mathcal P_{72}
-\frac1{63}[\delta]^*R_{24},
\qquad
\mathcal P_{72}:=N\bigl([\delta]^*K_{12}+252N\bigr).
}
\tag{E16}
$$
$\mathcal P_{72}$ 是原 whole degree72、型零、从第十二阶起的指定乘积。
(E2)使 $N[2]^*D_9$ 的整个二挠 trace 为零，
(E11)、(E13)、(E14)又处理(E16)其余两项。
因此
$$
\boxed{\mathrm T_{2,18}\mathcal P_{72}=0.}
\tag{E17}
$$
这不是把任意两个 new 来源的乘积认成 new；
它使用了原 T 的完整式和刚证明的(E11)。

另外，(D18)中的两个原乘积各有准确的核：
$$
\boxed{
\mathrm T_{2,18}\bigl(N[2]^*C_9\bigr)=0,\qquad
\mathrm T_{\delta,24}\bigl(N[\delta]^*K_{12}\bigr)=0.
}
\tag{E18}
$$
两式都来自完整投影公式，仍不等于它们的 $\mathfrak B$ 为零。

### E.5. 原 S/T 行中同一旧标量的准确消去

以(A7)的同一严格低卷积定义
$$
x_{N,p}=\mathscr X_p(N,[2]^*D_9),\qquad
x_{12,p}=\mathscr X_p(A_{12},B_{12}).
\tag{E19}
$$
这里 $\mathscr X_p$ 指显示的全部 $6\le r\le p-5$、
$r\equiv0\pmod6$ 的 $1/[r(r-1)]$ 加权和。
$[2]^*D_9$ 的质量为 $-1$，所以完整 Leibniz 的端项准确给
$$
\mathfrak B(N[2]^*D_9)=-\mathfrak B(N)+x_{N,p}.
$$
另有
$$
\mathfrak B(R_{24})=\mathfrak B(A_{12})+x_{12,p},\qquad
\mathfrak B(N)=\mathfrak B(S)+\mathscr X_p(S,\Theta)
+\frac1{21}\mathfrak B(A_{12}).
$$
最后一式直接来自 $A=S\Theta=N-[\delta]^*A_{12}/63$。
所有来源在被读取处质量零，倍点首位倍率准确为
$\delta^{p+1}\equiv3$；没有给任何热伙伴添中央零。

将这三式代入同一个(E16)，同一 $\mathfrak B(A_{12})$ 完全相消：
$$
\boxed{
2b\,\mathfrak B(\mathcal P_{72})
=\mathfrak B(S)-\mathfrak B(T)
+\mathscr X_p(S,\Theta)-x_{N,p}-\frac1{21}x_{12,p}
\pmod p.
}
\tag{E20}
$$
$\mathcal P_{72}$ 的实际首行也可原样写成
$$
\mathfrak B(\mathcal P_{72})
=\mathcal Q_p(N,[\delta]^*K_{12})
+252\mathcal Q_p(N,N).
\tag{E21}
$$
所以(D18)与(E20)确实在同一 $N,K_{12}$ 乘积上接合；
全 old 项已按其来源相消，没有靠环境维数删除。

在原 $S,T$ 的必要中央零下，(E20)右端只剩三个显示低卷积。
(E17)不使左端为零；(E18)也不允许删掉(D18)任一配对。
原 U 仍按(D16)、(D17)保其完整 new 余项与同 C8 运输。
本附录增加的是实际二挠核与同源旧标量的消元，
没有将这组派生恒等式当作第五条独立中央条件。

全文(E1)–(E21)为固定 whole 截面、完整四纤维 Newton 及
原首除 $p$ 乘积律的手证；没有新增数值执行。


## 附录 F. 两个原配对的完整双投影与 T 的同源旧项相消

本附录继续使用附录 E 的绝对 trace、原奇偶半特征及全部四纤维。
记 $N=N_{36}$，所有未标模 $p$ 的式均为特征零来源恒等式。
下文所谓“同时 new”准确指同一截面的完整二挠 trace 与范数三
trace 都为零；不包含对其 $\mathfrak B$ 读数的任何零断言。

### F.1. 同一个 N 平方的完整二挠迹

原 $N^2$ 在输入原点至少十二阶、在三个非零二挠点至少八阶消失。
故 whole degree18、型零的目标只能为
$\sigma^{18}(c_0+c_1X)$。
目标 $x=0$ 的全部四个逆像被原 $X(X-8b)$ 因子杀掉，
所以 $c_0=0$。

还须核 $c_1$。在目标非零二挠点 $a^3=-b$，
四个逆像的 $u=X/b$ 是
$$
u^2+20u-8=0
\tag{F1}
$$
的两个根，每个恰出现两次。
这是完整四次纤维
$(x^2-2ax-2a^2)^2=0$ 的 $X$ 值；
四点的规范 sigma 乘子仍由(C2)保留。
原实际商为
$$
\frac{N^2}{\sigma(2z)^{18}}
=\frac{X^2(X-8b)^2(X+4b)^2}
       {49\cdot2^{14}(X+b)^5}.
\tag{F2}
$$
在(F1)上，$(u-8)(u+4)=-24(u+1)$。
置 $v=(u+1)^{-1}$，两个 $v$ 满足
$27v^2-18v-1=0$，因而
$$
\sum v=\frac23,\qquad
\sum v^2=\frac{14}{27},\qquad
\sum v^3=\frac{10}{27}.
$$
(F2)除去固定非零倍率后的两根和是
$$
\sum\frac{u^2}{(u+1)^3}
=\sum(v-2v^2+v^3)=0.
$$
计入每根的重数二仍为零。
目标 $\sigma^{18}X$ 在该二挠点不为零，故
$$
\boxed{\mathrm T_{2,18}(N^2)=0.}
\tag{F3}
$$
这里使用的是原完整迹的剩余系数计算，
没有由 $N$ 的 new 性推任意乘积的 new 性。

### F.2. 同一平方的完整范数三旧部分

保持正文(5)–(6)的目标 $(a,c)$ 与三次纤维
$x^3+3ax^2+4b=0$。原 $N$ 的真实商可写成
$$
\frac{N/\sigma^{36}}{(\delta x)^{12}}
=\frac{4\delta}{567}\,ac\,\frac{y^3}{x^4}.
$$
平方以后，
$$
\frac{N^2/\sigma^{72}}{(\delta x)^{24}}
=-\frac{16a^2c^2}{49\cdot3^7}
\left(x+\frac{3b}{x^2}+\frac{3b^2}{x^5}+\frac{b^3}{x^8}\right).
\tag{F4}
$$
正文(17)已经支付所需的全部正、负幂迹：
$$
\begin{aligned}
\operatorname{Tr}x&=-3a,&
\operatorname{Tr}x^{-2}&=-\frac{3a}{2b},\\
\operatorname{Tr}x^{-5}&=\frac{15a}{16b^2},&
\operatorname{Tr}x^{-8}&=\frac{81a^4}{128b^4}-\frac{3a}{8b^3}.
\end{aligned}
$$
因此(F4)括号的完整迹恰为
$81a(a^3-8b)/(128b)$。
利用 $c^2=a^3+b$，在目标原坐标得到
$$
\boxed{
\mathrm T_{\delta,24}(N^2)=-\frac{R_{24}}{10584b},
\qquad R_{24}=\sigma^{24}X(X+b)(X-8b).
}
\tag{F5}
$$
特别定义
$$
Z_{72}^{\circ}:=N^2+\frac{[\delta]^*R_{24}}{31752b}.
\tag{F6}
$$
由于 trace-pull 的准确倍率为三，(F5)给范数三 trace 零；
(E13)–(E14)、(F3)给二挠 trace 零。
所以(F6)是同一平方的完整同时 new 部分。

### F.3. 原 P72 的参考项准确相消

由(E16)的定义及(F5)，
$$
\mathrm T_{\delta,24}\mathcal P_{72}
=-\frac{R_{24}}{42b}.
$$
将(E16)整个施以 $\mathrm T_{\delta,24}$，
使用正文(11)的原 $\mathrm T_{\delta,24}T=0$，
以及 $\mathrm T_{\delta,24}[\delta]^*R_{24}=3R_{24}$，
两项旧来源精确相消，得到
$$
\mathrm T_{\delta,24}\bigl(N[2]^*D_9\bigr)=0.
\tag{F7}
$$
又由 $D_9=[\delta]^*R_3+12bC_9$，
完整投影公式和 $N$ 的范数三 trace 零给
$$
\mathrm T_{\delta,24}\bigl(N[2]^*C_9\bigr)=0.
$$
另一方面，(E17)、(F3)直接给
$$
\mathrm T_{2,18}\bigl(N[\delta]^*K_{12}\bigr)=0.
$$
结合(E18)，得到原(D18)中两个指定乘积的完整结论：
$$
\boxed{
N[2]^*C_9\quad\text{与}\quad N[\delta]^*K_{12}
\quad\text{分别同时 new。}
}
\tag{F8}
$$
从而其原组合 $NJ_{36}$ 也同时 new。
这一步没有对低配对假设投影自伴性。

现在令
$$
\begin{aligned}
\mathcal P_{72}^{\circ}
&:=\mathcal P_{72}+\frac{[\delta]^*R_{24}}{126b}\\
&=N[\delta]^*K_{12}+252Z_{72}^{\circ}.
\end{aligned}
\tag{F9}
$$
它的两个完整迹均为零。
代回原(E16)，得到真实旧项已经相消的身份
$$
\boxed{T=-N[2]^*D_9-2b\mathcal P_{72}^{\circ}.}
\tag{F10}
$$
右端两项都是指定的同时 new 来源。
质量 $-1$ 的 $D_9$ 和原 $[2]$ 拉回全部保留；
不能把第一项改成两个质量零因子的配对。

### F.4. 第二原配对 NA 的完整二挠像

记实际 whole degree18 来源
$$
H_{18}:=\sigma^{18}X(X+4b).
\tag{F11}
$$
下面完整计算 $N[\delta]^*\sigma^{12}$，而不从环境维数赋值。
它在输入原点至少十八阶、非零二挠点至少四阶消失，
所以其 degree18、型零 trace 可写成
$\sigma^{18}(c_2X^2+c_1X+c_0)$。
目标 $x=0$ 的四个逆像仍被 $X(X-8b)$ 杀掉，故 $c_0=0$。

其原有理商是
$$
\frac{N[\delta]^*\sigma^{12}}{\sigma(2z)^{18}}
=\frac{2916}{7\cdot2^{18}}\,
 \frac{X^5(X-8b)(X+4b)}{(X+b)^7}.
\tag{F12}
$$
置 $f=X+b$，分子在 $f=0$ 的两首项准确为
$$
X^5(X-8b)(X+4b)=27b^7-129b^6f+O(f^2).
$$
使用(E6)–(E8)的同一完整逆根 Newton 迹，
$a^6$ 系数只来自 $f^{-7},f^{-6}$。
因此(F12)的完整最高系数为
$$
\frac{2916}{7\cdot2^{18}}
\left(\frac{64}{729b^4}\right)^2
\left(27b^7\,7\frac4{3b}-129b^6\cdot3\right)
=-\frac5{3024b^2}.
\tag{F13}
$$
没有其他正幂贡献：此处分子与分母同为七次，正幂商只是常数。

再在目标 $a^3=-b$ 读取(F12)。
沿(F1)，除去其固定倍率后的商为
$-24v(1-v)^5$，每个根仍出现两次。
同一二次递推进一步给
$$
\sum v^4=\frac{194}{729},\qquad
\sum v^5=\frac{418}{2187},\qquad
\sum v^6=\frac{2702}{19683},
$$
所以
$$
\sum v(1-v)^5=-\frac{1280}{19683}.
$$
计入全部四纤维及(F12)倍率，除去共同目标 $\sigma^{18}$ 后的迹值是 $5/1008$。
结合(F13)与 $c_0=0$，准确确定
$$
\boxed{
\mathrm T_{2,18}\bigl(N[\delta]^*\sigma^{12}\bigr)
=-\frac5{3024b^2}H_{18}.
}
\tag{F14}
$$
(F8)与 $K_{12}=9b\sigma^{12}-5A_{12}$ 随即给
$$
\mathrm T_{2,18}\bigl(N[\delta]^*A_{12}\bigr)
=-\frac{H_{18}}{336b}.
$$
最后用原 $A=N-[\delta]^*A_{12}/63$ 和(F3)，得到
$$
\boxed{
\mathrm T_{2,18}(NA)=\frac{H_{18}}{21168b},\qquad
\mathrm T_{\delta,24}(NA)=-\frac{R_{24}}{10584b}.
}
\tag{F15}
$$
第二式仍用同一个 $N$ 的完整投影公式。

这里两个旧部分没有交叉再生：
$$
\mathrm T_{\delta,6}H_{18}=0,\qquad
\mathrm T_{2,6}R_{24}=0.
\tag{F16}
$$
后式为(E13)；前式的真实商为
$-(1+4b/x^3)/27$，
而原三次纤维上 $\operatorname{Tr}x^{-3}=-3/(4b)$，
故全迹准确为零。
因此
$$
\boxed{
Q_{72}^{\circ}:=
NA-\frac{[2]^*H_{18}}{84672b}
+\frac{[\delta]^*R_{24}}{31752b}
}
\tag{F17}
$$
是第二原配对的指定同时 new 部分。
所有显示分母仅含固定坏素因子；特别 $b$ 仍为原单位，
无需增加目标素数的数值检查。

### F.5. 两实际配对及原 U 余项的准确读数范围

原 $Q_{1,p},Q_{2,p}$ 是附录 B 的同一完整
$1/[r(r-1)]$ 配对。
其两个因子均质量零，故它们等于对应乘积的首除 $p$ 行。
(F8)、(F15)–(F17)准确给
$$
\begin{aligned}
Q_{1,p}
&=2\mathfrak B\bigl(N[2]^*C_9\bigr)
  +\mathfrak B\bigl(N[\delta]^*K_{12}\bigr),\\
Q_{2,p}
&=\mathfrak B(Q_{72}^{\circ})
  +\frac{\mathfrak B(H_{18})}{21168b}
  -\frac{\mathfrak B(R_{24})}{10584b}
\pmod p.
\end{aligned}
\tag{F18}
$$
第一行的两个来源均同时 new；第二行的两个实际低 degree
旧读者已完整显示，没有赋值或删除。

(F10)的质量 $-1$ 端项给
$$
\boxed{
2b\,\mathfrak B(\mathcal P_{72}^{\circ})
=\mathfrak B(N)-\mathfrak B(T)
-\mathscr X_p(N,[2]^*D_9)
\pmod p.
}
\tag{F19}
$$
它与(E20)完全相容，因为
$\mathfrak B(\mathcal P_{72}^{\circ})
=\mathfrak B(\mathcal P_{72})+\mathfrak B(R_{24})/(42b)$。
原 $T$ 中被消掉的是同一 $[\delta]^*R_{24}$ 来源；
没有因此删除 $\mathfrak B(A_{12})$、$\mathfrak B(H_{18})$
或任一 new 读者。

原 U 的剩余行仍是(D17)的同一个
$\mathcal U_{144}^{\mathrm{new}}$：
$$
9828\bigl(
\mathfrak B(U)+\mathscr X_p(U,\Theta^4)
-\mathfrak B(\mathcal U_{144}^{\mathrm{new}})\bigr)
=3\mathfrak B(K_{12})-\mathfrak B(J_{36}).
\tag{F20}
$$
特别(F8)并不使(F20)右边为零，也不把
$\mathfrak B(J_{36})$ 变成 $\mathfrak B(NJ_{36})$。
在原四个必要中央零下，可删除的仍只有原
$\mathfrak B(S),\mathfrak B(T),\mathfrak B(U),\mathfrak B(V)$；
(F18)–(F20)的全部显示伙伴与余项保留。
本附录所付的新内容是两个原配对的完整双投影及
(F10)的同源旧项相消，不是第五条中央条件。

约化前始终保 $2^{p+1}$、$\delta^{p+1}$ 及原固定整提升；
(F18)–(F20)只在原首位使用它们的剩余值四、三。
全文为完整纤维、Newton 递推和原投影公式的手证，
没有新数学数值执行。


## 附录 G. 原 U 余项的非零质量与 S/T/V 的完整同时 new 条件

本附录仍使用原 $\mathcal U_{144}^{\mathrm{new}}$，
而不以相同 degree 或相同 trace 核中的另一来源代替它。
全部来源的 trace 先在特征零形成；
涉及 $\mathcal D$ 时，始终使用 R856 的原特征零 Hasse 提升。

### G.1. 同一个 C9 的范数三旧部分

对(D9)的 $C_9=\sigma^9y$，由正文(5)准确有
$$
\frac{C_9/\sigma^9}{(\delta x)^3}
=\frac{c}{X-8b}.
$$
在原三次纤维 $x^3+3ax^2+4b=0$ 上，
$$
\operatorname{Tr}\frac1{X-8b}
=-\frac13\operatorname{Tr}\frac1{ax^2+4b}
=-\frac1{4b}.
$$
第二个完整迹可由同一三次 Newton 公式或商代数直接求得，
并与 R879(C6)所用恒等式一致。
所以
$$
\boxed{
\mathrm T_{\delta,3}C_9=-\frac{R_3}{4b},
\qquad R_3=\sigma^3y,\qquad
\mathrm T_{\delta,3}D_9=0.
}
\tag{G1}
$$
最后一式使用原(E15)的
$D_9=[\delta]^*R_3+12bC_9$。
这还明确了 $D_9$ 的质量 $-1$ 与范数三 new 性可以同时成立；
不能从 new 性推质量为零。
$R_3,C_9,D_9$ 的奇 degree 标准半特征全部保留。

### G.2. 原 U 的指定 degree48 来源与两个准确边界

定义同一个完整原输入的迹
$$
Q_{48}:=\mathrm T_{\delta,48}(U\Theta^4).
\tag{G2}
$$
在 $E[\delta]$ 的三个原输入点，$U\Theta^4$ 都至少六阶消失：
原点使用原 $U$ 的六阶零；
另两点为 $x=0$，原(C5)的 $x^2$ 与 $\Theta^4=x^4\sigma^8$
分别给二阶、四阶零。
canonical 局部倍率为单位，故
$$
Q_{48}=\sigma^{48}q_b(X),\qquad
q_b(X)=\sum_{j=0}^7 q_jb^{7-j}X^j,\qquad Q_{48}(0)=0.
\tag{G3}
$$
式末的 $Q_{48}(0)$ 是原 $z=0$ 处的质量；
下文 $q_b(0)$ 则是有理系数在 $X=0$ 的值，二者不混用。

原输入的完整三纤维公式为
$$
\boxed{
\frac{Q_{48}}{\sigma^{48}}
=\frac1{91\cdot3^{24}}\,
 \operatorname{Tr}
 \frac{(X+b)Q_7(X)A_2(X)F_4(X)G_4(X)H_8(X)}
      {X^{14}},
}
\tag{G4}
$$
其中全部三个 $X$ 满足
$$
(X+4b)^3+27a^3X^2=0.
\tag{G5}
$$
(G4)来自原 $U\Theta^4=\sigma^{144}X^2(X+b)Q_7A_2F_4G_4H_8/91$
和准确 $(\delta x)^{48}=3^{24}X^{16}$；
不是只用目标 degree 恢复的拟合公式。
(G5)及其倒数三次式给全部 $-14\le k\le7$ 的 Newton 幂和，
因此(G4)已经指定整个 $q_b$。完整结果为
$$
\boxed{
\begin{aligned}
6552q_b(X)={}&-245X^7+11074bX^6+28416b^2X^5
+7328b^3X^4\\
&+69248b^4X^3+7680b^5X^2-20480b^6X-8192b^7.
\end{aligned}}
\tag{G4a}
$$
这不是由(G3)的两个边界拟合：公开 Fraction producer
对(G4)的全部正、负幂逐项求迹，使用全部原(C5)–(C6)因子。
该完整结果及运行来源列在本附录末尾。

例如目标 $a=0$ 时，三个输入的 $X$ 都为 $-4b$。
在这个实际值，
$$
\begin{aligned}
Q_7&=2^4 3^2b^2,& A_2&=-2^3 3^2b^2,\\
F_4&=G_4=2^8 3^4b^4,& H_8&=-2^{15}3^8b^8 .
\end{aligned}
$$
直接代入(G4)，包含三个原纤维的重数，得
$$
\boxed{q_b(0)=-\frac{1024}{819}b^7.}
\tag{G6}
$$
它在原好特征下为单位，尤其 $Q_{48}$ 确是非零来源。
本式不将该来源边界当作其 $\mathfrak B$ 非零。

现在取原(D14)的同一个余项，令
$$
W_{48}:=\mathrm T_{\delta,48}\mathcal U_{144}^{\mathrm{new}}.
$$
由(D14)、(G1)及 canonical 两倍点交换，
$$
\boxed{
W_{48}=Q_{48}-\frac{[4]^*R_3}{78624b}.
}
\tag{G7}
$$
若要直接在原多项式模型中读取同一来源，准确倍点公式还给
$$
[4]^*R_3=-\sigma^{48}K_8,\qquad
K_8=X^2(X-8b)^6+1280bX(X-8b)^3(X+b)^3
-32768b^2(X+b)^6.
\tag{G7a}
$$
所以 $W_{48}=\sigma^{48}(q_b+K_8/(78624b))$，
并保完整七次与八次项。
因为 $R_3(0)=-1$，这个真实迹的质量准确是
$$
\boxed{W_{48}(0)=\frac1{78624b}.}
\tag{G8}
$$
它不是一个中心零的派生来源。

全部二挠返回也保持相容：
由(C4)、(D9)、(G1)，
$$
\mathrm T_{2,12}Q_{48}
=\frac{[2]^*R_3}{19656b}
=-\frac{\sigma^{12}A_2}{19656b},
\qquad
\mathrm T_{2,12}W_{48}=0.
\tag{G9}
$$
这里用了
$\mathrm T_{\delta,12}\mathcal H_{36}
=[2]^*R_3/(157248b^2)$，
以及同一规范 $\mathrm T_{2,12}[4]^*R_3=4[2]^*R_3$。
因此原 $U$ 的这个实际余项确实返回到一个
质量非零而二挠 new 的 whole degree48 来源，
不是从它的环境中另选的向量。

### G.3. 不能省略的质量 Hasse 项与准确除 p 行

以下固定原 $p=6s-1>211$。
记 R856 的实际特征零提升为
$$
\widehat c_p=(L_2H_p)|_{\rm CM}
=(p+1)c_p^{\mathrm{int}},\qquad
c_p^{\mathrm{int}}=\binom{3s-1}{2s-1}b^s .
$$
$c_p$ 为其模 $p$ 单位；先除 $p$ 后约化。
不能在减项中把 $\widehat c_p$ 换成
$c_p^{\mathrm{int}}$，二者的差除 $p$ 后一般不为零。
由于 $H_p|_{\rm CM}=0$，(G8)与 whole degree48 递推准确给
$$
\boxed{
j_{p+1}(W_{48})\equiv
48c_pW_{48}(0)=\frac{c_p}{1638b}\ne0\pmod p.
}
\tag{G10}
$$
所以此处的原整读者必须是
$$
\boxed{
\mathcal D_{48,p,1}(W_{48})
=\frac{j_{p+1}(W_{48})-\widehat c_p/(1638b)}p.
}
\tag{G11}
$$
不能把它写成中心零来源的裸 $j_{p+1}/p$。

为完整处理(G7)的实际旧项，定义
$$
D_{R_3,p}:=\frac{j_{p+1}(R_3)+3\widehat c_p}{p}.
\tag{G12}
$$
本式的整性不借一个未支付的奇 degree 普遍定理。
事实上 $[4]^*R_3$ 是原 whole degree48 截面；
其质量为 $-1$，且
$j_k([4]^*R_3)=4^k j_k(R_3)$。
用 R856 及单位 $4^{p+1}$ 可直接推出(G12)整。
更准确地，置 $q_p(4)=(4^{p-1}-1)/p$，则特征零全式为
$$
\mathcal D_{48,p,1}([4]^*R_3)
=4^{p+1}D_{R_3,p}-48\widehat c_pq_p(4).
\tag{G13}
$$
这里 $R_3$ 的实际半特征、质量和全部 $p$ 高位都已固定。

由于(G3)的 $Q_{48}$ 严格中心零，(G7)、(G11)逐项给
$$
\begin{aligned}
\mathcal D_{48,p,1}(W_{48})
={}&\mathfrak B(Q_{48})
-\frac{4^{p+1}}{78624b}D_{R_3,p}
+\frac{\widehat c_p}{1638b}q_p(4),\\
\equiv{}&
\mathfrak B(Q_{48})
-\frac{D_{R_3,p}}{4914b}
+\frac{c_p}{819b}q_p(2)\pmod p .
\end{aligned}
\tag{G14}
$$
第一行中 $\mathfrak B(Q_{48})$ 表示其准确整商
$j_{p+1}(Q_{48})/p$；第二行才取模 $p$。
这保留了与原 $[4]$ 拉回配套的全部 Fermat 缺陷。
不假设 $q_p(2)$ 非零，也不以(G10)的单位断言
(G11)或 $\mathfrak B(Q_{48})$ 非零。

(G10)给的是一个实际未除 $p$ 的非零读数：
它说明原 $U$ 余项的该返回必须带(G11)的非齐次减项。
原 $\mathfrak B(U)=0$ 不使
$\mathcal D_{48,p,1}(W_{48})$ 或 $\mathfrak B(Q_{48})$ 为零，
也没有证明 $\mathfrak B$ 与本 canonical trace 可直接交换。

### G.4. 同一 V 来源的两个旧部分与原 S/T/V 条件

附录 B 的原全来源式是
$$
V\Theta^3-T=2bNJ_{36}+504bNA.
$$
应用(F8)、(F15)及原 $T$ 的两个 trace 零，准确得到
$$
\boxed{
\mathrm T_{2,18}(V\Theta^3)=\frac{H_{18}}{42},
\qquad
\mathrm T_{\delta,24}(V\Theta^3)=-\frac{R_{24}}{21}.
}
\tag{G15}
$$
因此原固定截面
$$
V_{72}^{\circ}:=
V\Theta^3-\frac{[2]^*H_{18}}{168}
+\frac{[\delta]^*R_{24}}{63}
\tag{G16}
$$
同时 new，并且满足完整身份
$$
\boxed{
V_{72}^{\circ}-T=2bNJ_{36}+504bQ_{72}^{\circ}.
}
\tag{G17}
$$
这次被运输的是原 $V$，所有伙伴与 $[2]$、$[\delta]$ 倍率都有来源，
而非任意选择一个 degree72 中心零截面。

记
$$
x_S=\mathscr X_p(S,\Theta),\quad
x_V=\mathscr X_p(V,\Theta^3),\quad
x_U=\mathscr X_p(U,\Theta^4),\quad
x_N=\mathscr X_p(N,[2]^*D_9).
$$
在原四个必要中央零
$\mathfrak B(S)=\mathfrak B(T)=\mathfrak B(U)=\mathfrak B(V)=0$
下，已经支付的实际条件可并列写成
$$
\boxed{
\begin{aligned}
2b\,\mathfrak B(\mathcal P_{72}^{\circ})
&=x_S+\frac{\mathfrak B(A_{12})}{21}-x_N,\\
2b\,Q_{1,p}+504b\,\mathfrak B(Q_{72}^{\circ})
&=x_V-\frac{\mathfrak B(H_{18})}{42}
       +\frac{\mathfrak B(R_{24})}{21},\\
9828\bigl(x_U-\mathfrak B(\mathcal U_{144}^{\mathrm{new}})\bigr)
&=3\mathfrak B(K_{12})-\mathfrak B(J_{36}).
\end{aligned}}
\tag{G18}
$$
同时 $\mathfrak B(R_{24})=\mathfrak B(A_{12})+
\mathscr X_p(A_{12},B_{12})$，所以第一、二行的旧标量仍可按同源消去。
(G14)则是第三行同一 $U$ 余项取实际 trace 后所须保留的整读者，
不额外添加一个零方程。

至此原 $S/T/V$ 的两项配对和原 $U$ 的余项均在确定的
来源／投影／质量规范内：
(G17)保两项同时 new 的全部读数，
(G10)–(G14)保原 $U$ 余项返回时确实非零的质量及其 Hasse 减项。
尚未支付的仍是这些指定整余项之间能排除四原首行同时为零的关系；
不能把本附录的迹或单位质量代作额外算术中央条件。

### G.5. 全八系数的精确算法与公开执行来源

为直接复现(G4a)，固定 $b=1$，令 $A=a^3$，
$c=12+27A$，$s_j=\operatorname{Tr}X^j$。
完整正幂初值与递推为
$$
s_0=3,\quad s_1=-c,\quad s_2=c^2-96,\qquad
s_j=-cs_{j-1}-48s_{j-2}-64s_{j-3}\quad(j\ge3).
$$
令 $v_j=s_{-j}$，则原倒数多项式为
$u^3+3u^2/4+cu/64+1/64=0$，因此
$$
v_0=3,\quad v_1=-\frac34,\quad
v_2=\frac3{16}-\frac{27A}{32},\qquad
v_j=-\frac34v_{j-1}-\frac c{64}v_{j-2}-\frac1{64}v_{j-3}.
$$
把原二十一次多项式
$(X+1)Q_7A_2F_4G_4H_8=\sum_{i=0}^{21}P_iX^i$
逐项代入
$$
q_1(A)=\frac1{91\cdot3^{24}}\sum_{i=0}^{21}P_i s_{i-14}
$$
便得到(G4a)，这里下标一仅表示 $b=1$。
原齐次权再恢复一般 $b$ 的 $b^{7-j}$。

这一完整 Fraction 算法已经公开执行，且同一次运行独立使用
原(C7)的全部四纤维再次核定(G9)，没有只核两个边界：

- run 43870426107，job 133309825034；
- source commit d5e37c59b7c93488772d4319e41d9a55a4429bde；
- 脚本：[check-r884-original-u-theta4-norm-three-trace.py](../scripts/check-r884-original-u-theta4-norm-three-trace.py)，无参数，Python 标准库 Fraction；
- script SHA256：a943b4c799af265c703248ee9cf5abffe0b571023e534ddbef69ba4fe9d160fb；
- RANK2_U_THETA4_DELTA_RESULT SHA256：5e2e9bdafb00b70178499294aba0ff58588000a6fd7f748815440595d970b71b。

没有提交可重算输出文件，也没有目标素数扫描。
(G3)、(G6)、(G8)–(G18)的来源、质量、整性及全部减项由上面的
全纤维和 whole Hurwitz 证明独立支付；
(G4a)进一步固定了同一实际来源的全部系数。


## 附录 H. 原纯 sigma 参考的低配对与同 U 余项的完整质量补偿

本附录只继续读取(G7)的原 $W_{48}$。
下列中心补偿始终显写为同一来源的差；
它不为补偿后的截面添加中央零，也不把(G11)的原质量减项删除。

### H.1. 已付全来源中的准确因子

用(G4a)、(G7a)完整多项式相加并除以 $X+4b$，准确得到
$$
\boxed{
W_{48}=[\delta]^*\Theta\,W_{42},\qquad
W_{42}=\frac{\sigma^{42}}{78624b}\,L_7(X),
}
\tag{H1}
$$
其中
$$
\begin{aligned}
L_7={}&X^7-1712bX^6+81048b^2X^5-32608b^3X^4\\
&-220672b^4X^3-397824b^5X^2-266240b^6X-32768b^7.
\end{aligned}
\tag{H2}
$$
因为 $[\delta]^*\Theta=\sigma^6(X+4b)$，直接乘回(H2)
恢复公开完整八次多项式，故(H1)没有遗漏低端。
$W_{42}$ 的质量仍为 $1/(78624b)$；
不能将(H1)的质量一因子视作 $p$ 次幂而穿过 Cartier。

置以下原固定 sigma 来源：
$$
v=\sigma^6,\qquad u=-R_3=-\sigma^3y,\qquad u(0)=1.
\tag{H3}
$$
它们满足完整身份
$$
u^2=\Theta^3+bv,\qquad
[\delta]^*v=-27v\Theta^6,\qquad
[2]^*v=64vu^6.
\tag{H4}
$$
这些式子均由原 $\sigma(\delta z)=\delta x\sigma^3$、
$\sigma(2z)=-2y\sigma^4$ 和 $y^2=X+b$ 直接得到。
$u$ 的奇 degree 标准半特征保留；
(H4)中的 $u^6,u^{12},u^{16}$ 都是实际偶 degree whole 来源。

### H.2. 原 sigma 六次、十二次参考的真正严格低窗口

以下仍取 $p=6s-1>211$，
$\mathscr X_p$ 为(A7)的全部严格低于 $p$ 的实际配对。
$ v,\sigma^{12}$ 的质量严格为零，而
$\Theta^6,u^6,\Theta^{12},u^{12}$ 的质量均为一；
所有一阶 jet 为零。
因此(H4)用完整 Leibniz 给
$$
\begin{aligned}
3\mathfrak B(v)&=-27\bigl(\mathfrak B(v)+
              \mathscr X_p(v,\Theta^6)\bigr),\\
4\mathfrak B(v)&=64\bigl(\mathfrak B(v)+
              \mathscr X_p(v,u^6)\bigr).
\end{aligned}
$$
得到
$$
\boxed{
\mathfrak B(\sigma^6)
=-\frac9{10}\mathscr X_p(\sigma^6,\Theta^6)
=-\frac{16}{15}\mathscr X_p(\sigma^6,u^6)
\pmod p.
}
\tag{H5}
$$
这里原 norm-three 和倍点首位倍率分别为三、四；
右端的 $-27,64$ 是来源身份中的固定绝对常数，
不能将这两类倍率混同。

平方(H4)，同理有
$$
\boxed{
\begin{aligned}
\mathfrak B(\sigma^{12})
&=\mathcal Q_p(\sigma^6,\sigma^6)\\
&=-\frac{243}{242}\mathscr X_p(\sigma^{12},\Theta^{12})
=-\frac{1024}{1023}\mathscr X_p(\sigma^{12},u^{12})
\pmod p.
\end{aligned}}
\tag{H6}
$$
这使用准确 $[\delta]^*\sigma^{12}=729\sigma^{12}\Theta^{12}$、
$[2]^*\sigma^{12}=4096\sigma^{12}u^{12}$。
显示分母的素因子至多三十一，均在原范围内为单位。

(H5)、(H6)给原参考的完整低配对表达，
没有证明其中任一配对非零。
在模 $p$ 以前，左端的 multiplier 仍是
$\delta^{p+1}$、$2^{p+1}$；
由于此处被搬运的输入严格中心零，
没有遗漏一个质量 Hasse 项或先将其除 $p$。

### H.3. 同一个 Q48 与 U 返回的准确中心补偿

(G3)、(G4a)给实际整除
$$
Q_{48}=v\,A_{42},\qquad
A_{42}:=\sigma^{42}q_b(X),\qquad
A_{42}(0)=-\frac{35}{936}.
\tag{H7}
$$
$A_{42}$ 是 whole degree42 的确定截面，
不是只保同质量的替代函数。
将(H5)代入完整乘积律，得到
$$
\boxed{
\mathfrak B(Q_{48})
=\mathscr X_p(v,A_{42})
+\frac7{208}\mathscr X_p(v,\Theta^6)
\pmod p.
}
\tag{H8}
$$
两个右端都只读原低于 $p$ 的 jets，
所以(G14)的同一 $Q_{48}$ 高标量在此已经被准确消去。

对(G8)的质量，使用(H3)中同一个真实 $u$，
定义完整差
$$
W_{48}^{0}:=W_{48}-\frac{u^{16}}{78624b}.
\tag{H9}
$$
因为 $u^{16}=\sigma^{48}(X+b)^8$，其八次最高项恰与
$W_{48}$ 的最高项相消。因此存在实际 whole degree42 来源
$$
\boxed{
W_{48}^{0}=v\,A_{42}^{0},\qquad
A_{42}^{0}
=\frac{\sigma^{42}}{78624b}
 \bigl((X+4b)L_7(X)-(X+b)^8\bigr).
}
\tag{H10}
$$
括号的 degree 至多七。其七次系数为 $-1716b$，
所以准确质量为
$$
A_{42}^{0}(0)=-\frac{11}{504}.
$$
没有从八次式中丢掉有限点的极；
(H10)在全部原椭圆曲线上都是 whole 截面。

再次使用同一(H5)，得到
$$
\boxed{
\mathfrak B(W_{48}^{0})
=\mathscr X_p(v,A_{42}^{0})
+\frac{11}{560}\mathscr X_p(v,\Theta^6)
\pmod p.
}
\tag{H11}
$$
(H8)、(H11)给的是(G2)、(H9)两个指定来源的读数；
不能以它们具有相同的 $\sigma^6$ 因子就将两个配对相认。

### H.4. 原未补偿 D1 中必须保留的同一参考行

(G12)已经通过实际 $[4]$ 拉回支付
$D_{R_3,p}=(j_{p+1}(R_3)+3\widehat c_p)/p$ 的整性，
其中仍为原
$\widehat c_p=(p+1)c_p^{\mathrm{int}}$。
对 $u=-R_3$，相应整行是 $-D_{R_3,p}$。
明确对每个实际整数 $a\ge1$ 置
$d_a=(j_{p+1}(u^a)-3a\widehat c_p)/p$。
$u^a(0)=1$、$j_1(u^a)=0$；完整 Leibniz 的零阶与
$p+1$ 阶两端给 $d_a+d_1$，一阶与 $p$ 阶两端准确为零。
质量减项逐字满足
$3(a+1)\widehat c_p=3a\widehat c_p+3\widehat c_p$，
故其余严格低项给
$d_{a+1}=d_a+d_1+\mathscr X_p(u^a,u)\bmod p$。
从 $d_1=-D_{R_3,p}$ 归纳支付全部中间整性，得到
$$
\mathcal D_{48,p,1}(u^{16})
=-16D_{R_3,p}+\Gamma_{16,p}\pmod p,\qquad
\Gamma_{16,p}:=\sum_{a=1}^{15}\mathscr X_p(u^a,u).
\tag{H12}
$$
即使中间 degree 为奇数，其整性也由这个实际乘法归纳支付；
没有调用一个未证明的奇 degree 普遍定理。
每个 $\mathscr X_p$ 仍为全部 $6\le r\le p-5$、
$r\equiv0\pmod6$ 的严格低窗口。

因此(H9)在原完整整读者上准确是
$$
\boxed{
\mathcal D_{48,p,1}(W_{48})
=\mathfrak B(W_{48}^{0})
-\frac{D_{R_3,p}}{4914b}
+\frac{\Gamma_{16,p}}{78624b}
\pmod p.
}
\tag{H13}
$$
这条式子保留了原未补偿来源的质量一参考行。
联立(G14)，同一个参考行被合法消掉，得到
$$
\boxed{
\mathfrak B(W_{48}^{0})
=\mathfrak B(Q_{48})
+\frac{c_p}{819b}q_p(2)
-\frac{\Gamma_{16,p}}{78624b}
\pmod p.
}
\tag{H14}
$$
将(H8)、(H11)代入后，(H14)是同一个原 U 返回的
全低配对相容式；没有高 $\Theta$ 商、未说明的
$\sigma^{12}$ 高标量或被丢弃的质量减项。
它也没有将 $q_p(2)$ 预设为非零。

(H9)是完整来源补偿，不能用
$\mathfrak B(U)=0$ 推出 $\mathfrak B(W_{48}^{0})=0$。
原 $S/T/V$ 与 $U$ 的必要条件仍为(G18)，
并继续保留其实际同时 new 余项和全 cross。
本附录净消掉的是(G14)中
$\mathfrak B(Q_{48})$ 及补偿后的高读者，
把它们都写成(H8)、(H11)的同来源严格低配对；
它未证明这些低配对不可能满足原四中央条件。

全部(H1)–(H14)为已公开(G4a)全系数、
固定 sigma 倍点身份及原整首行的手推；
没有新数值运行或目标素数扫描。
