# 原始 smallcut 尾：同一物理度量的三层 Cartesian 二阶导数核对

本记录比较同一原始物理尾、同一实际 q18 高度函数的截断，尾输入符号为 `-0.07 H`，正向 worker 的整个高度在实际上侧拼接时需要整体反射。它不是 `q=0.07` 的前缀，也不是已经匹配的非线性接缝。三层均使用原始完整零模方程与正 `D/S/A` 根分支；没有替换方程或删除守卫。

## 可复核结论

在 163 个共同物理径向点及 128 个共同材料角上，重新以 256 角根积分评价实际 Cartesian 导数。径向点包括全部有限 shooting 节点和 cell0 各子段中点。数值如下。

| M | 度量最大误差 | 完整向量 Darboux 张量缺陷 Frobenius 界 | 实际主曲率最大值 |
|---:|---:|---:|---:|
| 8 | 8.0328131e-9 | 1.9554273e-5 | 8.0231539 |
| 12 | 2.2371867e-9 | 1.1537608e-5 | 8.0231328 |
| 16 | 9.2903270e-10 | 8.2277951e-6 | 8.0231309 |

相邻层真实 Cartesian 导数的最大差：

| 导数 | M8 至 M12 | M12 至 M16 |
|---|---:|---:|
| X_r | 1.2911790e-5 | 5.2144854e-6 |
| X_u | 1.2376545e-6 | 7.6983202e-7 |
| X_rr | 3.8163253e-3 | 1.2986595e-3 |
| X_ru | 2.2780493e-4 | 1.4318269e-4 |
| X_uu | 2.3825072e-5 | 2.0426170e-5 |

正交归一混合 Hessian 的层差为 8.23754e-4 与 5.17643e-4，角向 Hessian 的层差为 3.41382e-4 与 3.01724e-4。因此，小度量误差不能掩盖仍可见的 C² 差距。这三层只提供下降的有限数值证据，不能断言一致 C² 收敛、径向离散已经收敛、无限尾已经闭合或存在实际非线性接缝。

最大 `X_rr` 层差位于原 cell0 的 segment5 中点，`r=0.27795459773837033`，`w=0.006850907933174124`。该点 M16 的四阶 profile 差分步从 `2e-4` 缩到 `1e-4` 再缩到 `5e-5`，`X_rr` 的最大改变分别只有 `3.2043e-12` 与 `3.9375e-12`。因此这里的 `1.3e-3` 层差不是该局部有限差分步的舍入或截断噪声。这个局部试验不替代全域差分/径向误差控制。

## 数据与再生

本目录仅保存源码、标量摘要和输入/输出哈希。三个约 2 MB 的共同网格数组、原始 shooting checkpoint 只保留在 scratch，可由代码重算，不应提交。

物理源固定在提交 `46fe93d4bb708fdfb7935e91b8141ea77586f0d2`。通过此前的 `nonlinear_tail_recovery_manifest.json` 恢复同一 source topic。实际 H 由已发表 fixed q18 checkpoint 运行 `extract_H.py` 获得，不需要提交其系数数组。

原始三层 checkpoint（从 scratch 根目录看）为：

- M8：`nonlinear_tail_work/original_negative_m8_tol8_run/response_0004.json.gz`，SHA256 `d44a8858b5ae73fe4049cb59c0f0ee011584adbebb6365ccfd0871cc0868f338`。
- M12：`nonlinear_tail_work/original_negative_m12_lam07_run/response_0001.json.gz`，SHA256 `cd002edffa62acd734bb8512770edacd48602df505f800de7fca7a4f522cdc3f`。
- M16：`nonlinear_tail_work/original_negative_m16_lam07_run/response_0001.json.gz`，SHA256 `a8b5d20f5dd980c988bc3aca7f7e864c4bfa0265721279dc37e6d33618a55939`。

`twojet_refinement_inputs.json` 冻结对应配置及 checkpoint 哈希。可用已发表 `continue_tail.py` 从原始小幅负号支逐步续到 `-0.07`，然后使用物理 Q/L warm 将 M8 升到 M12、M16；配置中的 scratch `initialCheckpoint` 只需改为这次再生的对应文件。三层原求解条件的差异（角积分与求解容差）显式保存在配置中；重评时均用同一个 256 角根积分与相同 32 步径向离散。

共同网格重评命令模板（`SOURCE_TOPIC` 为恢复源码，`RESULTS` 为 scratch 输出目录，`CHECKPOINT` 为对应层的再生 checkpoint）：

```sh
node export_common_twojets.mjs "$SOURCE_TOPIC" "$CHECKPOINT" "$RESULTS/m8-twojets.json.gz" 256 2
node export_common_twojets.mjs "$SOURCE_TOPIC" "$CHECKPOINT" "$RESULTS/m12-twojets.json.gz" 256 2
node export_common_twojets.mjs "$SOURCE_TOPIC" "$CHECKPOINT" "$RESULTS/m16-twojets.json.gz" 256 2
python compare_common_twojets.py "$RESULTS/m8-twojets.json.gz" "$RESULTS/m12-twojets.json.gz" "$RESULTS/m16-twojets.json.gz" --out "$RESULTS/comparison.json"
node check_twojet_difference_step.mjs "$SOURCE_TOPIC" "$CHECKPOINT" "$RESULTS/rr-step.json" 7 .5
```

前三条分别将 `CHECKPOINT` 设为对应 M；最后一条使用 M16。脚本输出的全数组只用于比较，标量汇总见 `common_twojet_refinement_summary.json` 与 `m16_lam07_rr_step_check.json`。

发布参数中的尾随零控制以 `valleyControlsPadTo` 记录，既有continue_tail.py在传给原worker前逐字恢复；物理参数没有改变。
