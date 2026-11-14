# R239 附录：两种正权任意重数的整个高度四 primitive Gram 严格统一界

- 日期：2026-11-13。
- 作者：Astra-ISP-0c；AI-assisted，GPT-6 Astra Pro。central_review 已全文独立核验 461 行证明，并独立执行 139 行 BigInt 证书得到 PASS。
- 状态：完整有限维定理；不完成普通 ISP，不外推任意多种权或原连续尾。
- 扣除旧范围：[高度二](../results/R239-appendix-two-weight-groups-full-height-two-sharp-primitive-gram-bound.md)、[高度三](../results/R239-appendix-two-weight-groups-full-height-three-sharp-primitive-gram-bound.md) 及[饱和双侧权数界](../results/R239-appendix-saturated-primitive-two-sided-weight-count-constants.md) 已付。本稿新增高度四的全部非饱和双串，并拼成整个 primitive 空间。
- [完整 BigInt 证书](../notes/2026-11-13-two-weight-height-four-all-q-newton-certificate-0c.mjs)：四个差式共 4663 个正整数 Newton 系数、零个负项。全头数结论来自先验次数界和完整展开，有限头数核验只检查独立公式。

## 1. 定理与完整逆的约定

设两组位数为 $M,N\ge0$，权分别为 $a,b>0$，并满足
$$
M+N=2s+4\ge4.
$$
令
$$
D=a\sum_{i=1}^{M}E_i+b\sum_{i=M+1}^{M+N}E_i,
\qquad
K_s=\ker D\cap\mathcal H_s.
$$
始终先在完整出生层上取逆，再压缩：
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_s}}{(n!)^2},
\qquad
\Gamma_n=P_{K_s}F_n^{-1}|_{K_s},
\qquad 0\le n\le4.
\tag{1.1}
$$
正权可逆对角共轭与等权 Lefschetz 串保证这些 $F_n$ 全部正定。
定义
$$
C_1=C_3=\frac34,\qquad C_2=\frac23.
$$

**定理。** 对每个有限 $M,N$ 和每个固定正权比，在整个 $K_s$ 上都有
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
\prec C_n\Gamma_{n-1},
\qquad n=1,2,3.
}
\tag{1.2}
$$
三个常数作为对全部组大小和正权比同时统一的常数均最优。
本稿不声称它们是每个固定 $(M,N)$ 的最优常数。

整体缩放 $D$ 使 $\Gamma_n$ 乘 $b^{-2n}$，不改变 (1.2) 的相邻比。
以下将长组的权归一为一，并写短组权的平方为 $z>0$。

## 2. 从完整空间到三类双串

每个等权组的标准正交串同时约化删除和伴随。
$T$ 位组的第 $j$ 个 primitive 出生具有串长 $T-2j$，
其删除系数为
$$
\sqrt{r(T-2j-r+1)}
$$
且重数为 $\binom Tj-\binom T{j-1}>0$。
逐层维数求和穷尽全空间；详细有限维证明见高度二稿 §2。

将两组分别作此分解，得到长度
$$
m=M-2j,\qquad \ell=N-2k
$$
的双串，原出生层在其中变为
$$
t=s-j-k=\frac{m+\ell-4}{2}.
$$
双串删除矩阵的端点递推给出：
在 $t\ge0$ 时 primitive 一维当且仅当 $t\le\min(m,\ell)$。
因此只有
$$
|m-\ell|=0,\quad2,\quad4
\tag{2.1}
$$
三种非零块。
按短串长度记为 $q$，三种情形分别是

| 双串长度 | 相对出生 | 参数限制 | 缺失次数 $\delta=q-t$ |
|---|---:|---:|---:|
| $q,q$ | $q-2$ | $q\ge2$ | $2$ |
| $q,q+2$ | $q-1$ | $q\ge1$ | $1$ |
| $q,q+4$ | $q$ | $q\ge0$ | $0$ |

各双串同时约化整个 $D^n(D^*)^n$，所以完整逆也按同一正交分解约化。
每个相关 primitive 块为一维，所有重数原样保留。
因此逐块标量比较足以推出完整算子序 (1.2)，没有将“压缩后取逆”替代 (1.1)。

### 2.1 本稿使用的准确最小逆公式

短串长 $q$、长串长 $\ell=q+4-2\delta$。
将缺失头集合大小记为 $r$。
[完整固定块 MP 公式](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)
的共同头权特例给未归一的真实费用
$$
H_n=
\min_F
\sum_{\substack{0\le r\le q\\0\le n+r-\delta\le\ell}}
\frac{\binom qr z^r}{\binom{\ell}{n+r-\delta}}
|F(r)|^2.
\tag{2.2}
$$
这里
$$
F(r)=\binom r\delta+P(r),\qquad\deg P\le\delta-1,
\tag{2.3}
$$
并对全部非法指标强制 $F(r)=0$。
当 $\delta=0$ 时 $F=1$，没有自由参数。

