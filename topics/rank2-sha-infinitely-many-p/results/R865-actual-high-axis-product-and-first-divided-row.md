# R865 — 实际高轴的有限乘积与首位唯一除 p 行

日期：2026-11-16。**状态：以下准确读取及首位范围已证明。没有证明指定第二、第三页非零。**

本篇全程固定共同 $E_1$、$b=1$，使用 [R861](R861-original-hasse-aligned-gaussian-and-three-hurwitz-readers.md) 的完整 $M^{\rm orig}$ 和 Hasse 对齐规范
$$
p=6s-1>211,\qquad
\mathcal C_p=(p+1)\binom{3s-1}{2s-1},\qquad
a_*=-34\mathcal C_p,\qquad h_0=-a_*/18 .
$$
全部 $P_{134},c_*U_0,w^{13}$、总 charge 四十与三条十三行带保留。只使用原 canonical 单部分；若扩大来源，仍须逐列核原零角帽。

## 1. 原实际 H 的全精度有限乘积

[R828](R828-original-four-high-axis-reflection-and-native-central-compatibility.md) 的原数为
$$
H_p=\frac{17}{3}(-1)^s
 \frac{(1/3)_{s-1}}{(5/6)_{s-1}} .
$$
定义以下三个实际单位：
$$
\mathcal A_p=\prod_{j=1}^{s-1}
 \frac{1-p/(6j+3)}{1-p/(6j)},\qquad
\mathcal B_p=\prod_{j=1}^{s}\left(1-\frac p{2j-1}\right),
\qquad
\mathcal E_p=\mathcal A_p/\mathcal B_p .
\tag{1}
$$
显示分母均为 $p$ 单位，且 $\mathcal E_p\in1+p\mathcal O$。
则在特征零中准确有
$$
\boxed{H_p=h_0\mathcal E_p.}
\tag{2}
$$

证明令 $C_s=4^{-s}\binom{2s}{s}$。反序原 Pochhammer 乘积给
$$
\frac{(1/3)_{s-1}}{(5/6)_{s-1}}
 =\prod_{j=1}^{s-1}\frac{p-6j-3}{p-6j}
 =2sC_s\mathcal A_p .
$$
另一方面
$$
\binom{3s-1}{2s-1}
 =\prod_{j=1}^{s}\frac{3s-j}{j}
 =(-1)^s C_s\mathcal B_p.
$$
代入 $p+1=6s$ 即得 (2)，没有换掉任何 Gaussian 首 residue。

为按原四位读取，置
$$
L_\nu=\sum_{j=1}^{s-1}
 \big((6j)^{-\nu}-(6j+3)^{-\nu}\big)
 +\sum_{j=1}^{s}(2j-1)^{-\nu},\qquad \nu=1,2,3 .
\tag{3}
$$
这些是显示的有限有理数。对 (1) 作整 $p$-adic 对数，
$$
\boxed{
\mathcal E_p\equiv
1+pL_1+\frac{p^2}{2}(L_1^2+L_2)
+\frac{p^3}{6}(L_1^3+3L_1L_2+2L_3)
\pmod{p^4}.
}
\tag{4}
$$
分别需要 $L_1\bmod p^3,L_2\bmod p^2,L_3\bmod p$；不能同时只取它们的首剩余类。

R861 的同一个移后低卷积因而准确等于
$$
\boxed{
\mathcal R_p^\flat
=a_*\left\{
 \frac4{3(p+1)}
 +\frac{p-3}{3(p+1)}\,\frac{\mathcal E_p-1}{p}
 \right\}.
}
\tag{5}
$$
这由 $a_*=6(p-3)H_p/(p+1)+p\mathcal R_p^\flat$ 和 (2) 直接得到。
所以 (1)–(5) 可计算同一实际高位，不必重新展开原低 $K$/sigma 卷积；
但没有将该真实数赋为零或自由参数。

例如在原四中央零的假设下，沿原一标量 Newton 规范记
$C=\eta_0\mathfrak F(h_0)\in p\mathcal O$、
$D=\eta_0\mathfrak F'(h_0)\in\mathcal O^\times$。
既有 $H_p=h_0-C/D\bmod p^3$ 与 (4) 给准确必要式
$$
\boxed{
\frac{C}{p h_0D}
\equiv-L_1-\frac p2(L_1^2+L_2)\pmod{p^2}.
}
\tag{6}
$$
其余三个完整中央残差及第四位二次修正不由 (6) 消失。

## 2. 在真实首核上三条 D 的首位压为一条

令 $Q=40+n$、$m=34Q$，把同一个未分割的完整物理列写成
$$
\Phi(w)=w^{13}A_\Phi(w)e^{a_*Qw^s/p}.
\tag{7}
$$
$A_\Phi$ 已含完整 $c_*U_0$ 和角因子。R618 的第二 Gaussian 圆盘及 R821/R861 的原列运输保证这里所读的 regular 系数整；具体本节只用 $[w^s]A_\Phi$，因 $p>211$，该范围在原第二圆盘的整系数窗内。这里不用任意环境形式列替代原列。
本节的 $A_\Phi$ 和下节的 $\bar g$ 始终来自 Hasse 对齐后的实际完整
$g^\flat$，包括真实 $h_\Theta$。若改写成参考 $g_0$，须恢复原
$3H_p[w^4](B W_3)$ 项；它只在 $\ell\ge5$ 时由短首核自动消去，
不能在其它范围凭规范选择删除。

