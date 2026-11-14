# 同一度量的 S11 弯平尾：完整端口与独立 frame runner

2026-11-14，mechanism。本文记录一个新的物理尾部与可运行实现。旧的五个 frame、ellipse、seed、enriched、audit 模块保持原字节；**没有本地评价真实研究候选，也没有构造出闭等距曲面**。真实回放、求解和精化由公开仓库自己的 Actions 运行。

准确尾的度量、帽内单射、全部尾内法弦与条件球预算已在 [R40](../results/R40-bent-flat-tail-normal-chord-and-ball-budget.md) 独立证明。这里主要支付完整标量 jets、共同中心积分和新 runner 的身份与导数接口。

## 1. 固定物理定义与共同高度

本次参数为

\[
r_c=11/50,\quad w_b=27/500,\quad r_f=137/500,\quad A_b=1/4.
\]

\(w_b\) 是弯曲开启的 Cartesian 宽度，区别于中央椭圆柱半宽 \(w_c=1/50\)。令

\[
S_{11}(x)=462x^6-1980x^7+3465x^8-3080x^9+1386x^{10}-252x^{11},
\]

并在 \(x\le0\) 延为 0、\(x\ge1\) 延为 1。定义

\[
\alpha(y)=\operatorname{sgn}(y)A_b S_{11}((|y|-r_c)/w_b),\quad
Y(y)=\int_0^y\cos\alpha(v)\,dv,\quad H(y)=\int_0^y\sin\alpha(v)\,dv.
\tag{1}
\]

两侧 \(\sigma=\pm1\) 的准确尾为

\[
P_\sigma(r,\theta)=
(r\cos\theta,Y(r\sin\theta),\sigma[h-H(r\sin\theta)]).
\tag{2}
\]

连接参数 \(t\) 从核心指向帽，开放尾上 \(r=r_c+L-t\)，所以 \(r_t=-1\)。源码保留旧标记 `s` 代表这个 \(t\) 导数；不把它与极坐标的正半径导数混用。

这里 \(h\) 不是每一截面独立的平移。R28 的同一个中心函数满足

\[
X=z_c(t)e_z+a(t)\Pi T,
\qquad z_c(0)=\sigma w_c,\qquad z_c'=\langle V_z\rangle.
\tag{3}
\]

由于准确尾上
\(a\Pi T=P_\sigma-\langle P_\sigma\rangle\)，其唯一高度常数是

\[
\boxed{h=\sigma z_c(L)
=\sigma z_c(t)+\langle H(r(t)\sin\theta)\rangle.}
\tag{4}
\]

右式的任意两个尾截面给同一个数。实际数值审计固定 \(h=\sigma z_c(L)\)，把所有尾圈与这个唯一 \(P_\sigma\) 比较，另报其他尾圈右式的求积偏差。它不通过逐圈重置 \(h\) 消掉误差。

实现中 \(w_b\) 准确取 `seed.length_exact * seed.flat_fraction_exact`。当前同一旧度量具有 \(L=9/10\)、flat fraction \(3/50\)，故恰为 \(27/500\)。外半径从这两个准确有理数与 \(r_c\) 相加定义，不借用另一个不匹配模型的 \(.274\) 预算。

## 2. 全角标量支与完整二阶数据

记 \(s=\sin\theta,c=\cos\theta,q=\alpha(rs)\)、\(C=\cos q,S=\sin q\)、
\(d=(1-c^2S^2)^{1/2}\)。准确单位正交目标为

\[
T=(-s,cC,-\sigma cS),\qquad
V=(-c,-sC,\sigma sS).
\tag{5}
\]

R28 的一个固定连续 lift 是

\[
u=\arctan\frac{sc(1-C)}{s^2+c^2C},\qquad
v=-\frac{\sigma cS}{d},\qquad
\beta=-\sigma\pi+\sigma\arctan(s\tan q).
\tag{6}
\]

分母以及 \(d\) 都至少为 \(\cos(1/4)>0\)。两个 arctan 使用主支便连续，不逐点 unwrap 或任意加减 \(2\pi\)。\(u,v\) 为 \(\theta\) 的奇函数，\(\beta\) 为偶函数，三者均为 \(\pi\) 周期。水平分量的平均由两重旋转对称消掉；\(T_z\) 的平均由反射奇性消掉。这里没有误称整个 \(T\) 在 \(\theta+\pi\) 下反号。

从 (5) 直接微分给

