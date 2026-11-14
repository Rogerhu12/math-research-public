# R171：无界一阶乘子的 UHF 最高系数多项式不能有界化

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R171。

状态：完整证明。所有测试向量都是实际有限柱向量；真实进位通过有限张量截断差逐项付清。本稿不对未知不变限制声称同一结论。

## 1. 主结论

设

$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
a\in\ell^2\setminus\ell^1,
$$

且 $X=X_u$ 是 R125 的实际闭一阶乘子。记 $\mathcal D$ 为有限柱向量空间，$\mathfrak U$ 为实际 UHF 代数。

**定理1.1。** 令 $p\ge1$，取 $E_0,\ldots,E_p\in B(H)$，并假定

$$
E_p\in\mathfrak U\setminus\{0\}.
$$

则 $\mathcal D\subseteq\operatorname{Dom}X^p$，并且

$$
\boxed{
\sum_{k=0}^pE_kX^k
\text{ 在 }\mathcal D\text{ 上无界}.
}
\tag{1.1}
$$

只有最高系数要求属于 UHF；低阶系数甚至无需与 $X$ 交换。

更精确地，存在有限柱单位向量 $x_n$、复数 $\lambda_n$ 及 $c>0$，使

$$
|\lambda_n|\longrightarrow\infty,\qquad
\|E_px_n\|\ge c,
$$

且

$$
\left\|\sum_{k=0}^pE_kX^kx_n-\lambda_n^pE_px_n\right\|
=O(|\lambda_n|^{p-1}).
\tag{1.2}
$$

可以令 $x_n$ 两两正交。这里的 $\lambda_n$ 随测试向量趋于无穷，不是给 $X$ 增加一个有限近似谱点。

证明分三步：真实 carry 的一致次数加权界、任意有限 Walsh 翻转后的统一中心矩界，以及 UHF 最高系数的局部下界。

## 2. 有限支撑算子的次数加权界

令 $\mathcal N$ 为 Walsh 次数算子，$\mathcal N\chi_F=|F|\chi_F$，置

$$
\Lambda=I+\mathcal N.
$$

若有界算子 $B$ 只作用于某个含 $L$ 位的有限物理张量块，则对每个整数 $s\ge0$，

$$
\boxed{
B\operatorname{Dom}\Lambda^s\subseteq\operatorname{Dom}\Lambda^s,\qquad
\|\Lambda^sBx\|
\le(L+1)^s\|B\|\,\|\Lambda^sx\|.
}
\tag{2.1}
$$

证明：按块外 Walsh 次数 $q$ 分解，$B$ 不改变 $q$。在该分量上，块内次数介于0和 $L$，因此

$$
\|(q+1+\mathcal N_{\rm block})^sBv\|
\le(q+L+1)^s\|B\|\|v\|
\le(L+1)^s\|B\|\,
\|(q+1+\mathcal N_{\rm block})^sv\|.
$$

对各 $q$ 平方求和，并用闭性取极限，得到 (2.1)。

记 $J_F=M_{\chi_F}$，$F$ 为任意有限位集。若 $B$ 支撑于上述块，则

$$
J_FBJ_F=J_{F\cap{\rm block}}BJ_{F\cap{\rm block}}
$$

仍支撑于同一块，范数仍为 $\|B\|$。所以 (2.1) 的常数不依赖 $|F|$，即使 Walsh 翻转使用很多高位也不增加块的支撑长度。

## 3. 实际 carry 的局部绝对分解

沿用真实算子

$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
\eta_j=\alpha_{j+1}/\alpha_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1},
$$

以及纯算子

$$
S_j=I-2E_j.
$$

本模型有 $\eta_*:=\sup_j\eta_j<1/4$、$\eta\in\ell^2$。

对 $m>j$，在第 $m$ 位把递归尾置零，得到

$$
N_j^{[m]}
=\sum_{r=j}^{m-1}
\frac{\alpha_r}{\alpha_j}
E_j^*\cdots E_{r-1}^*E_r.
\tag{3.1}
$$

它支撑于 $[j,m)$，是有限物理链上的加权前移，所有非零权不超过1，所以 $\|N_j^{[m]}\|\le1$。平方递归仍给

$$
\|(N_j^{[m]})^2\|\le\eta_j.
$$

因此

