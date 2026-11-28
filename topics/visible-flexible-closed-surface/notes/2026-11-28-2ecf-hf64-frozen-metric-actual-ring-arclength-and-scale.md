# HF64–M80 全后缀的真实逐圈弧长重参和半径缩放

**数值证据。**

固定 HF64–M80 加真实 W 的显式场及冻结设计 3 目标。各材料圈的实际平均速率为 a，弧长加权中心 C。用完整弧长原函数求 v(s,u)，使原参数 0..v 的弧长等于 au。对 β,γ 取表中值，独立构造 vβ=(1−β)u+βv，λγ=1+γ(f/a−1)，空间图取 C+λγ(P(s,vβ)−C)。β改变角参数，γ改变空间大小。R103 的逐圈弧长原理、R233 的整套隐微分公式在这张新的实际全后缀上重新计算，每组都固定同一个 f。准确 b、S 两端有原开放端口的相同 P、P_s、P_ss 的函数迹，按角微分后决定弧长导数。由于端口上原图已经是各自准确目标的单位材料角速率，对于变换两端的角钟和尺度的一、二阶径向修正均为零。前缀及真 tail 的图按原定义接回。
采用同一径向/角向确切物理 Fourier、B 样条和端口的数据源。在 512 与 1024 个角积分点上计算每个实际圈的弧长原函数及两阶径向导数，五次 Hermite 反求材料角；端口的非多项式角函数在每次有限观察中用该阶的独立角采样。两次分别重算全 4291840 行和错移 G11。下表取 1024 阶。F 是产出 HF64–M80 数据的工作目录。

| 角钟插值 β | 半径缩放插值 γ | G10 原 R² | G11 metric | G11 κ | G11 held |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.0 | 0.044540432913 | 0.14343181847 | 28.815157711 | 0.65827509682 |
| 0.0 | 1.0 | 0.19497464385 | 0.34965639645 | 36.099266848 | 0.65057940856 |
| 1.0 | 0.0 | 0.115336464 | 0.2179019266 | 28.815467448 | 0.6582756279 |
| 1.0 | 1.0 | 0.28829740598 | 0.34236267879 | 36.099725414 | 0.65057995957 |
| 0.5 | 0.5 | 0.07585626164 | 0.1980204023 | 32.466132161 | 0.65442750116 |
| 0.5 | 0.0 | 0.055032953046 | 0.15631417157 | 28.815312617 | 0.65827536215 |
| 0.0 | 0.5 | 0.066392996577 | 0.21744799957 | 32.465939898 | 0.65442723089 |

β=γ=1 时，连续模型在准确后缀上按构造有 |X_u|=f。整网格 G 分量的误差峰为 9.8521e-13，此数还包括前缀。完整独立 metric 升至 .34236268，缩放与重参均没有使应付的全指标下降。1024 角的全部三个网格反解原函数残差小于 3.0e−14，实际速率与局部原函数的插值导数差小于 9.5e−10。四个不同半径、七个实际角，另以中央差分核查 X_s、X_u、X_ss、X_su 的两个导法、X_uu，最大绝对三维差 3.2633e-07。中间候选无优化接受，亦无全域连续误差结论。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-hf-actual-ring-normalization.py" --scripts "$S" --hf-entry "$S/2ecf-strong-port-hermite-fourier-background-physical-W.py" --hf-report "$F/strong-physical-hf64m80-W.json" --field "$F/strong-physical-hf64m80-W.json.field.npz" --prepared polar-physical-H65-prepared.json --independent polar-physical-H65-independent.json --frozen polar-H65-two-space-design-step03-step01-state.json --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --quadrature 512 --variants 0,0 0,1 1,0 1,1 .5,.5 .5,0 0,.5 --output polar-HF64-M80-normalize-512.json
python3 -u "$S/2ecf-polar-hf-actual-ring-normalization.py" --scripts "$S" --hf-entry "$S/2ecf-strong-port-hermite-fourier-background-physical-W.py" --hf-report "$F/strong-physical-hf64m80-W.json" --field "$F/strong-physical-hf64m80-W.json.field.npz" --prepared polar-physical-H65-prepared.json --independent polar-physical-H65-independent.json --frozen polar-H65-two-space-design-step03-step01-state.json --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --quadrature 1024 --variants 0,0 0,1 1,0 1,1 .5,.5 .5,0 0,.5 --output polar-HF64-M80-normalize-1024.json
python3 -u "$S/2ecf-polar-hf-ring-normalization-derivative-audit.py" --scripts "$S" --hf-entry "$S/2ecf-strong-port-hermite-fourier-background-physical-W.py" --field "$F/strong-physical-hf64m80-W.json.field.npz" --prepared polar-physical-H65-prepared.json --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --quadrature 1024 --output polar-HF64-M80-normalize-actual-FD.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-hf-actual-ring-normalization.py | 51b6a780060cebcb61d9578e1aee614063ef2c757e8dd95150d14d4889e11077 |
| 2ecf-polar-hf-ring-normalization-derivative-audit.py | 39cd1b4d8a2a03b37b8e6796be55f7bcdb9378a9a9ae9711fab588337443f247 |
| polar-HF64-M80-normalize-512.json | 88d4e2ad4afe8d1c0b8a9e021367b31734b2e59caf4301fc81da57c964f9942d |
| polar-HF64-M80-normalize-1024.json | 38717e9a82658de7e67f2eabac9a0f2806824cf134a12c338b143bd03926fbc3 |
| polar-HF64-M80-normalize-actual-FD.json | c26625345847b894b565b8fccd4a4cdf03ce49e62600ed7e7c41110c771780f2 |
| polar-HF64-M80-normalize-512-exit.json | 2a8756ff155152305d863c9f293c060169a40d37177cda31c744569832aaee93 |
| polar-HF64-M80-normalize-512.log | 8baf8f5e2c74c28855fc0642c0a49bd0453b3e047446bd94e1c37d4282ef9c29 |
| polar-HF64-M80-normalize-1024-exit.json | 4b2f74edffe89b53c2503fcf4d243df0c3c36b364217f15c131f1dc70118bb89 |
| polar-HF64-M80-normalize-1024.log | 5b07fa8a231c95ad8cf5e2c696258f185ca37db4bdac0a7b63c87ba04a7dfd39 |
| polar-HF64-M80-normalize-actual-FD-exit.json | 806059c78d78ce2a36a7424390f1e15c8c2cf58b1c08b58360ae52bb0d58b297 |
| polar-HF64-M80-normalize-actual-FD.log | d6acbf124dcfa4f17ff14d31f38349af3744dfc6b0311bc5333cfffd1a16d691 |
