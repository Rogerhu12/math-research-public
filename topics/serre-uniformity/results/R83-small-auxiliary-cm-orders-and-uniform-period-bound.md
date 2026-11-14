# R83：小辅助 CM 序、球面装填与统一三次周期界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，根会话已逐节独立复核。** 本文给出对所有虚二次底域和变化环类导子均适用的显式非消失判据：
$$
\boxed{p\ge\frac{2M}{h(\mathcal O)^{1/4}}
\quad\Longrightarrow\quad P_\eta\ne0.}
$$
证明使用真实 Brandt 理想类，而非极大序的 type 数；允许辅助二次序的判别式被 $p$ 整除。它不限于某个固定 $M/p$ 区间或有限素数表。结合 Siegel 下界可得 $p\gg_\epsilon M^{7/8+\epsilon}$ 的无条件但常数无效的推论；显式类数判据本身没有这个无效性。

此结果仍是非消失的充分范围及变化导子的必要下界，不给 $M$ 上界，不排除 exceptional 素数，也不完成 Serre 一致性。

## 1. 设定与主定理

设 $\mathcal O$ 是虚二次域 $K$ 中的序，判别式为 $-M$，记
$$h=h(\mathcal O)=|\operatorname{Pic}(\mathcal O)|.$$
设 $p>3$，$p\nmid M$，且 $p$ 在 $K$ 惰性。取
$$B=B_{p,\infty},\qquad R\cap K=\mathcal O,$$
其中 $R$ 为极大序。令 $\eta:\operatorname{Pic}(\mathcal O)\to\mu_3$ 为阶恰为 $3$ 的字符，并沿用
$$
\varphi([\mathfrak a])=[\mathfrak aR],\qquad
P_\eta=\sum_{[\mathfrak a]}\eta(\mathfrak a)^{-1}[\varphi(\mathfrak a)].
\tag{83.1}
$$
周期层面的结论不要求 $\eta$ 原始；接 $L$ 值时会明确加上原始性。

**定理 83.1。** 如果 $P_\eta=0$，则 $r=M/p>1$，并有
$$
\boxed{
h<16r\lfloor r\rfloor^3\le16r^4.
}
\tag{83.2}
$$
因此下列任一显式条件保证 $P_\eta\ne0$：
$$
p\ge M;
\qquad
1<r=M/p,\quad h\ge16r\lfloor r\rfloor^3;
\qquad
\boxed{p\ge2M/h^{1/4}.}
\tag{83.3}
$$
这里未假设 $p\equiv2\pmod3$。

**推论 83.2。** 若 $\eta$ 是准确导子 $c$ 的原始三次环类字符，$\mathcal O=\mathbb Z+c\mathcal O_K$、$M=|D_K|c^2$，则在 (83.3) 的任一范围内，存在权 $2$、水平 $p$、平凡 nebentype 的新形式 $g$，满足
$$
L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.
\tag{83.4}
$$
使用 R76 §6 核准的已发表 Cai–Shu–Tian 公式。这个推论的常数 $2$ 不依赖 $K,c$ 或 $\eta$。

## 2. 三点碰撞给一个判别式小的辅助序

R76 §2 的理想证明将同一 $\varphi$ 纤维中的不同类注入到同一极大序 $S$ 的最优嵌入共轭类；它们在 $p$ 处具有相同取向。令
$$
\omega_i=\iota_i\!\left(\frac{t+\sqrt{-M}}2\right),\qquad
v_i=\omega_i-t/2.
$$
则
$$
\operatorname N(v_i)=M/4,\qquad
\omega_i-\omega_j\in\mathfrak P,\qquad
\mathfrak P^2=pS,
\tag{83.5}
$$
其中 $\mathfrak P$ 是 $S$ 的 $p$ 两边素理想。不同类的点不相等。

若 $r<1$，正的差范数不可能既是 $p$ 的倍数又不超过 $M$，所以每个纤维至多一个类，$P_\eta$ 不会为零。$r=1$ 与 $p\nmid M$ 不相容。以下只考虑 $r>1$，并记
$$s=\lfloor r\rfloor.$$

