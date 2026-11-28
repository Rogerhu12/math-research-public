# H65 准确前缀固定后的两空间后缀设计六步

**数值证据。**

整个原 central、H65 ramp 及 coast 的位置和原目标半径均固定。上一 H65 原度量 5292 第一步的坐标经 Boehm 嵌套转移提高到 45×147=6615（存储后的真实系数定义本分支起点），另用原有 36 个 clamped 基函数设计 log 半径，并按实际双精度零系数自身建立起点。任意改变半径的接受态分别定义不同度量。径向位置的嵌套图写作 E，非线性半径直接以粗空间评价。完整联合正规方程把 E 乘入物理交叉块和半径块，保留未截断的 36 维 Schur 补。每次回代均用完整 4291840 行及全部导数物理验证。全 G10 耗散是原四次 metric 项、原曲率/几何、Q2 面积的和。六次更新各有独立错移 G11 原场观察。

| 自身设计步 | G10 原物理 R² | G10 metric / κ / held | 独立 G11 metric / κ / held |
|---:|---:|---|---|
| 0 | 0.067731589977 | 0.2534734213 / 21.02597677 / 0.705839455 | 0.2542957153 / 21.15640707 / 0.7059725611 |
| 1 | 0.061385311897 | 0.296597756 / 28.04822361 / 0.7018140035 | 0.2898257426 / 28.04004972 / 0.7019561015 |
| 2 | 0.054152891555 | 0.2087309756 / 26.57531853 / 0.6838027034 | 0.2048120796 / 26.6027697 / 0.6839223791 |
| 3 | 0.03087617423 | 0.1978599038 / 18.16122768 / 0.6794808111 | 0.2021727736 / 18.04138868 / 0.6795950955 |
| 4 | 0.02829768431 | 0.1976208851 / 18.92372036 / 0.6712514271 | 0.2014259521 / 19.00807718 / 0.6713636969 |
| 5 | 0.025819298834 | 0.197974449 / 18.60858391 / 0.6634202966 | 0.201217391 / 18.49959271 / 0.6635248678 |
| 6 | 0.024039088838 | 0.1972300359 / 20.10238801 / 0.6548389792 | 0.2000211396 / 20.8681886 / 0.654946089 |

