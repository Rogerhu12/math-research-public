# 2026-11-14 — 两个惰性 forcing 的完整 addition 整卷积与首分母常数

**状态：已证明的同源恒等式；不另编号为主结论。** 本条保留 R533 两个完整 $S_6\otimes S_6$ 核的实际混合系数。它说明首 Gaussian 分母确有非零常数，但两份原整卷积仍能准确补偿；不能据该常数直接赋 $c_{4,p}$ 或 $c_{1,p}$ 非零。

取 $p=6s-1>71$、$b=17$，并允许 R586 的共同解析单位尺度。令
$$
a=2+\omega,\quad a^6=-27,\quad
f_4=x\sigma^6,\quad f_1=-xy\sigma^6,\quad
B_3=-y\sigma^3,\quad H=(x^3-2b)\sigma^6.
$$
原 $D x=2y$、$\sigma\sim z$ 规范下，
$$
H(z)=1-\frac{12b}{5}z^6+\cdots.
\tag{1}
$$
记实际特征零系数为
$$
C_{4,p}=[z^{p-1}]f_4,\qquad C_{1,p}=[z^{p-4}]f_1,
$$
其整性和约化 $c_4,c_1$ 已由 R586、R591 保留。另记
$$
c_p=\binom{3s-1}{2s-1}b^s\in k^\times.
\tag{2}
$$
这是 R356/R587 的第二类 Cartier 常数，不能与 $c_4,c_1$ 混同。

## 1. 完整双变量来源的两条精确行

R533 的两个全函数恒等式是
$$
F_P(u,v)=\sigma^3(u+v)\sigma(a(v-u))
=a[H\wedge f_4+2f_1\wedge f_3],
$$
$$
F_B(u,v)=B_3(u+v)\sigma(a(v-u))
=a[H\wedge f_1+6b f_3\wedge f_4],
\qquad f_3=-y\sigma^6.
\tag{3}
$$
按完整 $\mu_6$ 型取系数，右侧分别只剩
$$
\boxed{
[u^{p-1}v^6](F_P/a)=\frac{12b}{5}C_{4,p},
\qquad
[u^{p-4}v^6](F_B/a)=\frac{12b}{5}C_{1,p}.}
\tag{4}
$$
这里两边都是完整来源的真实混合 Taylor 行，没有先忘掉任一输入。

定义
$$
e_j=[z^{6j}](\sigma/z),\quad
d_j=[z^{6j}](\sigma/z)^3,\quad
b_j=[z^{6j}]B_3,
$$
$$
M(A,B)=[X^6](1+X)^A(X-1)^B
=\sum_{q=0}^6\binom Aq\binom B{6-q}(-1)^{B-6+q}.
\tag{5}
$$
则 (4) 在特征零准确展开为
$$
\frac{12b}{5}C_{4,p}
=\sum_{i+j=s}(-27)^j d_i e_j M(6i+3,6j+1),
$$
$$
\frac{12b}{5}C_{1,p}
=\sum_{i+j=s}(-27)^j b_i e_j M(6i,6j+1).
\tag{6}
$$
指数与 $\sigma(a(v-u))$ 的全部 $a$ 尺度均在 $(-27)^j$ 中保留。

## 2. 两个端点的绝对非齐次常数

令
$$
\gamma=[z^{p+1}]\log(\sigma/z).
$$
R356/R586 的规范是
$$
p\gamma\equiv-c_p\pmod p.
\tag{7}
$$
第一处 $p$ 分母恰给
$$
e_s=\gamma+\mathcal O,\qquad
d_s=3\gamma+\mathcal O,\qquad
b_s=3\gamma+\mathcal O.
\tag{8}
$$
所有 $e_j,d_j,b_j$（$j<s$）都整。后一个式子保持 $B_3(0)=1$；$y$ 在该窗口的系数整。

四个实际端点中的整数混合系数各含 $p$，且
$$
\begin{array}{c|cc}
& i=s,\ j=0 & i=0,\ j=s\\ \hline
F_P& M(p+4,1)/p=7/30&
 M(3,p+2)/p=7/10\\
F_B& M(p+1,1)/p=-1/12&
 M(0,p+2)/p=1/60
\end{array}
\pmod p.
\tag{9}
$$
例如 $M(p+4,1)=\binom{p+4}{5}-\binom{p+4}{6}$，除 $p$ 后分别为 $1/5$ 和 $-1/30$。其余三个用 (5) 同样直接计算。所有分母在 $p>71$ 为单位。

$p$ 惰性，所以 $a^p=\bar a$，因此
$$
(-27)^s=a^{p+1}\equiv a\bar a=3\pmod p.
\tag{10}
$$
结合 (8)–(10)，$F_P/a$ 的两个端点总和准确为
$$
\left(3\cdot\frac7{30}+3\cdot\frac7{10}\right)p\gamma
=-\frac{14}{5}c_p.
\tag{11}
$$
$F_B/a$ 的两个端点总和准确为
$$
\left(3\cdot\left(-\frac1{12}\right)
 +3\cdot\frac1{60}\right)p\gamma
=\frac15c_p.
\tag{12}
$$
没有把各自的有限整部分误乘成非零：它们在这里都另外带一个 $p$，模 $p$ 为零。

## 3. 完整整卷积与实际可用的结论

保留 (6) 中全部内部项，定义
$$
R_P=\sum_{\substack{i+j=s\\i,j\ge1}}
 (-27)^j\bar d_i\bar e_j M(6i+3,6j+1),
$$
$$
R_B=\sum_{\substack{i+j=s\\i,j\ge1}}
 (-27)^j\bar b_i\bar e_j M(6i,6j+1).
\tag{13}
$$
则两个指定 forcing 的真实非齐次式是
$$
\boxed{
\frac{12b}{5}c_4=R_P-\frac{14}{5}c_p,\qquad
\frac{12b}{5}c_1=R_B+\frac15c_p.}
\tag{14}
$$
相加得到
$$
\boxed{
R_P+14R_B=\frac{12b}{5}(c_4+14c_1).}
\tag{15}
$$
已知首分母常数在这一完整组合中恰消失。特别，若两个指定 forcing 都为零，则 (14) 要求的不是两个整卷积都为零，而是
$$
R_P=\frac{14}{5}c_p,\qquad R_B=-\frac15c_p.
\tag{16}
$$
两者都为单位，且满足 (15)。当前没有原 $S/T$ 算术中央条件把 (13) 两份实际卷积赋成零，所以 (14) 不能单独排除同时消失。

这也不能把 R533 的普通负矩 $I_4,I_1$ 与本条的惰性 prime-diagonal 系数换名；原地点、Gaussian 规范和完整单位域不同。若要接 R595 的原 $S_{34},T_{72}$ 对角，仍须将 (13) 与那两个完整来源的同参数行真正比较。

## 4. 精确复核

[check-inert-addition-regular-carries.mjs](../scripts/check-inert-addition-regular-carries.mjs)
在 R589/R592 已用的同一解析 $p=17$ 纤维、$b=1,2$ 上，用原有理级数核 (6) 的特征零等式、端点 (11)–(12)、全部整卷积 (13) 和组合 (15)。这是小的归一证书，不是新增素数扫描；一般证明已经由 (3)、(5)、(7)–(10) 完成。