$$
\|(I+N_j^{[m]})^{-1}\|
\le\frac{2}{1-\eta_*}<3.
\tag{3.2}
$$

令

$$
V_j^{[m]}=(I-N_j^{[m]})(I+N_j^{[m]})^{-1}.
$$

在第一层有 $V_j^{[j+1]}=S_j$。对 $m\ge j+1$，置

$$
B_{j,m}=V_j^{[m+1]}-V_j^{[m]}.
$$

(3.1) 给

$$
\|N_j^{[m+1]}-N_j^{[m]}\|
=\alpha_m/\alpha_j.
$$

由 $V=2(I+N)^{-1}-I$ 的逆差恒等式和 (3.2)，

$$
\boxed{
\operatorname{supp}B_{j,m}\subseteq[j,m],\qquad
\|B_{j,m}\|\le18\,\alpha_m/\alpha_j.
}
\tag{3.3}
$$

同时 $V_j^{[m]}\to V_j$ 按范数成立，所以

$$
\boxed{
V_j-S_j=\sum_{m\ge j+1}B_{j,m}
}
\tag{3.4}
$$

是实际 UHF 内的绝对范数收敛式。并且

$$
\alpha_m/\alpha_j
=\prod_{\nu=j}^{m-1}\eta_\nu
\le\eta_j\eta_*^{m-j-1}.
\tag{3.5}
$$

### 3.1 任意有限 Walsh 翻转后的统一 Sobolev 界

设

$$
K(a)=\sum_j a_j(V_j-S_j).
$$

由 (3.3)—(3.5) 及 Cauchy–Schwarz，这个级数按范数绝对收敛。对任意有限 $F$，令

$$
K_F=J_FK(a)J_F.
$$

用 (2.1) 逐项估计 (3.4)，得到对每个整数 $s\ge0$，

$$
\boxed{
\|\Lambda^sK_Fx\|
\le\kappa_s\|a\|_2\,\|\Lambda^sx\|,
}
\tag{3.6}
$$

其中可以取

$$
\kappa_s
=18\|\eta\|_2
\sum_{\ell\ge1}(\ell+2)^s\eta_*^{\ell-1}<\infty.
\tag{3.7}
$$

常数只依赖 $s$ 及固定模型，不依赖 $F$ 的位置或大小。

这里还包含真正的域保持。对 $x\in\operatorname{Dom}\Lambda^s$，局部有限和在该加权范数中 Cauchy；其普通范数极限是 $K_Fx$，由 $\Lambda^s$ 闭性得到 $K_Fx\in\operatorname{Dom}\Lambda^s$。没有仅凭普通算子范数收敛就断言保持无界次数域。

## 4. 纯一阶算子的统一次数界

在 Walsh 基上，

$$
S_j\chi_G=
\begin{cases}
\chi_{G\cup\{j\}},&j\notin G,\\
2\chi_G-\chi_{G\setminus\{j\}},&j\in G.
\end{cases}
\tag{4.1}
$$

令 $X^0(b)=\sum_jb_jS_j$ 的纯闭实现，$b\in\ell^2$，此处不含常数项。它分为创建、消去、对角三个部分。

在纯次数 $q$ 上，这三部分的范数分别至多

$$
\sqrt{q+1}\|b\|_2,\qquad
\sqrt q\|b\|_2,\qquad
2\sqrt q\|b\|_2.
\tag{4.2}
$$

前两项由每个输出集合上的 Cauchy–Schwarz 得到；第三项使用 $|\sum_{j\in G}b_j|\le\sqrt q\|b\|_2$。

因创建只使次数增加1，(4.2) 给对整数 $s\ge0$，

$$
\boxed{
\|\Lambda^sX^0(b)x\|
\le(2^s+3)\|b\|_2\,\|\Lambda^{s+1/2}x\|
\le(2^s+3)\|b\|_2\,\|\Lambda^{s+1}x\|.
}
\tag{4.3}
$$

先在有限 Walsh 和上证明，再在 $\operatorname{Dom}\Lambda^{s+1}$ 中逼近，并利用 $X^0(b)$ 和 $\Lambda^s$ 的闭性，便得完整域式

$$
X^0(b)\operatorname{Dom}\Lambda^{s+1}
\subseteq\operatorname{Dom}\Lambda^s.
\tag{4.4}
$$

这些估计不要求 $b\in\ell^1$，也不要求同一相位。

