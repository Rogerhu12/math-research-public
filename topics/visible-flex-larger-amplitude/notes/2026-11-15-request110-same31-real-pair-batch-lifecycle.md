# Request110：同一 Actions 任务内的真实 31-query 连续批次

类别：运行编排与原结果读出。actual107 已完成，最近拒绝仍在已建模 LEFT464，故本请求保持 same31，最多运行 8 个原子模型/FD 对。这里只完成源码和唯一工作流/请求草稿，不执行科学、不派发，不预填未来 110 run、输出哈希或成功结论。

## 1. 使用的源与边界

新入口为 `geometry_20261115_same31_temporary_batches.py`，25980 B，SHA `a1ba1cd895892906f594cd65313d03f11230edb940c8b0c77977dad92591552f`，仅 Python 标准库。它复用冻结的第 107 轮临时编排器的输入恢复、字节读取、子进程调用和紧凑摘要函数：

- `geometry_20261115_actual98_same31_temporary_resume.py`：`2b4e9f2132263d166d7d4ee298725f55e547427cb1c25c335edf366b4aa784ba`。
- `public-same31-resume-request.json`：`f508c1e5e5396b5f9a9a927703557e89cd24542d16ddd4a74774aa780121c545`。该文件保存原 70 项源 pin、1 项参数 pin、actual98 artifact tuple 和每个原子模型的全部参数。

新入口不调用 107 的 `main()`，因为其一次调用结束即销毁整个临时树；也不猴补其中任何函数。新入口自己管理跨批的两件真实父文件。数学仍由原 `geometry_20261114_thirty_one_query_collocation_observer_warm.py` 和 `geometry_20261114_thirty_one_query_condensed_response.py` 在独立子进程中运行。31-query 定义、A/B/H、固定 C 支持及其完整 outside offset、原方向与选择方法均未修改。

第 107 轮源码已经发布并实际执行完成；本稿不修改它，也不为保留它已清理的输出改写原清理责任。

## 1.1 actual107 直接依据

实际 run `43683739473`，source `6df3e818bf5acb8e144c1839fb57647c8b3587f4`，job `132719696865`，科学 warm 与 FD 均退出 0。完整紧凑摘要 35131 B（含 LF），SHA `42dd12dfab65e25c8e8c7153fb514852bd5832be14f66c5e6fa8ac393f24c491`；下列数字只抄原保存结果，没有本地数学重算。

本轮 fresh W 下 merit 从 `43.363003729098274` 降至 `43.33594286031892`，原接受 α=`0.125`，原实际下降 `0.02706086877935121`，预测下降 `0.026913362440847455`，比值 `1.0054807844552296`。节点、中点、两套各 698 点 RMS 全通过；FD 主误差 `8.81884772255149e-10`。结果依旧是未接受的 warm，而非完整 BVP。

最近拒绝 α=`0.25` 时节点/中点合法，merit=`43.33703438037944`、实际下降 `0.025969348718831498`、比值 `0.4901184851120571`；全 RMS 只剩 LEFT464 失域，β²=`-0.2683514415128212`、φ=`0.16566992509164924`、index54、4 个负角。LEFT464 已是原 31 查询的第 0 项，因此没有按最近失败新增查询的依据。更远 α=`0.5` 的 LEFT464/472/483 失败及 α=`1` 的 MID471/483/487 失败不会被自动用于本次扩点；整步未执行实际 merit/RMS。

原 QP 选 R270 候选，63488 个线性 slack 全正，最小值 `1.053046538856961e-12`；原 stationarity L2=`0.003038625816318205`，原浮点 gap=`3.000998560764856e-9`。这些不是验证包围或非线性接受保证。接受后原 physical col max=`0.007107481419519517`，BC max=`6.857449986338445e-9`；最大 col 仍在 interval461，不能由 QP 后验直接保证它快速收敛。禁止与前轮不同 W 下 merit 直接相减。

## 2. 初始场与“再现”的确切含义

初始场只能是原已存在 actual98 artifact 中的真实 warm/status 双件：run `43677587785`，source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`，artifact `14147700690`，完整 ZIP `809042943` B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。完整 ZIP 校验后只读两件原成员，CRC/size/SHA 保持；不重新序列化，科学开始前删除 ZIP。

初始 warm：`b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`；原 status：`b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。四件历史数学输入和 78 件源码恢复亦直接复用 107 的冻结合同。

