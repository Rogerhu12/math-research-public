# Run 06 actual 42: 完整 current-PCG 方向已返回，纯报告读取失败

## 1. 实际返回范围与原证据

本条记录公开 Actions run **45904402595/1** 的实际第 **42** 步。该步的单次准入 wrapper 已完整尝试两个原 child：科学 launcher 返回 **0**，原纯 reader 返回 **1**。wrapper 因第二个 child 失败而整体返回 **1**。因此这是“完整科学结果已返回、纯归因尚未返回”，不能把 wrapper 的失败标签改写成科学场失败。

实际 step id 为 `complete-current-PCG-from-actual40-after41-independent-pair-20261127-run06`；公开索引的更新时刻为 **2026-11-27 03:16:04 UTC**。该时刻记录的 source commit 为 `a6d1b337b3622b8aa65790a96401f0be836a5662`。科学与纯读取实际都使用这个同 job 的原始完整输入和源工作树；后续 API 的 job 仍在运行，只说明控制器可能继续其他步骤，不否定此步已经返回。

本条只读取已公开有界卷的完整原字节；没有从连接器读取 33 MB 科学 report、原 NPZ、行矩阵或大日志，也没有在本地执行 F、J、转置、root、QP 或数值试验。

原 compact 卷：

- 路径：`notes/2026-11-26-public-actions-45904402595-1-part-004.md`。
- 实际包含第 39–42 步；**42,483 bytes**。
- Git blob：`e67e7aa9d362e897811e10733f6e0ae095b69b27`。
- SHA256：`8488ba556960a6c626e28bea9f7d809b662238c964db9c53486d20de6cb30cf3`。
- 本次取回时固定公开 head：`37c083b9539cea50cb76b752e940355eba63c1da`。
- 索引当时的 Git blob：`1f9aabd346788fe12a6dca58efe1c6bd9bbecfef`。

以下数值全部逐项摘自实际 compact，不是待执行参数的预测；本条没有据此填写尚缺的方向、QP 或预条件器归因。

## 2. 完整源、实际父与同单位阻尼

科学 report 的实际 schema 是 `complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1`，完整科学 driver 为 `fullclosed_so3_cached_current_pcg_soc.py`，SHA256：

`a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743`

本次 pair 完整源为 `run_current_pcg_from_interior_complete_pair.py`：

`b527b42440ebb792830c288cb28567b1c7c1cd7eba921dfc16e18ca3d76a0b24`

原纯 reader 为 `read_so3_cached_current_pcg_soc_report.py`：

`0d659ab94bff7fe12337cc8f1eb18263ae1623f8fb8bcbb40108e7e03ad3856f`

这次科学点从 **actual 40 的完整变量**继续，actual 41 的完整报告作为额外永久地点输入。它没有以 actual 41 的末点代替 actual 40，也没有将原四次 history 重演标成已完成。

| 身份 | 实际 SHA256 |
|---|---|
| 原固定参考 bundle | `d466ef7605281dcb951f821fe2de08953c53eb3a021a08a436f9529c6af4de04` |
| actual 40 restart checkpoint | `75f0fd9fab2b2c542fdaf3da6fef970332e252d6da364e35a19219420c46bdd3` |
| actual 40 restart report | `e62c283ee56a36e82e626762f002c484a5bd5209ad576813983784a64d6f3d84` |
| actual 40 完整 driver | `0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6` |
| 当前完整模型 | `b28b7f76ea615cb317b4ca98f0d4b75a67c1e2792abc47e6f86c91266773d086` |
| 固定标量目标 | `364e73ce2ed258b923c0dff10a1c4dfdc846e143930d4c56b55944d0d2c18853` |
| 全坐标范数 | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |
| 本次初点 NPZ | `75f0fd9fab2b2c542fdaf3da6fef970332e252d6da364e35a19219420c46bdd3` |
| 本次末点 NPZ | `2b37a650e513ba9860d736b1947f209f34925677ac6f7bb54c6a591d4310f9ca` |

初点 NPZ 的实际完整 SHA 等于实际 40 restart NPZ；该等号针对原始 NPZ 字节，不是从 Phi 接近或相同参数推断。实际模型保留 **1333370 个自由变量**以及逻辑完整正权指标中的 **45324288 行**；quarter 实际算子行数及每次操作的实调用另由完整 report/reader 提供，不能把逻辑完整行数当作实际一次输出长度。

pair 从 actual 40 的真实完成 report 读取了阻尼，并核验模型、目标、范数和全部原输入。两项实际值均为：

- metric damping：`0.01`，binary64 字 `0x1.47ae147ae147bp-7`；
- restoration damping：`0.01`，binary64 字 `0x1.47ae147ae147bp-7`。

