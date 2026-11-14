# R281：最大阶类群的实际非零二阶项与同标签分歧提升

日期：2026-11-13。**状态：本文的降层恒等式、正密度提升、
实际非空例及全部群论已证明。未证明目标素数 $p$ 有无穷多个。**

本篇给 O4 一个不需先选择原 $\ell$ 的充分输入：直接在最大
整环的完整 Hilbert 类群上检验低阶 theta 项。若该项非零，
同一 CM 标签的 Hecke 范数关系把它送入 R271 的原分歧来源。
这里允许 $p\mid h_F$，且先付清环类 $p$ 扩张的分裂条件。

这个输入不是被秩至少二恒强迫为零的条件。固定 E389、
$p=11,q=13,F=\mathbb Q(\sqrt{-2267})$ 的真实最大阶来源满足
$$
                  [T^0]\Theta_1=[T]\Theta_1=0,\qquad
                  [T^2]\Theta_1=4\ne0\pmod{11}.
\tag{1}
$$
本文保留这一个实例，以排除“新条件可能恒空”的具体疑问；
不增加目标素数的有限扫描。

## 1. 固定对象与最大阶全来源

固定
$$
        E:y^2+y=x^3+x^2-2x,\qquad N_E=389.
\tag{2}
$$
取 R271 合法的 $p\ge7$：$E$ 在 $p$ 好普通且非异常，
$\bar\rho_{E,p}$ 满像，并保留 R234 的固定参数化单位条件。
取虚二次域 $F$，满足
$$
 \mathcal O_F^\times=\{\pm1\},\qquad
 389\text{ split in }F,\qquad p\nmid\operatorname{disc}F.
\tag{3}
$$
由于 $F$ 在 $p$ 不分歧，而满像的唯一可能二次行列式子域
在 $p$ 分歧，限制到 $G_F$ 仍为满像。后文只使用 R271
已付清的整个通常 Selmer 接口。

设 $H_1=F[1]$ 为 Hilbert 类域，
$$
       \mathcal C=\operatorname{Cl}(F),\qquad
       C=\mathcal C_{(p)},\qquad k=\mathbb F_p,\qquad
       J=\ker(k[C]\longrightarrow k).
$$
固定同一模参数化的最大阶 CM 点 $x(1)$ 和 $P[1]$。
R271 (5) 前的 Gross--Zagier 论证给
$P_F=\operatorname{Tr}_{H_1/F}P[1]$ 为扭点。
取与 $p$ 互素的整数 $t_F$ 杀掉它。

取 R234 的一般 admissible 观察 $q$：
$$
 \begin{gathered}
 q\nmid p389\operatorname{disc}F,\qquad q\text{ inert in }F,\\
 q^2\not\equiv1\pmod p,\qquad
 a_q\equiv\epsilon(q+1)\pmod p,\qquad \epsilon=\pm1.
 \end{gathered}
\tag{4}
$$
令 $\varphi_q$ 为该文实际升层和逐 CM 标签比较得到的
definite 本征函数。定义
$$
 \Theta_1^{\mathrm{full}}
   =\overline t_F
      \sum_{a\in\mathcal C}
       \varphi_q(\operatorname{Red}_q x(1)^a)\,a^{-1}
            \in k[\mathcal C].
\tag{5}
$$
将阶与 $p$ 互素的标签完整求和，记所得元素为
$\Theta_1\in k[C]$。这只是群环 pushforward；
**没有除以任何类数或取 $p$ 类群上的半单幂等元。**
由同一个单位的逐点比较，
$$
                         \Theta_1\in J.
\tag{6}
$$
因此本文的新输入是
$$
                         \Theta_1\notin J^3.
\tag{7}
$$
它仍然是一个实际完整类群和的非零条件，不是环境
$\varphi_q$ 的非零。

## 2. 同一 CM 标签的准确 Hecke 范数式

暂取任意与 $pq389\operatorname{disc}F$ 互素、在 $F$ 惰性的
素数 $\ell$，并令 $H_\ell=F[\ell]$。环类映射为
$$
 \pi:\mathcal G_\ell=\operatorname{Gal}(H_\ell/F)
                   \longrightarrow\mathcal C.
$$
其核阶为 $\ell+1$。定义 $\Theta_\ell^{\mathrm{full}}$
时使用 (5) 的同一 $\varphi_q,t_F$、同一 $389$ 方向和
同一度零 Hecke 规范，只把 $x(1)$ 换为原 $x(\ell)$。