置
$$
U_1=(p+79)!/p,\qquad
T_p=\frac{U_1+79\cdot78!}{p}\in\mathcal O.
\tag{8}
$$
整性使用 $U_1\equiv-79!\bmod p$。
在 (7) 的 $w^{s+13}$ 系数上准确有
$$
J_{p+79}=U_1\big(a_*Q A_\Phi(0)+p[w^s]A_\Phi\big).
$$
因 $a_*Q=-m\mathcal C_p$，R861 的实际整行满足
$$
\boxed{
\mathcal D_{m,p,79}(R_\Phi)
=U_1[w^s]A_\Phi-m\mathcal C_pT_p A_\Phi(0).
}
\tag{9}
$$
此处没有删掉原 $79m\mathcal C_pJ_{78}$。

仍记
$$
r(Q)=(Q-40)(Q-41)(Q-42),\qquad
\Lambda_0=\sum_{j=0}^{3}\frac{r_jj!}{a_*^j}
 [\epsilon^jw^{13}].
$$
取同一个原 $P\in K_1=\ker\bar M$，各坐标以任意整 lift 表示。
其三条常数行使 charge $40,41,42$ 的 $A_\Phi(0)$ 组合逐个为零模 $p$；
其它 charge 的这个常数已在特征零为零。
因此 (9) 与原 native 行准确给
$$
\boxed{
\Lambda_0\beta_1(P)
=\frac1{a_*U_1}
 \sum_\Phi P_\Phi\,r'(Q_\Phi)
       \mathcal D_{34Q_\Phi,p,79}(R_\Phi)
\pmod p.
}
\tag{10}
$$
也可把首系数写为 $-1/(a_*79!)$。
这里 $r'(40+n)=3n^2-6n+2$。乘这个多项式不是给变换后的来源添中央零，
也没有证明它保持 $K_1$。

所以 R861 的三个整 Hurwitz 行在**首位的这个指定读数**中不提供三个独立输入。
(10) 不延伸为后两位的一行公式：真实第二、第三页仍须保
$\mathcal D_{m,p,p+80}$、$\mathcal D_{m,p,2p+81}$、完整低项以及同一 $R,S$。

## 3. 高接触 quartic 首形上的真实范围

假设同一个实际首核具有
$$
\bar P=t^rF^4q,\qquad
F(t(w),\bar g(w))=w^hu,\qquad
e=(Y\partial_YF)(t(w),\bar g(w)),
$$
其中 $h\ge1$，$u(0),e(0),q(0,1)$ 为单位；保原全帽和原短块首核条件。
令
$$
k=r+13+2h-s .
$$
原源端 Euler $\mathcal E=Y\partial_Y$ 满足
$$
r'(\mathcal E+40)=3\mathcal E^2-6\mathcal E+2 .
$$
其作用于 $\bar P$ 的最低项准确是
$$
(3\mathcal E^2-6\mathcal E+2)\bar P
=36t^rF^2e^2q+O(F^3).
\tag{11}
$$
所以原首配对也等于
$$
\Lambda_0\beta_1(P)
=\frac1{a_*}[w^s]\,
 c_*U_0(w)(3\mathcal E^2-6\mathcal E+2)\bar P(t(w),\bar g(w)).
\tag{12}
$$
显示级数的首阶是 $r+2h=s+k-13$。因此
$$
\boxed{
\begin{array}{ll}
k=13:&
\Lambda_0\beta_1(P)=
\displaystyle\frac{36c_*U_0(0)}{a_*}
 \left(\frac{t(w)}w\right)_{\!w=0}^{r}
 q(0,1)u(0)^2e(0)^2\ne0,\\[2mm]
k>13:&\Lambda_0\beta_1(P)=0.
\end{array}}
\tag{13}
$$
第一行正是已付 [R824](R824-original-quartic-first-correctors-and-native-central-schur.md) 第十三行边界；不重复计算为新的排除。
第二行明确该首读数在高接触 quartic 区域的限制，不能据 R861 最后一个
$\gamma$ 系数是单位就声称首 Bockstein 非零。

后续真正未定的仍是同一个 $P,R,S$ 的
$\mathcal H_{\rm nat}(P)+p\mathcal H_{\rm nat}(R)+p^2\mathcal H_{\rm nat}(S)$，
连同原全矩阵的其它行。特别首位 (13) 为零不使 native 整商
$\mathcal H_{\rm nat}(P)/p$ 自动可删，也不允许分别选择两次修正。

本篇是完整符号推导，无数学数值执行。它补充实际参数和首位读取，
不把任何一种重写当成主目标的非零证明。
