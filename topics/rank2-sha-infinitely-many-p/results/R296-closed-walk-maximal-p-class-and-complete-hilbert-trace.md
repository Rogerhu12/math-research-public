# R296：真实闭路、最大阶的 $p$ 阶理想类与全部 Hilbert trace

日期：2026-11-13。**状态：以下闭路与最大阶类群比较、全 88 标签的原 theta 计算及固定几何族已证明。没有证明新的无穷素数 Sha 有限性。**

本篇先在 R276 的同一个 $q=13$、层 $389$ 图上，把“一个 loop 重复，再作一次 excursion”变成一个实际 CM 类群轨道。该轨道的低矩不能直接代替原完整 Hilbert 和：在本文的实际例子中，一个 11-cycle 的三矩为 $(5,8,1)$，而全部八个 coset 的三矩为 $(0,0,9)$。

另一个完整结论是：同一固定闭路模板对每个素数 $p\equiv11\pmod{16296}$ 产生虚二次域 $F_p$，其**最大整环**中 $2$ 上的理想类阶恰为 $p$，且 $p$ 不分歧、$389$ 分裂、$13$ 惰性。这是几何和类群结论。固定 $q=13$ 对 E389 的 admissibility 只允许 $p=11,17$，所以不能将这个几何族当作原 E389 的无穷 level-raising 族。

## 1. 同一个原有限图与固定的闭路模板

曲线与最大四元数整环均严格使用 R276：
$$
E:y^2+y=x^3+x^2-2x,\qquad N_E=389,
$$
$$
\mathcal O=\mathbf Z\langle
1,\ i,\ (1+i+j)/2,\ (2+i+ij)/4\rangle,
\quad i^2=-2,\quad j^2=-13.
\tag{1}
$$
坐标写在 (1) 的四个整数基上。R276 已证明 $\mathcal O$ 最大、理想类数一且单位仅 $\{\pm1\}$。原有限 Shimura set 是
$$
X_{13}=\mathbf P^1(\mathbf F_{389}),\qquad |X_{13}|=390.
$$
三个范数二同源代表依次为
$$
A=(0,0,0,1),\qquad I=(0,1,0,0),\qquad \bar A=(1,0,0,-1).
\tag{2}
$$
以下用字母 $0,1,2$ 标记这三个边，逆边分别为 $2,1,0$。它们在原 $389$ 层的准确矩阵为
$$
M_0=\begin{pmatrix}297&0\\195&93\end{pmatrix},\quad
M_1=\begin{pmatrix}0&387\\1&0\end{pmatrix},\quad
M_2=\begin{pmatrix}93&0\\194&297\end{pmatrix}.
\tag{3}
$$
特别地，$0$ 是 $A$ 的真实 loop 节点。取长度十的 excursion
$$
\mathcal W=(1,0,1,0,1,0,0,0,0,1).
\tag{4}
$$
其实际节点序列为
$$
(0,389,205,148,191,334,199,207,203,389,0).
\tag{5}
$$
按同源的复合顺序相乘，得到
$$
B=(-6,-21,4,18),\qquad \operatorname{nrd}(B)=2^{10},
\qquad \operatorname{trd}(B)=10.
\tag{6}
$$
(4) 无相邻反向边，其首尾也能和 $A$ 的 loop 相接而不回退。

对任意素数 $p>10$，定义实际长度 $p$ 的闭路及其复合
$$
\mathcal C_p=0^{p-10}\mathcal W,
\qquad \alpha_p=B A^{p-10},
\qquad \operatorname{nrd}(\alpha_p)=2^p.
\tag{7}
$$
该闭路 cyclically nonbacktracking；因 $p$ 为素数而字中至少有两种边，它不是较短闭路的幂。其完整 $389$ 层结构在 (3)–(5) 中逐步运输，未只在无层的 supersingular 点集上闭合。

## 2. 闭路最初给哪个二次整环

写
$$
t_n=\operatorname{trd}(BA^n),\qquad
t_0=10,\quad t_1=-39,\quad t_{n+2}=t_{n+1}-2t_n.
\tag{8}
$$
最后的递推来自 $A^2=A-2$。令
$$
\Delta_p=t_{p-10}^2-2^{p+2}<0,\qquad
F_p=\mathbf Q(\alpha_p),\qquad
\mathcal O_p^{\rm opt}=F_p\cap\mathcal O.
\tag{9}
$$
判别式为负：正定四元数范数给严格不等式，等号会使 $\alpha_p$ 为有理数，而有理整数的范数是平方，不能等于 $2^p$。

