# R60：惰性新增素数的 Selmer 矩阵、Kummer 剩余符号与联合控制域

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的算术结构定理；主目标仍未解决。** 在 R50 的固定 CM 参考曲线
$A:y^2=x^3-x$ 上，本文将实际 Selmer 交替矩阵的惰性素数部分写成
$T=\mathbb Q(A[p])$ 内的 $p$ 次剩余符号。单素数松弛类具有唯一归一化；
它们定义的扩张在 $T$ 上联合线性不交，并给出新增矩阵条目的精确零／非零密度。
这些陈述也适用于没有给定实际非 CM 曲线的修改 Selmer 条件；它们不能倒推出这种曲线存在。

## 1. 假设、两种“分裂”与全局像

固定
$$
p>37,\qquad p\equiv3\pmod4,\qquad
V=A[p],\qquad T=\mathbb Q(A[p]),\qquad
G=\operatorname{Gal}(T/\mathbb Q).
$$
R50 已无条件证明
$$\operatorname{Sel}_p(A/\mathbb Q)=0. \tag{60.1}$$
令
$$
\mathcal P_p=\{q\text{ 为素数}:q\equiv-1\pmod{4p}\}.
\tag{60.2}
$$
其中每个 $q$ 都在 CM 域 $K=\mathbb Q(i)$ 中**惰性**，并且
$q\equiv-1\bmod p$。如果 $q$ 同时属于一条实际同余曲线 $E$ 的新增
**分裂乘法**素数集，它在 R50 中改变局部条件。后一“分裂”描述
$E/\mathbb Q_q$ 的约化类型，与前一“惰性”没有矛盾。

CM 作用将 $G$ 嵌入非分裂 Cartan 的正规化子
$$
N=\mathbb F_{p^2}^{\times}\rtimes\langle w\rangle,\qquad
w(x)=x^p.
$$
它到 $N/\mathbb F_{p^2}^{\times}$ 的商特征正是 $K/\mathbb Q$。
这里实际有
$$
G=N,\qquad |G|=2(p^2-1).
\tag{60.3}
$$
理由是 $A$ 在惰性 $p$ 处好超奇异，其形式群在 $K_p$ 上是高度二的
Lubin–Tate 群，$p$ 处惯性在 $V$ 上给出整个
$\mathbb F_{p^2}^{\times}$；复共轭给外陪集。这个局部满像事实也由
Pollack–Rubin (2004), §1，印刷页 450 明确给出。特别地 $p\nmid|G|$。

将 $V$ 视为 $\mathbb F_{p^2}$ 的加法群，Cartan 的乘法作用说明它作为
$\mathbb F_p[G]$ 模不可约。进一步，
$$
\operatorname{End}_{\mathbb F_p[G]}(V)=\mathbb F_p:
\tag{60.4}
$$
与 Cartan 交换的线性映射恰为乘以 $\mathbb F_{p^2}$ 元素，而再与
$w$ 交换将该元素限制为 $\mathbb F_p$。后面证明联合线性不交时会使用
(60.3)、(60.4)，并非仅比较分歧素数。

## 2. 每个惰性素数的两条规范局部直线

对每个 $q\in\mathcal P_p$，固定一个分解群、一个算术 Frobenius 提升
$F_q$，并记
$$
g_q=\bar\rho_{A,p}(F_q),\qquad
V_q^\pm=\ker(g_q\mp1),\qquad
\pi_q^+=(1+g_q)/2.
$$
$A$ 在 $q$ 好约化且 CM 惰性迹为零，故
$$
\operatorname{tr}(g_q)=0,\quad
\det(g_q)=q=-1\in\mathbb F_p,\quad g_q^2=1.
$$
两个特征空间 $V_q^\pm$ 都是一维。

R17 的局部上同调计算给出规范直和
$$
H^1(\mathbb Q_q,V)
=\mathfrak a_q\oplus\mathfrak e_q,\qquad
\mathfrak a_q=H^1(\mathbb Q_q,V_q^+)
=H^1_{\rm ur}(\mathbb Q_q,V),\quad
\mathfrak e_q=H^1(\mathbb Q_q,V_q^-).
\tag{60.5}
$$
两条直线各一维，$\mathfrak e_q$ 没有非零不分歧类。
它们对 Weil 配对诱导的**对称**局部 Tate 形式 $B_q$ 各向同性，
且彼此非退化配对。选择基
$$
a_q\in\mathfrak a_q,\qquad e_q\in\mathfrak e_q,\qquad
B_q(a_q,e_q)=1.
\tag{60.6}
$$
对不分歧类，Frobenius 取值先落在 $V/(g_q-1)V$；通过
$\pi_q^+$ 规范识别为 $V_q^+$。记 $a_q$ 的该取值为
$$t_q\in V_q^+\setminus\{0\}. \tag{60.7}$$

