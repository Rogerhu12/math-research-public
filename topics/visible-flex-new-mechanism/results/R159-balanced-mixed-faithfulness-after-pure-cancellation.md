# R159：pure 消去后的完整成本由 balanced mixed 原式忠实决定

日期：2026-11-15。**已证明的普适函数结构与既有真实维数推论。** 本稿只作纸面推导和已发表结果的逻辑组合，不运行新的研究计算。使用 [R78](R78-complete-phase-P1-symmetric-square-conditions.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R131](R131-third-G-translation-separation-and-111-query-control.md)、[R151](R151-general-pure-J-identity-nine-dimensional-range-and-kernel.md)、[R156](R156-input-phase-rotation-fails-canonical-cost-invariance.md) 和 [R157](R157-general-pure-D0-identity-and-34-dimensional-zero-pure-kernel.md)。

主结论是一个准确的成员门：**目标与比较空间先已证明 pure 为零后，完整 canonical 函数成员关系，等价于 mixed $-2$ 模式的 $(q^2,\bar q^2)$ 双次数原式成员关系。** 该投影对这个函数空间单射。R151 的 31 条真实 pure 关系因此直接给一个 31 维、完整且忠实的响应核比较空间；R157 的 34 维已知完整 pure 核也忠实转成 34 维 balanced 像，无须重算旧原列或旧关系。

本稿不把投影值当成实际成本，不使用输入相位旋转的几何可达性，也不从新的商方向独立性推出 signed control。

## 1. 函数空间和完整两槽公式

固定共同物理区间与右 collar。令 $\mathcal P$ 是该区间上满足共同右 collar 条件的实光滑 profile 向量空间，随后作普通复线性延拓。几何、端口和所有右原函数锚保持不变。

对一条完整 canonical 路径，或此类完整成本的实线性组合，使用 R156(6)–(8) 的函数值双线性表

$$
K:\operatorname{Sym}^2\mathcal P\times
\operatorname{Sym}^2\mathcal P\longrightarrow\mathcal F,
\qquad K^T=K,
$$

$$
L:\operatorname{Sym}^2\mathcal P\times
\operatorname{Sym}^2\mathcal P\longrightarrow\mathcal F.
$$

$\mathcal F$ 表示整个 $\xi$ 函数的实向量空间。$K,L$ 包含整条路径的全部累计二、三阶历史，不是把历史置零后的局部替代式。

固定

$$
F=f^2,\qquad P=\phi_\theta^2,\qquad
\phi_\theta=\cos\theta f+\sin\theta g,\qquad D=F-P,
$$

则完整成本是

$$
V(F,\phi_\theta)=K(D,D)+L(P,D)
=L(F,D)+Q(D,D),
\qquad Q=K-\operatorname{Sym}L.
\tag{1}
$$

令 $\pi V=V_{-4}$，其中模式使用 $\zeta=e^{-i\theta}$。R78 给

$$
\pi V(q)=\frac1{16}Q(q^2,q^2),\qquad q=f+ig.
\tag{2}
$$

本文的 $\pi V=0$ 始终是对全部共同右 collar profiles 成立的**普适原式身份**。一个固定幂尾、一个固定圆、若干采样或模素数为零，都不替代这个前提。

## 2. pure 恒等式的完整极化及它没有强制的条件

$Q$ 对两个对称平方槽对称。由 (2)，$\pi V=0$ 等价于

$$
Q(a^2,a^2)=0\quad\text{对全部实或复 }a.
\tag{3}
$$

四次极化准确给

$$
\boxed{
Q(a\odot b,c\odot d)+Q(a\odot c,b\odot d)
+Q(a\odot d,b\odot c)=0.
}
\tag{4}
$$

例如

$$
Q(a^2,a\odot b)=0,\qquad
Q(a^2,b^2)+2Q(a\odot b,a\odot b)=0.
\tag{5}
$$

这说明 $Q$ 的完整四线性对称化为零，**不说明 $Q=0$**。在原表中，(4) 只要求

$$
\operatorname{Sym}_4K=\operatorname{Sym}_4L.
\tag{6}
$$

