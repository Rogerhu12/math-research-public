# R408：两来源导子的全部特征 p 核与无十七倍损失的饱和范围

日期：2026-11-14。**状态：已证明。** 本篇在 R406 的同一个实际扩源上计算导子的全部模 $p$ 核。特别，对共同惰性范围 $p>83$，R406 的条件 $p>17f_D+151J$ 可以替换为 $f_D<p$，同时保留全部十七个实际 $T$ 部分。这里不声称这个简短充分条件是所有 $D$ 的最优界；下文的完整核公式给出每个 $D$ 的准确判据。所得饱和属于实际来源导子，不把它混同于物理评价矩阵的饱和或两条完整中央条件的非零。

## 1. 固定扩源与两个真正独立的指标

取 R403/R406 的共同 $E_1$ 模型及
$$
h_7=16t^2+4t+7,\qquad a=t(t-1)h_7,
$$
$$
V=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3).
$$
原径向变量记为 $\mathscr R$。新来源 $T$ 满足
$$
T^{17}(1+8t)^{19}
=\mathscr R^{36}(aV/7)^{17}.
\tag{1}
$$
系数取特征零 DVR $\mathcal O$，均匀化元为 $p$，剩余域 $k$ 完美。只涉及来源代数的部分允许所有 $p\notin\{2,3,7,17\}$；与已有三块/中央比较合用时仍保留原共同条件 $p=6s-1>83$。

令
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
q_n=\frac{(th_7)^{A_n}(t-1)^{B_n}}{(1+8t)^{C_n}},
\qquad
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2,
$$
$$
f_n=\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4.
\tag{2}
$$
对 $D\ge1$、$0\le J\le16$，仍取原有限自由来源
$$
\mathcal W_{D,J}
=\bigoplus_{n=0}^{D}\bigoplus_{j=0}^{J}
 \mathscr R^nq_n(t)\mathcal O[t]_{\le e_{n+1}}T^j.
\tag{3}
$$
没有除以 $T$、$V$ 或原公共 $G_0$ 来创造新的列；(3) 正是 R406 的实际列，乘回同一个 $G_0$ 后保留原 charge 四十。

以下使用保持 $\mathscr R$ 不动的导子 $\partial_t$ 在 (1) 上的唯一延伸，以及 R406 已证闭合的
$$
\delta=t\partial_t,\qquad
W_3=\mathscr R^3t(t-1)^2h_7^2V,\qquad
\mathcal Q_3=W_3\delta:
\mathcal W_{D,J}\longrightarrow\mathcal W_{D+3,J}.
\tag{4}
$$
闭合来自真实多项式 (R406.8)，所有分母仅含固定单位；目标仍有整个明确整基。

**独立性核定。** 在 $K(t)(\mathscr R)$ 的 $\mathscr R$ 赋值处，(1) 右端赋值为 $36$。设一个根生成扩张的赋值分歧指数为 $e$，则 $17\mid36e$，故 $17\mid e$。扩张次数至多十七，因而恰为十七。这同样适用于特征零和上述好特征。于是 $1,T,\ldots,T^{16}$ 在 $K(\mathscr R,t)$ 上独立。固定 $j$ 后，$\mathscr R^n$ 在 $K(t)$ 上独立。导子 $\delta$ 保持每个 $j$ 分量，其系数与 $\mathscr R$ 无关，所以核条件可以分别对每个 $(n,j)$ 读取。这里没有把 $k(\mathscr R)$ 当作 $k$，也没有将不同 $j$ 的 Kummer 分量相混。

## 2. 固定除子没有遗漏的碰撞

在上述好特征，五个多项式
$$
t,\quad t-1,\quad h_7,\quad V,\quad 1+8t
\tag{5}
$$
均平方自由且两两互素。需要的非平凡整数为
$$
\operatorname{disc}(h_7)=-2^4 3^3,
\qquad \operatorname{disc}(V)=2^{52}3^{39},
$$
$$
\operatorname{Res}(h_7,t)=7,\quad
\operatorname{Res}(h_7,t-1)=3^3,
$$
$$
\operatorname{Res}(V,t)=1,\quad
\operatorname{Res}(V,t-1)=3^8,\quad
\operatorname{Res}(V,h_7)=2^{22}3^{16},
$$
$$
\operatorname{Res}(1+8t,h_7)=2^4 3^3,\quad
\operatorname{Res}(1+8t,V)=-2^{11}3^8,
$$
而 $1+8t$ 与 $t,t-1$ 的结式分别是 $-1,-9$（采用所列次序）。符号不影响互素性。特别 $V$ 的六个几何零点全都真实存在且互异；在每点旧 $q_n$ 是单位。

