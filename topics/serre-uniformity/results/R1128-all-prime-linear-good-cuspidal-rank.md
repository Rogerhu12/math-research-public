# R1128：全素数原 good 尖点模块的线性维数下界

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；global_route，
o2_high_coefficient 独立纸核。

**已证明，纯纸面。** 对每个 $p>37$，沿用 R1069 的同一个完整原
$X_{\rm ns}^+(p)$、真实 cuspidal 模块 $V=C_\Sigma[p]$
及 Bernoulli-good 子模块 $W_{\rm good}$，不加 regular 或 Vandiver 假设。
其维数满足
$$
\boxed{\qquad
\dim_{\mathbf F_p}W_{\rm good}\ge\lfloor p/16\rfloor+3.
\qquad}
\tag{1128.1}
$$
更精确的显式整数下界见 (1128.4)，其渐近为
$p/16+(\log24/8)p/\log p-O(1)$。
这把 R1069 的实际 $\Omega(p/\log p)$ 下界提升到线性下界；
没有换掉原模块、圆单位、Galois 方向或全局标签。

核心是完整原 $V$ 的低角色：某个 forced 高角色的 Bernoulli 数不为单位时，
它有时会使另一个低角色进入 $V$。
将这些角色配成互不重叠的对，一对完全不提供 good 分量需要消耗
两个不同的 irregular 指标。全局类数界于是给 (1128.1)。

本篇没有计算或排除原共同辅助像，没有证明任何指定剩余圆盘内
点的唯一性，也没有宣称主 Serre 目标完成。全篇无数学程序执行。

## 1. 不更换的原对象与精确整数结论

设
$$
m=(p-1)/2,\qquad h=\lfloor p/4\rfloor-1,\qquad
a=\lceil h/2\rceil,
$$
$$
\mathcal H_p=
2p\left(\frac{(p-1)(p-2)}{24p}\right)^{(p-1)/4},
\qquad M_p=\lfloor\log_p\mathcal H_p\rfloor.
\tag{1128.2}
$$
$B_n$ 取 $B_1=-1/2$ 的通常 Bernoulli 规范。
令 $I=i(p)$ 为 $2\le n\le p-3$ 中满足
$p\mid\operatorname{num}(B_n)$ 的偶指标数。
R1069 的奇字符正交、相对类数公式与 Kummer 整除已经证明
$$
I\le M_p.
\tag{1128.3}
$$
这里只消费这个无条件整数上界，不假设各 class-group
eigenspace 循环或 $I=v_p(h_p^-)$。

$\omega$ 是 R1062 的实际 Teichmüller 字符；
对非平凡偶角色 $\chi=\omega^n$，
$V_\chi$ 至多一维。原
$$
W_{\rm good}=
\bigoplus_{\substack{2\le n\le p-3,\ n\ {\rm even}\\
                    V_{\omega^n}\ne0,\ p\nmid B_n}}
V_{\omega^n}
$$
正是 R1069 (1069.5)，不是本篇另定义的相似空间。

记 $d_{\rm good}=\dim W_{\rm good}$。本篇证明
$$
\boxed{\quad
d_{\rm good}\ge
\max\left\{
 h-M_p,\
 \left\lceil\frac{h+a-M_p}{2}\right\rceil
\right\}.
\quad}
\tag{1128.4}
$$
更原始的计数可把 $M_p$ 换成实际 $I$。
(1128.1) 将由同一个 R1069 类数估计推出，
不以有限素数扫描替代全素数证明。

## 2. 每一个低偶角色的实际出现判据

### 2.1 原 Stickelberger 格，而非形式上的 ambient 角色

固定偶整数
$$
2\le r<m,\qquad \chi=\omega^r,\qquad
\psi=\chi^{-1}=\omega^{-r},\qquad\eta=\omega^m.
$$
$\psi,\eta,\psi\eta,\psi^2$ 均非平凡。
特别排除了 $r=m$ 的 quadratic 角色，
以及位于此区间之外的 $r=m+1$ 异常角色。

