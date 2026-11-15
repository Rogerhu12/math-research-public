# R647 — 三条原算术来源的共同有理替代与前五块 Cartier 必要式

日期：2026-11-15。**状态：已证明。**

本篇直接把原 $S_{34}$、$T_{72}$ 和 R469 的 degree136 来源放回同一个
有理函数域，不先通过辅助 $f_4,f_1$ 再省略低卷积残差。
全部前五个原中央系数可由同一个 $\Theta_p$ 的实际 Cartier 值读出。
第五块保留原参数的共同仿射项 $6\kappa_5$。

由原完整 $j_m=0$ 得到的是含有低块真实除 $p$ 商的必要式。
它不令所有 Cartier 行分别为零；即使显示的仿射项是单位，
本篇也没有删除与它相等的实际补项。

## 1. 原模型、三个完整来源与物理尺度

保持
$$
p=6s-1>71,\quad b=17,\quad d=p+1,\quad L=(p^2-1)/6,\quad w=z^6,
$$
$$
E_b:y^2=x^3+b,\quad D=\frac d{dz},\quad Dx=2y,\quad Dy=3x^2,\quad
\omega_E=\frac{dx}{2y}.
$$
原展开为 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$。
设
$$
c=[w^s]\log(\sigma/z),\quad \sigma^\circ=\sigma e^{-cz^d},
\quad v_p(c)=-1,\quad \Theta=x\sigma^2.
\tag{1}
$$

为避免 $x^3$ 与中央变量混淆，记 $V=x^3$。
采用完整固定多项式
$$
P_S(t)=\frac{(1+t)(1-8t)(7-4t+16t^2)}7,
$$
$$
P_T(t)=P_S(t)(1+4t)(1-96t+48t^2+64t^3)(1+20t-8t^2),
\tag{2}
$$
及
$$
\begin{aligned}
P_U(t)={}&(1+t)(1+20t-8t^2)(7-4t+16t^2)\\
&\cdot(1+40t+2112t^2+3136t^3+1792t^4)\\
&\cdot(13+52t+1536t^2+1024t^3+256t^4)\\
&\cdot(1+1232t-58688t^2-49408t^3-439040t^4\\
&\hspace{12mm}-2111488t^5-1949696t^6-851968t^7-32768t^8)/91.
\end{aligned}
\tag{3}
$$
它们的次数分别为 $4,10,21$，常数项都是一。
置
$$
F_4(V)=V^4P_S(b/V),\quad
F_{10}(V)=V^{10}P_T(b/V),\quad
F_{21}(V)=V^{21}P_U(b/V).
$$
三个原来源准确为
$$
\begin{array}{c|c|c}
m& A_m& \Theta\text{ 表示}\\ \hline
34&S_b=\sigma^{34}x^2F_4(V)&\Theta^{17}V^{-1}P_S(b/V)\\
72&T_b=\sigma^{72}x^3F_{10}(V)&\Theta^{36}V^{-1}P_T(b/V)\\
136&U_b=\sigma^{136}x^2F_{21}(V)&\Theta^{68}V^{-1}P_U(b/V).
\end{array}
\tag{4}
$$
式 (3) 是 R466/R469 的完整原多项式，不是按首项另选的来源。
三者都满足 $A_m=z^6+O(z^{12})$。

令
$$
\mathscr G_m=A_me^{-mcw^s},\qquad
g_{m,h}=[w^{hs}]\mathscr G_m.
\tag{5}
$$
R614 给 $1\le h\le5$ 的整性。
同一证明也适用于 (3)：所有 $x$ 次数非负，
除去首 $w$ 后只用固定非负幂 $W=z^2x$ 与原整 sigma 余项。

