# R150 附录：秩一第三累积量的高接触均值极线分类

日期：2026-11-26。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 本稿登记原请求14已经成功执行的 $4+1$、$3+2$、$2+3$ 三个完整分支，
并与已闭五重点和三重乘二次余因子分支组合，得到不依赖余因子分拆的高接触分类。
所有有限、重根、合流及射影无穷远参数均保留。

## 1. 原定义与统一参数族

沿用[三重乘二次余因子的完整附录](R150-appendix-rank-one-third-cumulant-three-plus-one-plus-one-mean-divisor-classification.md) §§1–3 的
原整数 $K$、$u(a,b)=(a^5,a^4b,\ldots,b^5)^{\mathsf T}$、原 Hankel 矩 $H,V$ 和完整 $\mathcal Q_3$。
以下重列所有用于有限计算的公式，使三族的实际输入明确。

设
$$
V=v u(s)^{\otimes3}\ne0,\qquad
P_y(x)=(Ky)^{\mathsf T}u(x),\qquad
k_s(x)=u(s)^{\mathsf T}Ku(x)=-\Delta_s(x)^2q_s(x).
\tag{1.1}
$$
$\Delta_s(a,b)=s_0b-s_1a$，$q_s$ 是原二元三次式；有限图中
$$
q_s(z)=(s^3-5s^2)+(s^3-3s^2+22s)z
 -(3s^2+3s+5)z^2+(s+1)z^3.
\tag{1.2}
$$
全部十六条最高方程是
$$
P_y^3-6P_yG_H+4v k_s^3=0,
\qquad G_H=u^{\mathsf T}KHK u.
\tag{1.3}
$$
它迫 $P_y\ne0$ 及 $P_y\mid k_s^3$。

本稿处理下列三个族，其中始终有 $q_s(t)=0$：
$$
f_{41}=\Delta_s^4\Delta_t,\qquad
f_{32}=\Delta_s^3\Delta_t^2,\qquad
f_{23}=\Delta_s^2\Delta_t^3,\qquad P_y=\sigma f_{ij},\quad \sigma\ne0.
\tag{1.4}
$$
三个记号只表示显示的原五次多项式，不预设 $s\ne t$ 或根恰有显示的重数。
原权缩放 $(y,H,V)\mapsto(\sigma^{-1}y,\sigma^{-2}H,\sigma^{-3}V)$ 允许置 $P_y=f_{ij}$，
$\eta=4v/\sigma^3\ne0$。
令 $d_{s,t}=q_s/\Delta_t$，这是已付根约束上的二元二次多项式，则
$$
\begin{array}{c|c}
\text{族}&w_{ij}=k_s^3/f_{ij}\\\hline
41&-\Delta_s^2q_s^2d_{s,t}\\
32&-\Delta_s^3q_s d_{s,t}^2\\
23&-\Delta_s^4d_{s,t}^3
\end{array}
\tag{1.5}
$$
每个商是一个完整十次齐次多项式，没有删去任何参数因子。

由 $\det K=-25600$、$\det J_2=-64701092257700249600$，(1.3) 唯一给出
$$
y=K^{-1}[f],\qquad
H_m=X_m+\eta Y_m,\qquad
X=\tfrac16J_2^{-1}[f^2],\quad Y=\tfrac16J_2^{-1}[w],\qquad
V=\tfrac\eta4u(s)^{\otimes3}.
\tag{1.6}
$$
这里 $(J_2)_{mn}=\sum_{i+a=m,j+b=n}K_{ij}K_{ab}$，方括号始终是完整齐次系数列。
(1.5) 被 $\Delta_s^2$ 整除，而 $f$ 也被 $\Delta_s^2$ 整除，因此
$P_y(s)=G_H(s)=0$。
完整原低梯度中的三阶贡献
$V(p,p,\cdot)$、$V:(KHK)$、$V_p$ 均准确为零。
余下全部梯度为
$$
\tfrac13K^{-1}\nabla_y\mathcal Q_3
=\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp,
$$
$$
-\tfrac16\partial_{H_m}\mathcal Q_3
=n_m=[z^m]u(1,z)^{\mathsf T}KNKu(1,z),
$$
$$
N=Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH,
\tag{1.7}
$$
其中 $p=Ky$、$F=y^{\mathsf T}Ky/2$、$h=Hp$、$b_0=p^{\mathsf T}Hp$、
$\tau_2=\operatorname{tr}((KH)^2)$。
这些是全部六 mean 与十一二阶梯度的原公式；仅在排除阶段取其中三个必要条件。