如果实际有 $E[p]\simeq A[p]$，且 $E$ 在 $q$ 分裂乘法，
R13、R17 给 Tate 参数为 $p$ 次幂，并给
$$
L_q^A=\mathfrak a_q,\qquad L_q^E=\mathfrak e_q.
\tag{60.8}
$$
若在该处是**非分裂乘法**，则 $L_q^E=\mathfrak a_q$，不应把它放入
本矩阵的改变条件素数集。反过来，实际新增乘法素数若在 $K$ 惰性，
其 Frobenius 迹与 Tate 描述强迫 $q\equiv-1\bmod p$，故它确实属于
$\mathcal P_p$。

## 3. 唯一的单素数松弛类与矩阵

记 $L_v^A$ 为通常的 Kummer 局部条件。对 $q\in\mathcal P_p$ 定义
$$
R_{\{q\}}=
\{c\in H^1(\mathbb Q,V):
\operatorname{loc}_v(c)\in L_v^A\quad(v\ne q)\}.
$$
在 $q$ 处不附加限制。R50 的 Poitou–Tate 条件比较，结合 (60.1)，给
$$
R_{\{q\}}\xrightarrow{\sim}
H^1(\mathbb Q_q,V)/\mathfrak a_q.
\tag{60.9}
$$
因此有唯一的类 $c_q$，其右边坐标是 $e_q$。

这个类在 $q$ 的完整局部化其实为
$$\boxed{\operatorname{loc}_q(c_q)=e_q.} \tag{60.10}$$
确实，先写成 $x a_q+e_q$。在其余位置，$c_q$ 落在各向同性
Kummer 条件中；全局 Brauer 互反于是给
$$
0=\sum_v B_v(\operatorname{loc}_v c_q,\operatorname{loc}_v c_q)
=B_q(xa_q+e_q,xa_q+e_q)=2x.
$$
因 $p$ 奇，$x=0$。所以这不是“选一个具有某局部分歧的类”的非唯一过程；
归一化 (60.6) 一旦固定，$c_q$ 就唯一。

现在取互异素数
$$S=\{q_1,\ldots,q_s\}\subset\mathcal P_p,\qquad c_i=c_{q_i}.$$
在全部 $S$ 处松弛，得到 $R_S$。同一比较式给
$$
R_S\xrightarrow{\sim}
\bigoplus_{i=1}^s H^1(\mathbb Q_{q_i},V)/\mathfrak a_{q_i}.
\tag{60.11}
$$
单素数类 $c_i$ 都属于 $R_S$，且映为标准基，因而它们就是
$R_S$ 的一组基。定义
$$
\operatorname{loc}_{q_j}(c_i)=m_{ji}a_{q_j}\quad(i\ne j),
\qquad m_{ii}=0.
\tag{60.12}
$$
两类的全局互反给
$$m_{ji}+m_{ij}=0. \tag{60.13}$$
例如，只有 $q_i,q_j$ 两个位置可能贡献配对，分别为
$m_{ij}$ 和 $m_{ji}$。因此
$$M_S=(m_{ji})\quad\text{是交替矩阵}. \tag{60.14}$$

令 $\operatorname{Sel}^{\,S}(V)$ 表示在 $S$ 处用
$\mathfrak e_q$、其余位置用 $L_v^A$ 的修改 Selmer 群。由 (60.11)、
(60.12)，
$$
\boxed{\operatorname{Sel}^{\,S}(V)
=\left\{\sum_i x_i c_i:M_Sx=0\right\}
\simeq\ker M_S.}
\tag{60.15}
$$

若实际 $E$ 的所有新增分裂乘法素数恰为 $S$，则这就是
R50 的 $M_E$ 和实际 $\operatorname{Sel}_p(E)$。
若实际改变条件的素数集中还含有在 $K$ 分裂的素数，本构造给出
$M_E$ 的惰性素数主子块：单素数类在其余位置都落在 $L_v^A$，
所以仍是 R50 归一化基中相应的列。本文没有将 $q\equiv1\bmod p$
处可能四维的完整局部上同调错当成 (60.5)。

