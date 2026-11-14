# 2026-11-14：保持完整原方程的带状 LU 接续

## 实际触发原因

公开 Actions run 43590496434 在 M112/T112/N2048 的同一 699 节点初场上完成
第一份完整 Jacobian，但原单向正交消元求得的线性方向满足

$$
\|A\Delta-b\|_\infty=0.006494337572127054,\qquad
\|b\|_\infty=0.0071105950777444905,
$$

比例约为 $0.9133324991$。最大误差位于最后一个区间 697 的物理行 335，即
$z_{110}$。常值核心、常值 scalar 和左边界线性残差分别约为
$9.02\times10^{-17}$、$3.33\times10^{-16}$ 和 $2.91\times10^{-15}$。
右边界线性残差约为 $2.00\times10^{-7}$。

原日志只有一次 linear solve。原 17 次回溯只有在试验残差全部有限时才会再次
调用 linear solve，因此这 17 次全部在非有限值检查处失败，没有接受任何更新。
保存的 prepared 与首 Newton checkpoint 的 mesh、states、rhs 逐项相同。
随后的 966 节点 pending 是未接受的自适应插值状态，不作为新的初场。
本次也没有请求一个新的非零 H 尾；原 T112 零锚真实缓存保持不变。

以上证据要求先解决实际原线性系统的求解精度，不能将这一步失败解释为非线性
大幅解不存在。新入口不再移动控制支撑、修改 BC、减少模数或增大接受容差。

## 1. 原系统与精确行置换

每个节点有 $n$ 个完整增广未知数 $y_j$，$j=0,\ldots,m-1$。记左、右边界行数为
$\ell$ 和 $k=n-\ell$。线性化的原方程为

$$
L_j\Delta y_j+R_j\Delta y_{j+1}=b_j,\quad
j=0,\ldots,m-2,\qquad
B_a\Delta y_0=b_a,\quad B_b\Delta y_{m-1}=b_b.
$$

原求解器把右端排列为“全部区间、左边界、右边界”。新后端只将方程行排列为
“左边界、全部区间、右边界”，未知数仍保持逐节点的全部 $n$ 个分量。若 $P$ 是
这个行置换，则

$$
A_{\rm band}=P A_{\rm original},\qquad
b_{\rm band}=P b_{\rm original}.
$$

$P$ 是正交置换矩阵，所以精确解不变，Newton 方向本身及其欧氏范数不变。
原 residual 的 $\ell^2$ 与 $\ell^\infty$ 范数也不变；返回解不需要逆置换。
每个完整物理、核心、scalar 行和所有边界列都保留。

## 2. 带宽与存储

在新行序中，第 $j$ 个区间的行范围为 $\ell+jn$ 到 $\ell+(j+1)n-1$，
列落在第 $j$ 和 $j+1$ 节点。于是所需的完整下、上带宽分别为

$$
k_l=n+\ell-1,\qquad k_u=2n-\ell-1.
$$

左、右边界块也在这个带内。LAPACK 的主元填充额外需要顶部 $k_l$ 行；故
AB 的形状为

$$
(2k_l+k_u+1,\;mn),\qquad
AB[k_l+k_u+i-j,j]=A_{\rm band}[i,j].
$$

本次 $n=453,\ell=341,k=112,m=699$，得到
$k_l=793,k_u=564$，AB 形状为 $(2151,316647)$，float64 字节数为
$5\,448\,861\,576$。原 max_nodes=1200 不变；达到该节点数时，相同带存储为
$9\,354\,268\,800$ 字节。这里是存储计数，并非已完成这次因子的实际内存读数。

AB 直接分配为 float64 Fortran-contiguous 数组，不先构造另一个完整稀疏或
稠密矩阵。逐 chunk 产生的原 $L_j,R_j$ 写入 AB；未经因子化的两块另存于临时
磁盘供残差核验。dgbtrf 使用 overwrite_ab=1，并记录、核对返回 LU 与输入共享
存储且指针相同。dgbtrs 接受 Fortran-order 的 $(mn,1)$ 单右端，不手动修改
LAPACK 返回的 ipiv。