这些固定除子正是下面核公式中的全部有限除子。$p>83$ 因而足以保证所有碰撞排除；没有另外随 $p$ 变化的坏点假设。

## 3. 每个分量的完整模 p 核

对整数 $u$，写 $\langle u\rangle_p\in\{0,\ldots,p-1\}$ 为最小非负剩余数。对 $0\le j\le16$，令 $E_j$ 是满足
$$
17E_j\equiv19j\pmod p,\qquad0\le E_j<p
\tag{6}
$$
的唯一整数。定义
$$
r_{n,j}=\langle-A_n-j\rangle_p,\quad
u_{n,j}=\langle-B_n-j\rangle_p,\quad
v_j=\langle-j\rangle_p,
$$
$$
z_{n,j}=\langle C_n+E_j\rangle_p,
$$
$$
\boxed{
P_{n,j}^{(p)}(t)
=t^{r_{n,j}}(t-1)^{u_{n,j}}h_7(t)^{r_{n,j}}
 V(t)^{v_j}(1+8t)^{z_{n,j}},
}
\tag{7}
$$
$$
\mu_{n,j}=\deg P_{n,j}^{(p)}
=3r_{n,j}+u_{n,j}+6v_j+z_{n,j}.
\tag{8}
$$

**定理 1（准确核）。** 在分量 $\mathscr R^nq_nk[t]_{\le e_{n+1}}T^j$ 上，$\bar{\mathcal Q}_3$ 的核准确为
$$
\boxed{
\mathscr R^nq_nT^j P_{n,j}^{(p)}(t)
\left\{Q(t^p):Q\in k[t],\quad
 p\deg Q+\mu_{n,j}\le e_{n+1}\right\}.
}
\tag{9}
$$
故整个模 $p$ 核的维数准确为
$$
\boxed{
\sum_{n=0}^{D}\sum_{j=0}^{J}
\max\left\{0,\ 1+\left\lfloor
\frac{e_{n+1}-\mu_{n,j}}p\right\rfloor\right\}.
}
\tag{10}
$$