## 4. 非对角项的 Frobenius 公式及其不变性

为 $c_i$ 取任意连续 cocycle 代表
$$z_i:G_{\mathbb Q}\longrightarrow V.$$
当 $i\ne j$ 时，$V$ 在 $q_j$ 不分歧，且 $c_i$ 的局部类不分歧，
于是
$$
\boxed{m_{ji}\,t_{q_j}
=\pi_{q_j}^+z_i(F_{q_j}).}
\tag{60.16}
$$
这是不分歧上同调的 Frobenius 取值描述。

必须检查它不依赖随意的代表：

- 换成 cohomologous cocycle 会使右侧未投影的值增加
  $(g_{q_j}-1)v$；$\pi_{q_j}^+(g_{q_j}-1)=0$。
- 因 $V$ 在 $q_j$ 不分歧，coboundary 在惯性上恒为零。
  一个不分歧局部类的每个 cocycle 代表因而都在惯性上为零。
  改变同一个分解群中的 Frobenius 提升，不改变 (60.16)。
- 改变分解群是共轭变换，相应同时搬运 $g_{q_j}$、特征线、
  $a_{q_j},e_{q_j},t_{q_j}$。它不会改变矩阵所表示的 Selmer 条件。
  改变 (60.6) 的双基只作相应的行列归一化；零／非零及核维数不变。

这也解释了为何不能直接把任意 $z_i(F_{q_j})$ 的某个坐标叫作
矩阵条目，而忽略投影及基的选择。

## 5. 单素数扩张及联合线性不交

### 5.1 定义扩张并证明其完整 Galois 群

在 $G_T$ 上 $V$ 的作用平凡，所以限制
$$h_i=z_i|_{G_T}:G_T\longrightarrow V$$
是同态；coboundary 在此恒为零，故它只依赖上同调类 $c_i$。
令 $N_i$ 为 $h_i$ 核的固定域。对 $\sigma\in G_{\mathbb Q}$、
$\tau\in G_T$，cocycle 关系给
$$h_i(\sigma\tau\sigma^{-1})=\bar\rho_{A,p}(\sigma)h_i(\tau). \tag{60.17}$$
因此 $N_i/\mathbb Q$ 正规，而 $h_i$ 的像是 $G$ 子模。

在 $q_i$，$T/\mathbb Q$ 不分歧，惯性群包含在 $G_T$ 中。
由 (60.10) 及 (60.5)，$h_i$ 在该惯性群上的像是一条非零直线。
不可约性遂给
$$
h_i(G_T)=V,\qquad
\operatorname{Gal}(N_i/T)\simeq V,\qquad [N_i:T]=p^2.
\tag{60.18}
$$
映射
$$
\sigma\longmapsto(z_i(\sigma),\bar\rho_{A,p}(\sigma))
$$
的像是 $V\rtimes G$ 的子群，并同时包含整个核 $V$、满射到 $G$。
所以
$$\operatorname{Gal}(N_i/\mathbb Q)\simeq V\rtimes G. \tag{60.19}$$
$N_i$ 不依赖 cocycle 代表；将 $e_{q_i}$ 乘以非零标量也不改变这个域。

对任意有理素数 $\ell\notin\{2,p,q_i\}$，
$c_i$ 与 $V$ 在 $\ell$ 都不分歧，故 $N_i/\mathbb Q$ 在 $\ell$ 不分歧。
特别地，对 $j\ne i$，$h_i$ 在 $q_j$ 的惯性上为零。
在 $2$ 处 $L_2^A=0$，还可知 $N_i/T$ 在每个二进分解群上平凡；
后面的独立性只需要前述 $q_j$ 惯性信息。

### 5.2 联合线性不交的完整证明

令
$$
N_S=N_1\cdots N_s,\qquad
H=\operatorname{Gal}(N_S/T)
\subset V^s,
$$
其中嵌入由 $(h_1,\ldots,h_s)$ 给出。它是对角 $G$ 作用下的子模，
并且满射到每个因子。

