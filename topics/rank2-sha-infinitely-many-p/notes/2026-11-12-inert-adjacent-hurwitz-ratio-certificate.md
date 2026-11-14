# 惰性中央导数的相邻 Hurwitz 整数比证书

日期：2026-11-12。状态：本文解析恒等式、分母赋值及有限精度充要证书
均已证明。证书充要于实际惰性半因子导数非零；由 R50/R54，它足以
初级有限，没有在惰性处宣称初级有限的反向。

## 1. 使用同一固定整数流

先取 R54 的 $E_0:y^2=x^3-x$ 模型中的实际十七次截面

$$
A_1(z)=\sum\beta_mz^m=z^4+O(z^8),\qquad
B_1(z)=A_1^{(4)}(z).
$$

这里 $A_1$ 仍是原秩二目标的下降截面，不是秩零参考。
R57 的固定整数流给

$$
a_r=(4r)!\beta_{4r}\in\mathbb Z.
\tag{1.1}
$$

对原曲线 $E_{17}$ 的规范 $A_{17}=\sum b_mz^m$，有

$$
h_{4r}:=(4r)!b_{4r}=17^{r-1}a_r\in\mathbb Z.
\tag{1.2}
$$

所以相邻比满足 $h_{4r}/h_{4r+4}=a_r/(17a_{r+1})$。
以下固定惰性 $p\ge7$，写 $d=p+1$、$a=17c$，其中 $v_p(a)=-1$。
同一 R54 正式分解 $A_1=e^{az^d}G$ 定义

$$
J(u)=\mathcal J_{p,0}(u),\qquad
J_4(u)=\mathcal J_{p,4}(u)
$$

（下标 $4$ 为 Taylor 余类，不是导数），具体见
[全余类 Stokes 分解](2026-11-12-inert-euler-primitive-stokes-decomposition.md)。
其准确整性为

$$
J\in pu\mathbb Z_p\langle u\rangle,\qquad
J_4\in1+p\mathbb Z_p\langle u\rangle.
\tag{1.3}
$$

第二式来自 $[z^4]G=1$ 以及
$v_p(a^{-h}[z^{dh+4}]G)\ge\lceil h(p-1)/(2p)\rceil$。

## 2. 四阶导数参考的精确变换

令

$$
P_4(u)=\prod_{r=1}^4(du+r).
$$

使用同一个首坏指数 $a$ 对 $B_1$ 定义解析变换 $J_B$。
在非负整数 $k$ 处，直接求导及取系数给

$$
k!a^{-k}[z^{dk}]B_1
 =P_4(k)\,k!a^{-k}[z^{dk+4}]A_1
 =P_4(k)J_4(k).
\tag{2.1}
$$

$e^{-az^d}B_1=(D+ad z^{d-1})^4G$ 在 R54 的同一个更大闭盘解析；
有限次微分与多项式相乘只改变 Gauss 常数，不改变所需的严格指数
衰减。因此其下降阶乘变换在包含 $\mathbb Z_p$ 的开盘解析。
由恒等定理，(2.1) 升为

$$
\boxed{\qquad J_B(u)=P_4(u)J_4(u).\qquad}
\tag{2.2}
$$

特别地 $J_B(0)=24$。在 $u\in p\mathbb Z_p$，每个 $du+r$ 都是单位，
故 $J_B(u)$ 为单位。这里不能声称它在整个 $\mathbb Z_p$ 上无零点：
$u=-r/d$ 恰是 (2.2) 明示的零点。

由于 $J_B$ 具有整系数且常数项 $24$ 为单位，其形式逆在
$\mathbb Z_p[[u]]$ 中。因此

$$
Q_1(u)=J(u)/J_B(u)\in pu\mathbb Z_p[[u]],
\qquad Q_1'(0)=J'(0)/24.
\tag{2.3}
$$

这个有界形式级数在开单位盘收敛，尤其在 $p\mathbb Z_p$ 上收敛。
若 $k$ 为正整数且 $p\mid k$，则 (2.1) 的各量非零分母已由 (2.2)
控制，准确得到纯有理值

$$
\boxed{\quad
Q_1(k)=\frac{(dk)!\beta_{dk}}{(dk+4)!\beta_{dk+4}}
      =\frac{a_{dk/4}}{a_{dk/4+1}}.
\quad}
\tag{2.4}
$$

这来自两个真实变换之商，并没有把函数商直接作 Mellin 变换。

为直接使用原曲线整数 (1.2)，置

$$
Q_{17}(u)=Q_1(u)/17,\qquad
\lambda_p=Q_{17}'(0)=J'(0)/(24\cdot17)\in p\mathbb Z_p.
\tag{2.5}
$$

