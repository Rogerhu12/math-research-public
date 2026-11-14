# R586 — 七个原 Euler 来源的全部共振系数与首 p² 窗口

日期：2026-11-14。**状态：已证明。**

本篇对 R583 的同一七个固定 Euler 原函数，给全部 $k$ 的准确
Gaussian 系数同余；其余不确定性只在两条原来源的首区块中。
在首 $p^2$ 窗口内，得到每个原函数指定共振系数的精确赋值，
并明确原首共振所需的两个实际系数。
证明不由有限素数计算推断非消失。

这些结论首先属于实际系数行。
单个来源的一个高阶系数非整，不等于同次数多项式格的真正饱和 jet 非整；
第 6 节保留这个区别。

## 1. 原 Gaussian 与两条完整 forcing

固定 $b=17$，$p=6s-1>71$ 为惰性好素数，$w=z^6$。
使用原
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,\qquad
R_4=2,\quad R_1=5,
$$
以及
[R583](R583-nine-coordinate-inert-resonance-absorption-and-sharp-envelope.md)
第 5 节的固定来源
$$
W_{4,h}=z^h\int_0^z t^{1-h}f_4(t)\,dt\quad(h=0,1),
$$
$$
W_{1,h}=z^h\int_0^z t^{4-h}f_1(t)\,dt\quad(0\le h\le4).
\tag{2}
$$
它们与原七个 $V_{\ell,r}$ 由固定的 $p$-整可逆矩阵相连，
仍在同一个 $w$ frame；没有改变积分常数。

准确取
$$
c=[z^{p+1}]\log(\sigma/z),\qquad a=6pc.
\tag{3}
$$
R356 (2)–(4) 给
$$
\bar a=-6\,\binom{3s-1}{2s-1}b^s\in k^\times.
\tag{4}
$$
因此 $a$ 是原规范下的单位，未换成另一局部地点或任意有利的参数。

令
$$
A_4=z^2f_4,\qquad A_1=z^5f_1.
$$
两条实际全函数都准确写成
$$
\boxed{
A_\ell(w)=w\exp\!\left(\frac ap w^s\right)G_\ell(w),
\qquad G_\ell=\sum_{j\ge0}g_{\ell,j}w^j .
}
\tag{5}
$$
对真实半径 $R_p=p^{-1/(2p)}$，有
$$
\boxed{\|G_\ell(z^6)\|_{R_p}\le1,\qquad
v_p(g_{\ell,j})\ge-\left\lfloor\frac{3j}{p}\right\rfloor.}
\tag{6}
$$

下面核 (6) 的原来源。
记 $\Theta=x\sigma^2$、$X_0=z^2x$，
并令 $\Theta_0=\Theta\exp(-2cz^{p+1})$。
R301 及 R418 (13) 保证 $\|\Theta_0\|_{R_p}\le1$，
且 $X_0,X_0^{-1}$ 在该圆盘范数均为一。
由 $y^2=x^3+b$，$-z^3y$ 也在该圆盘范数至多一。
因而 (5) 中的函数准确为
$$
G_4=\frac{\Theta_0^3}{X_0^2},\qquad
G_1=(-z^3y)\frac{\Theta_0^3}{X_0^2}.
\tag{7}
$$
这同时保留了完整 sigma charge 6 和全部原椭圆因子。
由 $R_p$ 的系数界立即得到 (6)。

因为 $s>13$，首两系数无 Gaussian 修正：
$$
g_{4,0}=g_{1,0}=1,\qquad
g_{4,1}=-\frac{4b}{35},\qquad
g_{1,1}=\frac{6b}{35}.
\tag{8}
$$
对于整个首区块 $0\le r<s$，有
$$
g_{4,r}=[z^{6r+4}]f_4,\qquad
g_{1,r}=[z^{6r+1}]f_1,
\qquad g_{\ell,r}\in\mathcal O.
\tag{9}
$$
(9) 是固定原来源的精确系数等式，不仅是模 $p$ 比较。

## 2. 全部 k 的唯一最低 Gaussian 项

**定理 1。** 任意 $k\ge1$，唯一写成
$$
k-1=Ls+r,\qquad L\ge0,\quad0\le r<s.
$$
则
$$
\boxed{
p^L L![w^k]A_\ell\in\mathcal O,\qquad
p^L L![w^k]A_\ell\equiv a^L g_{\ell,r}\pmod p .
}
\tag{10}
$$
这里 $L$ 不要求小于 $p$。

证明。由 (5) 的完整系数乘法，
$$
p^LL![w^k]A_\ell
=a^Lg_{\ell,r}
+\sum_{d=1}^L
p^d a^{L-d}\frac{L!}{(L-d)!}\,g_{\ell,ds+r}.
\tag{11}
$$
阶乘比 $L!/(L-d)!$ 始终为整数，即使 $L\ge p$ 也不会引入分母。
另一方面，由 $p=6s-1$、$r\le s-1$，
$$
dp-3(ds+r)
\ge(3s-1)(d-1)+2>0.
$$
故
$$
\left\lfloor\frac{3(ds+r)}p\right\rfloor\le d-1.
\tag{12}
$$
用 (6) 代入，(11) 的每个 $d\ge1$ 项至少被 $p$ 整除。
首项按 (9) 整，得到 (10)。证毕。

