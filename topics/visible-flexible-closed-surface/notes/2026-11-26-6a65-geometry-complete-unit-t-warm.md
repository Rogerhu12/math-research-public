# 完整新 half 的 C2 位置与单位 T warm 供应器

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

## 1. 交付范围和实际状态

[正 K Cauchy 尾消费](2026-11-26-6a65-geometry-actual-cauchy-tail-stops.md) 未到达完整圆 cut。这里不继续径向 IVP，而是提供一个包含真实中央柱、Cauchy 前缀、R137 coast、完整非 flat 右连接及 R205 真尾至平 cuff 的新全局 warm 函数，供 R201 的全半面单位 T 空间拟合。

两个入口分别为：

- [6a65-geometry-cauchy-unit-t-warm.py](../scripts/6a65-geometry-cauchy-unit-t-warm.py)：`WarmMaster.jet(s,u)` 返回完整 raw 位置两jets和 `Xssu`；`normalized(s,u)` 返回准确弧长/尺度定义的完整两jets，数值积分误差另列。
- [6a65-geometry-cauchy-warm-base.cjs](../scripts/6a65-geometry-cauchy-warm-base.cjs)：`createCauchyWarmBase(engine,a0)` 返回 R187/R196 可直接消费的 `a0/end/height/centralLength/segments/at(s)`；`at` 含 a、as、ass、z、zs、zss。

本次只是新输入，尚非合格等距核。完整表的 G 误差达到机器精度，右连接的 E/F、面积与曲率仍明确失败；不能把 G 自动准确称为全度量成功。

## 2. 全部物理片和端值

| 片 | 物理 s 范围 | f 端值及坡度 |
|---|---|---|
| 准确中央椭圆柱 | [0,.1015625] | f=a0，f'=0 |
| 真 Cauchy ramp 的 C2 位置表示 | [.1015625,.2815625] | a0 → 1.0175828380214686；0 → .15 |
| R137 coast | [.2815625,.3315625] | 1.0175828380214686 → 1.0250828380214687；f'=.15 |
| 新完整右连接 | [.3315625,1.0815625] | 1.0250828380214687 → .8；.15 → −1 |
| 原 R205 developed tail | [1.0815625,1.5615625] | .8 → .32；f'=−1 |

全部接点 f''=0；ramp 的内部函数仍为既有 \(f'=vS_9\)。中央半轴同 gap=1 强输入，a0≈1.0040828380214686。尾幅 A=.8746432018013935，真实平 cuff 高度 Z=.51，位于 R219 的已证明窗口中。

这里把右长度改为 .75，不能继承短正 K turn 的同 g 身份。物理 cut=1.0815625；附加真实 R205 尾后平 cuff=1.5615625。R201 核参数拟合取 s≤cut；cut 后的附加样本用于检查真实尾和 cuff，而不是可任意改变的另一个连接。

## 3. C2 位置定义没有省略端迹

真实 ramp 用 191 阶旧 hybrid GC、768 native 角点重新运行，以 33 个径向节点存 P=X、V=Xs、A=Xss 的同一有限 Fourier 圆周函数。内部节点来自实际 DOP853 dense interpolant；不是另一条 PDE 解。相邻节点之间用 Cartesian quintic Hermite 插值，因此共有的 P/V/A 函数给出准确的 C2 拼接定义。

最后一个 ramp 格长度为 .005625。其末端 P/V/A 明确替换为 R137 新准确形式入口函数，避免保留一个未支付的拼缝。替换前的完整两jets差为：

| 量 | 有限最大差 |
|---|---:|
| X | \(1.204\cdot10^{-13}\) 以下 |
| Xs | \(5.42\cdot10^{-10}\) 以下 |
| Xss | \(1.433\cdot10^{-7}\) 以下 |
| Xu | \(6.39\cdot10^{-12}\) 以下 |
| Xsu | \(3.89\cdot10^{-8}\) 以下 |
| Xuu | \(9.79\cdot10^{-10}\) 以下 |

这是一条新的小修补位置场，不再声称该最后格是未经改变的 GC 演化。补过的前缀另检查 32 个真正格内中点、256 角点，raw 全度量峰约 \(4.140\cdot10^{-10}\)，自己主曲率峰约 9.77651。记录节点上的误差约 \(10^{-12}\)；二者明确区分，没有用节点误差代替格内检查。

右连接用同一个 R137 完整出口和 R205 外 cut 的 P/V/A 作 Hermite 插值。两端所需的所有角导数从同一 master curve、材料反函数或 R205 原 C/H 积分推得，未独立投影端口。最后尾部在所有半径都使用原 `.34/.8` S9 profile；半径变小时不把其过渡宽度从 .46 擅自改小。到 r=.32 时它确实是高度 Z 的平环。

## 4. 新 g 的平 cut 正则性

最初曾使用简单 quintic scalar f。它虽有 f''cut=0，却不足以保证旋转参考的 Zss→0。本次最终表和 JS base 使用同一更平滑的坡度定义。

在右段 t∈[0,1]，令

\[
q(t)=(1-\beta)S_9(t)^2+\beta S_9(t)^3,
\qquad f'=v-(1+v)q(t).
\]

有准确积分

\[
I_2=\frac{38251}{92378},\qquad I_3=\frac{17141}{46189}.
\]

以 \(f_b=1.0250828380214687\)、L=.75、v=.15 定义

\[
J=\frac{v-(.8-f_b)/L}{1+v},\qquad
\beta=\frac{J-I_2}{I_3-I_2}\simeq .5276428813895414.
\]

因此准确积分到 fcut=.8。q 单调从 0 到 1，故 f' 始终在 [−1,.15] 内；两端 f' 的前四阶导数为零。特别在右端 \(1+f'=O((1-t)^5)\)，旋转参考 \(z_s=\sqrt{1-f'^2}\) 与 \(z_{ss}\) 都趋于零，可 C2 接到原平 cut。JS 实现使用显式 16 点 scalar、32 点 height Gauss 求积；连续余项未认证。

