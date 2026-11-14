# 迭代 GM Frobenius、准确 Hodge 截断与惰性完整导数证书

日期：2026-11-12。状态：本文的迭代矩阵、可除 $p$ 的锐界、
完整导数的有限证书及输入精度界均已证明。
尚未证明这些证书对无穷多个素数成功；主问题仍未完成。

本文固定 $p\ge7$、$p\equiv3\pmod4$。
模参数 $t=\lambda_{\rm Leg}-1/2$ 与 theta 的加法参数 $z$ 不同。
所有赋值以 $v_p(p)=1$ 规范，$v_p(0)=+\infty$。

## 1. 实际固定对象及高权问题

沿用 [R66](../results/R66-full-weight-one-and-fixed-division-unit-model.md)
和 [R68](../results/R68-integral-crystalline-frobenius-and-exact-critical-comparison.md)：

$$
s=1-4t^2,\qquad
Y(t)=\begin{pmatrix}K&L\\ K'&L'\end{pmatrix},\qquad
Y(0)=I,\qquad \det Y=s^{-1},\qquad J=L/t.
\tag{1.1}
$$

这里 $K,L$ 满足

$$
s y''-8ty'-y=0,\qquad
K(0)=1,\ K'(0)=0,\ L(0)=0,\ L'(0)=1.
$$

固定代数函数 $M_1\in t^4\mathbb Z_p[[t]]$ 的首系数为一。
它是实际 $68$ 阶除法单位模型产生的函数，不随 $p$ 重新选取。
实际全权一系数为

$$
\boxed{\quad
C_m=[t^m]\frac{M_1K^m}{sJ^{m+1}}
 =\frac{m!}{24\,17^{m-4}}\beta_m^2\quad(4\mid m),
\quad \beta_m=[z^m]A_1(z).
\quad}
\tag{1.2}
$$

$A_1$ 是已认证的次数十七目标截面，$\beta_4=1$。
整个固定序列及普通、惰性的完整门槛已见
[固定原函数 Bockstein 笔记](2026-11-12-fixed-primitive-bockstein-and-complete-depth.md)。
本文增加的是：在任意层

$$
k=p^n,\qquad m=(p+1)p^n,\qquad n\ge0,
\tag{1.3}
$$

用真实迭代 Frobenius 完全恢复 (1.2)，并明确允许的除 $p$ 和所需精度。
首层 $U_p,V_p$ 的短 jet 等式不能未经证明移到这些高权。

## 2. 真实迭代矩阵与特征零完全相等的恢复式

在 R68 的行约定下，实际 crystalline Frobenius 满足

$$
F(t)=Y(t^p)F_0Y(t)^{-1}\in M_2(\mathbb Z_p[[t]]),
\qquad
F_0=\begin{pmatrix}0&p\alpha\\ \beta&0\end{pmatrix},
\quad\alpha\beta=-1,
\quad\alpha,\beta\in\mathbb Z_p^\times.
\tag{2.1}
$$

这里 $\alpha,\beta$ 是矩阵常数；$\beta$ 不表示 theta 系数 $\beta_m$。
所有系数均在 $\mathbb Q_p$，所以迭代中的系数 Frobenius 是恒等。
定义

$$
F_{[h]}(t)=F(t^{p^{h-1}})\cdots F(t^p)F(t).
$$

逐项消去中间的 $Y^{-1}Y$，得到准确公式

$$
\boxed{\quad
F_{[h]}=Y(t^{p^h})F_0^hY(t)^{-1},\qquad
\det F_{[h]}=p^h\frac{s(t)}{s(t^{p^h})}.
\quad}
\tag{2.2}
$$

特别 $F_{[h]}$ 完整地整。另一方面

$$
F_0^{2a}=(-p)^aI,\qquad
F_0^{2a+1}=(-p)^aF_0.
\tag{2.3}
$$

置 $Q_h=F_0^{-h}F_{[h]}$。因 $Y(t^{p^h})=I+O(t^{p^h})$，
在特征零级数环中

$$
\boxed{\quad Q_h=Y^{-1}+O(t^{p^h}).\quad}
\tag{2.4}
$$

(2.4) 是次数断言，不是整性断言。事实上 $Y^{-1}$ 有真正的 $p$ 分母。