若 $P_\eta=0$，每个非空纤维的三种颜色数量相等，故至少有三个类。任选三个相应的点 $\omega_0,\omega_1,\omega_2$，置
$$a=\omega_1-\omega_0,\qquad b=\omega_2-\omega_0.$$
写
$$
\operatorname N(a)=kp,\quad
\operatorname N(b)=lp,\quad
\operatorname N(a-b)=mp,
\qquad1\le k,l,m\le s.
\tag{83.6}
$$
三个纯部在同一球面上且不同，故不共线，$a,b$ 线性独立。由 (83.5)，
$$
\beta=-ab/p\in S,\qquad
\operatorname N(\beta)=kl,\qquad
\operatorname{Tr}(\beta)=k+l-m.
\tag{83.7}
$$
因 $a,b$ 不平行，$\beta$ 不是标量。因此 $\mathbb Q(\beta)$ 为虚二次域，而 $\mathbb Z[\beta]$ 的判别式为 $-d$，其中
$$
\begin{aligned}
d&=4kl-(k+l-m)^2\\
 &=2(kl+lm+mk)-(k^2+l^2+m^2)>0.
\end{aligned}
$$
用
$$k^2+l^2+m^2\ge(k+l+m)^2/3$$
得
$$
\boxed{0<d\le(k+l+m)^2/3\le3s^2.}
\tag{83.8}
$$

令
$$
\mathcal A=S\cap\mathbb Q(\beta).
$$
这是一个最优嵌入于 $S$ 的虚二次序，包含 $\mathbb Z[\beta]$。若 $u=[\mathcal A:\mathbb Z[\beta]]$，则
$$
|\operatorname{disc}(\mathcal A)|=d/u^2\le3s^2.
\tag{83.9}
$$
所以：

> 若周期消失，每一个被 CM 类占用的 Brandt 类，其左序都含有某个绝对判别式不超过 $3s^2$ 的最优虚二次序。

这个辅助序一般不同于原来的 $\mathcal O$，也可能有不同的分数域。不能用原底域的类数取代这些辅助序的类数。

## 3. 一个辅助序至多占用 $2h(\mathcal A)$ 个 Brandt 类

**引理 83.3。** 给定任意虚二次序 $\mathcal A$，令 $n_R(\mathcal A)$ 为 $\mathrm{Cls}(R)$ 中左序容许 $\mathcal A$ 最优嵌入的右理想类数。则
$$
\boxed{n_R(\mathcal A)\le2h(\mathcal A).}
\tag{83.10}
$$
若 $p$ 整除 $\mathcal A$ 的导子，则 $n_R(\mathcal A)=0$。若 $p$ 在其分数域分歧，则更有 $n_R(\mathcal A)\le h(\mathcal A)$。这些结论包含 $p=2$ 以外的所有局部判别式情形；本文的原始 $p$ 已假定大于 $3$。

### 3.1 改换基准序及固定嵌入

若没有这样的理想类，结论平凡。否则选一个含最优 $\mathcal A$ 的极大序 $S_0$，固定其分数域 $F\subset B$。如 R80 §3.3，用可逆 $(S_0,R)$ 双模理想可将两个右理想类集合双射，同时保持左序及最优嵌入问题。因此只需对右 $S_0$ 理想计数。

给定一个容许该嵌入的理想类，Skolem–Noether 使我们可左乘 $B^\times$，将嵌入改成固定的 $F\subset B$。于是其代表 $J$ 满足
$$
\mathcal A J\subset J,\qquad
\mathcal O_L(J)\cap F=\mathcal A.
\tag{83.11}
$$

### 3.2 $q\ne p$：最优性固定唯一局部环面轨道

在 $B_q\simeq M_2(\mathbb Q_q)$ 中，右极大序理想等价于二维 $\mathbb Z_q$ 格。把 $\mathbb Q_q^2$ 识别为 $F_q$ 的正则模；左序与 $F_q$ 的交就是该格的乘子环。

我们需要以下局部事实：

> 一个 $F_q$ 中的满秩 $\mathbb Z_q$ 格，在 $F_q^\times$ 缩放下由其乘子二次序唯一确定。

若 $F_q$ 是域，取格中赋值最小的非零元素并除以它，便得到
$$1\in\Lambda\subset\mathcal O_{F_q}.$$
取整数环基 $1,\theta$。第二坐标的像为 $q^e\mathbb Z_q$；从一个第二坐标为 $q^e$ 的格向量减去整数倍的 $1$，得到 $q^e\theta\in\Lambda$，于是
$$
\Lambda=\mathbb Z_q+q^e\mathbb Z_q\theta.
$$
这个格本身为序，且因含 $1$，乘子环恰为它自身。