R1062 (1062.4)、(1062.6) 的真实 cusp-unit 格给出
$$
(C_\Sigma\otimes\mathbf Z_p)_\chi
 \simeq\mathbf Z_p/(S_\psi),\qquad
S_\psi=-\frac14J(\psi,\eta)B_{2,\psi^2}.
\tag{1128.5}
$$
因式恒等式的范数纤维证明只需上述四个字符非平凡，
并不要求 $\psi$ 的指数落在原 forced 区间。
因此这里确实计算完整原 $V_\chi$ 是否出现。

模 $p$，
$$
J(\psi,\eta)
 \equiv\sum_{z\in\mathbf F_p}z^{p-1-r}(1-z)^m
 =-\binom mr\ne0.
\tag{1128.6}
$$
中间唯一能给非零幂和的是第 $r$ 项，指数为 $p-1$；
$r$ 为偶数，故其二项式符号为正，而幂和为 $-1$。
全部其余指数介于 $1$ 与 $2(p-1)-1$，且不等于 $p-1$。
$r<m<p$ 保 $\binom mr$ 为单位。

置
$$
T(r)=p+1-2r.
$$
则 $T(r)$ 为偶数且 $4\le T(r)\le p-3$。
广义 Bernoulli 的原规范给
$$
\frac{B_{2,\omega^{-2r}}}{2}
 \equiv\frac{B_{T(r)}}{T(r)}\pmod p.
\tag{1128.7}
$$
所以准确得到
$$
\boxed{\quad
V_{\omega^r}\ne0
 \quad\Longleftrightarrow\quad
p\mid\operatorname{num}(B_{p+1-2r}),
\qquad 2\le r<m,\quad r\ {\rm even}.
\quad}
\tag{1128.8}
$$
出现时维数为一。这里只比较是否被 $p$ 整除；
不把模 $p$ 同余提升为两个 Bernoulli 数的精确高阶 valuation 等式。

### 2.2 广义 Bernoulli 规范的直接核对

为完整付清 (1128.7)，令 $n=T(r)$，
并对 $1\le b\le p-1$ 写纸面 Fermat 商
$q_p(b)=(b^{p-1}-1)/p$。
Teichmüller lift 满足
$$
\omega(b)\equiv b^p=b(1+pq_p(b))\pmod{p^2}.
$$
用 $\omega^{-2r}=\omega^{p-1-2r}$，得到
$$
b^2\omega(b)^{-2r}
 \equiv b^n\bigl(1-(2r+1)pq_p(b)\bigr)\pmod{p^2}.
$$
若 $S_n=\sum_{b=1}^{p-1}b^n$，则
$$
\sum b^2\omega(b)^{-2r}
 \equiv (2r+2)S_n-(2r+1)S_{n+p-1}\pmod{p^2}.
\tag{1128.9}
$$

$\omega^{-2r}$ 为非平凡偶字符，故
$\sum\omega(b)^{-2r}=0$，而按 $b\leftrightarrow p-b$ 配对也有
$\sum b\omega(b)^{-2r}=0$。于是原定义准确为
$$
B_{2,\omega^{-2r}}
 =\frac1p\sum b^2\omega(b)^{-2r}.
$$
两个普通偶指标 $n,n+p-1$ 都在 $[4,2p-4]$，
且不被 $p-1$ 整除。Faulhaber 公式给
$S_v\equiv pB_v\pmod{p^2}$；
紧随首项的奇 Bernoulli 数为零，
更高项即使有一次 $p$ 分母也不影响此精度。
普通 Kummer 同余又给
$$
B_{n+p-1}\equiv\frac{n+p-1}{n}B_n\pmod p.
$$
代入 (1128.9)，其系数模 $p$ 为
$$
(2r+2)-(2r+1)\frac{n-1}{n}
 =\frac{n+2r+1}{n}\equiv\frac2n.
$$
这就是 (1128.7)。所用分母都是 $p$-单位。
本计算只是有限恒等式的纸面证明，没有执行数值幂和。

## 3. 互不相交的高、低 Bernoulli 配对

