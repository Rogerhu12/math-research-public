# 混合曲率准确圆参考的非圆双端继续与变长实步

从 [R275](../results/R275-exact-mixed-gaussian-round-seed-with-two-true-ports-and-reach.md) 出发，首次同时移动本参考的真实中央截面、R205 弯尾振幅和整段径向目标。在转角段上优化三维实际位置。下面各峰是稠密有限观测；只有中央与整片开发尾的准确等距、两端的准确二阶接合及表中负 Gaussian 曲率上界属解析结论。

## 完整物理定义

给定半轴 $a=R_0+\lambda/2,b=R_0-\lambda/2$，按真椭圆弧长材料化，$a_e=\operatorname{perim}(a,b)/(2\pi)$。中央柱半长 $c=Z-LI$，$R_0=4/5+LI$，$I$ 是 R275 的真实相位积分。$t=(s-c)/L$。以 R275 旋转图为底，加上左右两端的 quintic Hermite 位置、径向速度和加速度修正。左端给真实椭圆与原圆的差。右端给整个开发面 $D_A(r\cos u,r\sin u)$ 在 $r=4/5$ 处相对零幅平盘的三项差；其中纵向弧为 $(C_A(y),Z-H_A(y))$，其单位切向角是 $A\,\mathrm{sgn}(y)S_9((|y|-.34)/.46)$，内领按原 R205 定义平坦。Hermite 因子包含物理 $L$ 各阶幂。因此两头的位置和所有总阶不超过二的物理偏导都匹配。中央处用关于水平面的反射，固定帽沿真实水平领接入。零幅参考的 $\kappa$ 和 reach 未转移给这些新位置。

在转角段再加径向五次夹紧 B 样条乘角 Fourier 系列，各端省掉三行。每个物理坐标有 $m$ 个实际模式，$x$ 取奇次 cos，$y$ 取奇次 sin，$z$ 取偶次 cos。新目标
$$g=ds^2+f(s)^2du^2,\qquad
 f=(R(t)+(a_e-R_0)H_{00}(t))\exp\left(\sum_j B_j(t)y_j\right).$$
所有 $x,y_j,A$ 的数值都存于各行独立 JSON，按 binary64 精确系数解释。用物理十进有理 $L,4/5,7/200$、存储的高度 $Z$ 以及相应连续积分定义解析场；数值观测使用 binary64、分段 32 点和开发尾 48 点 Gauss 求积。原中央周长不随材料角变化；整片真实开发尾的参数导数正交且径向单位速，两个区域的度量余差均准确为零。每次改变 $L,Z,y$ 或中心都独立登记目标，未把这些新基线相互当作固定 $g$ 的加密。

## 实际结果

训练为 $145\times96$，普通复查为 $257\times192$，独立移位为 $235\times256$，包括径向两端。表内为训练中真正接受的联合步数，及独立移位的相对 Gram 算子峰、最大绝对主曲率与实际尾幅。每次联合步重新求值原非线性位置与目标，振幅方向用真开发端口的中心差分；带曲率引导的步骤含几何二基本形式、法向与 Gram 的变化。早期 18 跨度高模式步及一次不能接受的加倍也保留。

| 态 | 间隙 | $L$ | $Z$ | 径跨度×每分量角模 | 接受步 | Gram 峰 | 主曲率峰 | $A$ | $K_g(1/16)$ 严格上界 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.03125 | 0.4 | 0.51 | 18×6 | 3 | 0.132881565 | 9.768283 | 0.02413205 | -3.221 |
| 2 | 0.0625 | 0.4 | 0.51 | 18×6 | 0 | 0.254685752 | 19.097182 | 0.04826410 | -5.805 |
| 3 | 0.03125 | 0.4 | 0.51 | 5×2 | 19 | 0.027841126 | 9.799358 | 0.00498276 | -3.031 |
| 4 | 0.03125 | 0.4 | 0.51 | 5×2 | 6 | 0.028811689 | 9.324735 | 0.01799913 | -2.678 |
| 5 | 0.03125 | 0.4 | 0.51 | 10×4 | 9 | 0.024227941 | 9.058573 | 0.08957530 | -5.237 |
| 6 | 0.0390625 | 0.4 | 0.51 | 10×4 | 11 | 0.031081065 | 9.202239 | 0.09868297 | -5.328 |
| 7 | 0.0625 | 0.4 | 0.51 | 10×4 | 5 | 0.049005456 | 9.741090 | 0.10508639 | -5.975 |
| 8 | 0.0625 | 0.5 | 0.51 | 10×4 | 12 | 0.037596576 | 9.241076 | 0.20092153 | -5.215 |
| 9 | 0.0625 | 0.65 | 0.53 | 10×4 | 10 | 0.029635144 | 9.145304 | 0.15034371 | -4.297 |
| 10 | 0.09375 | 0.8 | 0.58 | 10×4 | 8 | 0.036606840 | 9.188904 | 0.19915780 | -3.889 |
| 11 | 0.0625 | 0.92 | 0.6 | 10×4 | 14 | 0.021970811 | 8.924227 | 0.01575723 | -3.257 |