假设 $H\ne V^s$。因为 $p\nmid|G|$，Maschke 定理使
$\mathbb F_p[G]$ 模半单；$V^s/H$ 是非零的 $V$ 等型模。
因此存在非零的 $G$ 线性映射
$$
\ell:V^s\longrightarrow V,\qquad \ell(H)=0.
$$
由 (60.4)，它必形如
$$
\ell(v_1,\ldots,v_s)=\sum_i b_i v_i,\qquad b_i\in\mathbb F_p,
$$
且至少一个 $b_i$ 非零。

限制到 $q_j$ 惯性群。所有 $h_i$、$i\ne j$ 在此为零，而
$h_j$ 有非零像；所以 $\ell\circ(h_1,\ldots,h_s)=0$ 强迫 $b_j=0$。
对全部 $j$ 应用，矛盾。故
$$
\boxed{\operatorname{Gal}(N_S/T)=V^s,\qquad
[N_S:T]=p^{2s},\qquad
\operatorname{Gal}(N_S/\mathbb Q)=V^s\rtimes G.}
\tag{60.20}
$$
最后一式也可直接由所有 cocycle 组成的映射证明，和 (60.19) 相同。

因此这些域在 $T$ 上**联合**线性不交。仅说每个域在不同的
$q_i$ 分歧并不足以得到这个结论；(60.17)、全 $G$ 作用下的不可约性、
(60.4) 以及唯一非零惯性一起排除了所有多因子关系。

## 6. 除法域中的精确 $p$ 次剩余符号

### 6.1 Kummer 根式

Weil 配对给 $\mu_p\subset T$。固定 $V$ 的基 $P_1,P_2$ 及
一个本原根 $\zeta_p$。Kummer 理论给出
$a_{i1},a_{i2}\in T^\times/T^{\times p}$，满足
$$
h_i(\sigma)=
\chi_{a_{i1}}(\sigma)P_1+
\chi_{a_{i2}}(\sigma)P_2,\qquad \sigma\in G_T,
\tag{60.21}
$$
其中
$$
\frac{\sigma(\sqrt[p]{a})}{\sqrt[p]{a}}
=\zeta_p^{\,\chi_a(\sigma)}.
$$
这是通常的 Kummer 正合列与 Hilbert 90；(60.18) 还说明两个根式类
线性无关，并且
$$N_i=T(\sqrt[p]{a_{i1}},\sqrt[p]{a_{i2}}). \tag{60.22}$$
所选 $P_1,P_2,\zeta_p$ 固定了坐标；(60.21) 没有省去
$G$ 对根式数据的圆分扭曲作用。

### 6.2 先把赋值化为零

取 $j\ne i$，并取 $T$ 中位于 $q_j$ 上、与已固定分解群相符的素理想
$\lambda_j$。由于 $g_{q_j}$ 的阶为二，
$$f(\lambda_j/q_j)=2,\qquad \#k_{\lambda_j}=q_j^2. \tag{60.23}$$
$N_i/T$ 在 $\lambda_j$ 不分歧。每个 Kummer 根式代表因此满足
$$v_{\lambda_j}(a_{ir})=p\,d_{ir}\quad(d_{ir}\in\mathbb Z).$$
在局部域 $T_{\lambda_j}$ 取统一化元 $\varpi_{\lambda_j}$，置
$$
b_{ir}=a_{ir}\varpi_{\lambda_j}^{-p d_{ir}}\in
\mathcal O_{T_{\lambda_j}}^\times.
\tag{60.24}
$$
(60.24) 只改变一个局部 $p$ 次幂，故不改变 Kummer 特征。
不能直接对可能有零点或极点的 $a_{ir}$ 取有限域剩余符号。

定义 $r_{ir}(\lambda_j)\in\mathbb F_p$ 为
$$
\overline{\zeta_p}^{\,r_{ir}(\lambda_j)}
=\overline{b_{ir}}^{\,(q_j^2-1)/p}
\quad\text{于 }k_{\lambda_j}^{\times}.
\tag{60.25}
$$
$p\mid(q_j^2-1)$，且 $\mu_p$ 在该剩余特征不为 $p$ 的地方约化单射，
所以此定义唯一。换统一化元，或把原根式代表乘以 $p$ 次幂，
只使 $b_{ir}$ 的剩余类乘以一个 $p$ 次幂；(60.25) 不变。

