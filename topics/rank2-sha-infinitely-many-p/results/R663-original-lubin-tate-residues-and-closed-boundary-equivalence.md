# R663 — 原 Lubin–Tate 坐标、完整共振余数与同一正规解的闭边界判据

日期：2026-11-15。**状态：已证明。**

本篇继续 R660，保持原 $m=34,72$ 来源、完整 $T_{\rm g}$ 及同一个算术值 $j_m$。
把原形式群整地送到 $[-p](v)=-pv+v^{p^2}$ 后，全部首边界轨道的多项式准确成为
$$
Q(W)=W^{p-1}-p.
$$
原完整轨道和仍给整级数 $\mathcal B_m(W)$，其常数仍为 $[z^{p+1}]A_m$。
全部 $Q^\ell$ 整除条件可以写成保留无限高尾的有限组准确 $p$ 进值。

此外，将 R639 的同一个正规解作下面明确的 $H^{-m}$ 变换后，它属于闭首边界 Tate 代数，
当且仅当 $Q\mid\mathcal B_m$；这时实际还延到略大的盘。
证明使用同一个完整连接的严格常数主导，因此支付了全盘粘合，不只是各边界点的局部存在。

这个变换后的闭盘条件仍未由 $j_m=0$ 推出。原 $X$ 坐标中 $\mathcal R_m$ 的闭盘条件更强，
R660 的 $Q^{p+1-m}$ 必要式仍保留。

## 1. 原形式群的严格整坐标

固定
$$
p\equiv5\pmod6,\quad p>101,\quad q=p^2,\quad d=p+1,\quad e=p-1,
\quad K=\mathbf Q_p(\omega),\quad\mathcal O=\mathcal O_K,\quad b=17.
$$
仍取
$$
u=x^{-1/2},\qquad z'(u)=C(u)=(1+bu^6)^{-1/2},\qquad z=u+O(u^7).
$$
标准形式参数 $t=-x/y$ 与 $u$ 整可逆，故原好约化形式群及全部 CM 标量在 $u$ 中整。

因为 $x\mapsto x^3$ 在 $\mathbf F_p$ 上是置换，
$$
\#E_b(\mathbf F_p)=p+1+\sum_x\left(\frac{x^3+b}{p}\right)=p+1.
$$
故约化 Frobenius 的关系为 $\operatorname{Fr}_p^2=[-p]$。
在原 $u$ 参数中，$\operatorname{Fr}_p^2$ 正是 $u\mapsto u^q$。
于是原
$$
f(u)=[-p]_E(u)
$$
满足
$$
f(u)=-pu+O(u^2),\qquad f(u)\equiv u^q\pmod p.
\tag{1}
$$
第二式是全部级数的同余，不仅到 $q$ 阶。

令 $g(v)=-pv+v^q$。存在唯一
$$
\boxed{v=h(u)\in u+u^2\mathcal O[[u]],\qquad h(f(u))=g(h(u)).}
\tag{2}
$$
其逆也整。为完整支付这里的坐标，逐次数构造如下。
若 $h$ 已构到 $n-1$ 次，误差 $h\circ f-g\circ h$ 的第 $n$ 个系数是 $E_n$。
将 $h$ 改为 $h+c u^n$，该误差系数变为
$$
E_n+c\bigl((-p)^n-(-p)\bigr).
$$
模 $p$ 时，因剩余域为 $\mathbf F_q$，
$$
\bar h(u^q)=\bar h(u)^q,
$$
所以 $E_n\in p\mathcal O$。
而 $((-p)^n+p)/p$ 是单位，故唯一选择的 $c$ 整。
同样反向构造，组合唯一性给整逆。
同一递推对任意指定线性项也唯一；由此坐标同时输送原形式群加法和 CM 标量。
这就是 Lubin–Tate 系数构造在这里的完整证明。

两个整可逆级数在整个开单位盘上收敛、互逆、保持绝对值；
它们的导数也处处为单位。
对 $\zeta\in\mu_{q-1}$，线性映射 $v\mapsto\zeta v$ 与 $g$ 交换，
因此由上述唯一性，原 CM 作用在 (2) 中准确为
$$
v([\zeta]_E u)=\zeta v(u).
\tag{3}
$$
没有将有限阶 CM 作用改成另一个来源。

