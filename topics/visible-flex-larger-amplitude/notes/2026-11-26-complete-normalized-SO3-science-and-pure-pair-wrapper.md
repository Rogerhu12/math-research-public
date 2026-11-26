# 2026-11-26 完整 normalized SO3 科学／纯读取对的单次准入包装

## 1. 目的和准确范围

run04 的控制器对每个队列step单独作预算准入。一个已经准入的完整科学child自然返回后，控制器可能已越过新step的准入窗口，因而其独立纯reader尚未执行。这个新完整包装只把原科学launcher和原纯reader顺序放在**同一次已准入child**内。科学源、全部argv、真实父、固定目标、范数、观测、全C、Phase I、ray、SOC、接受门和完整reader验证均不改变。

它不能延长GitHub Actions job硬时限。若job硬取消或进程被杀，未返回的child仍是未返回；包装不会宣称其完成，也不会用缺失报告补科学值。当前已排的原48/49两个独立step不被本包装替换；后续如需使用，必须在新真实父返回后另保存完整参数并由根代理实际发布准入。

## 2. 完整来源绑定和完整参数

完整新源为 `scripts/resume_20261126/run_normalized_so3_complete_pair.py`。其只接受以下已锁完整来源：

| 角色 | SHA256 |
|---|---|
| 原科学launcher | `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| 原完整科学driver | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 原完整pure reader | `009e1e1d54ccd41e8ac2b4e6efe43541ebc327b7a6f3d4fa743e145517c897e6` |

包装逐一核实际checkout中的完整文件字节。科学launcher及reader内部原有全部来源、父、模型、范数、全body和cache验证继续执行，不修改其声明，不伪造兼容标签。

单独发布的小参数文件 schema 是 `complete-bound-normalized-SO3-launch-and-reader-pair-parameters-v1`，保留完整的两个原step对象于 `steps`。每一对象保留原step身份、script、scope、admission parent、全部argv、outputs、summary和清理责任，不能缩成“同前”。包装对该参数文件的实际完整字节执行SHA256核。它只替换原有字面占位符 `{repo}`、`{work}`，不增删、重排或修改任何科学argv。

CLI为：

```text
python -u run_normalized_so3_complete_pair.py
  --repo ACTUAL_CHECKOUT
  --work ACTUAL_RUNNER_RESEARCH
  --parameters ACTUAL_CHECKOUT/COMPLETE_PUBLISHED_PARAMETER_FILE
  --parameters-sha256 COMPLETE_PARAMETER_SHA256
  --output ACTUAL_RUNNER_RESEARCH/FRESH_PAIR_STATUS.json
```

`--print-only`只完成来源/完整参数/现存父及路径验证并打印完整将执行命令，不启动任何child。实际科学执行要求本公开仓库的真实Actions环境。

## 3. 完整同父和路径条件

两step必须保留同一个已经实际存在的admission parent，它必须逐路径等于科学argv中的 `--restart-checkpoint`；包装实际读取并记录该父SHA。这仅适用于完整已有父的continuation，不拿新包装代替无restart的初场构造。

科学 `--outdir/report.json` 必须逐路径等于纯reader的 `--report`，原reader的 `--verify-final-bundle`、`--verify-cache-files` 都必须保留。两step各自的输出声明完整保存；所有新结果及pair-status在本runner work目录内、源repo之外，并要求fresh而不能覆写旧父、旧结果或已返pair。参数文件本身必须是完整公开checkout内的小文件。

外层单step仍须声明两个child的全部实际outputs和原summary映射，并保原明确cleanup pattern；包装本身不清理科学缓存或永久地点。不把在参数文件里记录了旧cleanup声明当作清理已经执行。

## 4. 真实执行和失败语义

包装先把自己的源SHA、参数SHA、完整来源、实际父和将执行的完整命令写到runner独立status，随后顺序执行原两个child。stdout/stderr直接流向原Actions日志，不吞掉科学或纯reader的真实错误。

第一个child返回后，无论exit是否为零，第二个原pure reader都会实际尝试。如果科学在生成报告之前失败，pure也会按其真实原逻辑失败；两者各自的启动、返回码、耗时、错误和存在／缺失输出记录均保留，不能把pure成功假定为科学成功。

每个child返回立即写入pair-status，再继续后继；已存在outputs逐一记录完整实际SHA和bytes，缺失仅记 `exists=false`，不生成占位报告。包装不解析大科学报告来制造新的几何、QP或收敛声明。外层exit0仅在两个child都实际exit0时返回；否则exit1。pair的过程完成与 `scientific_success`、`pure_success`、`both_children_returned` 各字段明确分开，永不宣称连续场认证。

如果发生真实中断，记录已经进行到的child及异常后重新抛出；不能声称保证在硬取消后执行pure。本入口仅消除“自然返回后需要第二次控制器准入”的间隙。

## 5. 验证和未完成责任

本地只作完整源码读取、AST、compile、py_compile、尾空白及三完整来源SHA比较，未执行F、J、QP、root、科学数组或任何数值fixture。新实际参数必须等待其对应真实父返回；当前没有为尚未返回的下一父填科学SHA、位置或结果。

本次是执行编排入口，不是新的数学结论、科学方向或完成证书。README的全域误差、同g精化、全t几何和全部历史地点责任均保持。
