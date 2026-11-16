# R877 — 原 C30 的范数三消失、C24 三列投影与 H22 的实际伙伴

日期：2026-11-16。本文只用原固定 sigma 来源与 $[\delta]$ 的完整三点纤维，给出其绝对 trace／投影。所有等式先在特征零成立。它们不把原首除 $p$ 读数当作与 trace 无修正交换的泛函。

## 1. 同一个标准 theta 覆盖

沿用
$$
y^2=x^3+b,\quad X=x^3,\quad Dx=2y,\quad
\delta=1+2\omega,\quad\delta^2=-3,\quad b\ne0.
$$
原绝对除法恒等式与坐标是
$$
\sigma(\delta z)=\delta x\sigma(z)^3,\qquad
x_\delta=-\frac{X+4b}{3x^2},\qquad
y_\delta=-\frac{y(X-8b)}{3\delta X}.
\tag{1}
$$
特别 $\sigma(\delta z)/\sigma(z)^3$ 是准确的 $\delta x$，
不是只到一个未定常数的除法函数。

对 whole degree $3m$ 截面 $A=\sigma^{3m}R$，定义原 theta 结构中的推前
$$
\mathrm T_{\delta,m}(A)
=\sigma(w)^m\operatorname{Tr}_{K(E)/\delta^*K(E)}
\frac{R}{(\delta x)^m},
\qquad w=\delta z.
\tag{2}
$$
它把 whole 截面送到 whole degree $m$ 截面。
固定除法函数给了实际线丛同构，故这里无需另猜半特征或准周期倍率。

更具体地，令 $r=A/\sigma(\delta z)^m$。
对于 $T\in E[\delta]$，实际 deck 提升为
$$
\mathcal T_T^{(3m)}A(z)
=\sigma(\delta z)^m\,r(z+T).
\tag{3}
$$
$r$ 是椭圆有理函数，所以 (3) 不依赖 $T$ 的周期代表；
所有准周期相位已经在这个商中保留。它满足群律，且不同 degree 的乘法相容。
因此
$$
\Pi_{\delta}^{(3m)}
=\frac13[\delta]^*\mathrm T_{\delta,m}
=\frac13\sum_{T\in E[\delta]}\mathcal T_T^{(3m)}
\tag{4}
$$
是准确幂等投影。若 $B$ 是原 degree $n$ 截面，则有完整投影公式
$$
\mathrm T_{\delta,m+n}(A\,[\delta]^*B)
=B\,\mathrm T_{\delta,m}(A).
\tag{5}
$$
本文所有“范数三消失”均指 (2) 为零，不把其它平移规范代入 (4)。

## 2. 三点纤维与共享奇来源

在目标坐标 $(a,c)=(x_\delta,y_\delta)$ 上，完整纤维由
$$
x^3+3ax^2+4b=0,\qquad
y=-\frac{3\delta Xc}{X-8b}
\tag{6}
$$
给出。三根的幂和准确为
$$
\operatorname{Tr}x=-3a,\qquad
\operatorname{Tr}x^{-2}=-\frac{3a}{2b},\qquad
\operatorname{Tr}x^{-5}=\frac{15a}{16b^2}.
\tag{7}
$$
例如逆根满足
$u^3+(3a/(4b))u+1/(4b)=0$，Newton 递推直接给后两式。
计算先在非退化纤维上进行，再由有理函数恒等式延拓。

记
$$
Q_7=7X^2-4bX+16b^2,\qquad
F_6=\sigma^6(X-8b),\qquad
C_{24}=-\frac{\sigma^{24}x^2yQ_7}{7}.
$$
原共享奇来源为
$$
C_{30}=C_{24}F_6
=-\frac{\sigma^{30}x^2yQ_7(X-8b)}7.
\tag{8}
$$
它从 $z^5$ 起，首系数为一。若 $\gamma=3+\omega$，则同一绝对来源还可写为
$$
C_{30}
=-\frac{\sigma(\gamma z)\sigma(\bar\gamma z)
 \sigma(z)\sigma(\delta z)\sigma(2\delta z)}{42}.
\tag{9}
$$
式(9)由原
$\sigma(\gamma z)\sigma(\bar\gamma z)=\sigma^{14}Q_7$
以及
$\sigma(2\delta z)=-2\delta xy(X-8b)\sigma^{12}$
直接得到；五个因子的 leading product 为 $-42z^5$。