**命题 2.1（完整同标签范数）。** 在未删任何类群标签的
群环中，准确有
$$
              \boxed{\quad
       \pi_*\Theta_\ell^{\mathrm{full}}
                =\overline a_\ell\,\Theta_1^{\mathrm{full}}.
                     \quad}
\tag{8}
$$
先仅合并两侧阶与 $p$ 互素的标签，置
$G_\ell=(\mathcal G_\ell)_{(p)}$，同样得到
$$
              \boxed{\quad
       \pi_*\Theta_\ell=\overline a_\ell\,\Theta_1
                     \quad\text{in } k[C].
                    \quad}
\tag{9}
$$

**证明。** 固定 $a\in\mathcal C$。因 $\ell$ 在 $F$ 惰性，
最大阶 CM 点 $x(1)^a$ 的全部 $\ell+1$ 个循环
$\ell$-isogeny 邻点都具有 conductor $\ell$；它们正是
$\pi^{-1}(a)$ 的全部 CM 标签，没有水平邻点或额外旧项。
对每个这样的纤维用实际本征关系
$T_\ell\varphi_q=a_\ell\varphi_q$，得到
$$
 \sum_{g\in\pi^{-1}(a)}
       \varphi_q(\operatorname{Red}_q x(\ell)^g)
       =\overline a_\ell
          \varphi_q(\operatorname{Red}_q x(1)^a).
\tag{10}
$$
若 Artin 采用整体相反约定，两侧同时反转标签。
对 $a$ 求和即得 (8)。群环 pushforward 的复合相容给 (9)。
等价地，先在原椭圆曲线上使用
$$
       \operatorname{Tr}_{H_\ell/H_1}P[\ell]=a_\ell P[1]
$$
再用 R234 的同一单位比较，也得到同一个式子。
没有在此过程中平均 $h_F$、$\ell+1$ 或 $C$。$\square$

特别地，如果 $\overline a_\ell\ne0$，则
$$
            \Theta_1\notin J^3
            \quad\Longrightarrow\quad
            \Theta_\ell\notin I_\ell^3,
 \qquad I_\ell=\ker(k[G_\ell]\longrightarrow k).
\tag{11}
$$
理由是 $\pi_*(I_\ell^3)\subset J^3$。要应用 R271，
还必须确实存在在 $\ell$ 分歧的次数 $p$ 商。下一节支付
这一点，并同时保留 $p\nmid a_\ell$ 和 $v_p(\ell+1)=1$。

## 3. 分裂环类 $p$ 扩张的正密度构造

写
$$
       C=\bigoplus_{i=1}^r\langle c_i\rangle,\qquad
                   |c_i|=p^{e_i},\quad e_i\ge1.
$$
取代表这些类的整理想 $\mathfrak a_i$，使其与预先指定的
有限坏集互素，并写
$$
 \mathfrak a_i^{p^{e_i}}=(\alpha_i),\qquad
 n_i=N\mathfrak a_i>0,\qquad
 \alpha_i\overline\alpha_i=n_i^{p^{e_i}}.
\tag{12}
$$
定义实际有限 Kummer 域
$$
             K=F(\mu_p,\alpha_1^{1/p},\ldots,\alpha_r^{1/p}),
             \qquad K_0=F(\mu_p).
\tag{13}
$$
允许这些根式之间有关系；不预设 $[K:K_0]=p^r$。

### 3.1 $K/\mathbb Q$ 的实际群及 cyclotomic $p^2$ 交

(12) 给
$$
          \overline{\alpha_i^{1/p}}
                  =n_i^{p^{e_i-1}}/\alpha_i^{1/p}
\tag{14}
$$
（取实际复嵌入中的根；其他根只相差 $\mu_p$）。
所以 $K/\mathbb Q$ 是 Galois。令
$P=\operatorname{Gal}(K/K_0)$，它是一个初等阿贝尔
$p$ 群，维数可以小于 $r$。

