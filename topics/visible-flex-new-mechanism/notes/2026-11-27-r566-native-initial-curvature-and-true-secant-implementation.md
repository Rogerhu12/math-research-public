# B030 原 native 初始曲率接口与真 secant 最小消费实现

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
状态：纯源码 / 纸面算法实现，尚未编译或执行新科学范围。
依据[原终态与控制流收据](2026-11-27-r566-true-secant-restart-source-receipt.md)：
原33次调用都在首个可形成新 BFGS secant 的新 J 前结束；原未输出的 H / λ 不可恢复。

## 1. 冻结文件与准确原源补丁

| 文件，均位于 scripts/ | 字节 | SHA-256 |
|---|---:|---|
| `r566_seeded_slsqp_native_20261127.patch` | 5796 | `53926005cd188c164ed3cf243e91929f20060e6462edb03930a0d0c8c9c17d1c` |
| `r566_build_seeded_slsqp_20261127.py` | 9921 | `e23cc8d65c092a5bfff350ac9416de1be8711e5f99fdefb9d43d5181cd22774e` |
| `r566_true_secant_curvature_20261127.py` | 21857 | `76c38d9ebdb51698d115d667adb7ab33cc2d1b18af99697f1a0e1058e6b27a0f` |
| `r566_seeded_slsqp_SCIPY_LICENSE.txt` | 1531 | `221e59f5e910fd7f94e44f0dac77436a11338c285c6346232e4a850a50da0e94` |

补丁基于 SciPy Developers，*SciPy 1.17.0*，tag `v1.17.0` 的原
`__slsqp.c/__slsqp.h/__nnls.c/__nnls.h`；各准确源大小、SHA 和官方链接在上述收据。
应用后 C 主源为33889 B，SHA
`6c51bc16553050db0c392ed3cd07e1dbf647d0da3252aac20327507e00aad1cf`；
header 为18918 B，SHA
`cbbcbea90fe3aed039c3bd68fee68e7d39b08d0c0164ab2462b3be121751d1f5`。
NNLS 两源不改。只发布完整补丁 / 来源清单 / builder，不保存每次可重建的第三方源树或二进制。

新增 C 参数 `initial_ldl` 只在第一次 `MODE0` 有效。原初始化仍先清 step / penalty 状态；
有 seed 时复制其 n(n+1)/2 项，设置与原第一次初始化一致的 `reset=1`，再进入原 `ITER_START`。
没有 seed 时逐字执行原 identity reset。**后续全部 `RESET_BFGS` 分支仍置 I**，
没有把失效矩阵强行续用，也没有继承旧线搜索 / reverse-communication 状态。

原 wrapper 的参数序列、QPs、增广不可行问题、线搜索、迭代终止、浮点 ULP box clamp
及 Python `_minimize_slsqp` 原控制流保留。只新增 dict 的可选 `_r566_initial_ldl` 项，
并将扩展模块名改为 `_r566_slsqp_seeded_20261127` 以免覆盖原 wheel。
wrapper 要求 seed 是相应长度的连续 float64 数组，全部有限，packed 对角 D 严格正；
这不是给物理场添加新门，而是这个新增 native 指针接口的实际类型 / 正定定义。

## 2. packed LDL 的单位与正定性

native 工作区最前部按**下三角列主序**存单位下三角 L 的非对角元及 D 的对角元。
原主源的两个 `dtpmv` 与中间 D 乘法实际构成 $H=LDL^T$。
坐标仍是原81q加 e，没有缩放参数、旋转 J 或把 box 变成另一类约束。
这里 n=82，packed 长度3403。

解包按原顺序读取每列，重建 H；准备 seed 时用实际 Cholesky $H=CC^T$，
以 $D_j=C_{jj}^2$、$L_{ij}=C_{ij}/C_{jj}$ 回到同一 packed 定义。
原输入没有 H 时首次走原 I 初始化，没有从旧接受步长或 q 猜一个矩阵。

每个外部新 secant 采用上述收据的 Powell 阻尼。
随后对**近似 QP 矩阵**作声明的特征值截断 `[1e-6,1e6]`，再 Cholesky 打包。
这不是物理 Hessian 的上下界，更不是问题凸性或 Newton 收敛证明。
所有 eig / Cholesky 费用计入新科学；失败明确回 I 并登记，不隐藏失败成本。
非有限或非正 D 的实际 native 因子不会进入 FINAL 的 JSON；只记录其原字节哈希与显式重置。

## 3. 真 J、真乘子与两条不同轨道

`TrueSecantSLSQP.minimize` 接收原 `minimize` 的全部参数，不替换 original callback，
不改 working fun/Jac、物理 box、ftol、maxiter 或 backend 的 raw 数组。
它只在本次同步调用内临时接管 `_slsqp_py.slsqp` 的 native 入口，`finally` 原样恢复。
原 wrapper 首次实际请求的 C/g 已完整付费，再由 `_prepare` 消费；helper 不调用一次额外
model value、Jacobian、full fine 或旧诊断。
算法改变后正常 backend 请求的新点 / J 仍由原成本账本完整支付，不能据“helper直接额外调用为0”
把自然增加的求解工作算成免费。

原一次 QP 返回、major iteration 增加且 mode 为0或1时，从实际 native 工作区记录：

- `x0`，是该 QP 真 J 的原点；不把 callback 的 raw 试探点当成它。
- `v=gradient-C.T@lambda`，是同一次 QP / 同一 C 的真实加权梯度。
- `mult[:m]` 的所有准确非零乘子与其真实行 key，不设小数阈值；零乘子准确省略。
- 当前 packed H、backend / major / reset 身份和有序行库哈希。

