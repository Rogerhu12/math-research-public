# 全部 868 个 direct-LD 块与原 1372 系统的独立接线

类型：计算流程与源码接口；作者：exact_refinement / root；日期：2026-11-14。

## 1. 当前范围

本说明登记两个独立源码入口；尚未运行本轮新矩阵的求解，也没有新的 native 接受或课题完成结论。

- `computations/exact_20261114_rawcell0_direct_ld_system.py` 绑定新的 868 个原坐标 binary64 Jacobian 块，并复用 actual41 的完整有限基态与方程数据。
- `computations/exact_20261114_rawcell0_direct_ld_equilibrated_correction.py` 在这个明确的新矩阵上调用冻结的完整带状均衡、LU 和精确残差修正程序。

新矩阵形成由独立 producer `geometry_20261114_native_rawcell0_direct_ld_capture.py` 负责。它按原 868 个已存步起点调用原局部导数函数，使用 actual50 已执行的 direct-longdouble RK 算术路径，最后一次转为原坐标 binary64。消费者不调用 RHS、root、ODE、局部导数、native solve 或 nonlinear trial。

actual50 只对 old43/step11 的完整给定四个有限局部导数矩阵做了精确参考对照；它不能证明其余 867 个块，也不能把 longdouble 成果当作精确 flow 导数。相应实际证据见 [actual50 全矩阵说明](2026-11-14-actual50-complete-rational-RK-reference-and-covariant-comparison.md)。本入口的目标是让全部新块与一次完整新方向一致，随后仍须读回原非线性方程。

源码字节身份（仅静态语法检查，尚无本轮数值执行）：

| 源码 | SHA256 |
|---|---|
| `exact_20261114_rawcell0_direct_ld_system.py` | `b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e` |
| `exact_20261114_rawcell0_direct_ld_equilibrated_correction.py` | `42e10320252935015c65bbc34579947e559182bb1b2a74ca1aa13a6597c064b9` |

本版 source pin 跟随完整 spec 的 gzip 传输修复。request52 在写入完整明文 spec 的 1MB 上限处停止，尚未启动 native、worker 或新矩阵形成；旧52源码仍由 Git 历史保留。本次仅更新 capture/hook/worker 的传输源码身份及 adapter/consumer 的对应 pin，窗口、actual50 算术、矩阵定义、均衡、LU、精确残差和原接受规则不变。

## 2. 不变的数据与唯一变化的数据

原件固定如下。