## 5. 翻转后的实际中心矩一致有界

R125 的实际构造给准确的有界扰动关系

$$
X=a_*I+X^0(a)+K(a),
\qquad \operatorname{Dom}X=\operatorname{Dom}X^0(a).
\tag{5.1}
$$

对有限 $F$，定义

$$
a_j^F=
\begin{cases}
-a_j,&j\in F,\\
a_j,&j\notin F,
\end{cases}
\qquad
\lambda_F=a_*+2\sum_{j\in F}a_j.
\tag{5.2}
$$

因为 $J_FS_jJ_F=2I-S_j$ 当 $j\in F$，否则不变，有限柱上的恒等式及闭包给

$$
\boxed{
L_F:=J_FXJ_F-\lambda_FI
=X^0(a^F)+K_F
}
\tag{5.3}
$$

连同其真实定义域相等。$\|a^F\|_2=\|a\|_2$。

结合 (3.6) 和 (4.3)，置

$$
D_s=(2^s+3+\kappa_s)\|a\|_2,
$$

则

$$
\boxed{
\|\Lambda^sL_Fx\|
\le D_s\|\Lambda^{s+1}x\|,
\qquad
L_F\operatorname{Dom}\Lambda^{s+1}
\subseteq\operatorname{Dom}\Lambda^s.
}
\tag{5.4}
$$

常数与 $F$ 无关。

固定 $r\ge1$ 及 $v\in\operatorname{Dom}\Lambda^r$。逐次使用 (5.4) 得

$$
v\in\operatorname{Dom}L_F^r,\qquad
\boxed{
\|L_F^rv\|
\le\left(\prod_{s=0}^{r-1}D_s\right)\|\Lambda^rv\|.
}
\tag{5.5}
$$

特别有限柱 $v$ 属于所有这些自然幂域。这也独立证明 $\mathcal D\subseteq\bigcap_r\operatorname{Dom}X^r$；本稿不需要预设高次自然乘积已经闭。

由 (5.3)，对固定有限柱 $v$，

$$
\boxed{
\|(X-\lambda_FI)^rJ_Fv\|
=\|L_F^rv\|\le C_{r,v}
}
\tag{5.6}
$$

且 $C_{r,v}$ 不依赖有限集 $F$。

这是后文的关键：翻转位数可以增长，但 carry 估计没有随该位数乘上不受控常数。

## 6. 选出趋于无穷的中心

$a\notin\ell^1$。把非零 $a_j$ 的辐角分进有限多个开角小于 $\pi$ 的扇区，至少一个扇区满足其中 $\sum|a_j|=\infty$。

所以存在 $\theta\in\mathbb R$、$c_0>0$ 及无限指标集 $I$，使

$$
\operatorname{Re}(e^{-i\theta}a_j)\ge c_0|a_j|
\quad(j\in I),\qquad
\sum_{j\in I}|a_j|=\infty.
\tag{6.1}
$$

删掉任意固定有限头后仍成立。可递归选择两两不交的非空有限集 $F_n\subset I$，都位于该头之外，且

$$
\left|\lambda_{F_n}\right|
=\left|a_*+2\sum_{j\in F_n}a_j\right|
\longrightarrow\infty.
\tag{6.2}
$$

这里只需要有限子集和无界，不依赖原顺序部分和是否收敛。例如交替调和型系数也符合 (6.1)。

## 7. UHF 最高系数的下界与主定理证明

令 $E_p\in\mathfrak U\setminus\{0\}$。取有限头 $[0,m)$ 上的矩阵 $K$，使

$$
\|E_p-K\otimes I\|<\tfrac14\|E_p\|.
\tag{7.1}
$$

在该有限维头空间中选单位向量 $v$，使 $\|Kv\|=\|K\|$。对所有尾向量 $h$，

$$
\begin{split}
\|E_p(v\otimes h)\|
&\ge(\|K\|-\|E_p-K\otimes I\|)\|h\|\\
&>\tfrac12\|E_p\|\,\|h\|.
\end{split}
\tag{7.2}
$$

把 $v$ 视为头上有限柱、尾上常向量。按 §6 在 $m$ 之后选 $F_n$，令

$$
x_n=J_{F_n}v=v\otimes\chi_{F_n},
\qquad \lambda_n=\lambda_{F_n}.
$$

