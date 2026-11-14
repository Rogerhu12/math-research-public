# 全深度共同 jet 核、两层真实消元与准确 AS 缺陷

日期：2026-11-12。**状态：以下全精度公式、两层前缀消元及实际径向
数据比较均已证明。** 它们使用 R177 的完整归一化级数，并一直作用在
同一个原有限次数源上。更高层仍含本文第 5 节的真实缺陷；本文没有把
第一层 Artin–Schreier 方程反复当成特征零等式。

固定惰性素数 $p=4r-1\ge7$，记

$$
R=r(p-1),\qquad X=a-1,\quad Y=b,\qquad
E_D=\mathbb Z_p[X,Y]_{\le D}.
$$

R174 的整 Cartan 坐标及同一个整形式逆给

$$
\widetilde P(U,V)=P(X(U,V),Y(U,V))
 =\sum_{i,l\ge0}L_{i,l}(P)U^iV^l,\qquad P\in E_D.
\tag{1.1}
$$

每个 $L_{i,l}$ 都是原 $E_D$ 上范数至多一的整线性泛函；不按列
另选坐标。取首项一的输出 $v=V(w)$，并记

$$
r_k(P)=[v^k]P(\gamma_v(v)),\qquad
S_{D,k}=\{P\in E_D:r_0(P)=\cdots=r_{k-1}(P)=0\}.
\tag{1.2}
$$

前缀中的零全是准确的特征零等式。输出换参不改变前缀，也不改变
其第一个可能非零系数，故以下结论同样是原 $w$ 参数的真实 jet 结论。

## 1. 全深归一化与准确有限和

R177 已证明

$$
U=\frac{v^r}{p}G\left(\frac{v^R}{p^p}\right),\qquad
G\in\mathbb Z_p[[T]],\quad g_0=G(0)\in\mathbb Z_p^\times,
\quad \bar G+T\bar G^p=\tau,
\tag{1.3}
$$

其中 $\tau=\bar g_0\in\mathbb F_p^\times$。置

$$
C_q^{(i)}=[T^q]G(T)^i\quad(i,q\ge0),\qquad
C_q^{(0)}=\mathbf1_{q=0}.
\tag{1.4}
$$

负下标的 $C$ 约定为零。直接将 (1.3) 代入 (1.1)，对每个 $k$
得到有限和

$$
r_k(P)=
\sum_{\substack{i,q\ge0\\ri+Rq\le k}}
p^{-i-pq}C_q^{(i)}L_{i,k-ri-Rq}(P).
\tag{1.5}
$$

该等式无需交换无限的非收敛求和：固定 $k$ 时，非零 $i,q,l$ 的
集合有限，且 $i=0$ 时只有 $q=0$ 有贡献。

对 $k\ge r$ 唯一写成

$$
k=r\{\alpha+(p-1)t\}+j,\qquad
1\le\alpha\le p-1,\quad t\ge0,\quad 0\le j<r.
$$

令

$$
e=\alpha+pt,\qquad
\mathcal B_{t,\alpha,j}=p^e r_k\in E_D^*.
\tag{1.6}
$$

这里 $e$ 正是 R173 的 $e_p(k)$。以 $q=t-b$、
$i=\alpha+(p-1)b-s$ 重标 (1.5)，得到全深度共同矩阵

$$
\boxed{\quad
\mathcal B_{t,\alpha,j}
=\sum_{b=0}^{t}
 \sum_{s=0}^{\alpha+(p-1)b}
 p^{b+s}C_{t-b}^{(\alpha+(p-1)b-s)}
 L_{\alpha+(p-1)b-s,\,j+rs}.
\quad}
\tag{1.7}
$$