对 (1.3) 统一取 $h=n+2$，则 $p^h>m$。
因为 $M_1$ 从四次开始，(1.2) 只需 $K,J$ 到次数 $m-4$，
亦即 $L$ 到次数 $m-3$。
由 $Y^{-1}=s\begin{pmatrix}L'&-L\\-K'&K\end{pmatrix}$，
定义所需截断

$$
\mathcal K_h=(Q_h)_{22},\qquad
\mathcal L_h=-(Q_h)_{12}/t.
$$

在上述范围内它们分别准确等于 $sK,sJ$，常数项均为一。
因此有不丢失任何 $p$ 进精度的高权恢复式

$$
\boxed{\quad
C_m=[t^m]M_1\frac{\mathcal K_h^m}{\mathcal L_h^{m+1}},
\qquad h=n+2.
\quad}
\tag{2.5}
$$

这是从同一实际 rank-two Frobenius 取得的完整高权公式。
其指数和 jet 长度仍随 $p,n$ 增长；没有把它称为固定维数的线性矩阵条目。

### 2.1 偶数次迭代完全消去中心周期单位

还可以不把 $\alpha,\beta$ 当作计算输入。定义真实的二次 Frobenius

$$
G_p(t)=F_{[2]}(t)=-p\,Y(t^{p^2})Y(t)^{-1}.
\tag{2.6}
$$

因 $K,L$ 的系数有理，且左边是真实整 Frobenius 的乘积，

$$
G_p\in M_2(\mathbb Q[[t]])\cap M_2(\mathbb Z_p[[t]]),
\qquad G_p(0)=-pI.
\tag{2.7}
$$

这不是仅在中心纤维成立的矩阵：右边给出整个形式盘的准确式。
它的全部所需系数可以用 (1.1) 的有理递推有限计算；
整性来自 (2.6) 的实际晶体解释，不能由分别估计两个非整周期来省略。

令 $a=\lceil(n+2)/2\rceil$，并取

$$
G_{p,[a]}=G_p(t^{p^{2a-2}})\cdots G_p(t^{p^2})G_p(t).
$$

则

$$
G_{p,[a]}=(-p)^aY(t^{p^{2a}})Y(t)^{-1},\qquad
(-p)^{-a}G_{p,[a]}=Y^{-1}+O(t^{p^{2a}}).
\tag{2.8}
$$

因为 $p^{2a}>m$，(2.5) 可以直接以
$Q=(-p)^{-a}G_{p,[a]}$ 取代 $Q_h$。
因此完整高权证书只需实际有理的 $p^2$-Frobenius，不需要先计算
$\alpha,\beta$ 的 $p$ 进周期规范。
偶数层归一仍然可能非整；它的准确代价由下一节给出。

## 3. 迭代矩阵可共除多少个 $p$：锐的截断界

### 3.1 单步矩阵的真实首项

由 (2.1)、$K'=t+\cdots$、$L=t+\cdots$，以及 R68 的整个第一行除 $p$，

$$
\begin{array}{ll}
F_{11}\in pt\mathbb Z_p[[t]],&[t]F_{11}=-p\alpha,\\
F_{12}\in p\mathbb Z_p[[t]],&F_{12}(0)=p\alpha,\\
F_{21}\in\mathbb Z_p[[t]],&F_{21}(0)=\beta,\\
F_{22}\in t\mathbb Z_p[[t]],&[t]F_{22}=-\beta.
\end{array}
\tag{3.1}
$$

后两条非零首项和第一行的整除均适用于真实族，不仅适用于 $t=0$。

### 3.2 锐界定理

对 $1\le b\le\lfloor h/2\rfloor$，令

$$
d=h-2b+1,\qquad \tau(h,b)=p+p^2+\cdots+p^d.
$$

则

$$
\boxed{\quad
F_{[h]}\in p^bM_2(\mathbb Z_p[[t]])+
t^{\tau(h,b)}M_2(\mathbb Z_p[[t]]),
\quad
v_p([t^{\tau(h,b)}](F_{[h]})_{21})=b-1.
\quad}
\tag{3.2}
$$

所以 $F_{[h]}/p^b$ 在次数严格小于 $\tau(h,b)$ 时整；
在该边界次数已不整。

**证明。** 展开矩阵乘积的一条路径，从最左的 $j=h-1$ 因子走到
最右的 $j=0$ 因子。设路径有 $a$ 次从行状态一出发。
由 (3.1)，它至少带因子 $p^a$。
每个对角步骤另至少带 $t^{p^j}$；非对角步骤可取非零常数。