将 (8) 除以 $\sigma(\delta z)^{10}$ 并用 (6)，得到
$$
\frac{C_{30}}{\sigma(\delta z)^{10}}
=\frac{3\delta^{-9}c}{7}
  \left(7x-4b x^{-2}+16b^2x^{-5}\right).
\tag{10}
$$
完整迹的括号是
$-21a+6a+15a=0$。所以
$$
\boxed{\mathrm T_{\delta,10}C_{30}=0,\qquad
       \Pi_\delta^{(30)}C_{30}=0.}
\tag{11}
$$
这是原 $C_{30}$ 自身的全三纤维关系。

原两个中央来源保持
$$
S=C_{30}\frac{\sigma(2z)}2,\qquad
V=C_{30}\frac{\sigma(6z)}6.
\tag{12}
$$
由于 $6=(-2\delta)\delta$，$\sigma(6z)$ 准确等于
$[\delta]^*(\sigma(-2\delta z))$，目标因子 degree12。
由 (5) 得
$$
\boxed{\mathrm T_{\delta,22}V=0,\qquad
       \Pi_\delta^{(66)}V=0.}
\tag{13}
$$
相反，$\sigma(2z)$ 不在此式中被认作一个 $\delta$-pullback；
(11) 不给原 $S$ 同样的投影消失。

## 3. 原 C24 三列的完整有限行

固定原三列和原指定向量
$$
E_j=-b^j\sigma^{24}x^{8-3j}y,\quad 0\le j\le2,\qquad
c_*=(1,-4/7,16/7)^{\mathsf t},
\quad C_{24}=\sum_jc_{*,j}E_j.
\tag{14}
$$
式(6)还给
$$
\operatorname{Tr}\frac1X=-\frac3{4b},\qquad
\operatorname{Tr}\frac1{X-8b}=-\frac1{4b}.
\tag{15}
$$
第二式可直接核：三根的平方具有初等对称式
$9a^2,-24ab,16b^2$，故
$$
\sum_i\frac1{a x_i^2+4b}
=\frac{48b(b+a^3)}{64b^2(b+a^3)}
=\frac3{4b},
$$
再用 $X_i-8b=-3(ax_i^2+4b)$。因此不是以一个边际值替代完整纤维。

对 $E(c)=\sum c_jE_j$，准确有
$$
\boxed{
\mathrm T_{\delta,8}E(c)
=-\frac{1}{9\delta}
 \left(c_0-\frac{c_1}4+\frac{c_2}{16}\right)\sigma^8y,
}
\tag{16}
$$
以及
$$
\boxed{
\mathrm T_{\delta,10}\bigl(F_6E(c)\bigr)
=-\frac{1}{9\delta}
 \left(c_0+\frac{c_1}2-\frac{5c_2}{16}\right)\sigma^{10}xy.
}
\tag{17}
$$
第一式用
$b^j\operatorname{Tr}(X^{1-j}/(X-8b))
=(1,-1/4,1/16)$；
第二式用 (7)。
两个绝对倍率相同，因为 $3\delta^{-7}=-9\delta^{-9}=-1/(9\delta)$。

将 (16) 拉回，得到原三维空间上的完整投影矩阵
$$
\boxed{
\Pi_\delta^{(24)}
=\frac13
\begin{pmatrix}1\\-8\\0\end{pmatrix}
\begin{pmatrix}1&-1/4&1/16\end{pmatrix}.
}
\tag{18}
$$
行列相乘为三，故幂等性也可直接核。对原 $C_{24}$，
$$
\Pi_\delta^{(24)}C_{24}
=\frac37(E_0-8E_1),
\qquad
(I-\Pi_\delta^{(24)})C_{24}
=\frac47(E_0+5E_1+4E_2).
\tag{19}
$$
第二项准确为
$-(4/7)\sigma^{24}x^2y(X+b)(X+4b)$，不能省掉。

R863(A6) 的实际算术参考平面是
$$
-4c_0+c_1+2c_2=0.
$$
在这个同一平面内，(17) 的消失条件唯一留下原直线 $Kc_*$。
这是两个固定线性方程的直接联立。
旧 $D_{\rm ref}$ 在三列中的向量是 $(5,28,-4)$，其 (17) 括号为 $81/4$，
所以它不满足这条完整消失关系。
这只定位原参考来源，并未增加一个中央条件。