确实 $e-i-pq=b+s$，而剩余的 $v$ 次数准确为 $j+rs$。
在 $\alpha=p-1$ 的端点，(1.5) 还容许 $q=t+1$，但这时只能
有 $i=0$；其系数 $C_{t+1}^{(0)}=0$，故 (1.7) 未漏掉非零项。
$i=0,q=0$ 的一项位于 $b=t,s=\alpha+(p-1)t$，其系数为
$p^eL_{0,k}$；它没有被遗漏。其他 $i=0$ 项由 (1.4) 自动为零。
所有幂 $p^{b+s}$ 非负，因此 (1.7) 同时重新证明 $\mathcal B$ 整。
$k<r$ 时则直接只有 $r_k=L_{0,k}$，无分母。

## 2. 任意精度的同一个有限泛函集合

对任意整数 $N\ge1$，(1.7) 模 $p^N$ 只需保留

$$
b+s<N.
\tag{2.1}
$$

因此，给定余数 $(\alpha,j)$ 后，所有深度 $t$ 在精度 $p^N$ 上
只用同一集合中的至多 $N(N+1)/2$ 个泛函

$$
\boxed{\quad
L_{\alpha+(p-1)b-s,\ j+rs},\qquad
b,s\ge0,\ b+s<N,\ \alpha+(p-1)b-s\ge0.
\quad}
\tag{2.2}
$$

对特定 $t$ 另外取 $b\le t$。这些泛函的指标满足

$$
\begin{aligned}
i&\le\alpha+(p-1)(N-1),\qquad l\le j+r(N-1),\\
i+l&\le\alpha+j+(p-1)(N-1).
\end{aligned}
\tag{2.3}
$$

这里的总阶为 $O(pN)$，不随深度 $t$ 增长。若 $e\ge N$，
上述 $i=0,q=0$ 项自动消失；若 $e<N$，(1.7) 仍准确保留它，
故不需为低层另作不正确的删项约定。

必须区别两种有限性。(2.2) 限制的是**同一源上所用泛函的数目与
Taylor 阶数**。其系数 $C_{t-b}^{(i)}$ 仍来自真实 $G$ 的高阶项。
本文没有把它们换成一组与 $t$ 无关的已知常数，也没有把这些
$L$ 当成 $E_D^*$ 的任意自由坐标。形式逆的次数可能大于 $D$；
这项成本在 (1.1)、(2.3) 中完整保留。

## 3. 第一层可由实际早行整消去

固定 $(\alpha,j)$，以下略去这两个下标。
(1.7) 模 $p$ 只有 $b=s=0$，所以

$$
\mathcal B_t\equiv C_t^{(\alpha)}L_{\alpha,j}\pmod p.
\tag{3.1}
$$

最早的 $t=0$ 行满足

$$
\mathcal B_0=
\sum_{s=0}^{\alpha}p^s g_0^{\alpha-s}
                 L_{\alpha-s,j+rs},
\qquad
\mathcal B_0\equiv g_0^\alpha L_{\alpha,j}\pmod p.
\tag{3.2}
$$

因此对 $t\ge1$，令

$$
u_t=C_t^{(\alpha)}/g_0^\alpha\in\mathbb Z_p,\qquad
\mathcal W_t=(\mathcal B_t-u_t\mathcal B_0)/p.
\tag{3.3}
$$

这是整个原源上的整泛函。若 $P\in S_{D,k}$，$t=0$ 行是真正
较早的行，故 $\mathcal B_0(P)=0$。于是

$$
t\ge1\quad\Longrightarrow\quad
v_p(r_k(P))\ge-e+1.
\tag{3.4}
$$

这不是从某个单项式的分母得来的估计；实际准确前缀正是消掉
$\mathcal B_0$ 所需的条件。

## 4. AS 方程再给第二层真实消元

由 (1.7) 保留 $b+s\le1$，对 $t\ge1$ 有

$$
\begin{aligned}
\mathcal B_t\equiv{}&C_t^{(\alpha)}L_{\alpha,j}
 +p C_t^{(\alpha-1)}L_{\alpha-1,j+r}\\
