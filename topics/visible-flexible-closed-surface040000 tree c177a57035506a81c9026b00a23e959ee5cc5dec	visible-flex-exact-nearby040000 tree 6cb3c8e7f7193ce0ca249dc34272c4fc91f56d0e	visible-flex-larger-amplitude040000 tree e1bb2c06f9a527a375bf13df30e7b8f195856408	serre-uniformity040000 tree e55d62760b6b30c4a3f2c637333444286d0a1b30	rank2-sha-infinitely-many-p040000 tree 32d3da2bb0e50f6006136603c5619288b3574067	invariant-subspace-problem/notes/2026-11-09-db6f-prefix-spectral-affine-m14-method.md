# M14/N512 的谱权仿射诊断：冻结输入与最小接线

状态：**实现与纯输入准备；尚未运行真实 BVP 或 DN。** 作者为 `coupled_prefix`。谱权共轭模块已有完整独审；本批新 runner 与准备器另交 `tail_theory` 全文审查。本诊断的全部新结果均保持

$$
\texttt{actual\_nonlinear\_tail=false},\qquad
\texttt{frozen\_affine\_dn=true}.
$$

即使配点成功，也只是冻结仿射边界问题的成功，不能称为新的真联解、完整图或 README 完成门已经满足。

## 1. 唯一输入问题

基线是冻结 `scripts/db6f-prefix-affine-replay.py`，SHA `8eab6d580c2ad04a794e051c6b552eebe3d6d228feb653b9fa84cd4a9b3d34a4`。新 runner 复制其数学流程，使用真正完成的 M14/N512 prefix，及该 prefix **自己的**最终真实 DN/J/audit 包：

| 输入 | SHA256 |
|---|---|
| `...fixed-m14-d12-p8-s32-q512-outer-from14.json.gz` | `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0` |
| 同 stem 的 `_tail_0002.json.gz` | `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762` |
| 原物理 linear port | `500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702` |

完整绝对路径在新 launch 中。原 tail 包明确 `converged=true`，真实 residual 为 `5.397833270174952e-10`，请求 Jac/audit 均 true，物理 Jacobian 长度为 $(3\cdot14+2)14=616$，17 个完整 jet 字段及 8 个 audit 字段均核验。prefix 的原 `tail_seam.tail_record` 必须精确指向该包；不能改用另一幅图的 DN。

原已发布闭清单 `prefix-m14q512-m15failed-publication.json` 和原 reproduction/summary 同时绑定，区分其 M14 真成功与 M15 的历史失败。它们只是已完成输入的来源；本批不修改或重标旧结果。

保持 $M=14$、prefix 角求积 $N=512$、原冻结 metric、原 gauge $0.1$ 与原 warp reference $0.1$。三项容差分别为

$$
\mathrm{tol}=2\times10^{-9},\qquad
\mathrm{bc\_tol}=10^{-8},\qquad
\mathrm{physical\_bc\_tol}=2\times10^{-11}.
$$

`max_nodes=6500` 只是本次配点资源上限。没有改变模态、真实尾的 RK 步长、尾角求积、projection floor 或物理参数；实际上本诊断根本不发出新尾请求。

## 2. 数学体中的唯一替换

原仿射端口仍由 `AffineTailForInnerBVP` 给出：以原请求 $H_0$ 及其真实物理 slope/Jacobian 为基点，

$$
S_{\rm aff}(H)=S_0+J_0(H-H_0).
$$

原 `TailMixin.terminal`、`TailMixin.bc_jac`、中央 support 参数、free parameter、数值 chart、saved-mesh restart 和所有 callback 原样复用。新代码不调用 `seam_audit`，因为仿射端口不能提供新的真实尾二 jet 审计。

唯一数值变量改变是已审模块

`scripts/db6f-root-spectral-collocation-v2.py`

SHA `47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854` 的

`make_solver(power2_weights(14))`。

设原 43 个物理未知量为一个 mean 槽及三组 14 模系数。mean 权为 1，其余三组第 $j$ 模采用不小于 $1+(3j)^2$ 的最小二幂。正对角 $W$ 只作 $u=Wy$ 共轭；参数 $p$ 不变，边界仍以物理 $y=W^{-1}u$ 代入原式。模块返回物理 `y/yp/PPoly`，并复算原物理 cubic collocation RMS 与原 scaled BC。

随后仍按基线执行

1. `physical.x = obj.chart(sol.x, sol.p[0])[0]`；
2. `physical.y = sol.y`（此时已经是物理未知量）；
3. `physical.sol = flow.c2_interpolant(physical)`。

这个最后的 quintic C² 图使用原 `adapt_c2_interpolant`。**原 cubic RMS 只标记配点残差，不能据此冒称新 quintic 图的实际 metric。** 新 quintic 的有限采样诊断仍调用原 `adaptive.audit`；若需要真联解和连续证书，后续必须按原真实 DN 及完整图流程另做。

## 3. 原边界与六项物理身份

沿用原 `bcweights=physical_bc_tol/bc_tol`。新增 `boundary_diagnostics` 只报告原 scaled BC、原 inlet BC 和原物理 terminal 分子