$p\nmid\operatorname{disc}F$ 给
$F\cap\mathbb Q(\mu_p)=\mathbb Q$，故
$\Delta=\operatorname{Gal}(K_0/F)\simeq\mathbb F_p^\times$。
Kummer 配对中，radicand 空间由 $\alpha_i\in F^\times$
生成，因而 $\Delta$ 作用平凡；配对的值域 $\mu_p$
带 cyclotomic 特征 $\omega$。于是 $\Delta$ 在 $P$
上的共轭作用准确为 $\omega$：
$$
                   \sigma_a\tau\sigma_a^{-1}=a\tau
                         \qquad(a\in\mathbb F_p^\times,\ \tau\in P).
\tag{15}
$$
这里右侧用 $P$ 的加法记号。选 $a\ne1$，
$[\sigma_a,P]=(a-1)P=P$。由于 $K_0/\mathbb Q$ 阿贝尔，
$$
             [\operatorname{Gal}(K/\mathbb Q),
                 \operatorname{Gal}(K/\mathbb Q)]=P.
\tag{16}
$$
因此 $K$ 的最大阿贝尔子域恰为 $K_0$，从而
$$
                  \boxed{\quad
                K\cap\mathbb Q(\mu_{p^2})
                         =\mathbb Q(\mu_p).
                         \quad}
\tag{17}
$$
最后一步还用了 $F\cap\mathbb Q(\mu_{p^2})=\mathbb Q$：
若这个交是 $F$，则 $F$ 是只在 $p$ 分歧的二次 cyclotomic
子域，与 (3) 矛盾。等价的局部群论说法是：Kummer
$p$ 核带 $\omega$，而 cyclotomic $p^2/p$ 核的
$\Delta$ 共轭作用平凡；二者没有共同非零 $p$ 商。

### 3.2 与 $E[p]$ 的交

令 $M=\mathbb Q(E[p])$，
$K_2=K\mathbb Q(\mu_{p^2})$。$K_2/\mathbb Q$ 是可解
Galois 扩张，而
$\operatorname{Gal}(M/\mathbb Q)=\operatorname{GL}_2(k)$。
对 $p\ge5$，$\operatorname{SL}_2(k)$ 完美。
例如在 $\operatorname{SL}_2(k)$ 内取
$d=\operatorname{diag}(a,a^{-1})$、$a^2\ne1$，
则与 $d$ 的交换子给全部上下初等幺幂矩阵，而这些矩阵
生成 $\operatorname{SL}_2(k)$。所以到可解群的任何同态
都杀掉这个子群。

因此 $M\cap K_2$ 包含在 $M$ 的 determinant 子域，
后者由 Weil 配对准确为 $\mathbb Q(\mu_p)$。两侧本来
都含这个域，故
$$
                  \boxed{\quad
                 M\cap K_2=\mathbb Q(\mu_p).
                          \quad}
\tag{18}
$$
这一步没有把一个可解 Kummer 条件与整个剩余像默认独立；
它明确计算了全部共同子域。

### 3.3 同时满足全部原局部条件

令 $c$ 是 $K$ 上的实际复共轭，故 $c^2=1$，
它在 $F$ 非平凡，在 $\mu_p$ 上为逆元。由 (17)，
$c$ 可与
$$
        -1+p\in(\mathbb Z/p^2\mathbb Z)^\times
\tag{19}
$$
拼成 $K_2/\mathbb Q$ 的一个自同构：两者在
$\mathbb Q(\mu_p)$ 上相同。再由 (18)，它可与
$$
                 A=\begin{pmatrix}2&0\\0&-2^{-1}\end{pmatrix}
                        \in\operatorname{GL}_2(k)
\tag{20}
$$
拼成 $K_2M/\mathbb Q$ 的一个自同构。
其 determinant 是 $-1$，正好与 (19) 模 $p$ 相容；
其 trace 是 $3/2\ne0$，因为 $p\ge7$。

Chebotarev 用这个实际共轭类给出正密度的素数 $\ell$，
避开任意预先给定的有限集合，并同时满足
$$
 \begin{gathered}
 \ell\text{ inert in }F,\qquad
 \ell\equiv-1+p\pmod{p^2},\\
 a_\ell(E)\equiv3/2\pmod p,\qquad
 \operatorname{Frob}_\ell^2|_K=1.
 \end{gathered}
\tag{21}
$$
尤其
$$
                       \ell+1=pu,\qquad p\nmid u a_\ell.
\tag{22}
$$
在 $F$ 唯一的 $\ell$ 素位处，(21) 的最后一项使
所有 $\alpha_i^{1/p}$ 的剩余值都位于
$\mathbb F_{\ell^2}$；已排除分母和零范数素位。
于是
$$
       \alpha_i^{(\ell^2-1)/p}
            =\alpha_i^{(\ell-1)u}\equiv1\pmod\ell
                    \qquad\text{对每个 }i.
