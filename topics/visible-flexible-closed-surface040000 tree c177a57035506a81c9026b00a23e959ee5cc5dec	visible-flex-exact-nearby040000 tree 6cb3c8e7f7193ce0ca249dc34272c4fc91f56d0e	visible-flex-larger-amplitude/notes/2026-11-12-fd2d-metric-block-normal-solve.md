# R159 同尺度、同阻尼 normal 的块 Cholesky 解与真实25消费

**状态：** 有限 SPD 块消元的等价性证明完整；独立新源已冻结，小合成检查和当前25完整 normal 的实际消费均真实 exit0。它是原方向问题的另一种线性求解实现，不改变物理场、有限目标、参数域或原线搜索；不构成强闭曲面完成证明。

## 1. 实际输入与冻结接口

25的48片已经合并保存成完整未缩放 normal，manifest SHA：

`e022f588dd0731aca74896ea8ef7fcbf649bd89c4a8d336e50b57a55c730a732`。

随后原通用稀疏方向进程 `41499 / 427b32 → be8cc0` 真实137/child−9，未产方向。终止原因仍未知。本组直接复用完整 normal，没有重算48片、F 或 J。

新源 `scripts/fd2d_gc_block_normal_solve.py`，10816字节，冻结 SHA：

`d992719316f0375ef3fe52b0feb75d970d3a560703edd9072ec1dacdd7457e26`。

```python
from fd2d_gc_block_normal_solve import solve_scaled_normal_field
out = solve_scaled_normal_field(normal, damping=1e-7, progress=None)
```

返回键：`solved, field_scale, parameter_scale, hfp, hpp, gf, gp, info`。其中 `solved[:,0]` 为原 $i_g$，其余54列为原 $i_c$。所有尺度和箭头块按原定义产生；`normal` 本身不修改。progress 仅接收字符串与 Python 整数，不传大数组。

helper 完全不调用 `normal.hff()`、`normal.scaled()` 或 sparse LU，不创建整张 field COO/CSC，也不做 $S@H@S$ 的整矩阵稀疏装配。

## 2. 必须保留的原缩放问题

输入已付 R159 精确消元：中央 raw 节点方向归入中央参数列，固定 cut 和完整 coast 无效帽列删除，terminal trace 方向为 $J_n-J_l$。本层只读取该完整 mapping 的节点宽度和 offsets，不重新猜测任何独立 tail 布局或 gauge。

令原未缩放 field normal 为 $H_{ff}$，全部自由场与参数列平方范数分别为 $\nu_f,\nu_p$。准确沿用

$$
S_f=\operatorname{diag}\!\left(\frac1{\max(\sqrt{\nu_f},10^{-12})}\right),\qquad
S_p=\operatorname{diag}\!\left(\frac1{\max(\sqrt{\nu_p},10^{-12})}\right).
$$

令

$$
A=S_fH_{ff}S_f+\lambda I,\quad
B=S_fH_{fp}S_p,\quad
g=S_fg_f.
$$

本轮 $\lambda=10^{-7}$，解的是同一55右端问题

$$
AX=R,\qquad R=[g\ \ B],\qquad X=[i_g\ \ i_c].
$$

小参数块同时保留原式

$$
H_{pp}^{\rm sc}=S_pH_{pp}S_p+\lambda I,\qquad
g_p^{\rm sc}=S_pg_p.
$$

**不是逐片或逐节点重算尺度。** 若一列原导数准确为0，原 $10^{-12}$ scale floor 仍给出既定尺度，其对应 field 块方向靠同一正阻尼处理，没有删除列、调节阻尼或新增“可逆性门”。

## 3. 块前后代完整证明

R159 已证明 $H_{ff}$ 块三对角。按保存节点分块，令 $A_j$ 为 $A$ 的对角块，$B_j$ 为相邻上块。实数算术下

$$
A=\begin{pmatrix}
A_0&B_0&0&\cdots\\
B_0^T&A_1&B_1&\cdots\\
0&B_1^T&A_2&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}.
$$

