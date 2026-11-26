# R699 — 完整SO3积分范数正定白化与带状QR

**状态：已证明（仅指正文完整证明的恒等式、条件命题与适用范围）。**

本文件按根README3、8、12正式登记已有完整证明；没有重做科学计算或把旧结论算作新进展。[原完整笔记](../notes/2026-11-26-integral-so3-norm-positive-whitening-and-banded-qr.md)保持原字节（SHA256 `8ff55d0d54155ef5eae933f9b7c8340f9bcdc47c2b14347e90c148959dc4cd6d`）。原文中实施/运行状态以其记录时点理解；当前真实结果见[HANDOFF](../HANDOFF.md)。没有将条件界、失败或数值证据升级为所求闭族的存在证明。

日期：2026-11-26。本文只做完整源码、解析及实际登记记录的读取；没有计算当前网格的数值范数、因子、条件数、场、J/J*、QP 或任何科学 fixture。新增 QR 实现由 construction 代理独立负责；本文给出其完整数学与接口规范，不把准备新实现作为原 integral 分支实际求解的前门。

## 1. 所核完整来源与实际证据

完整来源是：

- [so3_closed_meridian_operator.py](../scripts/resume_20261126/so3_closed_meridian_operator.py)，SHA256 234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42；
- [so3_axisymmetric_meridian_operator.py](../scripts/resume_20261126/so3_axisymmetric_meridian_operator.py)，SHA256 7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf；
- [gauss_observed_closed_gram.py](../scripts/resume_20261120/gauss_observed_closed_gram.py)，SHA256 26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d，其中 hermite_weights 给出完整共享五次的三个物理径向 jet。

已用纯 stdlib AST 比较确认，前两个完整文件中的 RotationH2Coordinates **整个类 AST 相同**。以下核验同时适用于这两个已刊版本，不把其中一份改名作另一种算法。

已刊 [完整 SO(3) 入口说明](../notes/2026-11-26-complete-closed-SO3-meridian-solver.md) 和 [独立轴对称入口说明](../notes/2026-11-26-independent-axisymmetric-so3-complete-entry.md) 都只说：integral 分支若普通带状 Cholesky 失败，就实际报错，不静默改范数。这是失败处理规则，不是已经发生过的数值失败。

对当前可读的相关 notes、2026-11-26 公开 Actions 分卷、HANDOFF、log、open 和相关 ready 做文本检查，**未找到当前 SO(3) integral 分支已经实际失败的登记证据**。03b 的实际 [第1卷](../notes/2026-11-26-public-actions-45820592817-1-part-001.md)、[第2卷](../notes/2026-11-26-public-actions-45820592817-1-part-002.md)、[第3卷](../notes/2026-11-26-public-actions-45820592817-1-part-003.md) 及 [第4卷](../notes/2026-11-26-public-actions-45820592817-1-part-004.md) 可见的相应 norm_kind/命令都是 jet-sum。这一检索结论不证明 integral 必定成功，也不替未返回或未保存的运行编造状态。

[节点 jet 范数与径向积分控制](../notes/2026-11-26-node-jet-norm-and-radial-integral-control.md) 已完整证明 jet-sum 在共享五次细化族中不一致控制径向积分 H²。本文不重复该局部反例；本次新增内容是 integral 的准确正定和全变量坐标核验、实际未返/失败边界，以及保持同一积分范数的带状 square-root 实现规范。

## 2. 自由槽、插值及准确积分矩阵

令正网格宽度为 $h_j=s_{j+1}-s_j>0$，$J$ 为节点数。每一角通道的完整节点三 jet 依次为

$$
(f(s_0),f_s(s_0),f_{ss}(s_0),
 \ldots,f(s_{J-1}),f_s(s_{J-1}),f_{ss}(s_{J-1})).
$$

234ac/7f 的 radial_free 是按原槽序排列的完整自由子集。仅由原表示固定的三个槽为

$$
0,\qquad 3(J-1),\qquad 3(J-1)+1.
$$

以下不删除任何其他自由槽、角通道、core 或 H。

在一胞内取 $u=(s-s_j)/h_j$。完整 Hermite 基写为

$$
\begin{aligned}
B_0&=1-10u^3+15u^4-6u^5,\\
B_1&=u-6u^3+8u^4-3u^5,\\
B_2&=\tfrac12u^2-\tfrac32u^3+\tfrac32u^4-\tfrac12u^5,\\
B_3&=10u^3-15u^4+6u^5,\\
B_4&=-4u^3+7u^4-3u^5,\\
B_5&=\tfrac12u^3-u^4+\tfrac12u^5.
\end{aligned}
$$

