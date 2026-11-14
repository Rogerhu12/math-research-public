# 变化辅助域：无穷可选域与完整类群的两条 AS 迹坐标

日期：2026-11-12。**已证明。** 本文继续 R146，目标曲线始终是
$E=389\mathrm a1$。对每个合法固定 $(p,\ell)$，先证明存在无穷多个
满足所需分裂和类数条件的辅助域，再把指定的完整 Heegner 类群迹
准确写成两个有限域迹。没有证明这两个迹在其中一个域上非零。

## 1. Wiles 定理确实允许把 p 本身指定为分裂素数

固定素数
$$
 p\ge7,\quad p\ne13,389,\qquad
 \ell\ne p,389,\quad \ell+1=pu,\quad p\nmid u a_\ell(E).
\tag{1}
$$
这里暂不要求 $p$ 在目标 $E$ 上普通；使用 R146 时再加普通、
非异常及其固定有限例外以外的条件。

Wiles（2015）*On class groups of imaginary quadratic fields* 的
Theorem 0.0.1 对奇素数 $l$ 和三组有限奇素数 $S_+,S_0,S_-$，
在以下限制下给类数不被 $l$ 整除的虚二次域：$S_+$ 排除
$q\equiv-1\pmod l$，$S_0$ 排除 $q\equiv1\pmod l$，$S_-$ 排除
同时满足 $q\equiv1\pmod l$、$q\equiv-1\pmod4$ 的素数。
所得域在三组素数处依次分裂、分歧、惰性。

这里采用作者接受稿的原始定理。它**没有**要求 $l\notin S$；
§2.1 的 (2.1.1) 专门处理 $q=l\in S_+\cup S_-$，印稿页 11
并核对这个局部相容条件。因而可以取
$$
             l=p,\qquad S_+=\{p,389\},\qquad S_-=\{\ell\}.
\tag{2}
$$
在 (1) 下，$\ell\equiv-1\pmod p$ 不触及 $S_-$ 的禁例；
$389\equiv-1\pmod p$ 对 $p\ge7$ 只可能在 $p=13$，已排除。
于是存在虚二次域 $F$ 满足
$$
 p\nmid h_F,\qquad p,389\text{ 在 }F\text{ 分裂},\qquad
                  \ell\text{ 在 }F\text{ 惰性}.
\tag{3}
$$

事实上这样的 $F$ 有无穷多个。若已有有限个候选域，选一个新的
奇素数 $q>3$，不整除它们任一判别式且 $q\not\equiv1\pmod p$，
也不在 (2) 中。Dirichlet 定理保证这样的 $q$ 存在。
在 (2) 外加 $S_0=\{q\}$ 再用 Wiles 定理，新域在 $q$ 分歧，
所以不在此前有限列表中。这个条件同时排除了有额外单位的
$\mathbb Q(i)$ 和 $\mathbb Q(\sqrt{-3})$。迭代即得无穷性。
该论证没有给判别式上界，也没有指定任何模 $p$ Heegner 迹值。

### 1.1 同一固定有限 p 例外足以保证 full GL2

Serre（1972）Théorème 3 的 Corollaire 1（印页 300）给：对固定
非 CM 曲线 $E$，除有限多个 $p$ 外，
$$
                    \rho_{E,p}(G_{\mathbb Q})
                              =\mathrm{GL}_2(\mathbb Z_p).
\tag{4}
$$
若 $p\ge5$ 且 (4) 成立，则对**每个**在 $p$ 不分歧的二次域
$F$，同样有 $\rho_{E,p}(G_F)=\mathrm{GL}_2(\mathbb Z_p)$。

证明：若后者是真子群，其指数为二，故给
$\mathrm{GL}_2(\mathbb Z_p)$ 的非平凡二次角色。交换子群含
$\mathrm{SL}_2(\mathbb Z_p)$：上下幺幂矩阵由对角矩阵和幺幂矩阵
的交换子产生，且它们生成 $\mathrm{SL}_2$。因此二次角色经
行列式分解。$\mathbb Z_p^\times$ 唯一的二次商是模 $p$ 的
平方类商；由 Weil 配对，它对应
$\mathbb Q(\sqrt{(-1)^{(p-1)/2}p})$。这个域在 $p$ 分歧，与
$F$ 的条件矛盾。证毕。

所以 (3) 的无穷个域统一满足 R146 的 full-GL2 输入，所删
素数集合只依赖固定 $E$，不随 $F$ 增大。