已出版的 Arpin–Chen–Lauter–Scheidler–Stange–Tran，*Orientations and Cycles in Supersingular Isogeny Graphs*，Theorem 3.2、Lemmas 3.6–3.9，把无回退且非幂的长度 $p$ 闭路识别为一个 primitive oriented volcano rim。因此它首先给的是 $\mathcal O_p^{\rm opt}$ 中一个 $2$ 理想的精确阶 $p$。这里 $q=13$ 没有额外自同构，文中的额外单位歧义仅为 $\pm1$。

**不能因此直接把 $\mathcal O_p^{\rm opt}$ 写成 $\mathcal O_{F_p}$。** 下节用这个固定模板的额外整数恒等式，直接在最大阶中证明阶仍恰为 $p$；仍不宣称原嵌入本身总是最大阶嵌入。

## 3. 最大整环中 $2$ 理想阶恰为 $p$

由 (8)，$t_n$ 对 $n\ge1$ 恒为奇数，所以 $\Delta_p\equiv1\pmod8$。因此 $2$ 在 $F_p$ 分裂，且 $\mathbf Z[\alpha_p]$ 的 conductor 不被 $2$ 整除。令
$$
\mathfrak l_p=(2,\alpha_p)\subset\mathcal O_{F_p}.
$$
范数和奇 trace 给
$$
(\alpha_p)=\mathfrak l_p^p,
\qquad N\mathfrak l_p=2.
\tag{10}
$$
确实，$\alpha_p$ 在两个 $2$ 素位上不可能都具有正赋值；其范数为 $2^p$，故两赋值分别是 $p,0$。因此 $[\mathfrak l_p]$ 的阶为 $1$ 或 $p$。

若该理想主，$F_p$ 就含有范数二整数。此整数的 trace 只能为 $0,\pm1,\pm2$，相应二次域仅为 $\mathbf Q(\sqrt{-2})$、$\mathbf Q(\sqrt{-7})$、$\mathbf Q(i)$。由于 $2$ 已分裂，唯一可能是
$$
F_0=\mathbf Q(\sqrt{-7})=\mathbf Q(A).
\tag{11}
$$
下面完全排除 (11)。在 $F_0$ 中记 $A$ 的根为 $\pi$，故
$\pi^2-\pi+2=0$。$B$ 在该二次子空间的 trace 投影为
$$
B_\parallel=\frac{-9+88A}{7},\qquad
\operatorname{trd}(BA^n)
=\operatorname{Tr}_{F_0/\mathbf Q}(B_\parallel\pi^n).
\tag{12}
$$
这是由 $\operatorname{trd}(B)=10$、$\operatorname{trd}(BA)=-39$ 解出的准确等式，亦可直接以 (8) 验证全部 $n$。

若 $F_p=F_0$，由 (10) 及 $F_0$ 的单位 $\{\pm1\}$，必有
$$
t_{p-10}=\pm\operatorname{Tr}(\pi^p).
$$
设 $n=p-10$，相应地置
$$
N_\pm=-9+88\pi\mp7\pi^{10}.
$$
这迫使
$$
N_\pm\pi^n+\overline{N_\pm}\bar\pi^n=0.
\tag{13}
$$
准确计算为
$$
\pi^{10}=34-11\pi,\qquad
N_+=-247+165\pi,\quad N_-=229+11\pi,
$$
$$
N(N_+)=74704=2^4\cdot4669,
\qquad N(N_-)=55202=2\cdot27601.
\tag{14}
$$
两分子的常数项均奇，所以在 $(\pi)$ 上赋值为零。对 (13) 比较 $(\pi)$ 赋值，正号情形只能有 $n=4$、负号情形只能有 $n=1$。前者给 $p=14$，不是素数；后者给 $p=11$，但
$$
t_1=-39\ne-67=-\operatorname{Tr}(\pi^{11}).
$$
故 (11) 对所有素数 $p>10$ 都不成立。结论为
$$
\boxed{\quad \operatorname{ord}_{\operatorname{Cl}(F_p)}
                 [\mathfrak l_p]=p.\quad}
\tag{15}
$$
这一步不依赖 $\Delta_p$ 是否平方自由，也不依赖 $\mathcal O_p^{\rm opt}$ 是否最大。

## 4. 一个无穷几何子族的全部局部条件

现在限制
$$
\boxed{\quad p\equiv11\pmod{16296},\qquad
16296=\operatorname{lcm}(168,388).\quad}
\tag{16}
$$
该互素等差类含无穷素数，例如由固定 cyclotomic 域中的 Chebotarev 得到。

