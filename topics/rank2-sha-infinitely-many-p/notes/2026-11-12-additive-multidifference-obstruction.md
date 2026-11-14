# 固定加法逆像不能兼有第二个互素 CM 差分方程

日期：2026-11-12。**状态：已证明。**

本篇处理上一笔记的一个具体后续方案：试图用几个不同 CM 伸缩的
共同共振条件，改善同一个固定形式函数在各个素数处的整性。
下面证明，已经构造的逆像不能获得所需的第二个代数右端。
这不排除另行构造不同的共同对象、带平移的分布方程或非线性关系。

## 1. 设置与结论

沿用
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
f=34(1+i),\quad b=35+34i\equiv1\pmod f,
$$
以及
$$
\ell=\delta\log\Phi\in K(E),\qquad
(\sigma_b-1)^m F_m=\ell,\qquad F_m(O)=0,
\qquad m\ge1.
\tag{1.1}
$$
此处把形式解记作 $F_m$，以免与导子生成元 $f$ 混淆。
上一笔记已经证明其全平面亚纯延拓
$$
\widetilde F_m(z)=
\sum_{j\ge0}\binom{m+j-1}{j}
\ell\!\left(\operatorname{Exp}_E\frac{z}{b^{m+j}}\right).
\tag{1.2}
$$
$\ell$ 的极点集合 $S_0$ 非空，包含在 $E[f]$ 中，且 $[b]$ 固定它的每个点。
$\ell$ 在这些点都有简单极点：
$\ell\,\omega_E=d\log\Phi$ 的留数为非零整数 $\operatorname{ord}_s\Phi$。

**命题。** 设 $c\in\mathbb Z[i]$ 是非单位，并且理想 $(c)$ 与 $(bf)$ 互素。
对任意非零多项式 $P(X)\in\overline K[X]$，都有
$$
\boxed{P(\sigma_c)F_m\text{ 不代数于 }\overline K(E).}
\tag{1.3}
$$
同样结论对 $F_m$ 加任意代数常数后成立。

例如 $c=69$ 满足条件：$\gcd(69,68)=1$，且
$N(b)=2381$ 与 $69$ 互素。因此不可能存在代数函数 $R$ 使
$$
(\sigma_{69}-1)^rF_m=R\qquad(r\ge1).
\tag{1.4}
$$
这已经排除给同一个非实 CM 逆像再补一个整数伸缩中心方程的直接办法。

## 2. 一个能精确计数极点层数的复对数

固定一个复嵌入。因为 $\mathbb Z[i]$ 为主理想环，可把周期格写成
$\Lambda=\Omega\mathbb Z[i]$。
取 $s\in S_0$，写其某个复对数为 $\Omega\eta_0/f$，
其中 $\eta_0\in\mathbb Z[i]$。

由 $(bf,c)=1$ 及 $(b,f)=1$，中国剩余定理允许选择
$$
\eta\equiv\eta_0\pmod f,
\qquad \eta\equiv1\pmod{bc}.
\tag{2.1}
$$
于是
$$
z_s=\frac{\Omega\eta}{f}
$$
仍是 $s$ 的复对数，而且 $b\nmid\eta$、$c\nmid\eta$。
这里不要求这个复对数具有最小绝对值。

令
$$
u_n=b^{m+n}z_s\qquad(n\ge0).
$$
式 (1.2) 中第 $j\le n$ 项的内点是 $b^{n-j}z_s$，
对应 $s$，所以该项在 $u_n$ 有极点。
若第 $j>n$ 项有极点，其内点必须是 $f$-division 点，故
$$
f\frac{u_n}{b^{m+j}}
=\frac{\Omega\eta}{b^{j-n}}\in\Lambda.
$$
这迫使 $b^{j-n}\mid\eta$，与 (2.1) 矛盾。
因此在 $u_n$ 处，恰好前 $n+1$ 项贡献极点。