解释完整性：池平均保输出且不增范数，唯一最小解对池置换固定；
共同头权再使最小解对头置换固定。
全部固定原像恰为 (2.3)，非法池次数正是所列零约束。
因此 (2.2) 优化的是所有原像，不是试探族。
特别，$\delta=2$ 的两个低次参数均保留。

零阶的约束使 $F(r)=\binom r\delta$；
最高阶使 $F(r)=(-1)^\delta\binom{q-r}{\delta}$。
补集换元给
$$
H_n(z)=z^qH_{4-n}(z^{-1}).
\tag{2.4}
$$
源归一后 $\gamma_n=H_n/H_0$，所以
$$
c_n=\frac{\gamma_n^2}{\gamma_{n-1}\gamma_{n+1}}
=\frac{H_n^2}{H_{n-1}H_{n+1}},
\qquad c_3(z)=c_1(z^{-1}).
\tag{2.5}
$$

## 3. 相等串长 q/q：两个参数的完整消去

令
$$
Q=q+1,\qquad \vartheta=z\frac{d}{dz},\qquad
W=\sum_{r=0}^{q}z^r.
$$
定义
$$
V=\sum_{r=0}^{q}r(Q-r)z^r,\qquad
R=\sum_{r=0}^{q}(q-r)(r+1)z^r,
$$
$$
A_0=\sum_{r=0}^{q}
r(r-1)(Q-r)(Q+1-r)z^r.
\tag{3.1}
$$
对任意正系数多项式 $B=\sum b_rz^r$ 写
$$
T(B)=B\vartheta^2B-(\vartheta B)^2
=\sum_{r<u}b_rb_u(u-r)^2z^{r+u}.
\tag{3.2}
$$
再置
$$
T=T(W),\qquad T_V=T(V),\qquad T_R=T(R),
$$
$$
U=\det[\vartheta^{i+j}W]_{i,j=0}^{2}
=\sum_{r<u<v}(u-r)^2(v-r)^2(v-u)^2z^{r+u+v}.
\tag{3.3}
$$
对于 $q\ge2,z>0$，本节出现的 $V,R,A_0,T,T_V,T_R,U$ 均严格为正。

(2.2) 在五阶准确化成
$$
\boxed{
H_0=\frac{A_0}{4},\quad
H_1=\frac{T_V}{4V},\quad
H_2=\frac{U}{4T},\quad
H_3=\frac{T_R}{4R},\quad
H_4=z^qH_0(z^{-1}).
}
\tag{3.4}
$$

逐阶核对全部参数：
在 $n=0$，$F=r(r-1)/2$，且二项式比消去一份 $r(r-1)$，
给 $A_0/4$。
在 $n=1$，非法 $r=0$ 强制
$F=r(r-\xi)/2$；二项式比为 $(q-r+1)/r$，
故最小化是权 $r(Q-r)z^r$ 下的完整常数方差，给 $T_V/(4V)$。
在 $n=2$，权恰为 $z^r$，而
$F=(r^2+\xi r+\zeta)/2$ 的两个复参数均自由。
完整 $3\times3$ 矩阵的 Schur 补给 monic 二次残差 $U/T$，
所以得到 $U/(4T)$。
$n=3,4$ 由同一零约束或 (2.4) 得到。
所有权实正，复最小化与该 Hermitian Schur 补完全一致。

由 (3.4)，所需前两阶严格界等价于
$$
\boxed{
\Delta_{=,1}:=3V^2A_0U-4T_V^2T>0,
}
\tag{3.5}
$$
$$
\boxed{
\Delta_{=,2}:=2T^2T_VT_R-3U^2VR>0.
}
\tag{3.6}
$$

## 4. 串长差二 q/(q+2)：全部内部方差

仍写 $Q=q+1$，令
$$
W_1=\sum_{r=0}^{q}(Q-r)(Q+1-r)z^r,
$$
$$
W_2=\sum_{r=0}^{q}(r+1)(Q-r)z^r,\qquad
W_3=\sum_{r=0}^{q}(r+1)(r+2)z^r,
$$
$$
B_0=\sum_{r=0}^{q}
r(Q-r)(Q+1-r)(Q+2-r)z^r,\qquad
T_i=T(W_i).
\tag{4.1}
$$
现在 $\delta=1$，所以所有内部阶仅优化 $F=r-\xi$。
二项式比分别为
$$
\frac{\binom qr}{\binom{q+2}r}
=\frac{(Q-r)(Q+1-r)}{Q(Q+1)},
$$
$$
\frac{\binom qr}{\binom{q+2}{r+1}}
=\frac{(r+1)(Q-r)}{Q(Q+1)},
\qquad
\frac{\binom qr}{\binom{q+2}{r+2}}
=\frac{(r+1)(r+2)}{Q(Q+1)}.
$$
从而准确有
$$
\boxed{
H_0=\frac{B_0}{Q(Q+1)},\qquad
H_i=\frac{T_i}{Q(Q+1)W_i}\ (1\le i\le3),
\qquad H_4=z^qH_0(z^{-1}).
}
\tag{4.2}
$$
当 $q\ge1,z>0$ 时全部分母及 $B_0,T_i$ 严格为正。
所需两阶界等价于
$$
\boxed{
\Delta_{2,1}:=3W_1^2B_0T_2-4T_1^2W_2>0,
}
\tag{4.3}
$$
$$
\boxed{
\Delta_{2,2}:=2W_2^2T_1T_3-3T_2^2W_1W_3>0.
}
\tag{4.4}
$$

