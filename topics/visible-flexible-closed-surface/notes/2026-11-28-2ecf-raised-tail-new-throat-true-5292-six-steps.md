# 上弯新长喉的真实 5292 位置求解六步

**数值证据。**

固定 R273 的上抬开发盘 A=.4,c=.56 及新长喉度量，初图取上条实际选定的真右端口位置差的全支撑 Hermite lifting，原 W 已加入底场。新增 5292 个后缀 Cartesian 位置坐标，初值为零，自身重新累计。保留完整 4291840 行、原物理 H²、面积、曲率等所有原组；高度 guide 取已定义的新喉窗口。初始原 R²30.9924377、G10 峰 1.11126395、κ121.62875、held .69774362。

| 自身接受数 | G10 R² | G11 metric / κ / held |
|---:|---:|---|
| 1 | 11.274709162 | 1.0436355659 / 78.468017642 / 0.65812163884 |
| 2 | 1.8395275058 | 0.84171525395 / 36.815787354 / 0.64111320301 |
| 3 | 0.53232157594 | 0.58661817364 / 25.160999064 / 0.62552819586 |
| 4 | 0.13342800126 | 0.41985441805 / 20.656505768 / 0.61961949564 |
| 5 | 0.098818921391 | 0.36546028515 / 23.373956112 / 0.61272389113 |
| 6 | 0.079040539223 | 0.36496629685 / 18.301867431 / 0.61274446211 |

