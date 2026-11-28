# 在原材料角联合构造三维子午线并对两真端口求解

**数值证据。**

每个真实材料角 u 采用随角转动的水平基，把单位切向写作 (cos φ cos β,sin β,sin φ cos β)。两端实际归一化切向及其径导分别固定，截断三次样条的内控乘偶余弦/偶正弦模；两角场共 187 个物理控制。积分三维速度后，以两端一、二阶导数为零的平滑阶跃修补三维端位差（右端位置修补为所需差，右端一、二阶为零）。在所有角间共同对离散的 E,F,G、两主曲率、7 个几何行和面积行做设计，再将真场按 64 物理格和 80 个存储角模定义完整位置。两边的 Hermite 端节点逐函数消费准确端口 P,V,A 及其所需角导。G10 的原全部 4291840 行、独立移位 G11 另按原权全观察；设计 collocation 的材料半径取原实际训练半径随物理 s 的线性插值，最终观察仍消费原完整目标。
两行次序为自身 L-BFGS 接受数 / 完整原 G10 R² / G11 metric / κ / held。R273 真实高弯 ridge 为 150 / 0.3836789346 / 0.3096103717 / 12.53048356 / 0.6397712114；R282 负端角为 220 / 2.348489529 / 0.5722909907 / 15.76631016 / 0.5813091995。高弯场的三维端位修补在密格仍约 .067，返回场约 .251；修补使径向速率发生变化。R273 高弯的曲率改善到 12.53048，held 仍比 .64 少约 .00023。

## 可移植重生

W 含 R267 的原 G10/G11 数据、两份 master、R273 ridge 与 R282 returning-down 的既有全径线设计和场。S 是公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-material-curve-coupled-spherical-design.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --iterations 150 --field polar-gap092-material-ridge-3D.npz --output polar-gap092-material-ridge-3D.json
python3 -u "$S/2ecf-polar-material-curve-coupled-spherical-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-ridge-3D.json --field polar-gap092-material-ridge-3D.npz --output polar-gap092-material-ridge-3D-full.json
python3 -u "$S/2ecf-polar-material-curve-coupled-spherical-design.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-returning-rays-down.json --seed-field polar-gap092-returning-rays-down.npz --iterations 220 --closure 16 --curvature 1 --geometry 40 --field polar-gap092-material-returning-3D.npz --output polar-gap092-material-returning-3D.json
python3 -u "$S/2ecf-polar-material-curve-coupled-spherical-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-returning-rays-down.json --design polar-gap092-material-returning-3D.json --field polar-gap092-material-returning-3D.npz --output polar-gap092-material-returning-3D-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-material-curve-coupled-spherical-design.py | cdcca844e230e2029708b79ff28af35980c5061edfba14eb305b727735ab7622 |
| polar-gap092-material-ridge-3D.json | c4fb2a2fd18b2f9120f7d32218703b74f8ba539fe450e5f8d773dca788c71552 |
| polar-gap092-material-ridge-3D.npz | c28fef7fca0dbbda1f03683c37362d86fb8a7e253ce8dd9365bf5742d7d72be4 |
| polar-gap092-material-ridge-3D-full.json | 37a63c26abe461d2745945d68cee85d1e52002c660d04f2cfd1fe1c37b47ff53 |
| polar-gap092-material-returning-3D.json | 7e68eba5d8f538534b65e6bc8a1f14e2848540dca16f26ed6b4b5a52dff6af67 |
| polar-gap092-material-returning-3D.npz | 94b0a1d9d66a7df998a32729c2e25fdb26d73009a9061d599c2eaac65fb7e144 |
| polar-gap092-material-returning-3D-full.json | 86616cafd94ec2f2646b573bfd02485efb84cdad960fb101a5a976ae0acaaaad |
| polar-gap092-material-ridge-3D-exit.json | 1920cacdcc295197a8f3fd6f0c4c11bb0bb1a4879ea4fa977949cf98e0e846c0 |
| polar-gap092-material-ridge-3D.log | 89342bb42f9f4a0ed3a39851649f97816a4126e2566fa0dcf4e8231f786478f1 |
| polar-gap092-material-ridge-3D-full-exit.json | b5cae3483a7af46170b32fac7377a89914787d0041acca785057a1a7308bd626 |
| polar-gap092-material-ridge-3D-full.log | 02f4fabfd381f1a825775e1f52b7ffce9c93b92e26c3bea99d95ed07b19ead09 |
| polar-gap092-material-returning-3D-exit.json | ae11b987665ef6b8a5cf4f87abd72324c43768be9ce5bb6c9fed11d1684bf4f2 |
| polar-gap092-material-returning-3D.log | c9a9393f4093ea82d930ff68a2dad22faa2f9f82cf5c5716a32cd2e3c5660c0b |
| polar-gap092-material-returning-3D-full-exit.json | 26b69b392df81179cb83efdc2550f94bec327239e3375871e04ef2c6a4bbe4cf |
| polar-gap092-material-returning-3D-full.log | bd54fa82ecccd69dc7702d58639db46162f1d3dc55335b39b72974b14f4ec29a |
