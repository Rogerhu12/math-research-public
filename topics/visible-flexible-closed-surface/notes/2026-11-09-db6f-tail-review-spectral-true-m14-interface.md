# 真 M14 联解的谱权接口：全文静态独审

审查者：`/root/tail_theory`，2026-11-09。结论：**PASS，限于冻结计划的方程等价、原调用接口及已闭输入身份。** 没有执行新选择器、导入或实例化候选类，也没有运行初始化、Newton install、BVP、DN、root 或 flow。未来新实现仍须另行全文审；本次没有预付其正确性或数值成功。

## 1. 冻结对象与实际核查

全文审查 `notes/2026-11-09-db6f-prefix-spectral-true-m14-interface.md`，13430 字节，SHA256 `39516e14f7185ecd4ff14c3a4df7c8501794a90bc34be0bb2622371f0b6c3f6d`。来源账本 SHA256 `150a196fc14b79ec21f0cae635d32f8635617ee79b14edd646b5449e50c50800`，正文七节均已读。

重新全文核读的关键代码为原 `db6f-prefix-coupled.py`、flat loader、谱权 v2 模块、shared client、preserve-restart、domain-aware Newton，并逐段检查 shared worker 的原初猜/恢复路径及 core 的返回维数。其余已审导出与连续证书组件按冻结身份复用；没有把它们的旧数值结论移植给未来新图。

独立 stdlib-only AST/metadata 检查实际回执 **`7120c6`、退出码 0**，工具报告耗时 `.09878965` 秒。39 项稿件来源及旧 affine launch 的 97 项输入全部重哈希，共 117 个不同文件前后同值；同时核了已闭 M14 自身的状态/参数/最后真实 tail schema、两个 prefix 系数分片的哈希和状态分区。

报告为 `notes/2026-11-09-db6f-tail-review-spectral-true-m14-interface-check.json`，35857 字节，SHA256 `262ae71305c8c3c588fc8831d0970c51051b25d0d866f36e33f645c192092627`。该检查没有载入系数数组或求解对象来运行方程；只读元数据、分片字节哈希及源码 AST。

## 2. 共轭代数与物理端口

M14 的状态数为 $3M+1=43$，参数数为14。固定正对角 $W$ 后令 $u=Wy$，方程及 BC 变为

$$
u'=Wf(x,W^{-1}u,p),\qquad
b(W^{-1}u_a,W^{-1}u_b,p)=0.
$$

链式法则准确给出

$$
\partial_u(Wf)=Wf_yW^{-1},\qquad
\partial_p(Wf)=Wf_p,
$$

以及两端 BC 状态列乘 $W^{-1}$，BC 参数列不变。实际谱权模块按此实现；其物理回调拿到的始终是 $W^{-1}u$ 和原参数 $p$。因此 TailMixin 中的物理请求仍是 $H=\sigma q_gY_Z$，原 tail slope Jacobian 的尺度和 $1/\sqrt E$ 链式因子没有额外乘谱权。

BC 值没有重新加权；只是其对新数值状态的 Jacobian 状态列换元。原 `physical_bc_tol/bc_tol` 行缩放仍由原 BVP 设置支付，不能再把 $W$ 加入物理高度或 BC 容差。

整数独立核验得到43个权重，首槽为1，其余三块相同；第 $j$ 模的权重为不小于 $1+9j^2$ 的二幂，且严格小于该数的两倍，最大权重2048。这是已审模块实际采用的权重，非新拟合参数。

零点集合等价不等于有限精度轨迹相同。带权 RMS 与 domain-aware Newton 的状态步范数改变了误差控制和回溯；参数并未随状态缩放。稿件已正确保留这个区别，没有把加权后的数值变化称为纯 Fourier 模数效应。

## 3. 两个真正的插入点与 lagged 外层

原 `solve_with_actual_tail` 恰有两处对未被局部变量遮蔽的 module-global `solve_bvp` 调用：非 lagged 路径的一次调用，以及 lagged 循环内的调用。flat loader 的 `.m` 就是含这两个调用的模块，故仅替换 `.m.solve_bvp` 在接口上足够；不需要替换 TailMixin、tail worker 或原非线性方程。

原 lagged 控制流已逐行核实：先用实际物理高度请求真 DN/J；至多八次内层 BVP；内层期间 `o.tail` 暂换成其真实响应导出的 affine slope port；`finally` 无条件恢复真 tail；内层成功后，对新的物理高度再请求真实 DN/J，然后以原 `o.bc` 检查实际外边界。满足原 `bc_tol` 才返回成功外层；八次仍不过则抛异常。

这里须明确一个容易混淆的量：**谱权 callable 返回前重算的 physical BC，是当前内层 affine 端口下、以物理状态计算的 BC。** 在它执行时，原 `finally` 尚未恢复真 tail。这不影响共轭正确性，但该内层物理 BC 不能冒充真实非线性 BC 证书；后者由恢复后的新 DN/J 和 `o.bc` 另付。冻结稿保留了完整控制流，本审查将此作用域显式写出，不要求修改原稿。

