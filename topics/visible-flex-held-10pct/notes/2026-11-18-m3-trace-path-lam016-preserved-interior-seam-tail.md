# λ=.16：保留真接受内部状态，新接缝 H 原门接受

**状态：数值证据与真实执行身份；不是连续几何证书。**

针对 [原完整 prefix audit 已保存、接缝尾失败](2026-11-18-m3-trace-path-lam016-prefix-audited-seam-tail-failed.md) 的实际新 H，只改变原接受尾的 cut Dirichlet 编码，保留全部内部/深端状态和 cut 动量。随后唯一原 worker 在迭代 0 真实接受，残差为

$$
1.83393059818419\times10^{-9}<2\times10^{-9}.
$$

完整 208 个有限 Jacobian 元素和有限尾 audit 返回；最终全部状态与候选逐位相同。没有重复前缀内解、完整 prefix audit 或 mean-height 积分，也没有再做全 stage 残差定位。

## 实际输入变化与唯一初值

原节点 H 的真实接受尾是 `c807ab79…`；物理 quintic 端点 H 的原失败尾是 `69e2d545…`。两者的物理/离散配置和执行源相同，实际 H 仅分量 0、3 有末位差异。首幅值比为 `1.0000000000000002`；原接受状态与原接缝迭代 0 失败状态共有 **18106** 个标量不同，已在紧凑记录中保留这次只读比较的确切输入。

新初值复制整个真实接受 checkpoint，仅用原 JavaScript `H/rCut**4` 重新编码 cut 高度，同时将 `cutHeight` 明确设为真正的新 H。这一步的完整状态差集恰为：

| 位置 | 原值 | 新值 |
|---|---:|---:|
| node 0 / component 0 | −0.020629307799470645 | −0.02062930779947065 |
| node 0 / component 3 | $7.11797597259182\times10^{-8}$ | $7.117975972591824\times10^{-8}$ |

所有 node≥1 的内部/深端状态和 node 0 的 8 个动量逐位保留，`rawStates` 按原 `rawNode` 一致重取。候选仍标记为未接受。原重新加载验证给 ratio=1、零边界修补；不能省略这一步而继续让旧首幅值比缩放所有内部态。

## 本次独立源的范围

[新入口](../scripts/resume_m3/solve_preserved_interior_original_tail.py) 从已执行的 `5e12714…` seam 初值源作最小派生：将旧 λ=.02 的三个固定输入 SHA、某一个固定失败数值及四个固定变化索引，替换为调用者必须显式给出的三个 SHA、实际原 line-search 失败和实际重新编码差集。它仍只处理本例原 M8/spacing3/parts16 结构；没有声称任意模式数已经验证。

原物理配置/源相同、完整 $1153\times16$ 状态、全部内部态保持、原 JavaScript cut 编码、ready IO 映射、原 Newton/全残差/J208/audit 和严格 $2\times10^{-9}$ 门全部不改。`closed_geometry` 的只读逐字派生核对为 `5049b4`/exit 0；该核对没有执行任何新 flow 或求解。本次才首次实际运行新入口。

新源 SHA-256：`af65f13ceb394589e9578c535ca337ca80b86bcb3bf4291b509af966b785b614`。八处字面派生的完整 scratch manifest SHA 为 `fb41b2c9f313d9762e74d7e5da896c8037325812b07329865b30328ada156dab`；旧已执行源保持原字节。

## 原真实接受与接续

session **4232**，启动块 `ec2fb1`，终态块 `67f901`；observer 于 **2026-11-18 04:34:28 UTC** 记录 child=0，原 worker=0。原 history 只有 iteration 0 一行，没有额外 Newton 修正、比例扫描或自动重试。

真实新 H 接受尾：

`m3_work/trace-path-lam016-seam-preserved-v1/seed_tail_0001.json.gz`

SHA-256：`1470c291844bbc89cc9afe17d1a24a07aacad4728cf6fb92f8afb2da87961c57`。

完整旧/新 H、初值差集、实际请求、源及文件 SHA、唯一命令和资源终态见 [紧凑执行记录](../scripts/resume_m3/trace_path_lam016_seam_preserved_execution.json)。它已经交给只补缺失 seam 的薄入口；已保存的物理 quintic、prefix metric 和 mean-height 计算不重复。此尾接受结论不代替后续完整曲面、固定 g 收敛或 10% 持握门。
