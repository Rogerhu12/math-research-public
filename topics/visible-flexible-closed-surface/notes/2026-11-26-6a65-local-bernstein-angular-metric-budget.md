# 原 M12 局部连续度量验证器：实际核验与复现

完整充分条件与证明已登记为 [R236](../results/R236-local-bernstein-angular-continuous-metric-budget.md)。以下保留两次真实人工场核验、未执行边界及同job消费命令；未借用任何已结束CI场的系数。

## 6. 实际执行与未执行边界

新脚本：`scripts/6a65-m12-local-bernstein-angular-metric-budget.py`。

已真实执行的独立检查：有理节点/随机有理控制行的 Boehm 提取及升阶导数与 SciPy `BSpline` 独立点调用比较，最大绝对差分别 $8.48\times10^{-22}$、$3.39\times10^{-21}$；两种向量平方范数的自相关与直接 Cartesian 计算差不超过 $2.55\times10^{-32}$。整数 Taylor 各盒额外用独立密角数值调用排查实现错误。解析证明是 (1)–(3)，这些数值比较仅检查实现。

完整入口使用另名人工场 `synthetic-field.npz`，形状 $361\times98$、原完整 $362$ 元网格，真实重新运行 R226 得绑定 receipt，然后调用本程序。运行 exit $0$，用时 $10.069$ 秒，$381$ 个最终闭片、$19$ 次细分、$267$ 个实际角向细化控制行。该人工场的旧导数界为 $3.7853473\times10^{-5}$，新界为 $1.0854336\times10^{-6}$；相应充分 metric 界 $2.1965895\times10^{-6}$，因此程序如实输出门槛 **false**。这验证了失败分支不会把显著改进冒充过关，亦不代表任何原实际 CI 场。

最初临时代数 harness 有一个括号语法错误，修正后检查 exit $0$；数学源始终单独作 `py_compile`。人工场和所有大/原始数组仅保留临时目录，仓库只保存源、证明及小标量回执。

同 job 消费实际场的完整调用为：

```bash
python "$SCRIPTS/6a65-m12-local-bernstein-angular-metric-budget.py" \
  --scripts "$SCRIPTS" --data "$M12_COLD_DIR/m12-prefix-data.npz.gz" \
  --field "$M12_COLD_DIR/entire-half/entire-half-result.json.field.npz" \
  --grid "$M12_COLD_DIR/entire-half/entire-half-grid.json" \
  --result "$M12_COLD_DIR/entire-half/entire-half-result.json" \
  --correction-bounds "$M12_COLD_DIR/entire-half/entire-half-continuous-change-bounds.json" \
  --out "$M12_COLD_DIR/entire-half/entire-half-localized-metric-budget.json"
```

新输出必须和该次实际 field SHA 一起发布。未完成该调用之前，已结束 run `45815969723` 的有效 metric 上界仍为 R234 所记录的 $4.862154697\times10^{-6}$。

## 7. 可重生的独立核验入口

第二个新源 `scripts/6a65-m12-localized-metric-independent-check.py` 保存了上述随机种子、有理小例、独立 SciPy/Cartesian 比较以及人工场的完整系数生成式。它要求原 $362$ 元、order $32$ 的临时 `prepare` 网格，自动生成另名人工 field，依次实际调用原 R226 与本 checker，数值子进程剥离恢复令牌环境变量；不接触任何 branch/ref。

```bash
python "$SCRIPTS/6a65-m12-localized-metric-independent-check.py" \
  --scripts "$SCRIPTS" \
  --checker "$SCRIPTS/6a65-m12-local-bernstein-angular-metric-budget.py" \
  --grid "$OLD_PREPARE_GRID" --data "$M12_DATA" \
  --out "$FRESH_TEMP_REPRODUCTION_DIR"
```

该完整重生入口已真实执行：总用时 $23.096$ 秒，两子步骤 exit 均为 $0$；checker 本次为 $13.500$ 秒。所有准确界与第一次人工场运行逐项相同；报告 SHA 因实际计时不同而不同，这是两个真实执行记录，不是假定逐字相同的回执。标量保存于 `notes/2026-11-26-6a65-localized-metric-checker-validation.json`。人工 field SHA 为 `a7705a3d94bbc2dfe58254398e5c219301d63035a87ec443ff9307b2bf21cf2c`，与任何之前真实解算场身份均分开。