\[
V_\theta=-T+rT_t,
\quad R=V_\theta-a'T-aT_t=0
\quad(a=r,\ a'=-1).
\tag{7}
\]

位置 jets 令 \(a_1=\alpha'(rs)\)，有

\[
P_t=(-c,-sC,\sigma sS),\qquad
P_\theta=(-rs,rcC,-\sigma rcS),
\]

\[
P_{tt}=(0,-s^2Sa_1,-\sigma s^2Ca_1),
\]

\[
P_{t\theta}=(s,-cC+rscSa_1,\sigma cS+\sigma rscCa_1),
\]

\[
P_{\theta\theta}=(-rc,-rsC-r^2c^2Sa_1,
\sigma rsS-\sigma r^2c^2Ca_1).
\tag{8}
\]

`bent_flat_tail_port.py` 逐式实现 (8)。标量部分用一个小的二变量 Taylor 商环
\(\mathbb R[dt,d\theta]/(dt^3,d\theta^3)\)，系数含阶乘归一化。初值为 \(dr/dt=-1\)、\(d\theta/d\theta=1\)。总次数四的精确链式运算足够返回
`value,s,ss,theta,st,tt,ss_theta,ss_thetatheta`。
所有 \(\alpha\) 导数用 \(S_{11}'=2772x^5(1-x)^5\) 的 Leibniz 公式评价，负半轴正确带上 \(\operatorname{sgn}(y)^{k+1}\)。这不是角向有限差分。

\(Y,H\) 的准确身份是 (1) 的积分。代码的 Gauss 求积只评价该身份，明确不作为区间误差证书或另一拟合模型。

## 3. 右端 Hermite 拼接与不变的自由空间

新 `frame_collar_bent_tail.py` 继承已冻结的 `EnrichedProblem`。核心、固定径向度量、原入口 Cauchy 基场、B 样条结点、旧五个材料角模、三个椭圆相位角模、\(u_{\rm core}\) 方向全部不变。当前未知数仍为

\[
9(9+8+9)=234.
\]

设活动区间长度为 \(\ell\)，归一坐标为 \(x\)。沿用旧左端 S9 基函数 \(H_0,H_1,H_2\)，其对应左端 value/first/second jet。新的右端基为

\[
\widetilde H_j(x)=(-1)^j\ell^jH_j(1-x),\qquad j=0,1,2.
\tag{9}
\]

其中 value 基在代码中使用旧的等价 \(H_{01}\)。第 \(d\) 个物理径向导数的权重是
\((-1)^{j+d}\ell^{j-d}H_j^{(d)}(1-x)\)。在旧基场上叠加“新右端减旧右端”的 value/s/ss 函数；\(\theta\) 导数同时叠加 theta/st/ss_theta 函数。入口 0–4 阶基场不受此项影响；自由场仍只硬锁端点 0–2 jets，不能说所有未知都锁住高阶 Cauchy 数据。

在整个开放尾 \(t\ge t_f\)，代码直接使用 (6) 的准确标量场，且自由 B 样条在那里准确为零。因而完整目标 frame、位置和两 jet 在数学定义上是 (2)，并与内侧平盘 \(r\le r_c\) 匹配。未来 C² 接缝需审计同一准确 \(\Pi\) 定义；有限 FFT 值有独立截断误差，见 §6。

这改变了物理端口和基场，**不声称新初态与旧几何相同**。它保留旧 234 个准确 binary64 有理系数作为新初态，既不重新投影成旧 64 个系数，也不裁剪、拟合这些系数。

## 4. 同一 g 与严格回放身份

新 loader 接受旧 `mixed-ellipse-frame-collar-v1` 报告，依次核对：

1. 当前旧五源码 SHA 与报告完全相同；
2. 报告内原 baseline 的准确核心、端口、seed 和度量身份能够原样回放；
3. 原 enriched 的完整 space、角基顺序、234 个准确有理系数及 binary64 数组一致；
4. 完整 metric dictionary、shape dictionary 与原数学状态 SHA 一致；
5. 新问题的完整 metric dictionary 与旧问题相同，未知数布局也相同。

新的物理模型另存尾身份、完整端口/空间模型身份、七个实现 SHA，以及实际所选系数的准确有理数。最终有限精化固定这些系数与同一度量，不重选物理参数。

公开 Actions 先在旧物理模型中只读回放原 234 态，记录真实球最大值及位置，并在网格相同的情况下与旧报告摘要比较。这一步没有新尾、没有重新优化。随后才将同一系数装入新尾模型并单独记录新的初始 cost。原 disk-strip/height 目标的 cost 与新目标不作直接下降比较。

## 5. 新的活动形状目标

当前采用 R40 的条件充分域

\[
|X|\le R=101/100,\qquad |X_y|\le p=19/50.
\tag{10}
\]

若完整闭面都在这个域中，核心含 \((1,0,\pm w_c)\)，相位 \(\pi/2\) 的支持见证给

\[
D\le101/50,\quad \delta_{\rm hold}\ge31/50,
\quad\delta_{\rm hold}/D\ge31/101>0.3,
\quad\operatorname{diam}(H)/D\ge22/101>0.2.
\]

\(\tau=61/1000\) 已大于 \(0.03D\) 的上界要求。这里的 \(H\) 可取准确固定的内侧闭圆盘，直径 \(22/50\)。这些都是**以完整面包含和 reach 支付为前提**的预算，不是当前计算的认证结论。

优化只加入三项 smooth-positive 残差

\[
|X|^2/R^2-1,\quad X_y/p-1,\quad -X_y/p-1,
\]

每项乘 \(2/\sqrt{N_rN_\theta}\)，积分性三分量同样除以 \(\sqrt{N_rN_\theta}\)。球项参数导数准确为 \(2X\cdot dX/R^2\)，条带项为 \(\pm dX_y/p\)。旧椭圆包含及 \(|z|\le.45\) 仅保留为 legacy 诊断，不再进入活动目标。整个残差共六个标量分量，234 列 dense Jacobian 在 \(61\times192\) 网格约为 125.5 MiB；运行时中间数组与求解器工作区另计。

没有为跨半带、帽与连接器的距离新增未经讨论的罚项。输出保留单一帽高、真实坐标范围、min(side*z)-core_width、曲率、面元和尾重构误差。未来仍需 R30 类型的全片点对证书。

## 6. 人工开发检查与真实数值误差

两个 `--check-only` 都只使用人工较圆的椭圆/尾，未优化。端口脚本核对位置全二 jet、标量到 ss_theta 的链式、反射/周期、准确 S11 端点有理 jets，以及两个固定 Gauss 阶数的积分比较。

runner 的正、负两侧完整方向 Jacobian 相对误差分别为约
\(4.50\times10^{-9}\)、\(7.51\times10^{-9}\)；st/ss_theta 的角差分比较约 \(3.72\times10^{-10}\)。原系数逐位回放、度量逐位相同、完整 metric 身份相同、损坏源码 SHA 被拒绝均通过。左右端位置全二 jet 的最大误差约 \(3.43\times10^{-14}\)。

人工准确尾本身的 \(R\) 为机器误差量级，标量端口匹配准确。但在旧通用 FFT \(\Pi\) 评价下，非解析角阈值使粗网格的二阶位置误差可见。原始数据全部保留：

| 角节点 | centered position 误差 | \(X_t\) 误差 | \(X_{tt}\) 误差 |
|---:|---:|---:|---:|
| 192 | \(4.93\times10^{-9}\) | \(3.99\times10^{-6}\) | \(1.27\times10^{-3}\) |
| 384 | \(3.65\times10^{-11}\) | \(6.08\times10^{-8}\) | \(3.54\times10^{-5}\) |
| 768 | \(4.69\times10^{-13}\) | \(7.26\times10^{-10}\) | \(1.88\times10^{-6}\) |

这是同一个人工物理模型的有限比较，不是连续误差界，也不是实际研究候选的结果。没有改动旧 geometry 来隐藏误差。正式输出同时保存 384/768 角的原 \(\Pi\) 评价、独立准确 \(P\) 的全尾位置二 jet 差、同一帽高比较，并另把准确 \(t_f\) 与 seed 分段点加入审计网格。若实际误差仍重要，下一步必须固定物理参数继续细化；不能仅凭“check passed”声称度量或 reach 已达标。

## 7. 单 case 公开 Actions 命令

开发检查：

```bash
python topics/visible-flex-new-mechanism/scripts/bent_flat_tail_port.py \
  --check-only --out "$RUNNER_TEMP/bent-flat-port-check.json"
python topics/visible-flex-new-mechanism/scripts/frame_collar_bent_tail.py \
  --check-only --out "$RUNNER_TEMP/frame-bent-tail-check.json"
```

一个主求解，直接回放已发布 enriched 输出：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_collar_bent_tail.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --out "$RUNNER_TEMP/frame-ellipse-bent-flat-fixed.json" \
  --radial-nodes 61 --angular-nodes 192 --quadrature-order 4 \
  --audit-radial-nodes 121 --audit-angular-nodes 384 \
  --ball-radius 101/100 --strip-half-width 19/50 --bend-amplitude 1/4 \
  --field-bound 6 --max-nfev 250 --checkpoint-every 10 --checkpoint-seconds 60
```

输出额外有 `-old-ball-replay.json` 与持续更新的 `-checkpoint.json`。每 10 次残差评价或最长 60 秒保存当前最优点，不把第二个主求解塞入同一 lane 共享预算。

## 8. 范围

新的尾 \(\alpha\in C^5\)、\(P\in C^6\)，但在 \(r\sin\theta=\pm r_c\) 等阈值处不联合解析，因此 [R38](../results/R38-analytic-flat-collar-tail-rigidity.md) 针对旧旋转平尾与有限统一径向解析片的证明不直接覆盖这个物理端口。它没有证明新连接存在。

[R17](../results/R17-revolution-linear-flat-port-compatibility.md) 仍说明从零弯尾出发的特定小线性分支有相容障碍；固定有限幅 \(1/4\) 的新联合求解也没有因此自动变为可解。完整闭合、固定同一 g 的精化、全部嵌入和 reach 门仍未支付。这里交付的是可核算的准确端口与单次公开实验接口。