特别，只要 $\bar g_{\ell,r}\ne0$，便有精确赋值
$$
\boxed{
v_p([w^k]A_\ell)=-L-v_p(L!).
}
\tag{13}
$$
若 $\bar g_{\ell,r}=0$，(10) 只给严格增加至少一阶；
本篇没有将下一位擅自置零或置为单位。

## 3. 七个完整 Euler 原函数的系数归一

由原恒等式
$$
(6w\partial_w-h)W_{\ell,h}=A_\ell,
$$
每个系数准确满足
$$
[w^k]W_{\ell,h}=\frac{[w^k]A_\ell}{6k-h}.
\tag{14}
$$
这个正整数分母始终保留。
写
$$
e=v_p(6k-h),\qquad u=(6k-h)/p^e\in\mathbf Z_p^\times.
$$
把 (10) 除以单位 $u$，得到全部次数的完整结论。

**定理 2。** 对上述所有 $p,k$ 和七个实际来源，
$$
\boxed{
p^{L+e}L![w^k]W_{\ell,h}\in\mathcal O,\qquad
p^{L+e}L![w^k]W_{\ell,h}
\equiv\frac{a^L g_{\ell,r}}u\pmod p .
}
\tag{15}
$$
若 $\bar g_{\ell,r}\ne0$，准确有
$$
\boxed{
v_p([w^k]W_{\ell,h})=-L-v_p(L!)-e .
}
\tag{16}
$$
这是同一个原函数的全部系数公式，没有为不同 $k$ 改选来源。

特别，(8) 同时给两条无条件算术进展：
对于每个允许的 $(\ell,h)$，在
$$
k=Ls+1\quad\text{或}\quad k=Ls+2\qquad(L\ge0)
\tag{17}
$$
上，(16) 均成立。
完整有限阶乘和实际 $e=v_p(6k-h)$ 都不能从 (16) 删除。

对共同的 $h=0,1$，还可保任意 $p$-整原线性组合
$$
c_4W_{4,h}+c_1W_{1,h},\qquad
\min(v_p(c_4),v_p(c_1))=0.
$$
首两行的实际矩阵是
$$
\begin{pmatrix}
1&1\\
-4b/35&6b/35
\end{pmatrix},
\qquad \det=\frac{2b}{7}\in\mathcal O^\times.
\tag{18}
$$
因此 $r=0$ 或 $r=1$ 至少一行给非零剩余值，
并在对应的整条 (17) 上给该原组合的精确赋值 (16)。
这是实际系数的结论。
它不把非中央 Stokes 值与系数行相互替代，也不赋任何新中央值为零。

## 4. 首 p² 窗口中的全共振族

固定一个允许的 $h$，取整数
$$
m=h+6t,\qquad 1\le m\le p-1,\qquad0\le t\le s-1,
$$
其中 $h=0$ 时自然要求 $t\ge1$。
置
$$
k=ms-t.
$$
则准确有
$$
6k-h=mp,\qquad
k-1=(m-1)s+(s-t-1).
$$
所以 $e=1$、$L=m-1$、$r=s-t-1$。
因 $m<p$，(15) 等价于
$$
\boxed{
p^m[w^{ms-t}]W_{\ell,h}
\equiv\frac{a^{m-1}}{m!}\,g_{\ell,s-t-1}\pmod p .
}
\tag{19}
$$
这族全部满足 $6k=mp+h<p^2$。
(19) 保每一个共振分母及其来自原 forcing 的准确剩余系数。

令 $t=s-1$，即
$$
m=p+h-5,\qquad
k=(m-1)s+1.
$$
原 $g_{\ell,0}=1$ 给
$$
\boxed{
p^m[w^k]W_{\ell,h}
\equiv\frac{a^{m-1}}{m!}\in k^\times,
\qquad
v_p([w^k]W_{\ell,h})=-m .
}
\tag{20}
$$
所以七个原来源各自都有一个完全指定、无条件非零的首 $p^2$ 窗口共振。

这也准确检验 R583 的逐因子包络。
由 $6k=mp+h$，
$$
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor
=m+\left\lfloor\frac{m+hp}{p^2-1}\right\rfloor=m,
$$
因为 $m\le p-1$、$h\le4$、$p>71$。
此时 R583 的高次误差也为零，(20) 恰达到该单个系数的 Gaussian 上界。
因此不能用“原分子总会消掉共振分母”来获得无条件的逐系数严格改善。