\tag{23}
$$
按 R271 (10)--(11) 的真实类群延拓公式，所有延拓系数
$b_i$ 因此为零。我们得到
$$
 \boxed{\quad
 0\longrightarrow\langle t\rangle\simeq C_p
    \longrightarrow G_\ell\longrightarrow C\longrightarrow0
       \quad\text{确实分裂。}
 \quad}
\tag{24}
$$
$t$ 是原 $\ell$ 惯性。这个证明不需要另加类数素于 $p$
的假设，也没有把存在次数 $p$ 子域误当成存在分歧的
次数 $p$ 子域。

**量词。** (21) 是对每个固定的 $(p,F)$ 的正密度结论。
它没有给 $\ell$ 关于 $p$ 的大小界，更没有保留
R149--R156 的同一个大因子、小高度联合子族。本文后面的
应用不需要那个高度筛：实际低阶项非零已经直接保证原点
非扭及两步条件。

## 4. 真实分歧商的定量非零与整个 Selmer 结论

**定理 4.1。** 在 (2)--(7) 的全部实际输入下，§3 的每个
$\ell$ 至少给
$$
                              (p-2)p^{r-1}
\tag{25}
$$
个互不相同、在原 $\ell$ 全分歧的次数 $p$ 子域
$L/F$，其原完整 Heegner 点满足 $a\le1$。于是
$$
             \operatorname{rank}E(\mathbb Q)=2,\qquad
                         \Sha(E/\mathbb Q)[p^\infty]=0.
\tag{26}
$$
若最大阶 theta 的一次项已经非零，(25) 可改为
$(p-1)p^{r-1}$。输入 (7) 自然要求 $r\ge1$。

**证明。** 用 (24) 取分裂提升 $g_i$，
$G_\ell=\langle t\rangle\oplus C$。在
$k[G_\ell]/I_\ell^3$ 中用 R271 的截断对数坐标
$x_0=\log t,\ x_i=\log g_i$，写
$$
 \Theta_\ell=L_0x_0+\sum_iL_ix_i
   +\frac12M_{00}x_0^2+\sum_iM_{0i}x_0x_i
   +\frac12\sum_{i,j}M_{ij}x_ix_j.
\tag{27}
$$
常数项为零。若
$$
           \Theta_1=\sum_i l_i x_i
                   +\frac12\sum_{i,j}m_{ij}x_ix_j\pmod{J^3},
$$
(9) 准确给
$$
                    L_i=\overline a_\ell l_i,\qquad
                    M_{ij}=\overline a_\ell m_{ij}
                           \quad(i,j\ge1).
\tag{28}
$$
原局部和混合项 $L_0,M_{00},M_{0i}$ 没有被 (9) 算出，
必须留在 (27) 中。

全部规范化真实分歧商为
$$
              \lambda_{\mathbf b}(t)=1,\qquad
              \lambda_{\mathbf b}(g_i)=b_i,\qquad
                        \mathbf b\in k^r.
\tag{29}
$$
其 kernel 不同：同一 kernel 的两个加法满射只差一个
非零倍数，而 $t\mapsto1$ 已固定这个倍数。故 (29) 确实
给 $p^r$ 个不同子域。

令 $T=\tau-1$，$\log\tau=T-T^2/2$。商中的两个实际矩为
$$
 \begin{aligned}
 m_1(\mathbf b)&=L_0+\overline a_\ell\sum_i l_i b_i,\\
 2m_2(\mathbf b)+m_1(\mathbf b)
       &=M_{00}+2\sum_iM_{0i}b_i
                         +\overline a_\ell\sum_{i,j}m_{ij}b_i b_j.
 \end{aligned}
\tag{30}
$$
这是同一个 $\Theta_\ell$ 的真实商，不是任意环境二次形式。
如果 $(l_i)\ne0$，第一式只在 $p^{r-1}$ 个点为零。
若 $(l_i)=0$ 而 $L_0\ne0$，全部商都已通过第一矩。
最后，若它们都为零，则 (7) 保证 $(m_{ij})\ne0$；
因 $p>2$，(30) 的第二式是一个非零、次数至多二的多项式。
它在 $k^r$ 上至多有 $2p^{r-1}$ 个零点。这给 (25)。