在 $13$ 处，$\mathcal O$ 的剩余域为 $\mathbf F_{13}[i]$、$i^2=-2$。其实际约化是
$$
(a,b,c,d)\longmapsto
(a+7c+7d)+(b+7c+10d)i.
\tag{17}
$$
$A$ 的剩余元为单位，其阶整除 $168$；而 (3) 给 $M_0^{388}=1$。因此 (16) 使 $\alpha_p$ 的这两种 trace/discriminant 约化与 $p=11$ 完全相同。此时
$$
\alpha_{11}=(-36,-13,21,12),\qquad
\Delta_{11}=-6671,
$$
$$
\Delta_p\equiv11\pmod{13},\qquad
\Delta_p\equiv331=135^2\not\equiv0\pmod{389}.
\tag{18}
$$
故 $13$ 在 $F_p$ 惰性，$389$ 分裂，且其两特征线不同。

还须保 $p\nmid\operatorname{disc}F_p$，这不能由 (18) 省略。由于 (16) 给 $p\equiv4\pmod7$，$-7$ 是模 $p$ 的平方。于是 $A^p\equiv A\pmod p$，且
$$
\operatorname{trd}(BA^{p-10})
\equiv\operatorname{trd}(BA^{-9})
=\frac{-1546}{1024}\pmod p.
$$
结合 $2^p\equiv2$，得到
$$
\Delta_p\equiv
\frac{(-1546)^2-8\cdot1024^2}{1024^2}
=-\frac{4\cdot23\cdot113\cdot577}{1024^2}
\pmod p.
\tag{19}
$$
式 (19) 的分子即 $(-1546)^2-8\cdot1024^2=-5998492$；(16) 的素数没有一个属于 $\{2,23,113,577\}$，所以该值非零。由此
$$
\boxed{\quad
p\nmid\operatorname{disc}F_p,\quad
389\text{ split},\quad13\text{ inert},\quad
\mathcal O_{F_p}^{\times}=\{\pm1\}.
\quad}\tag{20}
$$
这些域有无穷多个：一个固定二次域的有限类群不可能包含无界素数阶的元素，而 (15) 对 (16) 的每个素数成立。

## 5. $p=11$ 时确实是最大阶的原 Hilbert 轨道

只在本节起的实际 theta 计算中取 $p=11$。由 (18)，
$$
F=\mathbf Q(\sqrt{-6671}),\quad
\eta=\alpha_{11}+20=(-16,-13,21,12),
\quad \eta^2-\eta+1668=0.
\tag{21}
$$
$6671=7\cdot953$、$953$ 为素数，所以这是基本判别式。全部 reduced forms 的整数枚举给
$$
h_F=88=8\cdot11.
\tag{22}
$$
完整枚举保存在证书中，使用 $a\le\sqrt{6671/3}$ 的标准约化界。

固定原 $q$ 取向为 (17) 的 $7+7i$，固定 $389$ 取向为 $\eta$ 的特征值 $322$。原矩阵为
$$
\eta_{389}=\begin{pmatrix}68&0\\1&322\end{pmatrix},
\quad v_0=0.
\tag{23}
$$
枚举 $\mathcal O$ 中所有 trace $1$、norm $1668$ 且 (17) 等于 $7+7i$ 的元素，得到恰好 $88$ 个。对每个这样的 $r$，其原 level 标签是 $r_{389}$ 的 $322$ 特征线。这里未把两个 $q$ 取向或两个 $389$ 取向相加。

为给这些点付清实际类群标号，使用
$$
\mathfrak l=(2,\eta),\qquad \mathfrak a=(3,\eta).
$$
对 $\ell=2,3$，取 $r_\ell$ 的零特征线，在全部范数 $\ell$ 代表中选出相应核的唯一 $a$，使用原式
$$
(r,x)\longmapsto
\left(\frac{ar\bar a}{\ell},a_{389}x\right).
\tag{24}
$$
在 $2$ 处不能将 R276 的含 $1/2$ 基公式直接约化。本文使用真正的环同构 $\mathcal O/2\mathcal O\simeq M_2(\mathbf F_2)$，将 (1) 四个基依次送到
$$
\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
\begin{pmatrix}1&1\\0&0\end{pmatrix}.
\tag{25}
$$
十六个基乘积与线性双射均逐项核验。

