# R271：保留 $p$ 类群标签的原 theta 二阶项、真分歧商与全 Selmer 两步判据

日期：2026-11-13。**状态：本篇全部比较和充分条件已证明；实际二阶项的跨 $p$ 非零尚未证明。**

固定目标仍为
$$
 E:y^2+y=x^3+x^2-2x,\qquad N_E=389,\qquad
 \operatorname{rank}E(\mathbb Q)\ge2.
\tag{1}
$$
本篇允许辅助虚二次域 $F$ 随 $p$ 变化，也允许 $p\mid h_F$。
原完整 Heegner 点、原 $\ell$、全部类群和均保留。新增的内容有两项：

1. R146 的有限 conductor 两步判据不需要 $p\nmid h_F$。
   应替换为：**确实选择一个在原 $\ell$ 分歧的次数 $p$ 商**。
   本篇直接补全有限类群下降；不调用要求类数与 $p$ 互素的
   $\mathbb Z_p$ 塔定理。
2. 原 definite theta 元素在所有这些真实分歧商上的三维幺幂观察，
   对全 $p$ 类群群环的二阶增广商联合忠实。给出有限恢复矩阵、
   其 $2$ 幂行列式和类群 norm 的准确增广位移；没有半单 Fourier 投影。

这使“变化辅助域和次数 $p$ 商”成为一个准确的正向接口：若一个
实际全 theta 元素的总二阶项非零，就有一个实际完整类群迹满足
原两步条件，推出固定 $E$ 的 $\Sha[p^\infty]=0$。
没有把 theta 本征函数本原或某个高增广项非零当作该总二阶项非零。

## 1. 输入、真分歧商和完整 theta 元素

取 $p\ge7$，$E$ 在 $p$ 好普通且
$a_p(E)\not\equiv\pm1\pmod p$。取虚二次域 $F$，要求
$\mathcal O_F^\times=\{\pm1\}$、$389$ 分裂于 $F$、
$p\nmid389\operatorname{disc}F$，且 $G_F$ 在 $T_pE$ 上满像。
取原好约化素数 $\ell$，要求
$$
 \ell\text{ 在 }F\text{ 惰性},\qquad
 \ell+1=pu,\qquad p\nmid u a_\ell(E).
\tag{2}
$$
这些条件可用于 R149/R153 的同一原 $(p,\ell)$；本篇没有另外选
一个只满足固定 $p$ 的 Chebotarev 条件的 $\ell$，也没有证明所有
新增辅助域条件能在原联合无穷集合上同时满足。

记
$$
 H=F[\ell],\qquad \mathcal G=\operatorname{Gal}(H/F),\qquad
 G=\mathcal G_{(p)},\qquad C=\operatorname{Cl}(F)_{(p)}.
$$
有限阿贝尔群按阶的互素部分分解。
环类正合列的 $p$ 部分为
$$
 0\longrightarrow T=\langle t\rangle\simeq C_p
   \longrightarrow G\longrightarrow C\longrightarrow0.
\tag{3}
$$
这里 $T$ 是原 $\ell$ 的惯性群；本篇不预设 (3) 分裂。

令 $\lambda:G\to\mathbb F_p$ 为加法满射，要求
$\lambda(t)=1$。它也给 $\mathcal G\to\mathbb F_p$，在阶与 $p$
互素的部分为零。相应子域记为 $L_\lambda$。准确有
$$
 [L_\lambda:F]=p,\qquad
 L_\lambda/F\text{ 在 }\ell\text{ 全分歧，其他有限位不分歧}.
\tag{4}
$$
只允许 (4) 的商；任一个次数 $p$ 子域可能是 Hilbert 类域的
子域，不能自动用作原范数一扩张。

设 $P[m]$ 是同一模参数化的 Heegner 点。完整基层迹
$P_F=\operatorname{Tr}_{F[1]/F}P[1]$ 为扭点：由 (1) 和
Gross--Zagier--Kolyvagin 有 $L(E,1)=L'(E,1)=0$，故
$L'(E/F,1)=0$；对完整 Hilbert 类群迹用 Gross--Zagier 即得。
满像给 $E(F)[p]=0$，可用与 $p$ 互素的整数 $t_F$ 杀掉 $P_F$。
对每个实际商定义
$$
 Q_\lambda=[t_F]\operatorname{Tr}_{H/L_\lambda}P[\ell],
 \qquad N_{L_\lambda/F}Q_\lambda=0.
