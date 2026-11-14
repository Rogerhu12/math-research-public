# R596 — 原首极部的完整重建、两中央对角约束与全次数前缀矩阵

日期：2026-11-14。**状态：已证明。**

本篇把 R589 的同一个原 $W_{4,0}$ 首极部接回 R591/R595 的真实系数。原首极部的单位线性行先重建 $K$ 至倒数第二阶；原对数连接的非零终端行再恢复缺失的顶系数。因此两个指定 forcing 和原 $S_{34},T_{72}$ 对角都成为这一实际首极部上的显示多项式观测。

本篇进一步用真实 Cauchy 乘积重建所有次数的原强化整评价矩阵模 $p$。这一操作保留原列格、实际进位和真正饱和前缀；不是在平方零理想里直接相乘，也不把模 $p$ 核当成能提升的真核。

本篇依赖的完整前置为 [R589](R589-original-finite-euler-pole-algebra-and-polynomial-frobenius.md)、[R591](R591-original-inert-forcing-in-one-parameter-and-exact-resonance.md) 和 [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)。

## 1. 原来源、同一目标与指定首极部

取 $p=6s-1>71$、$b=17$，令
$$
N=s-1,\qquad
h_p=\binom{3s-1}{2s-1}\bmod p\in k^\times.
\tag{1}
$$
保持 R589 的
$$
\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p),
\qquad w=z^6,
$$
以及原九来源
$$
\boldsymbol F=(S,T,W_{4,0},W_{4,1},
 W_{1,0},W_{1,1},W_{1,2},W_{1,3},W_{1,4}).
\tag{2}
$$
原 $f_4=x\sigma^6$、$f_1=-xy\sigma^6$ 的共同 Gaussian 分解是
$$
z^2f_4=w\exp((a/p)w^s)G_4(w),\qquad
z^5f_1=w\exp((a/p)w^s)G_1(w),
$$
$$
a=6p[z^{p+1}]\log(\sigma/z),\qquad
\bar a=-6b^s h_p\in k^\times.
\tag{3}
$$
记 $G_\ell=\sum g_{\ell,r}w^r$。在 $0\le r\le N<s$ 的窗口，Gaussian 尚不贡献，所以
$$
g_{4,r}=[z^{6r+4}]f_4,\qquad
g_{1,r}=[z^{6r+1}]f_1.
\tag{4}
$$

本篇只使用同一个真实首极部
$$
\mathcal R_{4,0}=\overline{p\,\operatorname{ev}_p(W_{4,0})}\in J_p.
$$
R589 给它的全式
$$
\mathcal R_{4,0}
=\sum_{r=0}^{N-1}
 \frac{\bar a^{e_r}\bar g_{4,r}}{(e_r+1)!}
 w^{r+1}\epsilon^{e_r},
\qquad e_r=p-6-6r.
\tag{5}
$$
这里 $5\le e_r\le p-6$。令 $R_r$ 表示 (5) 对应的实际坐标，则
$$
\boxed{
\bar g_{4,r}=(e_r+1)!\bar a^{-e_r}R_r,\qquad0\le r\le N-1.}
\tag{6}
$$
每个系数都是单位。其原物理 Taylor 指标是
$$
n_r=e_rs+r+1,\qquad
R_r=\overline{p^{e_r+1}[w^{n_r}]W_{4,0}}.
\tag{7}
$$
所以 (6) 是原评价矩阵的真实行变换，不是添进若干自由 forcing 列。

## 2. 同一首极部单位线性重建 $K$ 的低阶

沿 R591/R595 的同一原参数
$$
u=x^{-1/2},\qquad t=bu^6,\qquad z=uH(t),
$$
$$
C(t)=(1+t)^{-1/2},\qquad
H(t)=\sum_{n\ge0}\frac{[t^n]C(t)}{6n+1}t^n,\qquad
K(t)=\left(\frac{\sigma(z(u))}{u}\right)^6.
\tag{8}
$$
在本篇需要的 $n\le N$，所有分母均为 $p$ 单位。

原函数直接给
$$
\frac{f_4(z(u))}{z(u)^4}=\frac{K(t)}{H(t)^4},
\qquad
w=z^6=\frac{t}{b}H(t)^6.
$$
结合 (4)，有
$$
K(t)=H(t)^4
 \sum_{r=0}^{N}\bar g_{4,r}b^{-r}t^rH(t)^{6r}
 \pmod{t^{N+1}}.
\tag{9}
$$
令 $\pi_N$ 表示保留次数严格小于 $N$，定义
$$
\boxed{
\widehat K(t)=
\pi_N\!\left(
 H(t)^4\sum_{r=0}^{N-1}
 (e_r+1)!\bar a^{-e_r}R_r\,b^{-r}t^rH(t)^{6r}
 \right).}
