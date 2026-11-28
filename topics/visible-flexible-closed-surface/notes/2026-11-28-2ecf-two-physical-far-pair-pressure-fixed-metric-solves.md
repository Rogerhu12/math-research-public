# 全带两向法球与实际远区弦距的两个位置求解

**数值证据。**

以 R290 所消费的原 hardspheres 真实位置和同一冻结 g 为起点，在完整设计网和另加的 11 个实际平环内圈上形成远径点对：两材料 s 差至少 .32，候选真点距小于 .265，每个阶段前后按真实位置重建邻域。第一个输入对两端分别处罚 max(0,|n·d|−|d|²/(2R)) 的平方，并经归一法向对两个真实切向量传播精确导数。第二个输入处罚 max(0,2R−|d|) 的平方。R=.1，两输入均保留原 14 行与两真见证排球。每个输入的三个权重阶段分别做 260 次自己接受，阶段后远区均重新做实际搜索。

| 输入 | 各阶段后设计网远区最小真法球比 | 完整 G11 误差 / κ / held |
|---|---|---|
| ball | 0.071676797 → 0.084805574 → 0.090869031 | 0.207476764 / 11.03974362 / 0.6539706607 |
| chord | 0.076175165 → 0.086099278 → 0.091770857 | 0.2271263563 / 11.28141864 / 0.653928696 |

首次两个试运行在 L-BFGS 线搜索中因实现给试探步附加 .05 面积下界而自然退出 1，未生成接受态。正式运行去掉此人为试探阈值，只在真正奇异法向时拒绝构造单位法向；重启后均完成。距离项首次独立观察受外部 signal 9 结束，另次原输入完整观察自然 0。远区统计还未覆盖闭帽和全部参数对，各自的 G11 局部曲率也超过 1/.097。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-physical-nonlocal-normal-ball-optimization-line-search.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-true-far-retry-ball.json --start polar-released40-actual-cartesian-hardspheres.json --pair-kind ball
python3 -u "$S/2ecf-polar-released-physical-nonlocal-normal-ball-optimization-line-search.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-true-far-retry-ball-full.json --solution polar-released40-true-far-retry-ball.json
python3 -u "$S/2ecf-polar-released-physical-nonlocal-normal-ball-optimization-line-search.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-true-far-retry-chord.json --start polar-released40-actual-cartesian-hardspheres.json --pair-kind chord
python3 -u "$S/2ecf-polar-released-physical-nonlocal-normal-ball-optimization-line-search.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-true-far-retry-chord-full-r2.json --solution polar-released40-true-far-retry-chord.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-physical-nonlocal-normal-ball-optimization-line-search.py | 98d7ad8844e7ea7cef3c76935aed441dc43353110bb22955e6adee9a42123482 |
| polar-released40-true-far-retry-ball.json | 3ea2cf99e1ec6f24da17525b9d6bcc3dcb8e5d013d9a20fad9756e25965616af |
| polar-released40-true-far-retry-ball-full.json | 285726b4143a88b44e6f400753543d857c109952b8f6c2fb3ac443c84c5404e1 |
| polar-released40-true-far-retry-chord.json | edd2ce472cee871fd8fd29a98fa2a30b411f1c5acb0d47ad935d06d5a35d5223 |
| polar-released40-true-far-retry-chord-full-r2.json | 5e571bb15e69ec88f82cc6b2cc02d35b86e338b5c64924f5845f6667ec93bd66 |
| 2ecf-polar-released-physical-nonlocal-normal-ball-optimization.py | 4f812e79f22345544e91103e05cbb51c78aa62ac06452b8512a48f7ebe0f2196 |
| polar-released40-true-far-ball-exit.json | d05e9d81fb76db149e89ec598fe17351ef86e1275c6cc109ab27489cca33d138 |
| polar-released40-true-far-chord-exit.json | 9af48bbd2cf51488f97626e3529c88e4f0abb2ced2bc7e6a4f6240860a5726ca |
| polar-released40-true-far-ball.log | 826e206445d16ac1123e1ba683a92d0cf1aa981c9e30cbfc3e66b4fc50e166eb |
| polar-released40-true-far-chord.log | 826e206445d16ac1123e1ba683a92d0cf1aa981c9e30cbfc3e66b4fc50e166eb |
| polar-released40-true-far-retry-chord-full-exit.json | f4d14a888ef25d9387f660e56f9381f4b1c4a33b418c484721afe8dddadb777e |
| polar-released40-true-far-retry-ball-exit.json | 5c9aae5723dac433d6453f11532e808cf4e053f5b3776fbd475e8d972caf0622 |
| polar-released40-true-far-retry-ball.log | 5e80dab0519ce08672f2be60716d650dc0bfee241b55eb803705c6faeb154af2 |
| polar-released40-true-far-retry-ball-full-exit.json | f1dd15d71c2a4db0ffc00c042167cc9a3d44c36f4bb37ee96199a867ae90b64b |
| polar-released40-true-far-retry-ball-full.log | f732f66da31f3d658edc21129065db6462e50a4a3bdc1f34547196370c791ca2 |
| polar-released40-true-far-retry-chord-exit.json | fe355cfffbbb9a5dbfde029bd314590b7a16a042878334adce296fe675c0c2e8 |
| polar-released40-true-far-retry-chord.log | 52328acd1cf0118719eda7ae63c78f3f570fa6ea735ae177e597593fcfd62a4e |
| polar-released40-true-far-retry-chord-full-r2-exit.json | c735499f67f45ff443e7c8061267b90b241fd9dd57cf6d50a30b1a06cd45e8f6 |
| polar-released40-true-far-retry-chord-full-r2.log | f4d790afc06f6e0b936d2111874c3351ee298a6e1b7493642268626857a5a249 |