对每一个通过的商，R271 (9) 保留全部 kernel 类群标签，
所以其点恰为
$$
          Q_{\mathbf b}
             =[t_F]\operatorname{Tr}_{H_\ell/L_{\mathbf b}}P[\ell].
\tag{31}
$$
不是部分 coset 和，也没有平均 $p$ 类群。
(21)--(24) 付清该篇所需的实际分歧、$p\nmid u a_\ell$
及不相交条件；低矩非零付清原非扭和 $a\le1$。
应用该篇整个通常 Selmer 的 Cassels--Tate/弱 Euler 系统
结论，便得 (26)。这里没有仅在已知 Mordell--Weil 子空间
上做高度非退化测试。$\square$

## 5. 新输入确实非空：$F=\mathbb Q(\sqrt{-2267})$

### 5.1 完整类群及主关系

令
$$
      \eta^2-\eta+567=0,\qquad
      F=\mathbb Q(\eta),\qquad p=11,\qquad q=13.
\tag{32}
$$
$2267$ 是素数。全部约化正定二次型为
$$
 \begin{gathered}
 (1,1,567),\quad (3,\pm1,189),\quad(7,\pm1,81),\\
 (9,\pm1,63),\quad(21,\pm13,29),\quad(21,\pm1,27).
 \end{gathered}
\tag{33}
$$
因此 $h_F=11$。理想 $\mathfrak a=(3,\eta)$ 非主：
若存在范数 $3$ 的整元 $x+y\eta$，则
$$
       N(x+y\eta)
          =(x+y/2)^2+\frac{2267}{4}y^2=3
$$
迫使 $y=0$，而 $x^2=3$ 无整数解。
故 $[\mathfrak a]$ 生成全部类群。

其准确主关系是
$$
           \mathfrak a^{11}=(324+11\eta),\qquad
             N(324+11\eta)=3^{11}.
\tag{34}
$$
在 $3$ 的另一根 $\eta=1$ 上，$324+11\eta\equiv2$，
故这个范数没有分到共轭素理想。这验证了 (34) 的方向，
而不仅仅验证一个数值范数。

$389$ 在 $F$ 分裂、$13$ 惰性，$11$ 不分歧；
R276 已付 $p=11,q=13,\epsilon=-1$ 的全部本征线、
剩余满像、普通非异常和规范单位。并且
$$
   \mathfrak n=(389,\eta+24),\qquad
             (24+\eta)=\mathfrak a\mathfrak n,\qquad
             N(24+\eta)=3\cdot389.
\tag{35}
$$
所以 $[\mathfrak n]=[\mathfrak a]^{-1}$，这也将确定两个
$389$ 方向之间的准确类群平移。

### 5.2 真实最大阶嵌入与全部十一项

使用 R276 的同一个最大整环
$$
 \mathcal O_{13}
   =\mathbb Z\left\langle
      1,\ i,\ \frac{1+i+j}{2},\ \frac{2+i+ij}{4}
                  \right\rangle,
       \qquad i^2=-2,\quad j^2=-13.
\tag{36}
$$
嵌入 $\eta\mapsto r$ 取
$$
           r=(-10,-11,4,17),\qquad
           \operatorname{trd}r=1,\quad\operatorname{nrd}r=567.
\tag{37}
$$
判别式为 $-2267$，故是最大阶的最优嵌入。
在 R276 的同一个 $389$ 分裂矩阵规范中，
$$
             r_{389}=
                 \begin{pmatrix}375&369\\175&15\end{pmatrix}.
\tag{38}
$$
两条特征线为 $v_+=2,v_-=189$，特征值分别是
$365=-24$ 和 $25$。因此它们正是 (35) 的
$\mathfrak n,\overline{\mathfrak n}$ 方向。

每一步取 R276 全部四个范数 $3$ 代表中唯一满足
$$
                  \ker(a_{j,3})=\ker(r_{j,3})
\tag{39}
$$
的 $a_j$，并作实际理想 isogeny
$$
          r_{j+1}=a_jr_j\overline a_j/3,\qquad
          v_{j+1,\pm}=a_{j,389}v_{j,\pm}.
\tag{40}
$$
(39) 取的是 $\eta=0$ 的素理想，即同一个
$\mathfrak a=(3,\eta)$，不是在每一步任意换方向。
全部真嵌入及两方向标签如下；坐标均相对于 (36)。

