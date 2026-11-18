# R47 固定控制槽：低层 basis/core 接口准备

维护：Astra-held10-7322d0de-20261118 / closed_geometry，2026-11-18（UTC）。

## 已完成的范围

依据 [R47](../results/R47-fixed-slot-nested-circle-homotopy.md) 和 [R48](../results/R48-exact-reference-compensation-for-mode-extension.md)，本批新增独立的固定槽 basis/core 源。当前 M8 同伦的旧源和正在运行的模型均未改动。本次仅执行文件哈希、限定 AST 字面值读取、可逆文字替换和语法解析；没有导入新增数学模块，没有实例化 basis/core，没有重新积分、构造新初猜、求 BVP 或调用尾端。

新入口为 `r47_fixed_slot_trace_core.make_core_factory(reference, original_cosine, settings, *, modes=M)`。高层调用者仍需提供真实的完整物理控制向量，并独立处理状态布局、参数尺度、lift、DN 维数和 mean-height。本批不安装一个高阶生产 BVP。

## 固定槽及 canonical 后端

对每个整数 $M\ge8$，lambda-one 的物理控制顺序固定为

$$
(B_2,B_3,B_4,B_5,B_6,T,U,B_7,\ldots,B_{M-2}).
$$

其中 $T=S_A-S_B$、$U=S_B$；$T,U$ 始终对应完整物理控制数组的零基索引 $5,6$。若参数数组第一个分量是轮廓的 $\delta$ 坐标，它们对应参数索引 $6,7$。新增模式只能在这些已固定槽之后追加，不能把 $T/U$ 移到每一层数组的末尾。

| 内容 | M8 | 一般 M |
| --- | --- | --- |
| 物理控制数 | 7 | $M-1$ |
| 最初五列 | $B_2,\ldots,B_6$ | $B_2,\ldots,B_6$ |
| 第六、七列 | $T,U$ | $T,U$ |
| 新增列 | 无 | $B_7,\ldots,B_{M-2}$ |
| lambda-zero 各槽 | $\cos(3j\phi),\ j=2,\ldots,8$ | $\cos(3j\phi),\ j=2,\ldots,M$ |

新增 `r47_fixed_slot_trace_basis.py` 复用已冻结的 `CircleTraceReplacementBasis(M)`。后者的 canonical 顺序是 $(B_2,\ldots,B_{M-2},T,U)$。定义置换

$$
p=(0,1,2,3,4,M-3,M-2,5,\ldots,M-4),
$$

则固定槽的函数列是 canonical 函数列按 $p$ 取出；物理系数反向放置为 `c_canonical[p] = c_fixed`。这只是索引赋值，不求解一个新矩阵，不缩放控制，也不丢弃低频自由度。

支撑零至四阶 jets、原函数零至五阶 jets、各列导数预算及系数求值误差预算都按相同置换处理。组合控制界先把完整物理 $c$ 放回 canonical 顺序，再调用原 `combined_control_rho_bounds`；因此原来先合并 $t+(u-t)\cos d$ 及两项低矩投影、随后才取绝对值的抵消保留。没有把 $t,u$ 错读为新增高模系数，也没有把两条迹列拆成一个更粗的新数值规则。

中间同伦仍逐槽定义

$$
C_j^\lambda=(1-\lambda)\cos(3j\phi)+\lambda E_j,
$$

其余弦频率按固定槽编号 $j$ 选取，不能改成 endpoint 中 $B$ 的编号。特别是 $j\ge9$ 对应 $E_j=B_{j-2}$，但余弦部分仍为 $\cos(3j\phi)$。

## 原始 M8 与完整积分接口保持

当 `modes=8` 时，新 core factory 直接返回旧 `circle_trace_homotopy_core.make_core_factory` 的结果；basis 的公开构造器也直接返回原 `CircleTraceHomotopyBasis` 实例。这里不通过新的排列和浮点求值去模拟旧实现。本次未执行实例化，因此没有把源定义上的直接委托写成已完成的数值逐位比较。

对于 $M>8$，lambda-zero 仍返回调用者提供的原余弦类。正 lambda 分支从已有 `raw_second_order_core.text` 派生，仅有四项替换：换入固定槽 basis 的 import，以及已登记 R44 使用的三项组合控制预算替换。原首控制释放、整体积分、材料角反函数、固定材料参数导数和数值正性门保持原定义；原 `rho>1e-5` floor、32768 网格上限以及原 triangle/一阶/C² 充分下界没有改变。

特别地，`normal_geometry`、`arc` 和 `parameter_derivatives` 通过同一 `_basis` 的完整列进行收缩，所以所有控制的参数 jets 按固定槽排序。`arc` 的原函数归一化、`f0/f20` 和 $u(0)=0$ 沿原实现保留。summary 中半径/圆心迹坐标明确改读 `c[5]` 和 `c[6]`，并注明只有 lambda-one 才是当前定义曲线的圆弧参数；继承的频率标签没有被冒充为 endpoint 的真实 Fourier 系数。

上述正性检查仍是既有数值 source guard，并不是新的连续曲面证书。支撑投影系数的既有有理包围也没有被扩大成跨模式浮点求值完全一致的结论。

## 为什么还需要高层 R48 转接

R47 的补零结论仅保持同一精确定义的 $h,\rho,\Gamma$ 及相应材料角对象。它不说明不同 $M$ 的有限入口投影相同，更不说明整条 physical quintic、mean-height 或完整尾响应相同。

高层需要逐块落实 $\mathcal B_N E=\mathcal B_M$，并按 R48 使用

$$
Z_N=EZ_M+\lambda a\chi(I_N-EI_M)
$$

及相应一、二阶径向补偿。数值 gauge、定义幅值、真实物理 $c$、材料图和完整背景必须保持；若参数尺度改变，应由高层重新编码参数，使物理 $c$ 不变。mean-height 的共同归一化和实际积分输入需要另外支付，不能由上式的平面抵消代替。只在节点上取值再生成新插值，也不能宣称连续表示恒等。

这些高层工作由后续真实候选的升模入口承担。本批没有产生高阶尾响应、BVP 接受、误差下降、闭族或 10% 证书。

## 可追溯执行

源为 `scripts/resume_closed/r47_fixed_slot_trace_basis.py`、`r47_fixed_slot_trace_core.py` 和 `prepare_r47_fixed_slot_sources.py`。紧凑记录是同目录 `r47_fixed_slot_source_preparation.json`；它绑定全部 11 个原始依赖源、R47/R48 正文和新增源。

实际只读准备执行 `73a2b1`，退出 0，耗时约 0.0063 秒。它重建并逐字反向还原原首控制释放、原二阶 guard 和新增四项派生替换；每个原锚点唯一，完整派生 core 通过 AST 解析。完整文字替换记录与派生源保存在 scratch 的 `closed_work/r47-fixed-slot-source-preparation-v1`，这里只登记其 SHA-256，不提交可再生副本。

完整准备记录的 SHA-256 为 `17b11cc74ee4589a1730e9982d059edc437dbccf6a46070dbba4b40889f289b6`，紧凑记录为 `58dfd2a74a4533862edbfe810417d5e90a3bf42a5cc7bad4ca99e2b706d484fb`。本次 `basis_instances/core_instances/new_integrals/BVP_calls/tail_calls` 均为 0，当前 M8 生产过程未修改。