若 $F_q=\mathbb Q_q\times\mathbb Q_q$，先分别缩放两个坐标，使格包含于 $\mathbb Z_q^2$ 且两个投影均满。其模 $q$ 像中存在两个坐标皆非零的向量：若像为直线，两个投影满强迫该向量存在；若为整个平面，取 $(1,1)$。这一论证在 $q=2$ 也有效。再除以一个对应的格向量，可令 $(1,1)\in\Lambda$。沿对角线取商后，同样得到
$$\Lambda=\mathbb Z_q+q^e\mathcal O_{F_q}.$$
其乘子环仍等于这个序。

将此事实用于基准格和 $J_q$ 对应的格，最优条件 (83.11) 使它们的乘子环都为 $\mathcal A_q$，因此
$$
J_q=t_qS_{0,q},\qquad t_q\in F_q^\times
\quad(q\ne p).
\tag{83.12}
$$
没有假定 $\mathcal A_q$ 为极大序，故这覆盖辅助导子的全部素因子。

### 3.3 $p$ 处：导子、分歧及两个取向

$B_p$ 是除法代数，因此 $F_p$ 不能分裂。其唯一极大序与 $F_p$ 的交为 $\mathcal O_{F_p}$：两者的整性由相同的延拓赋值判断。因此最优嵌入强迫
$$\mathcal A_p=\mathcal O_{F_p}.$$
这证明 $p$ 整除 $\mathcal A$ 的导子时没有最优嵌入。

局部右理想都形如 $\Pi^nS_{0,p}$，其中 $\Pi$ 的 reduced norm 赋值为 $1$。

- 若 $F_p/\mathbb Q_p$ 不分歧，$F_p^\times$ 的范数赋值为偶数。因此可写
  $$J_p=t_p\mathfrak P_{0,p}^{\,e},\qquad e\in\{0,1\}.$$
- 若 $F_p/\mathbb Q_p$ 分歧，一个 $F_p$ 均匀元的范数赋值为 $1$，所以每个 $\Pi^nS_{0,p}$ 已能写为 $t_pS_{0,p}$，只需 $e=0$。

这里 $\mathfrak P_0$ 为全局 $p$ 两边素理想。把 (83.12) 与 $p$ 处的 $t_p$ 拼合，得到某个局部主的可逆 proper $\mathcal A$ 理想 $\mathfrak a$，使
$$
J=\mathfrak a\mathfrak P_0^{\,e}.
\tag{83.13}
$$
因此至多有 $h(\mathcal A)$ 乘以两个 $p$ 取向的右理想类。这是 (83.10)。在分歧情形只有一个取向，得加强。

本证明给的是覆盖所有所需 **右理想类** 的上界，并未从左序共轭类数直接代换。与 R80 的特殊 $\mathcal A=\mathcal O_{-7}$ 不同，这里不要求 $\mathfrak P_0$ 主，也不把两个取向擅自合一。

## 4. 所有小判别式序的类数总和

**引理 83.4。** 对任意实数 $Y>0$，
$$
\sum_{\substack{0<d\le Y\\-d\ \mathrm{为二次序判别式}}}
h(-d)
\le\frac{2Y}{3}\left\lfloor\sqrt{\frac Y3}\right\rfloor
\le\frac{2Y^{3/2}}{3\sqrt3}.
\tag{83.14}
$$

每个 proper 理想类可由一个 primitive 正定约化二元型 $(a,b,c)$ 表示，并可选
$$-a<b\le a\le c.$$
其判别式绝对值
$$d=4ac-b^2\ge4ac-a^2\ge3ac.$$
若 $d\le Y$，则
$$
1\le a\le\sqrt{Y/3},\qquad
1\le c\le Y/(3a).
$$
对给定 $a$，有至多 $2a$ 个整数 $b$，以及至多 $\lfloor Y/(3a)\rfloor$ 个整数 $c$，故此 $a$ 的总数不超过 $2Y/3$。再对 $a$ 求和得 (83.14)。

我们计数时容许不 primitive 的型、可能不满足约化边界唯一性者及不存在对应判别式者，均只会增大上界。这是对所有判别式的有限**完整计数证明**，不需要任何类数表或渐近公式。

