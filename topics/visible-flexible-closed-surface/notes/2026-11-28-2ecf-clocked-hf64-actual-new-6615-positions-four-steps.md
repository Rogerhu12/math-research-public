# 角依赖径钟 HF64–M80 上的完整 6615 个新位置变量

**数值证据。**

使用 HF64–M80 连续位置、其中完整既有 W，以及真实角依赖径向材料钟 T=s+h(s,u)。固定原设计 3 的 36 个度量系数，目标定义 SHA256 为 52902e395f030eb515a7906e7c35993d05525f7bdbafd24137cf2d676818b55f。在钟换后的场上新增全部 6615 个 Cartesian 后缀位置系数，所有自由度初始取零，独立开始累计。实际 G10 两组和 G11 全六 jets 均从源的完整链式法则求值，并对各整个阵列作 SHA。前缀保持真实 H65，基础 W 与钟皆保其两端空间两 jets。下表仅为这个新固定 g 输入的观察。
训练用 4291840 行，保留原全部 13 种物理/几何列及 Q2 面积，完整物理 H²。优化度量采用 sextic 加权，曲率保留原阈值并将光滑谱聚集的 τ 从 1000000 改为 4；每个真实接受态同时重算原 quartic/原 τ 成本。线性化与矩阵转置在当前新源实测，相对导数差 2.50828e−10、adjoint 1.15699e−15。独立 G11 的 668×256 个点用单独 Fourier 评价。

| 自身接受数 | G10 新 R² | G10 原 R² | G11 metric / κ / held |
|---:|---:|---:|---|
| 0 | 0.21640332698 | 0.053314330373 | 0.12051274343 / 28.824819856 / 0.65827430317 |
| 1 | 0.11494839342 | 0.036639330541 | 0.14509304992 / 24.300214961 / 0.65487257586 |
| 2 | 0.085121867617 | 0.030500436471 | 0.14713605108 / 21.160399743 / 0.65245153199 |
| 3 | 0.073294559025 | 0.026485052869 | 0.1526239915 / 17.363851159 / 0.64950713057 |
| 4 | 0.071275653342 | 0.025788381082 | 0.14978020812 / 17.496853451 / 0.64599298144 |