对任意非零 field 向量 $v$，因原 $H_{ff}=J_f^TJ_f$，

$$
v^TAv=\|J_fS_fv\|^2+\lambda\|v\|^2>0.
$$

所以 $A$ 正定，其每个非空前导主块及对应 Schur 块都正定。可用局部 Cholesky 解线性方程，不必显式求逆。

递推定义

$$
D_0=A_0,\qquad C_0=D_0^{-1}B_0,\qquad Z_0=D_0^{-1}R_0,
$$

以及 $j\ge1$ 时

$$
\begin{aligned}
D_j&=A_j-B_{j-1}^TC_{j-1},\\
C_j&=D_j^{-1}B_j,\\
Z_j&=D_j^{-1}(R_j-B_{j-1}^TZ_{j-1}).
\end{aligned}
$$

末块无需保留不存在的下一耦合。第一块方程等价于 $X_0=Z_0-C_0X_1$。若消去到 $j-1$ 后已有 $X_{j-1}=Z_{j-1}-C_{j-1}X_j$，代入第 $j$ 块方程便得到

$$
D_jX_j+B_jX_{j+1}=R_j-B_{j-1}^TZ_{j-1},
$$

即 $X_j=Z_j-C_jX_{j+1}$。因此从末端 $X_{N-1}=Z_{N-1}$ 逆向代入

$$
X_j=Z_j-C_jX_{j+1}
$$

恰得到原 $AX=R$ 的解。正定性给唯一性，故这与原缩放正常方程的线性解在实数算术下完全相同，证毕。

### 零宽节点

零宽块是零维向量空间，其相邻矩阵具有对应的0行或0列。相关乘积准确为零，空线性方程有唯一空解；无需对空块调用 Cholesky。若零宽节点位于内部，因原矩阵只有相邻块，它会把两侧 field 链分离，不产生跨节点新耦合。实现保留节点索引，显式创建正确尺寸的空 $C_j/Z_j$，也覆盖连续中央零宽与最后固定 cut 零宽。所有 field 节点都固定时，返回形状 $(0,P+1)$ 的空解，参数块仍按原式返回。

## 4. 内存与原 Schur 阶段

前代只保存各 $C_j$ 和55列的 $Z$；当前块 Cholesky 因子用完即释放。逆代原位把 $Z$ 改成 $X$。额外存储为

$$
O\!\left(\sum_j w_jw_{j+1}+d_f(P+1)+d_fP+P^2+\max_j w_j^2\right),
$$

而非一张整 field COO/CSC 的重复索引／数值临时数组。这里 $d_f=\sum w_j$。输入 normal 自身另计，既有 typed mapping 不复制成另一套结构。

返回后 numerical 的 StageSchur 使用原式

$$
\mathcal S=H_{pp}^{\rm sc}-B^Ti_c,\qquad
\eta=g_p^{\rm sc}-B^Ti_g,
$$

然后保留原 Schur 对称化、最小特征值 shift、SLSQP 参数／gap约束和真实 trial。此 helper 不求 QP，不改原参数盒；保存 Schur 包是后续进程可复用的实际实体，不需要重求 F/J。

## 5. 浮点对称化及原方程后验

实数推导中的所有块对称。但 binary64 中，左右尺度的不同乘法顺序及 $B^TC$ 减法会使对称对应元素相差末位。因此每个 Cholesky 工作块使用

$$
D_j^{\rm work}=\tfrac12D_j+\tfrac12D_j^T.
$$

这是浮点代表的明确变动，非原数学问题的新增项。程序记录 scaled diagonal 的反对称量、forward Schur 的反对称量、这次对称化的最大实际元素改变量，以及上块转置与原 lower 独立左右尺度运算的差。没有 eigenvalue clipping、pivot floor、jitter 或额外 damping。若真实浮点分解失败，应保留失败而不是悄悄换问题。

解得 $X$ 后，逐节点重新以 **未平均的原对角块及各自方向独立左右缩放的上下块**计算 $AX-R$。分别保存每个右端的绝对峰、$\ell^2$ 相对残差以及