第 2 态仅是已实际完整评价的预测，真实尝试没有接受更新。其余步均接受了非零三维场和目标变化。此批所有固定目标附加试步的实际接受数均为零。第 3 态低维再优化降到了 .02784；第 4 态以降低曲率为代价将误差改变到 .02881；第 5 态在嵌套空间给 .02423。第 7 态与第 11 态同有中央间隙 $1/16$，改动物理弯段长度及对应目标使独立误差从 .04901 到 .02197。同一组结果仍不能显示非零间隙下固定目标的误差趋零。

最后一列为全部相应新目标自身的有理证明。设 $d=\lambda/2$。对椭圆弧速应用平方根的切线上界，并把单位圆切向投影作为下界，得 $0\le a_e-R_0\le d^2/(2R_0)$。R275 的相位对称与 $\sin\phi+\cos\phi>0$ 给 $R_0\ge4/5$。对 $r=R+(a_e-R_0)H_{00}$、$v=\sum B_j y_j$，有 $K_g=-(r''/r+2r'v'/r+v''+(v')^2)$，导数按物理 $s$。脚本在 $t=1/16$ 用有理上下界包含 $r,r',r''$，按实际存储的二进 knot 与系数作精确 de Boor 基函数导数。每一态都得到严格负上界。通过连续性，实际 $K_g$ 在该点的邻域为负。该符号没有给出精确非圆等距支路或几何 reach。

## 重生

令 `S` 为课题公开脚本目录，`W` 为新的空输出目录。下列 bash 命令重生所有已接受状态及逐态移位观察；删去无接受的末尾试步不改变输出文件。

```bash
set -eu
mkdir -p "$W"
python "$S/2ecf-round-negative-K-complete-small-gap-continuation.py" --scripts "$S" --gap 0.03125 --spans 18 --modes 6 --joint-steps 3 --fixed-steps 0 --output "$W/round-mixedK-small-gap-1over32.json"
python "$S/2ecf-round-negative-K-complete-small-gap-continuation.py" --scripts "$S" --gap 0.0625 --spans 18 --modes 6 --joint-steps 0 --fixed-steps 0 --parent "$W/round-mixedK-small-gap-1over32.json" --output "$W/round-mixedK-small-gap-1over16.json"
python "$S/2ecf-round-negative-K-complete-small-gap-continuation.py" --scripts "$S" --gap 0.03125 --spans 5 --modes 2 --joint-steps 19 --fixed-steps 0 --output "$W/round-mixedK-small-gap-1over32-coarse.json"
python "$S/2ecf-round-mixed-K-curvature-guided-continuation.py" --scripts "$S" --gap 0.03125 --spans 5 --modes 2 --joint-steps 6 --fixed-steps 0 --parent "$W/round-mixedK-small-gap-1over32-coarse.json" --output "$W/round-mixedK-guided-1over32.json"
python "$S/2ecf-round-mixed-K-nested-continuation.py" --scripts "$S" --gap 0.03125 --spans 10 --modes 4 --joint-steps 9 --fixed-steps 0 --parent "$W/round-mixedK-guided-1over32.json" --output "$W/round-mixedK-nested-1over32.json"
python "$S/2ecf-round-mixed-K-nested-continuation.py" --scripts "$S" --gap 0.0390625 --spans 10 --modes 4 --joint-steps 11 --fixed-steps 0 --parent "$W/round-mixedK-nested-1over32.json" --output "$W/round-mixedK-nested-gap5over128.json"
python "$S/2ecf-round-mixed-K-nested-continuation.py" --scripts "$S" --gap 0.0625 --spans 10 --modes 4 --joint-steps 5 --fixed-steps 0 --parent "$W/round-mixedK-nested-1over32.json" --output "$W/round-mixedK-nested-gap1over16-direct.json"
python "$S/2ecf-round-mixed-K-length-height-continuation.py" --scripts "$S" --gap 0.0625 --spans 10 --modes 4 --joint-steps 12 --fixed-steps 0 --parent "$W/round-mixedK-nested-gap1over16-direct.json" --turn-length 0.5 --cuff-height 0.51 --output "$W/round-mixedK-L50-gap1over16.json"
python "$S/2ecf-round-mixed-K-length-height-continuation.py" --scripts "$S" --gap 0.0625 --spans 10 --modes 4 --joint-steps 10 --fixed-steps 0 --parent "$W/round-mixedK-nested-gap1over16-direct.json" --turn-length 0.65 --cuff-height 0.53 --output "$W/round-mixedK-L65-gap1over16.json"
python "$S/2ecf-round-mixed-K-length-height-continuation.py" --scripts "$S" --gap 0.09375 --spans 10 --modes 4 --joint-steps 8 --fixed-steps 0 --parent "$W/round-mixedK-L65-gap1over16.json" --turn-length 0.8 --cuff-height 0.58 --output "$W/round-mixedK-L80-gap3over32.json"
python "$S/2ecf-round-mixed-K-length-height-continuation.py" --scripts "$S" --gap 0.0625 --spans 10 --modes 4 --joint-steps 14 --fixed-steps 0 --parent "$W/round-mixedK-L65-gap1over16.json" --turn-length 0.92 --cuff-height 0.6 --output "$W/round-mixedK-L92-gap1over16.json"
python "$S/2ecf-round-continuation-negative-gaussian-witness.py" --output "$W/round-mixedK-actual-target-negative.json" "$W/round-mixedK-small-gap-1over32.json" "$W/round-mixedK-small-gap-1over16.json" "$W/round-mixedK-small-gap-1over32-coarse.json" "$W/round-mixedK-guided-1over32.json" "$W/round-mixedK-nested-1over32.json" "$W/round-mixedK-nested-gap5over128.json" "$W/round-mixedK-nested-gap1over16-direct.json" "$W/round-mixedK-L50-gap1over16.json" "$W/round-mixedK-L65-gap1over16.json" "$W/round-mixedK-L80-gap3over32.json" "$W/round-mixedK-L92-gap1over16.json"
```

各实际输出指纹如下。

| 文件 | SHA-256 |
|---|---|
| `2ecf-round-negative-K-complete-small-gap-continuation.py` | `182bce938abadbd908685f65153e54ddc7c6e53f86fba2a1d700ed6abf4c98ba` |
| `2ecf-round-mixed-K-curvature-guided-continuation.py` | `3b2e114912f810d480cb2a1a21feb0653cc3be3e6846d9e9be241facf640af4c` |
| `2ecf-round-mixed-K-nested-continuation.py` | `ba5cba9a0721952d5a76efe08085a604b96c3ff7c7a74dffacdfa87d93bb6e0f` |
| `2ecf-round-mixed-K-length-height-continuation.py` | `ae7b73465cd6cefb8b87ca1b0ed80526e1129fc4d5da44251607c0a793f18a01` |
| `2ecf-round-continuation-negative-gaussian-witness.py` | `bc56a0aafc647e10806a4d2b16b50b76cf842444f48c3a622e11118a401295b7` |
| `round-mixedK-small-gap-1over32.json` | `5d2a45f8128fdadd9afd42da7873bde2aae8d7701d6fdaa074a5589a1cc44cf0` |
| `round-mixedK-small-gap-1over16.json` | `02bd5ef7626a1b1de7415bdf7fbd9a4ef87b944948890c1c2f4a95fdf9884a6c` |
| `round-mixedK-small-gap-1over32-coarse.json` | `fb6450bc13a52e5cfc9f9b099ef1ab133ae1bd7b61b9f9d5ea3f04e4d8ae0762` |
| `round-mixedK-guided-1over32.json` | `e33965cfad2e9fae2d875ea18b2265ce2c1e66365fa5eaa6946f47b8f832e0f4` |
| `round-mixedK-nested-1over32.json` | `41d86822c354c8538d13f062004bb273d859c798aeae0a95ba9d55252f39dbb5` |
| `round-mixedK-nested-gap5over128.json` | `43718788e1a2853f7d02659941f38a82a04abeed5f0f57d59b1a69e02a12c018` |
| `round-mixedK-nested-gap1over16-direct.json` | `5793fef0478ae72d2edf837e3fe656d67ec67b22dce2caa20087fd70d3add19b` |
| `round-mixedK-L50-gap1over16.json` | `c8a3de0a25a19efb3c56452c0d2841cacb35dc1a1eb4ab41b3791777373c0f22` |
| `round-mixedK-L65-gap1over16.json` | `88b52c7d35e45bab1acf38f6c6704e28dd43cb75a8c57475fb6a45a78f95d98e` |
| `round-mixedK-L80-gap3over32.json` | `548ed1b82aabed7fadcb21303fa162e8c609b16bf7d8ac008a69de2f7adc8a64` |
| `round-mixedK-L92-gap1over16.json` | `453d4b53b7718085ca395b3866e957d04a7389987009bed3d2d771cd311f2de7` |
| `round-mixedK-actual-target-negative.json` | `c2cbc4d52030f637bdb230f743fd0ec5cfc4be7fb99026b7c03c5514c3fee741` |
