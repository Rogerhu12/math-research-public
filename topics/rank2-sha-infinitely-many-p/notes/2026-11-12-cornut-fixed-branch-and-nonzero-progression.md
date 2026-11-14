# 固定普通素数的指定 Mellin 分支与非零系数进程

日期：2026-11-12。本文把 Cornut 的已发表原始 Heegner 点迹定理，
接到固定映射的一个指定 tame 分支。这里证明的是该分支不恒为零，
以及固定特征零级数在一条固定整数进程上的系数最终非零；
没有把它升级为随输入素数变化的中心导数非零或增广原始性。

采用 [R105 的固定映射](2026-11-12-minus15-classgroup-trace-primitivity.md)
及 [固定普通 ST 比较](2026-11-12-fixed-ordinary-st-mellin-branch.md)
的精确坐标、实际 CM 点和 Amice 比较。后一篇负责本文 §1 列出的
几何输入；下面给出完整的全迹归纳与非零进程论证。

## 1. 固定数据与所用的 ST 输入

固定
$$
F=\mathbb Q(\sqrt{-15}),\qquad
E:y^2=x^3-17x,\qquad N=9248,
$$
及一次规范为 $\pi(\infty)=O$ 的有理模参数化
$\pi:X_0(N)\to E$。令
$$
\Phi=\pi\circ d_1+\pi\circ d_3:X_0(3N)\to E,
\qquad \Psi=[2]\circ\Phi.                         \tag{1}
$$
$d_1,d_3$ 是 R105 中的两条确定的退化映射。若 $P[c]$ 是
导子 $c$ 的相容原始 Heegner 点，$3\nmid c$，则相应
$X_0(3N)$ 点 $z_c$ 满足
$$
\Psi(z_c)=2(1+\tau_3)P[c].                       \tag{2}
$$
这里 $\tau_3$ 是阶二分歧理想的 Artin 元，实际等式保留全部
类群和，不是模挠点或除阶后的等式。

以后只用一个普通素数
$$
q=61.
$$
它不整除 $3N\cdot15$，在 $F$ 与 $\mathbb Q(i)$ 中均分裂；
在 $F$ 中还有
$$
61=N_{F/\mathbb Q}(1+2\sqrt{-15}),
\qquad a_{61}(E)=-12.                            \tag{3}
$$
点数计算及 CM 普通性已在 R107 核实。主理想事实还使
$61$ 上两个理想在 $\operatorname{Pic}(\mathcal O_F)$ 中均平凡。

在一个固定最大 CM 点 $c$ 的普通正式盘取相容的 Serre–Tate
坐标 $T$。固定的 CM Gauss–Manin 比值坐标记为 $v$，其一次
归一选定后不随系数指标改变。上述 ST 比较给
$$
v=\kappa_q\log(1+T),\qquad \kappa_q\ne0.          \tag{4}
$$
取
$$
F_c(v)=\log_E\Psi(t_c(v))=\sum_{m\ge1}b_mv^m,
\quad h_m=m!b_m,
$$
$$
\mathcal F(T)=F_c\bigl(\kappa_q\log(1+T)\bigr),
\quad D=(1+T)\frac d{dT},\quad G(T)=D\mathcal F(T).
                                                               \tag{5}
$$
式 (4)–(5) 是正式级数以及充分小盘中的恒等式。在
$T=\zeta_{q^n}-1$ 处，不能把 $\log\zeta_{q^n}=0$ 代回
$F_c$ 后宣称值为零：外层 $F_c$ 与这个复合展开的收敛域
不允许这样重排。该处的实际值始终由 $\log_E\Psi(c(T))$
的全盘原函数，或等价的 Amice 原函数核来定义。
由于 $\Psi(c)=O$，$\mathcal F(0)=0$。对相应完备局部系数环
$\mathcal O$，有 $G(T)\in\mathcal O[[T]]$，故存在有界
$\mathcal O$ 值测度 $\mu$，其 Amice 变换为 $G$。准确矩公式是
$$
\int_{\mathbb Z_q}x^{m-1}\,d\mu(x)=\kappa_q^m h_m
\qquad(m\ge1).                                  \tag{6}
$$
证明非零时只需要 $\kappa_q\ne0$，不把一个未指定周期当成
全局有理系数。