这将产生**新 run 的实际重算轨迹**。如果 107 已清理新 warm，110 不能凭其哈希还原场，不能把 98 输入或本次重算输出称为原 107 文件。请求可以附上实际 107 已保存的小型参考身份；比较只作读出，不决定该新轨迹是否可继续。

比较分成三种不同责任：

1. 原 gzip warm 文件 SHA 与原 status 文件 SHA。只有完整字节相等才报告相等；不人为复刻 gzip 头、路径、时间、运行身份或来源对象。
2. 原 warm 解析后的 `mesh`、`states`、`rhs`、`field_representation`、`complete_scalar_profile` 五个字段的规范 JSON SHA。输出分别给每字段和整个明确子集的 SHA。这只是字段值选择与标准库编码，不执行数组运算或方程。
3. 若旧摘要没有同一字段子集的哈希，明确写“不可比较”；不能由原文件 SHA 不同反推物理场不同，也不能用若干标量相近冒完整物理场相等。

上述字段哈希不是 NumPy 原生数组字节哈希，也不是完整 warm 文档身份。旧文件 SHA 或字段 SHA 不相等不构成新的科学拒绝门。本次真实结果始终保留自己的 run、输入和输出身份。

## 3. 每批的原调用与继续条件

每批启动一个新 Python 子进程，运行原 warm 入口，明确 `--iterations 1`。原每批参数全部来自冻结 107 recipe：λ270、LSMR200、投影200、17 个真实回溯档、angles4096、jac-workers2、原总预算1200 s、condensed600 s、trial reserve90 s、recovery reserve30 s、working512、dual200、原 root 临时输出选项。

下一批的继续条件只有原调用及其既存身份责任：

- 原 warm 子进程退出 0，原 schema 正确，`optimization_progress=true`、`accepted_warm_steps=1`；新文件确是本批 `warm-001.json.gz`，其 SHA 与本批原 status 相符。完整 warm 和 status 的原 producer 对应关系保持。
- 在**该新文件**上运行原 FD 子进程。原报告实际存在，退出 0，原 `implementation_check_passed=true`，`prepared_sha256` 对应该新 warm，且保留原“当前 warm 的完整 FD 已重算”字段。
- 两件原父文件移交后字节 SHA 不变。

没有新 warm 就不运行 FD。原 FD 失败、原 warm 不接受、原调用异常或文件交接故障即停止；不把旧 FD 成功改标签，不把旧 warm 当新结果，不自动重试同模型，不调 λ、查询或预算。已有 source/schema、pair 和 FD 字段的核对是既存接口责任，没有增加阈值。

每个下一批的 `--resume` 与 `--parent-status` 指向上一批实际生成的两个原文件；`--expected-resume-sha`、`--expected-parent-status-sha` 用同批真实文件 SHA。原 own-schema 读取和原 producer 核对继续执行；不删减或重写 `resume_producer`。每个新子进程重新 setup、evaluate、冻结当前 W、构造一次原完整 J；没有跨批复用旧 J、旧方向、旧 merit 或旧 FD。

该链仍是未接受的 warm 优化，不运行真实当前非零 H 的 native/fullDN，不宣称完整 BVP、闭面或 held 目标成立。

## 4. 两件父文件的生命周期

所有编排拥有的工作数据放入 `RUNNER_TEMP/visible-same31-110-*`。

每批顺序为：

1. 用当前真实父双件调用原 warm，再按上述条件调用原 FD。
2. 在原两个子进程退出后读取原 model/status/QP/FD，保留全部原 trial 决策、selected-query 最小值/负角数、坏中点和已执行 RMS 的实际坏点标量及五件主输出 SHA。
3. 若可继续，将新 warm/status 用同一文件系统的 `os.replace` 移到独立 carrier；不改任一 JSON 或 gzip 字节。确认移动前后两个文件身份相同。
4. 删除该批剩余输出和日志；删除上一个已消费 carrier。下一批仅保留新双件以及公共原输入/源码。
5. 打印该批紧凑摘要后进入下一批。

失败批也先读取其已经存在的原报告，明确原 phase、退出码与未执行阶段；不制造缺失报告。最后退出 `TemporaryDirectory`，连最后一对新父文件也清理，只保日志中的小摘要与输出哈希。异常出口不谎称已完成清理。

