# 精确椭圆柱入口与始终向内的回折参考

**状态：启发式求解设计；入口公式和参考闭合公式已证明，尚未得到准确非圆连接。** 下列开发检查只评估几何和已经保存的候选，不运行新的非线性最小二乘。后续真实连接求解使用本公开仓库的 Actions。

## 1. 已保存 folded 候选的误差定位

`scripts/core_tail_saved_audit.py` 在 $161\times128$ 网格重新评估三个保存候选，不改变系数或度量。结果为：

| 候选 | 最大相对度量误差 | 残差角模 2 的能量占比 | 角模 3 占比 | 最大值径向位置 $u=s/L$ |
|---|---:|---:|---:|---:|
| unit，原第 05 组 | 0.02478673 | 0.6129 | 0.2566 | 0.15625 |
| Actions folded，$L=1.5$ | 0.10939206 | 0.5956 | 0.1757 | 0.18125 |
| Actions folded，$L=1.8$ | 0.11645046 | 0.6951 | 0.1712 | 0.14375 |

这里的最大值略高于原始 $81\times256$ audit，属于不同采样点的评估，不是新的优化或固定度量加密解。误差集中在靠近入口的第一个快速向负角摆动处，主要是已有的低阶角模。由此不能把失败归因于缺少角高频，更不能推出不存在连接；它说明仅增加角模并非本轮证据最支持的调整。

可复现输出为 `notes/core-tail-saved-residual-audit-20261114.json`。两份 folded 输入仍来自公开 Actions `43585440463`，来源 receipt 保存在原目录。

## 2. 精确椭圆柱入口

设椭圆物理半轴 $A=1$、$B=0.3$，$m=1-(B/A)^2$，
$$a_0=\frac{2A}{\pi}\operatorname E(m)=0.6980392675284104\ldots.$$
选参数 $\varphi$ 满足
$$A\operatorname E(\varphi\mid m)=a_0\theta.$$
令
$$\gamma(\theta)=(A\sin\varphi,-B\cos\varphi,0),\qquad
v(\varphi)=\sqrt{A^2\cos^2\varphi+B^2\sin^2\varphi}.$$
于是
$$\varphi_\theta=a_0/v,\qquad
\varphi_{\theta\theta}=-\frac{a_0^2(B^2-A^2)\sin\varphi\cos\varphi}{v^4}.$$
解析求导给 $|\gamma_\theta|=a_0$。准确中央柱段为
$$X(s,\theta)=\gamma(\theta)+s e_z,\qquad0\le s\le h_0,$$
其度量恰为 $ds^2+a_0^2d\theta^2$。在连接入口 $s=h_0$，完整径向位置二 jet 是
$$X=\gamma+h_0e_z,\qquad X_s=e_z,\qquad X_{ss}=0.$$
`core_to_tail_bvp.py --core-profile ellipse` 对每个实际角网格直接评估这些解析 jets；不先作傅里叶截面插值，也不调用混模 GC 积分。$h_0$ 通过 `--inlet-s` 设置，必须计入最后闭曲面的几何和总长度。

入口开发检查在 513 个角点上给：相对度量误差 $4.44\times10^{-16}$、$\gamma_\theta\cdot\gamma_{\theta\theta}$ 最大绝对值 $8.88\times10^{-16}$、弧长反演残差 $8.88\times10^{-16}$。椭圆的曲率半径范围是 $[0.09,10/3]$。

## 3. 不外鼓的两段回折与精确平尾

记 $S_5(t)=10t^3-15t^4+6t^5$。取 $0<\eta<\pi/2$，第一段长度 $L_1$，第二段长度 $L_2$，最后平段长度 $L_f$，并令
$$\beta(s)=\begin{cases}
\pi/2+(\pi/2+\eta)S_5(s/L_1),&0\le s\le L_1,\\
\pi+\eta-\eta S_5((s-L_1)/L_2),&L_1\le s\le L_1+L_2,\\
\pi,&L_1+L_2\le s\le L.
\end{cases}$$
其中 $L=L_1+L_2+L_f$，
$$a(s)=a_0+\int_0^s\cos\beta(\sigma)d\sigma,
\qquad z(s)=h_0+\int_0^s\sin\beta(\sigma)d\sigma.$$
因此 $a'^2+z'^2=1$，$a'\le0$。所有拼接点的 $\beta$ 一、二阶导数为零，入口和末端都具有需要的完整位置二 jet。第一段越过 $\pi$ 时，环向法曲率换号一次；这里不声称这自动解除圆基底的一阶刚性。

对固定比例 $\lambda=L_1/(L_1+L_2)$，设
$$q=-\lambda\int_0^1\cos\{\pi/2+(\pi/2+\eta)S_5(t)\}\,dt
-(1-\lambda)\int_0^1\cos\{\pi+\eta-\eta S_5(t)\}\,dt.$$
要从 $a_0$ 收到 $r_c$，令 $\Delta=a_0-r_c$，则
$$L_1+L_2=\frac{L-\Delta}{1-q},\qquad
L_1=\lambda(L_1+L_2),\quad L_f=L-L_1-L_2.$$
正长度条件恰为 $\Delta<L<\Delta/q$。实现不再需要最小二乘或多维边值求解来关闭圆参考的半径。

**不能用周长半径差代替真实材料位移。** 长轴核心点的 $x$ 坐标为 1，末端同一材料角的圆点是 $r_c$；所以任何等距连接都满足 $L\ge1-r_c$。若对应端点的真实空间弦长为 $d$，还必须 $L\ge d$。更一般地，若最大 $E$ 误差至多 $\varepsilon$，则 $d\le L\sqrt{1+\varepsilon}$，给出必要下界 $\varepsilon\ge(d/L)^2-1$。将整段抬高 $h_0$ 不改变这个连接内部的弦长条件。

