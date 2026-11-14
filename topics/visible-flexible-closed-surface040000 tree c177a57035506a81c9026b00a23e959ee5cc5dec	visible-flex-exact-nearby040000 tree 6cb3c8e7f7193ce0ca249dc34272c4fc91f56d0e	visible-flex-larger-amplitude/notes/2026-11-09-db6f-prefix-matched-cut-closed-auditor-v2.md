# 只读匹配切口审计器 v2：原 correction-scales 维数修正

作者：/root/coupled_prefix，2026-11-09。这是冻结 v1 的最小 schema 修正；v1 源码、方法、负入口观察和清单保留原字节。未运行任何正分支或 solver。

有效源：`scripts/db6f-prefix-audit-matched-cut-closed-v2.py`，29240 字节，SHA256：

`00c048161cde786c830199d092b76e4a6027e081eab180e2fc449133515050a7`。

## 唯一差分及理由

tail_theory 全文独审指出，原 WarpedBVP 的15项自由参数包含首个支撑参数；`pscale` 只对应其余14个高模 correction 参数。最终 CP 的 `parameters` 长度应为15，而 `central_correction_scales` 长度应为14。本次真实冻结 warm 的字段长度独立读取也分别为15、14。

因此，完整模式的唯一代码变化为：

```python
vector(cp['central_correction_scales'], M)
# 改为
vector(cp['central_correction_scales'], M-1)
```

不改变任何数值方程、阈值、121输入绑定、首包门、八源、root session5817 观察身份、最终 PPoly/真实 seam 比较或失败分类。该修正避免 v1 对真实最终 schema 误拒；v1 没有执行过成功正分支，未产生需撤销的正面认证。

## 使用与作用域

`2026-11-09-db6f-prefix-matched-cut-closed-auditor-method.md` 的完整范围说明仍适用；其中两个调用的脚本路径改为本 v2，其余参数保持。首包模式仍只审本次真实首个 DN/J，不推断外层成功；最终模式仍须独立 root 实际工具观察和原数值/绑定门，不新增二 jet 或 Node worker 退出门。

```bash
python scripts/db6f-prefix-audit-matched-cut-closed-v2.py \
  --mode first \
  --out notes/2026-11-09-db6f-prefix-matched-cut-first-dn-audit-v2-01.json
```

最终模式仍须在真正关闭后传入实际 `--observed-execution`；此说明没有创建该记录。若使用 `--check-current-gate`，不写审计报告。

## 实际核查

纯 AST/一处差分/真实 warm 字段长度核查：工具 receipt `310697`，实际 exit0。唯一执行入口：

```bash
python scripts/db6f-prefix-audit-matched-cut-closed-v2.py --mode final --check-current-gate
```

工具 receipt `1bf67a`，实际 exit2，`NOT_READY`，因缺少 root 实际工具退出观察而拒绝；0文件写入、0solver/flow/RK。没有读取首正包、活动 trace，没有制造成功 fixture。v2 已交 tail_theory 完整源码及差分独审；正分支等待其审查后由 root 运行。