它没有单独消去 $L$ 的换槽反对称部分，也没有消去两个对称平方槽中的其余四线性部分。特别不能从 universal pure 身份推出某个未证明的外槽交换律。

剩余数据可以准确收为一张表。因为 $F=f^2$、$P=\phi^2$ 都是真正的平方槽，(3) 给 $Q(F,F)=Q(P,P)=0$，于是

$$
Q(D,D)=-2Q(F,P)=2Q(F,D).
$$

定义

$$
\boxed{B=L+2Q=2K-L^T.}
\tag{7}
$$

代回 (1)，得到

$$
\boxed{
\pi V=0
\quad\Longrightarrow\quad
V(F,\phi)=B(F,F-\phi^2).
}
\tag{8}
$$

这里所有 $Q$ 修正都被准确并入 $B$；没有把它们在几何路径上删除。

### 2.1 B 是唯一的完整函数表

如果一张双线性表 $B$ 使右端 (8) 对所有 $f,g,\theta$ 为零，先取 $\theta=\pi/2,g=0$，得到 $B(f^2,f^2)=0$。再取任意 $g$，得到

$$
B(f^2,g^2)=0.
$$

平方槽通过极化张成 $\operatorname{Sym}^2\mathcal P$，故 $B=0$。所以 (8) 的 $B$ 完全由 canonical 成本函数确定；即使某个 $K,L$ 表示存在冗余，$B$ 也不依赖这种表示。

在纯代数层面，(8) 没有强迫 $B$ 再满足某个对称性：对任意双线性表 $B$，形式选择 $K=\operatorname{Sym}B,L=B$ 就有 $Q=0$，并产生 (8)。这只是说明从 pure 身份单独不能推出更多张量约束，**不是**任意 $B$ 的真实几何可达性声明。

R81 的已证真实 hook 响应在 $g=0$ 时为 $C_f\sin^2\theta$、$C_f\ne0$，也直接说明实际 $B(f^2,f^2)$ 并不被 pure 消去。

## 3. balanced mixed 投影的精确定义和忠实性

在 $\pi V=0$ 时，(8) 的 $-2$ 模式是

$$
\boxed{V_{-2}=-\frac14B(f^2,q^2).}
\tag{9}
$$

展开 $f=(q+\bar q)/2$ 得

$$
V_{-2}
=-\frac1{16}B(q^2,q^2)
-\frac18B(q\odot\bar q,q^2)
-\frac1{16}B(\bar q^2,q^2).
\tag{10}
$$

定义 $\Xi$ 为 mixed $-2$ 原式中，恰含两个 $q$ 和两个 $\bar q$ 的双次数分量。由 (10)

$$
\boxed{\Xi V=-\frac1{16}B(\bar q^2,q^2).}
\tag{11}
$$

这是函数空间中的线性投影。原 DAG 的微分、乘积和同右锚 Volterra 积分保持相应颜色次数，因此可以直接从完整原表达式抽出该分量。输入相位的形式 Fourier 投影也能定义同一个函数操作，但不把输入旋转当作保持 $U$ 的实际路径变换；R156 已证明后者一般错误。

**忠实性定理。** 在普适 canonical pure-zero 函数空间中，

$$
\boxed{\Xi V=0\quad\Longleftrightarrow\quad V=0.}
\tag{12}
$$

**证明。** 只需证明 $B(\bar q^2,q^2)=0$ 对全部复 $q$ 蕴含 $B=0$。

任取一个有限维实 profile 子空间，写
$q=\sum_j z_j e_j$。则

$$
B(\bar q^2,q^2)
=\sum_{i,j,k,l}
\bar z_i\bar z_j z_k z_l\,
B(e_i\odot e_j,e_k\odot e_l).
\tag{13}
$$

这是 $\bar z,z$ 双次数 $(2,2)$ 的函数值多项式。令
$z=x+iy$，$x,y$ 为独立实坐标。若 (13) 对全部实 $x,y$ 恒零，
其各个实多项式系数都为零。复化后可反代

$$
x=(a+b)/2,\qquad y=(b-a)/(2i),
$$

得到外、内槽独立的身份

$$
B(a^2,b^2)=0
\quad\text{对所有独立复 profiles }a,b.
\tag{14}
$$

再用