六步均按新固定输入自己的实际全成本接受。第六态仍缺闭面需要的同 g 精度、曲率和 held。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode prepare --scripts "$S" --parent polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --donor polar-new-gap-092-fixed-step02-step01-state.json --selection polar-gap092-raised-true-tail-select.json --output polar-gap092-raised-selected-prepared.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-gap092-raised-selected-position-source.py" --prepared polar-gap092-raised-selected-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --zero --initial-damping .04 --steps 3 --prefix polar-gap092-raised-xyz-own1
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-raised-selected-prepared.json --state polar-gap092-raised-xyz-own1-step01-state.json --output polar-gap092-raised-xyz-own1-G11.json
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-raised-selected-prepared.json --state polar-gap092-raised-xyz-own1-step02-state.json --output polar-gap092-raised-xyz-own2-G11.json
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-raised-selected-prepared.json --state polar-gap092-raised-xyz-own1-step03-state.json --output polar-gap092-raised-xyz-own3-G11.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-gap092-raised-selected-position-source.py" --prepared polar-gap092-raised-selected-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-gap092-raised-xyz-own1-step03-state.json --initial-damping .04 --steps 3 --prefix polar-gap092-raised-xyz-own4
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-raised-selected-prepared.json --state polar-gap092-raised-xyz-own4-step01-state.json --output polar-gap092-raised-xyz-own4-G11.json
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-raised-selected-prepared.json --state polar-gap092-raised-xyz-own4-step02-state.json --output polar-gap092-raised-xyz-own5-G11.json
python3 -u "$S/2ecf-polar-gap092-raised-selected-position-source.py" --mode observe --scripts "$S" --prepared polar-gap092-raised-selected-prepared.json --state polar-gap092-raised-xyz-own4-step03-state.json --output polar-gap092-raised-xyz-own6-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-gap092-raised-selected-position-source.py | 91042ab1ab82157dcfd9436982a8512289ba266d6cffb9f7986d09497ed8e1e7 |
| polar-gap092-raised-selected-prepared.json | 47000b283a2753d4fd056c03cd9ba4eb886a1480b3e5924109371fe302bcf7e3 |
| polar-gap092-raised-xyz-own1-initial.json | 53e34be5e738b9c8615cd9d17b8d08327262f5095d3f994a8013d4920bb94d63 |
| polar-gap092-raised-xyz-own1-report.json | 919f1ad268971d9be6cb70d6fbcb9c266e3167dfa8ff23565f0b14650fe9c9cc |
| polar-gap092-raised-xyz-own1-step01-state.json | 9355811c04b8ac54a878dac9b3810866fa348107252cc2abfd01c1452f8878a3 |
| polar-gap092-raised-xyz-own1-G11.json | 354737bfdea633881f0e7166094803f76bf772767e4c223a73b6fa3f3c5c96f4 |
| polar-gap092-raised-xyz-own1-step02-state.json | 10102ad39b6fb724cc09debf1d9550a39425a19f333628c3fc660a8f4daa7942 |
| polar-gap092-raised-xyz-own2-G11.json | 9196cdb4bc42696c96ec5ac82ff93cb84cff20654658a4ba55963a7b3f4df4dd |
| polar-gap092-raised-xyz-own1-step03-state.json | 80ad3f47ab2899fbf47477db8584640acf1730093e3a6e217a283d214a8da170 |
| polar-gap092-raised-xyz-own3-G11.json | 8676085af85e1ea9dc5718bd6e337cf998e51fc3b76662fdb9ec15f2711441b2 |
| polar-gap092-raised-xyz-own4-initial.json | 6500ed7ee7a6d370d8f87e0901601de0d502cdd65b762f4a4f7b9e887feb919b |
| polar-gap092-raised-xyz-own4-report.json | 2521a235e59cc9b2556b3ca9b335b363c6b2f611e8a467b9a0e92635647904fb |
| polar-gap092-raised-xyz-own4-step01-state.json | 61f427f3720597e571288186a8e30e01039417eaa4b879ef43f932e06835a920 |
| polar-gap092-raised-xyz-own4-G11.json | 85ec1c13d502afba532d0293b5efdb4917b40dd80d042f46750bf685e99d3455 |
| polar-gap092-raised-xyz-own4-step02-state.json | 132f707e7c1a98c0e157a25a4e03684c831dd2257b718fd05ff1ad65b264da44 |
| polar-gap092-raised-xyz-own5-G11.json | 86e604cdbd9e81bfbf8ea7c6a40d19fa2fd1e31c477df813a5a2ecafe59d0da5 |
| polar-gap092-raised-xyz-own4-step03-state.json | b9d86950ae21e20b39811872d16c608524cd64bf3ef8f0744129e8ae53614bbd |
| polar-gap092-raised-xyz-own6-G11.json | c1d0b320dedec75c549594b4a44c341afda9f9a6ebbced1b4b96a08672168b87 |
| polar-gap092-raised-xyz-own1-actual-derivative-check.json | 7f9e73115053d4691a140d9be81c340d46d63db638009190af15e4324bc1019d |
| polar-gap092-raised-selected-compose-exit.json | eae3f08b0bde85c27010af42885df0807ff223973a8285551b84338900d71d96 |
| polar-gap092-raised-selected-compose.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| polar-gap092-raised-xyz-own1-exit.json | 66b1a3383b55424e231f451503417e6bb40c1c208e216538ae6898a32978e348 |
| polar-gap092-raised-xyz-own1.log | 90b3e2695d73496d7da3814d59dbff10da673c6b082ba14f74c121ce7e8a4fee |
| polar-gap092-raised-xyz-own1-G11-exit.json | fd10e1cda3a030bc11b29b3d6c3952e9622c5d97f6031ead52111d2b09fb1a81 |
| polar-gap092-raised-xyz-own1-G11.log | b81719defd41c6b03b62333eeb9a98701eb17bfda436757e1c192ba99314fa81 |
| polar-gap092-raised-xyz-own2-G11-exit.json | c0a9ad95755889132c58df50ca828349322682b5d7b3d776ef64bc3134e4a3a8 |
| polar-gap092-raised-xyz-own2-G11.log | a4b0300ee6f634ace1c5cba6beb64cb57a1e3fbfc2bcc13d431301f69e2b2ade |
| polar-gap092-raised-xyz-own3-G11-exit.json | 9d0633072e73540920875dc31a83840d43a6b81de24a4346e56a89d2f079aaea |
| polar-gap092-raised-xyz-own3-G11.log | c8cd350c93479eb07f06c7abf20d3069a167706d4c6264ff3a06e9b3446af09e |
| polar-gap092-raised-xyz-own4-exit.json | 48d90293aeffec4572b140be2e1a69da354007dda201be09d0a321ce5f128d4c |
| polar-gap092-raised-xyz-own4.log | ceed897ea913e7e6a64caaee426744c2606f08cfed97522e022f9f507730207a |
| polar-gap092-raised-xyz-own4-G11-exit.json | 2024e500b01fe10292ff409887a136e3a1eb4c289d1d815d022ac001e960432d |
| polar-gap092-raised-xyz-own4-G11.log | fbc9810431cbad48f9eb04bd443b6e01b13276f1f03bcbc0d3bdced059f874f9 |
| polar-gap092-raised-xyz-own5-G11-exit.json | 98bee3ff3d316927ea941b721e14602c54515c0756793cfd545e18df2a7da6b7 |
| polar-gap092-raised-xyz-own5-G11.log | 6e38ef00042bc117182cfc6062529d7e3739d09f0d5fadae1300fff6b94da8d0 |
| polar-gap092-raised-xyz-own6-G11-exit.json | d51f649da6af3dc8b1ac1eb8b9b9e3c581ff9aa6f83e3a627d73bae822e14c25 |
| polar-gap092-raised-xyz-own6-G11.log | d782b48fcbd54fa08cf68df79fc1178af8fca9d4ad0fdded52c6e4027c56c01c |
