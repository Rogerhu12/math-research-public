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
