# 完整场的 R241 连续覆盖接口（尚未数值运行）

新增独立入口 `computations/geometry_20261114_full_state_continuous_cover.py`，
24,245 B，SHA256
`c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6`。
它把已有空间覆盖门接到真正接受的完整 v3 设计场或 v4 同度量精化场。
当前没有用 prepared、失败态或旧 A 代替新接受输入；本条只登记源码和接口，
没有新的覆盖数值结果。

## 场与输入的身份

新入口要求同一份 checkpoint、原 port、实际尾 config、最终实际 audited tail
response、完整径向 readout，以及该场已经生成的 plan、assembly、phase-zero mesh、
source background 和 normal packet。它沿用原完整场消费者的接受状态、全部 H、
完整 J、config、native source SHA、材料投影和物理 cut 门，并额外核对闭包各文件的
SHA 链；source background 必须同时绑定这份 plan 和 config。

`assembly.large_core_prefix` 决定是否启用 R249 inlet normal form。
入口调用 `geometry_20261114_inlet_parity_normal_form.read_saved(checkpoint, normalize=...)`，
随后要求整个 SavedPrefix 定义与 plan/assembly 一致，包括原始/新 nodal hashes、
源码、完整材料图和 normal-form 定义。没有该标记的输入不会被悄悄修补。
启用修补后的闭网格必须由同一接口重新生成；旧 plan 的 heights 不能冒作新 plan 的输入。

完整前缀的全部 `z0` 保留。所有活动中心直接调用 `LargeCoreAssembly.prefix_jets`
或 `tail_jets`；前缀角细分子点也直接读完整场。反射只作用于独立输出切片。
使用 assembly 已记录的唯一 planar registration 的 angle/translation，并检查其
cos/sin 矩阵定义；不另做 SVD 拟合。完整 mean gauge、实际尾和完整角 cut correction
继续与已生成的闭包相同。

所有中心位置与同材料点的已绑定 mesh 比较，法向与 normal packet 的共点比较。
这些比较检查接口一致性，不由此推出连续误差包络。前缀及 tail/collar 的中心法向
都由各自实际一阶 jet 得到；法向方向约定与原 assembly 相同。

## 保留的数学门与余量

原 `geometry_20261114_continuous_cover_budget_v3.py` 的 SHA256 为
`3362fc35c09b98a8feb10706f2b126c9bc45e7d45a4294c928b4b72e59d2c7a1`。
新入口运行时锁定它及原 assembly、tail adapter、position-cover writer 的 SHA。
源码适配只替换输入、场读出和来源说明；R241 的 distance、short-path、normal-cone、
cap exclusion、失败前缀父对的角细分门，以及 R37 直径/R24 marker 预算原式保留。

静态检查确认空间 pair-gate 整段逐字相同，段 SHA256 为
`3ccbb14d6c92d1975c3da2c4ee7c3c67bcf6b47f1d7a82c44cd89aba9128a599`；
diameter/marker 段逐字相同，段 SHA256 为
`792161f96da39473ed2b33515f6ee4cdc75f2a3436306eebf2453e79350b4d1f`。
源文件及实际变换出的程序均通过 AST 解析；没有本地执行数学运算。
变换程序 SHA256 为
`b800b0727c8c1683589fa80df9bb405443b19c3665e2a0b89d538d83b2b20e52`。

旧子点位置的 `3*position_error` 余量仍保留，但不再使用省略共同 mean 的角差恒等式：
每个子点现在是一次完整场求值。原门公式没有因换入口放宽。

## Actions 调用

仅允许在 `Rogerhu12/math-research-public` 自己的 GitHub Actions 中运行。
以下路径/包络变量由该次真实闭包 job 提供；包络须针对它自己的完整有限场，不能继承旧 A。

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_state_continuous_cover.py \
  --directory "$CLOSED" --basename surface \
  --checkpoint "$ACTUAL" --config "$CFG" --tail-response "$FINAL_AUDIT" \
  --complete "$COMPLETE" --source-topic "$SRC" --port "$PORT" \
  --curvature-upper "$K_BOUND" --relative-metric-upper "$METRIC_BOUND" \
  --tail-slope-upper "$SLOPE_BOUND" --radius-lipschitz-upper "$RADIUS_LIP" \
  --position-error "$POSITION_ERROR" --normal-angle-error "$NORMAL_ERROR" \
  --prefix-angular-subdivision "$CHILDREN" \
  --out "$OUT/full-state-cover.json"
```

`--basename surface` 对应 `surface-plan.json`、`surface-assembly.json`、
`surface-phase0.ply.gz`、`surface-heights.json` 和 `surface-normal-samples.npz`。
`--complete` 仍消费原径向 adapter 的完整 metadata 及其 hash-bound 节点文件；不删尾节点。
可另传原有 radial/angular strides 和批量参数。

输出包括覆盖报告以及分块的完整活动域 position-cover packet。包内记录实际闭包文件名、
完整场身份和中心对应的原 mesh material-query indices；中心本身来自直接求值。
原 held-Hausdorff CLI 的 `bundle_paths` 仍硬编码旧文件名，后续消费新 packet 时须显式
适配这一定位接口，不能直接把旧 A 路径当作新闭包。position-cover writer 本身已在此入口
中绑定实际新路径，原写包公式不变。

## 本次没有建立的结论

曲率、relative metric、尾斜率、半径 Lipschitz、位置及法向误差都是显式输入，
尚未由本入口证明为全域连续上界。样本被这些数覆盖也不等于区间证书。
R241 的覆盖结论仍以实际闭面为 regular closed C2 immersion、所有输入包络有效为条件。
R249 只处理已记录的 inlet parity normal form，其他 seam 和有限场问题没有被这条接口消去。
报告保留 `continuous_reach_interval_certificate=false`、`task_completed=false`；
不宣布新的 nonlinear BVP 接受、所需振幅、精确同 g 极限或课题完成。
