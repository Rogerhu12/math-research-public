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

## 附录 A — 同一原第一修正的两个 Fermat 商闭式

本附录仍固定正文的 Hasse 对齐 $a_*=-34\mathcal C_p$、
$h_0=-a_*/18$ 和 $p=6s-1>211$。设
$$
q_p(c)=\frac{c^{p-1}-1}{p}\in\mathbf Z
\quad(c=2,3),\qquad
H_j=\sum_{k=1}^j\frac1k,\quad H_0=0.
\tag{A.1}
$$
这些是原有理整数的 Fermat 商，后文只取其模 $p$ 的剩余类。
没有另选 $p$-进对数或改变 $\mathcal E_p$ 的提升。

正文 (3) 的同一个完整有限数 $L_1$ 满足
$$
\boxed{
L_1\equiv
\frac{q_p(2)}3-\frac{3q_p(3)}4+\frac13\pmod p .
}
\tag{A.2}
$$
因而原完整低卷积 (5) 的首剩余值准确为
$$
\boxed{
\frac{\mathcal R_p^\flat}{a_*}
\equiv 1-\frac{q_p(2)}3+\frac{3q_p(3)}4\pmod p .
}
\tag{A.3}
$$
特别，这里读取的是同一 $\mathcal R_p^\flat$，包括其原参考运输，
不是只保其中一个 $K$ 卷积项。

### A.1 两个谐和式的自含证明

首先
$$
\boxed{
H_{3s-1}\equiv-2q_p(2),\qquad
H_{2s-1}\equiv-\frac32q_p(3)\pmod p .
}
\tag{A.4}
$$
第一式由
$$
2q_p(2)=\frac{2^p-2}{p}
=\sum_{k=1}^{p-1}\frac1p\binom pk
\equiv\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}k
=-H_{(p-1)/2}\pmod p
$$
直接得到。最后一步使用 $H_{p-1}\equiv0$，
并把偶数分母的和写成 $H_{(p-1)/2}/2$。

为证明第二式，在原未分歧二次扩张中取
$\omega^2+\omega+1=0$。因 $p\equiv2\pmod3$，
$\omega^p=\omega^2$，且 $1-\omega^2$ 为单位。
令 $n=(p-1)/2=3s-1$。从
$(1+2\omega)^p=-(1+2\omega)$ 在剩余域的恒等式得
$(-3)^n\equiv-1\pmod p$。再平方并使用
$3^{p-1}=1+pq_p(3)$，得到
$$
(-3)^n\equiv-1-\frac p2q_p(3)\pmod{p^2}.
$$
因为 $(1-\omega)^2=-3\omega$ 和 $\omega^n=\omega^2$，这给
$$
(1-\omega)^p
=(1-\omega)\omega^2(-3)^n
\equiv(1-\omega^2)\left(1+\frac p2q_p(3)\right)
\pmod{p^2}.
\tag{A.5}
$$
另一方面，展开同一个左边，再减去 $1-\omega^p$ 并除以 $p$，
得到
$$
-\sum_{k=1}^{p-1}\frac{\omega^k}{k}
\equiv\frac{q_p(3)}2(1-\omega^2)\pmod p.
\tag{A.6}
$$
将分母按模 $3$ 的类分组，记
$A_r=\sum_{1\le k<p,\ k\equiv r\ (3)}1/k$。
置换 $k\mapsto p-k$ 给
$A_1=0$、$A_2=-A_0$，而
$A_0=H_{2s-1}/3$。故 (A.6) 的左边是
$-(1-\omega^2)H_{2s-1}/3$。
约去这个真实单位即得 (A.4) 的第二式。
因此这两个同余不需要选择额外射线或局部相位。