这里 `x0` 偏移为 n(n+1)/2，`v` 偏移为
`n(n+1)/2+n+m+2*(n+1)`，直接对应原 C 的分段指针。
bound 行是线性的；原 native 同样不把其乘子放进这条加权梯度，它们的冻结乘子梯度差为零。

下次交换后的原新 J 真正完成时，使用同一个旧 λ 的非零行，得到相同冻结
$L=f-\lambda^Tc$ 的两个梯度之差。新附加工作行在这个更新里 λ=0，随后原新 QP
仍使用全部新行并重新求全乘子。若完整旧非零乘子行不在新库，明确跳过这个 secant。
行 key 按原 field / s 的 binary64 hex / uniform angular index 或实际 theta hex 组成。

phase、完整冻结模型身份、参数顺序、实际 dataclass 参数、物理阈值、FFT节点数和 NumPy版本
进入行函数语义指纹；指纹改变时清 H / pending 并从 I 开始。仅 trust box 的线性右端变动
不会把同一非线性约束换成新函数。四点 orbit-min 切换分支时仍只称分段光滑数值近似，
没有假定它处处为光滑 Hessian。

若原 backend 未被交换中断而真正进入 `MODEM1`，它已经用自己的新 J 消费了上一条 secant，
外部 pending 立即清除；新的真实 QP 才能建立下一条 pending。
因此不会在下一次外部交换时重复应用 native 已用过的同一对数据。
每次外部 pending 一经消费也立即移除，即使随后 clock 停止也不重用。
raw optimizer 与单独通过全部门的物理 best 始终维持原分轨。

## 4. Actions 构建、runtime 与新费用

builder 在调用者同一个原 monotonic deadline 下执行，不能创建新的科学时钟。
它只允许本公开仓的 Actions，核实际 SciPy 为1.17.0、实际原 `_slsqp_py.py` SHA，
一次获取每个公开官方原源并核完整字节，以 `patch --fuzz=0` 应用本补丁，核应用后 C/header SHA。
所有 fetch 尝试 / 完成 / 时间，patch失败，compiler尝试 / 完成 / 输出哈希和失败文本均保留。

调用该 pinned SciPy wheel 自己 `scipy.libs/libscipy_openblas*.so` 的 LP64库，
核17个所需 `scipy_*_` 符号存在，并输出其原文件大小和 SHA。
没有静默选系统 BLAS，没有额外数值探针。
编译保留同一已安装 NumPy 的 C header 和 Python header；实际完整 argv / compiler版本在原stdout：
`-O2 -std=c11 -shared -fPIC -fvisibility=hidden -fno-fast-math -ffp-contract=off`，
原 BLAS 函数名映射到该 wheel 的符号前缀，rpath指定同一库位置。
新二进制的 SHA、导入和 build总秒在同一收据。

这明确改变了 native 模块的构建 / 二进制来源，不能声称与原预编译 wheel 逐位相同。
原算法除首次 H 接口外的完整源没有改变；实际数值表现仍须由新范围自然终态说明。
网络、编译和导入都在科学时钟内，无旧资格 preflight、A/B重复跑或额外独立测试。
构建失败同样记成本和实际边界，原物理 retained 状态仍由原 driver 的 FINAL 保存。

## 5. 最小消费入口与必要后继输入

下一次从 B030 正常自然终态恢复的**新 driver**可构造一个全段 engine：

```python
engine = TrueSecantSLSQP(
    original_minimize=old_minimize,
    model_identity=complete_bound_field_and_original_metric_row_recipe,
    emit=original_emit,
    check_clock=original_check_time,
    checkpoint=actual_prior_curvature_state_or_None,
)
minimize = engine.minimize
```

`complete_bound_field_and_original_metric_row_recipe` 必须由该新 request 的真实源 / 原metric行定义 / 参数链生成，
不是未经绑定的任意字符串。B030仍是原声明的静态设计：metric可随q变化，
这里固定的是整个原残差函数的定义，不把g宣称为固定，也不把变量q本身塞入需恒定的语义指纹。原 outer 在 snapshot 里另加 `engine.checkpoint()`，
只增加实际算法状态 / 费用；旧 source_input、pending队列、coarse/fine/orbit/nested/接受流程照原继承。
两个正在运行的 normal56e8 / normal311 不会被修改；本稿也不绑定尚未结束的某个猜测 q。
如果下一实际终态还有未闭 bracket，仍先按同 q / 同原网 / 全 pending 正常续接，不绕过该资格。

checkpoint 只保存3403个 packed数、82个旧点、82个加权梯度、实际非零 λ / 行 key、
当前语义和少量必要费用。完整 J、native workspace、逐步大轨迹 / 二进制不保存。
512 KiB必要输入上限包含小身份收据的余量；若完整 pending 超限，准确整体省略 pending并说明，
保留 H，绝不裁掉若干非零 λ 冒完整 secant。
更早全部成本留在调用者绑定的原终态完整 ledger；这里用前一曲率 checkpoint / cost 的 SHA
指向它，避免在必要 H 输入里再次递归复制同一长账本。

本地已做源码 / 补丁的文本核对及两个 Python文件的 AST解析；没有 import这些模块、
没有本地构建、数值求值或科学运行。该首次初始化和 secant 实作不提前宣称取得物理改善。
