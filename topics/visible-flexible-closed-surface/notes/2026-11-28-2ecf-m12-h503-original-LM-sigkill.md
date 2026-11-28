# M12 原固定几何 h503 首次 LM 被 SIGKILL

数值运行记录。原源增加416个准确半径、重绑原源连续界、原M64场Boehm注入分别自然返回0。接续的全阶原固定g物理LM持续903.059155768秒，子进程返回−9，外层收到247。最新打印行是完整Gram的4104/6036径向行，已组装361.46058559秒，当前RSS 1456052 KiB。没有接受步、非线性输出场或该场的后验报告。未取得系统杀进程原因；此退出不能推断数学方向失败或内存上限的精确数值。

| 本次保留回执 | SHA256 |
|---|---|
| 原始驱动日志 | `80ac617fa1576fb5a846f4f6b8a73f4cbb4000d0afe86b3952a5683b94308e40` |
| execution.json | `9ff324286805c279fa3e1e86b28b0aba6b09b282c4c8df74d8d1bd5435ea98ef` |
| source-and-solver-execution.json | `95b4517a92e0755256ef8c6c36a1601b8c7516bde8b08763fed3ca9dfafac639` |

[准备记录](2026-11-28-2ecf-m12-actual-m64-peak-h503-preparation.md)给出原数据、全部输入SHA及生成配方。原始 solver-entry SHA256 `b9c3c361bdad2d2271bbd00e771a44dcfd02b20bb304b56d7f4198c65e2827ba`。以准备记录所列数据在课题根目录运行以下命令；运行时替换尖括号路径。退出信号取决于外部运行环境。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-refinement-execute.py --scripts scripts --data <M12-prefix-data> --old-grid <actual-M64-output>/grid.json --old-field <actual-M64-output>/result.json.field.npz --old-result <actual-M64-output>/result.json --old-correction-bounds <actual-M64-output>/correction-bounds.json --new-grid <h503-output>/grid.json --query-report <h503-output>/exact-tail-queries.json --query-cache <h503-output>/exact-tail-queries.json.npz --source-bounds <h503-output>/original-source-bounds.json --out-dir <h503-output> --solver-entry scripts/2ecf-m12-h2-sparse-disk-normal-cached-lm.py --lambda-step 1e-13 --steps 1 --hessian-step-cap .05 --block 24 --normal-assembly-block 8
```