一条具有 $a$ 次行状态一的路径，非对角步骤至多为 $2a+1$：
$1\to2$ 至多 $a$ 次，$2\to1$ 至多 $a+1$ 次。
若恰达到上界，则必须从状态二开始、在状态一结束，
且所有状态一步骤均为 $1\to2$。
特别最后的 $j=0$ 步骤必须为 $2\to1$，不能是对角步骤。

当 $a\le b-1$ 时至少有 $h-2a-1$ 个对角步骤。
若非对角数达到上界，其最小可能总次数是

$$
p+p^2+\cdots+p^{h-2a-1}.
\tag{3.3}
$$

若非对角数较少，至少有 $h-2a$ 个对角步骤；即使把它们放到最低的
次数 $p^0,\ldots,p^{h-2a-1}$，其总次数也严格大于 (3.3)。
所以任何含少于 $b$ 个 $p$ 的路径都从次数至少 $\tau(h,b)$ 才能出现。
这证明 (3.2) 第一部分。

在次数恰为 $\tau(h,b)$ 且 $p$ 因子恰为 $p^{b-1}$ 时，路径唯一：
最高的 $2b-2$ 个因子交替走非对角步骤；
$j=d,d-1,\ldots,1$ 均取 $2\to2$；最后 $j=0$ 取 $2\to1$。
它贡献的首项为

$$
(-p)^{b-1}(-\beta)^d\beta\,t^{\tau(h,b)}.
\tag{3.4}
$$

其他路径若能达到这个次数，必含至少 $b$ 个 $p$。
(3.4) 的单位首项因而不可能被它们消去，第二部分得证。$\square$

### 3.3 高权目标窗口中，最大共同整除恰为一个 $p$

仍取 $h=n+2,m=(p+1)p^n$。令 $b=1$，则

$$
\tau(h,1)=p+p^2+\cdots+p^{n+1}>m-3.
$$

这里 $n=0$ 时是 $p>p-2$；$n=1$ 时边界恰为 $m$，
所以这两层也不能把结论误写成“直到全部 $m$ 阶均整”。
在实际所需的周期窗口 $0\le j\le m-3$ 内，准确有

$$
F_{[n+2]}/p\in M_2(\mathbb Z_p[t]/t^{m-2}).
\tag{3.5}
$$

当 $n=0,1$ 时，$F_0^{n+2}$ 已有一个条目赋值恰为一，
所以不能共除 $p^2$。
当 $n\ge2$ 时，(3.2) 的 $b=2$ 给

$$
\tau(n+2,2)=p+p^2+\cdots+p^{n-1}<m-3,
$$

且该次数的 $(2,1)$ 条目赋值恰为一。因此同样不能共除 $p^2$。

这明确解释了为何中心纤维 $F_0^h$ 的 $p^{\lfloor h/2\rfloor}$
整除不能免费搬到整个目标 jet。
(3.5) 的行列式为 $p^n$ 乘单位；当 $n>0$ 时也不是一个整可逆换基。
本结论没有对截断环宣称未经证明的 Smith 对角化。

## 4. 真实周期的统一 Gauss 界

取

$$
\rho=p^{-1/(p+1)}.
$$

则在该闭圆盘的 Tate 代数中

$$
\boxed{\quad
\|K\|_\rho\le1,\qquad
\|J-1\|_\rho\le\rho^2<1,\qquad
\|J^{-1}\|_\rho=1,\qquad
\|M_1\|_\rho\le\rho^4.
\quad}
\tag{4.1}
$$

这里 $K$ 在边界可能有零点，但下面只取 $K$ 的正整数次幂，不取其倒数。

**证明。** 固定周期的显式系数是

$$
k_j=[t^{2j}]K=\frac{\prod_{\ell=1}^j(4\ell-3)^2}{(2j)!},
\qquad
j_j=[t^{2j}]J=\frac{\prod_{\ell=1}^j(4\ell-1)^2}{(2j+1)!}.
\tag{4.2}
$$

对 $q=p^a$ 写 $j=qv+r$、$0\le r<q$。
$q$ 对 $v_p(k_j)$ 的贡献为

