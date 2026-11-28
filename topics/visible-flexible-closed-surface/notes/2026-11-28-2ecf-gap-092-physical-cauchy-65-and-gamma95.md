# 间隙 23/25 的新中央椭圆、65 节点 Cauchy 图及 Γ95

**数值证据。**

新中央设计取 P(A,B)=P(7/5,1/2)、A−B=23/25，在原椭圆周长的有理包围中求解。积分器采用两轴的存储值 A=1.407367534347312, B=0.48736753434731195。这对二进有理数自身的准确周长是新图前缀的度量基数。旧材料 c=13/128、r=.06、v=.045、coast=.02、原开发 cut 及 Z=.51 均保留。点距 guide 的标记 y 坐标随 A 改为真实新长轴。
重新积分 191 模的 Cauchy 系统至 r；工作角数 768，用 DOP853 实际 RHS 计算 1637 次，产生完整 65 个物理位置与径向一、二阶导数的 Fourier 系数。采用同一新终点数据形成新的 degree-95 Γ，继而将 r 的末端 P,V,A 通过真实新 R137 coast 端口修补到终格。新中央椭圆柱的曲率峰 A/B²≈5.92508162；65 个 IVP 节点的度量峰 8.18503e−13，曲率峰 7.47424991。准确连续图与端口的误差须另行证明。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-new-central-gap-physical-master.py" --scripts "$S" --gap 23/25 --prefix polar-new-gap-092-master
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-new-central-gap-physical-master.py | 14750635876a87803780a7b7d737a19eb36bc3b4ce4b095b41bc9d25f36a486e |
| polar-new-gap-092-master.json | 7013e681d36dc6d76b795951c2bf1daf2709d5024685539917a7047d23893d0e |
| polar-new-gap-092-master-ramp.npz | 6f06a6a54577e81b08d4e46339d457506a211da8a4d1eb2a25bc0191bf4234a1 |
| polar-new-gap-092-master-coast.npz | 71d63012f3142e9304196ef70238f028f914c74fe005c9c76bb436e7d0fae1d4 |
| polar-new-gap-092-master-exit.json | b2c4640f36ee12757d3a78e7a2d19be88112b04333e31982783559b383c8935c |
| polar-new-gap-092-master.log | a11b26b77b95b9f8e03cd7d8d1e496b84593d5086c262f48d05793d5f4392d37 |