$$
q\,f_Z(L,y,p)-\frac{S_{\rm aff}(H)}{\sqrt{E_{\rm cut}}},
\qquad H=\sigma q y_Z(L).
$$

它不增加新的二 jet、曲率、几何或嵌入阈值。实际 `solver_success` 来自已审模块的加权求解结果及其原物理残差门。

原 restart 的六项检查全部预绑定，并在真正调用原 restart 时仍再次执行：`angular_chart`、`chart`、`frozen_profile`、`physical_tail_parameters`、`physical_tail_cut`、`warp_reference_q`。gauge、物理 port 文件、profile/chart 原文件、tail config 和全部 coefficient chunks 也独立绑定。纯准备不运行 restart，也不声称已经支付其实际几何初始化门。

## 4. Newton 的运行身份

SciPy `_bvp.py` 的已审磁盘 SHA 只确认布局，不能证明实际调用的 Newton 函数是谁。新 runner 在真正调用原 `f6curve_domain_newton.install()` 后，立即要求

`scipy.integrate._bvp.solve_newton is f6curve_domain_newton.solve_newton`。

还检查其运行函数文件、qualname、首行、完整函数源码摘要和原 11 参数签名。求解返回后再次要求同一对象身份。这样不会把此前 toy 中未安装该 patch 的 SciPy 默认 Newton 当成本次原 prefix Newton。

15 个原 callback 都有独立 AST 来源绑定；真正 runner 在创建对象后核查其运行函数。范围含原 RHS/Jacobian、BC/Jacobian、terminal、中央 initial、chart、物理 flow RHS/Jacobian、C² 插值、仿射 DN、restart、save_checkpoint、domain install 与 domain Newton。它们的来源文件也都在 97 项 launch 绑定中。

## 5. 闭包范围与一次纯准备拒绝

初次纯准备工具 receipt `1141ac`、实际 exit 1，未写任何输出、未初始化或求解。原因是过宽的递归 AST 扫描把旧依赖模块从未调用的 CLI `main()` 也展开，因而要求两个不在当前可重现源目录中的旧 screen/recording 模块。该原准备器的精确字节已保存在

`scripts/db6f-prefix-prepare-spectral-affine-m14-pre-closure-scope.py`

SHA `f4215d26fd7b2ca297c559ca69bb6f9ee1467317a097b0479042460b7a56c0ea`。

实际所需回调和导入不依赖那两个 CLI。修订准备器明确把**未调用的依赖 CLI main**列入 launch 的排除入口，保留其整个源文件绑定；实际新 runner 自己的 main 及其导入不被排除。全部给定 source-root Python、实际回调链、flat acceleration law、原静态 client 定义、旧真实 DN 八源及被解析的本地导入均绑定。该闭包不声称可单独启动这些被排除的旧 CLI，也没有制造替代依赖文件。

第二次纯准备 receipt `9e16d0`，实际 exit 0，得到 97 项绑定的新 launch。没有构造 prefix、bridge、flow、真实 tail client；没有调用原 Newton install、谱权 solver factory、BVP 或 DN。

另外，定义层核对脚本 `db6f-prefix-check-spectral-affine-definitions.py` 实际 receipt `d0a6a9`、exit 0：只加载真实模块/类定义，15 个未绑定方法的真实 Python 来源全部吻合，SciPy 当前 Newton 对象未改变。它不构造对象、不调用任何 callback，也没有支付未来 runner 的“安装之后”运行门。该门仍必须由真实运行执行。

## 6. 新 I/O 与未来唯一命令

新 stem 为

`notes/2026-11-09-db6f-prefix-spectral-affine-m14q512-01`。

目前只存在 `-launch.json` 和 `-preparation.json`。未来 stdout、reproduction、summary、CP 及 coefficient 文件都预先列在 launch 中，不能复用旧 stem。原 tail config 只作为已审输入和输出 provenance，不启动 worker，故没有创建新的尾 trace、iteration 或 trial I/O。

未来 cwd 是仓库根目录；由 root 完成源码审查与资源检查后持有实际进程，命令为：

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/scripts/db6f-prefix-spectral-affine-replay.py \
  --launch /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json
```

stdout 为同 stem 的 `-run.log`。本批未执行此命令。不要用会改写本 runner reproduction 的另一 bound-command 包装器；若 root 加 guard，guard 观察记录须使用独立文件。

运行程序只写 `requested_process_exit_code`，不伪造实际 tool 退出。若配点未成功或捕获异常，程序请求 exit 2；完整配点流程成功则请求 exit 0，但两种情况都仍是仿射诊断。真正工具退出、会话和 receipt 由 root 另行实测。若 C² 重建或采样 audit 在首次保存 CP 后异常，任何已有 CP 也不代替最终 reproduction/summary 的完整状态。

所有新系数仍由原 `save_checkpoint` 按 4.4 MB 原始块 gzip 保存，并拒绝大于 5 MB 的压缩块；不改变系数或分片定义。完整源、纯准备和定义检查、真实失败/成功退出历史及本说明由同批闭清单绑定。