$$
2\mathbf1_{r\ge e_a}-\lfloor2r/q\rfloor,
\qquad
e_a=\begin{cases}(3q+3)/4,&a\text{ 奇},\\(q+3)/4,&a\text{ 偶}.
\end{cases}
\tag{4.3}
$$

负贡献只可能来自奇数 $a$，每次至多为 $-1$，
且出现时 $2j\ge q+1$。
若 $v_p(k_j)=-v<0$，至少有 $v$ 个这样的奇数层，故
$2j\ge p^{2v-1}+1\ge v(p+1)$。
这证明 $v_p(k_j)+2j/(p+1)\ge0$。

对 $J$，同一计数变成

$$
2\mathbf1_{r\ge f_a}-\lfloor(2r+1)/q\rfloor,
\qquad
f_a=\begin{cases}(q+1)/4,&a\text{ 奇},\\(3q+1)/4,&a\text{ 偶}.
\end{cases}
\tag{4.4}
$$

此时负贡献只来自偶数层。
若 $v_p(j_j)=-v<0$，则 $2j\ge p^{2v}-1$，从而
$v_p(j_j)+2j/(p+1)\ge2/(p+1)$。
若赋值非负且 $j\ge1$，同一下界显然成立。
计数 (4.3)–(4.4) 还给系数赋值绝对值为 $O(\log j)$，
所以两个级数确在闭 $\rho$ 盘收敛。
这证明前两项；后两项由几何级数和 $M_1\in t^4\mathbb Z_p[[t]]$ 得到。$\square$

## 5. 完整 $J'_p(0)$ 的更精确有限门槛

沿用 [R54](../results/R54-inert-analytic-half-factor-and-central-slope.md)
的实际半因子，令 $a=17c$，$v_p(a)=-1$。
其准确插值和 Tate 同余为

$$
J_p(k)=k!a^{-k}\beta_{(p+1)k},\qquad
J_p(u)\in pu\mathbb Z_p\langle u\rangle,\qquad
J_p(u)-J_p'(0)u\in p^2u^2\mathbb Z_p\langle u\rangle.
\tag{5.1}
$$

最后一个包含关系直接来自 R54 的完整同余
$J_p(u)\equiv(\beta_{p+1}/a)u\pmod{p^2}$。
因此对每个 $n\ge0$，

$$
\frac{J_p(p^n)}{p^n}\equiv J_p'(0)\pmod{p^{n+2}}.
\tag{5.2}
$$

定义实际有理数

$$
\boxed{\quad S_{p,n}=p^{p^n}C_{(p+1)p^n}.\quad}
\tag{5.3}
$$

设 $b_n=(p^n-1)/(p-1)$。Legendre 公式给

$$
v_p((p^n)!)=b_n,\qquad
v_p(((p+1)p^n)!)=p^n+2b_n.
$$

把 (5.1) 代入 (1.2)，准确得到

$$
\boxed{\quad
v_p(S_{p,n})=2v_p(J_p(p^n)),\qquad
S_{p,n}\in\mathbb Z_p.
\quad}
\tag{5.4}
$$

其所有周期、阶乘和 $17$ 因子已经在 (1.2)、(5.1) 中保留，
没有假定一个未确定的高权比较常数为单位。

由 (5.2) 得到完整有限判据

$$
\boxed{\quad
J_p'(0)\ne0
\ \Longleftrightarrow\
\text{存在 }n\ge0:\quad
S_{p,n}\not\equiv0\pmod{p^{4n+4}}.
\quad}
\tag{5.5}
$$

若导数为零，(5.2) 强迫 $v_pJ_p(p^n)\ge2n+2$，故所有测试均为零。
反之，若 $s=v_pJ_p'(0)<\infty$，则 $s\ge1$；取 $n\ge s-1$，
有 $s<n+2$，从而
$v_pJ_p(p^n)=n+s<2n+2$，测试成功。

$n=0$ 时 (5.5) 正是 $\beta_{p+1}$ 为单位的原首层条件。
与 R62 的相邻比误差门槛相比，(5.5) 使用了 (5.1) 的额外一层，
在 $s$ 已知有限时最迟于 $n=s-1$ 检出。
此前完整条件仍然成立；这里是每层精度的加强。

对固定原函数 $\mathcal H_i=\sum C_mu^{m-1}/(m-1)$，当 $n\ge1$ 时
$m-1$ 为单位，故导数为零还准确等价于所有 $n\ge1$ 满足

