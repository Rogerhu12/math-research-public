# 真实除幂源格、对数合流矩阵与逐层共同前缀

日期：2026-11-12。
**状态：以下首带内的整源格、逐层饱和命题及精确指数已证明。**
它处理同一有限次数源中真正相互抵消的混合列。适用条件
$k<pr$ 和 $N_t\le p$ 明确保留；尚未据此控制
$p\ll\sqrt{k}$ 的全部深带。

沿 R174，固定惰性 $p\ge7$，记

$$
r=(p+1)/4,\quad R=r(p-1),\quad
U=v^r g(v^R),\quad u_0=g(0),\quad
\pi_0=u_0^{-1}=p\kappa,\quad \kappa\in\mathbb Z_p^\times.
$$

原环境坐标是 $(a,b)$、基点 $(1,0)$；R174 的整形式坐标满足

$$
U=a-1-b/3+O((a-1,b)^2),\qquad V=b+O((a-1,b)^2).
$$

以下所有前缀均沿同一实际曲线，以 $v=V(w)$ 为输出。
它与 $w=z^4$ 的首项相同，故真实前缀范数不变。

## 1. 保留 b 理想与第一步源格

R174 对 $V$ 的角色平均中，每个实际 $F_{\alpha,2}$ 都含因子 $b$。
其商的原点值是一，因此准确地

$$
V=b\,e(a-1,b),\qquad e(0,0)=1,\qquad e\in\mathbb Z_p[[a-1,b]]^\times.
\tag{1.1}
$$

整形式逆也保留理想 $(V)=(b)$。

在 $k<pr$ 的全部行中，可使用同一个首一式
$V^r-\pi_0U$ 作 R174 的 Weierstrass 余式。
若 $b=V E(U,V)$，则 $E$ 为整形式单位，且在余式环

$$
\mathcal B=\mathbb Z_p[[U]][V]/(V^r-\pi_0U)
$$

中

$$
\frac{b^r}{p}
=\kappa U E(U,V)^r\in\mathcal B.
\tag{1.2}
$$

等式按首一除法理解；所有形式级数在该有限自由
$\mathbb Z_p[[U]]$ 代数中取收敛余式。
因此除 $p$ 后的新混合源确有整余式，而非把
$P=b^rQ+pP_1$ 的两个分量分别当成前缀零。

令

$$
E_D=\mathbb Z_p[a,b]_{\le D},\qquad
E_m=0\quad(m<0).
$$

第一步的真实新格为

$$
L_1=E_D+p^{-1}b^r E_{D-r}
\subset\mathbb Q_p[a,b]_{\le D}.
\tag{1.3}
$$

这是原有限次数空间内的明确格扩张，没有增加环境维数或多项式
次数。它确实允许分母，故也不能把它称作原 $E_D$ 的整基变换。

## 2. 全部有限层格与准确指数

对 $0\le t\le\lfloor D/r\rfloor$，定义

$$
\boxed{\quad
L_t=\sum_{s=0}^{t}p^{-s}b^{rs}E_{D-rs}.
\quad}
\tag{2.1}
$$

其一组真实基是

$$
p^{-\min(t,\lfloor j/r\rfloor)}a^ib^j,
\qquad i,j\ge0,\quad i+j\le D.
\tag{2.2}
$$

因此源格指数精确为

$$
\log_p[L_t:E_D]
=\sum_{s=1}^{t}\binom{D-rs+2}{2}.
\tag{2.3}
$$

每个 $L_t$ 元素在 $\mathcal B$ 中的余式都是整的，由 (1.2) 的
幂次直接得到。写余式为
$\sum_{j<r}V^jR_j(U)$，则对 $rh+j<pr$，

$$
[v^{rh+j}]P(\gamma_v)
=u_0^h[U^h]R_j(U).
\tag{2.4}
$$

因而所有这些 $L_t$ 使用的是同一完整余式矩阵，而不是各自选择
一个有利行。由整余式立即有

$$
\bigl|[v^{rh+j}]P(\gamma_v)\bigr|_p\le p^h
\quad(P\in L_t).
\tag{2.5}
$$

实际限制到准确前缀核时，(2.5) 还应乘相应余式行的像理想；
这里暂只记统一上界。

唯一分块表示可取为

$$
P=\sum_{s=0}^{t-1}p^{-s}b^{rs}Q_s(a,b)
  +p^{-t}b^{rt}Q_t(a,b),
\tag{2.6}
$$

其中 $\deg Q_s\le D-rs$，$s<t$ 时另要求
$\deg_bQ_s<r$；最后 $Q_t$ 的 $b$ 次数不加此限制。

## 3. 第二层真正出现的对数行

将 $\mathcal B/p\mathcal B$ 通过整坐标变换认作