若由共同 $b=1$ 模型转到本篇 $b=17$，准确有
$$
A_{m,b}(z)=b^{-1}A_{m,1}(b^{1/6}z),\quad
c_b=b^sc_1,\quad
g_{m,h}^{(b)}=b^{hs-1}g_{m,h}^{(1)}.
\tag{6}
$$
所以整个 Newton 导数乘 $b^{-1}$。
原 $E_{17},E_{24}$ 的物理身份，以及 $U$ 到 $E_{2312}$ 的额外
真实微分尺度，仍用 R303/R402/R469；这些都是当前的单位运输。
没有只换 Taylor 系数而保持一个错误的 Gaussian。

## 2. 一个实际 sigma 平方的全局替代

使用 R636 的原有理函数 $Z,G$：
$$
DZ=1,\quad D^p=0,\quad
DG=-x+c_pZ^{p-1},\quad
D^{p-1}G=(x^2/y)^p,
$$
$$
H_G=G+x^2/y,\quad
c_p=\binom{3s-1}{2s-1}b^s,\quad
H_G=(3b/5)z^5+\cdots.
\tag{7}
$$
R636 还准确支付
$$
\zeta^\circ-G=(3b/5)^p z^{6p-1}+\cdots,\qquad
Z=z-\kappa_5z^{5p}+O(z^{5p+1}),\quad
\kappa_5=\frac{(3b/5)^p}{c_p}\ne0.
\tag{8}
$$
所有涉及 $z$ 的模 $p$ 比较都在 R614 的实际整窗口内，
不将整个形式对数直接约化成全局函数。

设
$$
\nabla_2=D-2G,\qquad
Q_2=-\nabla_2^{p-1}Z,\qquad
P_2=Z^pQ_2=-\nabla_2^{p-1}Z^{p+1}.
\tag{9}
$$
在 $k(E_b)$ 上，完整曲率与逆为
$$
\nabla_2^p=-2H_G^p,\qquad
\nabla_2^{-1}=-\frac{\nabla_2^{p-1}}{2H_G^p}.
\tag{10}
$$
故 (9) 是下面两个方程各自唯一的有理解：
$$
\nabla_2Q_2=2H_G^pZ,\qquad
\nabla_2P_2=2H_G^pZ^{p+1}.
\tag{11}
$$
还可写成完整有限和
$$
P_2=\sum_{j=0}^{p-1}\frac{(-Z)^j}{j!}\nabla_2^jZ^2.
\tag{12}
$$
逐项求 $\nabla_2$ 后中间项相消，
剩余项等于 (11) 的右边；(10) 的唯一性给 (12)。
所有阶乘均为单位。

由 (12)，$P_2=z^2(1+\cdots)$，且其 $\mu_6$ 型为二。
与 R636 的 degree6 比较相同，由 (8)、(11) 得
$$
D\!\left(P_2/(\sigma^\circ)^2\right)=O(z^{6p-1}).
$$
比值型为零，首项为一；$6,12,\ldots,6(p-1)$ 均非零模 $p$。
因此
$$
\boxed{
P_2\equiv(\sigma^\circ)^2\pmod{z^{6p+2}},\qquad
\Theta_p:=xP_2\equiv\Theta e^{-2cw^s}\pmod{z^{6p}}.
}
\tag{13}
$$
这是全部相对 $w^{<p}$ 系数的同源比较，不是对若干点的拟合。
第一个可能的相对 Frobenius 项在 $w^p$，未赋零。

### 2.1 全部极点仍在原二挠除子

设 $\mathcal D_2=E_b[2]\setminus\{O\}$ 的三点和。
R636 的原极帽给
$$
(Q_2)_\infty\le(p-2)O+(p^3-2p^2+2p)\mathcal D_2,
$$
$$
(P_2)_\infty,\;(\Theta_p)_\infty
\le M_p\mathcal D_2,\qquad M_p=p^3-p^2+2p.
\tag{14}
$$
$xP_2$ 在 $O$ 的极与零准确相消，且值为一。
$\Theta_p$ 的型为零，所以
$$
\Theta_p\in k(V),\qquad
\Theta_p=1+\sum_{j=1}^{M_p/2}\frac{a_j}{(V+b)^j}.
\tag{15}
$$
最高项可为零；这是有界的完整有理表达。
极帽是 $O(p^3)$，不能当作固定 degree2 theta 截面。