同样取 $t=s-2$，便得到 (8) 的两条首一次 forcing 行，
其值由 (19) 完整运输，仍保 $a^{m-1}/m!$ 的原单位因子。

## 5. 真正最早的两个指定共振

把
$$
c_{4,p}=g_{4,s-1}=[z^{p-1}]f_4,\qquad
c_{1,p}=g_{1,s-1}=[z^{p-4}]f_1
\tag{21}
$$
保留为实际原系数。
这两个量与普通地点 R533/R540 的负二 $I_4$、负五 $I_1$ 不同。

最早几条 Euler 分母的完整关系如下。
所有表项都是原系数乘所列 $p$ 幂后的模 $p$ 等式。

| 来源 | 首个 $p$ 分母所在 $k$ | 精确剩余行 |
|---|---:|---|
| $W_{4,1}$ | $s$ | $p[w^s]W_{4,1}=c_{4,p}$ |
| $W_{1,1}$ | $s$ | $p[w^s]W_{1,1}=c_{1,p}$ |
| $W_{1,2}$ | $2s$ | $p^2[w^{2s}]W_{1,2}=(a/2)c_{1,p}$ |
| $W_{1,3}$ | $3s$ | $p^3[w^{3s}]W_{1,3}=(a^2/6)c_{1,p}$ |
| $W_{1,4}$ | $4s$ | $p^4[w^{4s}]W_{1,4}=(a^3/24)c_{1,p}$ |
| $W_{\ell,0}$ | $p=6s-1$ | $p^6[w^p]W_{\ell,0}=(a^5/720)g_{\ell,s-2}$ |

表中 $W_{1,2},W_{1,3},W_{1,4}$ 的首共振并没有给三个新的自由系数；
它们都由同一条 $c_{1,p}$ 决定。
但 $h=0$ 的首共振保留相邻的 $g_{\ell,s-2}$，不能直接改成 (21)。

本篇没有证明 $c_{4,p}$ 或 $c_{1,p}$ 总非零，也没有从 (20)
推出 (21) 的非消失。(20) 使用的是另一指定原系数，不能移换指标。

固定 $b=1$ 与原 $b=17$ 的运输也保全部常数。
原同次伸缩准确给
$$
g_{\ell,r,b}=b^r g_{\ell,r,1}\quad(0\le r<s),\qquad
a_b=b^s a_1,\qquad
[w^k]W_{\ell,h,b}=b^{k-1}[w^k]W_{\ell,h,1}.
\tag{22}
$$
因为 $k-1=Ls+r$，(15) 的两边都乘 $b^{k-1}$。
在所有好位这是单位运输，并未更换 p-adic 周期或 Frobenius 根。

## 6. 同一个真正前缀中的使用范围

R583、R579 的原源格仍是
$$
E_{D,9}=\bigoplus_{|\boldsymbol a|\le D}
\mathbf Z\,\boldsymbol X^{\boldsymbol a},\qquad
K_{D,k}=\ker(r_0,\ldots,r_{k-1})\cap E_{D,9}.
$$
本篇首先精确计算单列的 $r_k$，并没有证明该单列属于 $K_{D,k}$。

尤其对 $D=1$，函数 $1$ 与九坐标线性独立，故存在一个固定有限阶
$k_0$，使有限前缀已经具有全部十列的秩。
于是 $k>k_0$ 时 $K_{1,k}=0$。
(20) 中 $k$ 随 $p$ 增长；其原坐标系数即使非整，
相应 $\varphi_{1,9}^k$ 仍可准确为零。

因此，(15)、(19) 是可用于原系数矩阵的完整新输入，
而不是 R581 的高 $p$ 饱和层非整性的替代证明。
若要将它们运输到增长的 $D$、真正的前缀或原算术失败条件，
还须支付全部前行的实际关系、混合单项式及同一个核。
本篇不由七个不同 $h$ 的 scalar 公式删除这些条件。

原 $S/T$ 全中央到两个普通负矩的桥仍未完成；
上述惰性首行也未被增添为新的算术零。

## 7. 复核

[check-r586-original-euler-resonant-coefficients.mjs](../scripts/check-r586-original-euler-resonant-coefficients.mjs)
从 $x''=6x^2$ 及 $\sigma$ 的准确原点归一重建
$z^2x$、$6\log(\sigma/z)$、$f_4/z^4$、$f_1/z$ 的原有理系数。
在原先已用的两个小素数 $11,23$ 上核对 (15) 的前 81 个系数，
包括 $L\ge p$ 时的真实阶乘，并同时保 $b=1,17$ 的 (22)。

证书共完成 123,039 项精确检查，并核对 (12) 的有限整数网格和整个首窗口的指标关系。
有限计算只是核对；全部 $p,k$ 的定理由 (6)、(11)–(12) 证明。
没有扩大素数非消失扫描，也没有将另一个大阶系数的单位
误认成 (21)、普通负矩或原完整中央的单位。