$$
\max_i\frac{|(AX-R)_{i,k}|}{(|A||X|+|R|)_{i,k}}
$$

的有限浮点观察。分母和分子都为0时记0。这里报告的是实际计算残差，不是区间算术证书，也不把小 backward error 自动当成非线性残差或曲面误差。

## 6. 一次小合成检查

`scripts/fd2d-metric-block-normal-check.py` 构造三个小块 Gram 系统，参数维均为54，分别含：

1. `[0,0,5,3,4,0]`：连续中央零宽和末 cut 零宽；
2. `[0,2,0,0,3,0]`：内部零宽使两侧断开；
3. `[0,0,0]`：所有 field 固定。

每例都有55 RHS；前两例还故意留一条准确零 field 列和一条准确零参数 RHS。检查只为最多12维的合成 field 构造独立 dense **乘法残差**，不求参考逆，不用 dense／sparse LU，不构造当前实际 normal。调用前后的输入数组 hash保持；原 scale/hfp/hpp/gf/gp 全部逐项一致。

`70637 / d076fb → 44aa71` 真实 exit0。内部0.490870606 s，wrapper7.136458849 s，峰 RSS49348 KiB。三个独立乘法绝对残差峰分别为 $6.66134\times10^{-16}$、$2.22045\times10^{-16}$、0；componentwise backward 峰分别为 $3.95762\times10^{-16}$、$8.18661\times10^{-16}$、0。无失败轮，也没有追加大矩阵核验。

## 7. 当前完整25的实际消费

numerical 在源冻结后直接运行，不等待小 fixture。该真实 StageSchur：

- 执行 `62475 / 3ea4a1`，child与wrapper均自然0；
- 129节点，10953个 field 未知量，54参数，55 RHS；
- 119个非空块，零宽节点为0至8及128；
- 完整 normal 原行数50355，原 damping $10^{-7}$；
- helper 内部1.610877901 s，其中分解和前后代1.225992401 s；
- 整个被监控 child 19.148610128 s，kernel峰 RSS137308 KiB。

这些时间是不同作用域，不混为一项。真实数值为：

| 项目 | 实际值 |
|---|---:|
| 原未平均缩放块方程绝对残差峰 | $4.255946723513704\times10^{-13}$ |
| 各 RHS 最大相对 $\ell^2$ 残差 | $5.153930306637943\times10^{-12}$ |
| componentwise backward 峰 | $4.130340689588938\times10^{-14}$ |
| 局部工作块对称化最大改变量 | $1.3665284182007298\times10^{-15}$ |
| forward Schur 反对称峰 | $2.7330568364014596\times10^{-15}$ |
| 相反方向尺度乘法差峰 | $2.220446049250313\times10^{-16}$ |
| 最小实际 Cholesky 对角 | 0.0029634345968963466 |
| 保留的耦合 workspace | 8082608字节 |
| 返回的55 RHS解数组 | 4819320字节 |
| 原参数 Schur 最小特征值 | $1.0000849472642645\times10^{-7}$ |
| 原算法所需 Schur shift | 0 |

完整解及 Schur packet 已实际保存，manifest SHA：

`03412f96a6803bd1cde7c5e09b1b8ea749c215ff5418a3a47a5415182149fc28`。

准确位置为 `notes/2026-11-12-fd2d-raw-bump-staged25-work/reduced-factors/lambda1e7-block-a01/packet/manifest.json`。原 report 为 `notes/2026-11-12-fd2d-raw-bump-staged25-block-schur-a01-report.json`，资源由同stem的 `process-receipt.json` 记录。本文的小摘要绑定这些实际文件SHA，不重复复制其大数组。

这是完整 **线性求解阶段已成功并保存** 的证据。它不反推原−9的原因，不预报原 QP／Armijo 接受，不宣称非线性核或强目标完成。后续 numerical 用这个同源 packet 实跑原 QP 与 trial；数学主线继续。