## 3. 三条原来源同时返回，且没有新增三挠极点

以同一个 $P_2$ 定义
$$
\widehat A_{34}=P_2^{17}x^2F_4(V),\qquad
\widehat A_{72}=P_2^{36}x^3F_{10}(V),\qquad
\widehat A_{136}=P_2^{68}x^2F_{21}(V).
\tag{16}
$$
亦即在 (4) 的 $\Theta$ 表示中将 $\Theta$ 换成 $\Theta_p$。
式 (16) 明确约去其中表面出现的 $V=0$ 分母：
$x$ 的实际剩余幂分别是二、三、二。
所以三者只在 $\mathcal D_2$ 有极，在 $O$ 都从 $z^6$ 起，首系数一。
特别
$$
(\widehat A_m)_\infty\le(m/2)M_p\,\mathcal D_2,\qquad
\widehat A_m\in k(V).
\tag{17}
$$

由 (13) 逐项乘原完整多项式得到
$$
\boxed{
\widehat A_m\equiv A_me^{-mcw^s}
\pmod{z^{6p+6}}\qquad(m=34,72,136).
}
\tag{18}
$$
相对误差从 $z^{6p}$ 起，而原来源首阶为六。
因此 (18) 同时包含 $h\le5$ 的全部 (5)，
因为 $5(p+1)<6p+6$。
此处没有省略 $F_4,F_{10},F_{21}$ 的低卷积项；
R624 的 $\mathfrak R_1,\mathfrak R_2$ 已在这些完整多项式内。

## 4. 前五个原块的实际 Cartier 和留数

对 $1\le h\le5$，定义
$$
\mathcal B_{m,h}
=\frac{\mathcal C(Z^{-h-1}\widehat A_m\omega_E)}{\omega_E},
\qquad
\mathcal T_{m,h}
=\left(\frac{D^{h-1}\mathcal B_{m,h}(O)}{(h-1)!}\right)^p.
\tag{19}
$$
在 $O$，$Z^{-h-1}\widehat A_m$ 的阶为 $5-h\ge0$，
所以这里输入本身正则，Cartier 输出也正则。
其输出函数的 $\mu_6$ 型为 $h-1$，
从而低于 $z^{h-1}$ 的项全零。

$Z$ 是 $O$ 的实际局部参数，并有 $dZ=\omega_E$。
按这个参数的 Cartier 系数公式，准确有
$$
\boxed{
\mathcal T_{m,h}
=\operatorname{Res}_O\!\left(
\frac{\widehat A_m\omega_E}{Z^{h(p+1)+1}}
\right).
}
\tag{20}
$$
理由是 (19) 选择输入的 $Z^{hp-1}$ 系数，
等价于选择 $\widehat A_m$ 的 $Z^{h(p+1)}$ 系数。
在输出次数 $h-1\le4$ 上，$Z,z$ 及其导数归一相同。

原 $z$ 系数和 (19) 的准确关系为
$$
\boxed{
\overline{g_{m,h}}=\mathcal T_{m,h}\quad(1\le h\le4),\qquad
\overline{g_{m,5}}=\mathcal T_{m,5}-6\kappa_5.
}
\tag{21}
$$
证明到第五块只需保 (8) 的原首差。
将 (18) 写成 $Z$ 展开时，$z=Z+\kappa_5Z^{5p}+\cdots$，
故原首项 $z^6$ 在 $Z^{5(p+1)}$ 处新增 $6\kappa_5$。
其它正次项产生的误差更高；(18) 自身误差也高于目标。
前三个来源的首系数都为一，所以修正与 $m$ 无关。
等价地，在 (19) 输入中使用
$Z^{-6}=z^{-6}+6\kappa_5z^{5p-7}+\cdots$
得到同一符号和常数。