## 2. 环类域分解：先 u 项，再全部 h_F 项

选满足 (3) 的一个 $F$，令
$$
 C=\operatorname{Cl}(F),\quad h=|C|,
 \quad F_1=F[1],\quad H=F[\ell].
$$
因 $F$ 只有单位 $\{\pm1\}$ 且 $\ell$ 惰性，环类正合列的核
为循环群 $T$，$|T|=\ell+1=pu$。令 $U\subset T$ 为阶 $u$
子群，令 $L/F$ 为 $H/F$ 的唯一 $C_p$ 子扩张。因 $p\nmid h$，
$$
 M:=H^U=LF_1,\quad L\cap F_1=F,\qquad
 \operatorname{Gal}(M/F)=\Gamma\times C,
 \quad\Gamma=\langle\tau\rangle\simeq C_p.
\tag{5}
$$
这来自有限阿贝尔群的 $p$ 主部与素于 $p$ 部分的直积分解。
没有选择一个非规范的类群代表后删掉其它类。

取原模参数化 $\pi:X_0(389)\to E$，$\pi(\infty)=O$，以及
带固定 Heegner 方向的原点 $P[\ell]$。R146 的基层完整迹
$P_F=\operatorname{Tr}_{F_1/F}P[1]$ 是扭点；取 $p$ 单位整数
$t_F$ 杀掉它。于是指定整数点是
$$
 Y=[t_F]\operatorname{Tr}_{H/M}P[\ell],\qquad
 Q=\operatorname{Tr}_{M/L}Y
   =[t_F]\operatorname{Tr}_{H/L}P[\ell].
\tag{6}
$$
范数关系给 $N_\Gamma Q=t_Fa_\ell P_F=0$。
总共有 $uh$ 项；类数一是这个式子的特例，不能在一般情形
把 $Y$ 当成 $Q$。

## 3. 真正的普通 CM 约化和 Frobenius 轨道

固定 $v=\mathfrak p\mid p$ 的嵌入，故 $F_v=\mathbb Q_p$。
所有上述环类域在 $v$ 不分歧。写有限 étale 剩余代数
$$
 S_C=\mathcal O_{F_1}\otimes_{\mathcal O_F}\mathbb F_p,
 \quad S_\Gamma=\mathcal O_L\otimes_{\mathcal O_F}\mathbb F_p,
 \quad S=\mathcal O_M\otimes_{\mathcal O_F}\mathbb F_p
                 =S_C\otimes_{\mathbb F_p}S_\Gamma.
\tag{7}
$$
张量的等式保留全部完成，允许完全分裂的乘积代数。

ordinary CM 曲线且导子素于 $p$ 时，它就是约化的 canonical
lift，且约化保留完整自同态环。这里使用 Herrero–Menares–
Rivera-Letelier（2020）Proposition 3.1 和 Theorem 3.2（出版版
印页 1255）；同一定理还给 canonical Frobenius 商及 Hom 的
唯一提升。因此原 $N$ 循环子群和原 $\ell$ torus 标签必须沿
CM 同源运输，不能在约化点上任意另选一个 nonsplit torus。

在算术 Artin 约定下，quotient by $C[\mathfrak p]$ 将复格
$\mathfrak a$ 变成 $\mathfrak p^{-1}\mathfrak a$；它在约化上
就是算术 Frobenius。故源的 $h$ 个类群标签由
$c_p=[\mathfrak p]\in C$ 置换。令 $d=\operatorname{ord}_C(c_p)$，
则
$$
            S_C\simeq\prod_{h/d}\mathbb F_{p^d},\qquad p\nmid d.
\tag{8}
$$
这是 $h/d$ 条长度 $d$ 的实际 Frobenius 轨道，而非任取
$h$ 个闭点。固定 ordinary 几何点的 canonical lift 和其
自同态二次域已经唯一；改变 $F$ 不能在同一个点上随意改变
完整类群轨道。一般 ordinary 点的 $389$ 子群也未必是所需的
水平 CM 子群。

## 4. 原去 p 函数的完整类群迹

保留实际微分 $f_\pi=\pi^*\omega_E$ 的 Manin 常数，令
$$
 g_p=\frac{\Theta^{p-2}\overline f_\pi}{\mathrm{Ha}^p}.
\tag{9}
$$
它在 ordinary 源点正则，并是 R134 中去 $p$ Coleman 原函数
$G^{[p]}$ 的约化。细模覆盖只用来定义函数和运输标记；实际
权零函数及下列完整迹都下降回 $X_0(389)$，不改变整数迹点。