原对数 $z(u(v))$ 的导数在零处为一，且
$$
z(g(v))=-p z(v),\qquad z(\zeta v)=\zeta z(v).
$$
所以存在只依赖 $p$ 的级数 $\mathcal H_p$，使
$$
\boxed{
z(v)=v\mathcal H_p(v^{q-1}),\quad
\mathcal H_p(T)\in1+T K[[T]],\quad
[T]\mathcal H_p=\frac1{p^q-p}.
}
\tag{4}
$$
最后系数由比较 $z(-pv+v^q)=-p z(v)$ 的 $v^q$ 项直接得到。
$\mathcal H_p$ 在 $|T|<1$ 解析；不称它整。

## 2. 首边界准确为一个二项式

保持原半径
$$
R_E=p^{-1/(q-1)},\qquad r_E=R_E^d=p^{-1/e},
\qquad W=v^d,\qquad H(W)=\mathcal H_p(W^e).
\tag{5}
$$
原非零 $p$ 挠点在 (2) 中恰满足
$$
v^{q-1}=p.
\tag{6}
$$
其按原范数一群 $\mu_d$ 的 $e$ 个轨道，准确对应
$$
\boxed{Q(W)=W^e-p.}
\tag{7}
$$

这里也可直接核清下一层以前没有遗漏的对数零点。
对每个 $|v|<1$，迭代 $g$ 趋于零：
$$
|g(v)|\le\max\{p^{-1}|v|,|v|^q\}<|v|.
$$
在足够小盘上 $z$ 可逆；若 $z(v)=0$，
则 $z(g^{\circ n}(v))=(-p)^n z(v)=0$，
故足够大 $n$ 时 $g^{\circ n}(v)=0$。
反之挠点当然被 $z$ 杀掉。
所以开单位盘中 $z$ 的零恰是全部 $p$ 幂挠点。

首层非零点的半径为 $R_E$。
若点严格在首层外而其 $g$ 像在首层，则 $v^q$ 为唯一主导项，
故其半径是 $R_E^{1/q}$。
因此在
$$
|W|<r_2:=r_E^{1/q}
$$
内，$H$ 的全部零正是 (7) 的 $e$ 个简单根。
简单性也可由原 $z'(u)=C(u)$、$du/dv$ 均非零直接读出。
于是
$$
\boxed{H(W)=(1-W^e/p)\,U(W),}
\tag{8}
$$
其中 $U,U^{-1}$ 在每个闭 $r<r_2$ 盘都是 Tate 元。
这里没有给 $U$ 免费整系数，也没有把对数逆延过首边界。

## 3. 原完整轨道和与首系数不变

沿用 R639/R660 的原
$$
T(u)=T_{\rm g}(u),\qquad T^{\pm1}\in1+u^2\mathcal O[[u]],\qquad
E_{\rm c}=(\sigma/z)T.
$$
令
$$
F_m(u)=T(u)^{-m}\phi_m(x(u),y(u)),
\qquad
\Phi_m(u)=\frac1d\sum_{\zeta\in\mu_d}\zeta^mF_m([\zeta]_E u),
\tag{9}
$$
其中 $A_m=\sigma^m\phi_m$，$m=34,72$，原 $\phi_m$ 的极阶恰为 $m-6$。
这是 R660 的同一个函数 $\Phi_m$。

由 (2) 的整性、原极帽以及 (3)，完整字符投影给
$$
\boxed{
\Phi_m(u(v))=v^{d-m}\mathcal B_m(W),\qquad
\mathcal B_m(W)=\sum_{n\ge0}b_{m,n}W^n\in\mathcal O[[W]].
}
\tag{10}
$$
没有抛去任何 CM 支、原多项式项或 $T$ 的高尾。
原 $X=z^d$ 与 $W$ 的关系和完整来源身份为
$$
X=WH(W)^d,\qquad
\boxed{
G_{m,{\rm c},0}(WH^d)=WH^m\mathcal B_m(W).
}
\tag{11}
$$
因此
$$
\boxed{
b_{m,0}=g^{\rm c}_{m,1}=[z^{p+1}]A_m(z).
}
\tag{12}
$$
若用 $v_0$ 表示 R660 的平均坐标，则
$v_0=v A(W)$，$A\in1+W\mathcal O[[W]]$，整逆亦然。
原旧 $B_m$ 与本篇级数准确满足
$$
\mathcal B_m(W)=A(W)^{d-m}B_m(WA(W)^d).
\tag{13}
$$
故这只是同一个完整源的整坐标运输。