实际置换 $P_2,P_3$ 满足
$$
\operatorname{ord}(P_2)=11,\quad P_3\text{ 是一个 }88\text{-cycle},
\qquad P_2=P_3^{64}.
\tag{26}
$$
由 R276 使用的 Galois 等变 CM reduction／最优嵌入比较，(24) 就是相应理想的 Artin 作用。一个最大阶 CM 点的 $P_3$ 轨道已有 $88=h_F$ 个不同的最优嵌入标签，因此它确实是**全部**原 Hilbert 轨道，不是从环境枚举中挑出的非零函数样本。

特别地，$\operatorname{Cl}(F)\simeq C_{88}$，$[\mathfrak a]$ 是生成元。唯一规范化字符
$$
\psi:\operatorname{Cl}(F)\twoheadrightarrow\mathbf F_{11},
\qquad\psi(\mathfrak l)=1
$$
满足
$$
\boxed{\quad \psi(\mathfrak a)=5.\quad}\tag{27}
$$
这来自 $64\cdot5\equiv1\pmod{11}$。所有 coset 的相位均由 (27) 确定，不能逐周期任意选取。

## 6. 同一原函数的一个周期与全八个 coset

使用 R276 的原 $\varphi_{13}:X_{13}\to\mathbf F_{11}$，规范为按节点次序第一个非零值等于一。脚本重新逐节点验证 $T_2,T_3,T_5$ 的本征值分别为 $-2,-2,-3$。

从 (21) 的基点沿 $\mathfrak l$ 作用的准确 11-cycle，就是 (7) 的 $p=11$ 闭路；其原函数值依次为
$$
(0,0,0,0,10,7,4,7,10,0,0).
\tag{28}
$$
所以该**单周期**的 binomial 矩为
$$
\boxed{\quad (M_0,M_1,M_2)=(5,8,1).\quad}\tag{29}
$$
它的非零增广已经表明它不能等于原完整来源，因为完整 Heegner 迹的增广为零。

取其余七个 $\langle\mathfrak l\rangle$-coset 后，准确完整来源为
$$
\Theta_1=
\sum_{c\in\operatorname{Cl}(F)}
\varphi_{13}(\operatorname{Red}_{13}x(1)^c)\,
\tau^{\psi(c)}.
\tag{30}
$$
这里采用 (24) 的 Artin 方向；整体改用逆 Artin 只作 $\tau\mapsto\tau^{-1}$。杀掉原 $F$-迹扭点的整数可取为 $1\pmod{11}$，因为原满像排除 $11$ 挠点；故 (30) 可直接采用 R281 的同一规范。阶八部分只做全和，不除以八。

所有八个周期的实际部分矩和相位如下。每行的起点为该周期中四元数坐标的字典序最小者。

| Artin 相位 $s$ | $M_0$ | $M_1$ | $M_2$ |
|---:|---:|---:|---:|
| $6$ | $8$ | $1$ | $10$ |
| $0$ | $8$ | $3$ | $4$ |
| $9$ | $9$ | $3$ | $7$ |
| $10$ | $3$ | $10$ | $3$ |
| $5$ | $3$ | $3$ | $6$ |
| $4$ | $5$ | $10$ | $8$ |
| $1$ | $10$ | $6$ | $1$ |
| $8$ | $9$ | $7$ | $6$ |

每一行须乘真实 $\tau^s$。在 $T=\tau-1$ 下，它的三个贡献准确为
$$
M_0,\qquad M_1+sM_0,\qquad
M_2+sM_1+\binom{s}{2}M_0.
\tag{31}
$$
完整结果为
$$
\boxed{\quad
(\theta_0,\ldots,\theta_{10})
=(9,9,7,6,7,8,3,8,7,6,7),\qquad
(m_0,m_1,m_2)=(0,0,9).
\quad}\tag{32}
$$
并且完整反射为 $\theta_j=\theta_{1-j}$。在同一初始周期的规范中，其余七个 coset 把 (29) 的前两项准确取消，并把第二矩从 $1$ 改为 $9$。因此 (32) 是真正的原非零输入；(29) 单独不是。

本例没有新增目标素数，只检验同一个已知 $p=11$ 上新闭路方法是否保留原全 trace。由 R281 可把 (32) 送到合法原分歧辅助层；由 R285 也可读成同一 Hilbert Heegner 点的实际 $\delta^2$ 类非零。

## 7. 一般闭路的完整低 jet 公式与 $p\operatorname{Cl}$ 问题