按算术 Frobenius 约定，局部 Kummer 公式正是
$$
\chi_{a_{ir}}(\operatorname{Frob}_{\lambda_j})
=r_{ir}(\lambda_j).
\tag{60.26}
$$
可直接验证：对单位根式取根 $\alpha$，Frobenius 在剩余域上作用为
$q_j^2$ 次幂，所以
$\operatorname{Frob}(\alpha)/\alpha$ 的剩余值为
$\overline b^{(q_j^2-1)/p}$。

### 6.3 平方 Frobenius 给出的因子二

$F_{q_j}^2\in G_T$，并在 $\lambda_j$ 给出算术 Frobenius。
由 cocycle 关系及 (60.16)，
$$
\begin{aligned}
h_i(\operatorname{Frob}_{\lambda_j})
&=z_i(F_{q_j}^2)\\
&=(1+g_{q_j})z_i(F_{q_j})\\
&=2\,m_{ji}t_{q_j}.
\end{aligned}
\tag{60.27}
$$
结合 (60.21)、(60.25)，得到所求精确公式
$$
\boxed{
2\,m_{ji}t_{q_j}
=r_{i1}(\lambda_j)P_1+r_{i2}(\lambda_j)P_2.}
\tag{60.28}
$$
右边自动属于 $V_{q_j}^+$，这是由构造给出的兼容性检查。
去掉因子二会改变归一化条目。两个剩余符号都为零，当且仅当
$m_{ji}=0$；等价地，$\lambda_j$ 在 $N_i/T$ 中完全分裂。

## 7. 固定输入下的有限 Kummer 计算接口

(60.28) 并非断言两个根式已在本轮求出。它同时给出一个不依赖
猜测基本单位或假定类群 $p$ 部分为零的精确有限计算问题。

令 $\Sigma_i$ 为 $T$ 中位于 $2,p,q_i$ 上的所有素理想，并定义
$$
U_i=
\{a\in T^\times/T^{\times p}:
v_\lambda(a)\equiv0\pmod p\quad(\lambda\notin\Sigma_i)\}.
$$
有有限维 $\mathbb F_p$ 空间的正合列
$$
0\longrightarrow
\mathcal O_{T,\Sigma_i}^{\times}/
\mathcal O_{T,\Sigma_i}^{\times p}
\longrightarrow U_i
\longrightarrow
\operatorname{Cl}(\mathcal O_{T,\Sigma_i})[p]
\longrightarrow0.
\tag{60.29}
$$
具体地，$(a)=\mathfrak b^p$ 在 $\Sigma_i$ 外成立，映射取
$[\mathfrak b]$；核就是 $\Sigma_i$ 单位模 $p$ 次幂，而每个
$p$ 挠理想类由一个主化生成元给出原像。因此既要计算单位，也要保留
可能的理想类项。

令
$$W=\operatorname{Hom}_{\mathbb F_p}(\mu_p,V)=V(-1).$$
Kummer 同构与 $G$ 作用相容地给
$$
H^1(T,V)\simeq
(T^\times/T^{\times p})\otimes_{\mathbb F_p}W.
\tag{60.30}
$$
由于 $p\nmid|G|$，$H^1(G,V)=H^2(G,V)=0$；inflation–restriction
遂给
$$
H^1(\mathbb Q,V)\xrightarrow{\sim}H^1(T,V)^G.
\tag{60.31}
$$
在给定的不分歧范围内，只须取 $(U_i\otimes W)^G$。
$W$ 中的 $(-1)$ 扭曲记录了圆分特征；不能把根式数据简单当作
没有扭曲的两份 $G$ 不变单位。

因此对固定 $p,q_i$，完整流程是：

1. 用 (60.29) 求 $U_i$ 及其 $G$ 作用，取
   $(U_i\otimes W)^G$。
2. 经 (60.31) 的下降，在 $2,p$ 施加通常的 $A$ Kummer 条件，
   在 $q_i$ 施加 (60.10) 的归一化条件。其余好素数处的通常条件就是
   已要求的不分歧条件；实位置因 $p$ 奇没有额外条件。
3. 这是有限的线性条件。由 (60.9)、(60.10)，恰有一个解。
   将其在固定基 $P_1,P_2,\zeta_p$ 下写出，得到 (60.21) 的两个根式类。
4. 对目标 $q_j$ 先作 (60.24)，再在有限域中计算 (60.25)，由
   (60.28) 恢复 $m_{ji}$。