实际 pair 明确 `bound_from_actual_report=true`、`other_numeric_arguments_changed=false`、`hard_limit_extended=false`。这些是原单位下真实读取的两个输入，不是把另一种范数的旧数值阻尼迁移过来。

原完整参数文件：

`computations/resume-20261127-run06-current-PCG-from-actual40-after41-parameters.json`

为 **18,379 bytes**，SHA256 `6d3a9ea5cf4634bee21f7984f28f0e53e9b6c355f336927d3752cb62a0b322b0`，Git blob `dae2794cf4fb7890d8f909376725217a9e2e2543`；独立准入公布于 `1a3aced8a439459cb5dcbffc7a4f7bf01095fbaf`。该文件保存完整两 child 对象与全部 summary，不依赖本条缩写恢复。

## 3. 同一次科学报告的有限观测读数

| 字段 | 实际初值 | 实际末值 |
|---|---:|---:|
| 本 report 的 centered Phi | 0.00683704255256235 | 0.006746772540165999 |
| 原有限观测最大 metric/Gram 残差 | 0.03685242646034892 | 0.03671387499669269 |
| 真实有限筛几何最大 g | -5.350157428196667e-9 | -9.212618445886278e-10 |

这里的“最大残差”保持原字段在有限观测域的意义，不把它改称整面连续 operator-norm 上界。Phi 比较只使用本次 report 自己的 initial 与 final；没有从旧报告的浮点初值作跨 report 相减。

实际末态报告：

- `complete=true`；
- `final_geometry_feasible=true`；
- `all_permanent=true`；
- metric 完整记录数 **1**，restoration 完整记录数 **0**；
- `final_mu=0.01`，`restoration_mu=0.01`；
- 末态曲率永久地点数 **2891**，半径永久地点数 **2876**；
- 停止原因 `declared_metric_direction_budget`。

这些地点数是实际报告的两个类别计数，不是集合相同、保护标签相同或连续覆盖的证明。下一次同问题方向还须真正消费这个完整 report 的全部实际地点及 typed 来源责任。原有其他并行或待重建 history 并未被本分支免除。

上述 `metric_count=1` 在 compact 中是完整 metric 方向记录数。本条暂不将它单独当作原 ray/SOC 接受分类，也不填尚未由纯读取返回的 alpha、真实试点次数、最后 active face、Pg/tolerance、内部 iteration 状态、SOC rounds 或实际 J/J* 次数。

## 4. 当前八列算法与尚缺的实际归因

完整科学源使用已刊当前八列 SPD preparation 和原 v5 face PCG；Phase I 保原 v3，全部原 C、全变量、原范数、原目标及非线性验收保持。当前完整行 helper 的实际 SHA 为

`e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021`

原完整半空间投影源为

`a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e`

本次预算保留 1 个 metric 方向、每方向最多 64 次 QP、最多 4 个 restoration 方向各 64 次、15 次 ray budget、最多 8 轮 same-parent SOC、向内系数 .125、tau 0、投影可行读数容限 2e-11。它们是明确参数，不是本条已经拿到的实际使用次数。

由于原纯 reader 失败，当前 compact **没有**返回下列关键字段：

1. 八列 preparation 是否全部完成、实际 A/A* 调用数与耗时、是否在开始 QP 前显式回到 v3；
2. 原 v5 是否实际启用、last-face advances、Pg/tolerance、内部可靠更新和停止状态；
3. 真实 ray alpha、最近可行 fallback 与拒绝 anchor、SOC 修正是否被接受；
4. 每个真实候选的失败家族、地点、模型量与完整再筛结果。

因此目前不能把“选择了该完整入口”写成“已经证明八列生效或提速”，也不能把整个总耗时当作 PCG 本身的耗时。这些缺项应由同一真实 report 的纯读取补齐，不重跑科学方向补造缺失元数据。

## 5. 实际成本与结果文件

| 成本或缓存字段 | 实际值 |
|---|---:|
| 控制器记录的整 pair seconds | 2835.597657069 |
| pair 自己的 total seconds | 2832.399513487 |
| 科学 report total seconds | 2826.397416187001 |
| 科学 setup seconds | 403.0011950349999 |
| 缓存采用 seconds | 9.844882788998802 |
| 完整复用 cache entries | 2215 |
| 缺失旧 query entries | 19 |
| 本次新生成 cache entries | 2 |
| 科学 peak RSS（KiB） | 3959852 |

这些计时层级不同，原样并列，不强行作相互可加的阶段分解。cache adoption/snapshot 并不是新场、指标、曲率或连续证明。实际完整 manifest SHA 为 `816fe94bfb2b617c55b05b2581dbc91e615f2adfeb878f739bf3fd696f3332f0`，`cache_completed=true`。