## 4. 全部共振余数和高次理想的准确有限读数

对每个 $0\le i<e$，定义
$$
F_{m,i}(Z)=\sum_{k\ge0}b_{m,i+ek}Z^k\in\mathcal O[[Z]].
$$
于是 $\mathcal B_m(W)=\sum_{i=0}^{e-1}W^i F_{m,i}(W^e)$。
原全部首边界值消失，恰等价于
$$
\boxed{
\mathfrak r_{m,i}:=F_{m,i}(p)
=\sum_{k\ge0}p^k b_{m,i+ek}=0
\quad(0\le i<e).
}
\tag{14}
$$
这是 $\mathcal B_m$ 除以 $Q$ 的整余数
$\sum_{i<e}\mathfrak r_{m,i}W^i$；全部尾项按 $p^k$ 收敛。

更一般，对任意固定正整数 $\ell$，令
$$
\boxed{
\mathfrak r_{m,i,j}
=\sum_{k\ge j}\binom{k}{j}p^{k-j}b_{m,i+ek}
=\frac{F_{m,i}^{(j)}(p)}{j!},
\quad 0\le i<e,\quad0\le j<\ell.
}
\tag{15}
$$
这些都在 $\mathcal O$ 中，且
$$
\boxed{
Q^\ell\mid\mathcal B_m\text{ 于 }\mathcal O[[W]]
\iff
\mathfrak r_{m,i,j}=0\text{ 对所有 }i<e,\ j<\ell.
}
\tag{16}
$$
证明是将每个整 $F_{m,i}(Z)$ 在 $Z=p$ 展开。
其 Taylor 系数由 (15) 逐项收敛，模 $(Z-p)^\ell$ 只留 $j<\ell$；
余项整除 $(Z-p)^\ell$，商仍整。
代 $Z=W^e$ 即得完整 Weierstrass 余数。
这保留了每个原高尾，不用任意模 $p$ 提升替代实际 $\sigma$。

## 5. 原连接在这个坐标中的准确形式

定义同一个原正规解的变换
$$
\boxed{
Y_m(W)=H(W)^{-m}\mathcal R_m(WH(W)^d).
}
\tag{17}
$$
该式先在每个严格 $r<r_E$ 盘成立。
其中 $H^{\pm1}$ 是单位，$W\leftrightarrow X$ 是同盘 Tate 同构；
这是原 $z/u$ 内盘逆与本篇整 $u/v$ 同构的组合。

令
$$
a(W)=\frac{d}{dW}\log\left(\frac{\sigma(z(u(v)))T(u(v))}{v}\right)
\tag{18}
$$
先按正式 log 定义。
虽然 (18) 中的指数本身不被预支大盘解析，其导数却在整个 $|W|<1$ 解析。
具体地，若 $\Xi(u)=\zeta_{\rm W}(z(u))$，则
$$
d v^{d-1}a(W)
=\Xi(u)C(u)\frac{du}{dv}
 +\frac{d}{dv}\log T(u(v))-\frac1v.
\tag{19}
$$
右侧在 $v=0$ 的极相消，其余项全在开单位盘解析。
由原完整中央身份
$$
\frac{\sigma T}{v}=E_{\rm c}(X)H(W)
$$
及 $\mu_d$ 不变性，(19) 的正规级数只含 $v^{d-1+nd}$，
故除以 $d v^{d-1}$ 后确给整个开 $W$ 单位盘解析的 $a$。
因为 $H=1+O(W^e)$、$X=W+O(W^{e+1})$，其常数恰为原
$$
\boxed{a(0)=c=F_s,\qquad s=d/6,\qquad v_p(c)=-1.}
\tag{20}
$$

