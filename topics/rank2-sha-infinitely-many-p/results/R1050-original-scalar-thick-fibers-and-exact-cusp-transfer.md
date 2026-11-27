# R1050 — 原标量厚纤维的完整层数与 T、v 支撑的准确返回

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

**状态：已证明。** 本条在原完整有限自由代数中证明标量厚纤维的全部局部长度，并逐图落实到原 $T$、$v$。它不把完整非约化纤维换成约化支集，不从一个行列式猜局部重数。新的专用软件入口仍须在公开 Actions 运行；本条不宣称原四交、Norm 或 $18\times9$ 终门已经通过，更不宣称主无穷素数目标完成。

## 1. 固定同一完整代数与完整纤维

设 $k$ 为原常数域，$R=k[t]$，$A$ 为原交换 $R$-代数，并有已认证的完整自由基，秩为 $N$。取首一不可约 $\pi\in R$，记
$$
K=R/(\pi),\qquad d=[K:k],\qquad
B_m=A/\pi^mA,\quad m\ge1.
\tag{1}
$$
本条只处理实际完整理想 $\pi^mA$。在原自由基的行约定下，它的完整 Hermite 基是 $\pi^m I_N$，行列式为 $\pi^{mN}$。不得仅据后一个行列式把别的理想认作它。

在整个 $B_1$ 上，令
$$
1=e_1+\cdots+e_r,\qquad e_i^2=e_i,\quad e_i e_j=0\ (i\ne j)
\tag{2}
$$
为其实际 primitive 幂等元分解。写
$$
C_i=e_iB_1,\qquad
d_i=\dim_K C_i,\qquad
f_i=[\kappa_i:K],
\tag{3}
$$
其中 $\kappa_i$ 为这个局部 Artin 代数的剩余域。

这里 $d_i$ 是整个非约化分量的维数。它由原完整乘法算子 $m_{e_i}$ 的秩给出，不是剩余域次数 $f_i$。原厚分量中的所有 nilpotents 已包括在 $d_i$ 内。

## 2. 全部厚度的精确局部长度

**定理。** $B_m$ 的闭点与 $B_1$ 相同，且对应于 $C_i$ 的整个局部分量有
$$
\dim_k(B_m)_i=md\,d_i,\qquad
\operatorname{length}_{A_{P_i}}(A_{P_i}/\pi^mA_{P_i})
=\frac{m d_i}{f_i}.
\tag{4}
$$
其闭点度数仍为 $[\kappa_i:k]=d f_i$。因此全部闭点与真实重数满足
$$
\sum_i (df_i)\frac{md_i}{f_i}=mdN.
\tag{5}
$$

**证明。** $A$ 对 $R$ 自由，故乘 $\pi$ 在 $A$ 上单射。对 $0\le j<m$，乘 $\pi^j$ 给出完整 $A$-模同构
$$
A/\pi A \longrightarrow \pi^j A/\pi^{j+1}A.
\tag{6}
$$
满射来自定义；若 $\pi^j a\in\pi^{j+1}A$，消去非零因子 $\pi^j$ 得 $a\in\pi A$，故单射。它是 $A$-线性的，所以与每个 $P_i$ 的局部化相容。

$B_m\to B_1$ 的核由 $\pi$ 生成并且幂零，故二者的素理想集和剩余域完全相同。为把“对应局部分量”说清，也可在完整 $B_m$ 中提升 (2)：若 $x$ 是一个提升、$\epsilon=x^2-x$，则
$$
x_{\rm new}=3x^2-2x^3,\qquad
x_{\rm new}^2-x_{\rm new}=\epsilon^2(4\epsilon-3).
\tag{7}
$$
幂零误差有限次平方后为零。这给幂等元存在性；若两个幂等元同余模幂零核，则 $e(1-f)$ 和 $f(1-e)$ 都是幂零幂等元，因而均为零，故 $e=f$。原 primitive 系统于是唯一提升，正交性与总和为1也由唯一性得到。

