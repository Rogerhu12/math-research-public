# 单位速三维端位场上设计十一半径，再冻结新度量加密

**数值证据。**

在刚得到的真实三维闭合高弯场上，后带真实目标改为 a_old(s) exp(B(s)α)，共 11 个五次样条基；三阶夹紧使两端值和前两导消失，区间外为原目标。全部原物理行参与求导，新半径严格正。每次真实设计依然要解每角的三种三维端位方程。先用 575 个球向位置控制和 11 个目标控制，对新设计独立计 300 个接受。保存准确二进半径向量及物理长度的身份 SHA256 为 962678011b9ddeed3d2a29122b94fadd70eeb61baa8b04c5e8f6f86994b1d9c3。然后仅释放 961 个球向位置系数、保持同一保存 g，真实 350 个接受。
新 g 设计与后续同 g 位置加密的自身接受 / G10 R² / G11 metric / κ / held 依次为 300 / 0.1403309785 / 0.2048365082 / 11.77305372 / 0.6394178792、350 / 0.118178722 / 0.2011012872 / 11.64144708 / 0.6375724549。两次全 G10/G11 都使用各自真实后段目标及完整旧材料数据。固定目标后 metric 约 .20484→.20110、κ11.77305→11.64145，held 约 .63942→.63757，仍待强几何与精度。

## 可移植重生

W 含前条的实际 H24 球向场、原 R273 ridge 底、G10/G11 和两份 master。S 是公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-material-implicit-coupled-radius.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --start polar-gap092-material-ridge-implicit-h24.json --iterations 300 --geometry 180 --curvature 3 --field polar-gap092-material-implicit-radius11.npz --output polar-gap092-material-implicit-radius11.json
python3 -u "$S/2ecf-polar-material-implicit-coupled-radius.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-implicit-radius11.json --field polar-gap092-material-implicit-radius11.npz --output polar-gap092-material-implicit-radius11-full.json
python3 -u "$S/2ecf-polar-material-implicit-coupled-radius.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --start polar-gap092-material-implicit-radius11.json --frozen polar-gap092-material-implicit-radius11.json --iterations 350 --spans 32 --modes 15 --angles 152 --radials 145 --geometry 180 --curvature 3 --cells 96 --fine-radials 769 --fine-angles 320 --field polar-gap092-material-implicit-frozen11.npz --output polar-gap092-material-implicit-frozen11.json
python3 -u "$S/2ecf-polar-material-implicit-coupled-radius.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-implicit-frozen11.json --field polar-gap092-material-implicit-frozen11.npz --output polar-gap092-material-implicit-frozen11-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-material-implicit-coupled-radius.py | 13e0225b9fe2481c20c52e165e1e0efeb70a3492a3b377b3f727a4163350b66d |
| polar-gap092-material-implicit-radius11.json | 8db350328e610246bb850b8bbbde9e7ce2e5f3d1dcd78da7843c79e235da5ead |
| polar-gap092-material-implicit-radius11.npz | 76c01f5d997ba600e4ed7a6a62ca61778dc844c1fe41cb80b0ae8a8142c84be9 |
| polar-gap092-material-implicit-radius11-full.json | f1e2ba8d71582c1924088805bb6b38f7214c0cca06fdc2eebe4f5f1f031aa723 |
| polar-gap092-material-implicit-frozen11.json | e3a41e97719a7768199b071d6c6b8a6cef3e92d51657dd30254841dea86e545a |
| polar-gap092-material-implicit-frozen11.npz | a13cb8406d94dac7ebb8bc428502fbe3900a80bd03221b1cf078328c215c6c60 |
| polar-gap092-material-implicit-frozen11-full.json | e18110b170a9f72d0389c69cf6ffb2ed3b10cc20634e1928444f56a225ca39c4 |
| polar-gap092-material-implicit-radius11-exit.json | f46fb0b0cb61bebf433700cbcd4a02dd5ea0b26ed7901903f24fbcf47f2d45d4 |
| polar-gap092-material-implicit-radius11.log | 37c4a56d44707a0b897362440636e6c6d840e02a71578226f6b9609b58cfe780 |
| polar-gap092-material-implicit-radius11-full-exit.json | 17867cd3d95883ab9d97516d8fbbbce73b36486e809b9e7dc8d711a8f6c116f7 |
| polar-gap092-material-implicit-radius11-full.log | 480719de9863592a0ef803a5fa6fa3290ea14f61d20d1f5da6267b1f40ad8730 |
| polar-gap092-material-implicit-frozen11-exit.json | 36dddc73c3723b5d05440201873c070a3afce73a9a2110f698f4aae77620960f |
| polar-gap092-material-implicit-frozen11.log | 72706f2719005cadca5cda0673730bd3ae4a00e5a636f81a79ce29daeea1f5f3 |
| polar-gap092-material-implicit-frozen11-full-exit.json | 9801c8c80194e530ec0df03959eee6397cfc56e5a86db8bcf1bb87cec590ec64 |
| polar-gap092-material-implicit-frozen11-full.log | 4812ceb6a18475ee664d4bccb84063cb9dfa0ca9f17844dbef4ec2ca1c5da3e2 |