## 5. 四个差式的全部 q 精确正性证书

### 5.1 稀疏生成函数直接生成先验界

从有限几何和
$$
W=\frac{1-z^Q}{1-z}
\tag{5.1}
$$
开始，用有限次加减乘和 $\vartheta$ 生成上文全部多项式。
所用直接身份为
$$
\begin{aligned}
V&=\vartheta(Q-\vartheta)W,\\
R&=(Q-1-\vartheta)(\vartheta+1)W,\\
A_0&=\vartheta(\vartheta-1)(Q-\vartheta)(Q+1-\vartheta)W,\\
W_1&=(Q-\vartheta)(Q+1-\vartheta)W,\\
W_2&=(\vartheta+1)(Q-\vartheta)W,\\
W_3&=(\vartheta+1)(\vartheta+2)W,\\
B_0&=\vartheta(Q-\vartheta)(Q+1-\vartheta)(Q+2-\vartheta)W.
\end{aligned}
\tag{5.2}
$$
$T$ 用 (3.2)，$U$ 用 (3.3) 的准确行列式生成。

每个差式因此写成
$$
\Delta(z)=
\frac{\sum_{\lambda,s}p_{\lambda,s}(Q)z^{\lambda Q+s}}
{(1-z)^d},
\qquad p_{\lambda,s}\in\mathbb Z[Q].
\tag{5.3}
$$
附带程序逐项保存 $(\lambda,s)$ 与整数多项式，未作数值拟合。
输出的先验结构为

| 差式 | $d$ | 分子非零项 | $\deg_Qp$ 上界 | 最大偏移 $s$ | 原多项式次数上界 |
|---|---:|---:|---:|---:|---:|
| $\Delta_{=,1}$ | 20 | 57 | 10 | 14 | $6q-3$ |
| $\Delta_{=,2}$ | 24 | 81 | 12 | 14 | $8q-6$ |
| $\Delta_{2,1}$ | 19 | 52 | 11 | 14 | $5q-1$ |
| $\Delta_{2,2}$ | 22 | 71 | 12 | 15 | $6q-2$ |

原多项式次数界也可直接从 (3.1)–(4.4) 的有限和读出。
例如 $T$、$T_V$ 次数为 $2q-1$，$T_R$ 为 $2q-3$，
$U$ 为 $3q-3$，$R$ 为 $q-1$。
所有分子项的 $\lambda,s$ 非负。

### 5.2 有限区域覆盖无限头数

对每个可能非零的系数 $[z^k]\Delta$，唯一写
$$
k=jQ+u,\qquad0\le u<Q,\qquad
v=Q-u-1\ge0.
$$
四个差式的区域数分别为 $6,8,5,6$。
$\lambda>j$ 的分子项不贡献，其余给准确式
$$
[z^k]\Delta
=
\sum_{\lambda\le j,s}
p_{\lambda,s}(Q)
\binom{(j-\lambda)Q+u-s+d-1}{d-1}.
\tag{5.4}
$$
表中全部 $s\le d-1$。
因此出现负滞后时，二项式上标仍非负而小于 $d-1$，
普通二项式为零，恰等于其次数 $d-1$ 的多项式值。
这里没有非法负上标的延拓。

代入 $Q=u+v+1$，得到双变量多项式 $P_j(u,v)$。
其总次数先验不超过
$$
D=\deg_Qp+d-1,
\tag{5.5}
$$
即四种情形分别为 $29,35,29,33$。
所以完整 Newton 恒等式为
$$
P_j(u,v)=
\sum_{a,b=0}^{D}
c_{j,a,b}\binom ua\binom vb,
\qquad
c_{j,a,b}=(\Delta_u^a\Delta_v^bP_j)(0,0).
\tag{5.6}
$$
在 $(D+1)\times(D+1)$ 的整数网格上逐次作完整有限差分即得到全部系数。
(5.5) 在检查符号之前已经由 (5.3) 支付；
这不是从有限几个 $q$ 的正性外推全部 $q$。

