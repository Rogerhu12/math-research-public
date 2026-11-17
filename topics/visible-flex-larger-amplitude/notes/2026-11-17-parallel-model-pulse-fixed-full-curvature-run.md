# 同一 pulse 开前缀的固定全连续曲率计划（准备及唯一运行启动）

2026-11-17。保持原完整场 SHA `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`、全部保存二 jet、同一 q4096 构造及 R636/R641 的精确标量。已有 819 调用的 Gram 批次不变。准备阶段只形成全818胞连续主曲率批次的固定计划，新几何调用为0；随后已按该计划唯一启动，见末节。

## 1. 完整消费与分界核对

已完整读入并验证：分量盒源 `459dc01e...`、规范化生成器 `582b22d6...`、有限节点 λ 三 jet 核 `e6ddb8c5...`，以及现有 G458 的 `fd35f720...` / G817 的 `12b4b170...` 两份完整报告和它们的三份 λ 证书。所有完整 SHA 均在计划与入口常量中。

同一数据的精确 binary 网格恰有 481 个旧标量五次胞、17 个解析转向胞、319 个 pulse 第一半段整胞，以及第 817 胞的一个内部分界。旧标量 knots、origin 和 cut 都已是场节点，不存在被跨过的未处理公式分界。唯一内部点准确为

`1152921504606846971/1152921504606846976 = 1 − 5/2^60`。

λ 的两个子片覆盖按有理端点逐项核对，先后相接无缝、无重叠；每一阶界在两个子片上取最大，成为整第 817 胞的统一参数盒。该 union 已用于既有 G817 报告。本批不把它舍入成 1，不修改任何 scalar 或节点数据。现有 d066/e6 核已经支持所有这些范围，无需边界公式修补。

## 2. 预先固定的全部调用

- 458 与 817 两份已刊 G 证书直接逐字复制并复用，三份相关 λ 证书同样复用，不重跑代表胞。
- 其余 816 胞各一次 e6 有限节点 λ 证书调用：固定 4096 构造节点、4096 标量求积面板。旧区保准确有理五次标量；新段保同精确积分标量与已付 Taylor 余项。
- 这 816 胞各一次原 582/459 G 曲率调用：角 Q4096、径向八等分。已有 817 保原 Q8192/八等分；458 保原 Q4096/八等分。
- 没有自适应重试、后见之明加密、改变 g/场/原 q4096 或改用失败 Pr 场。若 λ 失败，则该胞曲率依赖未付，明确记失败；其余预定胞仍执行一次。所有异常及可用预算落盘。

程序不改数学核、不改运算顺序、不加运行时缓存替换，直接调用三个冻结入口；因此无需重跑已付代表来验证新算术。入口在执行前要求与预先准备的完整计划逐字段一致。源/输入/计划变化会阻止完整接受，已完成和未访问范围分别报告。没有暗设一个主曲率接受阈值；完整输出是实际得到的最大上界，是否足够 reach 预算另行判断。

## 3. 连续覆盖的数学范围

复用 R643 的原证明：真实移动正交架中各分量是最大物理频率 640 的有限三角多项式。对每一径向 Bernstein 系数先付连续角二阶覆盖，再在闭径向子胞上取 Bernstein 凸包，包围 G 的真实六 jet。G、G_s、G_ss 分别由

`G=c+λ(F−c)`、`G_s=c_s+λ(F_s−c_s)+λ_s(F−c)`、
`G_ss=c_ss+λ(F_ss−c_ss)+2λ_s(F_s−c_s)+λ_ss(F−c)`

准确代入；λ 三 jet 是整个胞上的统一区间参数，没有把参数盒当常数函数再微分。有限节点核先平均 D/ρ、R/ρ、S/ρ 的径向多项式再取界，保原均值抵消。全部分量盒进入同一完整 Gram/形算子公式，正的 E 和行列式由原核检查。

对每个成功胞所得上界适用于该胞全部 s 和全部角度。若全部 818 胞成功，取最大即得同一开放前缀 G 的全连续主曲率界；R638 已付的 C² 角坐标微分同胚把该界传给相同像的规范化场。它不证明 reach、闭合、全曲面族或固定 g 求解精化。

## 4. 已实际完成的准备与资源估算

准备仅用 1.184259208 秒，RSS 181352 KiB；新 λ 调用和新曲率调用均为 0。5 份既有报告全验证通过，未支持的内部分界数为 0。

使用已刊 cell458 的 λ 2.171806173 秒和 G 曲率 8.065863061 秒作粗估，816 次组合约 8354 秒（2.32 小时）；为当前并发和胞间差异预留 2–4 小时。计划只有一个顺序 worker。RAM 预计 512–1024 MiB，属于源中数组规模估算而非已测批次峰值；运行会逐批记录实际 RSS。新增报告/计划约 20 MiB，均在研究仓库外。时间不是终止条件。

冻结入口 [parallel-model-pulse-curvature-fixed-full-batch.py](2026-11-17-parallel-model-pulse-curvature-fixed-full-batch.py)，17073 B，SHA256：

`eb2b4e816175e314f54d5e4159318ad2e8a69b7975907673c398ddb1af3cf92f`。

计划 `parallel-pulse-curvature-full-fixed-20261117.plan.json`，SHA256：

`df745a9b3c204aaea2f1fee568282be24a13b1db7245095a743b52690fbf6602`。

准备报告 `parallel-pulse-curvature-full-fixed-20261117.plan.preparation.json`，SHA256：

`a3b43aa75452fcfdbda136f0060b46070d86cb59710788c310bed3b99b514bce`。

在仓库根目录，令 T 为 `topics/visible-flex-larger-amplitude`、WORK 为仓库外当前 scratch；已执行下面不带 `--execute` 的准备命令：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  "$T/notes/2026-11-17-parallel-model-pulse-curvature-fixed-full-batch.py" \
  --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
  --raw-source "$T/notes/2026-11-17-parallel-root-pulse-curvature-component-box.py" \
  --normalized-source "$T/notes/2026-11-17-parallel-root-normalized-component-curvature.py" \
  --scaling-source "$T/notes/2026-11-17-parallel-model-arclength-lambda2-node-kernel.py" \
  --engine "$T/notes/2026-11-17-parallel-model-pulse-gram-representative-cells.py" \
  --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
  --scalar-oracle "$T/notes/2026-11-17-parallel-inward-integral-enclosure.py" \
  --existing-reports "$WORK" \
  --plan "$WORK/parallel-pulse-curvature-full-fixed-20261117.plan.json" \
  --outdir "$WORK/parallel-pulse-curvature-full-fixed-20261117"
```

后续唯一执行须在同一命令末加 `--execute`，消费这份已冻结计划；输出目录必须为空或尚不存在，不能悄悄重启覆盖。准备报告写出时尚未启动；随后已真实启动同一固定执行。

## 5. 已实际启动的唯一完整批次

固定源eb2b4e81、计划df745a9b及26e53输入不变，执行原CLI加 `--execute`，一个顺序worker。日志为仓库外 `parallel-pulse-curvature-full-fixed-20261117.log`，逐胞证书与progress/result位于同名目录；constructive_model为唯一终态读者。原819调用的全Gram批次继续，至本条时664/819无失败。本条不提前填全曲率上界，已付458/817不重复，所有失败/异常/未访问范围由固定批次完整保存。