若回到原 $V=C_{24}J_V$，式(13)仍必须写成
$$
0=\frac13\sum_{T\in E[\delta]}
 (\mathcal T_T^{(24)}C_{24})(\mathcal T_T^{(42)}J_V).
\tag{20}
$$
不能把 (20) 拆成两个独立边际的消失；(19) 的两个部分都仍在真实乘积中。

## 4. 同一个 H22 的实际旧／新伙伴分解

R863(A20) 的实际伴随还给
$$
K_{30}:=\sigma(2z)^2H_{22}
=4\sigma^{30}X(X+b)(65X^2-380bX+464b^2),
\qquad C_0=-\frac{\sigma(2z)K_{30}}{21312}.
\tag{21}
$$
这里使用的是原 $H_{22}$，没有在其四维 CM 空间中改选输入。
由逆根 Newton 公式，
$$
\operatorname{Tr}x^2=9a^2,\quad
\operatorname{Tr}x^{-1}=0,\quad
\operatorname{Tr}x^{-4}=\frac{9a^2}{8b^2},\quad
\operatorname{Tr}x^{-7}=-\frac{63a^2}{64b^3}.
$$
而
$$
\frac{K_{30}}{\sigma(\delta z)^{10}}
=4\delta^{-10}
(65x^2-315b x^{-1}+84b^2x^{-4}+464b^3x^{-7}).
$$
括号的迹为 $891a^2/4$，$\delta^{10}=-243$。
因此
$$
\boxed{\mathrm T_{\delta,10}K_{30}
=-\frac{11}{3}\sigma^{10}x^2.}
\tag{22}
$$
特别它与 (11) 是不同的真实来源关系。

令 $B_{10}=\sigma^{10}x^2$。原拉回为
$$
[\delta]^*B_{10}=-27\sigma^{30}X^2(X+4b)^2.
$$
所以完整分解是
$$
\begin{aligned}
K_{30}^{\rm old}
&=\Pi_\delta^{(30)}K_{30}
=-\frac{11}{9}[\delta]^*B_{10}
=33\sigma^{30}X^2(X+4b)^2,\\
K_{30}^{\rm new}
&=K_{30}-K_{30}^{\rm old}\\
&=\sigma^{30}X
 (227X^3-1524bX^2-192b^2X+1856b^3),\\
\mathrm T_{\delta,10}K_{30}^{\rm new}&=0.
\end{aligned}
\tag{23}
$$
旧部分的系数 $-11/9$ 在原好素数处是单位；
这不声称其指定除 $p$ 读数是单位。

最后设
$$
C_0^\epsilon=-\sigma(2z)K_{30}^\epsilon/21312,
\qquad \epsilon\in\{\mathrm{old},\mathrm{new}\}.
$$
两个来源都在原 $\sigma^{34}x^3y\,K[X]_{\le4}$ 的连接定义域，
而且从七阶起。因此 R863(A19) 的完整读者
$$
\mathcal L_p(C)=\frac{j_{p+2}(C)}p+
\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
\frac{j_r(q_F)j_{p+1-r}(C)}{r(r-1)},
\qquad q_F=(\Theta^{17})'/\Theta^{17},
\tag{24}
$$
可以逐项合法作用于二者，保持所有原低连接配对。准确地，
$$
\boxed{
\mathfrak B(Z_2)-\frac{455}{2664}\mathfrak B(S)
=\mathcal L_p(C_0^{\rm old})+\mathcal L_p(C_0^{\rm new})
\pmod p .
}
\tag{25}
$$
式(23)不会把第二项赋零：读者 (24) 还含同一个
$\sigma(2z)$ 与 $q_F$，并非 (2)。
同理，本篇并未让 CM7／CM13 穿过这些固定乘法因子。
若要利用 R876 的 H22 四谱，须保 (21)–(25) 的完整伙伴，
而不能仅按环境特征空间删除某一个分量。

以上证明为固定有理函数与有限三点迹的手证，无数值执行。
参考：[原 C24 三差](../notes/2026-11-16-original-common-odd-degree24-and-three-row-pairing.md)；
[R863 原完整连接及 H22](R863-original-balanced-frobenius-factor-and-partner-chain.md)；
[R876 原 H22 全有限算子](R876-original-h22-complete-cm-source.md)；
[R816 原 V66 全角色](R816-original-minus-eleven-rank-two-schwartz-and-degree66-source.md)。