设一般最大阶类群为 $\mathcal C$，$a\in\mathcal C$ 的阶恰为 $p$。即使 (15) 已付，也仍须区分
$$
a\ne1\qquad\text{与}\qquad a\notin p\mathcal C_{(p)}.
\tag{33}
$$
只有后者才允许选择 $\psi:\mathcal C\twoheadrightarrow C_p$ 使 $\psi(a)$ 为生成元。若 $a=b^p$ 于 $\mathcal C_{(p)}$，则在 $\mathbf F_p[\mathcal C_{(p)}]$ 的增广理想 $J$ 中
$$
a-1=(b-1)^p\in J^p\subset J^3\qquad(p\ge5).
\tag{34}
$$
故该 $p$ 周期的局部一次、二次变化在原总二阶 jet 中不可见；存在一个阶 $p$ 类本身不支付早期非零。本文有限例由 $v_{11}(h_F)=1$ 排除了这个问题，但 (16) 的整个族尚未证明有相同性质。

若 (33) 的较强条件成立，选真实 $\psi(a)=1$，把类群分成 $a$ 的 coset。对每个真实代表 $b$，令 $s_b=\psi(b)$，并令 $M_{b,k}$ 为该周期的第 $k$ 个部分 binomial 矩。全部原来源必满足
$$
\begin{aligned}
m_0&=\sum_bM_{b,0},\\
m_1&=\sum_b(M_{b,1}+s_bM_{b,0}),\\
m_2&=\sum_b\left(M_{b,2}+s_bM_{b,1}
                         +\binom{s_b}{2}M_{b,0}\right).
\end{aligned}
\tag{35}
$$
这只是同一全群环 pushforward 的严格展开，因而也适用于 $p$-primary 类群有其他方向的情形。它不删除任何 coset，不在 $p$ 类群上用半单 Fourier 投影。非 Eisenstein 函数在某个 excursion 上非零，并没有给 (35) 的最后一项非零。

## 8. 非最大来源与改变观察素数时仍需保留什么

对 (16) 的一般 $p$，(15) 已经在最大阶得到精确阶 $p$，但原闭路可能仍在 conductor $f_p>1$ 的 $\mathcal O_p^{\rm opt}$ 上。由 (18)–(20)，该 conductor 与 $2p13\cdot389$ 互素。环类映射
$$
\operatorname{Cl}(\mathcal O_p^{\rm opt})\longrightarrow
\operatorname{Cl}(\mathcal O_{F_p})
$$
把选出的 $2$ 周期同构到其最大阶 $p$ 周期；不过，实际 CM 曲线的 conductor 下降还要运输原 level 标签，并对 conductor 纤维作完整 trace。闭路给出的值序列不能原样放到新的最大阶节点上。即使该下降完成，仍须保 (35) 的所有其余 Hilbert coset。

固定 $q=13$ 的另一个准确限制是
$$
a_{13}=-3,\qquad
a_{13}\equiv\pm(13+1)\pmod p
\quad\Longrightarrow\quad p\in\{11,17\}.
\tag{36}
$$
(16) 中仅 $p=11$ 命中这个集合。因此其余无穷几何成员没有可使用的原 $\varphi_{p,13}$。可以对每个 $(p,F_p)$ 重新用 R285 的 admissible Chebotarev 选择 $q_p$，但新 $\varphi_{p,q_p}$ 和新 CM reduction 必须实际重做，不能运输 (28) 的旧模 $11$ 数值来代替。

由此本篇实际付清的是：闭路到带原 level 的 CM 环类轨道、这个固定模板在最大阶中的精确 $p$ 阶、无穷几何族的全部局部条件，以及一个完整 88 类的原 trace。继续推进主目标需要在实际变化的 admissible $q_p$ 下，排除 (34) 的不可见性，并控制 (35) 的真实全和；不能以一个选中的周期替代它。

## 证书与来源

- [check-closed-walk-and-full-hilbert-trace.py](../scripts/check-closed-walk-and-full-hilbert-trace.py) 与同名 JSON 的 29 项准确检验全部通过；保存原四元数边、完整 88 个最优嵌入、两真实类群置换、全部 Artin 标签、八个周期和总 theta。未保存大稠密矩阵。
- R276：原最大整环与有限图、原 $\varphi_{13}$ 的剩余升层身份、全部 CM 标签的 Galois 等变比较。
- R271、R281、R285：原完整 $p$ 类群、二阶观察与整个通常 Selmer 接口。
- S. Arpin et al., *Orientations and Cycles in Supersingular Isogeny Graphs*, Research Directions in Number Theory, Association for Women in Mathematics Series 33 (2024), 25–86，尤其 Theorem 3.2、Lemmas 3.6–3.9：[已出版作者 PDF](https://cspages.ucalgary.ca/~rscheidl/Papers/WIN5-Proceedings.pdf)，[DOI](https://doi.org/10.1007/978-3-031-51677-1_2)。