完整实际输出清单如下；大 raw 均保留 runner，不搬进 Git 或此 note：

- `so3-closed-actual-profile-current-eight-column-PCG-SOC-from-interior-run06-first/report.json`：33240675 bytes，SHA256 `c5cee5af8641bf93b25367aae915eb5871c85687dc58f0fdba6788e9768a63b2`。
- `so3-closed-actual-profile-current-eight-column-PCG-SOC-from-interior-run06-first-command.json`：17813 bytes，SHA256 `0e83dc0b4dbb6e0889e395414391bf2973736e7a8fc8f23fcc5fa939ed62ae59`。
- `so3-closed-actual-profile-current-eight-column-PCG-SOC-from-interior-run06-first/initial-new-field.npz`：10720258 bytes，SHA256 `75f0fd9fab2b2c542fdaf3da6fef970332e252d6da364e35a19219420c46bdd3`。
- `so3-closed-actual-profile-current-eight-column-PCG-SOC-from-interior-run06-first/final.npz`：10720258 bytes，SHA256 `2b37a650e513ba9860d736b1947f209f34925677ac6f7bb54c6a591d4310f9ca`。
- `postprocess/so3-current-eight-column-PCG-SOC-from-interior-run06-first-pair-status.json`：22345 bytes，SHA256 `ae5b8c2fa317d81d763b3f7a8851d2b3c9ce3c715aadb22d2210f578249dabbc`。

科学 report 的 33,240,675 bytes 与最终 NPZ 的 10,720,258 bytes 是实际输出尺寸，不是已公刊 raw。原纯输出 `postprocess/so3-current-eight-column-PCG-SOC-from-interior-run06-first-summary.json` 未产生；controller 的 summary error 是该文件 ENOENT。缺少纯输出不能反推原科学报告未完成。

## 6. 原 pure 失败与事后诊断必须分开

实际 b527 wrapper 的 `run_pair` 逐一调用原两个 child，并用它们各自真实 return code 更新 `scientific_success` 和 `pure_success`。本次原记录是：

```json
{
  "scientific_child": {
    "state": "returned",
    "returncode": 0
  },
  "pure_child": {
    "state": "returned",
    "returncode": 1
  },
  "scientific_success": true,
  "pure_success": false,
  "both_children_returned": true,
  "complete": true
}
```

原 b527 调用 `subprocess.run(command, check=False)`，没有单独重定向 child 日志文件；两者继承控制器捕获的组合 stdout/stderr。原 3cb1 followup 控制器把该组合输出保存在实际 `followup-journal.json` 的对应 record 所指 `log` 路径；不能凭想象填写 `children[1].stderr`。

控制器在实际 step 返回后，另外明确清理了 **1** 项新生 row cache，共 **3,232,088,880 bytes**。其完整删除记录在 runner 的 journal/status，公开 compact 的 canonical SHA 为

`eb688ad9bbc82f25836cd08d973650fdc3fa60fe2780894c533da0355356f58b`。

这一清理不会把已经返回的科学 child 0 改为失败；但它改变事后纯读取的文件环境。因此再次执行原 `--verify-cache-files` 取得的异常，不能自动当作原 pure child 1 的原因。

独立准备的纯诊断必须首先凭唯一实际 step、source commit、b527/source SHA、科学 report、final 和 pair SHA 找到原始 log，size-first 记录其完整字节身份并仅摘取有界尾；随后才单独尝试 unchanged 0d65 的两原 verification flags。两种证据须明确保留各自时间范围。当前本条不预填原异常文本、是否由 source/schema/cache/字段接口造成，也不把静态候选称作已确认的实际原因。

## 7. 完整科学与纯 child argv

以下为原不可变参数文件里的完整 argv。两个 damping placeholder 的唯一实际替换已由第 2 节的真实 pair 记录绑定为 .01；其余参数保持原字面值。原科学 driver 没有因 pure 失败被替换。

### 科学 child