本脚本不上传 artifact/Release，不写 Git 数据，不清理别的任务目录。历史 `git show` 的按需 blob 可能存在于本次 Actions checkout 的临时 `.git` 对象缓存，直到 runner 回收；本脚本只删除自己拥有的临时树，不把 Git 缓存也声称为已擦除。工作流保留 `git config --global merge.stat false`，防规则监控 pull 的 diffstat 读取已删除的大历史数据。

## 5. 有界连续执行与摘要

新 request 明确 `maximum_batches=8` 和 `chain_budget_seconds=10500`（175 分钟）。这是外循环资源预算，不是原数学接受标准。编排器在两批之间检查时间，不改写已开始的原子模型或原 FD 的内部预算。工作流科学步骤外层上限也是 175 分钟，整个 job 为 185 分钟以容纳安装、规则准备和清理；外层到时可能中断仍活跃的调用，此时不能声称该批完成。job 的额外 10 分钟不是额外科学预算。

只有显式批次数或批间时间预算到达，才标记对应的正常编排停止。原模型自身无接受、原 FD 失败或其他异常保留其实际原因和失败退出，不冒“只因批次预算”。摘要和末表不跨不同 W 的模型直接相减 merit。

每批使用一份不超过 90000 B 的 `BEGIN_SAME31_BATCH_SCALAR_SUMMARY`，这是不同实际模型的独立科学读出，不是拆分大原件。17 档及 31 个 query 用列名、并行数值列表和坏点行数组避免重复来源树。超限只打印明确不完整的更小选择及原完整摘要 SHA/大小；仍超限就给有界错误摘要。输出尺寸不是候选接受门，也不因少打印字段伪称完整。

末 `same31_batch_chain_end` 给批次列名/行数组、每个输入/输出双 SHA、字段子集 SHA、原接受 α、各自 W 下的原 merit、两个子进程退出码和对应摘要 SHA。大原矩阵、因子和数组没有另作完整字节审计，不扩大已付科学范围。

## 6. 请求接口与实际运行

新 request 合同：

```json
{
  "request": 110,
  "schema": "same31-real-pair-batch-continuation-request-v1",
  "repository": "Rogerhu12/math-research-public",
  "source_sha256": "a1ba1cd895892906f594cd65313d03f11230edb940c8b0c77977dad92591552f",
  "base_request_sha256": "f508c1e5e5396b5f9a9a927703557e89cd24542d16ddd4a74774aa780121c545",
  "maximum_batches": 8,
  "chain_budget_seconds": 10500,
  "reference_first_batch": {
    "run_id": 43683739473,
    "source_commit": "6df3e818bf5acb8e144c1839fb57647c8b3587f4",
    "warm_sha256": "6d2e5b1c936f874a678a94cdfe44dfc25c45ad18c8b4c01274fbc76e7cf801c1",
    "status_sha256": "714347e07a160f56575fc76855fc890b53715923c2920a63a0d268f143a8850b",
    "field_identity": null
  }
}
```

完整实际请求为同目录 `public-same31-batch-request.json`，沿唯一 `.github/workflows/visible-larger-public-same31-batches.yml` push 路由。上例列关键字段；完整文件另含实际依据、已读规则、初始98身份和清理说明，没有未来 run 或输出身份。原 70 项源/参数由 f508 recipe 原文继续绑定，另加一个新编排器源，不丢弃原依赖合同。

`reference_first_batch` 使用 actual107 真实文件 SHA；107 没有输出同合同字段子集哈希且原文件已清理，所以本次 `field_identity=null`，物理字段子集比较必须明确不可用。仍可只读比较完整记录 SHA，不把不同 gzip/status SHA 当物理场不同的证明；也不把逐字再现当额外门。

CLI：

```bash
python -u computations/geometry_20261115_same31_temporary_batches.py \
  --repo-root "$GITHUB_WORKSPACE" \
  --request computations/public-same31-batch-request.json
```

运行依赖仍为原 Python3.12.14、NumPy2.3.5、SciPy1.17.0、单线程环境；只是子进程需要后二者，编排器本身不导入科学包。沿原 3b8 规则监控，固定 science checkout，基于当前真实已读两个 README 的 baseline；不改原 45 分钟同步和新规中止行为。根负责最终唯一 workflow/request 和 Git 发布。

## 7. 当前完成范围

只完成源文本、Python AST、工作流 shell/inline-Python 和引用接口的静态核；没有在本地导入 producer、数组库、求解器或运行科学 fixture。107 的原 source/request/workflow 不变。实际107已提供保持same31的直接依据，110的资源预算已明确；主控负责唯一发布。本设计不预言下一批接受或步长。