最后 seam 的 `audit=True` 绕过 shared client 的缓存，并请求 `jacobian=True`。需要沿保存 CP 的 `tail_seam.tail_record` 定位这个真实包；不能假定最终包永远是某个固定 call 序号。

## 4. 物理返回对象与实际运行身份

谱权 v2 的返回 `y/yp/PPoly` 已除以权重，参数保持原值。其 cubic PPoly 的自变量仍是原数值 chart 坐标，不是直接改名为物理经线坐标。原 coupled 随后执行 chart 转换、原 `flow.c2_interpolant`、物理 audit 和完整 seam；这条路径必须保持。

原 main 保存的是物理 quintic。物理 cubic 的 RMS、quintic 的采样 metric 和新图的连续 metric 是三个不同对象；计划没有把它们混用。谱权模块的原物理 RMS/BC 复核只会将已加权成功降为失败，不会将原 solver 失败升级。原失败 CP 仍可能被写出，随后甚至可能产生 seam 数据；因此最后必须同时检查 `solver_success`、summary 的 error、真实外层记录和最后 seam，不能只看 CP 存在或工具退出0。

运行期还须保留计划列出的身份门：原 main 执行 `domain_newton.install()` 之后，核 `_bvp.solve_newton` 与被审 `domain_newton.solve_newton` 为同一对象，且来源、函数签名及源码一致；返回和异常路径都记录身份。SciPy 磁盘哈希本身不足以证明这个运行期事实。本轮只静态核了其可接入位置，没有提前运行 install 或声称门已支付。

新 selector 的真实哈希及谱权调用记录应进入独立 reproduction。原 CP 不自动保存全部 `spectral_coordinate_audit`，不能靠替换 callable 后省略这份账本。prefix 的新来源也不能伪写成旧 driver；另一方面，本方案未改 tail 引擎，其实际响应仍应是普通 shared 八源，而非 M15 trial 八源或 linear-continuation 九源。

## 5. 已闭 M14 输入与 schema

优先输入的真实 M14/N512 CP 为 SHA256 `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0`，其自己的末包 `_tail_0002.json.gz` 为 `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762`。这组闭来源的以下维数已实际重新核查：

| 对象 | M14 的实际维数 |
|---|---:|
| prefix 状态 / 参数 / 中央高模尺度 |43 / 14 / 13|
| tail height Jacobian |616|
| cut jets |14个标量，3个长度14向量|
| tail audit |8个标量|
| staged / raw states |865×28 / 13×28|
| seam 角样本 |896|

原配置为 spacing3、depth12、parts8、steps32、N512、36轮、`solveTolerance=2e-9`。实际旧 config 没有 `trialDiagnosticFile`、`trialStatePrefix`、`projectionFloor` 或 `correctInitialBoundary`；因此准备器应保留相应缺席，并由已审原源码继续给出 `.05` 和默认边界修正。不能因 Python bool/number 比较相等而放过 JSON 类型变化。

原 preserve-restart 的六项固定输入、保存 mesh/chart、自由参数及入口修正应保持。初次请求须取真正重建后的 $H$；PPoly 重求不保证与旧尾目标逐位相同，原线性 warm 边界修正和真正 DN 仍不可省略。

若将来改用谱权 affine 输出作初猜，必须独立绑定其未解身份，仍以真实 tail warm 开始并对新目标真求解。本次优先用原真 M14 输入，不能通过翻转 affine 的标签制造真联解。

## 6. 后续认证和 G5 范围

正文没有要求修改或绕过现有 M15 身份工具。`prepare-final-m15-coupling-v3` 仍绑定 continuation03、M15、目标 s=1 和705项 Jacobian；matched-cut auditor 也仍绑定其自己的121输入和 trial 来源。这些工具不能直接当 M14 gate，应另建保留原数学门、但具有正确 M14 身份的关闭审计。

同一物理 $g$ 下换模数或改变数值误差控制不要求必须达到 M15；README 的要求落在真实新图、同 $g$ 加密到原精度以及全部几何/独立重跑门。旧 M14 非单调历史仍须保留。真 N512 要重新经历实际 root/flow/DN/外层，不由 exporter 的 angular 参数支付；parts8×steps32仍是原生径向分辨率，不能重命名为新 RK 对照。

新图需要自己的共同切口、完整尾表示、连续 metric/曲率、全时嵌入/reach、握持和非全等、网格及独立完整重跑。旧 supplier 或方法可以经相同 $g$ 和实际 manifest 绑定复用，旧图上的数值上界不能直接移植。

M14 的导出整数账本也核实：degree192 的 planar signed 模共128项，height15项，合计143系数；stride为575，1000行的原始 binary64 数据为4,600,000字节。仍须以实际输出核单文件限制，不把这个计数当作导出完成。Cartesian cutoff 也不等于 solver M14。

## 7. 结论与下一步边界

冻结计划在数学共轭、原 callback/返回 schema、实际 DN 外层和 M14 身份上没有必须修正的问题，可以作为新选择器与纯准备器的实现依据。

本次只付静态接口。新实现必须另核实际 module 注入、运行期身份门、I/O 隔离、配置 typed copy、完整输入绑定及失败关闭记录；实际真实联解、谱权改善、连续新图证书和独立完整重跑均未由本审查发生或保证。
