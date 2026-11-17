# n4 第一批：已有数值终态、旧基底诊断和消费窗口头部

本包冻结七组普通 flat 子午线线性设计、v25 q=.005 M4 的五个 homotopy 点、其固定度量 M8 失败，以及新的 case1 消费窗口 M6 试验。它们均未给出本题所需的非线性闭合族。正在运行的窄圆弧新窗不属于本包。

## 已知结论

- 普通 vu=.25/vd=.30 的 M4 λ=0 采样 metric 为 5.27e−9，但 λ=.1/.3/.6/1 分别升至约 3.36e−4、.001199、.002332、**.004072**。五次 collocation 接受不等于完整等距验收。λ=1 的精确核心圆弧半径是 .925，这个低 q 试验也不是 R19 的目标大振幅核心。
- 固定该 λ=1 度量的 M8 尝试达到节点上限，rms≈1.859、BC≈.12151，不能记成加密收敛。
- case1 的旧适配器最初在构造一个未使用的 legacy Hermite bridge 时退出，尚未进入 BVP。保留的初始化修正只接入实际使用的 ShortBridge，没有修改数学方程或正则域门。修正后 M6 λ=0 虽被求解器接受，完整 metric 仍为 1.67870e−4；λ=.15 在核心 ρ 正性检查处失败。
- 对后一失败，旧 t^6(1−t)^6 控制的低矩病态有直接数值证据：M6 ρ 矩条件数约 2.16e4，所需控制ℓ1约139.48；已表示ρ修正∞范数仅.00202，而恢复compact时的高频余项∞范数约12.53。固定该旧向量的同伦在 λ≈.08551 已出现ρ零。这个说明只针对该参数化/预测器，不是不可能性定理。
- `consumed_head/` 是另已完成的两个 m4 线性根、子午线源与有理 head 证书。其背景包围球只是采样，闭合和非线性前缀另需支付。

完整必要标量、实际输入/输出 SHA、失败分类和原记录参数在 `completed_first_batch.json`；旧基矩必要标量在 `old_basis_scalar_summary.json`。不包含可重算的 chart、DN、H、checkpoint、网格或角数组。

## 可移植恢复

```sh
python prepare_runtime.py --repo REPO --dest NEW_SCRATCH_RUNTIME
```

这一步恢复 70 个逐项 SHA 核验的原始源，复制本批冻结的 n4 helper 源，使用原950f真实 worker重新生成 m4 canonical8 端口，并再生原七组线性 profile/chart。它核 canonical 端口字节 SHA，然后写出 `bvp_replay_commands.json`，**不执行 BVP**。

端口实际输入为 `inputs/mode4_physical_config.json`：spacing=4、quadrature=256，其余原 r=.3/w=.08 物理工厂参数逐字面保存。导出器的历史 docstring 含“m3”，但代码的频率由配置 spacing 读取，未将三重端口冒充四重端口。

`regenerate_linear_cases.py` 对冻结原 `screen_linear_even.py` 只替换四个绝对路径绑定，保留数学源和原 SHA，并在运行目录记录变换后的 SHA。所有 chart 和生成端口均写到 scratch。

`bvp_replay_commands.json` 中的命令从保存的 parsed arguments 完整重建，显式补入等价 source/port/default-profile 路径。它们标为 **replay**，不假称原 shell argv。两组 v25 旧记录未保存顶层执行脚本 hash：本包将该字段留空，保留冻结当前源 hash、已记录底层源变换以及父模板的转换配方。window M6 的运行时脚本 SHA 与冻结源逐字节匹配。

初始 legacy-bridge 错误源已从两条记录过的修正精确逆变换，并通过原 old_sha256 验证，存为 `source/even_window_prefix_initial_failed.py`。它和修正后真实 BVP 失败分别列出，不混为几何障碍。

## 源完整性与限制

`source/` 的原执行/捕获源未为打包而修改。`provenance/` 保留 n4 变换配方和初始化修正的 old/new SHA。`recovery/` 是当前 source-only 70项依赖闭包，包含 original coupled worker/client、ShortBridge、所有 CJS 工厂依赖；生成数据不会进入仓库。

本包只记录数值事实和具体诊断。未给出完整闭曲面、全相位嵌入/reach证书或共同 g 的有效收敛序列。

## 实际空目录恢复检查

`recovery_smoke_result.json` 记录已实际完成的恢复：70 源逐项核验、真实四重 canonical8 端口字节 SHA 一致，七组线性案例的全部标量逐值一致，三条 BVP replay 命令已生成；没有重跑 BVP。

另附已完成旧基底的公平锁主模对照：`old_basis_locked_scalar_summary.json` 包含 a=.28/.16/.145、M4/6/8 的必要条件数与 canonical 放大标量，两个源可独立再生完整诊断。它与新的窄窗 BVP 无关。锁主模零是额外约束，其代价与仅解高模分开报告；sup 范数仍是采样值。
