# 真实三维端位乘子的单位材料速度场及固定度量加密

**数值证据。**

取消上条的阶跃位置修补。给原单位球向 T 加 h(s)ξ(u) 后再单位化，h=16t²(1−t)²，端点 h,h′ 为零。每个设计角直接把三维速度积分同真实端差做三维方程求根，雅可比为正权单位球切向投影的积分；实际 Newton 回溯要求候选归一化分母非零且三维真实残差下降。优化的梯度包含三维乘子的隐式导数，每个新问题另核完整差分。本条对这些有限求解并未证明每个实角的精确乘子分支。最后存储的 Fourier–Hermite 曲面按自己的真实坐标及端口重新观察全 G10/G11；也未把样本单位速度当成这一重建场的连续恒等式。
同原材料 g，187 球向控制的实际 180 个接受以及加密至 575 控制、24 个径向 span 与 12 个非零角频率后的 260 个接受。结果为自身接受 / G10 R² / G11 metric / κ / held；两状态依次是 180 / 0.3096501172 / 0.270076925 / 12.96745331 / 0.644688476、260 / 0.2896264981 / 0.2643349344 / 11.92883003 / 0.6390472374。细积分完整角列的最大端差分别为 4.445773850182777e-13、4.754148811043561e-13，没有人为补端位移。加密的几何、曲率权亦重新设置以兼顾强几何，接受计数各从零开始。G11 曲率降至 11.92883，held 重新低于 .64。首个原观察包装器读取了已清理的临时报告，退出 1；随后直接用已保存的同一曲面独立观察通过。联合入口已修复该输出路径并在加密场中自然 0。

## 可移植重生

W 含上条的真实三维高弯场、原 ridge 源及各完整 G10/G11 输入。S 是公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-material-unit-speed-implicit-port-closure.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --start polar-gap092-material-ridge-3D.json --iterations 180 --field polar-gap092-material-ridge-implicit.npz --output polar-gap092-material-ridge-implicit.json
python3 -u "$S/2ecf-polar-material-curve-coupled-spherical-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-ridge-implicit.json --field polar-gap092-material-ridge-implicit.npz --output polar-gap092-material-ridge-implicit-independent.json
python3 -u "$S/2ecf-polar-material-unit-speed-implicit-port-closure.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --start polar-gap092-material-ridge-implicit.json --spans 24 --modes 12 --radials 121 --angles 128 --geometry 80 --curvature 2 --iterations 260 --fine-radials 769 --fine-angles 320 --stored-modes 100 --cells 96 --field polar-gap092-material-ridge-implicit-h24.npz --output polar-gap092-material-ridge-implicit-h24.json
python3 -u "$S/2ecf-polar-material-coupled-implicit-design-and-observe.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-ridge-implicit-h24.json --field polar-gap092-material-ridge-implicit-h24.npz --output polar-gap092-material-ridge-implicit-h24-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-material-unit-speed-implicit-port-closure.py | 9e1b53d8f2bf76deb60df783ad20b8d324b482b2253bd2abed93cbd6285ccb42 |
| 2ecf-polar-material-coupled-implicit-design-and-observe.py | 5c440590eacafb988db302362429378f96d2d38c7a992a7f874e1d75b764a203 |
| polar-gap092-material-ridge-implicit.json | 55237e96955398d1815bf9f2296067f7bec3cc3a80bbe364e470509194439c7e |
| polar-gap092-material-ridge-implicit.npz | b5a5775a8d0bc3dc98a48302a73a76df8d931eefecead28fe54f4ff6a1427886 |
| polar-gap092-material-ridge-implicit-independent.json | 7ae7aeeeb55be30a20c169308d66d3320d3f68d8e0bb1d8e3f16b9527f502dcd |
| polar-gap092-material-ridge-implicit-h24.json | b96bda9826e4d2f4eac2a67785ece852b3a19c7790c684a236a5c8fd4c175840 |
| polar-gap092-material-ridge-implicit-h24.npz | 435e68cb9d686765128963c587d9897d8cacd9b371c817464621298a08bc1c0f |
| polar-gap092-material-ridge-implicit-h24-full.json | 4dbd6d5364711f304c9ac18b36c15d891f2142b9de3bd673e397bb1399a21bf7 |
| polar-gap092-material-ridge-implicit-full-exit.json | aaa2039faf1e450b08ec7b8dc302e533d7d04046b5d12a3448fe8018728c2c8c |
| polar-gap092-material-ridge-implicit-exit.json | 86657d6912fa073533f1c5405c828a21391eeb0edd50120e37ff8900591e2deb |
| polar-gap092-material-ridge-implicit.log | dc41e43191ed05b0dba2b87fd5aa83e93420960996c3f93ca29ac15ec9546fdb |
| polar-gap092-material-ridge-implicit-independent-exit.json | 18948823f189dc9f3aba3ac0d983b5ee121e72b72dc33ddae62f4776c138bd21 |
| polar-gap092-material-ridge-implicit-independent.log | 2955d074694edc13a43b28aae41305f182c1198d57d0731a07c051c613b83c1f |
| polar-gap092-material-ridge-implicit-h24-exit.json | 43e1e251b0cf2e23573f6e8466f8c166807bd1baf7f7079836a73863579ba6ea |
| polar-gap092-material-ridge-implicit-h24.log | 83acab18e87147ca435b7eee6a04bcddfe1300cd7f421d4d18ccd52e767c7b2e |
| polar-gap092-material-ridge-implicit-h24-full-exit.json | b37e0c75b7436db428e1b03015c8f585df661fd21dd2b301637cb3772f5f3ef4 |
| polar-gap092-material-ridge-implicit-h24-full.log | 9ab7597d19aa255b13df7ad81d0fe4408feea46eda0fb81ab3dbde0ab19e128d |