还需要准确的六分之一处谐和和：
$$
\boxed{H_{s-1}\equiv H_{3s-1}+H_{2s-1}\pmod p.}
\tag{A.7}
$$
以下给完整重排，避免混用三个截断端点。令
$$
U=\sum_{j=0}^{s-1}\frac1{3j+1},\qquad
V=\sum_{j=0}^{s-1}\frac1{3j+2}.
$$
则 $H_{3s-1}=H_{s-1}/3+U+V$。
对 $V$ 用 $p-(3j+2)=3(2s-1-j)$，得
$$
V\equiv-\frac13(H_{2s-1}-H_{s-1}).
$$
把所有 $3$ 的倍数再按奇偶分组，并使用
$p-3(2j-1)=2(3(s-j)+1)$，得
$$
\frac13H_{2s-1}
\equiv\frac16H_{s-1}-\frac12U.
$$
这两个式子代回 $H_{3s-1}$，便是 (A.7)。
结合 (A.4)，
$$
H_{s-1}\equiv-2q_p(2)-\frac32q_p(3)\pmod p.
\tag{A.8}
$$

### A.2 原有限乘积到完整低卷积

记 $O_s=\sum_{j=1}^s1/(2j-1)$。
直接从正文 (3) 而不是从另一个参考展开，有特征零的准确等式
$$
\begin{aligned}
L_1
&=\frac16H_{s-1}
  -\frac13(O_s-1)+O_s\\
&=\frac23H_{2s}-\frac16H_s+\frac13-\frac1{6s}.
\end{aligned}
\tag{A.9}
$$
因为 $6s=p+1$，
$$
H_{2s}\equiv H_{2s-1}+3,\qquad
H_s\equiv H_{s-1}+6,\qquad
(6s)^{-1}\equiv1\pmod p .
$$
把 (A.4)、(A.8) 代入 (A.9)，得到 (A.2)。

正文 (5) 在同一规范中给
$$
\frac{\mathcal R_p^\flat}{a_*}
\equiv\frac43-L_1\pmod p ,
$$
因此严格得到 (A.3)。所有原固定分母均为单位，
这里没有新增有限坏素数集。

### A.3 实际高轴第一位与同一个中央 Newton 值

保 [原一标量四位式](../notes/2026-11-16-r828-actual-one-scalar-four-digit-and-same-correction-pages.md)
(8)–(15) 的约定
$$
H_p=h_0+ph_1+O(p^2).
$$
由本篇准确恒等式 $H_p=h_0\mathcal E_p$，
$$
\boxed{
h_1\equiv-\frac{a_*}{18}
\left(\frac{q_p(2)}3-\frac{3q_p(3)}4+\frac13\right)
\pmod p.
}
\tag{A.10}
$$
这与同一低卷积中的
$h_1=\mathcal R_p^\flat/18-2a_*/27$
一致；不是另选一位高轴。

现在仅在原四个完整中央同时为零的假设下，沿原固定
$\eta_0=e_0^tB_4^{-1}$，记
$$
Q_c=\frac{\eta_0\mathfrak F(h_0)}p,\qquad
b_0=[w^0]B(w)\in\mathcal O^\times .
$$
$Q_c$ 的整性由该中央假设及原四位 Hensel 式支付，
$b_0$ 是原高轴级数的常数项，不是曲线参数 $b=1$。
因为
$\eta_0\mathfrak F'(h_0)\equiv b_0$，
同一个 Newton 方程准确给
$$
\boxed{
Q_c\equiv\frac{a_*b_0}{18}
\left(\frac{q_p(2)}3-\frac{3q_p(3)}4+\frac13\right)
\pmod p .
}
\tag{A.11}
$$
这并不把 $Q_c$ 等同某一个裸 $\mathfrak B_\nu$。
它仍是原四来源、原 $\eta_0$ 和完整参考上的那个组合；
另外三条中央残差没有因 (A.11) 消失。

(A.2)、(A.10)、(A.11) 都只支付所显示的首剩余位。
正文 (4)、(6) 的更高精度仍需
$L_1\bmod p^3,L_2\bmod p^2,L_3\bmod p$
及全部 native 来源项。没有证明
$q_p(2)/3-3q_p(3)/4+1/3$ 对某个原好素数非零，
也没有证明其对无穷多个目标素数非零。
同一 $P,R,S$ 的全部 normal/carry 方程仍须保留。