ST 几何比较还提供下列实际点识别：$T=\zeta_{q^n}^a-1$
（$a\in(\mathbb Z/q^n)^\times$）遍历一个固定最大 CM 点上方
的原始导子 $q^n$ CM 提升，且 (2) 与全部 $N$ 及 $3$ 层结构
一起运输。其作用是
$\ker(\operatorname{Pic}(\mathcal O_{q^n})\to
\operatorname{Pic}(\mathcal O_F))$ 的局部互反作用。
同时改变互反方向只把下面所有字符换成其逆，不影响非零结论。

以下使用的指定分支为
$$
M(W)=\int_{\mathbb Z_q^\times}
 x^{-1}(1+W)^{\log\langle x\rangle/\log(1+q)}\,d\mu(x)
 \in\mathcal O[[W]].                             \tag{7}
$$
注意积分核含完整的 $x^{-1}$；这是 tame 指数 $-1$ 的分支。
本文不是从“某个 tame 分支非零”推断 (7)。

## 2. Cornut 定理的准确范围

使用 Cornut（2002），*Mazur’s conjecture on higher Heegner points*，
Inventiones Mathematicae **148**, 495–523，
[作者提供的发表排版版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)，
DOI [10.1007/s002220100199](https://doi.org/10.1007/s002220100199)。

其引言主定理（上述 PDF 第 2 页）的输入是有理椭圆曲线及模参数化、
满足 Heegner 条件的虚二次域，以及一个不整除模曲线层数的素数。
结论是：把导子 $q^n$ 的原始 Heegner 点沿环类塔的有限部分取迹，
至少有一个 $n$ 得到非扭点。这里无“目标曲线无 CM”、残余表示
不可约或主点非扭的假设。普通性只出现在随后列举的 Iwasawa
推论中，不是这个非扭点定理的额外前提。

本文用 $\pi:X_0(N)\to E$ 应用定理，而不是把含分歧素数 $3$
的 $3N$ 误当成满足 Heegner 条件的新层数。之后再用 (2) 合并
两条确定的分支。该论文 §4.1 Lemma 4.2（PDF 第 23 页）
恰好给退化映射与分歧理想 Artin 作用的相容性。

设
$$
K_n=F[q^n],\quad K_0=F[1],\quad
K_\infty=\bigcup_{n\ge0}K_n,
$$
令 $H_\infty/F$ 是反圆分 $\mathbb Z_q$ 扩张，并令
$H_r/F$ 为其次数 $q^r$ 的子扩张。此处 $h_F=2$，而 $q$ 在
$F$ 中分裂，故对 $n\ge1$
$$
\operatorname{Gal}(K_n/F)
 \simeq\langle\tau_3\rangle\times(\mathbb Z/q^n)^\times,
\qquad
G_0=\operatorname{Gal}(K_\infty/H_\infty)
 \simeq C_2\times\mu_{q-1}.                       \tag{8}
$$
这也可从环类群正合列和 $\tau_3^2=1$ 直接得到；
$K_n\cap H_\infty=H_{n-1}$。定义实际整数点
$$
Z_0=\operatorname{Tr}_{K_0/F}P[1],\qquad
Z_n=\sum_{g\in G_0}gP[q^n]\in E(H_{n-1})
\quad(n\ge1).                                   \tag{9}
$$
对 $n\ge1$，$G_0$ 的作用忠实，和式恰为相应有限扩张的迹。
在 $n=0$，Cornut 的 $G_0$ 迹等于 $(q-1)Z_0$；这个重复因子
不影响扭性，但须在下一节的初始递推中保留。

Cornut 的主定理准确给
$$
\text{至少一个 }n\ge0\text{ 的上述全迹非扭。}       \tag{10}
$$
其 §4 Theorem A（PDF 第 22 页）甚至对 $G_0$ 的每个字符，
包括平凡字符，给出无限维的 Heegner 点张成空间。本篇只用 (10)，
也不需要该文模另一个辅助素数的 Theorem B 所附连通核条件。

## 3. 原始迹递推的两个初层

首先
$$
Z_0\in E(F)_{\rm tors}.                          \tag{11}
$$
若它非扭，Gross–Zagier–Kolyvagin 的原始 Heegner 点定理会给
$\operatorname{rank}E(F)=1$，与已有两个独立有理点矛盾。
这一步不假设 $\Sha$ 有限。R107 进一步证明
$E(F^{\rm ab})_{\rm tors}=E[2]$，故 $2Z_0=O$，与 (5) 的
原点规范相符。

记 $a=a_q(E)$。由于 $q$ 分裂且其两个理想都主，初始 Hecke
分布式给
$$
Z_1=(a-2)Z_0.                                    \tag{12}
$$
对 $n=2$ 和 $n\ge3$，准确递推分别为
$$
\operatorname{Tr}_{H_1/F}Z_2
 =a Z_1-(q-1)Z_0,                                \tag{13}
$$
$$
\operatorname{Tr}_{H_{n-1}/H_{n-2}}Z_n
 =a Z_{n-1}-Z_{n-2}\qquad(n\ge3).                \tag{14}
$$

这些等式可直接由 $q$ 次 Hecke 对应证明。最大阶的 CM 点有
两条水平分支，分别对应 $q$ 上两个理想，其余 $q-1$ 条分支
是导子 $q$ 的一个环类轨道。因此
$\operatorname{Tr}_{K_1/K_0}P[q]=(a-\sigma_{\mathfrak q}
-\sigma_{\bar{\mathfrak q}})P[1]$；主理想使两个 Artin 元
在 $K_0$ 上均为一，给 (12)。

导子 $q^{n-1}$、$n\ge2$ 的点有一条回到前层的分支及 $q$
条去下一层的分支，因此
$$
\operatorname{Tr}_{K_n/K_{n-1}}P[q^n]
 =aP[q^{n-1}]-P[q^{n-2}].                        \tag{15}
$$
对 $G_0$ 求和即得 (13)–(14)。在 $n=2$ 时，$P[1]$ 被 tame
群固定，所以该项成为 $(q-1)Z_0$；以后没有这个重复。
这些是原始点的关系，没有把单位根稳定化后的点混入。
模参数化的规范 $\pi(\infty)=O$ 保证 Hecke 关系没有额外尖点常数。

## 4. 指定分支不恒为零

**命题。** (7) 的 $M(W)$ 非零。

对一个 conductor 恰为 $q^n$、tame 部分平凡的乘法字符 $\psi$，
$n\ge2$，ST–Amice 比较中的原始 Gauss 和式为
$$
\sum_{a\in(\mathbb Z/q^n)^\times}\psi^{-1}(a)
 \mathcal F(\zeta_{q^n}^a-1)
 =\tau(\psi^{-1})
   \int_{\mathbb Z_q^\times}x^{-1}\psi(x)\,d\mu(x).
                                                               \tag{16}
$$
这里 $\tau(\psi^{-1})\ne0$。从原函数而非导数取 Gauss 和，
正是积分核 $x^{-1}$ 的来源；$q\mathbb Z_q$ 的部分被原始
Gauss 和消掉，$x=0$ 的原函数极限项也不贡献。

假设 $M\equiv0$。则 (16) 的右侧对所有上述 $\psi$ 为零。
用实际点识别 (2)，在一个固定 $q$ 进嵌入下，左侧是
$$
2\sum_{\gamma\in\operatorname{Gal}(H_{n-1}/F)}
 \psi^{-1}(\gamma)\log_E(\gamma Z_n).             \tag{17}
$$
一次固定互反或根单位规范最多改变非零 Gauss 标量，不能改变
所有原始字符和为零的结论。特别地，(17) 保留了 tame 和
类群的**全部**求和；没有用单个原始点的非扭性替代指定迹。

令 $\Gamma_n=\operatorname{Gal}(H_{n-1}/F)$，
$J_n=\operatorname{Gal}(H_{n-1}/H_{n-2})$，并置
$N_n=\sum_{g\in J_n}g$，$n\ge2$。字符正交性给
$$
q-N_n
 =q\sum_{\substack{\chi\in\widehat\Gamma_n\\
                   \chi|_{J_n}\ne1}} e_\chi,
\qquad
e_\chi=\frac1{|\Gamma_n|}\sum_{g\in\Gamma_n}\chi^{-1}(g)g.
                                                               \tag{18}
$$
$\Gamma_n$ 是阶 $q^{n-1}$ 的循环群，故 (18) 中的字符正好是
conductor $q^n$ 的原始 wild 字符。(17) 对所有这些字符为零，
遂有
$$
\log_E\bigl((q-N_n)Z_n\bigr)=0.                  \tag{19}
$$
关键是 $(q-N_n)Z_n$ 是一个真正的整数点，不是一个系数在
$\mathbb Q_q$ 中任意变化的 Mordell–Weil 张量向量。

对有限 $q$ 进扩张中的椭圆曲线点，$\log_E R=0$ 蕴含 $R$
为扭点：先乘一个整数进入足够小的正式群开子群，再用正式对数
在该子群上的注入性。每个 (19) 中的点均在有限扩张中，故
$(q-N_n)Z_n$ 为扭点。

现在归纳。由 (11)–(12)，$Z_0,Z_1$ 都为扭点；由 (13)，
$N_2Z_2$ 为扭点，再加 (19) 得 $qZ_2$、从而 $Z_2$ 为扭点。
若前两层已为扭点，(14) 给 $N_nZ_n$ 为扭点，(19) 再给
$Z_n$ 为扭点。因此所有 (9) 的全迹都为扭点，违背 (10)。
命题得证。

这个证明未使用
$E(H_r)\otimes\mathbb Q_q\to\mathbb C_q$ 的注入性；
该映射一般不能作为注入使用。也未把 imprimitive 字符的零 Gauss
和当成旧层消失：旧层由 (12)–(14) 及整数投影逐层处理。

## 5. 固定系数在一条固定进程上最终非零

**一般引理。** 设 $q$ 为奇素数，$\mu$ 是有界的整值测度，
并令 (7) 的 $M\ne0$。则存在整数 $k\ge0$ 与 $m_0$，使
$$
m\ge m_0,\qquad (q-1)q^k\mid m
\quad\Longrightarrow\quad
\int_{\mathbb Z_q}x^{m-1}\,d\mu(x)\ne0.          \tag{20}
$$

证明。写
$$
M(W)=A_dW^d+A_{d+1}W^{d+1}+\cdots,
\qquad A_d\ne0,\quad a=v_q(A_d)\ge0.
$$
取整数 $k$ 使 $k+1>a$。对于 $q^k\mid m$，置
$W_m=(1+q)^m-1$，则
$$
v_q(W_m)=1+v_q(m)\ge k+1.
$$
由于所有 $A_j$ 整，首项严格支配其余项，故
$$
v_q M(W_m)=a+d\bigl(1+v_q(m)\bigr).              \tag{21}
$$
这里仅用了幂级数的逐项赋值比较，系数域可以是固定的完备
$q$ 进扩域，不需先调用离散赋值环上的 Weierstrass 分解。

若再有 $q-1\mid m$，则 $\omega(x)^m=1$，因此
$$
\int_{\mathbb Z_q^\times}x^{m-1}\,d\mu(x)=M(W_m).
                                                               \tag{22}
$$
另一方面，测度有界且整，给
$$
v_q\left(\int_{q\mathbb Z_q}x^{m-1}\,d\mu(x)\right)
 \ge m-1.                                       \tag{23}
$$
由 $v_q(m)\le\log_q m$，充分大的 $m$ 满足
$$
m-1>a+d(1+\log_q m).
$$
于是 (22) 与 (23) 的赋值不同，不能抵消，得到 (20)。
若原测度只是有界而非整，先乘一个固定非零标量即回到上述情形。

应用 §4 的命题及准确矩公式 (6)，得到固定整数
$$
C=60\cdot61^k
$$
和固定 $m_0$，使
$$
m\ge m_0,\quad C\mid m
\quad\Longrightarrow\quad
h_m=m!b_m\ne0.                                  \tag{24}
$$
这个 $C$ 只依赖固定映射、固定 CM 点、坐标和 $q=61$；
不随之后研究的输入素数或辅助素数改变。
不需要知道 $d$ 或 $a$ 的数值，也不要求 $d\le1$。

### 5.1 有限个实际 CM 中心的统一进程

可把所需中心集明确包含在下列固定集合 $\Sigma$ 中。
对 $F$ 的两个理想类，分别取最大阶 CM 椭圆曲线；在 $2$ 与
$17$ 处各选择一个分裂素理想方向，以其 $2^5$ 和 $17^2$
核给循环 $N$ 层结构；$3$ 部分取唯一分歧理想的核。
这给 $X_0(3N)$ 上 $h_F\cdot2^2=8$ 个最大阶 CM 点。
实际固定 Heegner 方向及其 Galois 共轭只需其中一个子集。
所有这些点及所选代数参数、CM de Rham 基均可放进同一个
固定数域。

对每一种 $N$ 理想方向，$\tau_3$ 仍交换那两个理想类，
所以 $\Phi(c)$ 是该方向的原始类群全迹。若该迹非扭，
同样由 Gross–Zagier–Kolyvagin 得 $\operatorname{rank}E(F)=1$，
矛盾；R107 因而给 $\Psi(c)=O$。在 $q=61$ 处每个中心都有
同一类型的普通 ST 盘，§1 的构造逐个适用。

Cornut 的定理适用于每一个固定的 Heegner 理想方向；同一方向的
两个中心则是实际家族的 Galois 共轭。因而 §§2–4 分别证明
每个 $c\in\Sigma$ 的指定 $M_c(W)$ 非零，不是从一个中心的
局部值在未知嵌入下非零推断其他中心。

分别取 §5 的 $k_c,m_{0,c}$，再令
$$
k_* =\max_{c\in\Sigma}k_c,\qquad
C=60\cdot61^{k_*},\qquad
m_* =\max_{c\in\Sigma}m_{0,c}.
$$
便得到完全统一的结论
$$
c\in\Sigma,\quad m\ge m_*,\quad C\mid m
\quad\Longrightarrow\quad h_{c,m}\ne0.             \tag{25}
$$
因此后续乘积公式可先固定这八个中心及同一个 $C$，再让输入
素数与辅助素数变化；没有随素位重新选择未知中心的量词问题。

## 6. 供全局产品估计使用的准确接口

(24) 是特征零代数系数的非零性；由于 $\kappa_q\ne0$，
局部矩非零确实推出原固定 $h_m$ 非零。若另有 $h_m$ 的
固定数域定义、分母控制和高度上界，可对这些非零数作乘积公式。
本文没有从一个 $q$ 的非零性推断任何别的素数处为单位。

特别地，当前实际 Kolyvagin 点还需要先控制其 prime-to-$p$
迹 $Q_\ell$，再控制 $\Delta$ 增广商中的指定类。
即使全局系数产品论证最终推出 $Q_\ell\ne O$，也不能省略
后一个原始性步骤。Cornut 的固定塔非扭性在这里仅用于证明
一个固定分析分支不恒为零，没有替代随 $p$ 的中心证书。

## 来源与内部输入

- C. Cornut（2002），*Mazur’s conjecture on higher Heegner points*，
  Invent. Math. **148**, 495–523，DOI 10.1007/s002220100199。
  [作者发表排版版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)：
  PDF 第 2 页主定理；§4 Theorem A，PDF 第 22 页；
  §4.1 Lemma 4.2，PDF 第 23 页。
- [R105 的固定类群和映射](2026-11-12-minus15-classgroup-trace-primitivity.md)：
  $\tau_3^2=1$、两退化映射和及 (2)。
- [R107 的实际挠群与点数](2026-11-12-heegner-orbits-and-logarithmic-augmentation-depth.md)：
  $E(F^{\rm ab})_{\rm tors}=E[2]$、$a_{61}=-12$。
- [固定普通 ST/Mellin 比较](2026-11-12-fixed-ordinary-st-mellin-branch.md)：
  同一正式盘中的 CM 点、周期比、Amice 测度与原始 Gauss 求和。
