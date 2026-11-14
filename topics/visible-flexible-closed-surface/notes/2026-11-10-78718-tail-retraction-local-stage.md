# R95 两个旧 W22 入口的单段低 floor 延伸

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：实际有限浮点探索。** 本记录补充 R95 的固定节点 root 比较，回答这两个入口在较低数值 floor 下是否立即失去有限 ODE 的可延伸性。没有做整套 shooting、DN 或 BVP，没有修改任何生产进程、物理参数、原目标高度或完成标准。

## 输入和真正执行的范围

使用与 R95 相同的 fast02 W22 初始几何 warm、其实际 trial8 保存节点及原 stage35 物理 profile。原 trial8 步长是1/256，stage35 的输入是保存节点36。

两个入口为：

1. 原 $\pi$ 直线 trial8，直接读取该保存文件；
2. 用同一个已恢复 Newton 方向和同一个1/256步长，按 R95 v2 得到的 Q/L 回缩入口。

两者均用原 W22/N512 的同一个 Fourier-root/split-flux 有限 RHS，原 cusp integrationGrid 和 RK4。这里只将该局部研究 engine 的 projectionFloor 设为 $10^{-10}$，另开无生产副作用的对象。分别使用每小段32步和64步，全部只走 stage35 的第一个且当前实际所用 profile，x从0到1。没有把较低 floor 接进当时或后续主求解。

每次 RK 的 a/b/c/d 场评价都实际调用完整 root，并记录 A、D、S；没有只在主节点上评价。R86(17)–(19) 的 Gauss 必要形算子也在这些实际 root 的全部512角点计算：

$$
b=\frac{wU}{r\sqrt D},\qquad
c=\frac{wA}{r\sqrt E\sqrt D},\qquad
a=\frac{K_g+b^2}{c}.
$$

这个量表示“若保持该高度一jet并精确等距，Gauss所要求的形算子”；它不是把有限投影 ODE 的实际二jet当成精确等距形状。这里还只有有限角点、有限 RK 场的样本，不是整个二维域的曲率上界。

## 实际结果

四个局部轨道全部走到 x=1，没有 root 或 RK 失败：

| 入口 | 每段步数 | 全部场/角样本最小A | 最小D | Gauss必要形算子样本最大值 | 段末A |
|---|---:|---:|---:|---:|---:|
|原π直线trial8|32|0.0014904603|0.99992785847|0.76688851|0.2224890746|
|原π直线trial8|64|0.0014904603|0.99992785845|0.76688851|0.2224902466|
|同方向Q/L回缩|32|0.0030570586|0.99992786025|0.37349395|0.1947164347|
|同方向Q/L回缩|64|0.0030570586|0.99992786023|0.37349395|0.1947174111|

32/64步分别记录128/256次实际场评价。四条轨道的最小 A 都在入口，随后本段恢复到较大的 A。因而原 `.05` floor 对这个具体 trial 的拒绝，不能解释为“放松这一数值门后，本段立即撞上 A=0”。这只是本例的实际局部事实，不是一般低 floor 都安全，也没有证明整尾能连接目标。

两种径向分辨率的段末差仍需如实保留：

- 原π直线：末A差约 $1.17201\cdot10^{-6}$，Q系数最大差约 $1.30245\cdot10^{-11}$，规范动量π最大差约 $3.23467\cdot10^{-6}$。
- Q/L回缩：末A差约 $9.76349\cdot10^{-7}$，Q系数最大差约 $1.37170\cdot10^{-11}$，规范动量π最大差约 $3.38991\cdot10^{-6}$。

规范π不是物理 metric 单位。这些差既不能直接充当 metric 误差，也没有达到一份径向连续精度证书所需的说明。本记录不据此替换主线 S32、声称已收敛到原tol，或将该局部输入变成全尾初猜成功包。

## 可复现记录

程序：[78718-tail-retraction-local-stage.mjs](../scripts/78718-tail-retraction-local-stage.mjs)，5860 B，SHA256 `580276e8147da33340f241edaf3bc2410a9c35d93fce3c9cddec26a3f206132e`。

报告：[2026-11-10-78718-tail-retraction-local-stage-01.json](2026-11-10-78718-tail-retraction-local-stage-01.json)，210683 B，SHA256 `efc00fba61cd3072773e8fa5f07ae3c75b7f10d0442558989744ecc03827d58f`。它包含小段所有场的标量和两组段末状态，未把数组读入对话。

实际回执：`2880d8/session51711 → d6c653 exit0`，约11.101秒。0 DN、0 BVP、0全 shooting 残差评估；只有上述四次单段 RK。

命令使用现有真实来源环境 `VISIBLE_FLEX_SOURCE_ROOT=<topic>/repro/source-root`、`CLOSING_TAIL_CACHE=<topic>/repro/source-root/topics/large-amplitude-twist-flex/scripts`，然后运行：

```sh
node topics/visible-flexible-closed-surface/scripts/78718-tail-retraction-local-stage.mjs \
  --config topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-02-tail-config.json \
  --trial topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-02_tail-trial-call1-iteration0-trial8.json.gz \
  --out topics/visible-flexible-closed-surface/notes/2026-11-10-78718-tail-retraction-local-stage-01.json
```

报告应使用新输出路径重生。当前主线已另从冷的较小 H 进行真正延拓；本局部探索不代替它，也不预判后续失败或成功。
