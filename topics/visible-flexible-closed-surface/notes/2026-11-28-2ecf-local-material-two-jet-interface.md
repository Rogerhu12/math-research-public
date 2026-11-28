# 局部材料二jet预算的实际接口与生产入口

2026-11-28，Astra-visible-flex-2ecfcd69-20261128。

完整证明见 R249。非零两片、74角通道人工场的实际接口自然退出0，用27.334470433秒；12,545点独立样条/材料导数均在准确连续界内，链式与Fourier分子最大差4.5537353633559805e−20。人工坐标a=1、s=z、f=1明确不同于生产M12，不借此称研究场合格。

实际已执行 checker SHA为17f36619a2372cde6833254239305ba50d409db8be2369ec65daac031079bbfb；发布版只在输入入口追加“内部节点重数≤3”的C2守卫，计算函数未变，发布SHA为c7e5f4c82616ed43103e234ca774a6e5e95cb46e93dc18c6b2463654911fb632。fixture源码SHA为131472e2fd98faa52631f377a1b42ea378849424f71e72e6ac889f89a626117b，实际报告SHA为4849f1f585343e8f43fa47c77962e14baf8fd4284213ff507a679d9074027b7b。报告正文不入库。

复现人工接口：

```sh
OPENBLAS_NUM_THREADS=1 python "$SCRIPTS/2ecf-m12-local-material-two-jet-fixture.py" --scripts "$SCRIPTS" --data "$SCRATCH/m12-prefix-data.npz.gz" --out "$SCRATCH/two-jet-fixture.json"
```

生产入口：

```sh
OPENBLAS_NUM_THREADS=1 python "$SCRIPTS/2ecf-m12-local-material-two-jet-budget.py" --scripts "$SCRIPTS" --data "$SCRATCH/m12-prefix-data.npz.gz" --field "$FIELD" --grid "$GRID" --result "$RESULT" --correction-bounds "$R226_REPORT" --source-bounds "$R230_REPORT" --out "$SCRATCH/local-two-jet-budget.json"
```

默认128角盒、8阶Taylor、径向最大一层细分；所有缩放/源/field身份必须一致。原H1-M48/fullH的旧raw不可取，本轮将消费实际重新保存的新场，不能给旧场补未经执行的界。新程序仍未用source-cross-Gram或source法向投影抵消。
