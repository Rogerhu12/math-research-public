# 33 与 65 个物理节点的真实前缀接入完整 G10/G11 源

**数值证据。**

原准确 17 节点使用 R233 的归一化数学源；两新源取同一完整 Cauchy IVP 的 33/65 个物理位置节点及空间端口，在原椭圆材料角中直接采用完整 raw Hermite，终格用同一 Γ95 coast 端口。未改变目标半径。17→33 包含由原归一化源转向相同目标的 raw 候选，33→65 是同一 raw Hermite 配方的实际物理加密。
输入两份新 master 的 SHA256 分别为 4fcc0542ddf34674672556a85608ac0ab56c8b34f3bd81451f6c7b75e99f0544 与 479dab51bd77a211f64a256bbb16d67b4382e150af0deee7fa6baf84d8e5464a，coast master 为 f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d，原 G10 prepared 为 de75e9632855bc3547e174d7e1bfcefaa295d01dbe151d1c087ff0d83682df80，原错移 G11 为 9681d300b461ca13cd0f357a568d487c98ef3d15fbd45917221dd861ed254ed6。
每个网格严格在 c<s<c+r 的行上用 WarmMaster.jet(s,u) 替换 6 个实际 Cartesian jets。其他节点和每个目标半径、角、权重保持原字节。两中央/终端 ramp 端圈逐项和实际取值比较，保留每个误差，不把双精度比较当成完整准确端口证明。数值 b 为准确 c+r+l 减 3/288230376151711744，固定后缀算子依然使用原浮点 b；数学接合还要绑定真实端口的坐标。以下是实际固定 g 的有限采样峰，非整个闭面上界。

| 实际物理源 | G10 128角 ramp 峰 | G10 192角 ramp 峰 | G11独立256角 ramp 峰 |
|---|---:|---:|---:|
| 17 | 6.981399491847435e-08 | 6.981399491847435e-08 | 6.760159413932205e-08 |
| 33 | 2.067076509959573e-09 | 2.067076509959573e-09 | 2.190184380138336e-09 |
| 65 | 6.771181947994723e-11 | 6.770279944547758e-11 | 6.322532082407464e-11 |

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raw-ramp-source-compose.py" --scripts "$S" --parent-prepared polar-c2-G10s-prepared.json --parent-observer polar-independent-G11r-shifted256-independent.json --ramp "$E/ramp-33.npz" --coast gap105-prefix-coast-master.npz --prefix polar-physical-H33
python3 -u "$S/2ecf-polar-raw-ramp-source-compose.py" --scripts "$S" --parent-prepared polar-c2-G10s-prepared.json --parent-observer polar-independent-G11r-shifted256-independent.json --ramp "$E/ramp-65.npz" --coast gap105-prefix-coast-master.npz --prefix polar-physical-H65
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-raw-ramp-source-compose.py | a57dc860c6c92c04af9a7204ea1a8eda06eb4ae290d2ef62b8364cb2c83638f3 |
| polar-physical-H33-training-source.json | 83167dd2b742a126dfa3c814c83c53242e2854b5d7acb1164752bfa78c32de1b |
| polar-physical-H33-training-jets.npy | befbbcf3420b13efc9a0d920c1e01a5d59e9d6c1002f6584e5a7b21315dda4e4 |
| polar-physical-H33-observer-source.json | 0ca40d78cd7f68f1edd693c8e285ef273413fc26e4dcdf2256cd6de4867a93d2 |
| polar-physical-H33-observer-jets.npy | 10d9698ab580996cfabd318d49363769f4166026fc0f0cbc992a479e7f388223 |
| polar-physical-H33-independent-source.json | b570a1e77352cae319bf4694bcb95c9debc898e7e54af76a0979115ea1f88d8d |
| polar-physical-H33-independent-jets.npy | b54b0b93bef3625dfaf39fed6c775b88c831baa8f5857ce403ee8b758c1fa4d8 |
| polar-physical-H33-prepared.json | 957652be72f0228a7b3bab1d2efabf68c2bd08e88d4852731418c20546b7fa12 |
| polar-physical-H33-independent.json | 8662be3ded90db2de15afd5473960606e97fe51b33a688a5b4fedeafd8e47393 |
| polar-physical-H65-training-source.json | 9f90c82416c40edb2cabe39ab02426eb51ccad6a48e01f3c7ef6da15d8328c73 |
| polar-physical-H65-training-jets.npy | 44b502247bcbb3aa37e776b268727504274a142550bc83831eaa767f555cfd1c |
| polar-physical-H65-observer-source.json | 8fc33a17ee9659356605c8ef103547da281496134bde1660000869ba1b151662 |
| polar-physical-H65-observer-jets.npy | b55023989389e3e89622d2a6ab705efed67fb3ab39a6158bb44f8d6e0a929ed5 |
| polar-physical-H65-independent-source.json | 647e6e8e9a7c08261c62b0652fa4a56e98aac0eb760e0b42a376817b9cfc2e36 |
| polar-physical-H65-independent-jets.npy | baf348a10c0ba7995d470b652389126c4dde887caaa5dc2be5e7119ea697e91d |
| polar-physical-H65-prepared.json | 8d9e74861e74b19532f006b7b4cf2e3076d0127fe63530e5d99bd22b10d27f86 |
| polar-physical-H65-independent.json | 5bb17709d1a3d1ac7719c82e10ce515ab73cac3c3256d6f1a21b7fbb9a36ff7f |
| polar-physical-H33-compose-exit.json | b74171c1eb2aed175c1751ff5466b39ed9edee3c070fe19275440a04850780f3 |
| polar-physical-H33-compose.log | aaa765af347c361f3c88e4edb30594b2da9a64f495c7c72a9fe3470cc6517421 |
| polar-physical-H65-compose-exit.json | d9b66ed75ed7b4137d6700142ebe51c8f4ff5d67b512225c7ac5b82549258119 |
| polar-physical-H65-compose.log | 7c2d08b5c482e5520573ddfc11642ef1db0f4faeda8b161021c4eda53eb84506 |