记 $r_s=\operatorname{ord}_s\Phi\ne0$，则
$$
A_n:=\operatorname{Res}_{z=u_n}\widetilde F_m(z)\,dz
=r_s b^m\sum_{j=0}^n\binom{m+j-1}{j}b^j.
\tag{2.2}
$$
并且
$$
\frac{A_n}{r_s b^{m+n}\binom{m+n-1}{n}}
\longrightarrow\frac{b}{b-1}\ne0.
\tag{2.3}
$$
证明可把和式按 $j=n-r$ 改写，再用几何级数作支配收敛。
特别地，$|A_n|\to\infty$。

## 3. 最高差分项的极点无法被低项消去

写
$$
P(X)=\sum_{j=0}^r a_jX^j,\qquad a_r\ne0.
$$
先设 $r\ge1$，并取
$$
z_n=c^{-r}u_n.
\tag{3.1}
$$
最高项 $a_r\widetilde F_m(c^rz)$ 在 $z_n$ 的留数为
$$
a_r c^{-r}A_n.
\tag{3.2}
$$

对任意 $j<r$，点 $c^jz_n$ 对应的椭圆曲线点不是 $f$-division 点。
否则
$$
f c^jz_n
=\frac{\Omega b^{m+n}\eta}{c^{r-j}}\in\Lambda,
$$
即 $c^{r-j}\mid b^{m+n}\eta$。
由 $(b,c)=1$ 得 $c\mid\eta$，与 (2.1) 矛盾。

另一方面，$\widetilde F_m$ 的全部极点都投影到 $S_0$：
若 (1.2) 的某一项在 $z$ 有极点，令其内点为 $s'\in S_0$，则
$$
\operatorname{Exp}_Ez=[b]^{m+j}s'=s'\in S_0.
$$
每个紧集上只有有限项可能有极点，余下项一致全纯收敛，
所以这确实控制整个和的极点。
因此所有 $j<r$ 项都在 $z_n$ 正则，不能消去 (3.2)。

## 4. 固定基点上的无界留数与代数性的矛盾

每个 $\operatorname{Exp}_Ez_n$ 属于有限群 $E[fc^r]$。
由于 $(b,fc^r)=1$，$[b]$ 在这个群上是双射。
因此 $n$ 限制到一个无限算术级数后，
$$
\operatorname{Exp}_Ez_n=u
$$
为同一个固定点。

反设 $P(\sigma_c)F_m$ 代数于 $\mathbb C(E)$。
其非零多项式关系延拓到整个亚纯函数
$$
G(z)=P(\sigma_c)\widetilde F_m(z).
$$
在上述固定投影点处，用 $w=z-z_n$ 写局部展开。
因为 $\operatorname{Exp}_E(z_n+w)=u+\operatorname{Exp}_Ew$，
所有 $G(z_n+w)\in\mathbb C((w))$ 都满足同一个
$\mathbb C((w))[Y]$ 中的非零多项式。
一个非零多项式只有有限多个根，故这些 Laurent 级数的留数只能取有限多个值。
但 (3.2) 的绝对值沿此子序列趋向无穷，矛盾。

若 $r=0$，则 $P(\sigma_c)F_m=a_0F_m$，直接在投影点 $s$ 使用 (2.2)
得到同样矛盾。给 $F_m$ 加常数只会给 $G$ 加常数，不影响任何留数。
命题得证。

## 5. 准确的适用边界

本命题比仅证明 $F_m$ 超越更强：它排除同一个 $F_m$ 在另一个互素 CM 伸缩下
满足任何**常系数、代数右端**的有限阶线性差分方程。
中心算子 $(\sigma_c-1)^r$ 属于这一范围。

不能据此断言所有多差分方法都失败。
例如带有 $E$ 上非恒定系数的方程、带平移的分布关系、非线性方程，
或者重新选择一个并非 (1.1) 逆像的共同对象，都未被本证明处理。
也不能先分别构造若干 $F_{m,b}$，再把它们的局部整素数集合当作同一个图像的整性。

本篇依赖 R19 的固定函数及前篇已证明的亚纯和，
其余论证在本篇完整给出，没有引用新的非消失或阶数猜想。