上述流程保留所有局部条件和下降条件；不能只挑两个看似合适的单位，
计算剩余符号后便把结果称为 $M_S$。数域单位、理想类和局部 Kummer
像都有固定输入下的有限计算方法，但这里的数域次数是
$2(p^2-1)$，本轮没有实际计算 $T$ 的这些数据或给出任何具体的
$m_{ji}$ 数值。这个固定参数流程也不产生对变化 $p$ 的统一界。

## 8. 新增素数处零／非零模式的精确密度

固定上述 $S$，现在令新的 $q\in\mathcal P_p\setminus S$ 变化。
用相同的单素数归一化定义扩大矩阵中的 $m_{q,i}$。
对 $I\subset\{1,\ldots,s\}$，考虑条件
$$
m_{q,i}=0\ \Longleftrightarrow\ i\in I.
\tag{60.32}
$$
这是“指定的条目恰好为零，其余均非零”，不固定非零数值的归一化。

**密度结论。** 满足 (60.32) 的素数，在 $\mathcal P_p$ 中的相对
自然密度与相对 Dirichlet 密度均为
$$
\boxed{p^{-|I|}(1-1/p)^{s-|I|}.}
\tag{60.33}
$$
尤其所有新增条目为零的相对密度为 $p^{-s}$。

这里的量词是先固定 $p$、旧素数集 $S$ 及 $N_S$，再让新增 $q$ 趋于无穷。
下文逐对选素数只用这种固定前缀的正密度来证明存在性；没有断言所有
$s$ 元素素数集同时落在一个大小为 $X$ 的盒子时具有某个联合秩分布，
那还需要对变化控制域的统一 Chebotarev 估计。

### 8.1 底层 Frobenius 共轭类

写 $C=\mathbb F_{p^2}^{\times}$。外陪集元素 $g=a w$ 满足
$$
g^2=N_{\mathbb F_{p^2}/\mathbb F_p}(a),\qquad
\det(g)=-N_{\mathbb F_{p^2}/\mathbb F_p}(a).
$$
故对应 $\mathcal P_p$ 的元素恰为
$$
\mathcal C_0=\{a w:N(a)=1\}.
$$
它们形成 $G$ 中一个共轭类：用 $b\in C$ 共轭把 $a$ 乘以
$b^{1-p}$，而这些元素遍历范数一子群。于是
$$
|\mathcal C_0|=p+1,\qquad
\frac{|\mathcal C_0|}{|G|}=\frac1{2(p-1)}.
\tag{60.34}
$$
这里用到 $G/C$ 为 CM 二次特征以及行列式为圆分特征，所以这个
Frobenius 条件准确等价于 $q\equiv-1\bmod4p$。

### 8.2 联合控制域中的计数

由 (60.20)，在每个固定 $g\in\mathcal C_0$ 上方，控制域的元素为
$$
(v_1,\ldots,v_s,g),\qquad v_i\in V,
$$
其中所有坐标可以独立变化。(60.16) 将 $m_{q,i}=0$ 识别为
$$\pi_g^+(v_i)=0,\qquad \pi_g^+=(1+g)/2.$$
每个 $\pi_g^+$ 秩一，所以其核有 $p$ 个元素，非零投影有
$p^2-p$ 个原像。