若局部端 jet 为 $v=(Y_0,U_0,A_0,Y_1,U_1,A_1)^T$，则

$$
f=\sum_{i=0}^{5}B_i\,d_i\,v_i,\qquad
(d_0,\ldots,d_5)=(1,h_j,h_j^2,1,h_j,h_j^2).
$$

令 $W_r(h,u)$ 为这个式子的第 $r$ 阶物理 s 导数行向量，$r=0,1,2$。源码的 hermite_weights 恰返回三行 $W_r$，包括 $h^{-r}$ 和端 jet 的 $h,h^2$ 因子，没有把局部 u 导数误当物理导数。

固定 $\ell>0$。以 $E_j$ 把完整全局自由向量 y 嵌入本胞的六个端槽，固定槽值为零。径向积分二次型为

$$
y^T G y=
\sum_j\int_{s_j}^{s_{j+1}}
 \left(f_y^2+\ell^2(f_{y,s})^2+\ell^4(f_{y,ss})^2\right)\,ds.
\tag{1}
$$

六点正 Gauss 在 $[0,1]$ 上的准确节点/权重记为 $(u_a,w_a)$。各乘积最高次数如下：

| 项 | 单个多项式最高次数 | 乘积最高次数 |
| --- | ---: | ---: |
| $W_0^T W_0$ | 5 | 10 |
| $W_1^T W_1$ | 4 | 8 |
| $W_2^T W_2$ | 3 | 6 |

六点 Gauss 对次数不超过 11 的多项式准确，所以在准确算术下，源码采用的完整装配式正是

$$
G=\sum_{j,a,r}
h_j w_a\,\ell^{2r}
E_j^T W_r(h_j,u_a)^T W_r(h_j,u_a)E_j.
\tag{2}
$$

没有删去质量项、斜率项或曲率项。这里“准确”指这一多项式恒等式；实际 leggauss、Hermite 求值、乘加和分解使用普通浮点，并不因 (2) 自动成为 outward enclosure。

## 3. 严格正定与带宽的完整证明

每个 $h_j,w_a$ 都正。若 $y^TGy=0$，由 (1) 的非负项可知每胞的 $\int f_y^2=0$。连续多项式在某胞上平方积分为零，当且仅当它在该胞恒零。因此全域各胞多项式及其端三 jet 全零。Hermite 端 jet 与全自由向量的嵌入是一一对应的，故 y=0。

因此对每个非零完整自由向量都有

$$
y^T G y>0.
\tag{3}
$$

这对任意严格正的有限网格宽度成立，不要求相邻宽度之比受控。它不等于一个与网格无关的最小特征值下界。

也可直接从准确 Gauss 表达式看出满列秩：仅 $r=0$ 的六个不同节点就能确定一个五次多项式。若所有这些评价为零，每胞多项式就恒零，随后全部自由 jet 为零。

每胞只关联原槽 $3j,\ldots,3j+5$。radial_free 按原顺序保留；删除原固定槽只能缩小索引距离，不能扩大。因此任一非零装配项的自由索引满足

$$
|i-k|\leq5.
$$

G 的半带宽至多为 5。原循环按局部下三角装配到

~~~text
band[ii-jj, jj] += local[i,j]
~~~

其中 ii≥jj 且 ii−jj≤5，和 lower 带状格式一致。相关带状布局直接按 SciPy 官方的 [cholesky_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky_banded.html) 与 [solve_banded](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_banded.html) 文档逐项核对；本文没有运行文档中的数值示例。

## 4. 原积分分支的白化与转置

准确地令

$$
D=\operatorname{diag}(G_{ii}^{-1/2}),\qquad
DGD=LL^T,
$$

其中 L 是正对角的下三角带状 Cholesky 因子。G 严格正定，所以这些准确量存在。

每个角通道 m 的原权为

$$
\sigma_m=\sqrt{1+(\nu_m/\tau)^2}>0,
$$

其中 $\tau$ 为 angular_transition。x、y 的 odd 通道及 z 的原 even 通道都完整保留。设 $\Sigma=\operatorname{diag}(\sigma_m)$，把旋转向量按原 row-major 布局写为矩阵 $Z\in\mathbb R^{n_{\rm rad}\times n_{\rm mode}}$。原 lift 的旋转部分为

$$
T_{\rm rot}(Z)=D L^{-T}Z\Sigma^{-1}.
\tag{4}
$$

原积分范数的旋转部分为

$$
\|Y\|_{\rm int,rot}^2
=\operatorname{tr}(\Sigma^2Y^TGY).
$$

