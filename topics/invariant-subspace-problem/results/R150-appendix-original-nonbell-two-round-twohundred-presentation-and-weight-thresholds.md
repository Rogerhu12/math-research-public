# 原非 Bell 二轮梯度参数模、完整 200 列呈示与来源权下界

作者：OpenAI ChatGPT（literature_audit），与 /root、normal_annihilator；日期：2026-11-16。

本篇是已付原来源恒等式及已经完成的指定右端计算的代数推论，没有新增消元、候选基或新的数学数组。系数严格为合法原剩余点 $\mathbf F_{127}$、$d=100$；不把有限域压缩或负结论提升到原数域 $E$。

## 1. 去掉 Bell 列后需要证明的完整性

令
$$
B=\mathbf F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
S=B[u_0,\ldots,u_4],\qquad F=B^{10}.
$$
权约定为 $\operatorname{wt}(y)=1$、$\operatorname{wt}(w)=\operatorname{wt}(u)=2$，十轴对应原单项式
$$
m=(1,u_0,\ldots,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$
记 $b=y\cdot w$，但本节不施加 $b-1=0$。

原五个 $B$ 线性乘法矩阵为 $N_i$。六个 mean 列为 $Y_j$，二十个保留低 commutator 列为 $C_\ell$。定义只含非 Bell 列的
$$
\Gamma_0=B\langle Y_1,\ldots,Y_6,C_1,\ldots,C_{20}\rangle,
\qquad
\Gamma_r=\sum_{|v|\le r}N_v\Gamma_0.
$$
本篇证明
$$
\boxed{\operatorname{Cl}_N(\Gamma_0)=\Gamma_2}
$$
以及未加 Bell 的完整原梯度参数商
$$
\boxed{F/\Gamma_2\simeq S/(\partial R').}
$$
这里的 $\partial R'$ 保留原十七个梯度；原完整坐标与 Jacobian 运输按父证明不变。

父证据是：

- [原完整十行参数模型与全部 116 来源](R150-appendix-actual-original-ten-generator-parameter-module-and-116-certified-seeds127.md)；
- [原 116 种子的完整 50 列压缩](R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md)；
- [原十四高列换源与完整首轮](R150-appendix-original-high-source-exchange-and-thirtysix-seed-stable-closure.md)；
- [原二轮停止及完整 210 列证明](R150-appendix-original-parameter-stable-closure-stops-at-two-and-complete210-presentation.md)。

不能仅从“加 Bell 后二轮稳定”形式删除一组关系。本篇使用的是这些父证明中的非 Bell 来源身份逐步重证。

## 2. 首轮的所有必要关系均不使用 Bell

记完整有符号 commutator 为
$$
C_{ij,a}=[N_i,N_j]e_a.
$$
原低列压缩和十四个高列换源全部只使用 $Y,C,D,N_iY,N_iC$；每一条原十八来源的 Bell 坐标严格为零。因此不需要 $(b-1)F$ 就有
$$
C_{ij,a}\in\Gamma_1\quad\text{对全部十轴 }a,
\qquad
C_{ij,u_k}\in\Gamma_0.
$$
后式的准确含义是低轴 commutator 由权五 mean 的一次 $y$ 倍及二十个权六低列生成。因此
$$
N_\ell C_{ij,u_k}\in\Gamma_1.
$$

原自由十轴中的字面路径仍为
$$
N_ie_0=e_{u_i},\qquad
N_pN_qe_0=e_{u_pu_q}
\quad((p,q)\in\mathcal V),
\qquad
\mathcal V=\{(1,4),(2,3),(2,4),(3,4)\},
$$
以及 $[N_i,N_j]e_0=0$。这些并非只在加 Bell 后的商中成立。

对原普通二次正规式
$$
N_ie_{u_j}=\rho_{ij,0}e_0+\sum_k\rho_{ij,k}e_{u_k}
+\sum_{(p,q)\in\mathcal V}\rho_{ij,pq}e_{u_pu_q}
$$
定义有序算子
$$
Q_{ij}=N_iN_j-\rho_{ij,0}I-\sum_k\rho_{ij,k}N_k
-\sum_{(p,q)\in\mathcal V}\rho_{ij,pq}N_pN_q.
$$
全部 $\rho$ 在中心环 $B$ 中。字面路径给 $Q_{ij}e_0=0$。对一次轴，
$Q_{ij}e_{u_k}=[Q_{ij},N_k]e_0$ 只含低轴 commutator；对保留二次轴，
$$
Q_{ij}N_pN_qe_0
=[Q_{ij},N_p]N_qe_0+N_p[Q_{ij},N_q]e_0.
$$
展开只出现 $N_aC_{bp,u_q}$、完整 commutator 在某个十轴向量上的作用，以及低轴 commutator 的一次 $N$ 像。上述首轮关系已完整支付它们，因此
$$
Q_{ij}F\subset\Gamma_1.
$$
此处没有假设 $\Gamma_1$ 已经稳定，也没有使用任何 Bell 列。

原十一矩梯度 $G_g$ 的完整二次正规式为零。将其固定有序算子写为 $\widehat G_g$，原二次单位关系给
$$
\widehat G_gF\subset\Gamma_1\qquad(0\le g<11).
$$

## 3. 三次关系仍给二轮停止

已付原 $35\times55$ 三次常数单位及二次回填，为每个普通三次单项式给出
$$
u_iu_ju_k
=\sum_g\left(\sum_\ell a_{g\ell}u_\ell+a_g(y,w)\right)G_g
+\sum_{a=0}^9r_a(y,w)m_a.
$$
这里 $a_{g\ell}$ 是固定系数域常数，$a_g,r_a\in B$；没有参数逆，原 $G_g$ 来源的 $u$ 次数至多一次。

按固定次序代入 $N$ 时，所有词序误差只有
$$
[N_i,N_j]F,\quad
N_\ell[N_i,N_j]F,\quad
[N_i,N_j]N_\ell F.
$$
它们分别在 $\Gamma_1,\Gamma_2,\Gamma_1$。最后一项使用 commutator 对整个 $F$ 的像，不能误用尚未证明的首轮稳定性。原主要项 $N_\ell\widehat G_gF$ 也在 $\Gamma_2$。

故任意三字算子减去仅用 $I,N_i$ 和四条保留二字路径的算子，其整个像落入 $\Gamma_2$。作用于 $\Gamma_0$，所有长度三的种子像均在 $\Gamma_2$。而 $\Gamma_2$ 按定义由长度至多二的种子像生成，所以
$$
N_i\Gamma_2\subset\Gamma_2,\qquad
\operatorname{Cl}_N(\Gamma_0)=\Gamma_2.
$$
稳定性只在这最后一步得到，证明不循环。

## 4. 完整 200 列及原十七梯度商

先按完整 commutator 统一二字顺序，再用 $Q_{ij}F\subset\Gamma_1$ 降到四条保留路径，得到
$$
\Gamma_2=\Gamma_1+
B\langle N_pN_qY_j,N_pN_qC_\ell:(p,q)\in\mathcal V\rangle.
$$
原首轮的非 Bell 列数为 $96$：六列权五、二十列权六、三十列权七以及四十列权八。四十个权八列可以用原十四个 $D$ 加已保留的二十六个 $N_iC_\ell$；不需要另作参数除法。

新增 $24+80$ 列的权分别为 $9$ 和 $10$。因此有带真实原来源公式的完整呈示
$$
B^{200}\longrightarrow F\longrightarrow S/(\partial R')\longrightarrow0,
$$
其命名生成列权的分组为
$$
\boxed{5^6,\ 6^{20},\ 7^{30},\ 8^{40},\ 9^{24},\ 10^{80}.}
$$
这是列数与权的声明，不是独立列数、参数秩或新数组运行结果。

双向完整性如下。每个种子和每次乘法都有纯原十七梯度来源：
$$
m v=(\partial R')\sigma(v),\qquad
\sigma(N_iv)=u_i\sigma(v)-S_iv.
$$
原边界矩阵 $S_i$ 的 Bell 来源坐标为零。因此 $e_a\mapsto m_a$ 给 $F/\Gamma_2\to S/(\partial R')$。

反之，稳定性使 $N_i$ 在 $F/\Gamma_2$ 上定义作用；完整 commutator 使其可交换。原字面路径使商由 $e_0$ 循环生成。全部十一矩梯度由 $\widehat G_gF\subset\Gamma_1$ 杀掉，六个原 mean 梯度由其完整原正规式 $Y_j$ 杀掉，所以 $1\mapsto e_0$ 给反向映射。两复合在 $1$ 及全部十个字面路径上为恒等。这一步也不需要 Bell 关系。

## 5. 已完成的低权计算现在属于完整齐次参数模

因为参数环只有非负权，新增权 $9,10$ 的生成列不能影响权 $7,8$。取任意来源表达式的相应齐次部分即可严格得到
$$
(\Gamma_2)_7=(\Gamma_1)_7,\qquad
(\Gamma_2)_8=(\Gamma_1)_8.
$$
不存在用更高权列相消而产生一个新的较低齐次分量的例外。

两个已完成的父矩阵正给这些完整低权部分：

| 权 | 原矩阵 | 已付秩 |
|---|---:|---:|
| $7$ | $7754\times312$ | $312$ |
| $8$ | $17674\times1386$ | $1312$ |

[七个原右端计算](../notes/2026-11-16-r150-original-rank-four-bounded-rhs127-boundary-789f.md) 已付
$$
b\delta e_0\notin(\Gamma_2)_7,\qquad
y_i b\delta e_0\notin(\Gamma_2)_8\quad(0\le i\le5).
$$
没有计算或声称任何 $\delta^2$ 余式。

[四个字面规范二次式计算](../notes/2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-boundary-789f.md) 由原规范系数块 $\operatorname{diag}(1,2,2,2)$、全部 $1312$ 原单位坐标上的目标为零及该单位限制的单射性，已付
$$
\operatorname{span}_{\mathbf F_{127}}\{q_jb^2e_0:0\le j\le3\}
\cap(\Gamma_2)_8=0.
$$
因此这个四维空间在完整齐次梯度参数商中仍独立非零，原增广矩阵秩恰 $1316$。此推论不要求重新计算新增 $104$ 列。

经 §4 的完整同构，上述特定多项式 $b\delta,y_i b\delta,q_jb^2$ 也给原 $\mathbf F_{127}$ 十七梯度商中的非零类。这不是 $q_j$ 或 $\delta$ 在加 Bell 理想、$b$ 饱和理想中的非成员性；更高的 $b$ 倍仍可能为零。也没有特征零非成员性推论。

## 6. 准确的参数呈示来源权与新下界

在上述 $200$ 个参数列的呈示中，定义来源权至多 $K$ 的 Bell 表示为
$$
fe_0=G+(b-1)H
$$
且每个参数系数单项式的权加对应命名梯度列的权至多 $K$，并满足 $\operatorname{wt}(H)+3\le K$。这一约束禁止先使用更高权来源、再只因最高项相消而降低来源权。

$B$、$F$ 及 $\Gamma_2$ 都按整数权分次，乘 $b$ 使权增加 $3$。故可以把等式投影到目标权模 $3$ 的那一类；其它同余类不会影响目标，也不会增大来源权。

### 四维规范 q 空间

令 $0\ne q\in\operatorname{span}_{\mathbf F_{127}}\{q_0,q_1,q_2,q_3\}$，其权为 $2$。若来源权至多 $10$，目标同余类可出现的梯度权只有 $2,5,8$，Bell 系数只需保 $H_2,H_5$。由于 $\Gamma_2$ 的最低权为 $5$，
$$
H_2=-qe_0,\qquad H_5=G_5-bqe_0,\qquad
b^2qe_0=G_8+bG_5\in(\Gamma_2)_8.
$$
这与 §5 的整个四维交零矛盾。因此
$$
\boxed{\text{每个非零规范 }q\text{ 组合均无此参数呈示内来源权至多 }10\text{ 的 Bell 表示。}}
$$
不能删掉中间可能非零的 $G_5$；上式已完整保留它。

### 固定四阶图 delta

$\delta=\delta_{14}$ 的权为 $4$。若来源权至多 $9$，目标同余类的最高梯度权仍为 $7$。最低权比较给 $H_1=0$、$H_4=-\delta e_0$，随后
$$
G_7=b\delta e_0.
$$
这与原权七非成员性矛盾。因此
$$
\boxed{\delta_{14}\text{ 无此参数呈示内来源权至多 }9\text{ 的 Bell 表示。}}
$$
这不是关于六个 $y_i\delta$ 的同样推论，因为它们的最低权已经是 $5$。

## 7. 本篇的边界与下一不同问题

上述新来源权下界严格属于此 $200$ 列参数呈示。若把它们改称任意原十七或十八生成元来源的最小权，仍需另证明原源与参数呈示之间的双向过滤保持；本篇不作该转换。§5 的原十七商中非零类来自不带过滤的完整商同构，是不同且已说明的推论。

新增 $104$ 列的实际生产另有独立有预算消费者；本篇没有将该生产预填为完成。所有稳定性与来源公式均只用已付原恒等式。

下一不同的低权目标是 $\delta b^2e_0$ 的权 $10$ 和 $q_jb^3e_0$ 的权 $11$。把新增 $104$ 列加入后再重跑已付 $q_jb^2e_0$ 不会改变答案。本篇没有建立或运行任何权 $10$、$11$、$12$ 的大矩阵，也没有证明 Bell 商为零。


## 根独立复核记录

/root（OpenAI ChatGPT / GPT-6 Astra Pro，2026-11-16）逐节复核全部正文。$Q_{ij}$ 的完整十轴展开只需首轮已付的低 commutator 一次像及完整 commutator；三次词序误差只在第二轮使用一次作用，稳定性没有循环。正权分次保证高权列不能贡献权七/八部分。规范 $q$ 的权 $2,5,8$ 比较保留非零 $G_5$，准确给 $b^2q=G_8+bG_5$；$\delta$ 的权 $1,4,7$ 比较给 $H_1=0,H_4=-\delta e_0,G_7=b\delta e_0$。正文的原十七商非零结论和仅在命名参数呈示中的过滤下界严格区分。normal_annihilator 已独立交叉复核通过；本结论不依赖新增104列数组已运行，也不声称加Bell商非零或特征零非成员性。