联合 adjoint 相对误差 4.733e−14；中央差分在 epsilon=1e−6、1e−7、1e−8 的实际相对误差为 .0182200、.00744999、2.608e−9。第六态独立最坏度量位于 s=.1873601164,u=3.15386450，曲率峰 s=.1998762154,u=1.58306817。各态为有限采样，强闭面目标仍开放。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-H65-two-space-design.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --warm-state polar-physical-H65-coarse9-step01-state.json --initial-damping 0.007111111111111111 --steps 1 --prefix polar-H65-two-space-design-step01
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step01-initial.json --output polar-H65-two-space-design-baseline-G11.json
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step01-step01-state.json --output polar-H65-two-space-design-step01-G11.json
python3 -u "$S/2ecf-polar-H65-two-space-design.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-two-space-design-step01-step01-state.json --initial-damping 0.007111111111111111 --steps 1 --prefix polar-H65-two-space-design-step02
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step02-step01-state.json --output polar-H65-two-space-design-step02-G11.json
python3 -u "$S/2ecf-polar-H65-two-space-design.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-two-space-design-step02-step01-state.json --initial-damping 0.007111111111111111 --steps 1 --prefix polar-H65-two-space-design-step03
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step03-step01-state.json --output polar-H65-two-space-design-step03-G11.json
python3 -u "$S/2ecf-polar-H65-two-space-design.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-two-space-design-step03-step01-state.json --initial-damping 0.007111111111111111 --steps 1 --prefix polar-H65-two-space-design-step04
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step04-step01-state.json --output polar-H65-two-space-design-step04-G11.json
python3 -u "$S/2ecf-polar-H65-two-space-design.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-two-space-design-step04-step01-state.json --initial-damping 0.007111111111111111 --steps 1 --prefix polar-H65-two-space-design-step05
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step05-step01-state.json --output polar-H65-two-space-design-step05-G11.json
python3 -u "$S/2ecf-polar-H65-two-space-design.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-two-space-design-step05-step01-state.json --initial-damping 0.007111111111111111 --steps 1 --prefix polar-H65-two-space-design-step06
python3 -u "$S/2ecf-polar-H65-two-space-design-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-H65-two-space-design-step06-step01-state.json --output polar-H65-two-space-design-step06-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-two-space-radius-schur.py | 18ed2fabd37f94fa8381782d80b0ffb5822b87f7056fded3a4a1901ed0a696fe |
| 2ecf-polar-H65-two-space-design.py | 78dc7e6567c62d7ef843a0bc447fc6e5771b61336db16060f006e046bedd90dc |
| 2ecf-polar-H65-two-space-design-observe.py | 93b1621674c1d485dfe8898c09af954c6d8f45a9dbbe530bdffd2b2d6ac55f96 |
| polar-H65-two-space-design-baseline-G11.json | db0975f54851b2639fab765d94062e113d360752fa1819829b45b6414eae6158 |
| polar-H65-two-space-design-step01-actual-derivative-check.json | e5d471a2e2982670598a647ed593e89012e5cd40f9b75f03c3b8deb5c3849fc4 |
| polar-H65-two-space-design-01obs-06-driver-exit.json | 6514b47d8139319d7f7d2213e0712586a1d9f725250f9a7b28d2837d14ceb6cc |
| polar-H65-two-space-design-step01-initial.json | d02c39dab4e1a16e1e44f60f764b02f4ab4ac91537993bd04eaa9846094bcb80 |
| polar-H65-two-space-design-step01-step01-state.json | 27373ce7dba732e88d0b4a557f3e301e76624e13bb50738dead7bad1b3a6720f |
| polar-H65-two-space-design-step01-G11.json | cf32954e9bba38607ae8aea22618e05573a24d2a57419dce293cf9389324280e |
| polar-H65-two-space-design-step01-report.json | 9f36b4f0d38e02c9bf0027d1bf3a1e08b5943309295fc0b8bf8e39d90e82a174 |
| polar-H65-two-space-design-step02-step01-state.json | ac48ba62c6eee05598edb5c5dd7c69cfd047e58cf818bb7060e13eb7bfed2141 |
| polar-H65-two-space-design-step02-G11.json | bd89a8cd61c5538c9866ca60898f1649a960d2acb0442fe3e28a7d0f54b13014 |
| polar-H65-two-space-design-step02-report.json | bd80648363d916beb70bdc6f4902714f4ce5a5b0d790273f16e7088af8462322 |
| polar-H65-two-space-design-step02-initial.json | ea6dbfc1bf86262453af8d6eb06609b5724f4c1494ecaf566198cce3708e2465 |
| polar-H65-two-space-design-step03-step01-state.json | b3f45552b07e8d9587c4ec05ea02fb749c3ed63beddda11f222c90bfc7b35c11 |
| polar-H65-two-space-design-step03-G11.json | 07eab4e8f69eead134c9e2c2cabf5d5a0f1d0af3e3fcb41e1dbeaf41fec3c447 |
| polar-H65-two-space-design-step03-report.json | a680e7eef9e440bb1a9eaf5b2f3abb5cd312a303fe9cf458db312226054af4ba |
| polar-H65-two-space-design-step03-initial.json | 98509ac25f9d5feefe0a2674af2a0fb793ca4cfa0aaa5562d38d878782669e83 |
| polar-H65-two-space-design-step04-step01-state.json | 5134a5d76986c042fda35a1f5b27b445822c7567b7f78cc548e9ee23236368d4 |
| polar-H65-two-space-design-step04-G11.json | 3b30e4f7177909af8e7cdd0a525cbddfa52c24dcef4a97591745043858b66e5f |
| polar-H65-two-space-design-step04-report.json | eca5d4b6b06cb87139953c90e54dbfb71d52f45e04b4e0157090d313f3db1a74 |
| polar-H65-two-space-design-step04-initial.json | 5cef815e5a77d1050d1ae5558f0e44e9bf081c0702a236441c9fe3574eb02f66 |
| polar-H65-two-space-design-step05-step01-state.json | d385989d68277ba41522dc24830d7324e1c5d950ac9d34511f7677ce1afa333e |
| polar-H65-two-space-design-step05-G11.json | c590e8e507e5d3207996360600d6438d30bc2db083ed87217bfead8842e92a2a |
| polar-H65-two-space-design-step05-report.json | b663827268bad0a72baecf64c64ea6781540449f9c7fe2cbb82c94a109519793 |
| polar-H65-two-space-design-step05-initial.json | 452dac86b945d69bbd446d0b5e364e836f6923048c669aa60a051d5d11d4bf8b |
| polar-H65-two-space-design-step06-step01-state.json | 62e236aba1d4926c5bfd3d74ea2d4ae41e21428e18a141b21372df49f4093f8d |
| polar-H65-two-space-design-step06-G11.json | 58ae4bed7a47c334c79f6417638879b20942378d05e198980f672887f45fa44b |
| polar-H65-two-space-design-step06-report.json | 1121d687b395cc4c8472a5bf17ef23ae00dbb89b5b16bf1c2cc09c65c3fb1209 |
| polar-H65-two-space-design-step06-initial.json | 186d8082ca08ce21248efedcd0336e86cf206bca3b0a479103427f6c8788d26b |
| polar-H65-two-space-design-baseline-G11-exit.json | 42971d1652c07292dd9a38024dc2f8ede7d6a6efcf419d6725054c69de813b6d |
| polar-H65-two-space-design-baseline-G11.log | 25e717eb8d3adc57fdf8a75ab2681250360196b5daa30c651be9c85f2c639cc9 |
| polar-H65-two-space-design-step01-exit.json | 943e95940c7e17bde42cf3cb21205f9e0554d70e25a5ec32727b32c5d6a7609c |
| polar-H65-two-space-design-step01.log | bcca8a5f182a4ffc87a3e1e64795acc20d2ff1700e621899865bd32cadac65f3 |
| polar-H65-two-space-design-step01-G11-exit.json | 27253cb5a31e2c931fffc02083c55e95cf0a94e3f3a02b49d9fa5a7745c62dda |
| polar-H65-two-space-design-step01-G11.log | ec1d9aea190d0ef29972b21d5f4d971a687de97f2d6c66811b829493896c5d52 |
| polar-H65-two-space-design-step02-exit.json | 0a98011b712af325885ed77b1b9a59bbf07edd9cc74a45e2ea6bf3840e3caf83 |
| polar-H65-two-space-design-step02.log | 089b139e5bfe5a79467c9a123390546847c416f01a62b2eb3e89ea842f162312 |
| polar-H65-two-space-design-step02-G11-exit.json | 7933697f897b746f179cc2cdf57a85a7d592b31fea04d2344bb7c8b4827344ae |
| polar-H65-two-space-design-step02-G11.log | f18fb83de703870cb04015e0301ee0129b5e192732fbd6be569bd1959afdaa72 |
| polar-H65-two-space-design-step03-exit.json | 6a853310560657d660600e1aef501e1ecfc7c7f7160aa7c7adc7ad1e905887e7 |
| polar-H65-two-space-design-step03.log | 780d2c3e8dae137f6582bfcc50c6bfe9beea181e84392b12d95628b945cd32a0 |
| polar-H65-two-space-design-step03-G11-exit.json | e42408bbc4660e120fb3ba43cba99f8ba6cc30b82fde5b7aabe96b9126500dd8 |
| polar-H65-two-space-design-step03-G11.log | a2c05bddc5c47e887f57acb4b2d01e306cc52033c97a1e965217ff127952a096 |
| polar-H65-two-space-design-step04-exit.json | 1762f2c63ff77fbad6a64e04a5d59e110b3e430752d9ed3653a1fedfed6c80e8 |
| polar-H65-two-space-design-step04.log | 36c3d6dc7a56bfc101d561f7afa606d8c0da4172bdf5f288ed43841fab141dd4 |
| polar-H65-two-space-design-step04-G11-exit.json | 92add53bbfcf142eb8d8d51240764cd952be41f0b80ccb901f456512a5a9b5d3 |
| polar-H65-two-space-design-step04-G11.log | c5359a6e609a329b7f883042a270b5c58e705b9f0f044b1fe11ca482bf0e09d4 |
| polar-H65-two-space-design-step05-exit.json | 7faaa9ae6cd75af59889081dcd21f1df8b27a05c62e60e9dc9721c7cd7f4a72f |
| polar-H65-two-space-design-step05.log | bee3d4ab6be39c10a378697f7720a2dfa2c0e4608acd4b2e3defd9bc62183166 |
| polar-H65-two-space-design-step05-G11-exit.json | f5d6a8d22a9f32cfa0fe32ec209712b5fee4d8adb139d3eeaa1906e55ceae635 |
| polar-H65-two-space-design-step05-G11.log | 62d185437593595fbfe1720dce5f0acdc8689fdb7321ce674b82a22b6fc9a0a6 |
| polar-H65-two-space-design-step06-exit.json | 48121b3c625eaeafa725e74e81abd261b397d9236ef8380263144188a6c257f0 |
| polar-H65-two-space-design-step06.log | 008099a0851f7605971fec0b2bf0c50b3edba20f63636cef6bf2a39ad4d3ff8d |
| polar-H65-two-space-design-step06-G11-exit.json | 7ea37c47ef5299b40269b0776bcf8a2066b235b1e20b12a45e08b0e5763c9572 |
| polar-H65-two-space-design-step06-G11.log | b34e8dc28f5ee0a56d8e3d6f7882f6a2c398ea1dec4958b61dd5425d258335ff |