代入 (4)，因 $DGD=LL^T$，得到

$$
\|T_{\rm rot}(Z)\|_{\rm int,rot}^2
=\operatorname{tr}(Z^TZ)=\|Z\|_F^2.
\tag{5}
$$

对任意 V，以 Frobenius 内积逐步转置：

$$
\begin{aligned}
\langle DL^{-T}Z\Sigma^{-1},V\rangle_F
&=\langle Z,L^{-1}DV\Sigma^{-1}\rangle_F,
\end{aligned}
$$

故

$$
T_{\rm rot}^*(V)=L^{-1}DV\Sigma^{-1}.
\tag{6}
$$

D 与 L 不可任意交换。原源码正是先在 lift 中解 $L^T$ 再左乘 D；transpose 中先左乘 D，再解 L，最后按角通道除 $\sigma$。

实际带状转换也正确。若 lower[k,j]=$L_{j+k,j}$，源码赋值

~~~text
upper[5-k, k:] = lower[k, :nrad-k]
~~~

恰把 $L^T_{j,j+k}=L_{j+k,j}$ 放进 upper 格式。随后 solve_banded((0,5), upper, ...) 解 $L^T$，solve_banded((5,0), lower, ...) 解 L。

原 core 的完整尺度为

$$
T_c z_c=\operatorname{diag}\!\left(
\frac1{\max(1,|1-\nu_m^2|)}\right)z_c.
$$

这里实际 core 频率是正 even 频率，故 $|1-\nu_m^2|\geq3$，max 分支不会改掉所声明的 core 二次型。H 的尺度是 1。因而全空间的 core、rotation、H 三块合起来仍是原声明的正积分母范数的完整白化，转置也逐块准确。

这一范数是源码明示的径向 H² 积分及角频权。它没有被偷换成原 q 表示的母范数，也没有被声称为已经认证的任意曲面内禀 Sobolev 范数。

## 5. 准确正定不替普通浮点分解作保证

(3) 是任意正网格上的准确命题。它没有给当前 922 胞 graded 网格的实际最小特征值、条件数、浮点 Cholesky 误差或成功状态。

对角平衡使准确矩阵 DGD 的对角为 1，但对角为 1 的正定矩阵仍可任意接近奇异。例如

$$
\begin{pmatrix}1&1-\epsilon\\1-\epsilon&1\end{pmatrix}
$$

在 $0<\epsilon<1$ 时正定，而最小特征值就是 $\epsilon$。这只是解析说明，并非当前矩阵的数值试验或已观测失败。

当前 G 的窄胞导数项包含不同的 h 次幂；对角平衡能处理一部分单位和幅值差异，却不能自动排除跨节点的近线性依赖。普通精度若实际失败，应如实记录，不能由准确正定命题宣布实际分解已经成功；反过来，也不能由潜在条件数风险捏造一场尚未发生的失败。

网格还有一个独立责任。物理场的准确域和节点来自原 symbolic affine-in-S 定义，q.mesh 是工作载体。原数值范数使用该载体的正宽度来组装算法矩阵。本文的准确代数对所声明的任意正宽度成立；它不把工作载体对准确物理节点的误差证明掉。作为明确的有限维算法坐标范数，正载体宽度可以单独定义正矩阵，但不能把其浮点积分记录称为准确物理域上的区间证书。

更具体地，实际 hhat 是 np.diff(q.mesh) 返回的浮点字；它与把两个 mesh 字先当准确实数再相减，也可能存在一次减法舍入。原 Cholesky 与建议 QR 消费同一 hhat/Hermite 输入。把这些正 hhat 字本身声明为有限维坐标范数的 cell-length 参数时，(1)–(10) 的准确代数仍适用；这不把它们冒称为真实 symbolic 物理宽度。新记录应分别保 mesh 与实际 width 数组摘要，并明确 width、Gauss、Hermite、factor 和 solve 的舍入误差均未区间包围。固定物理 g 和完整场定义不随此算法坐标解释改变。

## 6. 保持同一积分定义的 square-root 行矩阵

定义矩形评价矩阵 A。对每胞 j、六个 Gauss 节点 a、三个导数阶 r，放入一行

$$
A_{j,a,r}
=\sqrt{h_jw_a}\,\ell^r\,W_r(h_j,u_a)E_j.
\tag{7}
$$

每胞恰有 18 行，所有列都是原完整自由槽。由 (2)，

$$
G=A^TA.
\tag{8}
$$

因此可以直接对 A 做正交三角分解，不必先形成 G。若先按列二范数平衡

$$
D_{ii}=1/\|A_{\cdot i}\|_2,
$$