则 $Q_{17}(k)=h_{dk}/h_{dk+4}$。
这个 $17$ 正是 $A_{17}(z)=17^{-1}A_1(17^{1/4}z)$ 的固定缩放；
相应首坏指数按 $17^{d/4}$ 缩放，所以原曲线规范的半因子是 $J/17$。
该单位因子不改变所需非零性。

## 3. 不能把相邻整数分母当成单位

令 $n\ge1$、$k=p^n$、$m_n=(p+1)p^n$。
由 (1.3)–(2.2)，$J_B(k)$ 为单位，而

$$
J_B(k)=k!a^{-k}\frac{(m_n+4)!}{m_n!}\beta_{m_n+4}.
$$

$m_n+1,\ldots,m_n+4$ 都是单位，所以

$$
v_p(\beta_{m_n+4})=-p^n-v_p((p^n)!).
\tag{3.1}
$$

Legendre 公式给

$$
v_p((m_n+4)!)=\frac{(p+1)p^n-2}{p-1},\qquad
v_p((p^n)!)=\frac{p^n-1}{p-1}.
$$

第一式使用 $m_n+4=p^{n+1}+p^n+4$ 的数位和为 $6$，对 $p\ge7$
和 $n\ge1$ 没有进位。于是

$$
\boxed{\quad
v_p(h_{m_n+4})=v_p(a_{m_n/4+1})
             =\frac{p^n-1}{p-1}=:b_n.
\quad}
\tag{3.2}
$$

因此相邻分母通常有很大的 $p$ 因子，不能以其全局整数性替代
局部单位性。相邻比的整性来自 (2.3)，不是分母为单位。
特别地 $v_p(h_{m_n})\ge b_n+n+1$，因为
$Q_{17}(p^n)\in p^{n+1}\mathbb Z_p$。

## 4. 明确尾界的纯有理有限证书

由 $Q_{17}(u)=\sum_{r\ge1}q_ru^r$、$q_r\in p\mathbb Z_p$，
对每个 $n\ge1$ 都有

$$
v_p\left(\frac{Q_{17}(p^n)}{p^n}-Q_{17}'(0)\right)
 \ge n+1.
$$

结合 (2.4)–(2.5)，得到

$$
\boxed{\quad
C_{p,n}:=\frac{h_{m_n}}{p^n h_{m_n+4}}
       =\frac{a_{m_n/4}}{17p^n a_{m_n/4+1}}
\equiv\lambda_p\pmod {p^{n+1}},\qquad
C_{p,n}\in p\mathbb Z_p.
\quad}
\tag{4.1}
$$

这是只用同一固定整数流的证书，不需要计算 sigma 系数、局部周期或
某个无限级数的有限精度替身。其准确量词为

$$
\boxed{\quad
J'(0)\ne0
\iff\exists n\ge1:\ v_p(C_{p,n})<n+1
\iff\exists n\ge1:\ v_p(h_{m_n})<b_n+2n+1.
\quad}
\tag{4.2}
$$

右向左由 (4.1) 的尾界；左向右取 $n+1>v_p(\lambda_p)$ 即可。
所以任何一层通过不等式都已充分，而不会因某一层失败就断言导数为零。
若导数为零，则对所有 $n\ge1$，准确强迫

$$
p^{b_n+2n+1}\mid h_{m_n}
\quad\text{以及}\quad
p^{b_n+2n+1}\mid a_{m_n/4}.
\tag{4.3}
$$

此时 $17$ 是 $p$ 进单位，故两种整数规范的整除条件相同。

一个只校准分母和 $17$ 规范的有限例子是 $p=7,n=1$。
调用既有[整数流脚本](../scripts/check-theta-hurwitz-integers.py)
的 `coefficients(60, 17)`，纯整数递推给

$$
v_7(h_{56})=3,\qquad v_7(h_{60})=1,\qquad
\frac{h_{56}}{7h_{60}}\equiv28\pmod {49}.
$$

这与 R54 的 $J_{A_1,7}'(0)/7\equiv1\pmod7$ 及 (2.5) 一致：
$1/(24\cdot17)\equiv4\pmod7$。没有把这个有限例子作为无穷性输入。

这与 R60 的普通相邻比证书使用同一序列 $a_r$，但移动权分别是
$(p+1)p^n$ 与 $(p-1)p^n$，尾界和分母赋值也不同。
完整有限证书尚不提供跨素数非零：仍需证明 (4.2) 对无穷多个惰性
$p$ 成立，或利用全部失败时的真正整数约束 (4.3) 推出矛盾。