原 released_newton 在每次重建前已有 lu=None、J=None 和 gc.collect()；
新后端不保留历次 factor 的强引用，因子释放时清理其 AB 和临时块目录。
不需要为此修改原 Newton 的生命周期。

## 3. 直接对原矩阵读残差

求解后从磁盘重新读取原 $L_j,R_j$，在原行序计算

$$
r_j=L_j\Delta y_j+R_j\Delta y_{j+1}-b_j,\quad
r_a=B_a\Delta y_0-b_a,\quad r_b=B_b\Delta y_{m-1}-b_b.
$$

累加使用平台 long double，并在报告中记下实际尾数位数。报告保留每个区间
的最大误差、具体状态行、物理/常值核心/常值 scalar 分块，以及左右边界误差；
第一方向与完整原右端也分别压缩保存。全矩阵的 normwise backward error 与
直接 residual/RHS 比值分别报告，不能用前者的小值掩盖后者。

如果需要改进，用同一个带 LU 求解 $A\delta=-r$ 并更新
$\Delta y\leftarrow\Delta y+\delta$，最多四次，只保留实际原残差变小的更新。
这是同一个原有限线性系统的迭代改进，没有 SVD 截断、正则化项、丢行或新的
边界方程。$10^{-10}$ 的相对线性准确度只是改进循环的目标及报告字段，不是新
的非线性接受门；原 Newton 的所有判断继续决定接受与否。

大于仓库单文件限额的完整 RUNNER_TEMP checkpoint/诊断不会使数学计算失败。
它们保持在 Actions artifact 中，注明单 Git 文件资格，交原 publisher 过滤；
仓库文件大小规则不被用作求解器的数学门限。

## 4. 原 Newton、真实尾及接续命令

新增入口为
geometry_20261114_lifted_modes_banded_full_dn.py，
后端为 geometry_20261114_banded_collocation.py。CLI 与已冻结的
geometry_20261114_lifted_modes_full_dn.py 完全相同，只替换入口文件名。
继续使用实际 699 节点 prepared、原 response-check 和已经完成的真实 T112
零 H/J 缓存；不重建已经成功的准备场，也不使用失败的 966 节点插值。

入口直接调用原 released_newton 函数；它的 20 次迭代预算、每次 17 个试验、
原方向范数与 Armijo 表达式、RMS=$10^{-6}$、BC=$10^{-11}$ 及其它原判断均不改。
只对传入的 col_fun 与 bc 加只读包装，逐次记录哪些节点、中点或边界行实际
返回非有限值。这些日志是原 trial 调用的结果，没有替代原域判断。

原真实尾外循环、完整 T112 Jacobian、最后的真实 native audit、冻结物理场
RMS 和后续真实闭包也全部保留。第一份因子完成后在同一 run 继续原求解流程，
不为读一个阶段报告而重建相同 Jacobian。即使带 LU 取得准确线性残差，后续
仍可能因真实域、全 DN 或其它非线性因素失败；本文不预先宣称改法会收敛。

## 5. 本轮实现身份

| 文件 | SHA256 |
| --- | --- |
| geometry_20261114_banded_collocation.py | 0780dcc4e331f6cde64141b0fa9ebdd1325eec2af87d94fc455e72405a0524f1 |
| geometry_20261114_lifted_modes_banded_full_dn.py | 390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4 |
| 被复用的原 M112 full-DN 入口 | d885ebc8de5ebd02f006c4104d8b67e856047b4e58f0e125651b38187fb251a5 |

已经完成 Python AST 与源接口检查；本轮没有在本地运行矩阵因子化、SVD、PDE 或
新的尾计算。实际准确度、耗时和内存由下一次公开 Actions 的原件给出。
