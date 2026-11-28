# R272 已加帽全闭图的首个显式双侧管半径

**准确有理与区间证明。** [R277](../results/R277-first-explicit-full-closed-normal-tube-for-R272.md) 给同一 HF64 真修正、上下全 R205 与 R210 完整帽一个明确的全相位非局部双侧管。无需再检查 R272 已支付的 1331200 个有向势闭盒。HF64 全部 108 个共同元消费 Bernstein/Fourier 范数；非多项式真 Γ95 边额外算 512 个闭 native 角盒的三类二角阶。全图近弦沿单条材料圈的角弧与同一空间射线分解，内部锥、真实平盘极点及与新帽所有点对分别覆盖。
完整已加帽的实际图 reach≥1/27224130085289464320000000，归一化 reach/D≥25/2093972030865744073081567488。数量级分别为 3.67e−26 和 1.19e−26。此保守值没有达到 .03D。F 是重生 [R272 原真全图](../results/R272-actual-full-corrected-HF-kernel-and-fixed-cap-strong-shape.md) 及 R270 非多项式端口差报告的目录。

## 可移植重生

W 含原 gap1.05 的两个 master，F 含上述 R270/R272 数据，S 是公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-r272-edge-second-angular-bounds.py" --scripts "$S" --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --output polar-R272-new-edge-second.json
python3 -u "$S/2ecf-polar-r272-quantitative-full-reach.py" --scripts "$S" --field "$F/strong-physical-hf64m80-W.json.field.npz" --potential "$F/strong-hf-upper-disk-potentials-1024.json" --composite "$F/strong-upperdisk-actual-R210-graft.json" --edge-defects "$F/strong-hf-true-edge-defects-2048.json" --new-edge polar-R272-new-edge-second.json --output polar-R272-quantitative-full-reach.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-r272-edge-second-angular-bounds.py | 6f3781aae06c89cd4184929a40f7bbfcd0504bb6aa6f3770823cb036786ca0a0 |
| 2ecf-polar-r272-quantitative-full-reach.py | c36d90e932a4b0b8afb48ec13c8f95b7894514dc0b7cc4cbd8827a2840f3a907 |
| polar-R272-new-edge-second.json | 5e7444ba59989b6fdf41c582511856d27e6fdc3fc11f5569f9427b2d5ec5b7ac |
| polar-R272-quantitative-full-reach.json | 69ddaa9fb6f4fafe5d9792b5f57ff970434c32f74b4ab75c80a057ad15632663 |
| polar-R272-new-edge-second-exit.json | 77f77716a5664bfec5f2dac2fd808f9edff95244df670084b02e170cd1dfdf41 |
| polar-R272-new-edge-second.log | 5b73768c9b5a42bc177517e4e3301c710180e167646ab6661c824c2752ba3dd7 |
| polar-R272-quantitative-full-reach-exit.json | 2672b1fe2829a75d9af4e0f69c2c4b7cb4278391a7a087667cfb722bf76ba4b9 |
| polar-R272-quantitative-full-reach.log | 55d579f79d9ec432e8d52b5bfdfa59898f6d8002a7c5b193ae6ad7b18a82b446 |