## 2. 三个有限图的完全特征零排除门

有限 $s,t$ 时用无参数分母的恒等式
$$
q_s(z)=(z-t)d_{s,t}(z)+q_s(t),
$$
$$
d_{s,t}(z)=(q_1+q_2t+q_3t^2)+(q_2+q_3t)z+q_3z^2.
\tag{2.1}
$$
将 (1.4)、(1.5) 的 $\Delta_s,\Delta_t$ 换成 $z-s,z-t$，仍以 (1.6) 定义完整原矩。
在 $q=q_s(z)$、$q_*=q_s(t)$ 的记号下，原最高方程残差依次为
$$
-\eta(z-s)^6q^2q_*,
\quad-\eta(z-s)^6q q_*(2q-q_*),
\quad-\eta(z-s)^6q_*(3q^2-3qq_*+q_*^2).
\tag{2.2}
$$
所以它们在同一原根约束上恰为零。

每个 $n_i$ 都是 $\eta$ 的二次多项式。
对 $a=a_2\eta^2+a_1\eta+a_0$、$b=b_2\eta^2+b_1\eta+b_0$，置
$$
\mathscr R_2(a,b)
=(a_2b_0-a_0b_2)^2-(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
$$
这是固定四阶 Sylvester 行列式；存在共同有限根必使它为零，特殊化降次不影响这个必要性。
对三个族各自从原 (1.6)、(1.7) 构造
$$
R_{01}=\mathscr R_2(n_0,n_1),\quad R_{02}=\mathscr R_2(n_0,n_2),
$$
$$
A(s)=\operatorname{Res}_t(q_s(t),R_{01}),\quad
B(s)=\operatorname{Res}_t(q_s(t),R_{02}).
\tag{2.3}
$$
任一有限参数的完整临界点都使 $A(s)=B(s)=0$。
精确有理数运算与完整矩阵非零门如下：

| 族 | $\deg_tR_{01}=\deg_tR_{02}$ | $\deg A=\deg B$ | 原 QQ 公因子 $D$ | $\deg(A/D)=\deg(B/D)$ | 完整 Sylvester 阶数 | 模1009行列式 |
|---|---:|---:|---|---:|---:|---:|
| 41 | 16 | 244 | $s^{12}(s+1)^{12}$ | 220 | 440 | 166 |
| 32 | 32 | 264 | $(s+1)^{24}$ | 240 | 480 | 242 |
| 23 | 48 | 276 | $(s+1)^{36}$ | 240 | 480 | 838 |

所有 $D$ 的除法在 $\mathbb Q[s]$ 中余式为零。
原矩、低梯度、两层结式和余因子的每个有理数分母均为1009单位；
两个余因子的最高项模1009均非零。
故上表是 $\mathbb Z_{(1009)}$ 上完整固定 Sylvester 矩阵的非零约化，
从而其有理数行列式非零，余因子在 $\mathbb C$ 中无共同根。
结论是
$$
\begin{array}{c|c}
41&s\in\{0,-1\}\\
32&s=-1\\
23&s=-1.
\end{array}
\tag{2.4}
$$
这一提升只使用有理数环到有限域的环同态与行列式多项式身份，
不从模1009的点数或某个抽样纤维反推复数无解。

## 3. 特殊 $s=-1$ 纤维的真实次数

原三次在此处确实降次：
$$
q_{-1}(t)=-5t^2-26t-6.
\tag{3.1}
$$
必须先从相应原 $R_{01}(s,t)$ 特殊化，再按真实次数取结式。
成功运行给

| 族 | $\deg_t R_{01}(-1,t)$ | $\operatorname{Res}_t(q_{-1},R_{01}(-1,t))\pmod{1009}$ |
|---|---:|---:|
| 41 | 12 | 661 |
| 32 | 24 | 369 |
| 23 | 36 | 585 |

三者的有理数分母仍是1009单位，所以三个有理数结式都非零。
因此三族的 $s=-1$ 有限纤维全部为空。
特别是41、32中的12、24并非一般纤维的16、32；
此前错误的次数断言所对应失败运行不构成本证明的一部分。

41族的剩余有限 $s=0$ 满足
$$
q_0(t)=t^2(t-5).
$$
所以只能有 $(s,t)=(0,0)$ 或 $(0,5)$。
前者用 $f=z^5$、$w=z^7(5-z)^3$ 重新构造 (1.6)、(1.7)，
其 $n_0,n_1$ 的完整四阶结式模1009为 $686\ne0$，故排除。
后者会在 §5 完整验证为真临界族。

## 4. 射影边界逐一返回原矩

由
$$
q_\infty(a,b)=a^2(a+b),\qquad
q_s(\infty)=s+1\quad(s\text{ 有限}),
$$
有限图以外只有
$(\infty,\infty)$、$(-1,\infty)$、$(\infty,-1)$。
写 $h(z)=5z^2+26z+6$。
下表列出直接由原齐次多项式得到的 $f(1,z),w(1,z)$，
以及 (1.7) 两原梯度 $n_0,n_1$ 的四阶结式非零值。
所有 $f,w$ 都按五次、十次齐次式补足系数。

| 族 | $(s,t)$ | $f(1,z)$ | $w(1,z)$ | 四阶结式模1009 |
|---|---|---|---|---:|
| 41 | $(\infty,\infty)$ | $-1$ | $(1+z)^3$ | 462 |
| 41 | $(-1,\infty)$ | $-(1+z)^4$ | $-(1+z)^2h^3$ | 946 |
| 32 | $(\infty,\infty)$ | $-1$ | $(1+z)^3$ | 462 |
| 32 | $(-1,\infty)$ | $(1+z)^3$ | $(1+z)^3h^3$ | 191 |
| 32 | $(\infty,-1)$ | $-(1+z)^2$ | $1+z$ | 627 |
| 23 | $(\infty,\infty)$ | $-1$ | $(1+z)^3$ | 462 |
| 23 | $(-1,\infty)$ | $-(1+z)^2$ | $-(1+z)^4h^3$ | 131 |
| 23 | $(\infty,-1)$ | $(1+z)^3$ | $-1$ | 872 |

每个边界用对应的原 $u(s)$，即 $u(\infty)=e_5$ 或
$u(-1)=(1,-1,1,-1,1,-1)^{\mathsf T}$。
所有有理数分母和两个二次首项均已核为1009单位。
这些四阶行列式非零，严格提升后便排除所有显示的完整边界；
没有把无穷远当作有限坐标的极限猜测，也没有删去零分母支路。

只有41族的 $(\infty,-1)$ 未列为排除对象。它的齐次多项式恰为
$$
f=a^4(a+b)=-k_\infty,\qquad w=-a^8(a+b)^2=-k_\infty^2.
\tag{4.1}
$$

## 5. 三族的完整分类

由 §§2–4，32与23两个族完全没有原临界点。
41族只可能有
$$
(s,t)=(0,5)\quad\text{或}\quad(\infty,-1).
\tag{5.1}
$$
第一组给 $f=z^4(z-5)=-k_0$、$w=-z^8(z-5)^2=-k_0^2$；
第二组是 (4.1)。
所以这两组的唯一完整原矩均为
$$
y=-u(s),\qquad H=\frac{1-\eta}{6}u(s)u(s)^{\mathsf T},\qquad
V=\frac\eta4u(s)^{\otimes3}.
\tag{5.2}
$$
这确实是任意 $\eta\ne0$ 的真临界族：$u^{\mathsf T}Ku=0$ 直接给
$F=Hp=HKH=(KH)^2=0$，故 (1.7) 全零；
而最高方程为 $\{-1+(1-\eta)+\eta\}k_s^3=0$。
完整第三普通矩
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V
$$
也等于 $\{-1+(1-\eta)+\eta\}u(s)^{\otimes3}=0$。
因此所有方向上的完整 Bell 立方 $T_3(r,r,r)$ 都为零。
这一充分性直接从原张量等式验证，不是将仅用于排除的三个低梯度当作完整条件。

## 6. 不依赖分拆的高接触推论

**定理。** 若完整原 $\mathcal Q_3$ 临界点满足
$$
V=v u(s)^{\otimes3}\ne0,\qquad \operatorname{ord}_s P_y\ge3,
\tag{6.1}
$$
则 $T_3=0$。更准确地，经原权缩放后必有 (5.2)，
且 $s\in\{0,2,-6,\infty\}$。

**证明。** 由 (1.3)，$P_y$ 非零、齐次五次且整除 $k_s^3$。
按它在 $s$ 的准确重数 $j$ 分类，$3\le j\le5$。

若 $j=5$，则 $P_y\propto\Delta_s^5$，已由
[同点五重极线排除](R150-appendix-rank-one-third-cumulant-quintuple-mean-at-own-point-exclusion.md)
关闭，不存在完整临界点。

若 $j=4$，余下一条根 $t\ne s$ 必为 $q_s$ 的根，因为 $P_y\mid\Delta_s^6q_s^3$。
因此属于本文41族，§5已给结论。

若 $j=3$，余下二元二次式有两种因式分解。
若为 $\Delta_t^2$，必 $q_s(t)=0$，属于本文32族，故为空。
若为两个不同根 $\Delta_r\Delta_t$，两者都为 $q_s$ 的根。
二元三次式 $q_s$ 因此可准确写成
$c\Delta_r\Delta_t\Delta_v$，其中 $c\ne0$，
第三根 $v$ 允许与 $r$、$t$ 或 $s$ 相同，故没有无重根假设。
于是
$$
P_y\propto\Delta_s^3(q_s/\Delta_v),\qquad q_s(v)=0,
$$
正是[三重乘二次余因子的完整分类](R150-appendix-rank-one-third-cumulant-three-plus-one-plus-one-mean-divisor-classification.md)
所闭的全支。它的唯一存活族为 (5.2)，$s\in\{0,2,-6,\infty\}$，且 $T_3=0$。

三种准确重数已穷尽 (6.1)。这是一段二元多项式分解证明，不依赖有限图或一般位置；
所有合流都已归入平方项或带重根的 $q_s/\Delta_v$。证毕。

故任何尚可能具有非零匹配 Bell 值的秩一 $V$ 临界点，必须满足
$$
\operatorname{ord}_sP_y\le2.
\tag{6.2}
$$
当准确重数二且余下三次式为某个单根方向的三次幂时，它属于本文23族，亦已排除。
其余低接触除子型仍须继续，不能用 (6.2) 宣称整个秩一 $V$ 层已闭。

## 7. 完整原成功运行与源码身份

三个源已在
[run44738311930](https://github.com/Rogerhu12/math-research-public/actions/runs/44738311930)、
job136295226651成功执行；触发提交
`71e86b47cb04a2fffe6ee39331f660feb954ae0d`。
工作流时间为2026-11-20 12:44:31至12:44:58 UTC。
原请求为
[`2026-11-20-r150-short-exact-request-b2a9.json`](../notes/2026-11-20-r150-short-exact-request-b2a9.json)，sequence14。

| 族 | 原验证源 | 源内秒数 | stdout SHA-256 |
|---|---|---:|---|
| 41 | [four-plus-one](../notes/2026-11-20-r150-rank-one-v-four-plus-one-classification-b2a9.py) | 0.995488 | `a499161b1300339d35d970d3de5831fc71098cc0fd40e95e2c65f98fafa66232` |
| 32 | [three-plus-two](../notes/2026-11-20-r150-rank-one-v-three-plus-two-exclusion-b2a9.py) | 1.363287 | `928e1323f279dd291833f8b620c96f89a2b0797364a4ca24b273bd06c74d1154` |
| 23 | [two-plus-three](../notes/2026-11-20-r150-rank-one-v-two-plus-three-exclusion-b2a9.py) | 1.829895 | `f959500cbe0bd70f24495fe63c02f70e410e6a8c01dd647f7b7a04d9a2f23086` |

各源 SHA-256 依次为

- 41：`bbc7dc98b374c3fdf99365ce6d4f1beaa616f14b787ed3a6d273bd95b53f6c55`；
- 32：`e5d0bb10904b7280c182e7f6adeb2f5064090e44ed6c88f73c37215a7d17bf2b`；
- 23：`a6041b3fd3c6b8d39b4af09d10994343d9a338b3d734647a230bb90fe715aaeb`。

本次获取的完整任务日志 SHA-256 为
`149063edb8b52cc979646cb6eb3f49751da26847130af12fa86b19b526397dcc`。
三个标签分别 exit0；原QQ矩族、全部梯度、完整链式法则、两层准确结式、
全部单位分母、特殊降次纤维和射影边界在同一源码中顺序核验。
本稿使用这次成功回执，不重跑已闭大矩阵或更早的五重点计算。
按根规则不保存可重算展开数组。

本稿的高接触分类是原有限临界集中的完整子结果。
普通 Hilbert ISP、一般高秩第三累积量与全局 Jacobian 自然幂证书仍未由它解决。