| 对象 | 身份 |
|---|---|
| actual28 完整原系统 result | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
| actual41 完整逐步 capture result | `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf` |
| actual41 原 1372 有限矩阵身份 | `e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521` |
| 原逐步 system binder | `fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81` |
| 完整均衡与修正 helper | `8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3` |
| 深度无关精确 dyadic row kernel | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` |

新 adapter 先实例化冻结的 `RawCell0StepSystem`，核原 `e929…` 身份。之后直接借用其只读 `base-states`、`stage-residuals`、`stage-out`、`original-scales`、`cut-residual`、`end-residual`、`original-far-graph`、`physical-height` 和 `cut-target`；每个数组都重新核原 raw SHA，包含 signed zero。**不从新 producer 的状态另造残差。**

唯一替换的是 old0…71 的 868 个 shape Jacobian。old72…575 的 504 个 actual28 块逐字复用。每个原 stage 内的 producer 行顺序是 inner→outer，消费者依原 `cells` 映射反序放入 outer→inner 的 shooting 方程；步数取 actual41 已验证的 `integrationGrid`。实际四个 cusp stage 11、28、31、63 各有 13 步，其余各有 12 步；不使用 `72×12` 代替真实 868。

producer 只在每个原 stage 最后一原步的 Pi 出口施原 port 除法，消费者不再施一次。新两行 mean Jacobian 完整保留、核 hash，但原 native shape 系统仍为每节点 224 个变量；不会把 mean 行混入 224 个 shape 方程。

保持的系统是 1372 段、1373 节点、112 个非零模式、每节点 224 个变量，共 307552 个变量和同数方程。`old_to_new` 完整保留原 577 节点；插入节点的 sigma 仍为其原 parent stage 的实际 sigma，原节点 sigma 字节保持。

## 3. 完整新来源绑定

CLI 必须给本次实际 `result.json` 的 SHA256。新 producer 的四个源码 SHA 必须与当前已检出的四个对应源码逐字相同；这些身份全部进入新 binding。源码或结果未生成时不填写猜测值。

新 result/summary 中 `array_manifest`、`summary`、`stage_reports` 均用 `{file, bytes, sha256}` 描述器。所有 72 stage 报告逐一核对 `stage`、`original_stage`、真实 `step_count`、原 `schedule`、actual41 `full_states` 与 `shape_outputs` 的 raw SHA。每一步还核原完整起点、四个局部调用的状态与几何记录、原 h 和端口位置的逐位身份；这属于同一有限基态的来源验证，不是容差门。

每个新数组沿冻结 `StepArrays` 规则核所有完整 chunk：唯一名称、顺序与覆盖、shape、`<f8`、C-order、每文件 size/SHA、原始 bytes SHA、全数组串接 SHA。追加的 chunk journal 允许不同数组交错写入，但核每个 `(array, chunk_index)` 恰好一次、各数组内部顺序不变。

完整 1372 个块的虚拟流 SHA、逐块来源和 raw SHA、所有不变数组 SHA、旧新节点映射、四源身份以及新 result SHA 一起形成独立 `new_matrix_identity_sha256`。输入保全为 `input-binding.json.gz`；它包含完整原 `original1372_input_binding` 和新的 direct producer 身份。没有 G-shadow 或第二个可替代目标矩阵。

## 4. 方程、均衡与精确读回

令新已存 binary64 Jacobian 为 $\widetilde J_n$，所有已存残差与 sigma 仍取 actual41。阶段方程仍为

$$
\widetilde J_n\delta_{n+1}-\delta_n+r_n=0.
$$

cut 行仍为 $\delta_{0,Q}+r_{\mathrm{cut}}=0$，far 行仍为 $\delta_{D,\Pi}-G_D\delta_{D,Q}+r_{\mathrm{far}}=0$，其中原 $G_D$ 的完整对角数组逐字保留。新矩阵不是原 `e929…` 的矩阵，也不是其 G 变换影子。

消费者数学主体沿冻结 `30a467…` 逐步 consumer，继续使用冻结 `8f5cb5…` helper：原 sigma 邻近二幂作为初始表示尺度，三轮最大元素行列均衡，最后从原系数一次 `ldexp` 形成完整带矩阵；使用 `dgbtrf/dgbtrs`，从列尺度恢复完整原坐标方向。没有删模、截行、截奇异值或附加 ridge。

每一保留候选的所有 cut、1372 stage、far 行都由冻结 dyadic kernel 计算。对实际 binary64 保存数组，先精确形成 $r_n+\widetilde J_n\delta_{n+1}-\delta_n$，之后精确除以该行原 sigma。**没有先把 $J/\sigma$ 或 $r/\sigma$ 舍入为另一个矩阵。**逐行整数账、完整行序、各段最大值、全局最大值、最坏行全部操作数的 f64 bits 和正确舍入的修正 RHS 均保全。

精确残差修正最多使用显式预算，严格改善时才替换当前保留方向；未改善时保留上一完整方向。这个选择规则只比较本次新有限矩阵的候选。它不声称 computed Jacobian 是精确 $DF$，也不把小线性缺陷加入原 nonlinear trial 的准入标准。

原 576 长矩阵下的 577 节点限制只作原有附加诊断，既不选择也不拒绝新方向。最终方向仍须通过原全部 nonlinear guards、原 sigma norm 和原接受逻辑；本程序不运行这些试步，不宣称 native accepted。

## 5. 输出合同

| 输出 | schema 或关键合同 |
|---|---|
| `result.json.gz` | `native-rawcell0-direct-LD-f64-J1372-equilibrated-band-correction-v1` |
| `summary.json` | `native-direct-LD-f64-J1372-equilibrated-small-summary-v1`；完整 result 描述器和已存小读数 |
| full checkpoint | `complete-native-direct-LD-f64-J1372-shooting-direction-v1` |
| 原577节点限制 checkpoint | `complete-original-node-restriction-of-direct-LD-f64-J1372-direction-v1` |
| 输出数组清单 | `native-direct-LD-f64-J1372-shooting-direction-arrays-v1` |
| 输入 binding | `native-rawcell0-direct-longdouble-system-binding-v1` |

顶层继续保留 `step_delta`、`step_direction_checkpoint`、`restricted_old_node_delta`、`restricted_direction_checkpoint` 四个完整描述器。两个 checkpoint 都保存完整来源对象、逐节点方向、negative-zero 列、raw SHA 与 `old_to_new`；限制明确是该完整新方向在原 577 节点的字节抽取，不能冒原 producer/schema。

full result 中 `input_binding` 是 `input-binding.json.gz` 的描述器；checkpoint 中 `input_binding` 是同一个完整 binding 对象。`summary.json` 只选已有报告的值，不重算 norm。若将来的附加读数使实际格式化 JSON 接近 100KB，则保留完整 result 并输出小 receipt；这个出版控制不把已完成数值结果改为失败。

所有大阵、完整行账和方向保留在 artifact；不复制巨型新 J 虚拟流到输出目录。输入包的完整 array manifest 与所有 raw SHA 仍是结果身份的一部分。

## 6. 运行合同与资源

仅在 `GITHUB_ACTIONS=true` 且本公开仓库运行。

```bash
python "$C/exact_20261114_rawcell0_direct_ld_equilibrated_correction.py" \
  --capture-directory "$CAP28/native-correction-capture" \
  --step-directory "$CAP41/native-rawcell0-step-capture" \
  --step-result-sha256 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf \
  --direct-directory "$VISIBLE_OUT/native-rawcell0-direct-ld" \
  --direct-result-sha256 "$ACTUAL_DIRECT_RESULT_SHA" \
  --equilibration-passes 3 --refinement-steps 3 --exact-workers 2 \
  --max-band-bytes 4294967296 \
  --out "$VISIBLE_OUT/rawcell0-direct-ld-correction"