R1062 的真实 forced 模块是
$$
V_{\omega^{n_j}}\ne0,\qquad
n_j=p-1-2j,\qquad 1\le j\le h.
\tag{1128.10}
$$
其所有 $n_j>m$，所以只要 $B_{n_j}$ 为单位，
这一原角色便属于 $W_{\rm good}$。

对其中每个奇数 $j$，配一个低指数
$$
r_j=j+1.
\tag{1128.11}
$$
它是偶数，且
$2\le r_j\le h+1=\lfloor p/4\rfloor<m$。
更关键的是
$$
T(r_j)=p+1-2(j+1)=p-1-2j=n_j.
\tag{1128.12}
$$
因此每个奇数 $j$ 的 pair $(n_j,r_j)$ 至少给一个 actual good 角色，
除非这两个 Bernoulli 数都不为单位：

- 若 $p\nmid B_{n_j}$，使用已 forced 的 $V_{\omega^{n_j}}$。
- 若 $p\mid B_{n_j}$ 而 $p\nmid B_{r_j}$，
  (1128.8) 使 $V_{\omega^{r_j}}$ 实际出现；
  后一个 Bernoulli 条件使这个低角色本身 good。

共有 $a=\lceil h/2\rceil$ 对。
所有高指数彼此不同，所有低指数彼此不同；
高指数均大于 $m$，低指数均小于 $m$，所以两组也不碰撞。
没有模 $p-1$ 的回卷：全部指数已在 $[2,p-3]$ 内。
余下 $h-a$ 个偶数 $j$ 仅按其原 forced 高角色计数。

这同时给一个明确的实际子模块选择规则：
每个 pair 先取 good 高角色；高角色 bad 时才取出现且 good 的低角色；
unpaired 处取 good 高角色。
没有把 bad 角色冒作可逆 circular-unit 坐标，也没有从
$V_\chi$ 出现自动推出 $\chi$ good。

## 4. 不重复花费 irregular 指标的计数

设 $x$ 为上述 pairs 中两个 Bernoulli 都 bad 的对数，
$y$ 为 unpaired forced 高角色中 bad 的个数。
由于全部这些指标互不相交，
$$
2x+y\le I,\qquad 0\le y\le h-a.
\tag{1128.13}
$$
上述明确选出的不同 actual good 角色至少有
$$
h-x-y.
$$
一方面 $x+y\le I$，得到 $d_{\rm good}\ge h-I$。
另一方面
$$
2(x+y)=(2x+y)+y\le I+h-a,
$$
所以
$$
d_{\rm good}\ge
 h-\left\lfloor\frac{I+h-a}{2}\right\rfloor
 =\left\lceil\frac{h+a-I}{2}\right\rceil.
\tag{1128.14}
$$
以 (1128.3) 代入，证明 (1128.4)。
其它低角色或其它实际 good 分量只会增加维数，本篇未把它们扣除。

## 5. 全部 p>37 的显式线性界

这里逐用 R1069 (1069.22) 的同一个类数估计，
而不只引用其“至少五个 good 角色”的结论。
因为
$$
h\ge\frac{p-1}{4}-\frac32,\qquad
\frac{(p-1)(p-2)}{24p}<\frac p{24},
$$
有
$$
h-\log_p\mathcal H_p
 >
 \frac{(p-1)\log24}{4\log p}
 -\frac52-\log_p2.
\tag{1128.15}
$$
在 $p\ge41$ 上，$(p-1)/\log p$ 递增，
且 $\log41<4$、$\log24>3$、$\log_p2<1/4$。
所以右侧严格大于
$$
\frac{40\cdot3}{4\cdot4}-\frac52-\frac14
 =\frac{19}{4}.
$$
由 $I\le M_p\le\log_p\mathcal H_p$ 及整数性，
$$
h-I\ge h-M_p\ge5.
\tag{1128.16}
$$
(1128.14) 因而给
$$
d_{\rm good}\ge
 \left\lceil\frac{a+5}{2}\right\rceil.
$$
若 $k=\lfloor p/4\rfloor$，则 $h=k-1$、
$a=\lceil(k-1)/2\rceil=\lfloor k/2\rfloor$。
按 $k$ 的模 $4$ 余数直接有
$$
\left\lceil\frac{\lfloor k/2\rfloor+5}{2}\right\rceil
 =\lfloor k/4\rfloor+3=\lfloor p/16\rfloor+3,
