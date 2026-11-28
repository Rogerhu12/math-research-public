# h503 保存场的同节点独立观察与实际非线性梯度

数值证据。原固定g、原X+C源的M64/G12物理h加密已保存实际一步的新场451481cd；原M64场3ca49d46为父，用其真实Boehm注入ed281cfa与新场在全部相同7042个G14径向点、3072个独立角点上比较。张量积有21,633,024个观察点。比较同时覆盖503个物理跨度，父侧统计重新在新点集计算。

| 独立G14/N3072 | 实际暖输入 | 实际保存场 |
|---|---:|---:|
| 相对度量最大特征值绝对值 | 5.424143134351277e−10 | 4.944020895812999e−10 |
| 原目标加权能量 | 2.1422817208660946e−21 | 2.0744834931273227e−21 |
| 原未正则独立目标的实际 $\|J_{当前}^T r_{当前}\|_2$ | 9.018417856861304e−12 | 7.878211244343058e−12 |
| 观测曲率峰 | 6.428917514613397 | 6.428917289882362 |
| 观测支撑下界 | 0.8178848938021344 | 0.8178848938021428 |

梯度范数比0.8735691081722539，按对应场重算原Jacobian和原Gram残差。原线性步的正则/未正则normal见[已接受训练步](2026-11-28-2ecf-m12-h503-retained-full-Gram-accepted-step.md)；各量不互相替代，也不为原README添加驻点阈值。训练峰下降后，独立峰也下降。保存场独立峰在新跨度198、径向索引2776、角索引1782、尾半径0.5134714273891165195。前缀局部最高在新跨度157、径向索引2208、角索引2563，峰4.804799303389076e−10。上述峰仅属所列点集。

原LM自然exit0，内部2241.529412658秒，stage2242.923510525秒，实测进程RSS峰1156624KiB。完整原独立源包单组峰3,288,369,588字节，已清理。实际R226自然exit0/21.34966432秒，原全局几何消费者自然exit0/0.127054123秒。该消费者的原粗界给出全时握持比下界约0.05278295648、握区直径比下界约0.93545818；全时嵌入/管状转移条件真。其reach/D下界仅约0.01375398859、全局度量三角上界约0.00136208023，所以这个消费者未付reach/D≥0.03或全域度量目标。各严格量以报告所指有理数为准。原5778场的全域B=2e−9主线独立。本条终稿时旧R236、micro和11178点祖先并集仍在原始7阶段管线中，未提前称通过。

| 06r1实际文件 | SHA256 |
|---|---|
| 保存场 result.json.field.npz | `451481cdaff2e12c7c3bdb720274709652dd34a89ae63ae6554f8ac68789ead3` |
| 求解与独立观察 result.json | `c27a3c43ec70c8a653752802351eb8a0a095b10b4af3120e9536a041a7405b94` |
| correction-bounds.json | `f70c70630bf0650ef5cf92601f39c030982c6f9a4fba127cb7c799d4d4de9877` |
| geometry.json | `e53e42ee788237395863da6d49b7402e7d1eb2e14abef3aa3b6709bf254ec7ad` |

## 重生

从[原查询、全源和真实Boehm配方](2026-11-28-2ecf-m12-actual-m64-peak-h503-preparation.md)恢复相同输入；下列命令涵盖本条全部已返步骤。求解入口SHA256 `81d6ac5e8ea02b4da6bab1317f218eb3fcc12061475268097143fa87c49956a0`；各消费源码完整身份见前列已接受训练步和真实输出。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-refinement-execute.py --scripts scripts --data <M12-prefix-data> --old-grid <actual-M64-output>/grid.json --old-field <actual-M64-output>/result.json.field.npz --old-result <actual-M64-output>/result.json --old-correction-bounds <actual-M64-output>/correction-bounds.json --new-grid <h503-output>/grid.json --query-report <h503-output>/exact-tail-queries.json --query-cache <h503-output>/exact-tail-queries.json.npz --source-bounds <h503-output>/original-source-bounds.json --out-dir <fresh-h503-run> --solver-entry scripts/2ecf-m12-h2-mapped-disk-normal-cached-lm.py --lambda-step 1e-13 --steps 1 --hessian-step-cap .05 --block 24 --normal-assembly-block 8
```