例如小回折 $\eta=.2$、$L=.55$ 的紧凑参考虽曲率不大，对强椭圆的对应弦长却为 $.72388$，故 $E$ 误差至少 $.73225$。它不能作为准确连接候选。以下真正输入改用较大的向内回折角。

## 4. 两组实际待求解输入

末端 R128 平尾参数统一为 $r_c=.28$、平坦区外半径 $.26$、内切口半径 $.23$。这样给全曲面 $|y|\le.30$ 的候选支持见证留下余量；这些支持条件仍必须从实际非轴曲面检查，圆参考的半径 $a_0>.30$ 并不满足它。

| 参数或参考检查 | A | B |
|---|---:|---:|
| 柱段 $h_0$ | .19 | .23 |
| 连接长 $L$ | .75 | .80 |
| 过冲角 $\eta$ | 1.45 | 1.53 |
| 第一段比例 $\lambda$ | .70 | .67 |
| 活动长 $L_1+L_2$ | .6684009987 | .7368576415 |
| 末端高度 | .0887370093 | .0927053952 |
| 最高高度 | .3781252370 | .4260586170 |
| 参考最大主曲率样本 | 13.5584770 | 11.7975609 |
| 真实椭圆入口至圆尾的最大对应弦长样本 | .7270860976 | .7329732659 |
| 镜像圆参考与两平盘的法线弦半径样本 | .0737629049 | .0847652952 |

最后一行只检查**圆参考**；它没有检查待求的椭圆连接，也不是连续 reach 证明。所有几何检查可用 `scripts/inward_reference_geometry.py` 复现；数据在 `notes/core-tail-inward-reference-20261114.json`。

另一个非平凡圆控制将入口半轴同时改为 $.7$，直接使用完整 inward/Hermite 组装的零自由系数：最大相对度量误差 $1.24\times10^{-15}$，端口二 jet 误差 $2.78\times10^{-17}$。这只检查新实现的精确控制，不声称强椭圆情形有解。

## 5. 给公开 Actions 的命令

**新增端口曲率筛查：A不进入求解。** 准确目标度量的材料径向线是单位速测地线，入口切向为 $e_z$。若 reach 为 $\tau$，其环境曲率不超过 $1/\tau$，从竖直到水平最快转向给最大水平位移 $L-(\pi/2-1)\tau$（在 $L\ge\pi\tau/2$ 的情形）。这里真实横移至少 $.72$、中央长轴给 $D\ge2$，因此任务要求 $\tau\ge.06$，必须 $L\ge.7542477796$。A的 $.75$ 不够；这是精确等距极限的限制，不可直接把仅有C0小度量误差的场代入导数结论。

实际 Actions 改跑B和C，其中C为已有几何JSON的 $h_0=.25,L=.8,\eta=1.5,\lambda=.68$，圆参考法球弦样本`.08524744`、入口至尾弦样本`.73174386`。仍不把这些圆参考诊断当非轴 reach。

从仓库根运行。两个命令均为**设计**问题：它们允许径向度量控制变化，结果不能当作冻结共同度量后的加密序列。

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/core_to_tail_bvp.py \
  --core-profile ellipse --ellipse-major 1 --ellipse-minor .3 --inlet-s .25 \
  --background inward --length .80 --inward-overshoot 1.5 --inward-first-fraction .68 \
  --cut-radius .28 --flat-start .26 --cuff-radius .23 \
  --tail-plus 0 --tail-minus 0 --tail-plus-min -.1 --tail-minus-min -.1 --tail-angle-max .1 \
  --tail-height-min .05 --tail-height-max .6 --radius-floor .24 --radius-ceiling .9 \
  --radial-free 5 --modes 12 --angular 96 --radial-gauss 6 --inlet-angles 256 \
  --max-nfev 250 --out topics/visible-flex-new-mechanism/notes/core-tail-inward-C.json

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/core_to_tail_bvp.py \
  --core-profile ellipse --ellipse-major 1 --ellipse-minor .3 --inlet-s .23 \
  --background inward --length .80 --inward-overshoot 1.53 --inward-first-fraction .67 \
  --cut-radius .28 --flat-start .26 --cuff-radius .23 \
  --tail-plus 0 --tail-minus 0 --tail-plus-min -.1 --tail-minus-min -.1 --tail-angle-max .1 \
  --tail-height-min .05 --tail-height-max .6 --radius-floor .24 --radius-ceiling .9 \
  --radial-free 5 --modes 12 --angular 96 --radial-gauss 6 --inlet-angles 256 \
  --max-nfev 250 --out topics/visible-flex-new-mechanism/notes/core-tail-inward-B.json
```

在窄尾宽 $.02$ 上限制 $|A_\pm|\le.1$ 的理由是 $\max S_9'=630/256$，故平尾柱面的主曲率 $|\alpha'|$ 不超过 $12.3046875$。该界只控制这片独立的精确尾，不保证全曲面 reach。

## 6. 下一次实际结果的判读

首先看完整 $E,F,G$ 相对算子误差，端口二 jet、弧长反演或参考几何不能替代它。若误差仍不小，定位其径向位置及角谱，再选固定参考下的参数加密或改连接参数。若得到准确候选，才冻结共同度量，扩展为 `results/R3-mirrored-halfband-phase-family.md` 的闭相位族，检查真实全像集的支持见证、完整直径、上半带与平盘不相交及初始 reach。圆参考的好预算不会自动传递给非轴 field。