则 $x_n$ 是有限柱单位向量，且因 $F_n$ 两两不交、非空而两两正交。由 (7.2)，

$$
\|E_px_n\|\ge\tfrac12\|E_p\|.
\tag{7.3}
$$

对每个固定 $k\le p$，标量平移的有限二项式及 (5.6) 给

$$
X^kx_n
=\lambda_n^kx_n+
\sum_{r=1}^k\binom kr\lambda_n^{k-r}
(X-\lambda_nI)^rx_n,
$$

其中各个自然幂均已由 §5 证明有定义。因此

$$
\|X^kx_n-\lambda_n^kx_n\|
\le C_{k,v}'(1+|\lambda_n|)^{k-1}.
\tag{7.4}
$$

低阶各 $E_k$ 仅使用有界性。合并 (7.4)，有固定 $C$ 使

$$
\left\|\sum_{k=0}^pE_kX^kx_n-\lambda_n^pE_px_n\right\|
\le C(1+|\lambda_n|)^{p-1}.
\tag{7.5}
$$

所以

$$
\left\|\sum_{k=0}^pE_kX^kx_n\right\|
\ge\tfrac12\|E_p\||\lambda_n|^p
-C(1+|\lambda_n|)^{p-1}
\longrightarrow\infty.
$$

这证明定理1.1。

## 8. 直接后果及域范围

### 8.1 任何非恒定标量多项式都没有 UHF 左正则子

若 $q$ 是正次数标量多项式、$0\ne E\in\mathfrak U$，则

$$
\boxed{E\,q(X)\text{ 在 }\mathcal D\text{ 上无界}.}
\tag{8.1}
$$

只需把最高系数取为 $q_pE\ne0$。因此任何与这个有限柱作用一致的闭实现，都不能经一个非零 UHF 左乘变成有界算子。

$p=1$ 时重得 R170 的一阶左乘障碍；这里不依赖 $q(X)$ 的预解集是否为空。

### 8.2 不存在正次数的实际 UHF 系数代数关系

若 $E_p\ne0$ 属于 UHF，其余系数有界，则不可能在全部 $\mathcal D$ 上有

$$
\sum_{k=0}^pE_kX^k=0,
$$

甚至不可能使这个和等于任意一个全域有界算子。后者只需把该算子移入常数项。

特别，没有非零 $\mathcal A$ 系数的正次数多项式在有限柱上湮灭 $X$。这是实际算子作用的陈述；它不通过一个尚未建立的形式级数为无界 $X$ 定义符号。

### 8.3 快分式系数必须保留原关系的共同域

更一般，假设 $r_0,\ldots,r_p\in\operatorname{Frac}\mathcal G$、$r_p\ne0$，并声称

$$
\sum_{k=0}^p T_{r_k,H}X^kf=0
\qquad(f\in\mathcal D),
\tag{8.2}
$$

其中每个 $X^kf$ 确实在对应最大闭分式的域中。

选共同非零分母 $b\in\mathcal G$，使 $r_k=a_k/b$、$a_k\in\mathcal G$。R153 的真实分母恒等式允许将 (8.2) 乘以 $b$，得到

$$
\sum_{k=0}^p a_kX^kf=0
\qquad(f\in\mathcal D).
$$

最高系数 $a_p\ne0$ 属于 $\mathcal G\subseteq\mathfrak U$，与定理1.1矛盾。

这里明确要求原关系在全部有限柱上具有合法共同域。本稿没有把一个仅在未知较小域上成立的形式关系自动延拓到 $\mathcal D$。

## 9. 尚未解决的限制问题

测试 $x_n=v\otimes\chi_{F_n}$ 是为 UHF 局部下界构造的全空间向量。没有证明它们属于某个未知非零 $A$ 不变空间 $M$。

因此，本稿不排除 $X|_M$ 有界，也不排除慢平方共振中已知的

$$
X|_M=Y|_M,\qquad Y\in\mathcal A.
$$

同样，不能把 $P_M$ 在 R164 的较大渐近交换代数中，误当成 $P_M\in\mathfrak U$ 来使用 (7.1)。

自然幂的闭性与标量算子多项式的完整谱分类另见 R172；即使那些真算子多项式已全部单射稠密，也不等于相应点态 $q(u)$ 的乘子，因为后者仍有 Bell 修正。

一般慢共振核及完整 Hilbert 不变子空间问题仍未解决。
