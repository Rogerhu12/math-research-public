# R681 当前 normalized-Phi coarse Gram 的角矩组装接口

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

## 产物与实际状态

源码 [full_phi_coarse_moments.py](../scripts/resume_20261120/full_phi_coarse_moments.py) 为 22234 bytes，SHA256：

`da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719`。

它实现 [R681 第 5–6 节](../results/R681-current-J-coarse-frame-preconditioning.md)，供 [隐式 CoarseFrame](2026-11-20-R681-implicit-coarse-frame-source-interface.md) 消费。此次只写源码、静态逐项核对并用标准库 AST 解析，未 import 或执行科学代码，没有新 fixture、数值核验、场扫描、J/JT 调用、求解或预排。这个准备结果没有宣称已改善任何实际方向。

当前较大试步的真实 Phi 已降而几何筛选拒绝，与内层未收敛是两项不同事实。此模块准备数据预条件所需的小矩阵；它不修改非线性几何、活动面、永久点记忆或真回溯，也没有把预条件当成几何拒步的解决办法。

## 唯一入口与当前数据绑定

```python
Gc, metadata = module.assemble_current_coarse_gram(
    actual_R664_bridge,
    current_coarse_frame,
    stage_block=8,
    provenance=actual_parent_and_source_records,
)
```

`bridge` 必须是本轮实际 R664 `NativeLinearization`；`frame` 是当前同一 complete operator、DI、physical-height、literal B 和原 R 构成的 `CoarseFrame`。入口检查现有 `problem._base_x` 与 `bridge.x` 逐值相同，消费已经建立的 `_base_first` 和 `_base_p.rho`。本模块不调用 `set_base/prepare/residual/jvp/vjp`，也不另造场缓存。

返回 `Gc` 是当前 $U=BR$ 系数中的 **完整 normalized-Phi 数据 Gram**，不含 damping；可直接作为 `frame.small_hessian(Gc, actual_mu)` 或 `FixedSPDPreconditioner` 的输入。实际 mu、原母范数与全部原变量均不在这里改动。

入口检查 `GITHUB_ACTIONS=true` 和准确公开仓库名。导入仅加载依赖、定义函数/类与字符串常量，不执行科学组装。报告绑定本源码、实际被调函数的源路径/字节 SHA、实际 x/scale/R 因子/nodal B/mesh/角点/a/rho/权的数组身份；R671 同时保留当前 canonical model definition 与 model identity。大矩阵仅作为返回数组，未写入 Git。

## 从当前 R664 正块到移动六张量

现有 batch 与 R671 operator 的第一 jet 缓存已经是随 $\phi$ 旋转的 R/T/Z 正交分量。因此源码直接使用 $V=F_s$、$d=F_\phi$ 的这些分量。它不把缓存误当 Cartesian，也不重复应用旋转。

记 $r=a\rho$，构造

$$D_{\mathrm{loc}}=
\begin{bmatrix}
2V^T&0\\
d^T/r&V^T/r\\
0&2d^T/r^2
\end{bmatrix}.$$

将 `bridge.blocks` 的 axis/offaxis/root_plus/root_off/root_minus 五个实际冻结数组按 stage 取视图，仍调用同一已刊 `HessianBlocks.whiten_columns`。因此

$$S_{\mathrm{loc}}=(B_{\mathrm{R664}}D_{\mathrm{loc}})^T
(B_{\mathrm{R664}}D_{\mathrm{loc}})
=D_{\mathrm{loc}}^TL_{\mathrm{R664}}D_{\mathrm{loc}}.$$

它准确对应 R681 的 $O(\phi)^TS_{\mathrm{cart}}O(\phi)$。原场全部 M 模、解析转角与 lift 都保留在当前 V/d/rho 和正谱块中。R671 的固定 $k'$ 已在 V 缓存内；本模块没有从旧 lift 重新构造 V。R664 的 Frobenius cross 因子已在其正块中，不再额外乘 $\sqrt2$，也不以梯度用正块替代 Hessian 正块。

## 有限角矩与 v7 正规矩阵的逐项等价

对每个 stage 的 21 个对称六张量分量，直接用全部原角点和其正轨道权形成

$$\sum_\phi m_\phi(S_{\mathrm{loc}})_{ij}\cos(2k\phi),\qquad
\sum_\phi m_\phi(S_{\mathrm{loc}})_{ij}\sin(2k\phi),
\quad0\le k\le2m_c.$$

源码保留恒为零的 sin0 列以简化准确索引；当前 $m_c=12$ 共 50 列。这里没有假设 $S_{\mathrm{loc}}$ 带限。只对有限 coarse 测试列使用逐点乘积化和差，所以当前完整高模场没有被截断。