&+p C_{t-1}^{(\alpha+p-1)}L_{\alpha+p-1,j}
\pmod {p^2}.
\end{aligned}
\tag{4.1}
$$

当 $\alpha=1$ 时第一行的第二项按 $C_t^{(0)}=0$ 理解；
而 (3.2) 的相应低行仍保留 $pL_{0,j+r}$。
因此 (3.3) 准确给

$$
\begin{aligned}
\mathcal W_t\equiv{}&
\left(C_t^{(\alpha-1)}-g_0^{-1}C_t^{(\alpha)}\right)
 L_{\alpha-1,j+r}\\
&+ C_{t-1}^{(\alpha+p-1)}L_{\alpha+p-1,j}
\pmod p.
\end{aligned}
\tag{4.2}
$$

乘 R177 的 $\bar G+T\bar G^p=\tau$ 以
$\bar G^{\alpha-1}$，得到

$$
\bar G^{\alpha-1}-\tau^{-1}\bar G^\alpha
 =\tau^{-1}T\bar G^{\alpha+p-1}.
\tag{4.3}
$$

故整条行 (4.2) 缩成

$$
\boxed{\quad
\mathcal W_t\equiv C_{t-1}^{(\alpha+p-1)}
 \left(L_{\alpha+p-1,j}+\tau^{-1}L_{\alpha-1,j+r}\right)
\pmod p.
\quad}
\tag{4.4}
$$

$t=1$ 的系数是 $g_0^{\alpha+p-1}$，为单位，约化为 $\tau^\alpha$。
因此若 $t\ge2$，取

$$
v_t=C_{t-1}^{(\alpha+p-1)}/g_0^{\alpha+p-1}\in\mathbb Z_p,
$$

便有原源上的整泛函

$$
\mathcal Z_t=
\frac{\mathcal B_t-v_t\mathcal B_1-(u_t-v_tu_1)\mathcal B_0}{p^2}.
\tag{4.5}
$$

对真实 $P\in S_{D,k}$，两个早行 $t=0,1$ 都准确为零，所以

$$
\boxed{\quad
v_p(r_k(P))\ge-e+\min(t,2).
\quad}
\tag{4.6}
$$

全部操作都是同一源的共同整行组合。除以 $p$ 或 $p^2$ 前，
已先证明相应整行的所有值均有该整除性；没有除去一个可能非整
的个别列，也没有把前缀条件按分量拆开。

## 5. 再下一层是原曲线的明确缺陷

定义准确整级数

$$
\mathscr E(T)=\frac{G(T)+TG(T)^p-g_0}{p}\in T\mathbb Z_p[[T]].
\tag{5.1}
$$

它整是 R177 的完整约化，零常数则来自 $G(0)=g_0$。
在 Cartan 坐标取

$$
\mathcal H(U,V)=U^p+pU-g_0V^r.
$$

将 (1.3) 代入，三个因子准确相消为

$$
\boxed{\quad
\mathcal H(\gamma_v(v))
=p v^r\mathscr E\left(v^R/p^p\right).
\quad}
\tag{5.2}
$$

特别若 $e_t=[T^t]\mathscr E$，则

$$
[v^{r+tR}]\mathcal H(\gamma_v)=p^{1-pt}e_t,
\qquad
p^{1+pt}[v^{r+tR}]\mathcal H(\gamma_v)=p^2e_t.
\tag{5.3}
$$

因此两层消元之后真实出现的对象已经明确；其高阶系数不能由
单独的模 $p$ 方程任意删去。比如，若 $\mathscr E$ 的前若干系数
为零，(5.3) 仍必须保留第一个非零系数及其准确幂 $p^{1-pt}$。
本文不假定这种消失实际发生，也不以自由选取的 $\mathscr E$
替代原 theta 曲线。