\tag{5}
$$
不同 $\lambda$ 的点均来自同一个原 $P[\ell]$，且 (5) 包含
核中的每一个类群标签，特别包含其 $p$ 部分。

取 R234 的一个一般 admissible 观察素数 $q$：
$$
 q\nmid p\ell389\operatorname{disc}F,\quad q\text{ 在 }F\text{ 惰性},
 \quad q^2\not\equiv1\pmod p,\quad
 a_q\equiv\epsilon(q+1)\pmod p,\quad\epsilon\in\{1,-1\}.
\tag{6}
$$
满像保证这样的 $q$；这里不要求事先已知某个负号有理点。
其有限局部线
$W_q=E(\mathbb F_{q^2})/pE(\mathbb F_{q^2})$ 为一维，
有理 Frobenius 作用为 $\epsilon$。

R234 所核的已发表升层和 Zhang (2014), §4.2，给同一个
本征函数 $\varphi_q$ 与单位 $c_q\in\mathbb F_p^\times$，逐原
CM 标签比较 $\varphi_q$ 与原点的约化。此比较没有类数限制：
原 $\ell\equiv-1\pmod p$，所有标签仍在 Zhang 的
$\mathcal C_F^+$ 中，同一度零 Hecke 处理在全部标签上使用。
固定该规范，定义原全元素
$$
 \Theta^{\rm full}_{F,q,\ell}
  =\overline t_F\sum_{g\in\mathcal G}
      \varphi_q(\operatorname{Red}_q x(\ell)^g)\,g^{-1}
       \in k[\mathcal G],\qquad k=\mathbb F_p.
\tag{7}
$$
有理 $q$ 惰性于 $F$ 时，其在 $F$ 的素理想为 $(q)$；在所有
与 $q$ 互素的环类域中该理想为主类。因此 $q$ 在 $H/F$ 完全
分裂，(7) 的全部点都可在同一 $\mathbb F_{q^2}$ 约化。

先仅将阶与 $p$ 互素的标签作**完整求和**，得到
$$
 \Theta_p\in k[G].