$$
v_p([u^{(p+1)p^n-1}]\mathcal H_i)\ge4n+4-p^n.
\tag{5.6}
$$

R50/R54 已证明 $J_p'(0)\ne0$ 足以推出本曲线的
$\Sha[p^\infty]$ 有限；惰性方向的反向等价仍未证明。

## 6. 线性于层数的准确输入精度

§2 的特征零完全相等式使用指数增长的目标 jet。
这里先给出其足够且显式的精度界；§6.2 再以同一 Gauss 估计缩短输入。

**命题。** 置 $m=(p+1)p^n$、$h=n+2$、$P=4n+4$。
为确定 (5.3) 模 $p^P$，足够知道：

$$
\begin{array}{ll}
F(t),F_0\text{ 的所需整系数模 }p^N,
&N=4n+4+\lceil n/2\rceil,\\
M_1\text{ 到次数 }m\text{ 的系数模 }p^{4n+3}.&
\end{array}
\tag{6.1}
$$

这里在第 $j$ 个因子 $F(t^{p^j})$ 中只需 $F$ 到次数
$\lfloor(m-3)/p^j\rfloor$，$0\le j<h$。
所有乘积均截断在周期所需的次数 $m-3$。

**证明。** 令 $L=P-1$。
若 $\mathcal K_h=sK$、$\mathcal L_h=sJ$ 的所需系数误差均在 $p^L$，
且 $M_1$ 的误差在 $p^Lt^4$，则 (4.1) 给

$$
\|\mathcal K_h\|_\rho\le1,\quad
\|\mathcal L_h-1\|_\rho<1,\quad
\|\mathcal L_h^{-1}\|_\rho=1.
$$

可在有限截断代数中计算，不需要知道更高的未知系数。
正整数次幂的差用差商分解，负整数次幂的差用单位的倒数恒等式；
二者均不增加 Gauss 范数，也不引入阶乘分母。
所以 (2.5) 整个被取系数的函数误差不超过 $p^{-L}\rho^4$。
乘以 $p^{p^n}$ 后，其第 $m$ 次系数的误差赋值至少为

$$
L+p^n-\frac{m-4}{p+1}=L+\frac4{p+1}.
\tag{6.2}
$$

这些系数都在 $\mathbb Q_p$，赋值为整数；故误差至少为 $L+1=P$。

剩下只需控制从整 $F$ 到 $Q_h$ 的精度。
所有因子整，计算 $F_{[h]}$ 不损失绝对 $p$ 进精度。
由 (2.3)，

$$
F_0^{-2a}=(-p)^{-a}I,\qquad
F_0^{-(2a+1)}=(-p)^{-a-1}F_0.
\tag{6.3}
$$

因此从 $F_{[h]},F_0$ 得到 $Q_h$，至多损失
$\lceil h/2\rceil$ 个绝对精度。
只需输入精度 $L+\lceil h/2\rceil
=4n+4+\lceil n/2\rceil$，即 (6.1)。
此处 (6.3) 使用真实恒等式 $F_0^2=-pI$；
不需要对有限精度的矩阵再作不受控求逆。

计算时把已知初值
$Q_h(0)=I$、$[t](Q_h)_{12}=-1$ 和 $M_1=t^4+\cdots$
置为准确值。于是除以 $t$ 合法，两个待取幂的常数项准确为一。
这些替换只使用已证明的初值，不改变精度结论。$\square$

### 6.1 无需任何未知中心单位的输入版本

用 §2.1 的偶数迭代，精度界不变。
确实 $a=\lceil(n+2)/2\rceil$，(2.8) 只损失 $a$ 层精度，而

$$
(P-1)+a=4n+4+\lceil n/2\rceil=N.
$$

所以只需 $G_p$ 的相关整系数模 $p^N$，以及固定 $M_1$ 的相关系数
模 $p^{P-1}$。在第 $j$ 个二次因子中，只读到
$\lfloor(m-3)/p^{2j}\rfloor$ 次。

这些数据均有确定的有限来源：$G_p$ 由 (2.6) 的两个有理周期递推给出，
$M_1$ 由 R66 的固定代数除法单位模型给出。
若使用精确有理运算，最后再约到 $p^N$，无需预设一个未知实数或
$p$ 进周期的近似值；若使用有限精度周期计算，必须额外计入其计算
(2.6) 时的分母损失，不能把本命题对已经整的 $G_p$ 输入的界当作该损失为零。