则在准确算术下它和原 $G_{ii}^{-1/2}$ 完全相同。设

$$
AD=Q_R R,\qquad Q_R^TQ_R=I,
$$

R 为正对角上三角，便有

$$
DGD=R^TR.
\tag{9}
$$

这和原 Cholesky 的 $R=L^T$ 是同一个准确因子，不改变任何 norm 项或自由量。新的完整映射为

$$
T_{\rm rot}(Z)=D R^{-1}Z\Sigma^{-1},\qquad
T_{\rm rot}^*(V)=R^{-T}DV\Sigma^{-1}.
\tag{10}
$$

准确范数和转置的证明与 (5)–(6) 相同。

行矩阵实现的结构优势是：若 B=AD，则

$$
\kappa_2(B^TB)=\kappa_2(B)^2
$$

对满列秩 B 成立。直接形成平方矩阵再分解和直接在 B 上作正交消元是不同的数值途径。这个恒等式不是当前 B 的已测条件数，也不声称 QR 能克服任意精度下的病态性。

## 7. 带宽保持与全量流式算法

无需建立 $(18(J-1))\times n_{\rm rad}$ 的密集矩阵，也无需建立每个 mode 的巨大矩阵。所有角通道共用同一个径向因子。

按 cell 递增，再按 Gauss 节点和导数阶递增，产生 (7) 的每一完整行。它在按原槽压缩的 free 列中只占一个跨度不超过 5 的区间。局部固定槽原本就是零；不能按数值大小删除其他列。

### 7.1 第一次完整遍历：列缩放

逐行用缩放的平方和或 hypot 累积每一列的二范数，随后取 D。不要先把范数平方形成一个可能更易上溢的对角再开方。每个原自由列都有严格正的准确范数；若工作范数非有限或数值为零，明确返回本次数值构造不可用，不加 jitter、不丢列、不截秩、不换 norm。

### 7.2 第二次完整遍历：局部 Givens 插入

保存 upper R 的行带

~~~text
rowband[k,j] = R[j,j+k],   0 <= k <= 5.
~~~

将一行 AD 的工作值放到其完整 free 列区间 [first,last]。对 j 从 first 到 last，消去该行的第 j 分量。若当前两值是 a=$R_{jj}$ 与 b=v_j，使用一个实 Givens 旋转

$$
\begin{pmatrix}c&s\\-s&c\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}r\\0\end{pmatrix}.
$$

同时用同一份旧 tail 值更新

$$
(R_{\rm tail},v_{\rm tail})
\longmapsto
(cR_{\rm tail}+sv_{\rm tail},
 -sR_{\rm tail}+cv_{\rm tail}).
\tag{11}
$$

若符号规范化，则同时调整整个有关旋转或行，使 R 对角正；不能只改对角而不改同一行的其余项。消元后对角设置为 r，已消位置设置为零是该已执行正交消元的表示，不是丢掉原评价行。