还有必要的源限制：$\mathcal H$ 是整 **Cartan 形式坐标**中的
次数 $p$ 多项式；将它写回 $X,Y$ 一般是完整整形式级数。
它不是自动属于原 $E_p$ 的多项式。R177 第 6 节另外构造的
$X^p+pX-\widetilde\tau Y^r$ 是真正的原源提升，二者必须区分。
任何把 (5.2) 纳入新的有限源格的步骤，都仍要支付写回原源的
次数与尾界，并让缺陷和其乘子共享同一准确前缀。

## 6. 两层数据在原齐次源上准确闭合

这里把 (4.1) 的三个 $L$ 接回实际 theta 源，而不把它们当成自由
未知量。沿用 R175 的径向轴

$$
u(\eta)=\sum_{n\equiv1\ (p-1)}\eta^n/n!,\qquad
A(\eta)=u'(\eta),\qquad
\mathfrak a(U)=e^{\eta_0(U)},\quad
\mathfrak b(U)=A(\eta_0(U)),
\tag{6.1}
$$

其中 $\eta_0=u^{-1}$。已证明
$\mathfrak a\in1+U\mathbb Z_p[[U]]$、
$\mathfrak b\in1+U\mathbb Z_p[[U]]$，且

$$
\mathfrak b=\mathfrak a/\mathfrak a',\qquad
[U](\mathfrak a-1)=1.
$$

令 $H$ 在 $a,b$ 中齐次次数 $d$，且 $H(a,0)=0$。
取 $g_j=L_{0,j}(H)$。R175 已给 $1\le j\le r$ 的完整轴式

$$
\sum_{h\ge0}L_{h,j}(H)U^h
   =g_j\mathfrak a(U)^d\mathfrak b(U)^{-j}.
\tag{6.2}
$$

同时 $L_{h,0}(H)=0$ 对全部 $h$ 成立。
为覆盖 (4.1) 的第二项，下面再保留下一 $V$ 带。
写 $b_1=[w^{r+1}]b(w)$，置

$$
\kappa=u_0-b_1\in\mathbb Z_p.
\tag{6.3}
$$

其整性可直接核准。真实周期 $q(s)=s\mathcal L(s)^4$ 及其逆
到次数 $r+1$ 整；因为这段 $\mathcal L$ 的分母 $4n+1$
不含 $p$，而其他分母是 $2$ 的幂。
$a(w)$ 的 $w^r$ 项与 $u_0$ 只差整项，$b(w)=s(w)a(w)$ 的
$w^{r+1}$ 项又与该 $a$ 系数只差整项。因此 (6.3) 成立。

在真正的 $(\eta,w)$ 坐标，有限角色平均准确给

$$
\begin{aligned}
U&=u(\eta)+u_0 A(\eta)w^r+O(w^{2r}),\\
V&=A(\eta)w+b_1 A'(\eta)w^{r+1}+O(w^{2r+1}).
\end{aligned}
\tag{6.4}
$$

这些是保留真实第一类周期的公式。固定 $U$ 反解第一式，再用
$A'(\eta_0)=\mathfrak b\mathfrak b'$，得到

$$
\eta=\eta_0-u_0w^r+O(w^{2r}),\qquad
w=V/\mathfrak b+\kappa\mathfrak b'(V/\mathfrak b)^{r+1}
          +O(V^{2r+1}).
\tag{6.5}
$$

若 $H(\gamma(w))=\sum h_nw^n$，齐次性给
$H=e^{d\eta}\sum h_nw^n$。由于 $h_0=0$，二次误差从
$V^{2r+1}$ 才可能影响；比较 $V^{j+r}$、$0\le j\le r$ 得

