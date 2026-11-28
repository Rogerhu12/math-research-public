# H65 新总材料长度、真实单调时钟与同一新度量的三个全位置步

**已证明：** [R268](../results/R268-strictly-convex-physical-meridian-clock.md) 的逐点严格凸性与有限维条件。**数值证据：** 本次换一个总材料长度后，记录全 G10 暖输入与三个实际位置接受；G11 峰未随总代价单调下降。

固定 H65、旧 45×147 位置和 36 个半径设计系数，用[混合设计第 3 态](2026-11-28-2ecf-h65-two-space-six-actual-metric-designs.md)作为新构造的几何暖输入。原长到 cut 的二进坐标为 $.9772364498716914$，新 cut 约 $.9832364498716915$。前缀、两端空间位置两 jet、尾/cuff 及帽的初始像照旧，随后内侧的 6615 个 Cartesian 系数全部可调。目标是新的 $ds^2+a_{\rm parent}(x(s))^2du^2$。原计算标签 $x$ 单调，物理 $s$ 由 R268 的原函数精确定义。源与修正均用 $D_s=D_x/v$、$D_{ss}=D_{xx}/v^2-v_xD_x/v^3$、$D_{su}=D_{xu}/v$ 真正求六 jet。新物理函数为显式复合，未将其当作 $s$ 中的五次样条。

**准确参数。** 把实际保存的 45 个二进系数解释为有理数，得到
$$
\Delta S=95704415696513957457548859975134929/15950735949418990474845684723364134912.
$$
这给 $.00599999999999<\Delta S<.00600000000001$。准确的正速上下界分别为 $141299780483163341/144115188075855872$、$295267425065269037/288230376151711744$，约 $.98046419,1.02441467$。两端删去三个夹持基函数给 $v=1,v_x=v_{xx}=0$。实际 45 组正权 G10 径向基评价的有理行列式模素数 2147483647 为 652517266。脚本先取 45 行，再从原二进节点和 knots 在这个域上重算完整五层 de Boor 递推与行列式；挑行方法不参与非零证明。

**有限拟合。** 对 $|\gamma_i|\le.18$ 且总增量约 $.006$，取 R268 的原五个角矩，加入原曲率和几何测度。两套实际暖场 G10 的有限数值谱误差 $.19785991$ 以下给 $E>.80214$，故 $(1.18)^2<3E$ 有大余量。原暖场最小相对面积约 $.91804423$，全部拟合速度满足 $\sigma_0/1.18>.5$。这两处浮点代入不是连续源的区间包围。SLSQP 共 87 次，原全 14 行总代价从 $.030876174230295685$ 移到 $.028727766643234138$；按实际新物理六 jet 和所有 $vx$ 求积权（即原 $dx$ 权乘 $v$）直接重算为 $.028727766643234145$。正钟在前端为恒等、末端后只作材料平移。G10/G11 的原 $x$ 逐索引保留，可区分相差一个二进末位的原点。首尾和局部球包的数值 guide 保留。该阶段改变度量，自己的位置接受计数从零开始。

| 新 g 下实际位置接受 | 两全 G10 组总代价 | G11 metric | G11 曲率 | G11 held |
|---:|---:|---:|---:|---:|
| 0 | .028727766643234145 | .193990134325 | 18.041388682 | .679595095 |
| 1 | .02539449956826352 | .196944431084 | 18.121810710 | .671939308 |
| 2 | .023963413394178925 | .202397831019 | 18.091790563 | .659638951 |
| 3 | .023503298051944354 | .199041591353 | 19.976590389 | .652581892 |

每步保持同一新 $g$，实际带状正规方程保留 4291840 行、6615 列、全部跨 Cartesian／跨角项、真实物理二阶 Sobolev 增量正则。G11 的 668×256 错移点含 540 个训练外径向标签。外部不动的前缀同样付全部观察值。脚本输出中 worstMetric/worstCurvature 同列 $x,s(x)$，原面积辅助报告 minimumPoint 的历史键 s 指求积标签 $x$。训练代价下降，独立峰及曲率仍远超目的，本次未提供同一场全闭 reach 或同 $g$ 加密收敛。

## 复算

在 scratch 重生所列 H65 父输入。令 `HELPERS` 指包含已发表来源脚本的目录，`SCRIPTS` 指课题脚本目录，`DATA` 指重生原 H65 缓存和父态的目录，当前工作目录须可写。实际会话 `Astra-visible-flex-2ecfcd69-20261128`，单进程单 BLAS 线程，三个命令均自然退出 0。

```bash
common=(--helpers "$HELPERS" --scripts "$SCRIPTS" --prepared "$DATA/polar-physical-H65-prepared.json" --parent "$DATA/polar-H65-two-space-design-step03-step01-state.json")
python "$SCRIPTS/2ecf-strong-new-material-clock.py" "${common[@]}" --delta .006 --bound .18 --output clock-H65-d006.json
python "$SCRIPTS/2ecf-strong-material-clock-exact-rank.py" --clock clock-H65-d006.json --prepared "$DATA/polar-physical-H65-prepared.json" --output clock-H65-d006-exact.json
python "$SCRIPTS/2ecf-strong-new-material-solve.py" "${common[@]}" --clock clock-H65-d006.json --observer "$DATA/polar-physical-H65-independent.json" --prefix clock-H65-d006-fixed --steps 3 --damping .012
```

| 身份 | 本次 SHA-256 |
|---|---|
| H65 prepared | `8d9e74861e74b19532f006b7b4cf2e3076d0127fe63530e5d99bd22b10d27f86` |
| 实际混合 own3 父态 | `b3f45552b07e8d9587c4ec05ea02fb749c3ed63beddda11f222c90bfc7b35c11` |
| 36 系数冻结角半径 | `52902e395f030eb515a7906e7c35993d05525f7bdbafd24137cf2d676818b55f` |
| H65 独立源 | `5bb17709d1a3d1ac7719c82e10ce515ab73cac3c3256d6f1a21b7fbb9a36ff7f` |
| 新钟报告／固定定义 | `0644e15d87660376419fbdedec0b8f97319f5a83bdfd9c3cca76b72da3e971eb` ／ `a83089cb171e1488203fff31b72ab3ca59e5b138807b374ee5e98ada34765624` |
| 有理秩、长度回执 | `89a7bfb1e55b76b0be4a4d36f89378d1ec53656428f61e855e38c7469a31e835` |
| 初值 | `28aa4c0b872bd98586d383519bb716cfc152bab3d174891003c136b206b61961` |
| 三个接受态，依次 | `5fdcd0a837ef809adb9d7dfd5a6f44a592ec642518042edd8bc011b0932c56a3` ／ `f7e85d91c09d27cf1c78d92c66f1a637fc9ea3ed0bd507cb65b212f7cfc8e5b8` ／ `447a40d135cba9c857dc0e74eb4c8299f47c84842ee47d89fe95026ca10e4f9e` |

这些回执含时间或本次父文件 SHA；重生时应比较物理参数、场和数值，不能要求墙钟时间逐字相同。可重算数组及场不入库。