LAPACK 的 [DLARTG](https://netlib.org/lapack/explore-html/da/dd3/group__lartg_ga86f8f877eaea0386cdc2c3c175d9ea88.html) 明确采用缩放来处理平方和的 over/underflow；SciPy [dlartg](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lapack.dlartg.html) 的接口返回 cs、sn、r。此处只核了官方接口/原算法说明，没有执行数值调用。普通浮点结果的全部误差仍需按实际实现声明，不因调用 LAPACK 就冒称区间正确性。

带宽为何不会扩大：处理当前胞时，所有已经插入的旧胞的最大列不超过当前胞的 last。当前行的 first 到 last 跨度至多为 5。消去第 j 列时，只涉及 j 到 last，且 j≥first，所以本次新 R 元素满足列减行≤5。处理下一胞时，它仍只重叠共享节点的原三 jet。这给出按胞顺序的完整归纳，不依赖忽略小数值。

实现不应默默裁掉区间外非零项；可把上述结构作为内部一致性检查。它是完整装配的索引责任，不是新的几何或求解准入条件。

该算法的存储为 $O(6n_{\rm rad})$。每个完整局部行至多执行六次旋转，每次至多更新六个元素，因此因子工作的算术操作量为 $O(18(J-1)\,6^2)$，所有 mode 共用。这里是结构复杂度，不是一次实际耗时或峰值内存返回。

### 7.3 原接口的直接输出

因 $R^T_{j+k,j}=R_{j,j+k}$，可设置

~~~text
lower[k,:nrad-k] = rowband[k,:nrad-k]
upper[5-k,k:] = rowband[k,:nrad-k].
~~~

于是完整 lift/transpose 仍使用原两种带状三角解，分别解 R 和 $R^T$，并严格保持 (10) 的 D/角尺度顺序。

新类应保 .size、.problem、.record、.lift、.transpose 的完整接口，保 core、rotation、H 的原布局。R696 的另一个径向 profile 自由块不能误当作这个旧布局；本组件不能用一个错误的 free_size 关系吞掉它。

## 8. 数值误差边界：能说什么，尚不能说什么

准确 QR 的证明不等于工作 QR 的误差证书。没有本地或实际当前网格的数值因子读取，就不能填写最小 pivot、条件数、实际白化误差、迭代改善或因子耗时。

对任意可逆工作因子 $\widehat R$，定义其真实 Gram 缺陷

$$
E_G=\widehat R^T\widehat R-DGD.
$$

若暂把三角解当作准确实数操作，以 $\widehat T=D\widehat R^{-1}$，则直接恒等计算得到

$$
\widehat T^TG\widehat T-I
=-\widehat R^{-T}E_G\widehat R^{-1}.
\tag{12}
$$

所以

$$
\|\widehat T^TG\widehat T-I\|_2
\leq \|\widehat R^{-1}\|_2^2\,\|E_G\|_2.
\tag{13}
$$

这说明因子残差小与完整白化误差小之间仍有逆因子的条件数责任。实际带状三角解、列缩放、角尺度和完整浮点运算的误差还在 (12) 之外，需要另付，不能把它们设为零。

若在某个后续严格分析中已经得到一个正交向后误差表示 $B+E=Q_R\widehat R$，则还可准确推出

$$
\|\widehat R^T\widehat R-B^TB\|_2
\leq(2\|B\|_2+\|E\|_2)\|E\|_2.
$$

本文没有为当前计算提供那个 E 的实际界，也没有提出一次额外 fixture 作为主求解的门。新 norm 记录应明确 ordinary factor/solve errors unenclosed，保真实因子、D、mesh、自由槽及角/core尺度的摘要；若失败就记录真实失败，不把失败解释为数学正定性或场可解性的否定。

## 9. 下一实际输入的使用规范

已有 integral 分支具备完整准确公式和正确 lift/transpose，当前没有已登记失败。因此可以直接在一个实际完整父场上执行完整的新范数方向；不必等待 QR 源，也不应先造一个只测 norm 的科学 fixture。该方向仍须做真实全目标、原所有行、永久位置、幅度及最终场读取。

从 jet-sum 改成 integral 时，需要诚实保留以下区别：

1. 数学目标 g、实际完整自由点和其 model 可以保持同一，但算法坐标度量改变，norm identity 必须重新实际生成。
2. $\mu$ 在新的坐标单位下是新的显式算法输入。相同十进制数不能自动称为相同物理阻尼。
3. 每一原物理约束的完整梯度须重新经过新的 $T^*$，整个 C 及其归一化都要重建。不能沿用旧 norm 下的 C、projection cache 或预条件因子。
4. 原完整父 checkpoint/report、固定 scalar、源码、所有历史位置的来源仍要严格核验。若旧 continuation 守卫要求同 norm，应另走明确的“同物理点、新范数”初始化入口，不能删守卫或把旧 norm 身份改标签。
5. 同一父的实际 Phi baseline 需要原样重读；后续接受依旧只用真实同目标改善与完整几何。新的母范数本身不是几何证书。
6. 零闭合的首次端点根失败发生在真实场读取，和本处 QP 坐标范数是不同环节。仅改坐标 norm 不会改变同一初始物理点的端点方程，不能将其宣传为已经解决了那些初根失败。

若后续选择 QR，它是同一准确 integral 定义的独立数值因子实现，实际 source 与 norm record 会不同。原所有变量、约束行、目标和验收均保留。是否改善当前完整方向，只能由该真实方向的返回来决定。

## 10. 验证与本条结论

本条已经独立核对：

- 234ac/7f 整个坐标类的同一 AST；
- 完整共享五次端 jet 与物理导数；
- 正权六点 Gauss 的完整积分矩阵、严格正定及带宽 5；
- 原对角平衡、上下带转换、全变量 lift 和真实转置；
- 流式局部 QR 的准确 Gram 恒等式、带宽归纳与同 norm 映射；
- 官方带状/LAPACK 接口；
- 相关已登记实际记录中没有发现该 integral 分支的实际失败，已可见相应运行使用 jet-sum。

没有实际当前网格数值分解、没有新的方向、没有测得范数或条件数、没有连续场证书。原 integral 首次完整方向和 QR 源准备可并行；二者都不能替代课题 README 的最终标准。