$$
证明 (1128.1)。

此外原明确数 $\mathcal H_p$ 满足
$$
M_p=\frac p4-\frac{\log24}{4}\frac p{\log p}+O(1).
$$
在 (1128.4) 的第二项代入
$h=p/4+O(1)$、$a=p/8+O(1)$，得到
$$
\boxed{\quad
d_{\rm good}\ge
 \frac p{16}+\frac{\log24}{8}\frac p{\log p}-O(1).
\quad}
\tag{1128.17}
$$
这只是已显示下界的渐近，不声称实际维数等于右边。

## 6. 对原全局路线的实际后果与边界

R1069 对每个实际 good 角色已经逐项证明对应 real class-group 分量
消失，并证明原 $p$-only global-to-local map 为同构。
本篇选出的每个低角色也满足相同的 good 条件，故同一结论直接适用：
$$
\operatorname{Hom}_G(W_{\rm good},F(\{p\},p))
 \xrightarrow{\;\sim\;}
\operatorname{Hom}_G(W_{\rm good},F_{\mathfrak p}^\times/
                                  F_{\mathfrak p}^{\times p}).
\tag{1128.18}
$$
这里 $F=\mathbf Q(\zeta_p)^+$，原圆单位基仍是
$e_\chi[\eta_a]$，原函数基与 leading normalization 不变。

因此 R1064 的实际 geometrically connected étale covering
可使用同一个 $W_{\rm good}$，其 degree 至少为
$$
p^{\,\lfloor p/16\rfloor+3}.
\tag{1128.19}
$$
原 $p$-local 候选数仍至多
$p\,n_{\mathbf Q_p}(p)=O(p^{3/2}\log p)$；
这是已有有限候选进入一个更大实际 good 标签空间，
不是额外产生更多局部圆盘。

R1112 的原同时 Frobenius 选素、准确圆单位相位和同标签必要条件
对这个同一 $W_{\rm good}$ 仍成立。
$W_{\rm good}$ 的定义本来就保所有实际 good 角色；
本篇只改善它的已证维数，没有把原 forced 模块替换为一个
无几何来源的任意大子空间。
原辅助可见性仍逐角色由 $\omega\chi^{-1}$ 决定，
不会因维数下界变大而自动让固定小素读到全部角色。

特别，(1128.19) 不给一个足够小的有效辅助素，
不证明原有限域标签像遗漏每个非 CM 候选，
不证明 cusp 逆像具有 Runge 盈余，也不删掉剩余 bad 角色的类群。
完整一般 $p$ 的同点辅助排除和盘内控制仍须继续。

## 来源与纸核范围

- [R1062](R1062-original-full-nonsplit-cuspidal-kummer-descent.md)
  §§1–3：完整实际 cusp 格、Galois 方向、Jacobi/Bernoulli 因式，
  非平凡角色至多一维及 forced 高角色。
- [R1069](R1069-all-prime-good-cuspidal-characters-and-unique-global-labels.md)
  §§2–5：good 角色的真实全局—局部同构，
  $I\le\log_p\mathcal H_p$ 和原 (1069.22) 的完整类数估计。
- [R1127](R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)
  §1：原 $r=2$ 出现判据提供本篇配对思路；
  本篇 §2 已独立证明全部 $2\le r<m$ 的范围，
  不从 Gaussian 源外推原一般 $p$ 标签的其它几何性质。
- 普通 Kummer 同余：
  [NIST DLMF 24.10.3](https://dlmf.nist.gov/24.10.E3)。
  本篇所需广义特例在 §2.2 完整还原为两个有限幂和及这个普通同余；
  不依赖未经标定的广义 Bernoulli 记号。

o2_high_coefficient 独立纸核低角色出现 iff、
$T(r)=p+1-2r$、全角色异常边界、互不相交 pairs、
精确整数计数和 (1128.1)/(1128.17)。
root 独立核 $I\ge2x+y$ 与 $y\le h-a$ 的配对计数。
没有任何数学程序执行。