$$
\mathbb F_p[[a-1,b]]/(b^r).
$$

此时 (1.2) 的像是一个确定的形式函数

$$
F(a,b)=
\overline{\kappa U(a-1,b)(b/V(a-1,b))^r}\pmod{b^r}.
\tag{3.1}
$$

故 (2.6) 的准确余式模 $p$ 是

$$
\sum_{s=0}^{t} F(a,b)^s\,\overline{Q_s(a,b)}
\pmod{b^r}.
\tag{3.2}
$$

它包含所有分块之间的抵消，不能分别令各 $Q_s$ 的余式为零。

不过它在 $b=0$ 的行可准确计算。
令

$$
\eta(X)=\frac1{p-1}\sum_{\delta\in\mu_{p-1}}
\delta^{-1}\bigl((1+X)^\delta-1\bigr)
\in\mathbb Z_p[[X]].
\tag{3.3}
$$

由 R174 的实际平均式，在 $b=0$ 有

$$
U(X,0)=\eta(X),\qquad
\left.\frac Vb\right|_{b=0}=\eta'(X).
\tag{3.4}
$$

第二个式子不能只用原点线性项代替：
$F_{\alpha,2}$ 的 $b$ 系数准确为
$\alpha^4(1+X)^{N\alpha-1}$，乘平均权 $\alpha^{-4}$ 后对
$N\alpha\in\mu_{p-1}$ 求和，恰为 $\eta'$。
所以

