# 新 restart8000 入口：冻结版本、实际小检查与执行说明

日期：2026-11-10；会话：Astra-visible-flex-78718bd0。
状态：**新入口已纯准备，完整独审进行中；尚未启动新主 solver。**
设计见 `2026-11-10-78718-numerical-restart8000-design.md`。
run02 仍是 root 实际观察 exit2 的失败，所有旧源/旧门/旧输出保留。

## 1. 精确改动及来源

原 97 项 reference 由未改动的原 h.validate_inputs 验证；冻结 run02 launch
由未改动的原 direct-CSC validate_inputs 验证（141 项 launch 绑定）。
run02 真实 guard 的 152 项运行闭包也全部验证并继承，包括上次确实补齐的 Node 动态依赖。
新入口另外绑定失败 CP、全部四件 PP、实际 audited tail_0003、root 非零观察和只读初猜 RMS 报告。

原主 coupled main、actual-tail outer、物理 RHS/BC/Jacobian、W14、source snapshot、
release-LU Newton、CSC foundation/selector 都保持原字节与路径。
新声明的 argv 仅变输出/配置 I/O、`--restart` 失败 CP、`--max-nodes 8000`；
新尾 config 的 initialCheckpoint 为 run02 自有最后 audited 包，非 I/O 参数逐字同祖先。
所有物理 g、profile/chart/port、时间范围、M14/N512、2e−9 与两种 BC 容差不变。

新 driver/auditor 是明确另名文本派生，并非修改旧 module 的常量或 monkeypatch 旧 gate。
完整 27,907 B unified diff：`2026-11-10-78718-numerical-restart8000-source-diff-01.txt`；
生成账本：`2026-11-10-78718-numerical-restart8000-derivation-01.json`。
生成器实际 `131a8e` 自然 exit0，只解析/编译源文本，0数学调用。
原 driver SHA 为 b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24；
原 auditor SHA 为 b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0。

新来源完整库存：`2026-11-10-78718-numerical-restart8000-frozen-sources-01.json`，
3034 B，SHA f1e2bd219df49f8f9b2e2645b4d84ddca02e569153f9c883544d45ff851232d3。
下表文件均在本题 scripts。

| 文件 | SHA256 |
|---|---|
| 78718-canonical-runtime-code-v1.py | 797eb77b7d8c85087659a30a5bfbfc8b7093d434a9246a9071bd3b59ece82d28 |
| 78718-check-canonical-runtime-code-v1.py | f869c3e17f5ff58577fb43967dc3f7df825144a9a9650e0ca7c5bb4ff6b95762 |
| 78718-prefix-restart8000-inputs-v1.py | 8730f041dd471c8b37c915589ed3be9cc32049f6f2e34e43b05df481811d0dd6 |
| 78718-prefix-spectral-restart8000-v1.py | 200792dbe56a84c2cf1b3954f3a4c73a060bab8579029612d16ffe2f162c9b30 |
| 78718-prefix-prepare-restart8000-v1.py | dded46af332d471e7e6e12535295fcfb901ffc312689fdd748b6845f149b08a5 |
| 78718-prefix-audit-restart8000-v1.py | cd090888e4552317bce183c3b5788710ced9e17eea965b9489252e96d2f3496f |
| 78718-check-restart8000-runtime-v1.py | 57b49ef7d7ab4531c0cfed567a3cc3d85b5167773425b1fb9c1e3addeeadfdd6 |
| 78718-build-restart8000-entry-v1.py | 692dbb88beb3905af9ef30de8601be898811e747353f3e7cc03faaf23dce1d6a |

纯 resource guard 准备器是第九件库存文件；原 6 GiB wrapper SHA
8260d9e9ac76f4816b5c40aafd3c07ec841388ea9b88316556e56f60c85a0ccc，
原 disk guard SHA cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd。
二者不改变数学参数，DATA 上限按每进程计算，不是总 RSS 保证。

## 2. 新 code 身份的完整范围与实际检查

旧 raw marshal 记录逐字保留在明确的 `raw` envelope；新字段在运行时从实际 live
CodeType 捕获，类型化地编码 19 个公开 code 数据字段及递归常量，保留 float 原位字节。
出口从绑定源码、同 filename、dont_inherit、optimize0 重编译并比较规范化摘要。
这不主张 marshal v0 一般规范，也不修改旧 marshal gate 或把旧失败改成功。

原 selector 对原 exports、globals/defaults、闭包别名、源码、原数学 callbacks、
原工厂与实际15矩阵小检查的 provenance 对应、Newton STATS 别名的门全部继续执行。
新 canonical 覆盖原闭存编译检查的**全部10函数**：四个原 SciPy exports、三个 foundation
storage helpers、两个实际 selected closures、选定的 release-LU Newton。
每次 BVP 前后采集与验证，恢复前后再验证；原 raw 恢复记录仍保留。

实际执行：

