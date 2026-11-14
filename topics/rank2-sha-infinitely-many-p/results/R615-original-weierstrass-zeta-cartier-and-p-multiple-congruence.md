# R615 — 原 Weierstrass–zeta 有限 Cartier 身份与全部 p 倍指标同余

日期：2026-11-14。**状态：已证明。**

本篇证明 R614 所需的全部 $p$ 倍指标同余。证明只用原椭圆参数、原有理二项式系数、一个明确的进位计算和同一留数换元；不使用待证的 Gaussian 后 sigma 整性。

## 1. 原坐标与准确窗口

设
$$
p=6s-1>71,\qquad b=17,\qquad
x(z)=z^{-2}\sum_{n\ge0}X_nw^n,\quad w=z^6,\quad X_0=1.
\tag{1}
$$
保持 $Dx=2y$、$y\sim-z^{-3}$、$y^2=x^3+b$。在原点选
$$
u=x^{-1/2}\sim z,\qquad t=bu^6.
$$
于是准确的特征零恒等式为
$$
dz=C(t)\,du,\qquad
z=uH(t),\qquad
\zeta(z)=u^{-1}J(t),
\tag{2}
$$
其中 $\zeta=D\log\sigma$，且
$$
C(t)=(1+t)^{-1/2}=\sum_{n\ge0}C_nt^n,\qquad
C_n=\frac{(-1)^n}{4^n}\binom{2n}{n},
$$
$$
H(t)=\sum_{n\ge0}\frac{C_n}{6n+1}t^n,\qquad
J(t)=\sum_{n\ge0}\frac{C_n}{1-6n}t^n.
\tag{3}
$$
式 (2) 的 $\zeta$ 规范由 $D\zeta=-x$、奇性及首项 $z^{-1}$ 唯一决定；没有加一个未指定常数。

本篇使用
$$
M=p(s-1),\qquad
L=\frac{p^2-1}{6}=s(p-1),\qquad
M<L.
\tag{4}
$$
先证明 $H$ 的全部 $n\le M$ 系数整，再在这个**同一窗口**完成 $p$ 倍系数提取。

## 2. H 的唯一进位块

令
$$
m=\frac{p-1}{2}=3s-1,\qquad
r_0=p-s=5s-1.
\tag{5}
$$
定义两个实际有限多项式
$$
P(t)=\sum_{r=0}^{m}\frac{\bar C_r}{6r+1}t^r,
$$
$$
B(t)=\sum_{j=0}^{s-2}
 \frac{(2j+1)\bar C_j}{6j+5}t^j.
\tag{6}
$$
这里所有分母都是单位。尤其 $B$ 只定义到 $s-2$；不把 $j=s-1$ 的新 $p$ 分母并入约化级数。

令
$$
\delta=
-\frac{(-1)^{r_0}}{4^{r_0}}\,
\frac{(2r_0-p)!}{r_0!^2}\in\mathbf F_p^\times.
\tag{7}
$$

**引理 1。** $H_n=C_n/(6n+1)$ 对全部 $0\le n\le M$ 整，并且
$$
\boxed{
H(t)=P(t)\,C(t^p)
+\delta t^{r_0}B(t^p)
\pmod{(p,t^{M+1})}.
}
\tag{8}
$$
此外
$$
\boxed{\delta\,\bar C_s=\frac1{2s}=3\quad\text{于 }\mathbf F_p.}
\tag{9}
$$

证明。写 $n=pa+r$，$0\le r<p$。在当前窗口，
$a\le s-1$，故 $2a+1<p$。

若 $r\le m$，二项式没有个位进位，Lucas 公式给
$$
\bar C_n=\bar C_a\bar C_r.
$$
此时 $6r+1$ 不为零，得到 (8) 的第一块。

若 $r>m$，则 $\binom{2n}{n}$ 恰有一次 $p$ 进位。除去这一个 $p$ 后，分块阶乘的单位部分给
$$
\boxed{
\frac{C_{pa+r}}p
\equiv
-\frac{(-1)^r}{4^r}
 \frac{(2r-p)!}{r!^2}\,
 (2a+1)\bar C_a
\pmod p.
}
\tag{10}
$$
这里没有第二次高位进位，因为 $2a+1<p$。

在 $n\le M$ 时 $6n+1<p^2$，故原分母至多含一个 $p$。它含 $p$ 当且仅当 $r=r_0$。若 $r\ne r_0$，$H_n$ 的约化为零；若 $r=r_0$，则 $a\le s-2$，且
$$
6n+1=p(6a+5).
$$
用 (10) 消去唯一的 $p$，恰得 (8) 的第二块。这同时证明了全窗口整性，而非只证明被选中的指标。

最后用 $r_0=p-s$ 和 Wilson 的阶乘互补式化简：
$$
\delta=
(-1)^s4^{s-1}\frac{(s-1)!^2}{(2s-1)!},
\qquad
\bar C_s=(-1)^s4^{-s}\frac{(2s)!}{s!^2}.
$$
相乘即为 $1/(2s)$。因为 $6s=p+1$，这在模 $p$ 下是 $3$。证毕。

## 3. 同一有限窗口的两个 Cartier 提取式

对系数在 $\mathbf F_p$ 中的有限可约化级数，记
$$
\mathscr C_p\!\left(\sum a_nt^n\right)
=\sum a_{pn}t^n.
\tag{11}
$$
这是本篇明确的系数提取算子；没有将它作为新的固定全局来源加入原格。

