# 间隙 23/25 新固定度量的第一个真实后缀位置步

**数值证据。**

在新固定度量的完整 4291840 行上，导入旧 H65 原度量 own1 的 5292 个后缀位置系数。整个新 central/ramp/coast 固定，旧 α 设计不参与，右端和真帽保持。新 A=1.407367534347312 决定 held 距离；每个原曲率、球宽、高度和 held guide、Q2 面积、物理 H² 增量全部支付。复测新源与新约束对应的完整物理 J、JT、原正规残差；后者相对值 7.2551e−15。独立 G11 错移 256 角，整个训练和观察使用原几何范围但不同的新源。

| 自身步 | G10 R² | G10 metric / κ / held | G11 metric / κ / held |
|---:|---:|---|---|
| 0 | 0.42181581445 | 0.32475864995 / 20.402157014 / 0.65955441962 | 0.32419962956 / 20.236024338 / 0.65970512773 |
| 1 | 0.1825265815 | 0.28406843794 / 20.300470527 / 0.64670852743 | 0.28213560102 / 20.348188247 / 0.6468547291 |

拒绝步长 1 后接受 .5。新 g 自身只计 1 步；独立 metric 最大值从 s=.365647 移动到 s=.920208。第一步的 held 在内部 guide .65 以下，强目标仍须整个闭核证书。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --warm-state polar-physical-H65-coarse9-step01-state.json --initial-damping 0.021333333333333333 --steps 1 --prefix polar-new-gap-092-fixed-step01
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step01-initial.json --output polar-new-gap-092-fixed-baseline-G11.json
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step01-step01-state.json --output polar-new-gap-092-fixed-step01-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-new-central-gap-suffix-solve.py | c85d0d8820607873524baa1e1ddc6bc97e3a9a581225e2ee79d131badbbd6be8 |
| polar-new-gap-092-fixed-step01-initial.json | b3549fa7c768ca4abaeb2c782b291a543adddeb0a0d0f66e4abf7bf9c9707085 |
| polar-new-gap-092-fixed-step01-actual-derivative-check.json | 9fa989f4c113c157927c0341d09aaa1ad666874f511c3246cf87104e08eb64a8 |
| polar-new-gap-092-fixed-step01-step01-state.json | 8342119f84cc193d9812c4616c32798aba8bd1501a36f108e7234b9ae060cb4a |
| polar-new-gap-092-fixed-step01-report.json | ab93162cd97459b2aea8c0420579f7cdf945935baf2a326de1ab55dec7af9e36 |
| polar-new-gap-092-fixed-baseline-G11.json | 9860464a8fd0880b231138d7c67bebec4bb2fc84e2c9cc210fea1eb541baa5a0 |
| polar-new-gap-092-fixed-step01-G11.json | d192b774569efa3789fe40810780e05aa1a78e165bb70bd9d0a6076fa9221bf3 |
| polar-new-gap-092-fixed-step01-exit.json | c84b0ef2132bd36d698db9d4994fd948f49429a4a3294b579fbe7f7ce4bc7f3a |
| polar-new-gap-092-fixed-step01.log | fa24bc090e588dd11e8dedbdd82f0d867b7c9a1ae28d35dad6f243f65bed73ac |
| polar-new-gap-092-fixed-baseline-G11-exit.json | b5ff6815d83f15ff766d53b57177d1dafcf1698f80cabe6ffd7e1d5e3a62e616 |
| polar-new-gap-092-fixed-baseline-G11.log | dc06a2979a43f620cbded813a8f3d7a4d9a6b0752cc8597b54a5983580d8ace3 |
| polar-new-gap-092-fixed-step01-G11-exit.json | 9776fbe7b7a5895854e7a194f56948d07a47cff8e033205558f515b2a9ac6f14 |
| polar-new-gap-092-fixed-step01-G11.log | 4e8f0a50d7d99320cffc2220a17f551c14f8155a748776b7ea5895537c66e1ac |