把 (6) 的第一步保留成元素
$$
 \beta=\overline{t_F}\sum_{u_0\in U}g_p(x_\ell^{u_0})\in S,
 \qquad \beta_F=N_C\beta\in S_\Gamma,
 \qquad n=N_\Gamma\beta\in S_C.
\tag{10}
$$
这里两个 $T_0$ 轨道须按 R137 合起来才是原 $u$ 项 $U$ 迹。
完整 Hecke 关系和基层扭迹给
$$
 n=\overline{t_Fa_\ell}\,g_p(x_1)\quad\hbox{逐类群标签},
                  \qquad N_C n=0.
\tag{11}
$$
最后一个零是完整类群迹的零；一般不能断言每个分量 $n_c=0$。

令 $s=\operatorname{Art}_{L/F}(v)$。R134 的实际 Coleman 比较与
完整迹交换，给
$$
 \beta_F=(p-a_ps+s^2)\frac{\log_E Q}{p}\pmod p.
\tag{12}
$$
右侧首先在 $L$ 的完整半局部格中定义。因为该剩余次数为
$1$ 或 $p$，$a_p\not\equiv1\pmod p$ 保证约化群阶素于 $p$，
从而 $\log_E Q/p$ 整。不能据此声称每个未取完整类群迹的
$\log_E P[\ell]/p$ 都整。(9)–(10) 的各项则由 ordinary
模函数自身整性定义。

群环元 $p-a_ps+s^2$ 的增广模 $p$ 为 $1-a_p\ne0$，所以是
$\mathbb F_p[\Gamma]$ 的单位。由 R130/R134，
$$
 D_2\beta_F\ne0
 \ \Longrightarrow\ Q\notin\delta^2(A(F)\otimes\mathbb Z_p)
 \ \Longrightarrow\ \Sha(E/\mathbb Q)[p^\infty]=0,
\tag{13}
$$
其中 $D_2=\sum_{j=0}^{p-1}\binom j2\tau^j$。
第一非零本身已迫 $Q$ 非扭，因此 R146 的后续条件在这里
由同一个实际点支付；没有先假设 $Q$ 非扭再偷偷删掉该条件。

## 5. 两个完整有限域迹：准确的可选性目标

在 $S_\Gamma$ 选 AS 坐标 $y$，使
$$
                   \tau y=y+1,\qquad y^p-y\in\mathbb F_p.
\tag{14}
$$
该坐标总存在：取 $e\in S_\Gamma$、$N_\Gamma e=1$，令
$y=-D_1e$，其中 $D_1=\sum j\tau^j$。有限 étale 迹满射及
$(\tau-1)D_1=-N_\Gamma$ 给 (14)。它同时适用于分裂乘积。
因 $y\in S_\Gamma$，它在 (7) 中被整个 $C$ 固定。

R142 的群环计算给唯一 $a,g\in S_C$，使
$$
 D_1\beta=-ny+a,\qquad
 D_2\beta=\frac n2y(y+1)-ay+g.
\tag{15}
$$
取完整 $C$ 迹，并用 (11)，得到
$$
 \boxed{\quad
 A_F:=N_Ca\in\mathbb F_p,\qquad
 G_F:=N_Cg\in\mathbb F_p,
 \qquad D_2\beta_F=-A_Fy+G_F.
 \quad}
\tag{16}
$$
$1,y$ 在 $\mathbb F_p$ 上线性独立，即使在完全分裂代数中也
如此，因为 $y$ 的 $p$ 个值两两不同。因此
$$
 \boxed{\qquad
 D_2\beta_F\ne0\quad\Longleftrightarrow\quad
                         (A_F,G_F)\ne(0,0).
 \qquad}
\tag{17}
$$
换 $y$ 为 $y+b$、$b\in\mathbb F_p$，只把
$(A_F,G_F)$ 改成 $(A_F,G_F+bA_F)$，共同消失与否不变。

把 (8) 的各轨道代表记作 $r$，(16) 完全等于
$$
 A_F=\sum_{r\in C/\langle c_p\rangle}
                    \operatorname{Tr}_{\mathbb F_{p^d}/\mathbb F_p}(a_r),
 \qquad
 G_F=\sum_{r\in C/\langle c_p\rangle}
                    \operatorname{Tr}_{\mathbb F_{p^d}/\mathbb F_p}(g_r).