这些条件在整个 $V^s\rtimes G$ 中共轭不变。具体地，用
$(w_1,\ldots,w_s,h)$ 共轭，$g$ 变为 $g'=hgh^{-1}$，而第 $i$
个向量变为
$$
h v_i+(1-g')w_i.
$$
投影后恰为 $h\pi_g^+(v_i)$，故是否为零不变。
因此可以对这组共轭类直接应用 Chebotarev 定理。

在给定 $g$ 上满足 (60.32) 的比例为
$$
\left(\frac p{p^2}\right)^{|I|}
\left(\frac{p^2-p}{p^2}\right)^{s-|I|},
$$
结合 (60.34) 并除以底层 $\mathcal P_p$ 的密度，证明 (60.33)。
有限个已分歧素数和 $S$ 内的素数不影响密度。

### 8.3 对真正全局上同调的一个后果

对任意整数 $s\ge0$，以及
$$0\le d\le s,\qquad d\equiv s\pmod2,$$
存在由 $\mathcal P_p$ 中 $s$ 个素数组成的集合 $S$，使
$$\dim_{\mathbb F_p}\operatorname{Sel}^{\,S}(V)=d. \tag{60.35}$$
这是关于同一个实际 $G_{\mathbb Q}$ 模 $A[p]$ 的全局上同调的陈述。

证明可逐对选择素数。欲增加一个非退化二阶块，先选新素数使它与
所有旧素数的条目为零，再选另一个新素数使它与旧素数的条目全零、
只与刚选的素数条目非零。每一步由 (60.33) 有正密度，互反性自动给
对应的反对称条目。重复 $(s-d)/2$ 次，再添 $d$ 个与此前全部条目
为零的素数，即得到相应块矩阵和 (60.35)。

所以 R50 的各个奇偶允许维数确实能由这样的**修改 Selmer 条件**
实现，超出了纯粹任意矩阵的线性代数例子。
但本构造没有给出 R19 的整数三元组，也没有使整组修改条件成为
某条实际非 CM 同余曲线的全部 Kummer 条件。
(60.33)、(60.35) 均不构成 Serre 一致性反例；实际 $E$ 的存在性
仍是另一项必要约束。

## 9. CM 椭圆单位能否直接给出所需根式

CM 理论使 $T/K$ 阿贝尔，因此椭圆单位与显式互反是构造
(60.21) 的自然候选工具。不过必须区分已有定理的实际输出。

Pollack–Rubin (2004), §5、Theorem 5.1 的显式互反把适当
CM 分量中的椭圆单位，与 $p$ 处 Kummer 配对及 Hecke $L$ 值联系起来。
它没有直接给出本文每一个远离 $p$ 的 $q_i$ 所对应的唯一单素数
松弛类。若使用椭圆单位的导数构造，仍须证明所得数据：

1. 属于 (60.30) 的正确 CM 特征分量和圆分扭曲；
2. 在复共轭作用下满足下降到 $\mathbb Q$ 的条件；
3. 在 $2,p$ 满足通常的 $A$ Kummer 条件，在其他素数不新增分歧；
4. 在 $q_i$ 的分歧分量非零，并且能按 (60.6) 归一化为 $e_{q_i}$。

满足这些条件以后，唯一性才允许把所得类认作 $c_i$，再使用
(60.28)。本轮没有完成这样的椭圆单位构造，也没有算出替代流程
(60.29) 所需的全部单位和理想类数据。这里 $p$ 为超奇异素数，
不能省去假设而移植 ordinary 情形的互反公式。

本文的新输入是完整的单素数归一化、Frobenius/Kummer 公式、
联合控制域和密度证明。它没有将实际曲线的 $p$-Selmer 群与
R46 辅助 $j=0$ 曲线的三同源 Selmer 群联系起来，也没有获得
R53 原始高指数方程的全局解或排除。

## 10. 来源和依赖

- [R17：新乘法素数的精确 Selmer 局部条件](R17-local-selmer-conditions-at-new-primes.md)，特别是
  §3 的温和惯性计算与 §5 的 $q\equiv-1\bmod p$ 两条直线。
- [R50：实际固定 CM 同余的 Selmer 群与交替矩阵](R50-actual-selmer-alternating-matrix.md)，
  §1 的 $\operatorname{Sel}_p(A)=0$ 及 §§2–4 的 Poitou–Tate 条件比较。
  本文将单素数情形和矩阵条目另行展开。
- R. Pollack and K. Rubin, **The main conjecture for CM elliptic curves at supersingular primes**,
  Annals of Mathematics **159** (2004), 447–464。
  §1（印刷页 450）的 CM 超奇异惯性满像；§5、Theorem 5.1 的显式互反适用范围。
  [期刊页](https://annals.math.princeton.edu/2004/159-1/p11)，
  [已发表全文存档](https://arxiv.org/pdf/math/0509604)。
- J. S. Milne, **Fields and Galois Theory**，2022 版，
  §5、Theorem 5.30：Kummer 对应及 Hilbert 90 的证明。
  [作者提供的同版全文](https://www.jmilne.org/math/CourseNotes/FT.pdf)。
  本文 (60.24)–(60.28) 另推导所需局部符号归一化。
- 经典 Chebotarev 密度定理；本次核对的明确自然密度陈述见
  J. S. Milne, **Algebraic Number Theory**, v3.08，
  Theorem 8.31，[作者全文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)。
  本文 §8 独立完成所需共轭不变性与有限群计数，不引用任何随机 Selmer 模型。