**引理 2。** 在 $0\le n<s$ 的全部输出窗口，
$$
\boxed{
\mathscr C_p(CH)=CJ,\qquad
\mathscr C_p(H^2)=CJ
\pmod{t^s}.
}
\tag{12}
$$

证明先用真正的二项式恒等式
$$
C(t)=(1+t)^m C(t^p)\quad\text{于 }\mathbf F_p[[t]].
\tag{13}
$$
它可以由两边平方及常数项 $1$ 直接核定。

将 (8) 乘以 (13)。多项式 $(1+t)^mP(t)$ 的次数为 $p-1$，其 $p$ 倍指数只有常数项。另一个块
$t^{r_0}(1+t)^m$ 的范围中只有一次 $p$ 倍指数，即 $p$；其系数为 $C_s$。因此
$$
\mathscr C_p(CH)
=C^2+\delta C_s\,tCB
=C^2+3tCB.
\tag{14}
$$
由原二项式递推
$$
C_{j+1}=-\frac{2j+1}{2j+2}C_j
$$
准确得到
$$
\boxed{3tB=J-C\pmod{t^s}.}
\tag{15}
$$
这证明第一式。

对 $H^2$，$P^2$ 的次数同样为 $p-1$。交叉项的唯一 $p$ 倍指数系数是
$$
2P_s=\frac{2C_s}{6s+1}\equiv C_s.
$$
最后的 $t^{2r_0}B(t^p)^2$ 没有 $p$ 倍指数，因为 $2r_0$ 不被 $p$ 整除。因此同样得到 (14)，证明第二式。所有被取系数至多为 $p(s-1)=M$，完全位于引理 1 已付的实际窗口。

## 4. 两个原留数给出完整 p 倍同余

令
$$
A(w)=z^2x(z)=\sum X_nw^n,\qquad
Z(w)=z\zeta(z)=\sum Z_nw^n.
\tag{16}
$$
同一个原参数换元 (2) 给出两条特征零留数恒等式：
$$
\boxed{
X_n=b^n[t^n]\,C H^{1-6n},\qquad
Z_n=b^n[t^n]\,C J H^{-6n}.
}
\tag{17}
$$
例如第一式来自
$$
\operatorname{Res}_{z=0}x(z)z^{-6n+1}dz
=
\operatorname{Res}_{u=0}u^{-6n-1}C(t)H(t)^{1-6n}du;
$$
第二式同理，使用 $z\zeta=HJ$。这些公式没有引入可能为零的 Lagrange 分母。

取 $1\le k<s$。由引理 1，(17) 中计算 $X_{pk}$ 所需的所有 $H$ 系数都整；因此可以在整个窗口准确使用 Frobenius：
$$
\begin{aligned}
\overline{X_{pk}}/b^{pk}
&=[t^{pk}]\,CH\,(H^{-6k})^p\\
&=[t^k]\,\mathscr C_p(CH)\,H^{-6k}\\
&=[t^k]\,CJH^{-6k}.
\end{aligned}
\tag{18}
$$
由 (17)，最后一项正是低系数 $Z_k/b^k$。更一般保系数 Frobenius 时得到
$$
\boxed{\overline{X_{pk}}=\overline{Z_k}^{\,p}\qquad(0\le k<s).}
\tag{19}
$$
在本题的 $b=17$ 残数域中这就是普通的 $\mathbf F_p$ 等式。

另一方面，原 $D\zeta=-x$ 给
$$
6w\partial_w Z=Z-A.
$$
故对于 $k\ge1$，
$$
(6k-1)Z_k=-X_k.
\tag{20}
$$
当前 $1\le k<s$ 的 $6k-1$ 全为单位。合并 (19)、(20) 得到本篇主结论。

**定理 3。**
$$
\boxed{
X_{pk}\equiv-\frac{X_k^p}{6k-1}\pmod p,
\qquad 1\le k<s,\quad pk<L.
}
\tag{21}
$$
这里 $X_n$ 是原 $z^2x(z)$ 的真实系数，$b=17$ 尺度和 Frobenius 均已保留。式 (19) 还给出原 Weierstrass 系列与原 zeta 系列的整个有限 Cartier 对应，而非仅核 $k=1$。

## 5. 使用范围

本篇证明没有先假设
$\exp(6(\log(\sigma/z)-c w^s))$ 整，也没有由该整性反推 (21)。所以 (21) 可以独立用于 R614 的 Dwork 比较；R614 的全 addition 证明若另行付清，也只是相容的另一条路径。

$J$ 在本篇只读取 $n<s$。$n=s$ 的原 zeta 共振及更高窗口的分母没有在式 (12)、(19) 中被忽略。这里不声称同一个结论在全部 $k$ 或全部 $n$ 无条件继续成立，也未把这个有限系数算子认作原真前缀稳定算子。

## 6. 精确证书

[check-r615-weierstrass-zeta-cartier.mjs](../scripts/check-r615-weierstrass-zeta-cartier.mjs) 只复用既有 $p=17,23$ 的合法 $b=1,17$ 纤维，完成 247 项精确检查，逐个核：

- $H$ 的整个 $n\le p(s-1)$ 实际有理系数整性和唯一进位块；
- $\delta C_s=3$、两条完整有限系数提取式；
- 独立从原 Weierstrass 有理递推计算的全部 $X_{pk}$ 与 (21)；
- 所有截断和单位分母边界。

一般证明由 §§2–4 给出，不是由有限纤维归纳。它没有把原指定 $c_{4,p},c_{1,p}$ 或原 S/T 中央导数判为非零，原主目标仍需继续。