### 4.1 全局留数的支持不能缩错

式 (20) 是一个完整有理微分的留数。
除 $\mathcal D_2$ 外，它还可能在 $Z=0$ 的其它点有极。
R587 的准确等式
$Z=Z_*-c_p^{-1}(x^2/y)^p$ 中，$Z_*$ 在各非零二挠点正则，
所以 $Z$ 在这三点各有准确 $p$ 阶极。
由于 $dZ=\omega_E$，所有零点均为单零，
$\deg(Z)_0=3p$；其中包含 $O$。
所以可以使用完整留数定理，但必须保留这些其它零点。
本篇没有把 (20) 错写成只需三个二挠点的和。

第一两个块还可特别写为
$$
\overline{g_{m,1}}
=\left(\frac{\mathcal C(Z^{-2}\widehat A_m\omega_E)}{\omega_E}(O)\right)^p,
$$
$$
\overline{g_{m,2}}
=\left(D\frac{\mathcal C(Z^{-3}\widehat A_m\omega_E)}
                       {\omega_E}(O)\right)^p.
\tag{22}
$$
这里已经是原算术来源本身的两行，不需要先解 R595 的辅助两行矩阵。

## 5. 整 Gaussian 改变和完整中央规范

若 $c'=c+\eta$、$\eta\in\mathcal O$，应同时取
$$
G_\eta=G-\bar\eta Z^p,\qquad
\nabla_{2,\eta}=D-2G_\eta,\qquad
P_{2,\eta}=-\nabla_{2,\eta}^{p-1}Z^{p+1}.
\tag{23}
$$
这保留完整有限算子。
相同证明将 (18) 换成原 $A_me^{-mc'w^s}$；
(21) 的 $Z$ 坐标修正仍为 $6\kappa_5$。
非零 $\eta$ 的全局极帽可以增大；例如 $P_{2,\eta}$ 的每个二挠极帽应保为 $p^3+p$，不能继续套 (14) 的较小帽。

若用 R639 的完整中央规范
$$
F_c=\Pi_0\log(\sigma/z),\qquad E_c=e^{F_c},\qquad X=z^d,
$$
则令
$$
\exp\{-m(F_c-cX)\}
=\sum_{r\ge0}\gamma_{m,r}X^r,\qquad
\gamma_{m,0}=1,\quad\gamma_{m,1}=0.
\tag{24}
$$
所需 $r\le4$ 的系数都整，理由与 R636 §8.1 相同。
原完整中央系数为
$$
\boxed{
\overline{g^c_{m,h}}
=\sum_{r=0}^{h-1}\bar\gamma_{m,r}\,\overline{g_{m,h-r}}
\qquad(1\le h\le5).
}
\tag{25}
$$
因此第一、第二块逐项不变，第五块则是
$$
\overline{g^c_{m,5}}
=\mathcal T_{m,5}-6\kappa_5
+\bar\gamma_{m,2}\mathcal T_{m,3}
+\bar\gamma_{m,3}\mathcal T_{m,2}
+\bar\gamma_{m,4}\mathcal T_{m,1}.
\tag{26}
$$
这不是重新定义原完整 $j_m$。
R639 已付整个中央连接的唯一解在原点仍为同一个 $j_m$；
(25) 保留两个规范在实际低系数上的全部差异。

## 6. 原完整中央零究竟给哪些必要式

保持原首 Gaussian Newton 规范，令
$$
\gamma_m=pmc\in\mathcal O^\times,\qquad
L_{m,H}=\sum_{h=1}^H(-1)^{h-1}(h-1)!
        (p/\gamma_m)^h g_{m,h}.
\tag{27}
$$
R614 的整个无限尾准确给
$$
j_m\equiv L_{m,5}\pmod{p^6}.
\tag{28}
$$
同一尾证明对 $U$ 也成立。
式 (3) 的固定非负幂给 $g_{136,h}$ 在 $h\le p-1$ 整，
$h=p$ 至多一次分母，$p+1\le h\le2p-2$ 至多二次分母。
更高项仍有 R469 的原完整 Gauss 界
$$
v_p\!\left((h-1)!(p/\gamma_{136})^hg_{136,h}\right)
\ge \left\lceil\frac{h(p-1)+6}{2p}\right\rceil+v_p((h-1)!).
$$
右边随 $h$ 不减，在 $h=2p-1$ 已至少为 $p$。
所以所有高项确在 $p^6\mathcal O$ 中，(28) 不留下未知尾。

假设某一个实际 $j_m=0$。
对 $2\le h\le5$ 定义**实际部分和的除商**
$$
\mathscr B_{m,h}=p^{-h}L_{m,h-1}.
\tag{29}
$$
它整，因为原完整零及 R614 尾使
$v_p(L_{m,h-1})\ge h$。
它不是可以任意选择的剩余变量，也不是由 Cartier 值重新定义的量。

从原完整级数严格得到
$$
\boxed{
\mathcal T_{m,1}=0,\qquad
\mathcal T_{m,h}
=\frac{(-1)^h\bar\gamma_m^{\,h}}{(h-1)!}
 \overline{\mathscr B_{m,h}}
 +6\kappa_5\,1_{h=5}
\quad(2\le h\le5).
}
\tag{30}
$$
第二块尤其是
$$
\boxed{
\mathcal T_{m,2}
=\bar\gamma_m\,\overline{g_{m,1}/p}.
}
\tag{31}
$$
$g_{m,1}=[w^s]A_m$，因为 $A_m(0)=0$。
故 (31) 正保留 R606/R624 所需的原第一对角除 $p$，
没有把首行模 $p$ 为零误当成这个除商也为零。

第五块的非齐次必要式是
$$
\boxed{
\mathcal T_{m,5}
+\frac{\bar\gamma_m^5}{24}\overline{\mathscr B_{m,5}}
=6\kappa_5\ne0.
}
\tag{32}
$$
左右两项来自同一个原 $A_m$。
在同时假设 $j_{34}=j_{72}=0$ 时，(30)–(32)
必须分别对这两个实际来源成立。
只有在另外假设原第三条 $j_{136}=0$ 时，才同时加入第三套。
本篇没有从两条原零免费推出第三条零。

## 7. 本结果支付和没有支付的内容

(16) 把 R595/R606 的全部原低多项式残差直接纳入共同有理替代。
所以 (22)、(30)、(31) 比仅给辅助 $f_4,f_1$ 两行的映射更直接：
它们是原算术来源自身的 Cartier 值、原 $a_m/p$ 和原更高整部分和。

但 (32) 的单位右端不是一个矛盾。
它精确说明第五 Cartier 值与原低块除商不能同时为零。
尚须在这些同来源实际条目之间证明额外约束，
才能排除全部原完整中央同时失败。
同样，R636 的辅助 determinant 即使为单位，
也不能绕过 (29)、(31) 或原 $\mathfrak R_1,\mathfrak R_2$。

共同有理函数的极帽随 $p$ 增长，Cartier 观察依赖当前 $p$。
本篇没有把它们加入原固定预算列格，没有声称保全部有序前缀，
也没有给一个新的免费中央零。
所有结论由完整有理恒等式、原整窗口和完整 Newton 尾统一证明；
无新增素数扫描。

依赖：

- [R636](R636-original-rational-cartier-return-for-two-critical-rows.md)：
  原 $Z,G$、完整曲率、$z/Z$ 首差和有限窗口比较。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：
  全整窗口及原完整 Newton 尾。
- [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)、
  [R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md)：
  原 $S/T$ 全分子和首、次中央行。
- [R469](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)：
  第三个原 degree136 多项式及其完整算术尺度。
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：
  同一完整中央规范及未改变的原 $j_m$。
