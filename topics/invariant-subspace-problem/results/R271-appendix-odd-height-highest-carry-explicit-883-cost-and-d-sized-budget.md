# R271 补录：奇高度最高 carry 逆费用的 $883$ 常数与 $R=d$ 预算

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost，根复核；AI-assisted GPT-6 Astra Pro。

## 0. 本条证明什么

本条为原 N、Y 两族的最高 carry 逐层参数给出完整物理 MP 的显式常数。
结论保留旧头全部 carry、完整 Boolean 强段及所有 primitive 链。
它与完整 Galerkin 源的二阶消失是不同问题：最后的 $517$ 主阶余量只是已经核清的条件预算，
不是原实际费用已经变小的断言。

沿用 [奇高度最高 carry 的完整 MP](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md)
的精确块与剪切身份；本条在 §4 重新列出该身份和使用方式。
旧真实头的逆芽与 Jordan 常数来自
[R239 真头 Jordan 费用](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)
§§1–3，尤其 (2.7)–(2.8)、(3.5)–(3.9)。

## 1. 记号与参考头

取 $m\ge4$，置
$$
n=2^{m-1},\qquad a=16^{m-2},\qquad b=b_{m-1}=m^{-2}.
$$
旧权 $d_i$ 固定，最高权改为
$$
d_{m-1}(t)=t\rho,\qquad \rho=d_{m-2}^2.
$$
原最高参数为
$$
t_{\rm act}=\frac{d_{m-1}}{d_{m-2}^2}.
$$
记
$$
\widehat A(1)=F_{m-1}(B_m(\rho)),
\tag{1.1}
$$
即参考最高权为 $\rho$、但删除最高 Boolean 项的 $2n$ 维头；
$F_{m-1}$ 是固定旧 N 或 Y 函数。
它仍是完整循环幂零头，$F_{m-1}'(0)=d_0^{-1}\ne0$。

原权指数为
$$
\Lambda_i=-\log d_i
=100\,16^i-105\,8^i+(150i+25)2^i
\le100\,16^i.
\tag{1.2}
$$
原相邻 carry $d_{i+1}/d_i^2$ 均不超过 $e^{-1070}$；
参考最高相邻 carry 等于 $1$。

### 引理 1.1

两族都满足
$$
\|\widehat A(1)\|<6.
\tag{1.3}
$$

**证明。** 令 $N_i=B_m(\rho)^{2^i}/d_i$，$i<m-1$。
若无需借位，其非零权等于 $1$；若向第 $j>i$ 位借位，
其权为相邻 carry 的乘积
$$
\prod_{k=i}^{j-1}\frac{d_{k+1}^{\rm ref}}{(d_k^{\rm ref})^2}\le1.
$$
故 $\|N_i\|\le1$。
对 $i\le m-3$，
$N_i^2=\kappa_i N_{i+1}$，其中
$\kappa_i=d_{i+1}/d_i^2\le e^{-1070}$，于是
$$
\|N_i(I+N_i)^{-1}\|
=\|(N_i-N_i^2)(I-N_i^2)^{-1}\|
\le\frac{1+\kappa_i}{1-\kappa_i}<3.
$$
对 $i=m-2$，参考最高 carry 等于 $1$，但 $N_i^4=0$，
所以 Cayley 项恰为 $N_i-N_i^2+N_i^3$，范数至多 $3$。
N 项范数至多 $1$，而 $\sum_i b_i<2$，得 (1.3)。证毕。

## 2. 参考头的 $441a$ 真实 Jordan 条件数

### 定理 2.1

存在物理相似
$$
\widehat A(1)=\widehat V J_{2n}\widehat V^{-1}
$$
满足
$$
\boxed{\kappa(\widehat V)\le e^{441a}.}
\tag{2.1}
$$

**证明。** 使用 R239 中旧 $m-1$ 位函数的圆盘
$$
\varrho=e^{-110\,8^{m-2}}
$$
及其真实解析逆芽 $\psi=F_{m-1}^{-1}$。
该父结果给出
$$
|[w^k]\psi(w)^j|
\le(2d_0)^k\varrho^{j-k},\qquad j\le k,
\tag{2.2}
$$
而 $j>k$ 时系数为零。
这里使用的是旧有限函数的解析逆，不是无限形式函数。