将 R639 的原方程逐项代入 (17)，得到
$$
\boxed{
Y_m'+ma(W)Y_m=k(W)\mathcal B_m(W),\qquad
k(W)=1+dW\frac{H'}H,\qquad Y_m(0)=j_m.
}
\tag{21}
$$
这里没有改变零初值缺陷的定义。
由 (8)，准确分离全部首边界极为
$$
\boxed{
k(W)=q+dW\frac{U'}U+\frac{de\,p}{W^e-p}.
}
\tag{22}
$$
故全部极来自 (7)，在每个根 $\xi$ 的留数为 $d\xi$，非零。

## 6. 完整连接在闭首边界及略外侧仍严格常数主导

为支付全盘延拓，必须在真正边界上证明严格范数差。
R639 的原 zeta 级数为
$$
\Xi(u)=u^{-1}J(bu^6),\qquad
J_n=\frac{\binom{-1/2}{n}}{1-6n}.
$$
若 $a_n=v_p(6n-1)$，该篇的完整进位计数给
$$
v_p(J_n)\ge-\lceil a_n/2\rceil,\qquad v_p(J_s)=-1.
\tag{23}
$$
在 $R=R_E$，$J_s b^s u^d$ 的权估值为 $-1+1/e<0$。
其它项仍严格较大：

- $a_n=0$ 的项整；
- $a_n=1$ 的最早指标为 $s$，其余指标严格更大；
- $a_n\ge2$ 时
$$
v_p(J_n)+\frac{6n}{q-1}
\ge-\lceil a_n/2\rceil+\frac{p^{a_n}+1}{p^2-1}>0.
$$
$a_n=2$ 的右侧为 $2/(p^2-1)$；之后的两步增长严格为正。
全部高尾趋于无穷，因为 (23) 只有对数大小的分母。

因此在真正闭 $R_E$ 盘上，
$$
\|J(bu^6)-J_s b^s u^d\|_{R_E}<pR_E^d.
\tag{24}
$$
整坐标给 $u/v$, $du/dv$ 均为常数一且离一的范数小于一，
$C(u)$ 也如此。
于是 (19) 的首项准确为 $J_s b^s v^{d-1}$，误差范数严格小于
$pR_E^{d-1}$。
被减去的 $1/v$ 虽有原点极，但其 Laurent 范数为 $R_E^{-1}$，
且
$$
R_E^{-1}<pR_E^{d-1}.
$$
$T$ 的 log 导数同样严格较小。
完整极相消及字符型已在 §5 支付，故可以除以 $d v^{d-1}$。
用 (20) 的实际常数再作一次常数项比较，得到
$$
\boxed{\|a-c\|_{r_E}<p.}
\tag{25}
$$

$a$ 在开单位盘解析，(25) 是严格不等式；
所以可选
$$
r_E<r_+<r_2
$$
使 $a$ 在闭 $r_+$ 盘 Tate，且仍有 $\|a-c\|_{r_+}<p$。
适当缩小 $r_+$ 后，(8) 的 $U^{\pm1}$ 也已在该盘付清。

令
$$
\mathcal D_m=(mc)^{-1}\partial_W+(a-c)/c .
$$
由于 $m$ 为单位，$|c|=p$、$r_+>p^{-1}$，
$$
\|\mathcal D_m\|_{r_+}
\le\max\{p^{-1}r_+^{-1},\,p^{-1}\|a-c\|_{r_+}\}<1.
\tag{26}
$$
所以
$$
(\partial_W+ma)^{-1}
=(mc)^{-1}\sum_{n\ge0}(-\mathcal D_m)^n
\tag{27}
$$
是闭 $r_+$ Tate 代数上的真实有界逆。
此论证包括全部系数和算子尾，不是边界局部解的选择。

## 7. 同一个正规解的准确闭盘充要条件

**定理。** 对本篇原 $Y_m$，下列条件等价：

1. $Y_m\in K\langle W/r_E\rangle$；
2. $Q\mid\mathcal B_m$ 于 $\mathcal O[[W]]$；
3. (14) 的全部 $e$ 个原准确余数为零；
4. $Y_m$ 延为某个 $r_+>r_E$ 闭盘上的 Tate 函数。

先证 1⇒2。将 (21) 乘 $Q$。
若 $Y_m$ 属于闭首盘，左右均在该盘解析，故由严格内盘身份延到整个闭盘。
在 $Q$ 的每个根 $\xi$ 评价，(22) 给
$$
0=de\,p\,\mathcal B_m(\xi).
$$
于是所有边界值都为零，由 §4 得整除。

反之若 2 成立，则 $k\mathcal B_m$ 在 §6 的闭 $r_+$ 盘解析，
因为 (22) 的全部简单极准确消掉。
应用 (27) 得该盘唯一 Tate 解。
将其限制到任意 $p^{-1}<r<r_E$，与 (17) 的原解满足同一方程。
同一常数主导逆保证两者相同，故确实延拓原 $Y_m$，给 4。
4⇒1 显然，2⇔3 是 (14)。

这个定理付清了 R660 在各点局部无 log 后尚未断言的全盘粘合，
但作用在明确写出的 (17) 上。
它没有将 $H^{-m}$ 看成首边界单位。

## 8. 同一个 j 的准确读数与原 X 闭盘的更强门

在任何 $p^{-1}<r<r_E$，(21)、(27) 的同一逆给
$$
\boxed{
j_m=(mc)^{-1}
\left[
\sum_{n\ge0}(-\mathcal D_m)^n
       \bigl(k(W)\mathcal B_m(W)\bigr)
\right]_{W=0}.
}
\tag{28}
$$
所有对象都是原来源；右侧保全部 $k$、$a-c$ 和 $\mathcal B_m$ 的高尾。
这是同一个原中央值的关系，不把它重命名为另一个积分。
但 (28) 为零并没有在本文被证明迫 (14) 的全部余数为零。

若要求 R660 原 $\mathcal R_m(X)$ 属于闭 $r_E$ Tate 代数，
则该篇真正的 $t^d$ 下降必要式经 (13) 整运输后仍给
$$
\boxed{
j_m=0,\qquad Q^{d-m}\mid\mathcal B_m.
}
\tag{29}
$$
由 (15)–(16)，第二条等价于全部
$\mathfrak r_{m,i,j}=0$，$i<e,\ j<d-m$。
它也使 $Y_m$ 延过边界，但反向不能仅由 §7 推出：
$\mathcal R_m=H^mY_m$ 还须按原 $X=WH^d$ 同时下降，
不是任意全盘 $Y_m$ 都有这个性质。
R660 的高次整除、首有理系数赋值及复增长必要条件都继续有效。

**待证接口保持明确：** 原两条 $j_{34}=j_{72}=0$ 与 (14)/(29) 或原全九格
所有实际 $D/k$ 层之间的算术联系尚未得到。
$v,\mathcal B_m,H,a$ 依赖 $p$，不是固定全局来源格中的免费新列。
本篇没有重用已在 R632/R635 证明的原 $p$ 次幂半径作为新结果；
尤其没有从该幂预支开单位盘解析。

## 来源

- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：
  原完整 $T_{\rm g}$、$c$、$j_m$、全 zeta 进位界和严格内盘唯一逆。
- [R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md)：
  同一个完整 $\Phi_m$、原首系数和真正 $X$ 闭盘的下降必要式。
- [R632](R632-original-pth-power-formal-group-boundary-and-full-kummer-range.md)、
  [R635](R635-all-original-powers-and-formal-logarithm-boundary.md)：
  原 $u/z$ 内盘逆和首形式群边界。
- Kiran S. Kedlaya, *Notes on class field theory*, §4.6,
  Proposition 4.6.7、Corollary 4.6.8、Remark 4.6.11，
  [作者正文](https://kskedlaya.org/cft/sec_lubin-tate.html)，2026-11-15 核读。
  本篇 §1 已重写所需严格整同构的系数证明，未调用未审定新预印本。