对每个局部分量，(6) 给恰好 $m$ 层，每层为整个 $C_i$，其 $k$ 维数是 $d d_i$。这证明 (4) 的第一式。局部有限长度模的每个单因子均为 $\kappa_i$，每份 $k$ 维数为 $df_i$，故第二式成立且是整数。由 $\sum_i d_i=N$ 得 (5)。证毕。

证明没有假设纤维约化或未分歧。特别地，一个完整长度289的分量在 $m=2$ 时贡献578；不能把289替换成它的剩余域次数1。

整个局部 primary 理想也有不含歧义的定义：
$$
J_{i,m}=\ker(A\to(B_m)_i)
       =\pi^m A+(1-\widetilde e_i)A.
\tag{8}
$$
(8)右式对 $\widetilde e_i$ 任取 $A$ 中代表；两个代表的差在 $\pi^mA$ 中，故理想相同。(4) 给的是这个完整理想的局部长度，不是另一个同长度候选。本条的专用支撑入口无需物化 (8) 的 Hermite 基；若其它调用者确实需要该基、整个局部商或乘法返回，仍调用原完整分解程序，不能填入假的旧字段。

## 3. 同一完整商的范数推论

若 $h\in A$，它的乘法保持 (6) 的完整滤过，且每个伴随分次上的算子都是同一个 $\bar h$ 在 $B_1$ 上的乘法。因此
$$
\det_k(m_h\mid B_m)
=\det_k(m_{\bar h}\mid B_1)^m
=\prod_i\det_k(m_{\bar h}\mid C_i)^m.
\tag{9}
$$
所有行列式在原 $k$ 内，未改为素域绝对范数。$h$ 在 $B_m$ 中为单位当且仅当 $\bar h$ 在 $B_1$ 中为单位：幂零核中的逆元用有限几何级数提升，反向显然。

这里右边仍是整个非约化 $B_1$，并完整保留外层的 $m$ 次数。若实际目标理想不是 $\pi^mA$，不能引用 (9)。本条尚未把这个范数分支接入原一般 Artinian norm 实现。

## 4. 原 T 与 v 在两张图中的完整理想

R925 的原有限图以 $y=y_s$ 为底变量，原完整基秩 $N=306$；无穷图以 $s=1/y$ 为底变量，保原按权变换的整个基。实际源码 OriginalFractionModel.__init__ 明定
$$
y=\frac{R.{\rm gen}\cdot{\bf1}}{{\bf1}},
\qquad
v=y^2-1,\qquad
T=\frac{y^2(y^2-9)^2}{(y^2-1)^2}.
\tag{10}
$$
这是原函数身份，不是短展开拟合或另换参数。当前原执行的特征29、41均不为2或3，下面分子、分母彼此互素。

用 $(f)$ 表示整个 $A$-理想 $fA$；用于 Hermite 比较时取 $f$ 的首一 associate。原完整零、极理想严格为：

| 图与函数 | 完整零理想 | 完整极理想 |
|---|---|---|
| 有限图 $T$ | $(y^2(y^2-9)^2)$ | $((y^2-1)^2)$ |
| 有限图 $v$ | $(y^2-1)$ | $A$ |
| 无穷图 $T$ | $((1-9s^2)^2)$ | $(s^2(1-s^2)^2)$ |
| 无穷图 $v$ | $(1-s^2)$ | $(s^2)$ |

确切地，
$$
T=\frac{(1-9s^2)^2}{s^2(1-s^2)^2},
\qquad v=\frac{1-s^2}{s^2}.
\tag{11}
$$
因为分子、分母在底环中互素，Bezout 身份在整个原代数中仍成立，故没有共同零，也没有被遗漏的某个原地方。标量乘法在原全基上的矩阵为 $fI_{306}$；这直接支付全理想身份，不能只核次数。

第二图只计遗漏的 $s=0$ 边界，不能再次计有限图上的 $s=\pm1$。原完整 boundary 返回应为
$$
I_{T,+,\infty}=I_{v,+,\infty}=A_\infty,\qquad
I_{T,-,\infty}=I_{v,-,\infty}=s^2A_\infty.
\tag{12}
$$
每个式子都落实到实际完整 Hermite 矩阵相等。