记新参考二进制权为 $W_j^{\rm ref}$。
它的位指数为旧 $\Lambda_i$（$i\le m-2$）
以及最高位 $2\Lambda_{m-2}$。
每一位都满足
$$
\Lambda_i^{\rm ref}\le100\,8^{m-2}2^i.
\tag{2.3}
$$
最高位也成立，因为
$2\Lambda_{m-2}\le200\,16^{m-2}
=100\,8^{m-2}2^{m-1}$。

构造真实伴随链矩阵
$$
\widehat K e_k=(\widehat A(1)^*)^ke_0,\qquad0\le k<2n.
$$
按 R239 的准确权位置，
$$
(\widehat K^{-1})_{kj}
=\frac{[w^k]\psi(w)^j}{W_j^{\rm ref}}.
\tag{2.4}
$$
由 $2d_0<1$、(2.2)–(2.3)，对 $j\le k$ 有
$$
\begin{aligned}
\log\!\left((W_j^{\rm ref})^{-1}\varrho^{j-k}\right)
&=110\,8^{m-2}k\\
&\quad+
\sum_{i\in\operatorname{bits}(j)}
(\Lambda_i^{\rm ref}-110\,8^{m-2}2^i)\\
&\le110\,8^{m-2}k<440a.
\end{aligned}
\tag{2.5}
$$
关键是保留同一个输入列的真实 $W_j^{\rm ref}$；
不能把权最坏值与逆芽最坏值独立相加。
所以
$$
\|\widehat K^{-1}\|\le2n\,e^{440a}.
$$
由 (1.3)，
$$
\|\widehat K\|\le\sqrt{2n}\,6^{2n-1}.
$$
且 $\widehat V=\widehat K^{-*}$ 给出所需相似。
对 $m\ge4,n\ge8$，
$$
\frac32\log(2n)+(2n-1)\log6<8n\le a=n^4/16.
$$
于是 $\log\kappa(\widehat V)\le441a$，证毕。

同一 R239 父结果对旧 $n$ 维头直接给
$$
A_{m-1}=V_{\rm old}J_nV_{\rm old}^{-1},\qquad
\kappa(V_{\rm old})\le e^{221a}.
\tag{2.6}
$$

## 3. 完整强段的物理 sl2 成本

取原连续强位 $i=m,\ldots,m+R-1$，其中 $R$ 偶，置
$$
B_R=\prod_{i=m}^{m+R-1}b_i^{-1},\qquad
D=A_{m-1}+D_{[m,m+R)}.
\tag{3.1}
$$
$R=0$ 时积为 $1$。

单位后移 $J_s$ 与标准 sl2 降算子
$$
L_se_j=\sqrt{j(s-j)}\,e_{j-1}
$$
对角相似，条件数恰为 $(s-1)!$。
例如取对角项
$\sqrt{j!(s-1)!/(s-1-j)!}$；
其首项为 $1$、末项为 $(s-1)!$，逐项比给出所需相似。

强 Boolean 删除和与未加权删除和的对角相似条件数为 $B_R$：
对 $T e_I=(\prod_{i\in I}b_i)e_I$，有
$D_{[m,m+R)}=T^{-1}D_{\rm unweighted}T$。
因此 $D$ 与标准 unitary sl2 张量和的总相似条件数至多
$$
K_D=e^{221a}(n-1)!B_R.
\tag{3.2}
$$
参考 $\widehat A(1)+D_{[m,m+R)}$ 的相应条件数至多
$$
K_{\widehat D}=e^{441a}(2n-1)!B_R.
\tag{3.3}
$$

标准 sl2 张量和正交分解为标准链；这是把各因子的升、降、权算子相加后，
用互为伴随的升降关系逐条取最高权向量得到的完整分解。
在一条长度 $L$ 的标准链上，$r$ 次降幂的每个非零奇值为
$$
\sqrt{(j)_r(L-j)^{\overline r}}\ge r!,
$$
因为两边各含 $r$ 个正整数，分别至少为 $r!$。
故完整物理 MP 满足
$$
\|(D^r)^\dagger\|\le K_D/r!,\qquad
\|((\widehat A(1)+D_{[m,m+R)})^r)^\dagger\|
\le K_{\widehat D}/r!.
\tag{3.4}
$$
若某个幂为零，其 MP 为零，式子仍成立。
这里所有 primitive 链均保留；非正交相似只通过明列的条件数进入。

## 4. 奇高度完整 MP 的显式界