$$
\begin{aligned}
16B(a\odot b,c\odot d)
={}&B((a+b)^2,(c+d)^2)
-B((a+b)^2,(c-d)^2)\\
&-B((a-b)^2,(c+d)^2)
+B((a-b)^2,(c-d)^2)
\end{aligned}
\tag{15}
$$

得 $B=0$。所需任意四个 profiles 均包含在某个有限维实子空间内，
所以这个论证适用于整个 $\mathcal P$。对函数值，可逐 $\xi$ 应用该恒等式，
或在有限模板输出空间中逐坐标应用；没有选取独立的 Volterra 原函数值。
最后由 (8) 得 $V=0$。反向显然。证毕。

这里依赖的是所有复 profile 输入的多项式恒等式；单个 $q$ 的取值、
单个幂尾或一个孤立复数相位不具有 (13) 的系数独立性。也不能将
$\bar q$ 在真实原评价中任意赋值而不支付其与 $q$ 的关系。

## 4. 成员关系的等价门

令 $E$ 是已知的 canonical pure-zero 实函数线性空间，$X$ 也是已证明
pure-zero 的 canonical 函数。由 (12) 的线性性，

$$
\boxed{
X\in E
\quad\Longleftrightarrow\quad
\Xi X\in\Xi E.
}
\tag{16}
$$

若右端用同一组实常数 $a_i$ 给出准确原式身份

$$
\Xi X=\sum_i a_i\Xi E_i,
$$

则差 $X-\sum_i a_iE_i$ 先已有普适 pure 恒零，再由 (12) 得整个
canonical 函数恒零。参数必须对全部输入、全部相位和两个完整槽共用；
不能逐查询选择不同系数。

这给后续实际 consumer 一个小而完整的正确性门：

1. 先绑定目标和比较向量的真实完整原根，以及已发表的普适 pure-zero 身份；
2. 只从各自 mixed $-2$ 原根选择双次数 $(2,2)$ 部分；
3. 新候选关系必须在这些**原表达式的差**上作 sound 归零，不能只比较不完备 NF 标签；
4. 若要宣称非成员，仍须有真实比较空间上界及达到该上界的原有理评价，
   再以增广非零子式分离。非零不完备 NF 或模素数零均不够。

(16) 不要求把其它 mixed 荷再运行一次。它也没有把形式投影关系变成
独立实际控制；实际成本基准、端口与任何 signed control 仍须由已有真实构造另行支付。

### 4.1 目标原本尚未 pure-zero 时

给原完整响应空间 $R$。如果已准确找到 $K_0\in R$ 满足
$\pi X=\pi K_0$，令

$$
H=X-K_0,\qquad R^0=R\cap\ker\pi.
$$

则

$$
\boxed{
X\in R
\quad\Longleftrightarrow\quad
H\in R^0
\quad\Longleftrightarrow\quad
\Xi H\in\Xi R^0.
}
\tag{17}
$$

第一步的 pure 消去必须是普适原式证明，不能把旧模坐标提升为有理系数。
不同准确 $K_0$ 之差属于 $R^0$，所以最后的商类与该选择无关。

比较空间必须是 $R^0$。直接将全部未消 pure 的响应投到 $(2,2)$，
再声称其张成等价于 (17)，会允许不满足 pure 约束的组合，因而不合法。

更一般地，令

$$
U^p=\{X\in U:\pi X\in\pi R\}.
$$

则准确 pure 消去及 (12) 给

$$
U^p/R
\cong (U\cap\ker\pi)/(R\cap\ker\pi)
\cong
\Xi(U\cap\ker\pi)/\Xi(R\cap\ker\pi).
\tag{18}
$$

最后一个等号只比较实际函数空间及其像，没有声称 $\Xi$ 保成本锥。

## 5. R151 已直接给出 31 个完整响应核基

固定 profile 仿射权 $-2$，记该权真实完整响应空间为 $R_{-2}$。
R131 的完整两模式原式关系与原非零子式证明

$$
\dim R_{-2}=40.
$$

按 R151 的消费顺序，将同一组 40 个**完整两模式**真实基记作
$C_0,\ldots,C_{39}$。这里下标是 R151 的 **original_position**，
不是 R116 的全局列号。