JS base.height 的本轮数值为 .8894838920546868。因此在这条新 g 中，若真实 Z=.51，R201 cut-height 列初值必须为

\[
.51-.8894838920546868=-.3794838920546868.
\]

不能借旧 B32 或旧长度时钟的 base.height。rho 的新设计初值为零。Python 与 JS 在 105 个实际物理点的 a/as/ass 最大差分别小于 \(2.3\cdot10^{-16}\)、\(1.3\cdot10^{-14}\)、0。

## 5. 全角弧长归一和完整两jets

对任一 raw 正则闭角曲线 X(s,v)，令 h=|Xv|、a=周长/(2π)，以准确积分定义

\[
u=\frac1a\int_0^v h(s,\xi)d\xi,
\quad C=\frac{\int Xh\,dv}{\int h\,dv},
\quad \lambda=f/a,
\quad Y=C+\lambda(X(s,v(s,u))-C).
\]

则 Y 是闭合曲线，\(|Y_u|=f\)；单位 T 为 \(X_v/h\)。这一步不是只把切向量的长度归一后继续沿用旧位置。

完整 s 导数同时计算。例如

\[
v_s=\frac{u a_s-\int_0^v h_s}{h},\qquad
v_{ss}=\frac{u a_{ss}-\int_0^v h_{ss}-2h_sv_s-h_vv_s^2}{h},
\]

\[
h_{ss}=\frac{|X_{sv}|^2+X_v\cdot X_{ssv}}h-rac{(X_v\cdot X_{sv})^2}{h^3}.
\]

实现将这些式子、C 和 λ 的两阶导数全部送进 Y 的 Xs/Xss/Xsu/Xuu，不丢混合导数。数值积分使用 1024 角 Fourier primitive，真实反函数残差阈值为 \(5\cdot10^{-13}\)。尚未证明该求积的连续余项。

在准确 central/coast/tail 片，上述变换为恒等。准确端口上 h=f、hs=f'、hss=f''，故 λ=1、λs=λss=0 且材料回收在 s 方向的前两阶导数为零；变换保留完整端口两jets。这说明新全场 C2 定义与实际 R205 cut/cuff相容，而不是仅有值相接。

## 6. 真正全表和还很大的右段缺陷

最终自然 exit 0 导出 79 个径向截面、128 个全周期角点，实际耗时约 69.32 秒。输出键为 s、u、rawX、rawXu、X、Xs、Xu、Xss、Xsu、Xuu、unitT、mean、f、fs、fss。向量表尺寸为 79×128×3，mean 为 79×3。

| 实际有限量 | 最终 flat-cut 版本 |
|---|---:|
| 全场最大 G/f² 误差 | \(1.12\cdot10^{-15}\) 以下 |
| 128 点单位 T 离散均值闭合 | \(5.15\cdot10^{-13}\) 以下 |
| 全度量最大误差 | 1.458451113 |
| 最大自己主曲率 | 1309.053956 |
| 最小面积元 | .0525207666 |
| 最大包球半径 | 1.503651802 |
| 最大绝对 y | .8526546624 |
| 最大 z | .5421885337 |
| 最小 held 标记距离 | .6329811519 |

最大 E 误差在 s=.8471875、u=0：E=2.45845111，而 F/f 约为零，Xs≈(−1.56012,0,−.15647)。最大曲率和最小面积在 s=.8003125、u≈2.25802：E=.2440443、F/f=−.4914543，Xs 几乎沿角曲线切向；它法于角曲线的速度约 .050。这个缺陷不能靠 G 自动准确消失。全场 max |Tz|≈.52295，θ/φ 角图没有接近竖直极点。

高度和 held 也仍未通过完整强几何门槛。此表的用途是提供新的完整输入和可检查方向；root 的 R201 全参数拟合与 LM 需要另作真实记录，不能借这份表声称已解决右连接。

## 7. 复生与接口身份

先按真实 Cauchy 尾脚本的 `--modes 191 --exact-coast --curve-degree 95` 分支生成 coast master；它即便未完成尾部，也保存了先前真正得到的完整 coast master。然后：

```bash
OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-geometry-cauchy-unit-t-warm.py \
  collect "$SCRATCH_INLET_JSON" "$NEW_RAMP_PREFIX"

OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-geometry-cauchy-unit-t-warm.py \
  export "$RAMP_MASTER_NPZ" "$COAST_MASTER_NPZ" "$NEW_WARM_PREFIX" \
  --angles 128 --quadrature 1024 --Z .51 --amplitude .8746432018013935
```

完整 normalized 样本 SHA 为 `3675506acd0150593e9c1f21bd24e2f90990103be88bf56b4e9adecd08a4b5c0`；报告 SHA 为 `7a3dede0e4a9b141dc3dfb234b871a399ce35866a506205714e8fc020025c4ed`。两个源 master SHA 分别为 `888430b0550d9d8a30f04526d2f348f8c5852e1464125cc9101e79dc2b1600de` 和 `8a42012d2f7fc377b47284aeb64accb3e4e9bcd670516b0aae2844759a731987`。

Python 源码 SHA 为 `75dfcbd01870df003e6814b9cb07a992df3713e01b9fcedda432a57c4569463b`；JS base 源码 SHA 为 `b42a5213a12de4c11d4db9cb35272db5023da9511db61193aaa1b52b22e5ede9`。所有原始状态、master 和样本只留 scratch，不进 git。
