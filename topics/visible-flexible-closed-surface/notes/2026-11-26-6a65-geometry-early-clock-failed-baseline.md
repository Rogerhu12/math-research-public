# 外段长度保持 .05、时钟集中前 35%：实际失败基线

2026-11-26。实际 OS 退出码 0，5.083 秒，1 次完整 value，0 次 normal/LM。此输入没有改善本轮实际峰值或积分，因此没有继续其 LM 分支。

## 新准确时钟及端口

原外段坐标为 $t\in[c,S]$，令 $L=S-c$、$\Delta=.05$、$\beta=.35$，使用截断九次函数

$$
\sigma_\beta(t)=t+\Delta S_9((t-c)/(\beta L)).
$$

当 $t\ge c+\beta L$，它准确等于 $t+\Delta$；导数始终不小于 1。半径仍由 $a_\beta(\sigma_\beta(t))=a_0(t)$ 定义，单位速旋转参考高度用

$$
Z_\beta(\sigma_\beta(t))=c+
\int_c^t\sqrt{\sigma_\beta'(v)^2-a_0'(v)^2}\,dv
$$

重建。两端时钟一阶导数为 1、二阶导数为 0，中央和真实 R205 切口两 jet 保持；$\beta<1$ 时切口前还留有完整的恒定平移邻域。内部时钟终止点新增到全部 quadrature cuts；$S_9'$ 的四阶消失保证该点同样保持 $C^2$。本轮改变 $\beta$ 是新物理 g 设计，不是同 g 加密。

实现给默认 $\beta=1$ 保留原数学函数，显式传入其他时钟时才允许迁移。读取一个已保存时钟后若未显式允许转换，改变它会报错，避免把同一 $\Delta$ 误认成同一 g。

## 从真正第三态保持实际 cuff 高度

父态是 gap1-delta005-R215-lm03-state.json，SHA-256：

    90f335c1605f4ef54115561d74ba5246d3f150ff92929034d903d70d1f164e11

真正旧参考为 $\Delta=.05,\beta=1$，不是未伸长的原始 B32。程序重新计算旧、新背景高度，并取

$$
z_{\rm cut,new}=z_{\rm cut,old}+H_{\Delta,1}-H_{\Delta,.35}.
$$

实测旧高度 $.7969149179189924$，新高度 $.7937006343177616$，cut 系数补正 $+.003214283601230772$。因此实际 cuff 高度 $Z=.5384471976304932$ 与尾弯幅 $A=.8454837980191046$ 均保持，实际高度迁移差严格返回 0。原始基准高度 $.743536989256208$ 未误用来补正。

新原坐标时钟支撑终点是 $.376001507455092$，总物理端点仍为 $.9356739498716915$。全部原 1025 通道保留，完整 R211 四次 curvature、四次 metric $\tau=.05$ 和 R215 几何目标重新评价。

## 实际比较

| 量 | 真正父态 $\beta=1$ | 新基线 $\beta=.35$ |
| --- | --- | --- |
| 总平方目标 | $.2427674894$ | $.5132306112$ |
| 最大相对 metric | $.7389708287$ | $.8055184060$ |
| 二次 metric 平方积分 | $.0105954835$ | $.0153130369$ |
| 额外四次 metric 平方积分 | $.1972645612$ | $.4675762241$ |
| 最大曲率样本 | $17.01381050$ | $17.28550454$ |
| 最小 held 距离样本 | $.6251744630$ | $.6240559177$ |
| 最大 $|y|$ 样本 | $.8349021547$ | $.8359392820$ |

新 metric 最坏点为 $s=.2353722306162241,u=0$，$r_E=.8055076174574833$、$r_F=.0029479464948372757$。峰值与积分均恶化，所以没有用新目标下降或采样迁移掩盖这一结果。该测试仅复制有限系数到新时钟定义，没有声称对旧完整位置场做了精确坐标回拉；两者是不同初始化。

## 运行身份

入口及本次 SHA-256：

- 6a65-geometry-gap-length-value.cjs：88bc3019fe8fdabe4c000b677cfe00a18c0856ea503df5eece22942f68ed139c。
- 6a65-geometry-outer-length-design.cjs：181d243c16366072d2135a821a780f5f9b08ede280ee5828ec216c8feb8a72f6。

调用是原 value 命令末尾显式添加 $\beta$：

```sh
node --expose-gc --max-old-space-size=128 \
 topics/visible-flexible-closed-surface/scripts/6a65-geometry-gap-length-value.cjs \
 topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
 /tmp/visible-flex-6a65e705/geometry-work/gap1-delta005-R215-lm03-state.json \
 /tmp/visible-flex-6a65e705/geometry-work/gap1-delta005-beta035-value01 1 .05 .05 .35
```

raw seed SHA-256 为 8a3e2e9099e559db29f22980e724215f3555283a98bdb520c81cffd201a089aa；raw report SHA-256 为 8f26714bf6a176389613429f1eadf2da8bf4518a8325e74465f2a295e517a024。可重算 raw 输出留在 scratch，不进入 Git/artifacts。它不是完整 metric、reach 或任何完成条件的证书。