### 6.2 完整测试只需 $O(pn)$ 长度的实际输入

同一个 Gauss 估计还能缩短输入 jet，而不改变最后的高权测试。
置

$$
P=4n+4,\quad L=P-1,\quad
D=\min\{m,\ 2(p+1)L+4\}.
\tag{6.4}
$$

取 $M^{[D]}$ 为 $M_1$ 到次数 $D$ 的截断，
$K^{[D]},J^{[D]}$ 为 $K,J$ 到次数 $D-4$ 的截断。
定义仍取高权系数的有限表达式

$$
\widetilde S_{p,n}
=p^{p^n}[t^m]\frac{M^{[D]}(K^{[D]})^m}
 {(1-4t^2)(J^{[D]})^{m+1}}.
\tag{6.5}
$$

则

$$
\boxed{\qquad
\widetilde S_{p,n}\equiv S_{p,n}\pmod{p^{4n+4}}.
\qquad}
\tag{6.6}
$$

**证明。** 若 $D=m$，截断根本不改变被取的系数。
否则 $D=2(p+1)L+4$。
由 (4.3)–(4.4)，任一周期的第 $q$ 次系数赋值至少为

$$
-\lfloor\log_p(q+1)\rfloor.
$$

故其在 $\rho$ 盘的加权赋值至少为
$q/(p+1)-\log_p(q+1)$。
对 $q\ge2(p+1)L$，此函数递增，且

$$
p^L>2(p+1)L+1\qquad(p\ge7,\ L\ge3),
$$

从而加权赋值至少为 $L$。这里的初等不等式从 $L=3$ 直接成立，
再按 $L$ 归纳；所用函数的导数在该区间为正。
所以丢去的 $K,J$ 尾项 Gauss 范数均不超过 $p^{-L}$。
$M_1$ 整且从四次开始，其丢去的尾项范数不超过
$p^{-L}\rho^4$。
前面 §6 的幂次与单位逆的估计于是原样适用，(6.2) 给出 (6.6)。$\square$

再取最小的整数 $a\ge1$ 满足

$$
p^{2a}>D-3.
\tag{6.7}
$$

由 (2.8)，这些短周期截断可准确用真实 $G_p$ 的 $a$ 次迭代恢复。
足够的整输入现在只有

$$
\boxed{
\begin{array}{ll}
G_p\text{ 到次数 }D-3\text{，绝对精度 }p^{L+a},\\
M_1\text{ 到次数 }D\text{，绝对精度 }p^L .
\end{array}}
\tag{6.8}
$$

第 $j$ 个因子仍只读取到 $\lfloor(D-3)/p^{2j}\rfloor$ 次。
因此输入 jet 长度为 $O(p(n+1))$，迭代次数为
$O(1+\log_p(n+1))$，输入的 $p$ 进精度为 $O(n+1)$。
这些是实际晶体和同一个固定 $M_1$ 的输入范围，
没有把任意非整矩阵换成免费整基。

(6.5) 的指数和所取次数仍为 $m=(p+1)p^n$。
本结论没有声称整次运算的时间或内存因此成为线性，
也没有把取幂、系数提取自动当作一个固定秩线性 Frobenius 操作。
它准确减少的是为了完整导数证书必须读取的周期与代数函数数据。

## 7. 实现范围与下一算术问题

(2.5)、(3.2)、(5.5)、(6.1) 共同给出完整接口：
实际迭代晶体、明确的 Hodge 源格代价、有限 jet 和有限精度，
足以检测任意有限深度的惰性中央导数。
这没有把 $F_0$ 的斜率外推到全盘，也没有以首层 $U,V$ 近似替代高权周期。

初层的实际 divided-power 商结果可以用于 $n=0$；
到更高层，必须同时保留 (3.2) 已显示的非整方向和 (2.5) 的实际高次幂。
本文尚未把这些高权商降为一个固定秩的整线性对象，
也没有给出 (5.5) 对无穷 $p$ 成功的全局理由。
新的可用量是实际输入 jet 仅为 $O(p(n+1))$、精度为 $O(n+1)$；
需要的真实二次 Frobenius 迭代数也只有 $O(1+\log_p(n+1))$。
下一步可据此研究实际截断源格和固定 $M_1$ 关系，保留完整导数而不只首层单位性。
