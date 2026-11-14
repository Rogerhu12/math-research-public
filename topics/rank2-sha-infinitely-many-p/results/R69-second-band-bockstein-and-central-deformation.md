# R69. 第二坏带的真实 Bockstein 与中央变形

日期：2026-11-12。**状态：完整第二带公式、饱和商中的首个新行及实际证书已证明；未证明跨素数非零。**

沿用 R62、R67，令 $w=z^4$、$r=(p+1)/4$、$a=17c$，
$A=e^{aw^r}G$、$f_0=e^{aw^r}G_0$、$Y=4\mathscr H/f_0$。
记 $E=w\partial_w$，并定义同一固定实际函数
$$
\Psi_1=f_0^{-1}(4E+1)^{-1}(4\mathscr H)=w/5+\cdots,
\quad
\Psi_2=f_0^{-1}(4E+2)^{-1}(4E+1)^{-1}(4\mathscr H)=w/30+\cdots.
$$

## 1. 第二带的完整最高极项

Euler 逆的逐系数恒等式为
$$
e^{-aw^r}E^{-1}(e^{aw^r}G)
=\sum_{h\ge0}(-ar)^hw^{hr}
   [E(E+r)\cdots(E+hr)]^{-1}G.
$$
在次数不超过 $3r<p$ 的范围，残余 $G,G_0^{-1}$ 至多有一层 $p$ 分母。
因此对每个整多项式 $P(w,y)$，准确有
$$
p^2P(w,Y)\equiv(pa)^2w^{2r}
\left(\Psi_2P_y(w,Y_{\le r})+
\frac{\Psi_1^2}{2}P_{yy}(w,Y_{\le r})\right)
\pmod{(p,w^{3r+1})}.
\tag{1}
$$
这保留了真正二阶导数项，不能只重复首坏带的 $P_y$。

令 $B_n(P)=[w^n]P(w,Y)$、$D_0(P)=P_y(0,0)$。
第一条二阶极行是
$p^2B_{2r+1}\equiv(pa)^2D_0/30$，与旧行
$pB_{r+1}\equiv-paD_0/5$ 重复。取
$a_0=[w^r]f_0$，则 $a_0-a$ 整，真正需要的新整行为
$$
\boxed{R_p=pB_{2r+1}+\frac{pa_0}{6}B_{r+1}.}
\tag{2}
$$
它在全部原始 section 格上整；在旧前缀的真实核上，$R_p=pB_{2r+1}$。
故其模 $p$ 非零对应新增 jet 的范数 $p$，不是未经消元的 $p^2$。

## 2. 中央变形与独立精确证书

局部变形 $G\mapsto G+\delta w^r$（$\delta$ 整）保留既有 Gauss 界和首项，且
$$
\Delta Y=\frac{\delta}{ar}G_0^{-1}(1-e^{-aw^r}).
$$
旧约化前缀核不变。在该核上，新行的变化准确为
$$
\Delta\overline R_p=-\frac{pa\delta}{5r}P_{yy}(0,0).
\tag{3}
$$

对实际 $p=103$、$D=9$、$r=26$，55 列的旧 53 行秩为 53，
单位子式为 $43+48i$。在两个自由核方向上，
$$
P_{yy}=(60+50i,38+102i),\qquad
R_p=(59+6i,1+24i),
$$
两行行列式为 $92+18i\ne0$。
所以对每个中央 $\delta$，$R_p$ 都不变成零行；下一条真正二阶极行
给独立的 $P_{yy}$ 方向，完整 55 阶行列式的赋值为 $-26-1-2=-29$。
这里不从行列式单独声称全部 Smith 指数。

同时真实 Mahler 因子变为
$J_A(u)+a^{-1}\delta u$。因 $J_A'(0)\in p\mathcal O$，取
$\delta=-aJ_A'(0)\in\mathcal O$ 即可杀掉中央 Stokes 常数，
而上述局部矩阵的非零性仍保留。这是对这个有限 jet 检测的准确边界；
该依赖 $p$ 的变形不是另一条全局 theta，也不是主命题的反例。

全文及精确脚本见
[第二坏带证明](../notes/2026-11-12-second-band-bockstein-and-central-variation.md)、
[独立复算](../scripts/check-inert-second-band-bockstein.py)。根端已运行全部断言通过。
