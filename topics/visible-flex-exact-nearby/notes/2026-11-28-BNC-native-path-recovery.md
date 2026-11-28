# BNC 原生路径恢复：实际零目标失败及最小续接

2026-11-28，`visible-exact-astra-b0d5a16-20261128 / actual_inverse`。

**状态：已确认的执行故障与修复；没有新增数学数值结论。**

## 实际失败

公开 run `45941963989/1` 于 2026-11-27 06:11:57 UTC 结束。
完整 actual 的 SHA-256 是
`078ba88c2708850ec12ea1c1451d0d65b350f9fbd081156682721ae300589008`，
execution 的 SHA-256 是
`fa598e7342496c5bd8321a8a09d9ee1dc3d52c68432677f0740dba008bc61cb6`。
两个对象均保留原来的失败状态；未改写、删除或称为成功。

实际已有一个科学子进程，完整原 G grid 和原 B 行输入已经恢复，
随后 NP 恢复在读取原 candidate index 时失败。
`complete_observation_modes = saved_record_count = 0`，
`completed_targets = []`，`new_records = {}`，
NP 的四个原 trial carriers 尚未恢复，没有完整 BNC 配对或七个新目标。
这不是数学门失败。

完整 traceback 定位为 `candidate_reader.load_candidate` 的后缀分支。
原 index 是 `.json`，原 publication engine 却将所有历史文件命名为
`history_dir/(role + ".json.gz")`；原 loader 因此走 `load_single`，
而原输入合同刻意禁止这个分支，抛出
`only the complete original sharded JSON indices are admitted`。
只改成 `.json` 后缀也不够：index 内的五个 shard 使用原 sibling
basename，按角色改名仍会破坏相对定位。

## 修复与不变的数学对象

新增 wrapper 只把实际 materializer 的该条语句改成
`history_dir/topic_path(spec["path"])`。
`topic_path` 仍执行原路径约束；`atomic` 仍创建父目录并写完整原 bytes。
所有原 Git blob、长度、SHA-256 检查不变。
于是原 index 保持 `.json`，每个 shard 保持原 basename 及同一父目录。

原数学 owner、原 admission、原 public wrapper 和原 generator 均保留，
新 wrapper 在执行前核对它们的整个 SHA。owner 和 admission 仅替换
三个入口路径常量；原七个目标、所有参数、全部误差式及真实 mean/phase
义务不变。新 admission 另完整消费原 failed actual、execution、manifest
和 consumed marker，逐项确认旧执行完成了零个 BNC 数学目标。
新 consumed marker 专门标识这次 operational recovery，旧 marker 原样保留。

## 已实际执行的元数据检查

新 generator 已在本地仅执行一次元数据构造：

- 原 generator 重新构造的整个 manifest 与已推送原 manifest 完全相等；
- 新 worker 展开的实际 AST 仅有一个历史目标路径赋值，恰为
  `history_dir / topic_path(spec['path'])`；
- 读取完整原 candidate index 元数据，核对其 whole SHA，及全部五个
  sibling shard 的路径、长度和 SHA 与原 historical descriptors 一致；
- 新 entry 含 187 个 current inputs 和原 51 个 historical inputs；
- 未导入 `numpy`、`flint`、`scipy`，未运行任何积分、配对、残差、
  旧科学目标或新科学目标。

唯一新 manifest 是
`2026-11-28-target-normalized-strict-nu-native-paths-inputs.json`，
79,755 bytes，SHA-256
`74bb82d9c9640d8ffd3a6350c3d56a0fa34b6bd7d7b451775f428786a5e35b9e`。
实际 Actions run、完整数学输出和成功与否须由后续真实执行给出；
本记录不预报。

## 启动文件

- `fourfold_codazzi_target_normalized_strict_nu_native_paths_owner.py`
- `fourfold_codazzi_target_normalized_strict_nu_native_paths_inputs.py`
- `fourfold_codazzi_target_normalized_strict_nu_native_paths_public_worker.py`
- `make_target_normalized_strict_nu_native_paths_manifest.py`

新 generator 的 `workflow(root, manifest_sha256)` 返回完整 workflow 文本。
唯一入口为
`.github/workflows/fourfold-codazzi-target-normalized-strict-nu-native-paths-public.yml`。
恢复成功后仍只得到 BNC 的完整低 96 坐标，不能补零为整个 forward 列，
不能替代 BFP、真正 homogeneous 96 列、全 Schur、mean/height 或最终闭族。
