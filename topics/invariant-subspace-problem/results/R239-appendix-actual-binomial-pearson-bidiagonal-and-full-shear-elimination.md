# R239 附录：实际二项式 Pearson 双对角恒等式与全高度 shear 消元

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：本文双对角身份、所有端点的 shear 消元及两条实际范数线性关系已证明。把它们代入四次式后的统一正性仍需单独证明；本文不把该最后一步当成已完成。
- 独立精确核验：[948 项端点/完整最小范数核验](../notes/2026-11-13-binomial-pearson-bidiagonal-exact-check-0c.py)；这些检查验证恒等式实现，不代替下文结构证明。
- 输入：[全高度真实 MP、强制根与同源二维 shear](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)及[真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)。本文的 Pearson 与双对角证明是实际有限乘积权的直接计算，不适用于任意正底测度。

## 1. 实际参数和合法多项式空间

固定普通短串长 $q$、单位池长 $L\ge q$、短串权平方 $z>0$。二维异常位问题的相对出生为 $t=q-\delta\ge1$，高度为
$$
h=q+L+1-2t,\qquad D=\delta+1,\qquad 1\le D\le q,
\qquad h\ge2D-1.
$$
考虑旧高次首一问题：其高度为 $h+1$，权为
$$
\omega_j(r)=\frac{\binom qr z^r}{\binom L{j+r-D}},
\qquad I_j=\{r\in\{0,\ldots,q\}:0\le j+r-D\le L\},
\quad0\le j\le h+1.
\tag{1.1}
$$
只在 $I_j$ 上使用该权，全部权严格正。令 $\mathcal A_j^k$ 是次数至多 $k$、且在每个非法状态 $r\notin I_j$ 上为零的多项式空间。非法状态是真实强制根，而不是零分母的形式延拓。

令 $P_j$ 是 $\mathcal A_j^D$ 中唯一的首一最小范数多项式，写
$$
P_j(r)=r^D+c_jr^{D-1}+\cdots,\qquad a_j=\|P_j\|_{\omega_j}^2.
\tag{1.2}
$$
在 $1\le j\le h$，$\mathcal A_j^{D-1}$ 有唯一首一最小多项式 $Q_j$，且其平方范数准确是旧低次问题
$$
b_{j-1}=\|Q_j\|_{\omega_j}^2.
\tag{1.3}
$$
因为两个问题共用相同低、高强制根，这与已有 $b$ 序列的索引一致。两个端点 $\mathcal A_0^{D-1}=\mathcal A_{h+1}^{D-1}=\{0\}$；它们不对应有限 Gram。后文 $b_{-1}=b_h=\infty$ 只表示相应倒数项为零。

## 2. 跨阶 Pearson 身份及真实伴随

当两侧对应物理状态合法时，二项式直接给
$$
\boxed{(r+1)\omega_j(r+1)=z(q-r)\omega_{j+1}(r).}
\tag{2.1}
$$
另有
$$
(j+1+r-D)\omega_j(r)=(L-j+D-r)\omega_{j+1}(r)
\tag{2.2}
$$
在两权均有定义的重叠支撑成立。

定义
$$
\boxed{(\mathcal L_jF)(r)=(j+1-D+r)F(r)-rF(r-1)
=(j+1-D)F(r)+r\Delta^-F(r).}
\tag{2.3}
$$
它正是实际两串 $D$ 在完整 MP 多项式坐标中的表示；这里只需以下直接多项式性质。

对 $0\le j\le h$，$\mathcal L_j$ 将 $\mathcal A_{j+1}^k$ 映入 $\mathcal A_j^k$。其真实加权伴随在合法多项式上为
$$
\boxed{(\mathcal L_j^*G)(r)=(L-j+D-r)G(r)-z(q-r)G(r+1),}
\tag{2.4}
$$
并将 $\mathcal A_j^k$ 映入 $\mathcal A_{j+1}^{k+1}$。

证明伴随只需对 (2.3) 的第二项把 $r$ 换成 $r+1$，再用 (2.1)，第一项用 (2.2)。必须同时核边界：

- 输入在低端比输出多一个合法状态时，输出新非法点 $r=D-j-1$ 上，(2.3) 第一系数为零，另一项由已有强制根消失。
- 输入在高端比输出少一个合法状态时，新非法点 $r=L-j+D$ 上，(2.4) 第一系数为零，$G(r+1)$ 为旧强制根。
- 其余非法状态的两个函数值均已为零；$r=0$、$r=q$ 的外侧移位分别由 $r$、$q-r$ 因子消失。

因此重索引没有引入非法权或丢弃边界项。这一检查同样覆盖零阶和最高相邻阶。

## 3. 完整双对角公式

$\mathcal L_j$ 作用在首一 $k$ 次多项式上的最高系数是 $j+1-D+k$；$\mathcal L_j^*$ 作用在首一 $k$ 次多项式上的最高 $k+1$ 次系数是 $z-1$。

对 $1\le j\le h$，准确有
$$
\boxed{
\mathcal L_jP_{j+1}=(j+1)P_j+(z-1)\frac{a_{j+1}}{b_{j-1}}Q_j.
}
\tag{3.1}
$$
**证明。** 若 $R\in\mathcal A_j^{D-2}$，则 $\mathcal L_j^*R\in\mathcal A_{j+1}^{D-1}$，所以
$$
\langle\mathcal L_jP_{j+1},R\rangle_{omega_j}
=\langle P_{j+1},\mathcal L_j^*R\rangle_{omega_{j+1}}=0.
$$
因此其正交展开只剩 $P_j,Q_j$。最高系数给第一项 $(j+1)P_j$。而 $\mathcal L_j^*Q_j$ 的最高系数为 $z-1$；减去 $(z-1)P_{j+1}$ 后属于 $\mathcal A_{j+1}^{D-1}$，故与 $P_{j+1}$ 正交。于是 $Q_j$ 的系数为 $(z-1)a_{j+1}/b_{j-1}$。若其中某个更低空间为零，同一证明仍成立。