\tag{8}
$$
这是群环的 pushforward；不是先除任何类数。若要以幂等元
表示 (8)，只能在阶与 $p$ 互素的部分使用
$e'=|\mathcal G_{(p')}|^{-1}\sum_{h\in\mathcal G_{(p')}}h$；
规范识别 $e'k[\mathcal G]\simeq k[G]$ 后所得恰为 (8)。
绝不在 $C$ 上作这种除法。

令 $\tau$ 为 $\operatorname{Gal}(L_\lambda/F)$ 的生成元，
与 $\lambda(t)=1$ 一致。群环映射
$\pi_\lambda(g)=\tau^{\lambda(g)}$ 给准确恒等式
$$
 \boxed{\quad
 \pi_\lambda(\Theta_p)
   =c_q\,\iota_q\!\left(
       \sum_{j=0}^{p-1}
       \operatorname{red}_{q}(\tau^{-j}Q_\lambda)\tau^j
                     \right).
 \quad}
\tag{9}
$$
右边先对 $\ker\lambda$ 的全部标签求和，正是 (5)。
$c_q$ 对所有 $j$ 和所有 $\lambda$ 相同；因此 (9) 比较的是
同一个实际 theta 元素的一族商，没有标签相关单位。

## 2. 哪些 $p$ 商真的在原 $\ell$ 分歧

**命题 2.1。** 以下条件等价：

- 存在 $\lambda:G\to k$，$\lambda(t)=1$；
- $t\notin pG$；
- (3) 分裂。

写
$$
 C=\bigoplus_{i=1}^r\langle c_i\rangle,
       \qquad |c_i|=p^{e_i},\quad e_i\ge1,
$$
并选任意提升 $g_i\in G$。存在唯一 $b_i\in k$ 使
$$
                 g_i^{p^{e_i}}=t^{b_i}.
\tag{10}
$$
上述等价条件还等价于每个 $b_i=0$。

**证明。** 任一加法角色 $G\to k$ 都杀掉 $pG$。
若 $b_i\ne0$，则 (10) 给 $t\in pG$。
若全部 $b_i=0$，群 $\langle g_1,\ldots,g_r\rangle$ 向 $C$
满射，其给出的定义群阶至多 $|C|$，故恰为一个与 $T$ 交平凡
的补群。于是 $G=T\oplus C$，取 $t\mapsto1,C\mapsto0$。
这也证明所有逆向蕴含。$\square$

(10) 可以用真实理想类算出。取与 $\ell$ 互素的理想
$\mathfrak a_i$ 代表 $c_i$，写
$\mathfrak a_i^{p^{e_i}}=(\alpha_i)$，提升用同一理想的
环类 Artin 元素。采用“局部单位 idèle 映到 Artin 元素”的
约定，则 $t^{b_i}$ 是 $\alpha_i^{-1}\bmod\ell$ 在
$$
 (\mathcal O_F/\ell)^\times/\mathbb F_\ell^\times
$$
中的 $p$ 部分。理由是代表 $\mathfrak a_i^{p^{e_i}}$ 的
idèle 除以主 idèle $\alpha_i$ 后，在 $\ell$ 分量为
$\alpha_i^{-1}$，其他地方的单位被环类 Artin 映射杀掉。
换另一种整体 Artin 正逆约定会同时改变符号，不改变零判据。

具体可将商送入范数一群，$a\mapsto a^{\ell-1}$，再取 $u$
次幂。若所选 $t$ 的对应值的 $u$ 次幂为 $\zeta_\ell$，其阶
为 $p$，则
$$
 b_i=\log_{\zeta_\ell}
       \left(\alpha_i^{-(\ell-1)u}\bmod\ell\right)\in k.
\tag{11}
$$
这只是有限域里的离散对数，保留整个 $p$ 类群的延拓关系。

若命题条件成立，固定一组分裂提升后，全部规范化分歧商恰为
$$
 \lambda_{\mathbf b}(t)=1,\qquad
 \lambda_{\mathbf b}(g_i)=b_i,\qquad
              \mathbf b\in k^r.
\tag{12}
$$
这些是 $p^r$ 个不同的实际次数 $p$ 子域；未规范化时仅多一个
生成元的非零倍数。当 $p\nmid h_F$ 时 $r=0$，(12) 只给原来
唯一的分歧商。

## 3. 三维幺幂 theta 观察的联合忠实性

假设 (3) 分裂，记 $I\subset k[G]$ 为增广理想。
在 $k[G]/I^3$ 中定义
$$
 x_0=(t-1)-\frac12(t-1)^2,\qquad
 x_i=(g_i-1)-\frac12(g_i-1)^2.
\tag{13}
$$
由于 $p>2$，所有群关系的最低次数至少为 $p$，所以
$$
 k[G]/I^3\simeq
 k[x_0,\ldots,x_r]/(\text{总次数}\ge3).
\tag{14}
$$
这是完整的非半单商。任意 $\Theta\in k[G]$ 唯一写成
$$
 \Theta\equiv c+\sum_{i=0}^rL_i x_i
       +\frac12\sum_{i,j=0}^r M_{ij}x_ix_j\pmod{I^3},
           \qquad M_{ij}=M_{ji}.
\tag{15}
$$
若 $\Theta=\sum a_g g$，而 $v_i(g)$ 是 $G/pG$ 的坐标，
则这些**未除群阶**的系数为
$$
 c=\sum_ga_g,\qquad L_i=\sum_ga_gv_i(g),\qquad
 M_{ij}=\sum_ga_gv_i(g)v_j(g).
\tag{16}
$$

令 $R_3=k[T]/T^3$，$x=T-T^2/2$。对 (12)，真实群环商给
$$
 \begin{aligned}
 \pi_{\mathbf b}(\Theta)
    &\equiv c+L(\mathbf b)x+\frac12M(\mathbf b)x^2\pmod{T^3},\\
 L(\mathbf b)&=L_0+\sum_{i=1}^r b_iL_i,\\
 M(\mathbf b)&=M_{00}+2\sum_{i=1}^rb_iM_{0i}
                     +\sum_{i,j=1}^r b_ib_jM_{ij}.
 \end{aligned}
\tag{17}
$$
因此，若实际一、二次 $T$ 系数是 $m_1,m_2$，准确有
$$
              L(\mathbf b)=m_1,\qquad
              M(\mathbf b)=2m_2+m_1.
\tag{18}
$$
不能把二次 binomial 矩直接当作 $M/2$ 而漏掉第一矩。

**定理 3.1。** 在 (3) 分裂时，
$$
 \boxed{\quad
 \bigcap_{\mathbf b\in k^r}
    \ker\bigl(k[G]\xrightarrow{\pi_{\mathbf b}}k[C_p]/(\tau-1)^3\bigr)
                =I^3.
 \quad}
\tag{19}
$$
特别对实际 (8)，$\Theta_p\notin I^3$ 当且仅当至少一个
真实分歧商的完整 theta 三阶截断非零。

**证明及有限恢复式。** 每个映射显然杀掉 $I^3$。
常数由任一商恢复；一次项由
$$
 L_0=L(0),\qquad L_i=L(e_i)-L(0)
\tag{20}
$$
恢复。二次项只需以下 $(r+1)(r+2)/2$ 个实际商：
$$
       0,\quad e_i,-e_i\ (1\le i\le r),\quad
       e_i+e_j\ (1\le i<j\le r).
\tag{21}
$$
准确恢复式为
$$
 \begin{aligned}
 M_{00}&=M(0),\\
 M_{0i}&=\frac{M(e_i)-M(-e_i)}4,\\
 M_{ii}&=\frac{M(e_i)+M(-e_i)-2M(0)}2,\\
 M_{ij}&=\frac{M(e_i+e_j)-M(e_i)-M(e_j)+M(0)}2\quad(i<j).
 \end{aligned}
\tag{22}
$$
按 $M_{00}$、各对 $(M_{0i},M_{ii})$、最后 $M_{ij}$ 排列列，
并按 (21) 相同次序排列行，评价矩阵行列式为
$$
              2^{2r+r(r-1)/2}=2^{r(r+3)/2}.
\tag{23}
$$
先减去常数行，每一对 $e_i,-e_i$ 给块
$\left(\begin{smallmatrix}2&1\\-2&1\end{smallmatrix}\right)$，
最后每个混合项给对角元 $2$，即证 (23)。它在所有奇 $p$ 下
为单位。故所有观察为零迫 (15) 的全部系数为零。$\square$

作为表示，$R_3$ 上的 $\tau$ 是一个长度三的幺幂 Jordan 块。
它的所有单 Jordan--Hölder 因子都是平凡表示；以半单化替代
$R_3$ 会只剩 $c$，恰好丢掉本题要用的两项。

## 4. 类群 norm 的准确位移，和原两个符号

对任一 $H_0\subset G$，令 $\pi:k[G]\to k[G/H_0]$ 为
pushforward，定义
$$
 \iota(\bar g)=N_{H_0}g,\qquad N_{H_0}=\sum_{h\in H_0}h.
$$
不同 coset 的支集不相交，故 $\iota$ 在特征 $p$ 中仍单射，且
$$
 N_{H_0}z=\iota\pi(z),\qquad
                 \pi\iota=|H_0|\operatorname{id}.
\tag{24}
$$
当 $p\mid|H_0|$ 时第二式为零；这不使第一式中的 $\iota$
失去单射性。**先作 norm 再 pushforward** 会多出一个真的
$|H_0|$，不是原 (9) 的完整迹。

在 (12) 的商中，核由 $h_i=g_it^{-b_i}$ 生成，阶为
$p^{e_i}$。设 $y_i=h_i-1$、$T=t-1$，则
$$
 k[G]\simeq k[T,y_1,\ldots,y_r]/
       (T^p,y_1^{p^{e_1}},\ldots,y_r^{p^{e_r}}),\qquad
 N_{\ker\lambda}=\prod_{i=1}^r y_i^{p^{e_i}-1}.
\tag{25}
$$
置 $d_C=\sum_i(p^{e_i}-1)$。若 $\pi_\lambda(z)\ne0$，由
(25) 不同 monomial 的独立性得到准确等式
$$
 \boxed{\quad
 \operatorname{ord}_I(N_{\ker\lambda}z)
       =d_C+\operatorname{ord}_{T}(\pi_\lambda z).
 \quad}
\tag{26}
$$
所以原两项在保留全部类群标签的 norm 像中位于
$d_C+1,d_C+2$；不能在作完这个 norm 后再读总次数一、二。
例如 $G=C_p\times C_p$、$z=(t-1)^2$，原商为 $T^2\ne0$，
而保标签的 norm 为 $(s-1)^{p-1}(t-1)^2$，总次数是 $p+1$。

对实际 $\Theta_p$，完整基层迹为扭点给 $c=0$。
Heegner 共轭公式和 $w(E)=+1$，在 $p$ 群部分作唯一的平衡
平移后，给
$$
                        \Theta_p^*=-\epsilon\Theta_p,
                         \qquad g^*=g^{-1}.
\tag{27}
$$
解释平衡选择：复共轭对环类群作反演，原点可能多一个固定环类
平移；先求和掉阶与 $p$ 互素的标签，在奇阶 $G$ 中该平移有
唯一平方根，用它平移原源即可。观察素位也可在该奇阶二面体
扩张中选择为复共轭固定的素位。所有商同时使用这一选择。
乘一个群元素不改变 (19) 的零性，也不改变已知常数为零时
原低阶非零判据。

在 (13) 中 $x_i^*=-x_i$。因此 (27) 给：

| 观察符号 | 原全元素的最低候选项 | 商上实际条件 |
|---|---|---|
| $\epsilon=+1$ | $\sum_iL_ix_i\in I/I^2$ | 某个 $[T]\pi_\lambda(\Theta_p)\ne0$ |
| $\epsilon=-1$ | $\frac12\sum_{i,j}M_{ij}x_ix_j\in I^2/I^3$ | 某个 $[T^2]\pi_\lambda(\Theta_p)\ne0$ |

负号行中全部 $L_i=0$，故 (18) 退化为 $M=2m_2$。
两种符号的观察素数可以不同；没有在一个一般 admissible
一维局部空间里虚构两条相反符号线。

## 5. 保全部 $p$ 类群的有限 Heegner 下降

本节证明 R146 的两步判据可用于任一 (4) 的真实商，
不再要求 $p\nmid h_F$。为简洁记 $L=L_\lambda$、
$Q=Q_\lambda$、$\Gamma=\operatorname{Gal}(L/F)$，并设
$$
 B=\operatorname{Res}_{L/F}E,\qquad A=\ker(N:B\to E),\qquad
 \mathcal O=\mathbb Z_p[\zeta_p],\qquad
 \delta=\tau^{(p-1)/2}(\tau-1).
\tag{28}
$$

### 5.1 非零原迹及所有有限层的无挠点

若 $Q$ 非扭，由 $NQ=0$，$\mathbb Q[\Gamma]Q$ 是不可约
$\mathbb Q(\zeta_p)$ 表示。故每个非平凡角色的**未除群阶**
完整 Heegner 和均非扭。Nekovář (2007), Theorem 3.2，及
R139 §2 的整系数论证给
$$
 A(F)\otimes\mathbb Z_p=\mathcal O w,\qquad
 S=\Sha(A/F)[p^\infty]\text{ 有限},\qquad
 Q=\delta^a e w,\quad e\in\mathcal O^\times.
\tag{29}
$$
该角色定理不要求角色阶与 $p$ 互素；类群中其余标签已经在
(5) 的完整迹里。整论证仍用
$\sum_{\chi\ne1}e_\chi=p-N$，不引入 $1/p$。

另有
$$
                         E(F^{\rm ab})[p]=0.
\tag{30}
$$
因为满 $\mathrm{GL}_2(k)$ 的导出群包含 $\mathrm{SL}_2(k)$，
任一阿贝尔扩张所对应的 Galois 子群仍包含该群，而它在
$E[p]$ 上没有不变量。于是对每个环类域 $F[n]$，
$A[\delta](F[n])=E[p](F[n])=0$。沿
$0\to A[\delta^{j-1}]\to A[\delta^j]\to A[\delta]\to0$
归纳，得
$$
                A[\delta^j](F[n])=0\qquad(j\ge1).
\tag{31}
$$
Hochschild--Serre 因而给唯一下降
$$
 H^1(F,A[\delta^j])\xrightarrow{\sim}
 H^1(F[n],A[\delta^j])^{\operatorname{Gal}(F[n]/F)}.
\tag{32}
$$
两端之间的 $H^1$、$H^2$ 群的系数都是 (31) 的零群，
所以 (32) **不需要**扩张次数与 $p$ 互素。

### 5.2 指定分歧商与每个辅助层的真实域交

让 $n$ 是与 $p\ell389\operatorname{disc}F$ 互素的辅助平方自由
整数。$F[n]/F$ 在原 $\ell$ 不分歧，而 $L/F$ 在该位全分歧，
次数为素数 $p$，故
$$
                         L\cap F[n]=F.
\tag{33}
$$
特别 $L\cap F[1]=F$。在 $F[\ell n]/F[n]$ 中，原 $\ell$
局部群阶为 $pu$；它到 $\Gamma$ 的核为阶 $u$ 的群。定义
$$
 Y_n=\operatorname{Tr}_{F[\ell n]/LF[n]}P[\ell n]
       \in B(F[n]),\qquad
 Z_n=(\tau-1)Y_n\in A(F[n]).
\tag{34}
$$
由同一原 Heegner 范数和 Frobenius 同余，
$$
 N_\Gamma Y_n=a_\ell P[n],\qquad
 \operatorname{Tr}_{F[nq]/F[n]}Y_{nq}=a_qY_n.
\tag{35}
$$
这里 $Y_1$ 定义于 $LF[1]$，不应误写成 $Q$。其后才对
$\operatorname{Gal}(F[1]/F)$ 的**全部** coset 求和。

### 5.3 全 coset 导数、局部条件和有限--奇异恒等式

取任意所需精度 $p^m$。由 $L/F$ 在 $\ell$ 分歧、
$F(E[p^\infty])/F$ 在该位不分歧，二者域交为 $F$。
Chebotarev 可选择辅助 $q'$ 在复合域上的 Frobenius 为
复共轭，从而 $q'$ 惰性于 $F$、在 $L/F$ 分裂，且
$a_{q'}\equiv q'+1\equiv0\pmod{p^m}$。这些 $q'$ 是
Kolyvagin 导数的辅助素数，与 (6) 的一般 admissible 观察
素数及原 $\ell$ 都不同。

在 $F[n]/F[1]$ 的真实直积局部群上取
$D_{q'}=\sum_{j=1}^{q'}j\sigma_{q'}^j$、$D_n=\prod D_{q'}$。
选 $F[n]/F$ 中代表全部 Hilbert 类群 coset 的集合 $\mathscr S_n$，
并用 (33) 唯一地把其作用延到 $LF[n]/L$。原导出点为
$$
 \widetilde\kappa_n^B=\sum_{s\in\mathscr S_n}sD_nY_n,
 \qquad
 \widetilde\kappa_n^A=(\tau-1)\widetilde\kappa_n^B.
\tag{36}
$$
全部 $p$ 类群 coset 在 (36) 内，系数为一。
恒等式 $(\sigma_{q'}-1)D_{q'}=q'+1-N_{q'}$ 与 (35)
先给局部群不变性，再由完整 coset 求和给全
$\operatorname{Gal}(F[n]/F)$ 不变性；(32) 唯一地下降其
Kummer 类。此即 Howard 已发表 §1.7, Lemma 1.7.1 后的
有限层构造，他的 Theorem A 本身没有类数限制。

其非辅助地方的局部条件逐项保持：$F[n]/F$ 只在辅助 $n$
处分歧；原 $\ell$ 处因
$$
             \#E(\mathbb F_{\ell^2})
              =(\ell+1)^2-a_\ell^2\not\equiv0\pmod p
$$
给所有 $H^i(F_\ell,A[\delta^j])=0$。其余好位使用不分歧
范数和 Lang 定理；$389$ 的 $I_1$ Tate 参数赋值为一，消去
不分歧范数的赋值障碍。完整 Kummer 正合列给全部有限精度
的 Cartesian 性，正是 R139 §4/R146 §2 的计算；其内容只
依赖 $L/F$ 的局部行为，不依赖 $h_F$。

辅助 $q'$ 惰性于 $F$ 时在全部原 ring-class 标签上分裂。
对每一个 coset，先作原 Heegner Frobenius 同余，再搬回同一
完成，局部算子仍为 $\varphi_{q'}\otimes1$。因此 Howard
Proposition 1.7.4 的实际计算逐项给
$$
 \begin{aligned}
 c_n^B(\operatorname{Fr}_{q'^2})
    &=\frac{\varphi_{q'}^2-1}{p^m}
                       \overline{\widetilde\kappa_n^B},\\
 c_{nq'}^B(\sigma_{q'})
    &=\frac{a_{q'}-(q'+1)\varphi_{q'}}{p^m}
                       \overline{\widetilde\kappa_n^B},\\
 a_{q'}-(q'+1)\varphi_{q'}
    &=-q'\varphi_{q'}^{-1}(\varphi_{q'}^2-1).
 \end{aligned}
\tag{37}
$$
这些式子中的整除点按该命题的局部 Kummer 规范读取，
不是声称原点全局可除。完整 coset 求和、$B\to A$、
所有精度商都与同一整自同构
$-q'\varphi_{q'}^{-1}$ 相容。没有一个 $h_F$ 或 $1/h_F$
出现在 (37) 中。

在 $n=1$，(36) 的全 coset 和恰好给
$$
            [t_F]\widetilde\kappa_1^A=(\tau-1)Q.
\tag{38}
$$
因此首项在 (29) 的原格中指数仍为 $a+1$。
不能因为 $NQ=0$ 而把整个类族除一次 $\delta$；高层
$N_\Gamma Y_n=a_\ell P[n]$ 仍不是已知的零。

### 5.4 全 Selmer 上下界和两步结论

Howard H.0--H.5 的满像、Sah、共轭自对偶和 Cartesian
条件按 R139 §4 原样成立。其 Sah 条件用的中央 $(-I,1)$
来自 $L\cap F(E[p^\infty])=F$，也没有类数条件。
(37) 给 R139 §6 已完整证明的 weak-stub 输入，故
$$
                       \operatorname{length}_{\mathcal O}S
                                      \le2(a+1).
\tag{39}
$$
局部范数的同一计算给保复共轭的通常局部条件等式
$\operatorname{Sel}_\delta(A/F)=\operatorname{Sel}_p(E/F)$。
R146 §4 的有限 Cassels--Tate 原始层逐层配对给
$$
 \operatorname{length}_{\mathcal O}S\ge2\dim_k S[\delta]^+,
 \qquad
 \dim_k S[\delta]^+=r_E+d_+-\mathbf1_{a\ {
m even}},
\tag{40}
$$
其中 $r_E=\operatorname{rank}E(\mathbb Q)\ge2$，
$d_+=\dim_k\Sha(E/\mathbb Q)[p]$，允许未知可除部分。
这里用的是**整个通常 Selmer 群**，没有只在两个已知
Mordell--Weil 点上验一个高度行列式。

若 $a=0$，(39)--(40) 给 $r_E+d_+\le2$；若 $a=1$，
仍给同一个界。于是
$$
 \boxed{\quad
 Q\notin\delta^2(A(F)\otimes\mathbb Z_p)
  \Longrightarrow
  \operatorname{rank}E(\mathbb Q)=2,
              \qquad\Sha(E/\mathbb Q)[p^\infty]=0.
 \quad}
\tag{41}
$$
这证明所述 class-number 扩张。Howard Theorem B/§2.3 对
$\mathbb Z_p$ 塔加的类数条件不在本有限证明中被挪用或省略；
这里用 (33)、(31)--(32)、(36)--(38) 分别付清所需输入。

## 6. 实际总二阶项到固定曲线 Sha 的精确量词

**定理 6.1。** 取 §1 的同一 $(p,F,\ell)$，假设 (3) 分裂。
取任一个满足 (6) 的 $q$，并形成真正的 (7)--(8)。若
$$
                         \Theta_p\notin I^3,
\tag{42}
$$
则存在 (21) 的一个 $\mathbf b$，其实际子域 $L_{\mathbf b}$
及完整原点 $Q_{\mathbf b}$ 满足 (41)。因此固定 (1) 的
$E$ 满足 $\operatorname{rank}E(\mathbb Q)=2$、
$\Sha(E/\mathbb Q)[p^\infty]=0$。

对负号观察 $\epsilon=-1$，条件 (42) 准确为
$$
              [\Theta_p]_{I^2/I^3}\ne0.
\tag{43}
$$
对正号观察，准确为 $[\Theta_p]_{I/I^2}\ne0$。
原 $h_F$ 与 $p$ 互素时没有额外的 $\mathbf b$：这些条件分别
就是 R234 的第二负矩和第一正矩。

**证明。** (19)、常数为零和 (9) 给某个实际商的
$[T]$ 或 $[T^2]$ 完成非零。若
$Q_{\mathbf b}\in\delta^2(A(F)\otimes\mathbb Z_p)$，写
$Q_{\mathbf b}=\delta^2Z$。真实完成映射与群环作用相容，且
$NZ=0$ 使 $\Phi_q(Z)$ 常数为零。因此
$$
 \Phi_q(Q_{\mathbf b})
     =\frac{T^2}{1+T}\Phi_q(Z)\in T^3k[C_p]\otimes W_q,
$$
与上述低项非零矛盾。该非零也先保证 $Q_{\mathbf b}$ 非扭：
由 (30) 它没有 $p$ 扭点，阶与 $p$ 互素的扭点在 $W_q$ 中
为零。故 (29)--(41) 可全部应用。$\square$

注意 (42) 的 $\Theta_p$ 是**保留 $p$ 类群标签的原全元素**，
不是已经作完 $N_{\ker\lambda}$ 的元素；后者的正确位置由
(26) 给出。也没有将固定 $q$ 的一个任意非零值替代实际
CM 全元素 (7)。

## 7. 下一实际非零问题及已发表非零输入的范围

本篇将下一问题精确变为：在 R149/R153 的同一原联合无穷
$(p,\ell)$ 集合上，找到合法 $F$ 及真实一般 admissible $q$，
使 (3) 分裂且 (42) 成立；负号版本就是实际 (43)。
当允许 $p\mid h_F$ 时，(11) 还须全部为零。
固定 $p,F$ 另选 $\ell$ 的 Chebotarev 可行性，不是这一联合
无穷性。总二阶项非零也不由 (19) 的联合忠实性自行产生。

作为当前已核的文献输入边界，X. Zhang 的已发表
*Non-vanishing mod $p$ of theta lifts for $(O_{2n+1},Mp_{4n})$*
（Forum Mathematicum **38** (2026), 667--717）Theorems 7.5、7.8
需要 (C1)--(C4)。其中 (C1) 是系数代数表示维数大于一，
(C3) 是指定紧开层指数与 $p$ 互素；其 toric 非零构造变化一个
辅助 $\ell_0\ne p$ 的高导子角色。原 (7) 是权二的标量
definite 函数；原阶 $p$ 局部层的完整三维幺幂商也不是该文
的互素 Fourier 分解。故此定理没有证明 (42)。

Burungale--Tian 的已发表 *Horizontal non-vanishing of Heegner
points and toric periods*（Advances in Mathematics **362** (2020),
106938）给变化 CM 域时许多类群角色的非零；它没有断言
本篇指定的完整类群三维幺幂观察非零。这里没有从这些定理的
单向非零结论反推本篇原全元素为零；结论只是本篇仍须实际证明
(42)，并且 (19)、(26)、(41) 已将该输入到目标的全部所述
代价付清。

## 来源与依赖

- R2、R136：固定 E389 的模型、导子、根数、非 CM 和秩下界。
- R139 及其完整 note：范数一格、全部局部条件、实际有限--奇异
  比较、weak-stub 与不可删除的额外 $\delta$；R146 的完整 note：
  不用负扭曲低秩输入的全正号 Selmer/Cassels--Tate 下界。
- R234：原 conductor、同一度零规范及逐完整标签的 definite
  比较；本篇保留该已付比较并逐一说明不依赖类数的部分。
- B. Howard, *The Heegner point Kolyvagin system*, Compositio
  Mathematica **140** (2004), 1439--1472，Theorem A、§1.6--1.7，
  尤其 Lemma 1.7.1、其后的 Hochschild--Serre 唯一下降和
  Proposition 1.7.4；
  [发表全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)。
- J. Nekovář, *The Euler system method for CM points on Shimura
  curves*（2007），Theorem 3.2；[作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)。
- W. Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge Journal of Mathematics **2** (2014), 191--253，Theorem 2.1、
  §4.2 的 (4.7)--(4.9)，具体假设已由 R234 对原对象核验。
- X. Zhang，上述 Forum Mathematicum 论文，
  [DOI](https://doi.org/10.1515/forum-2024-0507)，
  [与发表稿对应的作者全文](https://arxiv.org/pdf/2203.05359)。
- A. Burungale--Y. Tian，上述 Advances in Mathematics 论文，
  [DOI](https://doi.org/10.1016/j.aim.2019.106938)，
  [作者机构存档](https://authors.library.caltech.edu/records/pby48-75q47)。

群代数、ramified 商判据、norm 位移及联合矩恢复均在本文直接
证明，不依赖未发表的全 Selmer 非退化或高阶 Heegner 猜想。

配套精确证书为
[脚本](../scripts/check-full-p-class-unipotent-theta-jets.py) 与
[输出](../scripts/check-full-p-class-unipotent-theta-jets.json)，67 项全部通过。
其中直接核验 $C_7\times C_7\times C_{49}$ 的全部 49 个
规范化分歧商，保留阶 $49$ 的类群标签；另核类群 norm 的
真实增广位移及前七个一般二次恢复矩阵的 $2$ 幂行列式。
这些有限证书补充本文的任意 $p,r,e_i$ 证明，不代替算术非零性。