R151 已用 31 条 fresh 原式差证明纯像由以下九个位置张成：

$$
I=\{0,1,2,3,8,9,10,12,19\}.
\tag{19}
$$

它们的 R116 全局列号依次是

$$
0,\ 48,\ 88,\ 112,\ 41,\ 73,\ 81,\ 193,\ 170.
$$

再利用 R131 已有非零 $40\times40$ 原 minor 中的九条 pure 行，
R151 得到真实维数

$$
\dim\pi R_{-2}=9.
\tag{20}
$$

对每个 $j\notin I$，消费已发表的准确有理关系

$$
\pi C_j=\sum_{i\in I}a_{ij}\pi C_i
$$

并定义完整向量

$$
\boxed{D_j=C_j-\sum_{i\in I}a_{ij}C_i.}
\tag{21}
$$

这不重新计算响应：$C_i$ 的两个原模式均已在 R131 原导出中保存，
$a_{ij}$ 及 pure 原差零证书已在 R151 保存。

每个 $D_j$ 准确属于 $R_{-2}\cap\ker\pi$。它们独立的理由是直接的
三角结构：若 $\sum_{j\notin I}b_jD_j=0$，在原 40 个真基 $C_i$ 中，
位置 $j\notin I$ 的系数恰为 $b_j$，故全部 $b_j=0$。再由 (20)

$$
\dim(R_{-2}\cap\ker\pi)=40-9=31,
$$

所以这些 31 个 $D_j$ 恰为整个响应 pure 核的一组基。由 (12)

$$
\boxed{
\dim\operatorname{span}\{\Xi D_j:j\notin I\}=31.
}
\tag{22}
$$

这是真实原函数维数，不是新 NF 秩或模秩推测。没有必要重新运行
40 个原列、31 条 pure 依赖或新的独立性采样来建立 (22)。

可复用的准确公开入口是：

- notes/actions-43653293263-1-g_translation_successor/ 的完整 R131 原响应导出；
- notes/actions-43657785023-1-general_pure_J_membership/general-pure-J-membership-certificate.json.gz，
  其中 **new_pure_dependency_proofs** 保存 (21) 的有理系数与原差，
  **pure_response_upper_bound.retained_original_positions** 给 (19)；
- 同一 R151 证书的 **pure_column_representatives** 保存已有全部 pure 代表，
  后继不应重编这些原列来获取同一结论。

构造新 $(2,2)$ 消费输入时，仅需从已发完整 mixed 原根作 (21) 的线性组合
及颜色投影。是否值得实际执行，应由一个具体的新目标决定；
本稿没有启动一轮“复验 31 维”的计算。

本节也没有声称 $\dim\Xi R_{-2}=31$：这里确定的是
$\Xi(R_{-2}\cap\ker\pi)$，并非不带 pure 约束的全部 40 列投影。

## 6. G、J、D0 三个新商方向的 balanced 像

记 $G_3=\mathsf N^3G$，不是 $G$ 的三次乘积。
R138 已付 $G$ 及其整个仿射轨道的 pure 像属于 $\pi R$；
R151 已付 $J$ 的同一性质；R157 的公开实际原式证明则给
$\pi\mathcal D_0=\pi K_D$，其中 $K_D$ 是已发表的九项准确有理响应组合。

因此可以选完整响应校正，使

$$
H_{G_3},\qquad H_J=J-K_J,\qquad H_D=\mathcal D_0-K_D
$$

都是真正的 pure-zero 成本向量。
R131/R136/R153 的原分离结果依次给三个类模 $R_{-2}$ 独立。
R157 据此准确得到

$$
E_D=R_{-2}+\operatorname{span}\{G_3,J,\mathcal D_0\},
$$

$$
\dim E_D=43,\qquad \dim\pi E_D=9,\qquad
\dim(E_D\cap\ker\pi)=34.
\tag{23}
$$

由 (12)，这些已有真实独立性直接转为

$$
\boxed{\dim\Xi(E_D\cap\ker\pi)=34,}
\tag{24}
$$

该空间由 31 个 $\Xi D_j$ 与
$\Xi H_{G_3},\Xi H_J,\Xi H_D$ 张成；后三者模 $\Xi R^0_{-2}$ 仍独立。
这不需要新的原有理矩阵或 profile 评价。