```json
[
  "--repo",
  "{repo}",
  "--parent-bundle",
  "{work}/deep-fixed-scalar-amplitude-first/final.npz",
  "--parent-report",
  "{work}/deep-fixed-scalar-amplitude-first/report.json",
  "--carrier",
  "{work}/deep-fixed-scalar-prepare-first/observations.npz",
  "--node-report",
  "{work}/deep-fixed-scalar-prepare-first/nodes.json",
  "--scalar-input",
  "{work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
  "--eta-start-node",
  "885",
  "--angles",
  "2048",
  "--stage-block",
  "64",
  "--angle-block",
  "8",
  "--integration-order",
  "8",
  "--norm-kind",
  "jet-sum",
  "--radial-norm-length",
  ".05",
  "--angular-transition",
  "24",
  "--torch-threads",
  "4",
  "--damping",
  "{actual_parent_final_damping}",
  "--directions",
  "1",
  "--maxiter",
  "64",
  "--restoration-directions",
  "4",
  "--restoration-damping",
  "{actual_parent_final_restoration_damping}",
  "--restoration-maxiter",
  "64",
  "--line-trials",
  "15",
  "--active-rows",
  "192",
  "--qp-atol",
  "0",
  "--qp-rtol",
  "1e-6",
  "--reach-ratio",
  ".03",
  "--reach-safety-factor",
  ".992",
  "--active-band",
  ".025",
  "--marked-diameter-budget",
  "4.2",
  "--witness-lower-budget",
  ".9",
  "--amplitude-height-floor",
  "1.01",
  "--spectral-p",
  "4",
  "--spectral-epsilon",
  ".001",
  "--spectral-scale",
  ".05",
  "--legacy-fraction",
  ".5",
  "--target",
  "1e-9",
  "--scalar-admission-seconds",
  "300",
  "--scalar-integral-tolerance",
  "1e-18",
  "--scalar-tail-cutoff",
  "1/8",
  "--outdir",
  "{work}/so3-closed-actual-profile-current-eight-column-PCG-SOC-from-interior-run06-first",
  "--restart-checkpoint",
  "{work}/so3-closed-actual-profile-interior-restore-first/final.npz",
  "--restart-report",
  "{work}/so3-closed-actual-profile-interior-restore-first/report.json",
  "--restoration-interior-margin",
  "1e-8",
  "--reference-cache",
  "{work}/so3-closed-actual-profile-interior-restore-first/frozen-parent-meridian-cache",
  "--reference-cache-report",
  "{work}/so3-closed-actual-profile-interior-restore-first/report.json",
  "--soc-rounds",
  "8",
  "--soc-tau",
  "0",
  "--soc-inward-fraction",
  ".125",
  "--soc-feasibility-tolerance",
  "2e-11",
  "--manifest",
  "{work}/deep-fixed-scalar-prepare-first/locations.json",
  "--manifest",
  "{work}/so3-closed-actual-profile-first/report.json",
  "--manifest",
  "{work}/so3-closed-actual-profile-interior-restore-first/report.json",
  "--manifest",
  "{work}/so3-closed-actual-profile-cached-backtracked-SOC-v2-first/report.json"
]
```

### 原纯 reader child

```json
[
  "--repo",
  "{repo}",
  "--report",
  "{work}/so3-closed-actual-profile-current-eight-column-PCG-SOC-from-interior-run06-first/report.json",
  "--output",
  "{work}/postprocess/so3-current-eight-column-PCG-SOC-from-interior-run06-first-summary.json",
  "--verify-final-bundle",
  "--verify-cache-files"
]
```

这次结果仍是固定离散测度、完整有限筛和声明方向预算下的实际返回。它没有给出整域误差认证、连续嵌入证明、目标精度达成、全题完成或已驻点的结论。

## 8. 原日志与事后独立读回的完整准入

本次将完整源 [diagnose_current_so3_pcg_reader_v2.py](../scripts/resume_20261126/diagnose_current_so3_pcg_reader_v2.py) 和 [完整参数](../computations/run06-actual42-original-pure-log-and-post-cleanup-ready.json) 插入仍活的 run06 队列。原六个队列对象完整逐字保留，没有删除待返科学方向，也没有改写科学 a0e 或原 pure 0d65。

新诊断源为 15,271 字节/SHA256 `28b100b7c0c7c984a1b4ac68e5d0615b12fb8f90a2ca3bcb7d7273ff655e6a78`；完整 ready 为 6,770 字节/SHA256 `72930b563d52d3c1c887fe477021dac9eaf14ab57c6e5df16435b79a86632202`。原始报告/final/pair 的完整实际SHA与原source pins均写入源码和全argv。

先查唯一实际journal record并核原返回身份，再stat/完整SHA/至多64000字节原组合log尾。若实际pure start与return事件都在所读范围，只截二者闭区间，排除后续pair日志；公开最多该区间末7000字符。未取得完整事件或原log缺失均显式未归因。随后单独重新调用原0d65，保原两verify flags，注明这是事后cleanup环境；新异常不能自动替代原异常原因。

完整源码已读和逐字摘要核对，环境失联期间没有宣称Python AST/compile或本机科学执行通过。新步还未返回时，不预填异常、归因或额外数值。全部大输入/完整日志仍仅runner；继续处理真实结果，不以诊断或阶段收尾。
