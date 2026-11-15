# R178：固定颜色次序的局部唯一 IBP 与有限终止的共同 word 映射

**状态：已证明的代数与原函数恒等式结论。** 本稿不运行研究目标，不宣称余下的 word 作为普适 profile 函数独立。用途是把 R75 的单颜色局部唯一分解推广到完整 mixed 原式，并为 R174 的 77 个字面基提供一个没有改写循环的共同 sound 表示。

这里固定颜色次序；在本课题中可取 $q<\bar q$。次序只是选取局部密度代表的算法，不把 $q,\bar q$ 当作两个可任意独立指定的真实历史，也不改变原物理右锚。

## 1. 固定多次数与最高存在颜色

取有限有序颜色集合 $\mathcal C$，定义

$$
\mathcal A=\mathbb Q[\xi,z_{c,j}:c\in\mathcal C,\ j\ge0],
\qquad
D=\partial_\xi+\sum_{c,j}z_{c,j+1}\partial_{z_{c,j}}.
\tag{1}
$$

每个多项式只含有限多个 jet。按每种颜色的 profile 因子数分解

$$
\mathcal A=\bigoplus_{\boldsymbol n}\mathcal A_{\boldsymbol n},
\qquad n_c=\text{颜色 }c\text{ 的因子总数}.
$$

$D$ 保持多次数 $\boldsymbol n$。以下固定非零多次数，设

$$
c_*=\max\{c:n_c>0\}.
$$

这里的“最高”先按颜色次序决定，**不先比较不同颜色的导数阶**。

称 $\mathcal A_{\boldsymbol n}$ 的一个 monomial 为余类型，如果在颜色 $c_*$ 中：

- 最高 jet 阶为 $0$；或
- 最高 jet 阶为 $m\ge1$，且 $z_{c_*,m}$ 的幂至少为 $2$。

较低颜色的 jet 阶在这个定义中不受额外限制。记所有余类型 monomial 的线性张成为 $\mathcal R_{\boldsymbol n}$。例如在 $q<\bar q$ 下，$q''\bar q$ 是余类型，即使 $q''$ 的阶高于 $\bar q$ 的阶；$q'\bar q'$ 则不是余类型。

## 2. 完整局部唯一分解

**定理 1。** 对每个非零多次数 $\boldsymbol n$ 和 $f\in\mathcal A_{\boldsymbol n}$，存在唯一

$$
f=DB+R,\qquad
B\in\mathcal A_{\boldsymbol n},\quad
R\in\mathcal R_{\boldsymbol n}.
\tag{2}
$$

因此 $B(f)$、$R(f)$ 都是有理线性映射。

### 2.1 存在性

只需处理不是余类型的一个 monomial。设颜色 $c_*$ 的最高 jet 是只出现一次的 $z_{c_*,m}$，$m\ge1$，写为

$$
f_0=\xi^p z_{c_*,m}z_{c_*,m-1}^{\ell}G.
\tag{3}
$$

其中 $G$ 的颜色 $c_*$ 因子阶数不超过 $m-2$；它可以包含较低颜色的任意有限阶 jet。取

$$
B_0=\frac{\xi^p z_{c_*,m-1}^{\ell+1}G}{\ell+1}.
\tag{4}
$$

$DB_0$ 中所有含 $z_{c_*,m}$ 的项准确合为 $f_0$。其余项的颜色 $c_*$ 最高 jet 阶至多为 $m-1$。对较低颜色求导可能提高那些颜色的阶数，但不会重新产生颜色 $c_*$ 的 $m$ 阶 jet。

故 $f_0=DB_0-r_0$，且每个 $r_0$ 项在固定最高存在颜色中严格降阶。递归只处理那些尚非余类型的项，所以每个分支有限终止。每步保持全部颜色多次数，系数仍为有理数，给出 (2)。

这一论证没有使用“所有颜色中的最高导数阶下降”；那个尺度在 mixed 情形一般不下降。它使用的是固定多次数下先决定的 $c_*$。

### 2.2 唯一性

设 $DB=R\in\mathcal R_{\boldsymbol n}$。若 $B\ne0$，取 $B$ 实际依赖的颜色 $c_*$ 最高 jet $z_{c_*,j}$。因为 $n_{c_*}>0$，这个 $j$ 一定存在，而且