| $j$ | $r_j$ | $a_j$ | $v_{j,+}$ | $v_{j,-}$ |
|---|---|---|---|---|
| 0 | $(-10,-11,4,17)$ | $(1,1,0,-1)$ | 2 | 189 |
| 1 | $(-2,-11,-6,11)$ | $(1,1,0,-1)$ | 45 | 28 |
| 2 | $(-8,-17,6,11)$ | $(1,1,0,-1)$ | 354 | 216 |
| 3 | $(-6,-7,-4,17)$ | $(1,1,0,0)$ | 250 | 137 |
| 4 | $(11,3,-10,-11)$ | $(0,1,0,-1)$ | 297 | 94 |
| 5 | $(-5,11,4,7)$ | $(1,1,0,0)$ | 268 | 15 |
| 6 | $(2,17,-6,3)$ | $(1,1,0,0)$ | 108 | 171 |
| 7 | $(5,17,0,-9)$ | $(1,1,0,0)$ | 158 | 53 |
| 8 | $(-4,11,6,3)$ | $(1,1,0,0)$ | 23 | 109 |
| 9 | $(-1,15,-4,7)$ | $(0,1,0,-1)$ | 244 | 344 |
| 10 | $(1,-7,10,-11)$ | $(1,1,0,0)$ | 385 | 179 |

第十一步准确回到各自原状态。每个方向的十一对
$(r_j,v_{j,\pm})$ 互异，且 (33)--(34) 证明这就是全部
类群标签，不是一个遗漏其他 coset 的短轨道。

取群环生成元，使上表的实际理想作用第 $j$ 项成为
(5) 中的第 $j$ 个系数；这等价于在 Artin 正逆约定中
固定一次整体反转。把 R276 唯一模本征函数的同一规范
值代入，得到两条**完整**系数行
$$
 \begin{aligned}
 \theta_+&=(4,7,5,7,4,5,4,5,5,4,5),\\
 \theta_-&=(4,6,4,7,6,7,6,6,7,6,7).
 \end{aligned}
\tag{41}
$$
在第一行有
$$
 \sum_j\theta_{+,j}=0,\qquad
 \sum_jj\theta_{+,j}=0,\qquad
 \sum_j\binom j2\theta_{+,j}=4\pmod{11}.
\tag{42}
$$
另一行的三个矩为 $(0,0,7)$，也非零。
真实负号观察的反射式为
$\theta_{+,j}=\theta_{+,4-j}$，下标取模 $11$。
它与 (42) 的偶增广阶一致。

### 5.3 共轭 $389$ 方向与扭点规范

(35) 还给出不靠浮点辨认的方向比较。
以实际 isogeny 步的格标记为 $\mathfrak a^{-j}$，
Atkin--Lehner $w_{389}$ 把正方向第 $j$ 项送到负方向
第 $j-1$ 项，因为
$\mathfrak n^{-1}$ 的类为 $[\mathfrak a]$。
固定曲线的 $w_{389}$ 特征为 $-1$，故应有
$$
                        \theta_{-,j}=-\theta_{+,j+1}.
\tag{43}
$$
(41) 逐项准确验证了这个等式。因此第二方向不是一个
未经支付的独立观测，也没有把共轭类标签忘掉。

此处事实上可取 $t_F=1$。$3$ 在 $F$ 分裂，而 $13$ 惰性，
对应的好约化群阶为
$$
                     \#E(\mathbb F_3)=6,\qquad
                     \#E(\mathbb F_{13^2})=187.
\tag{44}
$$
它们互素，且另一剩余特征也不整除对应阶。
两个好约化的 prime-to-characteristic 扭点单射给
$E(F)_{\mathrm{tors}}=0$。于是 (41)--(42) 使用原整数
Heegner 点，不需再乘一个不明整数。

由 R234 的单位比较和完整最优嵌入 reduction 对应，
(42) 就是 (1)。这证明一般的
“秩至少二迫使最大阶 $\Theta_1\in J^3$”断言为假。

对 §3 构造的每一个 $\ell$，(30) 在本例成为
$$
              m_2(b)=A_\ell+B_\ell b
                                  +4\overline a_\ell b^2,
                         \qquad b\in\mathbb F_{11},