$j=0$ 时低次空间为零，准确退化为 $\mathcal L_0P_1=P_0$。$j=h$ 时输入高次最小多项式已处在最高硬端点，(2.4) 保其全部强制根，所以 (3.1) 仍成立。

比较 (3.1) 的次高系数。因为
$$
r\Delta^-r^D=Dr^D-\frac{D(D-1)}2r^{D-1}+\cdots,
$$
得到
$$
\boxed{
jc_{j+1}-(j+1)c_j-\frac{D(D-1)}2
=(z-1)\frac{a_{j+1}}{b_{j-1}},\qquad1\le j\le h.
}
\tag{3.2}
$$
$j=0$ 的左侧为零，因为 $P_0(r)=r(r-1)\cdots(r-D+1)$，其 $c_0=-D(D-1)/2$。

若使用中矩形 $S_j$ 与 $f_j=\log S_j$，旧完整 Schur 身份给 $c_j=-D(D-1)/2-f_j'$，所以等价地
$$
\boxed{(j+1)f_j'-jf_{j+1}'=(z-1)a_{j+1}/b_{j-1}.}
\tag{3.3}
$$
本文不需要先假设任何 Turán 导数单调性。

## 4. 两种方向的全高度 shear 消元

异常位的准确剪切是 $k_j=c_{j+1}-c_j$。在相邻位置 $1\le n<h$，写
$$
x_n=k_{n-1}-k_n=2c_n-c_{n-1}-c_{n+1},
$$
$$
y_n=k_{n+1}-k_n=c_{n+2}-2c_{n+1}+c_n.
$$
对 (3.2) 作相邻差，得到
$$
\boxed{
x_n=\frac{z-1}{n}
\left(\frac{a_n}{b_{n-2}}-\frac{a_{n+1}}{b_{n-1}}\right),
\qquad
y_n=\frac{z-1}{n+1}
\left(\frac{a_{n+2}}{b_n}-\frac{a_{n+1}}{b_{n-1}}\right).
}
\tag{4.1}
$$
$n=1$ 时第一式的 $a_1/b_{-1}$ 准确取零，来自 $\mathcal L_0P_1=P_0$。

再用真正的坐标补集 $r\mapsto q-r$。首一多项式及范数满足
$$
c_j(z)=-Dq-c_{h+1-j}(1/z),\quad
a_j(z)=z^q a_{h+1-j}(1/z),\quad
b_j(z)=z^q b_{h-1-j}(1/z).
\tag{4.2}
$$
这些等式直接来自强制根、二项式和首一符号 $(-1)^D$，不是非正交源的任意运输。它们给
$$
k_j(z)=k_{h-j}(1/z),\quad
x_n(z)=y_{h-n}(1/z),\quad y_n(z)=x_{h-n}(1/z).
$$
将 (4.1) 代入并准确保留 $1/z-1=-(z-1)/z$，得到反向公式
$$
\boxed{
x_n=\frac{z-1}{z(h+1-n)}
\left(\frac{a_n}{b_n}-\frac{a_{n-1}}{b_{n-1}}\right),
}
\tag{4.3}
$$
$$
\boxed{
y_n=\frac{z-1}{z(h-n)}
\left(\frac{a_n}{b_n}-\frac{a_{n+1}}{b_{n+1}}\right).
}
\tag{4.4}
$$
$n=h-1$ 时最后的 $a_h/b_h$ 准确取零。两个硬端均已支付，四个等式保持原首一范数，没有丢掉倒数权的 $z$ 缩放。

## 5. 四次式局部变量的两条额外实际关系

使用已付完整四次式的记号
$$
a=a_{n-1},\ b=a_n,\ c=a_{n+1},\ d=a_{n+2},
\quad p=b_{n-2},\ q=b_{n-1},\ r=b_n,\ s=b_{n+1}.
$$
这里局部 $q$ 不再表示头数；局部 $s$ 为最后一个低次范数。四个剪切表达式是
$$
x=\frac{z-1}{n}(b/p-c/q)
=\frac{z-1}{z(h+1-n)}(b/r-a/q),
$$
$$
y=\frac{z-1}{n+1}(d/r-c/q)
=\frac{z-1}{z(h-n)}(b/r-c/s).
\tag{5.1}
$$
于是全部正 $z$ 均满足
$$
\boxed{z(h+1-n)(b/p-c/q)=n(b/r-a/q),}
\tag{5.2}
$$
$$
\boxed{z(h-n)(d/r-c/q)=(n+1)(b/r-c/s).}
\tag{5.3}
$$
对 $z\ne1$ 可直接相消；$z=1$ 用有限正权 Gram 的解析性延拓。因此这些关系在相等两权时也非空，不是只写成 $0=0$。

例如它们可以精确消去两端高次范数：
$$
a=\frac{qb}{r}-\frac{z(h+1-n)qb}{np}+\frac{z(h+1-n)c}{n},
$$
$$
d=\frac{rc}{q}+\frac{n+1}{z(h-n)}\left(b-\frac{rc}{s}\right).
\tag{5.4}
$$
低端 $p=\infty$、高端 $s=\infty$ 仍只表示消掉相应倒数项。

这两条关系是任意正底测度不具有的实际二项式耦合。旧两条 scalar log 凸性加任意 shear 当然不够；本文把 shear 的自由度消掉，并精确给出了可供统一四次正分解使用的额外范数条件。将 (5.1)–(5.4) 代回后是否有充分正分解，是下一步必须真实完成的数学命题。