取 $Y=3s^2$，得到
$$
\boxed{\sum_{0<d\le3s^2}h(-d)\le2s^3.}
\tag{83.15}
$$
由第 2 节及引理 83.3，如果 $P_\eta=0$，被 $\varphi$ 占用的 Brandt 类数因此满足
$$
\boxed{\#\operatorname{im}\varphi\le4s^3.}
\tag{83.16}
$$
同一个 Brandt 类可能含很多辅助序；这里取并集上界，不要求为每个像类指定唯一辅助序。

## 5. 每个纤维的球面装填界

同一纤维的点 $v_i$ 在半径
$$R_0=\sqrt M/2$$
的实三维球面上，由 (83.5) 两点弦长至少 $\sqrt p$。其球心角至少
$$\theta=2\arcsin\sqrt{p/M}.$$
以各点为中心、球心角半径 $\theta/2$ 的开球面帽两两不交。每个帽面积为
$$
2\pi R_0^2\left(1-\sqrt{1-p/M}\right).
$$
球面总面积为 $4\pi R_0^2$，故纤维大小 $n$ 满足
$$
\begin{aligned}
n&\le\frac{2}{1-\sqrt{1-1/r}}\\
 &=2r\left(1+\sqrt{1-1/r}\right)
 <4r.
\end{aligned}
\tag{83.17}
$$
边界上的相切不影响面积不等式。这里使用每个理想类选出的不相同嵌入点，R76 的注入保证没有把一个点重复计为几个类。

把 (83.16) 与 (83.17) 相乘，
$$
h=\sum_{x\in\operatorname{im}\varphi}|\varphi^{-1}(x)|
<4r\cdot4s^3
=16r\lfloor r\rfloor^3.
$$
这证明定理 83.1。若 $p\ge2M/h^{1/4}$，就有 $h\ge16r^4$，与 (83.2) 矛盾。

## 6. 从非零周期到中心值

若 $\eta$ 原始，$P_\eta$ 次数为零。R76 §6 中的素水平 Brandt 模谱分解及 Cai–Shu–Tian Theorem 1.2 给
$$
P_\eta\ne0
\quad\Longrightarrow\quad
\exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.
$$
所需条件仍是 $p$ 惰性、$p\nmid|D_K|c$、原始环类字符以及权 $2$；辅助序 $\mathcal A$ 只用于计数，不是这条 $L$ 函数的 CM 域或字符。不能在公式中把 $K,\eta$ 替换成辅助对象。

这证明推论 83.2。R83 不使用未发表稿件中的非消失结论，也不需要 GRH。

### 6.1 与 $M<3p$ 的关系

R81 在 $p>37$、$p\equiv2\pmod3$ 的三次字符情形给明确范围 $M<3p$。本篇的阈值是
$$p\ge2M/h^{1/4}.$$
当 $h\ge6^4=1296$ 时，该阈值不大于 $M/3$，开始覆盖 $M\ge3p$ 的新范围。类数较小时，R81 的三点特殊结构可能更强；两者是不同的已证充分条件。

## 7. 指数 $7/8+\epsilon$：量词和无效性

经典 Siegel 下界为：对每个 $\delta>0$，存在正数 $a_\delta$，使任意虚二次基本判别式 $-D$ 满足
$$h_K\ge a_\delta D^{1/2-\delta}.$$
这个常数一般不可有效计算。此输入的使用方式也见 Michel–Ramakrishnan 已发表工作的 §4；本篇只有本节使用它。

另一方面，对每个 $\delta>0$，存在可有效给出的 $b_\delta>0$，使
$$\phi(c)\ge b_\delta c^{1-\delta}.$$
具体取
$$
b_\delta=\prod_{\substack{q\ \mathrm{素数}\\q\le2^{1/\delta}}}(1-1/q)>0.
$$
对其余素数有 $1-1/q\ge1/2>q^{-\delta}$，所以
$$
\phi(c)/c=\prod_{q\mid c}(1-1/q)
\ge b_\delta\prod_{\substack{q\mid c\\q>2^{1/\delta}}}q^{-\delta}
\ge b_\delta c^{-\delta}.
$$
序类数公式和单位指数至多为 $3$ 给
$$
h(\mathcal O_c)
\ge\frac13h_K\phi(c)
\ge\frac13a_\delta b_\delta D^{1/2-\delta}c^{1-\delta}
\ge\frac13a_\delta b_\delta M^{1/2-\delta}.
\tag{83.18}
$$
因而对每个 $\epsilon>0$，取 $\delta=4\epsilon$（只需小正 $\epsilon$ 的情形），存在 $C_\epsilon>0$，使
$$
\boxed{
p\ge C_\epsilon M^{7/8+\epsilon}
\quad\Longrightarrow\quad
\exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.
}
\tag{83.19}
$$
量词对 $K,c,\eta$ 全部统一；$C_\epsilon$ 一般无效，来自 Siegel 下界，不是 GRH 条件。

相反，(83.3) 中的 $h(\mathcal O)$ 可用约化二元型精确计算，且常数就是 $2$，所以**定理 83.1 和推论 83.2 的类数版本完全有效**。不能将 (83.19) 的常数无效性倒灌到这个显式判据。

## 8. 对实际异常分支的必要条件

在 R66 的实际小惯性分支中，三次字符确为原始，故本篇的非零中心值可接 R69 的实际秩零商及 R72 的尖点排除。

如果某个 $F/\mathbb Q$ 满足 $F[p]\simeq E[p]$，并有一个非 exceptional 的 $j(F)$ 分母素数，则所有相关中心值必须为零；否则 R72 立即矛盾。因此，除 R81 的 $M>3p$ 外，还必须满足
$$
\boxed{
h(\mathcal O_{c_\eta})
<16\frac Mp\left\lfloor\frac Mp\right\rfloor^3
\le16\left(\frac Mp\right)^4,
}
\tag{83.20}
$$
特别
$$
\boxed{p<\frac{2M}{h(\mathcal O_{c_\eta})^{1/4}}.}
\tag{83.21}
$$
使用 (83.18) 后可改写成接近 $M\gg p^{8/7}$ 的无效必要下界；它依然不是 $M$ 的上界。

本篇不能处理所有分母均 exceptional 的情形，不能证明三次商导子受 $p$ 的统一上界控制，也不能把辅助序判别式小误读为原商域判别式小。

## 9. 文献比较与来源

Michel–Ramakrishnan 的已发表 Theorem 2 在其**奇基本判别式**及普通理想类字符设置中给 $p\gg_\delta D^{1/2+\delta}$。该设置的环类导子是 $1$，不覆盖本题类数一底域上必然分歧的三次字符。其证明对照说明，指数 $7/8$ 不是所有特殊情形中最强的已知结论；本篇的价值是对变化底域与变化环类导子给统一、显式的类数判据及完整初等几何证明。

Feigon–Whitehouse 的 Proposition 4.20 与 Lemma 6.7 还可对**固定底域**、变化字符导子比较正主项和 regular 误差；相关常数明确依赖底域。这一不同量词的解析接口另行展开，不在本篇把它声称为统一于变化 $K$ 的平方根阈值。

- [R76](R76-three-point-fibres-and-cubic-nonvanishing.md)：同取向嵌入、差的 $\mathfrak P$ 整性及非零周期接口。
- [R80](R80-three-colour-collapse-and-class-number-one-nonvanishing.md)：右理想类与取向问题。本篇引理 83.3 重新证明其一般计数版本，允许非极大辅助序及 $p$ 分歧。
- John Voight, *Quaternion Algebras*, GTM **288**, Springer, 2021，Chapter 42，尤其 Theorems 42.1.9、42.3.2 及 §42.2 的 $p$ 两边理想。[出版社全文](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)。本文的辅助序覆盖数由 §3 直接证明。
- L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, **Algebra & Number Theory 8** (2014), 2523–2572，Theorem 1.2。[原文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)。
- P. Michel, D. Ramakrishnan, *Consequences of the Gross–Zagier formulae: Stability of average L-values, subconvexity, and non-vanishing mod p*, in **Number Theory, Analysis and Geometry**, Springer, 2012, 437–459，Theorem 2、§4。[作者原文](https://www.its.caltech.edu/~dinakar/papers/Mi-Ra-SL-final.pdf)，[出版 DOI](https://doi.org/10.1007/978-1-4614-1260-1_20)。
- B. Feigon, D. Whitehouse, *Averages of central L-values of Hilbert modular forms with an application to subconvexity*, **Duke Math. J. 149** (2009), 347–410，Proposition 4.20、Lemma 6.7。[作者原文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，[DOI](https://doi.org/10.1215/00127094-2009-041)。

§§2–5 是本篇完整的独立证明。没有用有限计算代替关于所有判别式、所有导子或所有素数的量词。