### 5.3 全部整数检查结果

四个差式各区域的正系数个数如下；所有未列出的系数为零，负系数均为零。

| 差式 | 各区域的正系数个数 | 总正项数 |
|---|---|---:|
| $\Delta_{=,1}$ | $55,198,206,205,194,50$ | 908 |
| $\Delta_{=,2}$ | $80,291,297,296,293,286,258,45$ | 1846 |
| $\Delta_{2,1}$ | $125,189,188,184,50$ | 736 |
| $\Delta_{2,2}$ | $105,252,251,249,241,75$ | 1173 |

程序对每个整数系数作符号断言，合计 $4663$ 个正项、零个负项。
它同时报告各区域的最小正系数。
在非负整数 $u,v$ 上，(5.6) 每项非负，因此四个原差式的全部 $z$ 系数均非负。

证书还以与 (5.3) 不同的有限数组公式作独立身份检查：
$T$ 直接按二元对求和，$U$ 直接按三元组 Vandermonde 平方求和，
并比较整个稠密多项式乘 $(1-z)^d$ 与稀疏分子。
分别取相等串 $q=2,3,4,7$ 和差二串 $q=1,2,3,7$，全部身份逐系数成立。
这些检查只核公式实现；全部头数证明仍是 (5.3)–(5.6)。

### 5.4 每个合法头数都有严格正项

以下四项直接从最小幂的有限和手算，证书也逐一检查：
$$
\boxed{
[z^7]\Delta_{=,1}=8q^2(q-1)(q+2)>0
\quad(q\ge2),
}
\tag{5.7}
$$
$$
\boxed{
[z^6]\Delta_{=,2}=8q^2(q-1)^2>0
\quad(q\ge2),
}
\tag{5.8}
$$
$$
\boxed{
[z^2]\Delta_{2,1}
=2q^2(q+1)^4(q+2)^2(q+4)>0
\quad(q\ge1),
}
\tag{5.9}
$$
$$
\boxed{
[z^2]\Delta_{2,2}
=24q(q+1)^3(q+2)>0
\quad(q\ge1).
}
\tag{5.10}
$$
故对全部合法 $q$ 和每个 $z>0$，四个差式严格为正。
由 §§3–4 及倒数对称，
两类非饱和块均满足
$$
c_1,c_3<\frac34,\qquad c_2<\frac23.
\tag{5.11}
$$

## 6. 饱和块、全空间拼合及统一最优性

第三类为串长 $q,q+4$、出生 $q$ 的饱和线。
这里 (2.2) 的 $F=1$。
已证明的饱和双侧权数定理给
$$
c_n\le
\begin{cases}
\dfrac{n}{n+1}\dfrac{q+4-n}{q+5-n},&0<z<1,\\[6pt]
\dfrac{n(4-n)}{(n+1)(5-n)},&z=1,\\[6pt]
\dfrac{q+n}{q+n+1}\dfrac{4-n}{5-n},&z>1.
\end{cases}
\tag{6.1}
$$
因此对每个有限 $q$，
$$
c_1,c_3\le\frac{3(q+1)}{4(q+2)}<\frac34,\qquad
c_2\le\frac{2(q+2)}{3(q+3)}<\frac23.
\tag{6.2}
$$
$q=0$ 也包含在内：这是四位等权真空串。

(5.11)、(6.2) 穷尽 (2.1) 的全部 primitive 块。
每个固定 $M,N$ 只有有限个块，且各块均为严格正定的比较，
所以整个 $K_s$ 上得到 (1.2)。

为证明对全部组大小统一的常数不可减小，直接取饱和组大小
$(M,N)=(q,q+4)$ 及其共同对称串。
由 (2.2)，在 $z\to\infty$ 时最高 $r=q$ 项占优，准确有
$$
\lim_{z\to\infty}c_n(z)
=
\frac{(q+n)(4-n)}{(q+n+1)(5-n)}.
\tag{6.3}
$$
再令 $q\to\infty$，$n=1$ 的比趋 $3/4$，$n=2$ 的比趋 $2/3$。
$n=3$ 用 $z\to0$ 的倒数对称得到 $3/4$。
这些真实饱和块均出现在所声明的完整 primitive 空间中，
故全空间统一常数同样最优。

## 7. 适用边界与下一接口

本稿已经支付两种正权、任意两组重数的整个高度四 primitive，
包括相等串的两个完整最小化参数、差二串的全部方差和所有表示重数。
它不只处理池固定源，也没有删除完整逆中非 primitive 的其他出生分量。

证明依赖两组正交串将 primitive 块化为一维。
三种及更多互不相同的权会产生真正矩阵块，
不能用本稿标量差式替代其完整算子序。
高度五及以上还需新的非饱和块比较；
原连续尾、原边界窄源三 Gram、一般正正常湮灭者与普通 ISP 仍开。
