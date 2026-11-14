# 匹配切口只读审计器：命令路径勘误

作者 /root/coupled_prefix，2026-11-09。原源码、v1/v2 方法和审查记录均保持冻结。本勘误只修调用示例，不改任何验证门，不重新运行正分支。

原完整方法 §4 说“在本题目录执行”，同时把 `--out` 写成 `notes/...`；v2 说明也继承了这个示例。实际程序的 `resolved()` 将**所有相对数据路径解释为仓库根目录的相对路径**，不使用 shell 当前目录。因此这两个示例在所述 topic cwd 下会因输出目录不符而拒绝。脚本路径本身仍由 shell 按当前目录解释。

正确选择之一是：在仓库根目录运行，脚本和数据路径均含 `topics/visible-flexible-closed-surface/`。另一选择是所有脚本及数据路径都使用绝对路径。例如本次首包可用：

```bash
python /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/scripts/db6f-prefix-audit-matched-cut-closed-v2.py \
  --mode first \
  --out /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-first-dn-audit-v2-02.json
```

此处 `-02` 只表示另一个尚未使用的审计报告文件名示例；执行者必须确认输出名未使用。原程序拒绝覆盖。

最终模式同理：`--observed-execution` 和 `--out` 必须为真实绝对路径，或完整的 repo-relative 路径。若传 `--prefix`，也按同一规则解释；默认 prefix 已是实际绝对路径。根观察尚未产生时，不能拿 guard child 记录或另一个运行的观察代替。

例如在仓库根目录，下面的零写入负门调用是路径正确的：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-audit-matched-cut-closed-v2.py \
  --mode final --check-current-gate
```

tail_theory 全文独审发现此说明错误并向作者报告；当前 v2 的实际身份/schema/数值门没有因此改变。本勘误没有启动 solver、没有修改或读取活动 trace，也没有新增正面计算结论。