\tag{10}
$$
于是
$$
\widehat K=K\bmod t^N,\qquad [t^N]\widehat K=0.
\tag{11}
$$
由 $H(0)=1$，从 $(\bar g_{4,0},\ldots,\bar g_{4,N-1})$ 到
$(k_0,\ldots,k_{N-1})$ 的矩阵下三角，对角为 $b^{-r}$，全为单位。

本篇没有先对 $W_{4,0}$ 除以其零质量，也没有对 $J_p$ 作反卷积。

### 2.1 两个 forcing 的差已是一条原首极部线性行

设
$$
A(w)=z^2x,\qquad
Y_0(w)=-z^3y=A(w)-3wA'(w)
=1+\sum_{j\ge1}y_jw^j.
$$
由于 $G_1=Y_0G_4$ 是同一 Gaussian 下的原全函数身份，
$$
\boxed{
\bar g_{1,N}-\bar g_{4,N}
=\sum_{j=1}^{N}\bar y_j\,\bar g_{4,N-j}.}
\tag{12}
$$
右侧全部已经在 (5) 中。故这是 (6) 后的一条明确线性观测，而不需要未知的 $g_{4,N}$。其最后一项系数为
$$
y_1=\frac{2b}{7},\qquad
\text{在 }R_{N-1}\text{ 上的系数 }
=\frac{1440b}{7\bar a^5}\in k^\times.
\tag{13}
$$
“线性行本身非零”不等于它在当前实际首极部上的值非零。

按 R595 的归一记
$$
\mathfrak c_4=b^{-N}\bar g_{4,N},\qquad
\mathfrak c_1=b^{-N}\bar g_{1,N}.
$$
同一行在 $t$ 参数中是
$$
\boxed{
\mathfrak c_1-\mathfrak c_4
=[t^N]\widehat K(H^3-C).}
\tag{14}
$$
因为 $H^3-C$ 的常数项为零，缺失的 $k_N$ 不参与。

## 3. 原对数连接恢复缺失的顶系数

这一步使用原来源的实际连接，不将首极部的七列秩代替 forcing。