$$
DB=z_{c_*,j+1}\partial_{z_{c_*,j}}B
+\text{只含颜色 }c_*\text{ 的 }0,\ldots,j\text{ 阶 jet 的项}.
\tag{5}
$$

系数 $\partial_{z_{c_*,j}}B$ 非零。式 (5) 含有关于新的最高颜色 jet $z_{c_*,j+1}$ 的非零一次项，不含更高的同颜色 jet。

另一方面，$R$ 不可能含高于 $j+1$ 的同颜色 jet，否则与 $DB$ 的对应多项式系数不符；其中包含最高 $z_{c_*,j+1}$ 的每个余类型 monomial 又必须至少二次。它不能抵消 (5) 的一次项。因此 $B=0$，进而 $R=0$。

这同时排除了局部原函数常数：非零多次数不允许只依赖 $\xi$ 的多项式。证毕。

对一般有限正 profile weight 的多项式，先逐多次数应用 (2)，再相加即可。单一颜色时，该定理准确退回 [R75](R75-local-density-IBP-and-word-termination.md) 的规则与唯一性。

## 3. 正确的右端边界

所有实际输入颜色在同一个右 collar 上为零，包括所需全部 jets；固定

$$
I(f)(\xi)=\int_r^\xi f(t)\,dt.
\tag{6}
$$

因为 $B$ 有非零 profile 多次数，$B(r)=0$。故 (2) 给出原函数恒等式

$$
I(f)=B+I(R).
\tag{7}
$$

这是真正同右锚的恒等式。没有把左端 primitive 重置为零，也没有丢掉一个待支付的端点常数。

如果一个局部项没有 profile 因子，其原函数必须保留显式右端常数；定理 1 不适用于这种零多次数。下面只有在非空 word 乘子已使边界为零时才对这种多项式 letter 积分。

## 4. 一条具体 mixed 身份，以及旧循环的来源

在 $q<\bar q$ 下，由