下一条已取得 accurate pure 响应身份的原目标，若要检查它是否进入
$E_D$，便可只对其 pure-zero 代表的 balanced 原根使用这个 34 维比较空间。
若要只问是否属于 $R$，比较空间仍为 31 维，不能将已有新商方向
不经说明地并入响应。

这些结论保留的是实际函数独立性。没有声称 $H_J,H_D$ 已可由正长度
实际词取任意正负值；R122 已付的 $G$ 轨道与新的非 lineality 商
仍须区分，也不因 (24) 增加已有总维数下界。

## 7. 一般完整成本也有唯一的两张表

以下补充解释为什么 pure 与 balanced mixed 是自然的一对完整数据，
同时说明不能在第 4 节省掉 pure 前提。

对一般 $Q$，定义其完整四线性对称化

$$
S(a,b,c,d)
=\frac13\bigl\{
Q(a\odot b,c\odot d)+Q(a\odot c,b\odot d)
+Q(a\odot d,b\odot c)
\bigr\}.
\tag{25}
$$

将 $S$ 也视为两个对称平方槽上的表，令 $Q_0=Q-S$。
则 $Q_0(a^2,a^2)=0$。保留一般的

$$
B=2K-L^T=L+2Q,
$$

由第 2 节同一 rank-one 平方计算得到

$$
\boxed{
V(F,\phi)
=B(F,F-\phi^2)
+S(\phi,\phi,\phi,\phi)-S(f,f,f,f).
}
\tag{26}
$$

证明只需将
$L(F,D)+Q_0(D,D)+S(D,D)$
写成 $(B-2S)(F,D)+S(D,D)$，
再用 $D=F-\phi^2$ 展开；全部恒等式均在同一完整函数空间中成立。

两个原模式因此为

$$
V_{-4}=\frac1{16}S(q,q,q,q),
\tag{27}
$$

$$
V_{-2}
=-\frac14B(f^2,q^2)+\frac14S(q,q,q,\bar q).
\tag{28}
$$

(28) 的 balanced 分量仍是 (11)；$S$ 项属于双次数 $(3,1)$。
由普通四次极化，(27) 唯一决定 $S$；由 (13)–(15)，
balanced 分量唯一决定 $B$。所以

$$
\boxed{
V\longmapsto(\pi V,\Xi V)
\text{ 在完整 canonical 函数空间上单射。}
}
\tag{29}
$$

其它 mixed 荷的原式由这两张表恢复：

$$
(V_{-2})_{(4,0)}=-B(q^2,q^2)/16,
$$

$$
(V_{-2})_{(3,1)}
=-B(q\odot\bar q,q^2)/8+S(q,q,q,\bar q)/4.
\tag{30}
$$

(29) 是普适原式分解，不是对某个固定 $q$ 的两个数作维数计数。
它也不把 $S(\phi^4)-S(f^4)$ 称为已经无成本支付的 profile gauge。

若只保 $\Xi V=0$，只能推出 $B=0$，仍可能留下 (26) 的完整四次
单-profile 差。因此第 4 节的 pure-zero 前提不可删除。
反过来，pure 和 balanced 两个原差都已 sound 归零时，
无需另行重算 (30) 的两个冗余混合分量来证明同一 canonical 函数身份。

## 8. 已付与未付

已付的是：

- universal pure 恒等式的完整四槽极化及其对 $L$ 的准确限制；
- pure-zero 完整成本的唯一双线性表，以及 balanced mixed 投影的忠实性；
- 先消 pure 后的完整成员关系等价门；
- 由 R131/R151 旧原证书直接推出的 31 维完整响应核及其 31 维 balanced 像；
- R157 已知 34 维完整 pure 核的 34 维 balanced 像；
- 一般 canonical 成本由 pure 和 balanced 两张原函数表忠实确定的分解。

本稿没有计算新的目标商，没有假定全部 $U$ 的 pure 像均已属于响应像，
也没有把线性投影改称成本锥的对称。端口基准、实际有限负成本、
第四 ruling、更高阶和主课题完成标准保持原来的待支付状态。