令 $C_t=A_m(t)+D_{[m,m+R)}$，并取奇 $r\ge1$。
完整奇高度剪切恒等式为
$$
C_t^r=
\begin{pmatrix}
D^r&rbD^{r-1}+tT_r\\0&D^r
\end{pmatrix},
\qquad
D^{r-1}=D^rP+QD^r,
$$
其中可取
$$
P=(D^r)^\dagger D^{r-1},\quad
Q=(I-D^r(D^r)^\dagger)D^{r-1}(D^r)^\dagger.
$$
因为旧头维数为偶、强段长度为偶，$D$ 的全部链长为偶，
故没有链长恰为奇 $r$，上述恒等式成立。
左右固定剪切消去 $rbD^{r-1}$，剩余的完整矩阵由
$\operatorname{diag}(tI,I)$ 与 $t=1$ 参考矩阵相似。
构造完整真解并用 MP 最小性，得
$$
\|(C_t^r)^\dagger\|
\le\frac{(1+rbM_r)^2}{t}\,
\|((\widehat A(1)+D_{[m,m+R)})^r)^\dagger\|,
$$
其中 $M_r=\|D^{r-1}\|\|(D^r)^\dagger\|$。

原旧头范数小于 $6$，强尾权和小于 $2$，故 $\|D\|<8$。
由 (3.4)，
$$
M_r\le8^{r-1}K_D/r!.
$$
又 $K_D\ge1,r!\ge1$，因此
$1+rbM_r\le(1+rb)K_D8^{r-1}$。
代入 (3.2)–(3.4) 得：

### 定理 4.1

对 $m\ge4$、任意偶 $R\ge0$、任意奇 $r\ge1$、$0<t\le1$，
$$
\boxed{
\|(C_t^r)^\dagger\|
\le
t^{-1}e^{883a}
((n-1)!)^2(2n-1)!\,B_R^3\,
(1+rb)^2\,\frac{8^{2r-2}}{r!}.
}
\tag{4.1}
$$
同界适用于伴随 $r$ 次幂的完整 MP。
$883=2\cdot221+441$，分别记录两次物理剪切中的旧头成本
及参考全头的 Jordan 成本。

## 5. $R=d$ 时的主阶余量

取新头维数 $d=2n=2^m$、$R=d=2n$、$x=m+2n$，并取奇
$1\le r\le d$。记 (4.1) 除 $t^{-1}$ 外的右端常数为
$\mathcal C_{m,r}$。则
$$
\boxed{\log\mathcal C_{m,r}\le883a+21n\log x.}
\tag{5.1}
$$
事实上，
$$
2\log((n-1)!)+\log((2n-1)!)\le4n\log x,
$$
$$
3\log B_R=6\sum_{i=m}^{m+2n-1}\log(i+1)\le12n\log x,
$$
$$
(2r-2)\log8\le4n\log x,\qquad
2\log(1+rb)\le n\log x,
$$
而 $-\log r!\le0$。这些粗界对 $m\ge4$ 均成立。

原最高 carry 的精确指数为
$$
\begin{aligned}
-\log t_{\rm act}
&=\Lambda_{m-1}-2\Lambda_{m-2}\\
&=1400a-630\,8^{m-2}+300\,2^{m-2}.
\end{aligned}
\tag{5.2}
$$
所以若另行证明某个完整原 Galerkin 残差满足
$$
\|\xi_{m,r}(t_{\rm act})\|\le L_{m,r}t_{\rm act}^2,
\tag{5.3}
$$
则其完整真解满足条件估计
$$
\begin{aligned}
\log\|q_{m,r}\|
\le {}&\log L_{m,r}-517a+630\,8^{m-2}\\
&-300\,2^{m-2}+21n\log x.
\end{aligned}
\tag{5.4}
$$
特别，若同一参数序列上 $\log L_{m,r}=o(a)$，则右侧为
$-(517-o(1))a$。
纯远孔范数因子 $\sigma_{x,r}\le\sqrt{r!S_x^r}$
在允许高度 $r\ll\sqrt x/m$ 下只增加低于 $a$ 的阶数。

式 (5.3) 在原多 carry 族中尚未证明，且不能当成恒等式使用：
低层实际例子可以有非零最高 carry 极点。
本条支付的是完整 MP 与物理相似的统一常数；
真正未闭的仍是增长强段下原源的残余消失阶数。
