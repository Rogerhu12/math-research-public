# 真实材料场的两投影支持半平面与冻结度量后的四百二十步

**数值证据。**

先对前条五个位置的原完整 G10/G11 全上半核直接观察两充分排球平面。五个输入均实际违反充分平面，表内另列实际球距。

| 真实源 | G11 最大 $\lvert y\rvert-z$ | 超过 $A-.65\sqrt 2$ | 实际最小距离 |
|---|---:|---:|---:|
| 原三维材料场 | 0.5226135575 | 0.03448483865 | 0.6397712114 |
| 首个隐式端位场 | 0.5187884159 | 0.03065969712 | 0.644688476 |
| 原 g 径模加密 | 0.5304963464 | 0.0423676276 | 0.6390472374 |
| 新11半径设计 | 0.5343192799 | 0.04619056107 | 0.6394178792 |
| 冻结11半径加密 | 0.5353823426 | 0.04725362378 | 0.6375724549 |

从自己的冻结11半径实场出发，保其 961 个球向位置参数和新 g，再在实际材料空间增加两条平方及四次违反罚；原全部 14 行和闭合的三维隐式导数保留。这个新 merit 的自身 420 次 L-BFGS 接受由完整新物理目标决定。末独立 G11 metric / κ / held 为 0.2200042439 / 11.2696534 / 0.6389951104。软罚设计网内的最大正违反仍约 .0316141，这一场未满足全带支持平面。

## 可移植重生

W 含前条高弯材料与冻结 g 的五个真实位置和相应 G10/G11 原输入。S 是课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-material-projected-held-planes.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --states polar-gap092-material-ridge-3D.json polar-gap092-material-ridge-implicit.json polar-gap092-material-ridge-implicit-h24.json polar-gap092-material-implicit-radius11.json polar-gap092-material-implicit-frozen11.json --fields polar-gap092-material-ridge-3D.npz polar-gap092-material-ridge-implicit.npz polar-gap092-material-ridge-implicit-h24.npz polar-gap092-material-implicit-radius11.npz polar-gap092-material-implicit-frozen11.npz --output polar-material-ridge-held-planes.json
python3 -u "$S/2ecf-polar-material-frozen-radius-physical-support-planes.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --start polar-gap092-material-implicit-frozen11.json --frozen polar-gap092-material-implicit-radius11.json --iterations 420 --plane 3500 --curvature 7 --field polar-gap092-material-frozen11-spatialplanes.npz --output polar-gap092-material-frozen11-spatialplanes.json
python3 -u "$S/2ecf-polar-material-frozen-radius-physical-support-planes.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-frozen11-spatialplanes.json --field polar-gap092-material-frozen11-spatialplanes.npz --output polar-gap092-material-frozen11-spatialplanes-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-material-projected-held-planes.py | f522ad1974e5814d24a70ed4172cc883903dac65503658bcd52ba31ff597212d |
| 2ecf-polar-material-frozen-radius-physical-support-planes.py | f4c42219331c6d401b7a3ec218517b826a4641e0354938aa114e8f597e4828cc |
| polar-material-ridge-held-planes.json | 6d49933d6b40729fa1ae70fff3b132ef350dedabd948136ac4350ce5a9d2ee68 |
| polar-gap092-material-frozen11-spatialplanes.json | 31d18cfb3a311de696281140ef8c70b312d30feab9fa596b7027517d5c224d55 |
| polar-gap092-material-frozen11-spatialplanes.npz | 1fc8d060d843946065e6529d48b0de068822d629620d8aa34e63694956c7a152 |
| polar-gap092-material-frozen11-spatialplanes-full.json | e00c26c648e6a6a1abd587d8cf4a43e199795cdd9ae07fc3d1b057ce945a143d |
| polar-material-ridge-held-planes-exit.json | 588caeb704cfb06087310ad1b9929cb50c8b0d7e7d925f783406bff0f5e1317a |
| polar-material-ridge-held-planes.log | 2d4f4756b145d836de9364e54085032f599b4c5d69b35549f87ce0fee008dfe2 |
| polar-gap092-material-frozen11-spatialplanes-exit.json | fefad3d94b373a168d65cae6dadd307ab9fb5222deec3f6ccbe2db5b9252ae1c |
| polar-gap092-material-frozen11-spatialplanes.log | f03881ff56260d9bcb161633d86330ec509f93ec3f287d146d04d2402876f6c3 |
| polar-gap092-material-frozen11-spatialplanes-full-exit.json | da86dc7014a0aac0c6bc123ff975a4b4b6b1959ab43cd3b7afab721aa9899c67 |
| polar-gap092-material-frozen11-spatialplanes-full.log | ea80b34fc566ed9b1f664c7f4bee284065d3517135f17d96e016f332c98bc167 |