四个真实接受均按新成本取得。相对初始钟图，曲率峰从 28.82482 降到最低 17.36386，度量峰反而从 .12051274 升到 .14978021（末态）。末态 held .64599298 也低于原内部 .65 guide。整闭面及同 g 收敛结论均未达到。F 是产生 [HF64 物理场及真实材料钟](../scripts/2ecf-strong-hf-material-radial-clock.py) 的目录；在下面的命令前先重生该场、径钟及 H65 G10/G11 原源。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-clocked-hf-source.py" --scripts "$S" --field "$F/strong-physical-hf64m80-W.json.field.npz" --hf-report "$F/strong-physical-hf64m80-W.json" --clock-entry "$S/2ecf-strong-hf-material-radial-clock.py" --clock-state "$F/strong-hf-physical-radial-clock01.json" --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --parent polar-physical-H65-prepared.json --independent polar-physical-H65-independent.json --frozen polar-H65-two-space-design-step03-step01-state.json --output polar-HF64-clocked-prepared.json
python3 -u "$S/2ecf-polar-clocked-hf-xyz-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-clocked-hf-source.py" --prepared polar-HF64-clocked-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --frozen polar-H65-two-space-design-step03-step01-state.json --zero --initial-damping 0.03 --sextic 1 --curvature-tau 4 --steps 1 --prefix polar-HF64-clocked-xyz-step01
python3 -u "$S/2ecf-polar-clocked-hf-xyz-observe.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --state polar-HF64-clocked-xyz-step01-initial.json --output polar-HF64-clocked-xyz-baseline-G11.json
python3 -u "$S/2ecf-polar-clocked-hf-xyz-observe.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --state polar-HF64-clocked-xyz-step01-step01-state.json --output polar-HF64-clocked-xyz-step01-G11.json
python3 -u "$S/2ecf-polar-clocked-hf-xyz-solve.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --prepare-entry "$S/2ecf-polar-clocked-hf-source.py" --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-HF64-clocked-xyz-step01-step01-state.json --initial-damping 0.03 --sextic 1 --curvature-tau 4 --steps 1 --prefix polar-HF64-clocked-xyz-step02
python3 -u "$S/2ecf-polar-clocked-hf-xyz-observe.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --state polar-HF64-clocked-xyz-step02-step01-state.json --output polar-HF64-clocked-xyz-step02-G11.json
python3 -u "$S/2ecf-polar-clocked-hf-xyz-solve.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --prepare-entry "$S/2ecf-polar-clocked-hf-source.py" --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-HF64-clocked-xyz-step02-step01-state.json --initial-damping 0.03 --sextic 1 --curvature-tau 4 --steps 1 --prefix polar-HF64-clocked-xyz-step03
python3 -u "$S/2ecf-polar-clocked-hf-xyz-observe.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --state polar-HF64-clocked-xyz-step03-step01-state.json --output polar-HF64-clocked-xyz-step03-G11.json
python3 -u "$S/2ecf-polar-clocked-hf-xyz-solve.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --prepare-entry "$S/2ecf-polar-clocked-hf-source.py" --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-HF64-clocked-xyz-step03-step01-state.json --initial-damping 0.03 --sextic 1 --curvature-tau 4 --steps 1 --prefix polar-HF64-clocked-xyz-step04
python3 -u "$S/2ecf-polar-clocked-hf-xyz-observe.py" --scripts "$S" --prepared polar-HF64-clocked-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --state polar-HF64-clocked-xyz-step04-step01-state.json --output polar-HF64-clocked-xyz-step04-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-clocked-hf-source.py | a0892415fb9d2aa0fe86024515eecc911406b5c78dbe2f68dc80d50e12fabd20 |
| 2ecf-polar-clocked-hf-xyz-solve.py | 7ce980257d47a31f98e2a789a68a7a7f803d77d7088ee95d4addc8c35c526764 |
| 2ecf-polar-clocked-hf-xyz-observe.py | dae6c3b281cf4bee9aa64df462db7c377e82c40b037950edc62a9c98e50a5968 |
| polar-HF64-clocked-prepared.json | 8f733b83bf5edb38cd990a88c886ba18bcf2f0e60efffb7f6d5b98c447145569 |
| polar-HF64-clocked-xyz-01obs-04-driver-exit.json | 8183a82f92fcca5367d861c0a04e6d68f5a6debdd31f4632e9e86d94ea7b10c5 |
| polar-HF64-clocked-xyz-step01-actual-derivative-check.json | 7203bd717de1f3c678dbbc24eda59d0b3d83cc909ff5bec5bff70a526e7688a9 |
| polar-HF64-clocked-xyz-step01-initial.json | 4c92e8807e4368a752b999a9bee33eb7353be2525d8f4b486135fafcad688b9c |
| polar-HF64-clocked-xyz-baseline-G11.json | 6882bb9377e8c22a8076ffb555512cc096c0e8f54610b0d581cd1fc5d389a744 |
| polar-HF64-clocked-xyz-step01-report.json | 2506e27729756550fa4876cb3897997424d73d8ef744d8bf8bfc3da19d0f2326 |
| polar-HF64-clocked-xyz-step01-step01-state.json | 4940848d2df4cb6119511df2f9b767b1bb1442cef89bff2737375cc529b18bdb |
| polar-HF64-clocked-xyz-step01-G11.json | 1a15c11668bcc66ef26e8c12fe0577a622aed24958ea5ee97e7e9cdf39864c25 |
| polar-HF64-clocked-xyz-step02-step01-state.json | b9128f229a3e507df070d558e8da24b18077c8382d27e7a97a8f7efe7e75d2cd |
| polar-HF64-clocked-xyz-step02-G11.json | 30093e600d9953a3449274b3ecfa7336951874bee3e12ca50a043ea2cea3d463 |
| polar-HF64-clocked-xyz-step02-report.json | a76363a63f74a08b4560ba805ccfe12f09db466e2690e91d7469f09ff16e3c7c |
| polar-HF64-clocked-xyz-step02-initial.json | d0750bfbb6fd836802af1c9fd5cc914969352e507250272fb02d8225612330eb |
| polar-HF64-clocked-xyz-step03-step01-state.json | bf6fcb21bd1ff8ee830c3e6e054667bface063c1d7486171355d003e20a4b0d5 |
| polar-HF64-clocked-xyz-step03-G11.json | b36e7195e8707dfb345e78a2ac345a48426cbdc9fc21ad3b2f5ed7b6a27a902f |
| polar-HF64-clocked-xyz-step03-report.json | 26c8945fb60b205e34417e6a4bb842f8cbc80518ad9e0cdf6789fb3e6d8542ad |
| polar-HF64-clocked-xyz-step03-initial.json | e1d869ce8e8086c89d422004629cf60d0dc278be151631390f9626e86fe14281 |
| polar-HF64-clocked-xyz-step04-step01-state.json | 2f9e6f2e9c7440f22b8c332fca7bdc1257daa57c21c0472bf8d2a5e91f6ead0c |
| polar-HF64-clocked-xyz-step04-G11.json | fd5b93e91369962687b5ccb54994bf7bfa4d8b3ac7ce80ab6f5ef25733991f38 |
| polar-HF64-clocked-xyz-step04-report.json | c5a4711dca440cc1c165bd11a5711866432215749ce5eba06fe16524e8b27707 |
| polar-HF64-clocked-xyz-step04-initial.json | b0d6d9b98c6c34333b4babb26d49f02ec4844a876a8715d75a84e51f1a03d736 |
| polar-HF64-clocked-compose-exit.json | 521bdfca22d1d55b210b339a0315ed5d5dd710cb5481899140ff4f1f83897663 |
| polar-HF64-clocked-compose.log | 16d2911e5e29aca76079eff46d231accda13c0a70d02a2c93f1e8aa6ef697f24 |
| polar-HF64-clocked-xyz-step01-exit.json | 5f74a287018343268c1614369fa8385953bc5468e86d7803f924c176824e3a65 |
| polar-HF64-clocked-xyz-step01.log | 82d4469f58d83f7e954af8af56977f7bebf4fa81584e3b242181341b026d5585 |
| polar-HF64-clocked-xyz-baseline-G11-exit.json | 2dd1cb0404db5b4b522a222f341956041fc7db4ece824dada359863f1737d839 |
| polar-HF64-clocked-xyz-baseline-G11.log | ea44b514dafec5bb7819d7692fcabb8963bb49fd640fe8e1337c7e14ae258543 |
| polar-HF64-clocked-xyz-step01-G11-exit.json | bbea7ed6df605745a6019a7649eee730e40ebba178f5a787b76176c0c80ae007 |
| polar-HF64-clocked-xyz-step01-G11.log | 73a2713af33ca85a59f7387228ad2f26e8d00e25c6a26e63f5e1e81a7492c15d |
| polar-HF64-clocked-xyz-step02-exit.json | e0348fb2e52cb535c00f6b5689ed4795c53d1b42971c8080077956ceedf45189 |
| polar-HF64-clocked-xyz-step02.log | 81d806f2ca300918fbd40dc404f9c1c2e99d337858796518869f6ae8eb9ca4c8 |
| polar-HF64-clocked-xyz-step02-G11-exit.json | a8a2e5535ae9cc3b9269412236f11406f4347291a45b901893347c468dba6fc2 |
| polar-HF64-clocked-xyz-step02-G11.log | bd86f7783c502a7b5e131d767b7a2ebc9c8f992d99e882c7453f04896064ffc6 |
| polar-HF64-clocked-xyz-step03-exit.json | 5bc8af0ac83a7325c60f7a65ca9e40c4409f4251ef9366f6c4a3222b09cf9395 |
| polar-HF64-clocked-xyz-step03.log | 85638bca412aba4b9524402fbcf59bb6355c3d6ff1dd4924600e68b648773421 |
| polar-HF64-clocked-xyz-step03-G11-exit.json | 52c6558035f068aec07b7b8678c91bda793920f100f90692e85b91138bfea70a |
| polar-HF64-clocked-xyz-step03-G11.log | 1b0d4c1aa215fbacfab600a40021f60bf93e3d07f9b962ea2c4df80d3faa97e1 |
| polar-HF64-clocked-xyz-step04-exit.json | 9d8344ac90c89f4a06f928e92c88501725f89421f950f513782c5e93724ee1a1 |
| polar-HF64-clocked-xyz-step04.log | b0a22f02d141708e1fa94fdc5d412d4e1d9af8c22ebba1499b4f2592b7e99397 |
| polar-HF64-clocked-xyz-step04-G11-exit.json | 5107b51202f1b31aa0cf569e9ba69135b297fefb59aa66c6ad90e32bee3125fa |
| polar-HF64-clocked-xyz-step04-G11.log | c85d5527b1f7827f387fd0c3caee88668d5e6d85657c161425dea32ec64e4b8a |
