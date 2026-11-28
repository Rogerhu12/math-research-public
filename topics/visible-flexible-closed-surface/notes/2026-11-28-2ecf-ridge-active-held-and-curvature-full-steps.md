# 两握持排球及主曲率主动约束下的六个实位置步

**数值证据。**

从 V26 高弯全径线面自己的第二个位置场重新起算。固定原 g、完整 5292 个空间系数及全部 4291840 物理行和 H²。在每个 GN 方向上，直接算两个实际空间距离和两主曲率的方向导数，按预期违反的径角小块挑观测点，构造真实六 jet 余切，投影到最多 80 个线性不等式。投影为原 H² 白化系数的欧氏投影，双对偶非负优化；每个线性导数以实际未投影方向核对。最后对全 G10 硬检两排球 held≥.64、两曲率绝对值≤16.5 和 14 行原目标的 Armijo 一起决定接受。G11 始终独立。

| 自身接受数 | G10 R² / κ / held | G11 metric / κ / held |
|---:|---|---|
| 1 | 0.3802335124 / 16.19949421 / 0.6400039258 | 0.3425530284 / 17.33137958 / 0.6400262749 |
| 2 | 0.2626783054 / 16.26064496 / 0.6400726033 | 0.3251486423 / 16.92793476 / 0.6400642282 |
| 3 | 0.2571766631 / 16.40266133 / 0.6400725802 | 0.3230358237 / 16.91290374 / 0.6400644399 |
| 4 | 0.2544970769 / 16.47509523 / 0.6400725834 | 0.322039661 / 16.90491826 / 0.640064558 |
| 5 | 0.2538346938 / 16.4932818 / 0.6400725854 | 0.3217853338 / 16.90286917 / 0.6400645886 |
| 6 | 0.2536695425 / 16.49783044 / 0.640072586 | 0.3217222486 / 16.90235354 / 0.6400645962 |

第七个方向 12 个步长均未同时通过；最小步 κ=16.5001048390、held=.6400725863，完整记录保留。六个独立 G11 状态均保 held≥.64，宏观全观察 κ 却都超过训练约束 16.5。最后 G11 κ16.90235354、metric .32172225，不能推出连续上界或强厚度。

## 可移植重生

W 含前条高弯规定速率全径线源及该源的实际第二位置态，S 为公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-physical-rays-held-curvature-projected-gn.py" --scripts "$S" --prepared polar-gap092-physical-ridge-prepared.json --state polar-gap092-physical-ridge-innerGN-step02-state.json --steps 7 --prefix polar-gap092-ridge-projected
python3 -u "$S/2ecf-polar-physical-ray-G11-states.py" --scripts "$S" --prepared polar-gap092-physical-ridge-prepared.json --states polar-gap092-ridge-projected-step01-state.json polar-gap092-ridge-projected-step02-state.json polar-gap092-ridge-projected-step03-state.json polar-gap092-ridge-projected-step04-state.json polar-gap092-ridge-projected-step05-state.json polar-gap092-ridge-projected-step06-state.json --output polar-gap092-ridge-projected-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-physical-rays-held-curvature-projected-gn.py | aba7c321bb97f81505a838d1e74042e066c575ffc2e7e1378a552f41d8ad3500 |
| polar-gap092-ridge-projected-report.json | e17b0ddc9657e8da6b171f96dd67b04f5006d22780d483e87f8bcadbe0c81784 |
| polar-gap092-ridge-projected-G11.json | 50c86a5618576298a44dbbce15597d77fb4c52b31606f66de24c3434e73932fa |
| polar-gap092-ridge-projected-step01-state.json | 716168572d4d33d85de5cb1b8da1abc8bb40062b17925230a399fdb1b088519e |
| polar-gap092-ridge-projected-step02-state.json | a88e44045ebf581d33d31a11a590d34a44cd38cb1e35680635c85c97a346c939 |
| polar-gap092-ridge-projected-step03-state.json | c1286c76453d6b60587712a08540ce87f79a6484a74670ba02b5b8935d23c857 |
| polar-gap092-ridge-projected-step04-state.json | 0291ac099761bf92ce984c2f4d8e81277218ac5330779e6f70555d4fcaa27f10 |
| polar-gap092-ridge-projected-step05-state.json | cdc330dc86847c02de834dba9ac33eb4cda7189e8e8a1e019cdcd443a31d9254 |
| polar-gap092-ridge-projected-step06-state.json | 597f535e71242dfc47589405cdb02fdb9045772d8c78ba95f92cf1d7005935d4 |
| polar-gap092-ridge-projected-exit.json | 4c5bd1150551bdb94d7b229d29fb441b9580a8e04e3fae6e6793acb428ee5a2d |
| polar-gap092-ridge-projected.log | 44961b870a2270e3f13b2daa980419726e567de4f7668446cc415ce1e99ca673 |
| polar-gap092-ridge-projected-G11-exit.json | 50461f1ca4a7a07cd64c9e0a5851d6d877d576185b11372d1406a1536d5f31a8 |
| polar-gap092-ridge-projected-G11.log | dcba14efc162d2373bf0e72d00ba2b21bee89cc4ca07ff5628cebe50e916e43b |