**证明。** $W_3$ 在函数域中非零，因此可先计算 $\delta$ 的核。将 (1) 求对数导数，得到
$$
\frac{\partial_tT}{T}
=\frac{\partial_t(aV)}{aV}
-\frac{19}{17}\frac8{1+8t}.
\tag{11}
$$
这里 $\mathscr R$ 确实固定。对非零 $P\in k[t]$，$\delta(q_nPT^j)=0$ 等价于
$$
\frac{P'}P
=-(A_n+j)\left(\frac1t+\frac{h_7'}{h_7}\right)
 -\frac{B_n+j}{t-1}-j\frac{V'}V
 +\left(C_n+\frac{19j}{17}\right)\frac8{1+8t}.
\tag{12}
$$
(7) 的对数导数就是 (12)，因为各指数具有准确的模 $p$ 剩余值。因此
$$
\delta(q_nPT^j)=0
\iff\partial_t\left(P/P_{n,j}^{(p)}\right)=0
\iff P/P_{n,j}^{(p)}\in k(t^p).
\tag{13}
$$
最后一等价可直接证明：$1,t,\ldots,t^{p-1}$ 是 $k(t)$ 对 $k(t^p)$ 的基，逐项求导使除常数项外的所有系数为零。完美性也给 $k(t^p)=k(t)^p$。

在 (7) 的每个几何有限点，$P_{n,j}^{(p)}$ 的零阶小于 $p$；(5) 的互素性保证没有把两个指数相加成隐藏的 $p$。若 (13) 中的 $p$ 次幂有有限极，则该极阶至少为 $p$，不能被 (7) 抵消；这与 $P$ 为多项式矛盾。因此商没有有限极，必在 $k[t^p]$。反之每个这样的多项式商都满足 (12)。最后以次数上界截断，即得 (9)。第 1 节的真实独立性给各分量直接和，从而得到 (10)。$\square$

(9) 还给显式核基：在每个允许分量取 $P_{n,j}^{(p)}t^{pm}$，$0\le m\le\lfloor(e_{n+1}-\mu_{n,j})/p\rfloor$。这不是只有维数的估计。

## 4. 全部十七部分只需旧范围 fD<p

**定理 2。** 假定共同范围 $p>83$、$D\ge1$、$0\le J\le16$ 及
$$
\boxed{f_D=\lfloor9D/2\rfloor+4<p.}
\tag{14}
$$
则
$$
\boxed{\ker\bar{\mathcal Q}_3=k\cdot1\oplus k\cdot\mathscr R.}
\tag{15}
$$
特征零的核是相同两列的 $\mathcal O$ 格，且
$$
\boxed{
\mathcal W_{D,J}/\langle1,\mathscr R\rangle
\xrightarrow{\ \mathcal Q_3\ }\mathcal W_{D+3,J}
\quad\text{是像为 }p\text{-饱和的整单射。}
}
\tag{16}
$$

**证明。** 先取 $j=0$。导数核要求 $q_nP\in k(t^p)$。由 (2)，该有理函数在有限处仅可能有 $-1/8$ 的至多 $C_n$ 阶极，在无穷处至多有 $f_n$ 阶极。两界都小于 $p$。非恒定的 $p$ 次幂在某处有极，且极阶被 $p$ 整除，所以 $q_nP$ 必为常数。$n\ge2$ 时 $B_n\ge1$，它在 $t=1$ 的强迫零排除非零常数；而 $q_0=q_1=1$。因此这部分只给 $1,\mathscr R$。

现在取 $1\le j\le16$。因 $j<p$，(7) 中 $v_j=p-j$，所以
$$
\mu_{n,j}\ge6(p-j)\ge6(p-16).
\tag{17}
$$
这也有直接的几何读法：$T^j$ 在 $V$ 的六个零点各有 $j$ 阶零，旧 $q_n$ 在那里为单位；为了使 $q_nPT^j$ 成为导数核，$P$ 在每一点至少补上 $p-j$ 阶零。

另一方面，(14) 给 $D<2(p-4)/9$，且
$$
e_{n+1}=f_n-3A_n-B_n+C_n
\le f_D+C_D
<\frac{10p}{9}.
\tag{18}
$$
在 $p>83$ 下，$6(p-16)>10p/9$。所以 (17) 严格超过所有允许的多项式次数，(9) 中这些分量的核全为零。这证明 (15)。

特征零时，$j\ne0$ 的 (12) 在 $t=-1/8$ 有非整数的对数残数 $C_n+19j/17$。有理函数 $P$ 的对数残数必须是整数，而 $1\le j\le16$ 使 $17\nmid19j$，故该分量没有非零核。$j=0$ 的核仍由上述常数与强迫零计算给出 $1,\mathscr R$。

源、目标是 (3) 的有限自由整模，$1,\mathscr R$ 是其中实际整基的两列。由 R406 的闭合公式，$\mathcal Q_3$ 是一个整矩阵。特征零与模 $p$ 秩现在相同，故其每个非零 Smith 因子都是单位；相应余核没有 $p$ 扭结。这正是 (16) 的饱和性。$\square$

例如纯代数参数 $p=101,D=21,J=16$ 满足 $f_D=98<101$；旧的 $17f_D+151J<p$ 条件在这里完全不适用。此例只说明两饱和范围的差别，不作为主课题的数值证据。

## 5. 全部D的准确饱和判据及与原中央的界面

不用 (14) 时，特征零核依然只有上述两列。因此 (10) 等于二，当且仅当 (16) 的整像为 $p$-饱和。更一般，(10) 减二等于非零 Smith 因子中被 $p$ 整除的个数；它不记录各因子的更高赋值。此处的等价是一个完整的有限来源判据，无须再用粗略的 Laurent 指数长度作估计。

本篇扩大的是 R406 真正来源操作 (4) 的使用范围。该文的完整连接、一次物理行移、$\zeta$ 原像成员性、同一个 $P_2,\lambda_2$ 的双接触及其两种 Gaussian charge 均保持原样。特别，全 $P_{134}/U_0$、十三行和首次提升像没有改变。

但 (16) **不推出** $M$ 的物理评价像为 $p$-饱和：评价会把独立变量 $\mathscr R,t$ 限制到同一个 theta 形式轨道，且带真实除幂权。也不推出 R406 的接触对 $(q,r)$ 遍历环境直和。两条完整中央条件仍须保留 R403 的两个基准及全部 wrap。下一项实际比较应在放宽后的完整来源上进行，不能用本篇的来源单射替代它。

## 可复算依据

[check-r408-two-source-frobenius-kernel.py](../scripts/check-r408-two-source-frobenius-kernel.py) 只核固定多项式的判别式/结式、核指数的对数残数以及一个展示饱和范围的参数。全体参数的证明是上面的除子与函数域论证，不依赖扫描目标素数。

依赖：[R403](R403-two-original-rank-two-sources-joint-carry-and-second-top-row.md) 的两个真实来源；[R406](R406-two-source-degree-three-connection-and-coupled-contact-pullback.md) 的原次数三整闭合与完整物理接口；[R335](R335-full-integral-canonical-conductor-and-exact-relative-source.md) 的整格内容以 R352/R406 明列的 (2)–(3) 使用。没有引用一个尚未证明的跨素数非消失命题。
