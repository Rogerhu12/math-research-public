# 固定原度量时十二个延长 coast 与后缀位置的混合

**数值证据。**

沿 R263 的仿射 coast 计算实际 6 个 Cartesian jets，在 b..b+.24 左右的原材料采样上替换 H65 原度量第 1 态。半径始终取原目标的非仿射延拓。新 coast 在该带的单独采样指标为 {'training': {'fullRawCoastMetricVersusActualTarget': 0.0028401030231999247, 'fullRawCoastCurvature': 8.862750167228679, 'sampledRulingMaximumHeight': 0.4210454881455519, 'coastCacheSHA256': '08c43ba5a1710bf0561bee28f3ad412b98c75e875de6f1a78a363eadcc0a4c45'}, 'observer': {'fullRawCoastMetricVersusActualTarget': 0.0028401030232001467, 'fullRawCoastCurvature': 8.862750167228679, 'sampledRulingMaximumHeight': 0.4210454881455519, 'coastCacheSHA256': 'd3af9e5e7d10d4855359bac1f05202be684db0b240514bfd06185d35474efb55'}}。12 个候选在 hold 之后用五次 smoothstep 回接真实原后缀，三参数及全行结果如下。不同强度的候选只作比较，没有优化接受。

| hold | stop | 混合强度 | 完整 G10 R² | metric 峰 | κ 峰 |
|---:|---:|---:|---:|---:|---:|
|0|0.1|0|0.06773158998|0.2534734213|21.02597677|
|0.015|0.12|0.5|0.09706803218|0.4030520291|22.89916485|
|0.015|0.12|1|0.2314979882|0.7104787848|33.69161812|
|0.015|0.18|0.5|0.1248059768|0.447206889|21.4863371|
|0.015|0.18|1|0.4883267675|0.8679248096|28.8702955|
|0.015|0.24|0.5|0.1850470849|0.4718779767|21.73714419|
|0.015|0.24|1|1.261360493|1.01241882|31.32716404|
|0.04|0.12|0.5|0.1535483775|0.6118644128|29.81140149|
|0.04|0.12|1|0.9236586465|1.225947674|49.55650468|
|0.04|0.18|0.5|0.1896298227|0.597579433|23.94627532|
|0.04|0.18|1|1.417608361|1.249368738|35.94758119|
|0.04|0.24|0.5|0.2929931218|0.6062629287|23.88744312|
|0.04|0.24|1|3.198427547|1.354170858|37.46222802|

全 G10 最低的混合候选取 hold=.015,stop=.12,强度=.5，代价 .0970680 高于原 .06773159；该候选 G11 度量 .40149903、κ22.89368。此计算取 literal 坐标的 σ=s−(c+r)，未把 b 端两侧缓存的字节比较充作准确 C² 接合。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-extended-coast-cache.py" --scripts "$S" --ramp "$E/ramp-65.npz" --coast gap105-prefix-coast-master.npz --source polar-physical-H65-prepared.json --group training --length 0.24 --prefix polar-extended-coast-training
python3 -u "$S/2ecf-polar-extended-coast-cache.py" --scripts "$S" --ramp "$E/ramp-65.npz" --coast gap105-prefix-coast-master.npz --source polar-physical-H65-prepared.json --group observer --length 0.24 --prefix polar-extended-coast-observer
python3 -u "$S/2ecf-polar-extended-coast-cache.py" --scripts "$S" --ramp "$E/ramp-65.npz" --coast gap105-prefix-coast-master.npz --source polar-physical-H65-independent.json --group independent --length 0.24 --prefix polar-extended-coast-independent
python3 -u "$S/2ecf-polar-extended-coast-splice.py" --scripts "$S" --prepared polar-physical-H65-prepared.json --state polar-physical-H65-coarse9-step01-state.json --training-coast polar-extended-coast-training-extended-coast.json --observer-coast polar-extended-coast-observer-extended-coast.json --output polar-H65-coast-splice-select.json
python3 -u "$S/2ecf-polar-coast-alternatives-observe.py" --scripts "$S" --prepared polar-physical-H65-prepared.json --state polar-physical-H65-coarse9-step01-state.json --observer polar-physical-H65-independent.json --coast polar-extended-coast-independent-extended-coast.json --mode simple --input polar-H65-coast-splice-select.json --output polar-H65-coast-splice-select-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-extended-coast-cache.py | 42298253273802eda31e115d94debc05dbf7e622c9a1a82a9f17cab021af4915 |
| 2ecf-polar-extended-coast-splice.py | 420a2e118692f6f71d0b7235ffda16141835ec3ef6cacdd6acd38d5e808b02db |
| 2ecf-polar-coast-alternatives-observe.py | 065102bec9ff488ac0a2a840fdaf6ffd521a9d8179c47c17f3291c052289f930 |
| polar-extended-coast-training-extended-coast.json | 08c43ba5a1710bf0561bee28f3ad412b98c75e875de6f1a78a363eadcc0a4c45 |
| polar-extended-coast-training-extended-coast.npz | 5098c6372b86da624db8e46b894513dc984720c34976c53ba92a7fae99df9b52 |
| polar-extended-coast-observer-extended-coast.json | d3af9e5e7d10d4855359bac1f05202be684db0b240514bfd06185d35474efb55 |
| polar-extended-coast-observer-extended-coast.npz | 9fc02ef80578710adc66e9515b0aa6d35a589132fc246e124ed05bd55bf29585 |
| polar-extended-coast-independent-extended-coast.json | a8a215d7710d07c336e6b1eeb82a684d735a4d3d5f82ca05ca0125dc4cab64c6 |
| polar-extended-coast-independent-extended-coast.npz | d108bc5450c3142bf7d63a322715a0e82278e7243093b3b0a7dcf8745b1402b6 |
| polar-H65-coast-splice-select.json | 7f413ba9b9f1535b7de23b7943665340d935faec7cbfc7752967bc4ff07fb3eb |
| polar-H65-coast-splice-select-G11.json | a22c54cf22f1946ac02c7c5dd4d0bab745d8935beed2c392aa33890f1586a03c |
| polar-extended-coast-training-start-exit.json | 468af159b5c3e2e9c10b61723cbe51156832ae96a5c59ba006043b5fcdb4031e |
| polar-extended-coast-training-start.log | 6f7194da65a20f313b3526b2332b47149f927b6bb236c6f0e900540e48830831 |
| polar-extended-coast-observer-start-exit.json | 9176708f06104aad2642aab8b6788732ce25d7acec7671ff0333b16a92b7d0a6 |
| polar-extended-coast-observer-start.log | 99a86b2dd7b73a0ac63d6c325484a1ef571567b93c3972c2474c151623926490 |
| polar-extended-coast-independent-start-exit.json | 1928b5d7fb5badfa79dde914f4cb2a4f36d1def327f05d92f553423877aa7a09 |
| polar-extended-coast-independent-start.log | 7ba51c1bd2fdb2b238c1b21f7c9da80b5510fce0a2fa91cdbd17a0fad9a208c2 |
| polar-H65-coast-splice-select-exit.json | dc65ffd6aa6c1cc793a8b4211316d71f8567dc579ce5ef939bb1c261331d96ea |
| polar-H65-coast-splice-select.log | 2029b1db81d6c9c6ea6ab84530444d70fc640366bb1a933fb018e753a505b3f2 |
| polar-H65-coast-splice-select-G11-exit.json | d9d804c0bb7532aff4005b47a027fe976503d8d730dbc972b4790422fa1673b1 |
| polar-H65-coast-splice-select-G11.log | 126f97385c2575e79471843447c7540464a8270be671bf465e315f7b60cb1ab1 |
