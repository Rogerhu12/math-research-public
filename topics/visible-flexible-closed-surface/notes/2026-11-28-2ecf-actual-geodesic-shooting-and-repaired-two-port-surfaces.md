# 真实测地射击、端口偏差与实际修补后的两个完整场

**数值证据。**

从真实 R267 左端 P,V 出发，初次试验推进 X_s=T，T_s=k (T×X_u)/|T×X_u|，以两坐标的实际导数作离散伴随。光滑正则解在初端 E=1,F=0 时有 E_s=F_s=0。数值射击还需满足真实右端；40 控制的粗网最优化未能在独立密网维持原端位。第二种另以 12 阶截断正规化法向加速度并保持球切投影，实际方程有所改变，F 须重新观察。两者都将真实末端 P,V,A 偏差以径向 Hermite 逐角修补后生成了独立整场，重算全部原 G10 行和错移 G11。表中端误差按原物理单位计。

| 场 | 控制数 / 自身接受 | 修补前密网右端 P / V / A 最大范数 | 修补前密网 G 相对误差 | 修补后独立 G11 误差 / κ / held |
|---|---:|---|---:|---|
| first | 40 / 65 | 0.09040999 / 0.5623905 / 2.418983 | 3.601634 | 2.596939957 / 88.76329618 / 0.6264831128 |
| resolved12 | 60 / 85 | 0.06169992 / 0.0886766 / 0.8634618 | 0.3294532 | 0.4299018877 / 16.06320955 / 0.6317920111 |

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-geodesic-material-physical-shooting.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --input-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --iterations 65 --field polar-material-geodesic-first.npz --output polar-material-geodesic-first.json
python3 -u "$S/2ecf-polar-geodesic-actual-closed-field-observe.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-material-geodesic-first.json --field polar-material-geodesic-first.npz --output polar-material-geodesic-first-full.json
python3 -u "$S/2ecf-polar-geodesic-resolved-curvature-transport.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --input-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --iterations 85 --cut 12 --field polar-material-geodesic-resolved12.npz --output polar-material-geodesic-resolved12.json
python3 -u "$S/2ecf-polar-geodesic-actual-closed-field-observe.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-material-geodesic-resolved12.json --field polar-material-geodesic-resolved12.npz --output polar-material-geodesic-resolved12-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-geodesic-material-physical-shooting.py | 8958684372a82740b7dbe2928db1ccce508185df1045a8cb84f98d31355fb2e4 |
| 2ecf-polar-geodesic-resolved-curvature-transport.py | 4dd568d859e9bbafb77d0b7c07f5228b04a3ca856f234405d23bc527832a0ff5 |
| 2ecf-polar-geodesic-actual-closed-field-observe.py | 747847a1ed3c91a72aa7f55c7a0808fb27930b51120ae7452708bf3f9ad0dda6 |
| polar-material-geodesic-first.json | fee505337b972d245d7f245e21ddee601922d8d92ca2015fb01b62bd200d465e |
| polar-material-geodesic-first.npz | 477507648375ab8935c7e5ddb9bb7be0b42c748cf7452699908bf3ee30d425cd |
| polar-material-geodesic-first-full.json | 4e02d248267644185e91614776341f0f86a47f037314314e9de82ef3dac8ac79 |
| polar-material-geodesic-resolved12.json | 8add19f5b116f9250471965230440e1b83417aee288e694536fb0db9628121f2 |
| polar-material-geodesic-resolved12.npz | 4521cf7680f317fcd2cbae557b66cd0dcdab5c700960eb9b78fc05755ea1b739 |
| polar-material-geodesic-resolved12-full.json | 5a524c223b8af0b0f648b4a2b07545e180201d37ef66bd8b15dbc0c3e2b5dca4 |
| polar-material-geodesic-first-exit.json | 2704cbf28904b55a94befd2993aec0befd98b4d884ecb5807f505b7a506208ef |
| polar-material-geodesic-first.log | 9bab1763e66cb0b11d16a89393e01543574fa66fec2b029e3c8970caad66fdc2 |
| polar-material-geodesic-first-full-exit.json | eeea676aa36da22ad21db0c101a6f4c79616c3fecf3e30093583c8b1761d4d52 |
| polar-material-geodesic-first-full.log | 4255a9dc424949d270a700a64ca4a8ed767765506cd8274738c7e29289c32eac |
| polar-material-geodesic-resolved12-exit.json | 134809ff26a5faff3459d8db9d2740514240eb8071b20df86f8dcd189e8b1964 |
| polar-material-geodesic-resolved12.log | 47e203a920be617d17a7e554075257cadcc4cdc6de51163d3b7a1e3d14e81148 |
| polar-material-geodesic-resolved12-full-exit.json | 2adaedde2f084d2485a420d60283c9cd801c77a0bb3093ad23e66c74a85df4a3 |
| polar-material-geodesic-resolved12-full.log | 02c719e4f0ea961a0374c0fe4c3a7cc9b8cafab520b44d65e915e3937d9386c0 |