于是 $T$ 的六个基纤维为 $y=0,\pm3,\pm1,\infty$，每处原理想均恰为 $\pi^2A$；$v$ 的两个有限正纤维 $y=\pm1$ 为 $\pi A$，负边界为 $s^2A_\infty$。(4) 从各个当前完整非约化纤维的实际 $d_i,f_i$ 返回全部原重数和剩余次数，无须把一般理想套成标量理想。

## 5. 从同一个 T 极点准确返回 v

保原 point 对象、完整 maximal ideal、原常数嵌入和图表身份。若 $P$ 位于 $y=\pm1$，写 $e_P=v_P(y\mp1)$。另一线性因子和 (10) 的分子均为单位，因此
$$
v_P(T)=-2e_P,\qquad v_P(v)=e_P=-\frac12v_P(T).
\tag{13}
$$
若 $P$ 位于无穷图 $s=0$，写 $e_P=v_P(s)$；(11) 的分子和 $1-s^2$ 为单位，故
$$
v_P(T)=v_P(v)=-2e_P.
\tag{14}
$$
而 $T$ 的正支撑 $y=0,\pm3$ 上 $v$ 为单位。

所以从原全部 $T$ cusp 字典到 $v$ 的准确返回是：保有限负 cusp 的同一 point 并把有号重数变为原数的 $-1/2$；保无穷负 cusp 的同一 point 和原有号重数；其余没有 $v$ 支撑。偶性由 (4)/(10) 支付，不是运行时除数猜测。

这同时给 $\operatorname{Supp}\operatorname{div}(v)\subseteq\operatorname{Supp}\operatorname{div}(T)$。所有厚度仍保留，且原代码后续的立方分歧条件 $v_P(v)\not\equiv0\pmod3$ 仍用这个完整整数，不用剩余点个数替代。

## 6. 原代码的准确消费范围与后继边界

已逐式核对的源码位置为：

- original_ys_fraction_bridge.py：OriginalFractionModel.__init__ 和 build_original_ys_fraction_maps 内 formulas，给 (10)；
- original_ys_closed_point_tools.py：residue_component 中 small_local_dimension 为整个 $m_{e_i}$ 的秩，relative_residue_degree 来自实际剩余域；
- original_projector_hermite.py：complete_residue_maximal_ideal，仍负责返回原全最大理想、全剩余坐标和真正原域；
- original_ys_geometry_transport.py：whole_signed_support 只读取每项的 point 和 intersection_multiplicity，并保整个证据记录；它不读取 local primary ideal 或其 quotient；
- original_ys_artinian_shadow_consumer.py：原 $v$ 认证还会重新核完整正理想 $(y^2-1)I_{306}$、实际总长和全部有限/无穷有号重数。

因此允许另建一个仅供这个几何支撑调用点的入口：先对 actual target 核完整 $hI_{306}$，再把 $h$ 的全部素因子与指数、同一原完整纤维/primitive 幂等元、全部原最大理想和 (4) 合成诚实的 filtration receipt。每项和必须回到 actual target 的完整长度。原剩余域和 registry 不能更换，真正非约化纤维的乘法/Frobenius/primitive 门不能只以 reduced degree 代替。

这个入口不得冒充通用 decompose_complete_primary_block 的返回。后者的包装器确会消费 full_local_primary_ideal；其 API、构造和原门均保。专用入口明确说明未物化每个 (8) 的 HNF，不填写旧完整 projector 已执行的字段。实际四交、一般分式读值、任意非标量理想及其完整 Norm 继续使用原方法。

本条据原完整代数与源身份给出证明，不重复登记 R925§14 已算的六纤维数值，也不加载旧矩阵。后继应在新运行内构造当前纤维，或只在同一进程、同一 engine/原域/原 $\pi$ 和全部关系格准确相等后复用它。没有生成或保存任何数学结果缓存。

**依据与承接。** R925§§1–7、10、14、16（原自由基、双图和完整非约化纤维）；R1033（原全部最大理想返回）；上述已固定原源码。本条新增的是准确应用完整 $\pi$ 滤过的支撑入口及 (13)–(14) 的同对象返回，不将一般厚理想只凭行列式识别成标量理想。