R591 证明
$$
Q=1+tK'/K,\qquad
q_n=-\frac{6n-4}{6n-1}q_{n-1},\quad q_0=1,
$$
以及准确终端行
$$
q_N=-h_p/3.
\tag{15}
$$
定义实际低阶多项式观测
$$
E_p(\widehat K)=[t^N]\frac{t\widehat K'}{\widehat K}.
\tag{16}
$$
因 $\widehat K(0)=1$，(16) 是其系数的整多项式，有限截断的逆不引入新的坏分母。

写 $K=\widehat K+k_Nt^N\bmod t^{N+1}$，直接展开得
$$
q_N=Nk_N+E_p(\widehat K).
$$
而 $6N=p-5$，所以 $N=-5/6$ 于 $k$ 中。由此
$$
\boxed{
k_N=\frac25h_p+\frac65E_p(\widehat K).}
\tag{17}
$$
因此缺失的顶系数也由同一个实际首极部及已知 Gaussian 单位恢复。

### 3.1 两个指定 forcing 的完整重建

R591 的实际留数公式给
$$
\mathfrak c_4=[t^N]KC,\qquad
\mathfrak c_1=[t^N]KH^3.
$$
结合 (17)，得到
$$
\boxed{
\begin{aligned}
\mathfrak c_4&=\frac25h_p+\frac65E_p(\widehat K)
                  +[t^N]\widehat K C,\\
\mathfrak c_1&=\frac25h_p+\frac65E_p(\widehat K)
                  +[t^N]\widehat K H^3.
\end{aligned}}
\tag{18}
$$
R589 所说的“两个指定系数不在首极部七列公式中”依旧准确。本篇增加的是原对数连接 (15) 后的非线性重建；没有把 (5) 的上限从 $N-1$ 改成 $N$。

## 4. 原两中央对角的同一首极部表达

本节采用 R595 的**原实际 Taylor 对角**，并不另造算术观测。记
$$
\mathfrak a_{34}=b^{-N}\overline{[z^{p+1}]S_b},
\qquad
\mathfrak a_{72}=b^{-N}\overline{[z^{p+1}]T_b}.
$$
置
$$
P_S=(1+t)(1-8t)(7-4t+16t^2)/7,
$$
$$
P_T=P_S(1+4t)(1-96t+48t^2+64t^3)(1+20t-8t^2),
\qquad U=C/H^2.
\tag{19}
$$
R595 的完整原留数变元为
$$
\mathfrak a_{34}=[t^N]K^{17/3}P_SU,\qquad
\mathfrak a_{72}=[t^N]K^{12}P_TU.
\tag{20}
$$
定义
$$
A_S(\widehat K)=[t^N]\widehat K^{17/3}P_SU,\qquad
A_T(\widehat K)=[t^N]\widehat K^{12}P_TU.
\tag{21}
$$
分数幂取常数一的原分支；次数至 $N<p$ 的二项式系数均整。

(17) 给出全部两行：
$$
\boxed{
\begin{aligned}
\mathfrak a_{34}
 &=\frac{34}{15}h_p+\frac{34}{5}E_p(\widehat K)+A_S(\widehat K),\\
\mathfrak a_{72}
 &=\frac{24}{5}h_p+\frac{72}{5}E_p(\widehat K)+A_T(\widehat K).
\end{aligned}}
\tag{22}
$$
这与 (18) 同用 (5) 的唯一实际首极部。

### 4.1 两原对角同零的准确非齐次约束

令
$$
L_p(\widehat K)=36A_S(\widehat K)-17A_T(\widehat K),
$$
$$
B_p(\widehat K)=\frac5{34}A_S(\widehat K)+E_p(\widehat K).
\tag{23}
$$
则完整恒等式是
$$
\boxed{
L_p=36\mathfrak a_{34}-17\mathfrak a_{72},\qquad
B_p=-h_p/3+\frac5{34}\mathfrak a_{34}.}
\tag{24}
$$
由于所有显示常数为单位，得到实际等价
$$
\boxed{
\mathfrak a_{34}=\mathfrak a_{72}=0
\iff
L_p(\widehat K)=0,\quad B_p(\widehat K)=-h_p/3.}
\tag{25}
$$
右侧第二条具有非零单位目标，绝不是把全部极部观测赋成零。

在原算术论证中，凡已付的完整中央桥给出这两个实际对角同零，便可使用 (25)。本篇不将对角同零反推完整中央零或 $\mathrm{Sha}$ 的结论，也不把 (25) 自动改写成 $\mathfrak c_4=\mathfrak c_1=0$。

### 4.2 最高可见极部的单位三角约束

写
$$
\widehat K=K^-+z\,t^{N-1},\qquad
K^-=\pi_{N-1}K,\qquad z=k_{N-1}.
$$
保持 $k_1=-2/5$。因 $N\ge3$，$t^N$ 中关于 $z$ 的项只有一次。R595 的原计算给
$$
\boxed{L_p(\widehat K)=L_p(K^-)+\frac{76024}{5}z.}
\tag{26}
$$
直接展开 (16)、(21) 同时得到
$$
\boxed{
B_p(\widehat K)=B_p(K^-)-\frac{2141}{252}z,}
\tag{27}
$$
以及
$$
[t^N]\widehat K(H^3-C)
=[t^N]K^-(H^3-C)+\frac27z.
\tag{28}
$$
例如 $[t]P_SU=-111/14$，
$[t]P_TU=-1119/14$，
所以 $A_S$、$A_T$ 的 $z$ 系数分别为
$-(17/3)(2057/210)$、$-12(5903/70)$。
而 $E_p$ 的 $z$ 系数为 $-1/3$，给 (27)。

若两原对角同零，(25)–(27) 准确成为
$$
\boxed{
z=-\frac5{76024}L_p(K^-),}
\tag{29}
$$
$$
\boxed{
B_p(K^-)+\frac{10705}{19158048}L_p(K^-)
=-h_p/3\in k^\times.}
\tag{30}
$$
这里 $76024=8\cdot13\cdot17\cdot43$；所有分母在本篇范围内为单位。$K^-$ 只读取 (5) 更低的 $r\le N-2$，最高可见坐标由 (29) 唯一确定。

对应的 forcing 差为
$$
\mathfrak c_1-\mathfrak c_4
=[t^N]K^-(H^3-C)-\frac5{266084}L_p(K^-).
\tag{31}
$$
(30) 是一个实际低极部多项式在该假设下必须取单位值的条件。它没有与任何另一个已付“该多项式为零”的结论相矛盾；这一剩余关系必须继续证明，不能省略。

## 5. 整个第一窗口也是原代数的实际重建

(18) 补足 $g_{4,N}$ 后，(6) 给全部 $g_{4,r}$（$0\le r\le N$）。$G_1=Y_0G_4$ 给同样范围的 $g_{1,r}$。

取第一窗口的自由整目标
$$
\mathcal A_p^{(1)}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,w\epsilon,\epsilon^2).
\tag{32}
$$
其基为 $1,w,\ldots,w^{s-1},\epsilon$。这是 R589 目标的实际截断；每个原来源的像都整。

