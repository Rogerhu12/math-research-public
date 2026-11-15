# R179：固定颜色余密度 words 的普适原函数独立性

日期：2026-11-15。**完整纸面证明；没有运行新的研究目标、profile 积分、矩阵消元或查询。** 本稿补足 [R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 明确保留的解析问题：其最终规范余 letter words，在全部允许的光滑 profiles 上确实线性独立。证明用局部变分及互不相交的 profile packets，直接保留真实右锚；不把原函数当作可独立指定的形式变量。

由此，对已经正确转入本规范语法的有限表达式，非零规范代表就是普适原函数非零。对于 [R174](R174-nine-original-character-relations-and-rejection-of-the-positive-outer-point.md) 的 77 个字面基，如果新共同表的所有 letter 均通过该语法条件，并且各列有已绑定的同锚转换身份，共同表的核便是完整真实函数核。**这不是 R177 指定点已经良定义的结论：它仍须消灭该完整核。**

## 1. 语法、输入和要证明的命题

固定有限有序颜色集合 $\mathcal C$，设

$$
\mathcal A=\mathbb K[x,z_{c,j}:c\in\mathcal C,\ j\ge0],
\qquad
D=\partial_x+\sum_{c,j}z_{c,j+1}\partial_{z_{c,j}},
\tag{1}
$$

其中 $\mathbb K=\mathbb R$ 或 $\mathbb C$；每个表达式只含有限多个 jet。实际代入为 $z_{c,j}=D_x^j f_c$。

沿用 R178 的余类型：一个有正 profile 多次数的 monomial，先取其**最高存在颜色** $c_*$。若该颜色的最高 jet 阶是零，或其最高阶 $m\ge1$ 的 jet 幂至少为二，就称它为余 monomial。令 $\mathscr L$ 为全部这种 monomials 的集合。不同的 $x$ 幂、颜色或 jet monomials 是不同的 letter。所有 letter 都有正 profile 次数；纯 $x$ 多项式不是这里的 letter。

固定开区间 $I$ 及其右端锚 $r$。可以把 $r$ 置于共同右 collar 内，输入均在其邻域恒零。对有限 word $w=(\ell_1,\ldots,\ell_s)$ 定义

$$
I(f)(x)=\int_r^x f(t)\,dt,
\qquad
I_w=I\bigl(\ell_1 I_{(\ell_2,\ldots,\ell_s)}\bigr),
\qquad I_\varnothing=1.
\tag{2}
$$

一个最终规范表达式是有限和

$$
E=\sum_w C_w(x,jf)\,I_w[f],\qquad C_w\in\mathcal A,
\tag{3}
$$

其中相同 word 的局部系数已经合并。系数 $C_w$ 可以具有零 profile 次数，包括纯 $x$ 多项式；**word 内的每个 letter** 则必须属于 $\mathscr L$。

**主定理。** 如果 (3) 对每组允许的光滑 profiles、每个查询点 $x\in I$ 都是零函数，则所有 $C_w$ 都是零多项式。因此

$$
\operatorname{Eval}:
\bigoplus_{w\in\mathscr L^*}\mathcal A\,w
\longrightarrow
\{\text{普适同右锚 profile 函数}\}
\quad\text{是单射。}
\tag{4}
$$

若共同右 collar 是一个预先固定的区间，先在其左侧的自由部分固定任意非空开区间 $J_*\Subset I$。这里只需测试 $C_c^\infty(J_*)$ 输入；从 $J_*$ 到 collar 内锚 $r$ 的其余部分输入为零。这些确为原共同右 collar 输入的子类，所以没有增加原身份的假设。结论是**普适**函数身份，不是固定一个 profile、固定一个圆、有限采样或三矩受限子集上的独立性。

本课题的接口确实允许查询点在开区间内变化：[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的成本 $V_B$ 及 [R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 的 $U$ 都是整个 $\xi$ 函数，不是只在某个固定查询点的值。如果只给一个固定 $x_0$，以下 packet 论证仍提取该点的 local coefficient 值，但不能据此分离一个关于 $x$ 的完整多项式；本稿最后一步使用了原 $U$ 已有的整个开区间定义。

## 2. 任意小区间上的单积分张成

先固定任意非空开区间 $J\Subset J_*$ 和有限个不同余 letters

$$
\ell_1,\ldots,\ell_m\in\mathscr L.
$$

对一组支撑于 $J$ 的 profiles，令

$$
A_J(f)=\left(\int_J\ell_1(jf),\ldots,
                 \int_J\ell_m(jf)\right)\in\mathbb K^m.
\tag{5}
$$

**引理 1。** 这些值的线性张成为整个 $\mathbb K^m$。不要求值集本身是线性空间、包含邻域或具有任意符号。

### 2.1 积分湮灭给 Euler 恒等式

若结论不成立，存在非零常系数向量 $a$，使余多项式

$$
R=\sum_{i=1}^m a_i\ell_i
\tag{6}
$$

满足 $\int_JR(jf)=0$，对全部紧支撑输入成立。逐颜色作任意紧支撑变分并分部积分，没有端项，得到

$$
\mathcal E_c(R)=
\sum_{j\ge0}(-D)^j\frac{\partial R}{\partial z_{c,j}}=0.
\tag{7}
$$

这里 (7) 先沿任意 profiles 成立。任意有限 jet 可以用一段有限 Taylor 多项式乘以在查询点附近等于一的紧支撑 cutoff 实现。因此 (7) 对 $x\in J$ 的全部有限 jet 值成立，是一个真正的多项式恒等式。其 $x$ 系数在开区间上恒零，故作为多项式也恒零。

### 2.2 余类型不能成为非零零变分密度

取 $R$ 实际含有的最高颜色 $c$。先设其最高 jet 阶为 $m\ge1$。所有含 $z_{c,m}$ 的余 monomials 都至少二次含有它。

在 $\mathcal E_c(R)$ 中，最高新 jet $z_{c,2m}$ 的系数准确为

$$
(-1)^m\frac{\partial^2 R}{\partial z_{c,m}^2}.
\tag{8}
$$

理由是：$j<m$ 的项最多产生颜色 $c$ 的 $m+j<2m$ 阶 jet；只有 $j=m$ 项能够产生 $z_{c,2m}$，且其系数如 (8)。较低颜色即使有更高导数，也不改变这个固定颜色的阶数论证。

由 (7)，(8) 为零。因此 $R$ 关于 $z_{c,m}$ 至多一次。但余类型已经排除了全部一次项，所以 $R$ 根本不含该 jet。逐次降低 $m$。

降至颜色 $c$ 仅有零阶 jet 时，$\mathcal E_c(R)=\partial R/\partial z_{c,0}$。于是 $R$ 也不含该颜色。对其余颜色依次重复，最终 $R$ 不含任何 profile 因子。原 $R$ 的每项都具有正 profile 次数，因此 $R=0$，与不同余 monomials 的非零线性组合矛盾。

这个过程覆盖不同多次数的相加及不含当前最高颜色的项：后者不影响该颜色的 Euler 方程，在剥离该颜色后继续处理。也可以先逐多次数分解，结论相同。

这证明引理 1，无须先引入有理 jet 域、证明其无新原函数，或假定实际 primitive 值独立。

## 3. 不交 packets 对最大 word 长度的准确提取

设 (3) 的最大非零 word 长度为 $L\ge1$。收集其中用到的有限 letter 集，记为 $\ell_1,\ldots,\ell_m$。

在 $J_*$ 左部固定一个非空开区间，让查询点 $x_0$ 在其中自由变化；对每个这样的 $x_0$，在其右侧且仍在 $J_*$ 内选择 $L$ 个有序的非空小区间

$$
x_0<J_1<J_2<\cdots<J_L<r.
\tag{9}
$$

另取一个包含 $x_0$、且与这些区间不交的小区间 $J_0$。在 $J_0$ 内选取 profiles $f^{(0)}$，使它们在 $x_0$ 的有限 jets 任意指定。在每个 $J_j$ 内另取独立的一组 profiles $f^{(j)}$。

对 $S\subseteq\{1,\ldots,L\}$，同时按整个颜色组开关 packet，定义

$$
f_S=f^{(0)}+\sum_{j\in S}f^{(j)}.
\tag{10}
$$

所有输入仍光滑、紧支撑、同右锚。右侧 packets 不改变查询点的任何 local jet。

### 3.1 包含排除为何没有混合污染

对一个正次数局部 letter，支撑不交给准确恒等式

$$
\ell(jf_S)(t)=\ell(jf^{(0)})(t)+
              \sum_{j\in S}\ell(jf^{(j)})(t).
\tag{11}
$$

每个局部乘积在同一 $t$ 求值，故不同 packet 的 profile 因子不能交叉。这里不把幅度当作一阶小量；(11) 对整个 packet 的开关准确成立。

采用实际右锚 (2)，一个长 $s$ 的 word 为

$$
I_{(a_1,\ldots,a_s)}(x_0)
=(-1)^s\int_{x_0\le t_1\le\cdots\le t_s\le r}
\prod_{i=1}^s a_i(jf)(t_i)\,dt_1\cdots dt_s.
\tag{12}
$$

现在对 (3) 作有限包含排除

$$
\Delta_L E=
\sum_{S\subseteq\{1,\ldots,L\}}
(-1)^{L-|S|}E[f_S](x_0).
\tag{13}
$$

展开 (11) 后，只保留每个 $J_1,\ldots,J_L$ 都至少出现一次的项。因此：

- 长度小于 $L$ 的 word 全部消失；
- 长度恰为 $L$ 的 word，每个右侧 packet 恰好使用一个 letter；
- 这时没有 letter 留给 $J_0$，所以查询点附近的辅助 profile 不污染最高长度项；
- 由 (9)、(12)，第一个 letter 必须位于 $J_1$，依次类推，词序没有置换或阶乘因子。

故得到准确式

$$
\Delta_LE=(-1)^L
\sum_{|w|=L}C_w(x_0,jf^{(0)}(x_0))
\prod_{j=1}^L\int_{J_j}\ell_{w_j}(jf^{(j)}).
\tag{14}
$$

共同右 collar 保证所有原式原函数常数仍由同一 $r$ 固定。式 (14) 中没有重锚，也没有假定某个左尾为零。

### 3.2 张量积张成迫最高层系数为零

若 $E$ 是普适零函数，则 (14) 对所有 $f^{(j)}$ 为零。引理 1 对每个小区间 $J_j$ 分别适用。每个单积分向量值集的线性张成均为 $\mathbb K^m$，所以它们的张量积张成整个 $(\mathbb K^m)^{\otimes L}$。

式 (14) 对这些单积分向量是多线性的，因此各个词系数满足

$$
C_w(x_0,jf^{(0)}(x_0))=0\qquad(|w|=L).
\tag{15}
$$

在这个非空查询区间内 local jets 任意，因此所有 $C_w$ 是零多项式。分离 $x$ 多项式只需这个开区间，不需要在预定零 collar 内任选 jets。删除这一层，重复对 $L-1$ 作同样证明。最终只剩空词，其系数是一个对全部有限 jets 恒零的局部多项式，也只能为零。主定理得证。

## 4. 真实 q 与共轭 q 的约束

本课题的两种形式颜色为 $q,\bar q$，真实输入满足

$$
q=f+ig,\qquad\bar q=f-ig,
\tag{16}
$$

其中 $f,g$ 为实 profiles。不能直接把两种实际历史当作独立控制。

但本稿研究的是有限次 profile 多项式的**普适恒等式**。任取有限多个实测试 profiles，把 $f,g$ 展成这些 profiles 的任意实线性组合。原式在这些实系数上是有限次数的复值多项式；所有 Volterra 积分只是其多项式系数中的固定真实积分。若原式对全部真实 $f,g$ 为零，该多项式的所有系数都为零，因此可以将幅度变量复化。

复化后，线性可逆换元

$$
f=(q+\bar q)/2,\qquad
g=(q-\bar q)/(2i)
\tag{17}
$$

允许把两种颜色独立指定。上面的 packet 证明每次只使用有限多个 profiles，正落在这个复化论证内。因此 (4) 对物理共轭输入上的普适身份同样成立。

这个步骤没有对一个固定真实 $q$ 任意更改 $\bar q$，也没有把只在某个固定圆上成立的身份推广成普适身份。

## 5. 规范系数是可直接定义的真实函数泛函

主定理不仅排除了未见的 word 关系，也给出一个不依赖表达式写法的泛函构造。

先固定任意有限规范子空间：有限 letter 集、word 长度上限、local coefficient 的有限 monomial 集。由引理 1，在每个 $J_j$ 中可以选有限个 profiles，使单积分值组成一个可逆矩阵。对 (14) 作这些矩阵的张量逆，就从有限次真实函数评价中提取各个最高词的

$$
C_w(x_0,\zeta),
\tag{18}
$$

其中 $\zeta$ 是任选 local jet。

再选有限个 $x_0,\zeta$ 对局部系数多项式作插值，便得到所有最高词的每个局部 monomial 系数。减去已恢复的最高词函数后逐层下降，即得到全部规范系数。由于空间有限，整个过程只用有限线性运算及有限个函数评价。

因而每个规范系数提取都是该实际函数空间上的一个良定义线性泛函。任意有限规范系数的线性组合也如此。它们可以等价看作由有限个测试 profiles 和输出点组成的分布型评价；右 primitive 的值仍由实际积分给出。

如果上述构造使用了第 4 节复化后的 packets，取其中有限多个 profiles 的实部、虚部作为实测试基。表达式在这些幅度变量上是有统一有限次数的多项式，有限实幅度网格上的多项式插值便把每个复幅度查询准确写成有限个真实 $f,g$ 查询的线性组合。因此“真实函数评价”的表述不需要实际允许复 $f,g$ 控制；取实部、虚部即可得到所需实线性泛函。

这些是函数空间上的**有符号线性泛函或查询**。包含排除的负号、插值矩阵的逆及复化都不授予实际负成本，不提供输入相位的几何控制，也不证明成本锥在这些操作下不变；[R156](R156-input-phase-rotation-fails-canonical-cost-invariance.md) 的范围保持。

这里给的是存在性与准确的构造方式，不是本次已经选择、评价或优化了一套新的 profile 查询。也没有为 R177 提前填写一组未知的系数提取权。

## 6. 对完整 canonical 函数和共同表的结论

R178 已证明每一步 local IBP、shuffle 和同锚递归都 sound，而且终止于本稿的语法。结合主定理，得到

$$
\Phi(E)=0
\quad\Longleftrightarrow\quad
E=0\text{ 作为普适原函数}.
\tag{19}
$$

该等价仅适用于已经付清原式到规范代表的转换、且所有 letter 满足本稿条件的表达式。不能据此追认任意旧 cycle fallback、未规范 letter 或不完整中间输出为完备。

对本课题的 canonical 成本，[R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md) 已给 $E\mapsto(\pi E,\Xi E)$ 的共同忠实性。于是如果这两根分别采用本稿语法，原函数身份等价于两根规范系数同时为零。不能只保 balanced 而删去尚未支付的 pure 分量。

### 6.1 复用旧 sound 代表不必重算

设一个已发布的旧代表 $v_j$ 与原根 $E_j$ 有正确同锚身份，且 $v_j$ 本身已经处于本稿规范语法。则

$$
\operatorname{Eval}v_j=E_j
\quad\Longrightarrow\quad
v_j=\Phi(E_j),
\tag{20}
$$

因为两者之差在规范空间中评价为零，主定理使差的所有系数为零。这里不要求旧算法与新算法的执行顺序相同，也不需要重新展开旧原根。

所以 R178 的复用型共同映射 $\Psi$，在**逐列来源绑定、转换身份和最终语法均成立**时，也有

$$
\ker\Psi=\ker E.
\tag{21}
$$

如果某个旧代表未通过规范语法条件，这个推论不适用；应保留未付项或只转换必要部分，不能把它删除。程序资源退出仍表示共同表未完成，与主定理无关。

### 6.2 R177 的准确下一门

R177 对 R174 的 77 个字面基给出线性赋值 $\ell_*$。设其已绑定共同两根规范矩阵为 $A$。本稿给出准确充要条件

$$
\boxed{\quad
\ell_*\text{ 可降为真实原函数泛函}
\quad\Longleftrightarrow\quad
\ell_*|_{\ker A}=0.
\quad}
\tag{22}
$$

若条件成立，有限线性代数把 $\ell_*$ 表成规范系数的线性组合；第 5 节将其解释为一个直接作用于实际函数的泛函，自动消灭所有真实函数关系。若条件失败，核中的一条被赋成非零的关系就排除该指定点。

因此本稿将此前保守的单向关系检测升级为可完成的真实良定义门；但**没有假定 R177 会通过它**。共同矩阵尚未完成或只证明部分核时，仍只能报告相应已完成范围。

## 7. 范围与未付项

本稿证明的是正次数余 letter、局部多项式系数、同右锚、普适光滑 profile 函数的解析独立性及有限系数泛函构造。它不需要真实研究计算，也不增加已完成目标的复验门。

未由本稿取得：R177 实际核匹配结果；任意固定 profile 圆上的 word 独立；完整成本锥或半群的自由正负控制；第四 ruling、无限阶延拓、有限等距族、嵌入或 reach。有限原函数空间上的泛函良定义，必须与这些几何结论分开。