$$
F(a,0)=\bar\kappa\,
\frac{\bar\eta(a-1)}{\bar\eta'(a-1)^r}.
\tag{3.5}
$$

为给有限阶明确式，若 $1\le n<p$，利用
$\binom{\delta}{n}/\delta=\binom{\delta-1}{n-1}/n$ 及有限和，
得

$$
[X^n]\bar\eta(X)=(-1)^{n-1}/n.
$$

因此到次数 $<p$，

$$
\boxed{\quad
F(a,0)\equiv\bar\kappa\,a^r\log a
\pmod{(a-1)^p}.
\quad}
\tag{3.6}
$$

此处 $\log a$ 只表示其前 $p-1$ 次的整截断。
具体地，$\eta'$ 与 $a^{-1}$ 的误差从次数 $p-1$ 开始，
再乘 $\eta$ 的一次零，才使 (3.6) 的误差从次数 $p$ 开始。
没有把特征 $p$ 中不存在的完整对数原函数当成整级数。

## 4. 合流 Vandermonde 所给的共同饱和命题

设

$$
N_t=\sum_{s=0}^{t}(D-rs+1)
=(t+1)(D+1)-\frac{rt(t+1)}2.
\tag{4.1}
$$

这里仍取 $t\le\lfloor D/r\rfloor$，所以所有求和项均正。

**命题。** 假设

$$
N_t\le p,\qquad r(N_t-1)<k<pr.
\tag{4.2}
$$

若 $P\in L_t$ 的实际完整前缀满足
$\operatorname{ord}_vP(\gamma_v)\ge k$，则

$$
\boxed{\quad
P\in pL_t+p^{-t}b^{r(t+1)}E_{D-r(t+1)},
\qquad P/p\in L_{t+1}.
\quad}
\tag{4.3}
$$

在末层 $t=\lfloor D/r\rfloor$，将 $L_{t+1}$ 理解为 $L_t$；
第二项为零，结论实际迫该前缀核为零。

**证明。**
取唯一分块 (2.6)。由 (2.4)，完整前缀使余式的所有
$[U^hV^j]$ 行在 $rh+j<k$ 时准确为零，当然模 $p$ 也为零。
按 $b$ 次数 $j=0,\ldots,\min(r-1,D)$ 归纳，证明
每个 $\bar Q_s$ 的第 $j$ 个 $b$ 系数均为零。

假设更小的 $b$ 次数已经全部为零。因为整坐标变换保 $(b)=(V)$，
当前最低的 $b^j$ 系数变到 $V^j$ 时仅乘一个形式单位；
$a-1$ 与 $U$ 在该系数环中的换参也有单位首项。
所以前缀零等价地迫当前系数在 $a=1$ 有同样的零阶。
先前全部 $Q_s$ 的低 $b$ 系数已经消失，故当前系数准确是

$$
\sum_{s=0}^{t} F(a,0)^s q_{s,j}(a),\qquad
\deg q_{s,j}\le D-rs-j,
\tag{4.4}
$$

负次数上界表示该项不存在。其未知系数总数为

$$
N_{t,j}=\sum_{s=0}^{t}\max(D-rs-j+1,0).
$$

有 $N_{t,j}\le N_t-j$，所以 (4.2) 保证
$h=0,\ldots,N_{t,j}-1$ 的所需行 $rh+j$ 全在零前缀中。
同时 $N_{t,j}\le p$，允许用 (3.6) 替换 (4.4) 的全部所需 Taylor
系数。得到

$$
\sum_s\bar\kappa^{\,s}a^{rs}(\log a)^s q_{s,j}(a)
\tag{4.5}
$$

在 $a=1$ 消失到阶至少 $N_{t,j}$。

使用 $x=\log a$ 的截断坐标，(4.5) 的基函数是

$$
e^{ex}x^s,\qquad
0\le e\le D-j,\quad
0\le s\le\min(t,\lfloor e/r\rfloor).
\tag{4.6}
$$

其前 $N_{t,j}$ 阶导数矩阵为合流 Vandermonde。
不同节点 $e$ 均在 $0,\ldots,D-j$ 中，而
$D+1\le N_t\le p$，故它们模 $p$ 互异。
每个节点的重数连续从 $s=0$ 开始；行列式为节点差的正幂乘
相应的 $s!$ 和单位 $\bar\kappa^s$，因此是单位。
从导数改成所需 Taylor 行亦仅用 $n!$、$n<N_{t,j}\le p$，
均为单位。于是所有 $q_{s,j}$ 都为零。

逐 $j$ 归纳完成后，$s<t$ 的全部 $Q_s$ 被 $p$ 除；
$Q_t$ 除可被 $p$ 除的部分外，只能含因子 $b^r$。
这正是 (4.3)。最后一层若仍有非零前缀元，先在有限自由格
$L_t$ 中除去最大共同 $p$ 次幂，取得 primitive 元；
(4.3) 又迫其可除 $p$，矛盾。证毕。

## 5. 第一、第二步的明确式及 jet 增益

$t=0$ 时，(4.3) 恢复

$$
rD<k<pr
\quad\Longrightarrow\quad
P\bmod p\in b^r\mathbb F_p[a,b]_{\le D-r},
\quad P/p\in L_1.
\tag{5.1}
$$

当 $D<r$，这立即迫该范围的前缀核为零。

第二步不把 (5.1) 的两个分量拆开处理。
若 $D\ge r$ 且

$$
2D-r+2\le p,\qquad
r(2D-r+1)<k<pr,
$$

则对同一个 $P_1\in L_1$ 的完整零前缀，实际有

$$
P_1/p\in L_2
=E_D+p^{-1}b^rE_{D-r}+p^{-2}b^{2r}E_{D-2r}.
\tag{5.2}
$$

付清这一步的是 (3.6) 的真实对数行和 (4.6) 的共同合流矩阵；
没有以形式坐标可逆性略过混合源。

更一般，若能连续应用到第 $t-1$ 步，则

$$
\{P\in E_D:\operatorname{ord}_vP(\gamma_v)\ge k\}
\subset p^tL_t.
$$

结合 (2.4) 的整余式，得到该真实 jet 的统一上界

$$
\boxed{\quad
\|\varphi_{D,k}\|_p\le p^{\lfloor k/r\rfloor-t}.
\quad}
\tag{5.3}
$$

例如充分条件为
$N_{t-1}\le p$、
$r(N_{t-1}-1)<k<pr$，因各 $N_s$ 随 $s$ 增大。
这是真正限制在全部早行零核后的增益；(2.3) 同时记下了所用新
源格的全部指数。

## 6. 与全深度预算的边界

这里的两项范围限制各有明确来源：

1. $k<pr$ 用于 R174 的准确单首一式
   $V^r-\pi_0U$。到 $pr$ 后，真实稀疏图的下一项不能删去。
2. $N_t\le p$ 用于 (3.6) 的对数截断以及合流矩阵中前 $p$ 阶
   Taylor 与导数的单位转换。越过此范围需要继续支付真实的
   $p$ 进 carry，而不能把完整特征 $p$ 对数写入证明。

特别在 $D$ 取维数允许的最小尺度
$D\asymp\sqrt{2k}$ 时，首带通常只影响 $p\asymp D$ 的一段；
它尚不能制服 $p\ll\sqrt{k}$ 的累计成本。
因此 (5.3) 不等于 R159 的全素数严格不等式。
它提供的下一步对象是明确的格链 (2.1)、同一余式矩阵及其真实
对数重数；继续全深度时需要同步扩大这三者，而不是只数共振。

## 依赖

- [R170 实际全 CM 平面](2026-11-12-full-cm-theta-plane-and-sparse-resonance.md)：
  真整端同态及有限次数源的正确范围。
- [R174 整 Cartan 坐标与同一余式矩阵](2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)：
  $U,V$、准确 $pr$ 范围、首一除法及源尾。
- [R173 全深度基线](2026-11-12-full-depth-cm-carry-envelope-and-true-jets.md)：
  本文的有限带增益不取代其全部阶数基线。