原 $W_{\ell,h}$ 在模 $p$ 目标中的像准确为
$$
\boxed{
\sum_{k=1}^{s-1}
 \frac{\bar g_{\ell,k-1}}{6k-h}w^k
+\mathbf1_{h=1}\bar g_{\ell,N}\epsilon.}
\tag{33}
$$
原 $S,T$ 的 $\epsilon$ 系数为零，而全部较低 $w$ 系数仍由相同原 theta 函数重建。具体地，令 $A=z^2x$，则
$$
\Theta^3=A^2G_4\pmod{w^s},\qquad \Theta(0)=1.
\tag{34}
$$
使用 R418 的原式
$$
S_b=b^{-1}\Theta^{17}f(\tau),\qquad
T_b=b^{-1}\Theta^{36}f(\tau)V(\tau),\qquad
\tau=-bw/A^3,
$$
$$
f(\tau)=\tau(\tau-1)(16\tau^2+4\tau+7)(1+8\tau)/7,
$$
$$
V(\tau)=(1-4\tau)(1-20\tau-8\tau^2)
       (1+96\tau+48\tau^2-64\tau^3).
\tag{35}
$$
所有分母和常数一的三次根在当前窗口整。

因此，对任意原 $P\in E_{D,9}$，其在
$$
\overline{\mathcal A}_p^{(1)}
=k[w,\epsilon]/(w^s,w\epsilon,\epsilon^2)
$$
的真实像就是将 (33)–(35) 代入 $\bar P$。这同时保持全部 $D$ 和全部 $n<s$ 的原行，并保留第一共振的原 $\epsilon$ 行。不是只登记四个孤立数值。

## 6. 全部 $D$、全部首 $p^2$ 行的完整 Cauchy 重建

本节把重建接到 R589 的真正评价矩阵，不在 $J_p^2=0$ 中假作源乘法。

### 6.1 各实际因子的全部首项

对 $X=S,T$，写其原分解
$$
X=w\exp((a_X/p)w^s)G_X(w),
\qquad
a_S=(17/3)a,\quad a_T=12a.
\tag{36}
$$
R589 已由原径向式支付 $v_p(g_{X,j})\ge-\lfloor3j/p\rfloor$。对 $j\le N$，
$g_{X,j}=[w^{j+1}]X$，因此 (18)、(22)、(34)–(35) 重建全部这些数。

取 $0<k<ps$，写 $k=Ls+u$，$1\le u\le s$。定义实际单因子成本
$$
c_X(k)=L\quad(X=S,T),
$$
$$
c_{W_{\ell,h}}(k)=L+e_h(k),\qquad e_h(k)=v_p(6k-h)\in\{0,1\}.
\tag{37}
$$
R586 的完整系数证明给
$$
\boxed{
\overline{p^{c_X(k)}[w^k]X}
=\frac{\bar a_X^L}{L!}\bar g_{X,u-1}
\quad(X=S,T),}
\tag{38}
$$
$$
\boxed{
\overline{p^{c_{W_{\ell,h}}(k)}[w^k]W_{\ell,h}}
=
\frac{\bar a^L\bar g_{\ell,u-1}}
{L!\,\overline{(6k-h)/p^{e_h(k)}}}.}
\tag{39}
$$
对 (38)，只需将 R586 同一证明中的 $a,G_\ell$ 换成 (36) 已付的原 $a_X,G_X$；其它每项仍有严格至少一阶 $p$。由于 $L<p$，所有显示阶乘都是单位。

(38)–(39) 的全部输入现在都来自 (5)、已知的 $a,h_p$ 及原有限代数运算。

### 6.2 原强化整矩阵的全部列

令
$$
n=Qs+r,\quad0\le r<s,\qquad
t_n=Q+\mathbf1_{Q+6r\ge p}.
\tag{40}
$$
R589 对所有真实单项式逐项证明：每个 Cauchy composition
$k_1+\cdots+k_q=n$ 中，
$$
\sum_{i=1}^q c_{X_i}(k_i)\le t_n.
\tag{41}
$$
把 (38)–(39) 的右边简记为 $\eta_X(k)$。则对任何原单项式
$P=X_1\cdots X_q$，准确有
$$
\boxed{
\overline{p^{t_n}[w^n]P(\boldsymbol F)}
=
\sum_{\substack{k_i\ge1,\ \sum k_i=n\\
                 \sum c_{X_i}(k_i)=t_n}}
 \prod_{i=1}^q\eta_{X_i}(k_i).}