\tag{45}
$$
其中 $A_\ell,B_\ell$ 是尚未逐值计算的真实局部、混合项。
二次系数是非零的，故至少九个真实分歧商通过原两步门。
没有为了得到这个结论删掉 $A_\ell,B_\ell$。
这给固定 $p=11$ 无穷多个原合法 $\ell$ 的实质性提升；
其量词仍然不是无穷多个 $p$。

## 6. 与 R276 的第四阶类群像区别

从 R276 的 $F=\mathbb Q(\sqrt{-1307}),\ell=43$
原 $C_{11}^2$ 完整矩阵，仅对局部惯性标签求和，准确得到
$$
                  (4,10,7,7,10,4,10,7,1,7,10).
\tag{46}
$$
$a_{43}=12\equiv1\pmod{11}$，故 (9) 说明这正是该例的
最大阶类群行。其 binomial 系数从次数零到十依次为
$$
                       (0,0,0,0,1,6,3,4,8,8,10).
\tag{47}
$$
所以它准确从第四阶开始。R276 的二阶非零在那里来自
局部/混合方向，不能由 (46) 的类群低项提供。
本文没有用抽象 Hecke 范数式把那个未知来源换名为已知非零；
而 (41) 则给另一个实际最大阶来源，真正满足新输入。

证书
[脚本](../scripts/check-unramified-class-jet-and-ramified-lifting.py)、
[输出](../scripts/check-unramified-class-jet-and-ramified-lifting.json)
的 28 项精确检查全部通过。它读取已发表 R276 的实际
本征函数证书，不修改该证书；新的全部嵌入、类群动作、
两个方向和完整矩都用整数/有限域算术重新构造。
没有新增目标素数或用有限样本推断跨 $p$ 的规律。

## 7. 留下的跨 $p$ 输入

由本篇可以把一条足够完成固定 E389 目标的路线准确写成：
对无穷多个合法 $p$，找到满足 (3)--(4) 的实际
$(F_p,q_p)$，使
$$
       \Theta_{1,F_p,q_p}\notin
          \ker\bigl(\mathbb F_p[\operatorname{Cl}(F_p)_{(p)}]
                                      \longrightarrow\mathbb F_p\bigr)^3.
\tag{48}
$$
一旦 (48) 成立，原 $\ell$ 的存在、$p$ 类群延拓分裂、
全部类群和、原非扭性及整个 Selmer 两步结论都由本文和
R271 给出，不再要求另外证明一个小高度联合筛。

但 (48) 仍需新的算术非零证明。一个固定 $F$ 只有有限个
$p\mid h_F$，所以这条最大阶路线必须让 $F$ 真正变化。
一个固定 $q$ 也只允许有限个
$p\mid a_q-\epsilon(q+1)$，故 $q$ 同样必须变化。
本文的 Kummer--Chebotarev 构造没有制造 (48)，只支付其后的
真实分歧提升。它既不把无穷辅助 $\ell$ 说成无穷目标 $p$，
也不把 $p$ 类群的存在当成其实际 theta 低项的非零。

## 输入与来源

- R234，尤其完整逐 CM 标签比较、同一度零 Hecke 规范和
  实际 definite 群环；R271，尤其真实延拓系数、全类群
  二阶忠实性和整个通常 Selmer 两步门。
- R276：判别式 $13$ 最大整环、其理想类数一、完整
  $\varphi_{13}\bmod11$ 唯一本征线及秩子式证书；
  本篇没有任选另一条 quaternion 本征向量。
- C. Cornut--D. Jetchev, *Liftings of reduction maps for quaternion
  algebras*, Bulletin of the London Mathematical Society **45**
  (2013), 370--386，Theorem 3.1、§4.10；
  [作者全文](https://webusers.imj-prg.fr/~christophe.cornut/papers/liftings.pdf)，
  [DOI](https://doi.org/10.1112/blms/bds098)。
  这里使用其保 conductor、Galois 等变的最优嵌入对应；
  具体方向、类标签和理想 isogeny 已由 (33)--(43) 完整给出。
- W. Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge Journal of Mathematics **2** (2014), 191--253，
  Theorem 2.1、§4.2；实际适用方式已在 R234 支付。

§3 的 Kummer 群作用、两个域交和具体 Frobenius 拼接均在
本文证明。没有调用新的未发表非零定理，也没有把
Heegner tensor resolvent 的增广阶界套到本篇的实际标量
level-raising theta。