$$
D(q'\bar q)=q''\bar q+q'\bar q'
$$

得到

$$
\boxed{I(q'\bar q')=q'\bar q-I(q''\bar q).}
\tag{8}
$$

这里 $q''\bar q$ 已是本次固定次序的余类型，因为最高存在颜色 $\bar q$ 只有零阶 jet；不能再为了降低较低颜色的 $q''$ 而反向改写 (8)。

旧 ColoredWords 的规则先取所有颜色中的最大导数阶，并且只有该阶在所有颜色里只出现一次才触发。因此它在 $q'\bar q'$ 上不降阶，从 $q''\bar q$ 出发则会改写成含 $I(q'\bar q')$ 的代表；本例中这一步本身不会形成循环。对于一般嵌套输入，旧实现另有保守的 cycle fallback，保存原 word 而不丢项，所以其已发表零证仍然 sound。这里证明的是一个新的局部唯一代表和全递归终止性，不把本例误报成旧程序已经发生的循环。

式 (8) 也展示新增规则的意义：它处理了“同阶出现在不同颜色中”的真实 IBP，而不把重复最高 jet 的单颜色余类型强行消去。

本例不是研究目标评价，不说明 (8) 中的任何一项独立、可达或具有固定符号。

## 5. 与所有深度 shuffle 一起的有限 word 递归

设每个 letter 是正 profile weight 的局部 monomial，定义

$$
I_{(m_1,\ldots,m_s)}
=I\!\left(m_1I_{(m_2,\ldots,m_s)}\right),\qquad
I_{\varnothing}=1.
\tag{9}
$$

沿用已有全部深度的 shuffle 恒等式

$$
I_uI_v=\sum_{w\in u\shuffle v}I_w,
\tag{10}
$$

包括重字产生的准确整数重数。它在同一右锚下成立；不把不同深度的 primitive 当成独立数。

考虑一次待处理的 $I(f_0I_w)$。使用 (3)–(4) 的 $DB_0=f_0+r_0$，得

$$
I(f_0I_w)
=B_0I_w-I(r_0I_w)-I(B_0DI_w).
\tag{11}
$$

若 $w$ 非空，$DI_w=m_1I_{\operatorname{tail}(w)}$。于是：

- 第二项的 word 长度相同，但局部多次数相同、最高存在颜色的最高 jet 阶严格下降；
- 第三项的剩余 word 长度严格下降，可以容许新的局部最高颜色或导数阶变化。

所以递归尺度为

$$
(\text{剩余 word 长度},
 \text{局部最高存在颜色的最高 jet 阶}),
\tag{12}
$$

按字典序严格下降。余类型 local factor 不再递归，直接作为 word 的首 letter 保留。

若局部因子是没有 profile 的 $\xi^p$，$p\ge0$，但 $w$ 非空，则

$$
I(\xi^pI_w)
=\frac{\xi^{p+1}I_w}{p+1}
-\frac{I(\xi^{p+1}m_1I_{\operatorname{tail}(w)})}{p+1}.
\tag{13}
$$

其右边界因 $I_w(r)=0$ 消失，剩余 word 长度也严格下降。空 word 的纯 $\xi$ 多项式不使用 (13)；它需要另带 $r$ 的显式原函数。

每个 local IBP 分支都没有增加所有 local factors 和 word letters 中 jet 阶数的总和；较低颜色 jet 阶可以升高，但有这个总和作为有限界。$\xi$ 的幂上升只发生于有限次的多项式-letter 降长。给定有限原 DAG 后，拓扑递归和 (12) 因而均有限。

总 profile weight 不超过 $N$ 时，所有最终 letters 都有正 weight，word 长度不超过 $N$。本课题 $N=4$；有限 shuffle 每次仍只是有限 interleaving 的和。

**定理 2。** 固定颜色次序后，以上 local 分解、全部深度 shuffle 和 (11)–(13) 给出有限、确定的 sound word 映射。其数学递归不需要 cycle fallback。实际代码的项数、时间、缓存、系数位数和内存上限仍然必要；触及预算必须报告未完成，不能把剩余 word 删除。

## 6. 共同映射的线性与可证明的结论方向

把原 DAG 的每个 jet 转成对应局部因子，把原 primitive 按 (11)–(13) 处理，乘法全部使用 (10)，对有理线性组合逐项相加。记结果为 $\Phi(E)$。

固定次序的选择是确定的，所有递归严格终止；缓存只复用已经确定的答案，不再因活动递归路径而选择 fallback。因而

$$
\Phi(aE+bF)=a\Phi(E)+b\Phi(F),\qquad a,b\in\mathbb Q.
\tag{14}
$$

每个步骤都是同右锚原函数恒等式，所以在全部允许的真实 profiles 上

$$
E=\operatorname{Eval}_{\rm word}\Phi(E).
\tag{15}
$$

特别地，$\Phi(E)=0$ 是一个完整原函数零证明。对于列 $E_j$，若新共同 word 矩阵给出

$$
\sum_j a_j\Phi(E_j)=0,
$$

则准确原差 $E=\sum_ja_jE_j$ 必须在一个新的同规则映射实例中得到 $\Phi(E)=0$；这一步直接从原差做，避免仅以列标签为证书。通过后即得完整原式恒等式。

相反，**$\Phi(E)\ne0$ 只表示这份 word 代表非零**。本稿没有证明 Eval 在所得 word 空间单射，没有证明所有普适函数恒等式都由上述规则生成，也没有以 word rank 给真实函数 rank 下界。

颜色优先级可能使 $q,\bar q$ 的代表写法不对称。它不改变实际共轭输入上的等式，不产生输入旋转的几何可达性，也不让 $\bar q$ 的实际历史变成独立控制。

## 7. 接到 R174 原函数良定义问题的精确接口

R174 已给出一个 77 维的**字面多项式**子空间 $W$，由 40 个 R 原列和 37 个被保留的 normal 原列组成。70 条旧原依赖已经完整付清，后续不重做它们。

满足 R174 已有必要关系的 12 参数外点，对这 77 列赋值，因而在 $W$ 上定义一个准确线性泛函 $\ell_y$。真正尚未支付的是它能否降到实际原函数商：

$$
E:W\longrightarrow \{\text{普适 canonical profile 函数}\}.
$$

准确的良定义条件是

$$
\ell_y\big|_{\ker E}=0.
\tag{16}
$$

本稿提供一个可实际消费的新 sound 层。由 (15)，

$$
\ker\Phi\subseteq\ker E.
\tag{17}
$$

所以只需找到 $\ker\Phi$ 中一条被 $\ell_y$ 赋成非零的真关系，就能排除该点。若 $\ell_y$ 杀掉全部已取得的 $\ker\Phi$，仍不能反推 (16)；还可能存在未被这份 word 表示消去的真实关系。

依据 [R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md)，对于这里的 canonical 完整算子，使用

$$
E\longmapsto(\pi E,\Xi E)
\tag{18}
$$

即可忠实决定完整函数，其中 $\pi$ 为 pure $-4$，$\Xi$ 为 mixed $-2$ 的 $(2,2)$ 原分量。因此新增共同矩阵可以只用这两根；新候选关系必须在它们的**原差**上分别 sound 归零，然后由 R159 得整个 canonical 原式身份。不能只测 balanced 而略掉 pure。

### 7.1 明确复用与必要新增

- 只取 R174 证书 independent_columns_of_the_literal_matrix 的 77 个原列，直接从已发 head 原根读取；不重建 forcing、响应或十四族。
- R151 已保存 40 个 pure 响应的完整 word rows、原 hash 和 31 条真实 pure 依赖。这些完整已证的 sound 代表直接消费，不重做 pure R40 或那 31 条关系。R151 实际先用旧 RightIBP、再用单颜色 word；虽然新规则在单颜色情形的局部步与 R75 一致，本稿不据此宣称旧两步输出与新 $\Phi$ 直接作用原根逐字相同。复用后的共同矩阵只是由已证等值代表组成的新线性表示；它提出的关系仍须付原差证明。若 fresh 新映射未露出零，只能保留为该验证过程未决，不能把旧 rows 的标签相同当作 fresh 零证。
- R131 完整响应导出只保存了 mixed 原根及 word hash/term count，未保存其完整 mixed word rows。新的共同 balanced 表不能凭 hash 假装已有；这部分是明确必要的新展开，而不是重建旧原响应。
- 已发 J、D0 等 pure 身份如原根 hash 正确匹配，也可直接用其已保存的准确响应组合。未匹配的 normal pure 根才需要新表示，不能把 m8 纯尾已零推广成普适 pure 身份。
- 77 列的共同有理关系可以给新的 old-free 等式；每条仍保完整原列系数和两根 fresh 原差零证。非零 word 列不增加真实独立性声明。

为消除两种映射的歧义，若所有列都由同一新规则直接展开，使用的是第 6 节的 $\Phi$。若 pure 端复用了旧 sound 代表，则把每个字面基列 $C_j$ 的被绑定代表记为 $v_j$，并在 $W$ 上**按这 77 个基列线性延拓**为

$$
\Psi\Bigl(\sum_jt_jC_j\Bigr)=\sum_jt_jv_j.
\tag{19}
$$

每个 $v_j$ 都有原列到代表的正确同锚恒等式，故 $\operatorname{Eval}\Psi=E$，仍有 $\ker\Psi\subseteq\ker E$；但不主张 $\Psi=\Phi|_W$。因此对 $\ker\Psi$ 的候选，新的 fresh $\Phi$ 原差若非零，只能报告这一额外验证未决，不能报实现错误，也不能否认 R151 的旧零证。另一种完整证书是逐列绑定 R151 的已发转换身份和新列的转换记录，再准确求和，证明每个原列到相应代表、最后代表和为零；它同样给原差身份，并且不重复 40 个 pure 目标。实际 consumer 必须明确采用哪一种证书，不能在两种映射间暗换。

这不是再次比较“第 45 列是否在某个旧空间”；目标是一个明确 12 参数候选对**全局原函数关系**是否一致。当前未通过既有路径门的外点无需为此另跑原函数计算；应针对已经通过当前完整标量 action 门的明确点，或保存可继续使用的全局新关系。

## 8. 实现和资源边界

新实现应独立于已冻结的 ColoredWords 文件，只覆盖 primitive 的颜色选择规则，并保留已有 shuffle、portable 原式读写与同锚检查。其新人工应直接检查 (8)、高低颜色 jet 的转移、多次数分解、非空 word IBP、缓存顺序不影响结果、pure 已存代表的零新正规化读取，以及错误边界/预算没有被当成零。

真实 head/word 运算只在本公开仓库 Actions。完整新 word 表、每条新原差、精确关系系数和原输入身份都应保存；预算退出必须保存已完成列和共享表示状态，不把未完成列视为零。

本稿完成的是新的局部唯一性和没有改写循环的共同 sound 映射。它为原函数良定义关系提供具体下一运算，不改变真实 signed control、端口基准、第四 ruling 或主课题的完成标准。