\tag{42}
$$
成本严格小于 $t_n$ 的项都含额外 $p$，模 $p$ 为零；达到成本的项由各因子真实首项相乘。重复标签的排列和所有整数乘数均由原有序 Cauchy 展开保留。对任意整系数和线性延伸即可，$n=0$ 另保原常数行。

所以同一个原强化整评价矩阵
$$
\boxed{
\widehat M_{p,D}(n,\alpha)
=p^{t_n}[w^n]\boldsymbol F^\alpha,\qquad
|\alpha|\le D,\quad0\le n<ps}
\tag{43}
$$
的**全部模 $p$ 行、全部原列**由同一个 $\mathcal R_{4,0}$ 重建。没有改用依赖单项式次数的列缩放，也没有把极部多项式直接加入 $E_{D,9}$ 作为新列。

### 6.3 一个必须保留进位的实际二次行

例如 $n=2p=11s+(s-2)$，有 $t_n=12$。在原 $W_{4,0}^2$ 的 Cauchy 展开中，只有 $k_1=k_2=p$ 能达到总成本十二；其余成本至多十一。因此
$$
\boxed{
\overline{p^{12}[w^{2p}]W_{4,0}^2}
=
\left(\frac{\bar a^5\bar g_{4,N-1}}{720}\right)^2.}
\tag{44}
$$
这是原二次列的真实行。尽管 $J_p^2=0$，(44) 不被杀掉：原特征零乘法有 $w^s=p\epsilon$ 的进位和相应分母约去。不能用模 $p$ 理想内的普通乘法代替 (42)。

## 7. 真实前缀和 Bockstein 的范围

记
$$
r_n(P)=[w^n]P(\boldsymbol F),\qquad
K_{D,k}=E_{D,9}\cap\ker(r_0,\ldots,r_{k-1}).
$$
(43) 只作统一的非零行缩放，所以在分式域及与原整格相交后，
$$
\boxed{
K_{D,k}
=E_{D,9}\cap\ker(\widehat M_{p,D}(0,-),\ldots,
                 \widehat M_{p,D}(k-1,-)),}
\tag{45}
$$
且真正最后一行是
$$
\varphi_{D,9}^k=p^{-t_k}\widehat M_{p,D}(k,-)|_{K_{D,k}}.
\tag{46}
$$

原 $S,T$ 在 $k=s$ 处本身整，而 $t_s=1$。所以 $\mathfrak a_{34},\mathfrak a_{72}$ 是 (43) 对这两条实际列的**第一 Bockstein**：
$$
\mathfrak a_{34}
=b^{-N}\overline{p^{-1}\widehat M_{p,D}(s,S)},\qquad
\mathfrak a_{72}
=b^{-N}\overline{p^{-1}\widehat M_{p,D}(s,T)}.
\tag{47}
$$
(22)、(24) 用原来源的连接把这两个特定 Bockstein 从高极部重建。它们不能从 $\overline{\widehat M}(s,S/T)=0$ 直接读出。

本篇没有支付任意 $P$ 的全部 Bockstein，也没有证明
$\ker\overline{\widehat M}$ 等于真实 $K_{D,k}$ 的约化。
(25)、(29)–(30) 是实际首极部点所受的方程；
它们不是对任意自由极部点的零恒等式，更不是可直接增加到原前缀的线性行。
因此尚不能从这些方程推出 cutoff、指定 forcing 非零，或原主目标。

## 8. 精确证书与已付接口

[check-r596-pole-reconstruction-and-central-constraints.mjs](../scripts/check-r596-pole-reconstruction-and-central-constraints.mjs)
使用已经在 R586 中采用的同一解析惰性纤维 $p=23$，分别保 $b=1,17$：

- 直接从原有理 $f_4$ 高阶系数读取 (7) 的全部首极部，不先把 forcing 系数作为自由输入；
- 核对 (10)、(12)、(17)–(18)；
- 独立从原 $z$ 径向式重建 $S,T$ 的对角，核 (20)、(22)、(24)；
- 核对 (26)–(28) 的最高可见系数；
- 直接计算原 $W_{4,0}^2$ 的高阶有理系数，验证 (44)，两种单位尺度下该实际值均为 $3\bmod23$。

证书共 41 项精确检查，不增加素数扫描。一般全次数公式 (42) 已由 R586、R589 的全参数估计和实际 Cauchy 展开证明，不以有限样本替代。

本篇的后续对象已明确为：在 (25) 的两条实际非齐次约束下，继续分析 (43) 的真前缀及其 Bockstein，或将 (30) 的显示单位值接入已有的原算术 forcing。当前没有将它们擅作新的中央零。