\tag{18}
$$
这里没有额外 $h/d$ 倍数，也没有删掉某条 Frobenius 轨道。
若 $S_\Gamma$ 为域，则它为 $\mathbb F_{p^p}$，且原 (10) 的
$\beta_F$ 是 $h/d$ 个
$\operatorname{Tr}_{\mathbb F_{p^{pd}}/\mathbb F_{p^p}}(\beta_r)$
之和；若完全分裂，则相同式子逐个分量计算。由于 $(p,d)=1$，
两种描述与 (7) 的张量分解一致。

若已经在每个类群标签上用了不同的 AS 坐标
$y_c=y+b_c$，必须保留平移项。设当地系数为 $(n_c,a_c,g_c)$，
即 $D_1\beta_c=-n_cy_c+a_c$，第二式同 (15)，则
$$
 \begin{split}
 A_F&=\sum_c(a_c-n_cb_c),\\
 G_F&=\sum_c\left(g_c-a_cb_c+
                              \frac{n_c}{2}b_c(b_c+1)\right).
 \end{split}
\tag{19}
$$
这些和在共同几何剩余域中按完整类群运输解释；(18) 是其
降回 $\mathbb F_p$ 的写法。只有先选 (14) 的共同坐标，才能
无补偿地把两个当地系数直接相加。

## 6. 无限候选域不等于指定类群迹非零

$p\nmid h$ 的准确作用是使 $h^{-1}N_C$ 成为整的投影，
以及 (5)、(7)、(14) 的分解可用。它不使 $N_C$ 在
$S_C$ 上单射；在代数闭包上它只保留类群的平凡角色。
本题实际的一阶例子已经是 (11)：逐标签的 Hecke 总迹
可以非零，而完整类群迹因固定 E 的秩至少二必须为零。

因此 R145 的某个单点判别式极点、某个单点的 $(a_c,g_c)$
非零，或 ordinary CM 点的稠密性，都不能替代 (18)。
特别是 R141 的“每个源点 $n=0$ 且为简单零”依赖类数一的
固定源；变化 $F$ 后一般只有 $N_Cn=0$，不能直接对每个
标签再用同一简单零判据。

当前真正的正面充分条件是：对无穷多个合法 $p$，选一个
$\ell$ 和 §1 的一个域 $F$，使 **同一个实际原点** 的 (18)
两个完整迹至少一个非零。§1 已支付无穷候选 F 及 full GL2，
§§2–5 已支付完整类群、CM 标记、算术 Frobenius、所有单位
和有限格比较；尚未支付的正是这两个迹的共同非消失。

## 一手来源

- A. Wiles, *On class groups of imaginary quadratic fields*,
  J. London Math. Soc. **92** (2015), 411–426，
  [作者接受稿](https://ora.ox.ac.uk/objects/uuid%3A120f2970-8027-4bc5-bd93-b72a7fbc91ff/files/m0f7a4c0d075ccdcf1aa54ad58d333763)，
  Theorem 0.0.1；§2.1，(2.1.1)，接受稿第 11 页明确允许
  $q=l\in S_+\cup S_-$。本文无限多个域的迭代另有完整证明。
- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des
  courbes elliptiques*, Invent. Math. **15** (1972), 259–331，
  [作者机构全文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)，
  Théorème 3，Corollaire 1，印页 300。§1.1 给在所有本题 F
  上统一继承满像的直接群论证明。
- S. Herrero, R. Menares, J. Rivera-Letelier,
  *p-adic distribution of CM points and Hecke orbits I: Convergence
  towards the Gauss point*, Algebra Number Theory **14** (2020),
  1239–1290，
  [发表版](https://msp.org/ant/2020/14-5/ant-v14-n5-p04-p.pdf)，
  Proposition 3.1、Theorem 3.2，印页 1255；
  [作者预印本](https://arxiv.org/pdf/2002.03232)，相同编号。
- M. Bertolini, H. Darmon, K. Prasanna,
  *Generalized Heegner cycles and p-adic Rankin L-series*, Duke
  Math. J. **162** (2013), 1033–1148，
  [作者全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP1.pdf)，
  Lemma 3.23、Proposition 3.24，印页 1085–1087；R134 已逐项
  核定原权零 CM 标记及 $V$ 的算術 Artin 方向。
- R130、R134、R137、R142、R145、R146：实际两步整格、
  全 $U$ 轨道、AS 正规形和正号 Selmer 判据。本文所有新增
  类群求和、坐标补偿及有限域迹公式均在 §§2–5 直接证明。