- canonical checker：作者 `6ba2ec/session53940 → 2bd5ed` exit0；root 独立实际
  `c5e6d2/session86276 → fbfe98` exit0。4 个实际 SciPy live/source 对应、24 个改变
  拒绝、6 个 ±0/NaN 位模式检查；0数学 callback/矩阵/factory/solver。
  root 报告 `numerical-canonical-code-root-check-01.json` 为6264 B，
  SHA 56f0ff2c6bc29f799ca724ca04f5b3305dc733b70e721808378cfdb49c4a51cf。
  root 观察 `numerical-canonical-code-root-observed-01.json` 为1707 B，
  SHA 164bdb08c46d7d4e709fc3248a0b5f117364bec73e826531c3b2ac228a0a2b74。
- 新完整 runtime checker：`35c6ee/session27297 → 729f61` 实际 exit0，2.363秒；
  全部10个 live/source 规范身份、10处规范摘要篡改拒绝、原选择和原 prepare 恢复通过。
  它在 fresh 进程执行1次原 Newton install、1次无矩阵 CSC 函数工厂，未执行
  candidate/RHS/Jacobian矩阵/LU/Newton/BVP/DN；退出前恢复原 backend references。
  `numerical-restart8000-runtime-check-01.json` 为98,323 B，
  SHA 1b407deac288f23efcf0d026b3fe3d7b2577e97c3dd906419cabce7618b52522。
- 纯新 prepare：`fcd563/session43315 → 7a4be9` 实际 exit0，181绑定，
  0candidate/restart/RHS/Newton/CSC factory/BVP/DN。
- 负 final 门：`0eda2b/session66590 → 92ecca` 实际 exit2，理由为缺少 root 的
  真实成功退出观察；0solver，不读取不存在的未来数值输出。
- 纯资源元数据：`affc94/session84954 → dc3c10` 实际 exit0，184绑定，0solver。

以上简称文件均有本目录前缀 `2026-11-10-78718-`。
它们只支付其明确的小检查/输入范围；不支付新 solver 成功或新图证书。

## 3. 当前实际准备的启动对象

stem：`2026-11-10-78718-numerical-m14-restart8000-01`。

| 文件后缀 | 字节数 | SHA256 |
|---|---:|---|
| -launch.json | 103214 | 8fa55f4f50d70e363d91944624e10d394b6906350ab4a2f853b818613c0b5996 |
| -preparation.json | 5236 | 44747e331184f26b603b8db116432357f0764964fd4a84e56cac10622d8c60f5 |
| -guard-launch.json | 53915 | cd4793d8fa58ab495e55caf2dc8dcd67c6c2625f4cf74f46820d0f1cf71380c8 |

launch 超过100 KB，按仓库规矩仅在程序内校验/择取小摘要，不全文读入对话。
原 CP 保存器按每块原始4.4 MB自适应划分 state 轴；8000节点并不强制旧块大小。
仅以一次失败 call 形状展开8轮的元数据尺寸估算为789,105 B；这是存储规划，非未来输出事实。

完整审查通过后，**只有 root 执行**以下实际启动命令。本文件及准备脚本没有执行它。

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  /workspace/scratch/78718bd0c4a9/math-research/topics/visible-flexible-closed-surface/scripts/78718-run-m14-csc-resource-6g.py \
  --launch /workspace/scratch/78718bd0c4a9/math-research/topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m14-restart8000-01-guard-launch.json \
  --observation /workspace/scratch/78718bd0c4a9/math-research/topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m14-restart8000-01-guard-completion.json \
  --backup-observation /workspace/scratch/78718bd0c4a9/math-research/topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m14-restart8000-01-guard-live.json
```

## 4. 无 solver 独立核对命令

以下 cwd 均是当前 topic 根目录；`<独有名>`必须替换为未使用的自有stem。
解释器必须用上面的绝对 primary Python，不能用未核实的 PATH 别名。

```sh
# 只做 code 常量/源身份小检查
PRIMARY scripts/78718-check-canonical-runtime-code-v1.py --out notes/<独有名>-code.json
# 原函数选择/身份/恢复，不调用求解器
PRIMARY scripts/78718-check-restart8000-runtime-v1.py --out notes/<独有名>-runtime.json
# 只验当前闭存输入，不写任何文件
PRIMARY scripts/78718-prefix-prepare-restart8000-v1.py \
  --out-prefix notes/<独有名>-pure \
  --code-check-report notes/2026-11-10-78718-numerical-canonical-code-root-check-01.json \
  --code-check-observed notes/2026-11-10-78718-numerical-canonical-code-root-observed-01.json \
  --check-current-gate
# 预期 exit2：缺少未来实际成功的 root 观察
PRIMARY scripts/78718-prefix-audit-restart8000-v1.py \
  --launch notes/2026-11-10-78718-numerical-m14-restart8000-01-launch.json \
  --mode final --check-current-gate
```

去掉 preparer 的 `--check-current-gate`，即可在自有未用stem写三件纯元数据，仍0solver。
`PRIMARY` 是说明占位符，执行时写完整解释器路径。
未来 first 审计仅付首包；future final 须 root 实际自然 exit0 及全部 closed files 绑定。
成功后仍须自有末包、全部新图连续认证、原2e−9终门、网格及原种子独立全链重跑。