移动分量中的速度 channel 为 R: $(\cos,0,0)$、T: $(0,\sin,0)$、Z: $(0,0,\cos)$。位置 channel 取其实际 Cartesian 角导数的移动分量：

$$R:(-\nu\sin,\cos,0),\quad
T:(-\sin,\nu\cos,0),\quad Z:(0,0,-\nu\sin).$$

这些单位旋转项保留了 R681 中的 $\Omega h$，所以没有漏掉基底自身的角依赖。21 组矩通过同一 cos/cos、sin/sin、cos/sin 恒等式恢复完整 $2n_c\times2n_c$ velocity/position channel 核；每个原角权只乘一次。

冻结 v7 源 `702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8` 的 `spectral_evaluate` 逐点先形成

$$J_{\mathrm{channel}}=D_{\mathrm{loc}}
\operatorname{diag}(h_j,h_{j,\phi}),$$

再求 $J_{\mathrm{channel}}^T L J_{\mathrm{channel}}$。本模块按乘积恒等式对同一双线性型先取六张量角矩。两种次序逐点代数相同；不需要对 2534 个 coarse 列或约 133 万个原自由变量作单位 J 扫描。这里是源码/数学等价，未声称两种浮点加法顺序逐字相同，也未重复其既有 probe。

## 全观察行与真实 H 列

当前完整 solver 的 B 构造于 native structural template；其旧 `stage_y/stage_u` 仅有 legacy 行。新接口 **不使用这两个旧缓存**，而是从同一 `node_jets`、原 `observation_cells` 与 `(P,3,6)` Hermite observation weights 重建每个实际行的径向 y/u。

原自由布局固定的初始 Y/U、末端三 jet 按原 `free_direction/unpack` 处理，A0_xy 粗列仍保留；当前 Z 粗列的固定 A0_Z 为零。最后 H 列在其 nodal $b-h$ 重建值上再加本轮 `lift_scalar` 中准确的 $h,h'$：

$$Y_H=\operatorname{Hermite}_{\mathrm{mesh}}(b-h)+h.$$

过渡区没有换成理想 b。R671 native/observed 必须引用同一个实际 tail context。粗列不改自由 core-c，这由冻结 B 源绑定；全部原 core-c 仍在完整 DI 方向中，没有从原求解问题删除。

对 coarse 列 $\ell,j$，按实际 $u,y$ 累加

$$N_{\ell j}=\gamma\sum_s w_s
\left(u_\ell u_jK^{uu}+u_\ell y_jK^{uy}
+y_\ell u_jK^{yu}+y_\ell y_jK^{yy}\right)_{\ell j},$$

$$\gamma=\frac{k}{\mathrm{scale}^2C_0},\qquad
C_0=N_{\mathrm{full}}\sum_s w_s.$$

其中权全部直接来自当前 bridge 与 operator；零列 stage 的贡献确为零，不删任何观察行。对于匹配全行/当前场的 v7 正规矩阵，这里 N 就是其已乘 $k/\mathrm{scale}^2$ 的返回矩阵再除 $C_0$。没有取其旧 `norm_right`，也不使用虚拟 RHS 范数冒充 Phi。

## 保原 R 的白化与代价

最后准确声明

$$G_c=R^TNR=L_N^{-1}D^{-1}ND^{-1}L_N^{-T}.$$

当前原母范数的 Cholesky 按 channel 与独立 H 块分离。源码只在实际交叉块**逐项等于零**时按这些原块作两侧三角解，没有阈值截断或重新白化；若实际因子出现非零交叉块，则使用同一原完整三角解。输出只作对称化并报告反对称浮点差，不加 ridge、jitter 或特征值修正。

内存与复杂度是以下实现结构的静态估计，尚非测得耗时/峰值：

- 角累加为 $O(PN\cdot21(4m_c+2))$，加有限 channel 代数；$m_c=12$ 时是 21×50 组测试，全部 N 点保留。
- 径向累加为 $O(\sum_s p_s^2)$，$p_s$ 是该 stage 的实际非零 coarse 列数，未以数值阈值裁剪。
- 默认 stage block=8，仅留块内六张量、导数与 channel 矩，当前 N=513 时为数 MB 级暂存；共享既有完整场缓存和五数组正块，不再复制其全域数据。
- p=2534 的单个 dense 矩阵约 51 MB，白化使用数份同阶暂存。精确分块时两侧白化成本约 $O(p^2\max p_{\mathrm{channel}})$；一般非分块输入仍有完整三角解成本。没有巨大的 Q 或 J 列矩阵。

本模块的输入契约和有限算术失败会明确报错；可选预条件的调用者应如实处理，并保留原 solver 路径。这里没有增加任何科学入口检查门，也没有启动新的 PCG、SOC 或完整方向。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