```

`ACTUAL_DIRECT_RESULT_SHA` 必须在 capture 真正完成后由其原始 `result.json` bytes 取得。默认 3 轮均衡、最多 3 次后续误差修正、2 个 exact worker；不猜未来实际结果。它复用原完整带宽 `kl=112`、`ku=335`，单个 Fortran-order band 的实际尺寸仍是 `[560,307552]`、1377832960 字节。报告分别保存声明上限、可能的 LAPACK copy、实际共享内存/指针、RSS、LU 与 pivot hash、逐求解时间及恢复尺度账。

资源上限只限制是否能容纳完整系统，不允许截掉 cusp 步、行或模态。原始/new manifest 与 Python exact 整数、进程和 BLAS 工作区另行说明，不把单 band 的预算冒总 RSS。

## 7. 尚未支付的部分

新 producer 与消费者的首次真实执行、完整 raw 字节回执、新方向的原 nonlinear 十试步及最终原容差接受均未由这份源码说明支付。新 J 的有限精度与真正 flow 导数之间的误差仍独立；单块 actual50 精确参考不会自动推广为全部 868 块的精确证明。

若本次一致新矩阵仍给出无效方向，后续可以在原完整方程与原尺度上研究阻尼 least-squares/有界方向，保持原 cut/H/far 和最终接受逻辑；本入口没有实现该替代算法，也不通过重复同一错误修正来预言其有效性。
