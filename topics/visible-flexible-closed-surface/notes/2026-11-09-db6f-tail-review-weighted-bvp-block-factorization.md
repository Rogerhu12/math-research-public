# 同一 W14 配点系统分块内存方案的完整独立审查

**审查结论：正文的配点块公式、结构条目与数组尺寸账本、条件性的直接 CSC 等价命题，以及平衡 QR 的精确线性代数命题成立。它们尚不是新实现、数值稳定性证明、实际资源峰值或 BVP 成功记录。**

审查人：tail-review-continued-2。日期：2026-11-09。  
本审查先完整阅读冻结正文，再核实际引用的相关源码和官方稀疏转换实现。此前对局部 QR 引理提供过审查意见，要求明确“当前缩减系统非奇异”和“共享端点不在其它行出现”；该交流是纸面审查，不是 QR 执行。本稿完整公开这一审查沿革。

## 1. 被审身份与记号澄清

主稿为 [2026-11-09-db6f-prefix-weighted-bvp-block-factorization.md](https://github.com/Rogerhu12/math-research/blob/5c9236652d92f80d7dc59462c0873bae51737b28/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-weighted-bvp-block-factorization.md)：

- commit：5c9236652d92f80d7dc59462c0873bae51737b28；
- Git blob：03184b7b5ffa48f41dce0898d45e69182b2bd03a；
- SHA256：525cfd19f06732148d221e8cd270abb900c6cf2007e5dde47ea32bc2ad8a7741；
- UTF-8 字节数：14,882。

本次正式审查对象为主稿加作者另存的 [Jacobian 评价点勘误](https://github.com/Rogerhu12/math-research/blob/c405667a744a19b47c59f8a0126c97710b2bb3c6/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-weighted-bvp-block-factorization-notation-erratum.md)。勘误 commit 为 c405667a744a19b47c59f8a0126c97710b2bb3c6，Git blob 为 414886a6f34f343b6be22f2f73a85025a1055aaf，1,684 字节，独立重算 SHA256 为 d613c45b187c9357da8c8c95e25a96050852e53401cbe69c352e4e8e96f97fbd。该小勘误已完整阅读；它只澄清以下记号，不改变块公式或算法。原稿保持原字节。

原稿 §2 有一处记号冲突：先将 x_i 定义为待求节点修正，随后又写 F_i=f_u(x_i)、G_i=f_p(x_i)。正确解释必须是：在当前网格 s_i、当前加权状态 U_i、当前参数 p 处评价导数

\[
F_i=\partial_U f_w(s_i,U_i,p),\qquad
G_i=\partial_p f_w(s_i,U_i,p),
\]

而 x_i 始终只表示线性未知修正。中点同样使用当前配点构造得到的状态。不能在未知修正 x_i 处重新评价 Jacobian。以下接受的命题均采用这一定义，与原实际源码一致。

## 2. 独立来源核验与实际检查边界

完整读取并在可用 JavaScript 隔离运行时重算了以下四份文本的 SHA256；实现先通过空串及 abc 两个标准 SHA256 值。

| 完整文本 | Git blob | 独立重算 SHA256 |
| --- | --- | --- |
| 被审主稿 | 03184b7b5ffa48f41dce0898d45e69182b2bd03a | 525cfd19f06732148d221e8cd270abb900c6cf2007e5dde47ea32bc2ad8a7741 |
| 官方 SciPy v1.17.0，scipy/integrate/_bvp.py | c82ebd0a9c582685cbd1b1b1c128391abd57ebef | 59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2 |
| 原 f6curve_domain_newton.py | 45c794fc230fe5f2d70b78667a34ac2b1d1115fa | 6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654 |
| db6f-root-spectral-collocation-v2.py | 87f4148fc246187ab9ccc8dfc099bba133c30c0e | 47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854 |

两个本题 Python 文件读取自与主稿相同的固定 commit。官方文件的全文 SHA 确实等于谱权模块要求的冻结 SciPy SHA；这只核该文件，不推断失联环境内其它包的版本或进程状态。

源码审读范围包括官方 compute_jac_indices、stacked_matmul、construct_global_jac、collocation_fun、prepare_sys，原 domain-aware Newton 的完整文件，以及谱权模块的完整文件。未执行这些 Python 源，未安装或选择任何新函数。

另从官方 v1.17.0 阅读：

- [scipy/sparse/_coo.py](https://github.com/scipy/scipy/blob/v1.17.0/scipy/sparse/_coo.py) 的 tocsc 和 _coo_to_compressed，blob 5b0d0a3fb1d7066a6faaa5869533bda3e3c347fa；
- [scipy/sparse/sparsetools/coo.h](https://github.com/scipy/scipy/blob/v1.17.0/scipy/sparse/sparsetools/coo.h) 的 coo_tocsr，blob 9b6be5dbdada8176405fbd68fd1da8bc65b99b68；
- [scipy/sparse/sparsetools/csr.h](https://github.com/scipy/scipy/blob/v1.17.0/scipy/sparse/sparsetools/csr.h) 的 csr_sum_duplicates，blob 997ffdde6b34c88ca3329adf7ee2d29757f94f8c。

后两段用于核实无重复项时转换只搬运相应标量，显式零保留，而非凭 canonical 一词假设没有额外算术。

### 实际工具返回

| 检查 | UTC | 结果与范围 |
| --- | --- | --- |
| 完整来源哈希 | 2026-11-09 22:39:17 UTC | 2 个 SHA 标准值及 4 个完整文本 SHA 全部匹配 |
| BigInt 尺寸账本 | 2026-11-09 22:40:28 UTC | PASS_INTEGER_STORAGE_DIMENSIONS_ONLY，25 项 |
| 矩阵组装 | — | 0 次 |
| QR、LU 或任意线性求解 | — | 0 次 |
| BVP、DN、tail、RK、几何后台 | — | 0 次 |

上述两次为 functions.exec 隔离运行时真实完成返回；不是失联终端执行，也没有读研究数据数组。尺寸检查只使用 n=43、k=14 和文中三个 m 的整数公式，不创建 Jacobian 或候选网格。

## 3. 原线性系统和 Jacobian 块

W14 的 n=43、k=14，节点数 m≥2，未知总维数 N=nm+k。按原 Fortran 顺序将加权状态修正逐节点排列，再接未缩放参数修正，配点行和边界行是

\[
A_ix_i+B_ix_{i+1}+C_i\xi=b_i,\qquad
Dx_0+Ex_{m-1}+F\xi=b_{\rm bc}.
\]

配点共 (m−1)n 行，边界 n+k 行，总行数 N。D、E 各为 (n+k)×n，F 为 (n+k)×k；实际所有端点和参数边界行都必须保留。这里没有将边界数误当成 n，也没有消去自由参数。

为独立核各块，可从原配点公式直接求导。当前中点状态为

\[
U_{i+1/2}
=\frac{U_i+U_{i+1}}2-\frac{h_i}{8}(f_{i+1}-f_i).
\]

配点残差为

\[
r_i=U_{i+1}-U_i-\frac{h_i}{6}(f_i+4f_{i+1/2}+f_{i+1}).
\]

对两端状态的中点导数分别为 I/2+h_iF_i/8 和 I/2−h_iF_{i+1}/8。因此

\[
A_i=-I-\frac{h_i}{6}(F_i+2F_{i+1/2})
-\frac{h_i^2}{12}F_{i+1/2}F_i,
\]

\[
B_i=I-\frac{h_i}{6}(F_{i+1}+2F_{i+1/2})
+\frac{h_i^2}{12}F_{i+1/2}F_{i+1}.
\]

对参数的中点状态导数为 h_i(G_i−G_{i+1})/8，故

\[
\widetilde G_{i+1/2}
=G_{i+1/2}+\frac{h_i}{8}F_{i+1/2}(G_i-G_{i+1}),
\]

\[
C_i=-\frac{h_i}{6}
(G_i+G_{i+1}+4\widetilde G_{i+1/2}).
\]

这与官方 construct_global_jac 的转置、stacked_matmul 顺序及两个 h² 项的相反符号一致。参数中点更新在原源中是原地加法；任何新实现必须确保它只应用一次，不能复用已更新数组后再次累加。

谱权模块的实际回调确认

\[
F=Wf_yW^{-1},\qquad G=Wf_p,
\]

边界状态列右乘 W^{-1}，参数列不缩放。W 在本次 factor 内固定，故没有遗漏其导数。本文讨论的 J 就是这个加权坐标系统，不是事后换回物理坐标的另一个矩阵。

## 4. Newton RHS、符号与 merit

原 domain-aware Newton 取完整 residual，调用 factor.solve(residual)，随后试 y−αd_y、p−αd_p。因此线性方程是 Jd=residual，不应再将 RHS 取负。

原 cost 为完整 step 的平方范数。在每次回溯，仍用同一 factor 求试探 residual 的 newstep，再用

\[
\operatorname{newcost}<(1-0.4\alpha)\operatorname{cost}
\]

及有限性条件接受。平方范数包括加权节点修正和未缩放参数修正。因此替代 factor 必须为每个试探 RHS 返回完整原序 J^{-1}b。

QR 投影后的 RHS 范数、压缩系统 residual、物理坐标 step 范数、线性后验残差都不能替代原 merit。主稿对此限制正确。

源码还确认 24 次 Newton 上限、最多 8 次刷新、21 档回溯，完整步复用原因子，域异常拒绝和严格接受不等式。上述候选方案不授权改变这些控制流、原容差、BC 门或后续真实 DN/seam/G5。

## 5. 条目计数和实际内存结论的边界

六类结构块分别贡献

\[
2(m-1)n^2,\quad 2(n+k)n,\quad
(m-1)nk,\quad(n+k)k.
\]

总数化简为

\[
L=(2n+k)(nm+k)=100N.
\]

第一次 values 拼接尚未加参数列，长度

\[
L_0=2nN=86N.
\]

官方 prepare_sys 在闭包外先创建 i_jac、j_jac，并被 sys_jac 引用。构造最终 values 的第二次拼接也要先保留输入的旧 values；所以只计算最终 values 的大小会漏掉这些明确存活对象。

独立 BigInt 账本核对：

| m | N | L | float64 values 字节 | 两个 int64 索引字节 |
| ---: | ---: | ---: | ---: | ---: |
| 5047 | 217035 | 21703500 | 173628000 | 347256000 |
| 6344 | 272806 | 27280600 | 218244800 | 436489600 |
| 6500 | 279514 | 27951400 | 223611200 | 447222400 |

m=6500 时的两批状态导数 192281208 字节、两批参数导数 62603184 字节、第一份 values 192305632 字节也正确。

这些是明确数组维数，不是完整运行峰值。导数临时量、COO→CSC 转换、LU fill、底层工作空间与其它缓存的生命期不同；不能简单相加称为实测，也不能因单个 values 小于某个 cap 就保证运行成功。

原两个失败长度与 L 在相应 m 的数值吻合，只支持结构对应。尤其 m=6344 仍只是反推值，不能据此制造已保存的 mesh 或 checkpoint，也不能推断旧 LU 是唯一内存失败原因。执行环境失联同样不提供 OOM 结论或工具退出码。

## 6. 直接 CSC 命题的严格含义

对每个节点列，B_{j−1} 的行号在前、A_j 的行号在后，再接全局端点对应的边界块；参数列依次为所有 C_i，再接 F。每列行号严格递增，同列块的行区间不交。m≥2 使左右端点列不同，边界 D/E 不产生同一坐标重复。

这一枚举恰覆盖全部 L 个结构条目，包括数值为零的条目。原 COO 构造的六类索引与此逐项对应。官方转换先搬运同一输入标量，随后对已排序同索引项求和；本结构无重复，所以不会发生重复项算术累加，显式零仍保留。

因此，若输入各块的标量字节、data dtype、index dtype 都相同，直接按该枚举构造的 data、indices、indptr 与原 canonical CSC 相同。原 SuperLU 和 Newton 控制流可保持。

这是一项条件性的表示等价证明。仅仅实现相同实数公式，还不足以声称输入块逐字节相同：原地操作次序、矩阵乘积次序、转置视图、dtype 和中点参数更新都必须实际核对。未来新实现仍须与原三个 CSC 数组直接比较，而不能把本次纸审说成比较已经做过。

采用 int32 时三数组账本为

\[
12L+4(N+1),
\]

三个 m 分别给 261310144、328458428、336534860 字节，已精确核对。是否和恢复环境原 CSC 的 dtype 一致仍须实际查明。

另一个实际必要条件是替换索引准备路径：如果仍调用旧 prepare_sys，两个全局 COO 索引仍被闭包保留，不能获得完整预期节省。主稿已指出这一入口依赖，不是只改最终拼接函数就结束。

## 7. 单向递推与平衡 QR

### 7.1 单向递推的适用范围

若额外假设每个 B_i 可逆，直接解出 x_{i+1} 的公式正确，最后可形成 (n+k) 维端点系统。但原 J 非奇异并不推出所有 B_i 可逆；长期传播矩阵也可能产生数值增长。因此这不是当前问题已验证的替代算法。

### 7.2 局部 QR 消元

两段关系堆叠后，内部共享端点 x_m 的系数为

\[
M=\begin{pmatrix}B_l\\A_r\end{pmatrix}\in\mathbb R^{2n\times n}.
\]

当前缩减系统的其它行不含 x_m。若 M 有非零核向量，就令仅 x_m 取该值，得到当前全系统核向量；这与当前缩减矩阵非奇异矛盾。因此 M 满列秩。

完整正交 QR 将 M 变为 [R;0]，R 可逆。将同一个 Q^T 应用于两段所有列和 RHS，前 n 行给 x_m 的唯一回代，后 n 行给左右端点和参数的关系。按内部端点列置前、上 n 行置前的顺序，全变换系统具有块三角结构

\[
\begin{pmatrix}R&K\\0&S\end{pmatrix}.
\]

原系统非奇异与 R 可逆立即推出 S 非奇异。对非齐次 RHS，每个缩减解由上方关系唯一提升；因此这是精确等价消元，不是删除一部分方程或最小二乘近似。

### 7.3 归纳与根系统

保留参数 ξ 作为所有段共同 border，边界只依赖两个全局端点和 ξ。每次只合并相邻段，上一层消去的端点有独立回代关系；尚存内部端点仍只出现在左右相邻关系中。上一节保持“当前缩减矩阵非奇异”，因此每层 M 都满列秩。

重要的是这一结论经当前缩减系统归纳获得，不是直接假设所有原始或后续局部 A/B 块可逆。

最终 n 行段关系加 n+k 行原边界，未知量为 x0、x_{m−1}、ξ，所以根矩阵为 (2n+k)×(2n+k)，本例 100×100，且非奇异。消去端点数为 m−2；相邻两两平衡合并，奇数末段原样传递，最大深度不超过 ceil(log2(m−1))。

根解后逆树回代，恢复所有完整节点修正。因子仅依赖 J；对每个新 RHS，重复保存的正交变换、根因子和回代，就得到同一精确 J^{-1}b。这足以在精确算术层面保留原 merit。

### 7.4 主系数存储模型

每个被消去的端点保存 packed Householder/R 的 2n² 个位置和 n 个 tau，再保存回代关系 U、V、W 共 2n²+nk 个系数，合为

\[
4n^2+nk+n=8041
\]

个浮点标量。根阵另占 (2n+k)² 个。因而主系数模型

\[
8(m-2)(4n^2+nk+n)+8(2n+k)^2
\]

在三个 m 处分别为 324614760、408048176、418083344 字节，已独立核对。每次 RHS 正向压缩保存上半部回代向量、反向恢复，所需量为 O(mn)。

模型正确，但没有计入层内关系块、原导数或块副本、工作空间、元数据、回调缓存及其它进程；不能升级为总峰值界。主稿没有作这种升级。

## 8. 数值实现仍未支付的事项

精确线性代数正确，不等于浮点执行轨迹相同。局部 R 与根阵的条件数、数值秩判定、QR 和 SuperLU 舍入差异，都会影响实际 Newton step 与回溯路径。正交消元避免显式长传播乘积，但不自动证明真实 Jacobian 良态、甚至非奇异。

未来实现至少还须：

- 绑定实际新的 prepare_sys、Jac builder、factor 创建及执行入口来源；
- 保留原物理回调、参数、网格、权重、边界和误差阈值；
- 对每个 RHS 返回完整原序 step，保留原严格 merit 与 refresh/reuse；
- 在数值秩或线性后验检查不满足时明确拒绝，不能正则化或放宽原门；
- 将原 J 上的线性残差、backward error 与非线性/BC/DN/连续几何最终证书分开。

这些不是已经完成的测试，也不是授权某个未写实现开始真实数学运行。磁盘源码哈希不能替代实际运行函数身份；旧入口与旧源码必须保持冻结。

## 9. 完整审查结论

在第 1 节明确的当前状态导数记号下，接受主稿两个精确命题及全部整数维数账本：

1. 同块、同 dtype、同结构零条件下，给定逐列枚举形成相同 canonical CSC；
2. 原 J 非奇异时，平衡两段 QR 和完整回代对任意 RHS 精确返回 J^{-1}b，不要求单个 A_i/B_i 可逆。

本次未实现新 builder 或 factor，未实际创建 CSC，未验证任何真实矩阵的 QR、秩、条件数、线性残差或求解速度，未测资源峰值，也未产生新的 BVP/曲面结果。存储 C 的环境恢复后独立重放仍另待完成。

本稿只保存小文本审查，不改 HANDOFF、LOG、results、活动求解器或旧文件。它没有改变 README 完成标准，不以源分析或整数账本替代最终数学完成。