$$
\boxed{\quad
\sum_{h\ge0}L_{h,j+r}(H)U^h
=\mathfrak a^d\mathfrak b^{-j-r}
       \{g_{j+r}+j\kappa\mathfrak b' g_j\}.
\quad}
\tag{6.6}
$$

具体地，反解先给括号
$h_{j+r}+(j\kappa\mathfrak b'-du_0)h_j$。
在 $U=0$，$\mathfrak b'(0)=0$，故
$g_{j+r}=h_{j+r}-du_0h_j$；这正好给 (6.6)，并保留了
两项中原有的相同首极。不能将 $h_{j+r}$ 单独视为整。

所以对每个实际齐次 $H$，(4.1) 在所有深度所需的数据仅是

$$
g_j,\quad g_{j+r},\quad
[U^n]\mathfrak a^d\mathfrak b^{-j},\quad
[U^n]\mathfrak a^d\mathfrak b^{-j-r},\quad
[U^n]\mathfrak a^d\mathfrak b^{-j-r}\mathfrak b'.
\tag{6.7}
$$

这里的径向级数是同一组真实整级数；$d$ 是原齐次次数。
特别，越过 $h=p-1$ 后的 $L$ 已由 (6.2)、(6.6) 支付，
没有把 R175 的低总次数 Euler 式无误差外推。

### 6.1. 任意 V 带的同一整径向坐标

上述两带也包含在一个全精度的整构造中。这里的 $s=b/a$ 是
环境变量。解整隐函数方程

$$
U(a_{\mathrm{sec}}(s)-1,s a_{\mathrm{sec}}(s))=0,
\qquad a_{\mathrm{sec}}(0)=1.
\tag{6.8}
$$

对 $a$ 的初始导数为一，故
$a_{\mathrm{sec}}\in1+s\mathbb Z_p[[s]]$ 唯一存在。
令

$$
\nu(s)=V(a_{\mathrm{sec}}(s)-1,s a_{\mathrm{sec}}(s))
      =s+O(s^2)\in\mathbb Z_p[[s]].
$$

在同一个真整逆 $a=a(U,V),b=b(U,V)$ 中定义

$$
\Gamma(U,V)=\frac{a(U,V)}{a_{\mathrm{sec}}(b/a)},\qquad
\zeta(U,V)=\nu(b/a).
\tag{6.9}
$$

分母常数为一，故二者均整；它们满足

$$
\Gamma(0,V)=1,\quad\zeta(0,V)=V,\qquad
\Gamma-1=U+O((U,V)^2),\quad\zeta=V+O((U,V)^2).
\tag{6.10}
$$

因此 $(\Gamma-1,\zeta)$ 是另一组同一环境的整形式坐标。
对齐次次数 $d$ 的 $H$，沿径向缩放到 $U=0$ 截面，准确有

$$
\boxed{\quad
\widetilde H(U,V)=\Gamma(U,V)^d g_H(\zeta(U,V)),
\qquad g_H(V)=\widetilde H(0,V).
\quad}
\tag{6.11}
$$

这是齐次性的实际等式，既非近似，也未将 $\Gamma,\zeta$
添加为原有限次数源的自由列。

取真实 Teich 群中范数为一的子群，除去原作用核 $\mu_4$
后其阶为 $r$。它在 $(U,V)$ 上是 $(U,V)\mapsto(U,\epsilon V)$，
$\epsilon\in\mu_r$，保留 (6.8) 的 $U=0$ 截面。
因对应实际 CM 映射齐次次数为一，它与径向缩放交换。
故 $\Gamma$ 不变，$\zeta$ 具有 $V$ 的特征，从而可写成

$$
\Gamma(U,V)=\Gamma_*(U,V^r),\qquad
\zeta(U,V)=V Z_*(U,V^r),
\tag{6.12}
$$

其中 $\Gamma_*,Z_*\in\mathbb Z_p[[U,W]]$ 都为单位。
此角色论证可先在未分歧二次整数环进行；(6.9) 的原系数本在
$\mathbb Z_p$，所以支撑结论下降到同一个原系数格。
在 $W=0$ 上有 $\Gamma_*(U,0)=\mathfrak a(U)$、
$Z_*(U,0)=\mathfrak b(U)^{-1}$。

若 $g_H(V)=\sum g_lV^l$，对全部 $h,q\ge0$、$0\le j<r$，
(6.11) 给

$$
\boxed{\quad
L_{h,j+rq}(H)
=[U^h]\sum_{s=0}^{q}g_{j+rs}
 [W^{q-s}]\Gamma_*(U,W)^d Z_*(U,W)^{j+rs}.
\quad}
\tag{6.13}
$$

因此精度 $p^N$ 的 (2.2) 对每个原齐次部分，只用
$g_j,g_{j+r},\ldots,g_{j+r(N-1)}$ 和同一个整径向核。
所有 $h$ 均合法；(6.2)、(6.6) 是其前两带的明确展开。
这进一步限制了实际源输入，但仍不消除 (1.7) 中
$C_{t-b}^{(i)}$ 所含的真实高阶 $G$ 系数，也不取消原源次数
与整形式变换高次尾的成本。

## 7. 中央余数 j=0 的准确解释

在原源 $\mathbb Z_p[\mathcal A,\mathcal B]_{\le D}$ 中，
正次数齐次部分 $H_m$ 的 $ab$ 次数为 $d_m=17m$，且被 $b$ 除。
令 $c_m=\beta_r(H_m)=[w^r]H_m(\gamma(w))=g_{m,r}$。
对 $1\le\alpha\le p-1$，(6.2) 的低阶系数准确给

$$
\boxed{\quad
L_{\alpha+p-1,0}(H)+\tau^{-1}L_{\alpha-1,r}(H)
 =\frac{\tau^{-1}}{(\alpha-1)!}
        \sum_{m=1}^D(17m)^{\alpha-1}c_m
\quad\text{于 }\mathbb F_p.
\quad}
\tag{7.1}
$$

第一项本来恒为零；第二项只读次数 $\alpha-1\le p-2$，
此处 $\mathfrak a^d\mathfrak b^{-r}$ 的系数就是
$d^{\alpha-1}/(\alpha-1)!$。
因此本篇两层共同核在中央余数上，准确回到 R175 的同一组
中央矩，没有凭空产生新的全局 Hecke 值。

当 $D<p$、$H$ 已有 $rD$ 的完整前缀且原两线性中央值都模 $p$
为零时，R175 给全部 $c_m=0\pmod p$。此时 (4.1) 在所有深度
$t$ 的 $j=0$ 行模 $p^2$ 都为零。
但应保留已付范围：若前缀本来已经到 $r(D+1)$，同样的全部
$c_m$ 消去无需中央假设就成立；对 $t\ge2$，(4.6) 又已经有
无条件的两层收益。不能把这些相同消去重复累计成新的全深
预算，或假定高次数乘积自身具有 rank-two 中央零性。

## 8. 已付的共同性与下一算术输入

(1.7) 对所有 $D,k$ 是同一原源的准确行，(2.2) 对任意精度
保留全部列，(4.5) 对真正饱和前缀给两次合法整消元。
(5.2) 与 (6.6) 分别准确指出下一深层缺陷和原齐次源的两带
径向数据。它们没有免费扩大源，也没有将 Cartan 高次尾丢弃。

两层自动收益仍不构成 R159 的严格总和。
若要继续迭代，需给实际 $\mathscr E$ 的高精度共同关系，或在
含其乘子的真实次数格中完成进一步饱和消元；单独重复
$\bar G+T\bar G^p=\tau$ 不足以支付这一步。

## 依赖

- [R174：真实整 Cartan 坐标及同一原源](2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R173：全部阶的准确分母基线](2026-11-12-full-depth-cm-carry-envelope-and-true-jets.md)。
- [R175：原 Euler 轴与中央矩](2026-11-12-euler-cartan-rows-and-joint-central-prefix-gain.md)。
- [R176：首带的实际除幂源格](2026-11-12-actual-divided-source-lattices-and-prefix-saturation.md)。
- [R177：完整 AS 约化、正反向整级数及原源提升](2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)。
