# 完整极坐标正高度连接：真实二阶端口、同一目标度量基线与侧轴速度谷

日期：2026-11-26。会话：Astra-visible-flex-6a65 / geometry。

本条给出一个可在任意 $(s,u)$ 消费全部六个位置 jets 的新连接场。它保持 R233 已登记前缀、真实 R205 圆 cut 和平 cuff；没有把新场的周长定义成新的目标度量。端口与导数检查实际通过，整半核的独立有限基线已真实返回，但最坏度量误差为 $0.9914923$，自身曲率峰为 $747.8091$，仍不是合格完整核。所有连续全角不等式及全闭 reach 仍欠。

## 1. 输入、边界与冻结身份

保留前缀的两份本地重生 master 字节与 R233 相同：

- ramp SHA256：`0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7`；
- coast SHA256：`f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d`。

重生仅用于本次新位置输入，未重新登记旧结论。其进程实际自然退出 0，用时 $47.704613248$ 秒；新 report SHA256 为 `84c6d4f7d56971766a61db1c552cd783827ab1f11ed036f1256d890c87c6c751`。R233 的准确形式证书与 literal 浮点求值误差仍分开。

参数固定为

$$
c=0.1015625,\quad b=0.1815625,\quad
L=0.7956739498716915,\quad S=b+L=0.9772364498716914,
$$

$$
s_{\rm cuff}=S+0.48,\qquad
(A_q,B_q)=(1.4532280772048913,0.4032280772048914),
$$

$$
A_{\rm tail}=0.8746432018013935,\qquad Z_c=0.51.
$$

左端为 gap $1.05$、$v=.045$、长度 $.02$ 的 R137 coast 真出口；右端为原 R205 在 $r=.8$ 的真 cut。两端不是傅里叶投影后的独立 jets。$s>S$ 仍直接用原 $.34/.8$ 转角轮廓，直至真实 $r=.32$ 平 cuff。

目标 $g=ds^2+a_*(s)^2du^2$ 独立定义：$s\le b$ 保留原前缀标量；$b<s<b+.2$ 用已公开 compact-window 场的准确自然周长定义；窗口后保留公开 recipe 的零自由系数 Cauchy 半径。该构造与本次新极坐标场无关。

为了查询这个目标，本轮只从公开 candidate/recipe 构造明确的零参数定义文件；没有重算旧完整 value、旧 full cache，也没有把文件标成实际 CI checkpoint。其 SHA256 为 `dacede8a21b610d25fae4d0a5c3ffed6896b1693e9fbe7f7538234f970d7689f`，完整 1788 参数向量的 ECMAScript JSON SHA256 为 `15e86b1087587de2bf4bc7060dee7bb4b28c4f94fef6fbfd55895a360b329832`。接口仍明确 `interfaceProbeOnly=true`；这里只消费其数学目标定义，不借它的旧指标、接受数或 runner cache 字节身份。

## 2. 位置定义与完整端口

在共同平面极角 $\theta$ 下设

$$
Y(s,\theta)=
\bigl(\rho(s,\theta)\cos\theta,\rho(s,\theta)\sin\theta,z(s,\theta)\bigr),
\qquad X(s,u)=Y(s,\Theta(s,u)).
$$

端曲线的极角 $\phi_i(u)=\arg(P_{i,x}+{\rm i}P_{i,y})$ 使用连续 degree-one lift。由每个端口的同一 $P,V,A$ 及角导数求得 $\phi_i,\phi_{i,s},\phi_{i,ss}$。$\Theta$ 是连接这些完整径向二阶端迹的物理 quintic Hermite 多项式。

$\log\rho$ 在固定 $\theta$ 下也用完整径向二阶 Hermite 插值。指数形式自动保持 $\rho>0$；端点的 $\rho,\rho_s,\rho_{ss}$ 经链式法则严格恢复。固定 $\theta$ 的端口导数不是固定材料角的导数；源码显式消费

$$
u_s=-\frac{\phi_s}{\phi_u},\qquad
u_{ss}=-\frac{\phi_{ss}+2\phi_{su}u_s+\phi_{uu}u_s^2}{\phi_u},
$$

再转换 $P,V,A$。为给整个场的两个角导数，源码同一条曲线传播 $P$ 到 $u^4$、$V$ 到 $u^3$、$A$ 到 $u^2$，没有用分别拟合的 Fourier jets 替代。

高度速度为 degree $N=31$ Bernstein 多项式。记固定极角的端点高度为 $z_0,z_1$，速度为 $v_0,v_1$，加速度为 $a_0,a_1$，$\Delta z=z_1-z_0$。定义

$$
b_0=v_0,\quad b_1=v_0+\frac{L a_0}{N},\quad
b_{N-1}=v_1-\frac{L a_1}{N},\quad b_N=v_1,
$$

$$
b_j=B(\theta)=
\frac{(N+1)\Delta z/L-b_0-b_1-b_{N-1}-b_N}{N-3},
\qquad 2\le j\le N-2.
$$

令 $z_s=\sum b_j B_j^N(t)$，$t=(s-b)/L$，再从 $z_0$ 积分。由 Bernstein 多项式积分等于 $1/(N+1)$，高度差准确为 $\Delta z$；速度与加速度端迹也准确匹配。

因此这些函数的准确积分/反参定义在两端恢复原 $X,X_s,X_u,X_{ss},X_{su},X_{uu}$。实际求值仍有已经明示的数值求积与反参误差。完整源中同时给出六个解析链式导数，例如

$$
X_{ss}=Y_{ss}+2Y_{s\theta}\Theta_s+
Y_{\theta\theta}\Theta_s^2+Y_\theta\Theta_{ss},
$$

$$
X_{su}=Y_{s\theta}\Theta_u+
Y_{\theta\theta}\Theta_s\Theta_u+Y_\theta\Theta_{su}.
$$

## 3. 非折叠条件与已实付的端口预算

直接展开给出

$$
|X_s\times X_u|^2=
\Theta_u^2\left[
\rho^2z_s^2+(z_s\rho_\theta-\rho_s z_\theta)^2+\rho^2\rho_s^2
\right].
$$

因此只要在连续角域上 $\Theta_u>0$、$\rho>0$、内部 $z_s>0$，连接内部就是浸入。若各端曲线的极角 chart 是 degree-one，则该连接自身也单射：相同平面位置先决定 $\theta$，再由同一 $\theta$ 下严格递增的 $z$ 决定 $s$。这不自动排除它与其他整核部分或帽的交会，也不等于全闭 reach 证书。

对 $\Theta_u$ 的六个 Hermite-to-Bernstein 控制函数，正性可逐控制函数检查。对 $z_s$，四个端控制非负、其余控制严格正即使内部速度严格正。这里这些还只是明确可检验条件，不以采样充当连续证明。

实际 $1024$ 个角的端口审计自然退出 0，用时 $14.096315845$ 秒，报告 SHA256 为 `aa931ecae030a8e3ea595d8269c94e3983a18dab8f4f24968c2da9daf0b7ad2f`，得到：

| 端口预算 | 实际有限值 |
|---|---:|
| 左端 $\min\phi_u$ | $0.4540410002319598$ |
| 右端 $\min\phi_u$ | $0.9213969253250919$ |
| 同极角 $\min\Delta z$ | $0.14691330611130698$ |
| 最小内部高度控制 $B$ | $0.08674229808601315$ |
| 四个端高度控制的共同下界 | $0$ |
| $\Theta_u$ 六个控制的共同下界 | $0.4540410002319598$ |

右端 $z_s=0$ 的角区同时 $z_{ss}=0$，没有与非负速度相冲突的端加速度。此处为 literal 有限检查；连续全角界尚未支付。

## 4. 实际导数核对及完整新基线

最终源码的端口/导数核对自然退出 0，用时 $3.933529745$ 秒；报告 SHA256 为 `07cfd8c4e6179850aefb066d98841fe12be4b4b16906f06297a6c3f17fc67c10`。两端全部六 jets 最大差小于 $2.071\times10^{-15}$。中央差分步长从 $10^{-4}$ 到 $3\times10^{-5}$ 再到 $10^{-5}$ 时按二阶收敛；最后一阶导数差小于 $3.787\times10^{-10}$，二阶差小于 $5.652\times10^{-9}$。叉乘平方恒等式的实际差小于 $2.23\times10^{-16}$。

首次代码核对曾发现 $P_{uuu}$ 的 $e_1$ 系数漏了一个 $f$；正确值是 $-f^3mn$。修正后才获得上述收敛回执。未用首次有限差分平台当作通过。

随后在整半核 $[0,s_{\rm cuff}]$ 取 $97\times128=12416$ 个点，保留完整 13 行，总 $161408$ 行。径向用包含两端的显式非均匀梯形权 $ds/S$，连接节点为 sine-squared 分布；这不是 CI 的两组训练网格，成本不与 CI 成本直接排序。两份源参数与所有目标半径在整次评估中冻结。

实际自然退出 0，用时 $188.363246425$ 秒，最大 RSS $205704$ KiB。目标定义 oracle 也自然退出 0。完整输出仅留 scratch：

- 报告 SHA256：`2ac6194544cb00b1b24abbf31d3afab64765afe51e8e8c90397ec6c993503617`；
- stdout SHA256：`1934cce2e4f0e09fdbd7c484b95de2695d3467be21ea723aea59609be2bdb036`；
- 外部退出回执 SHA256：`1770aa737460e2f58fc093d655ac75c23f02bf89e5f2c097fd8bd52eee07de8f`。

| 整半核实际有限指标 | 值 |
|---|---:|
| 完整 13 行平方成本 | $113.77335089148343$ |
| metric / curvature / geometry 成本 | $98.47005290090145/15.303297990581983/0$ |
| 最大相对 metric 谱误差 | $0.991492290526681$ |
| 最大自身主曲率绝对值 | $747.809085610484$ |
| 最小归一化 Gram 行列式 $\eta$ | $0.008534102758085206$ |
| 最小面积比 $\sigma=\sqrt\eta$ | $0.09238020761010014$ |
| 最小实际面积元 $|X_s\times X_u|$ | $0.08834736087973309$ |
| 最小 held 见证距离 | $0.7138586958673055$ |
| 最大到原点距离 / 最大 $|y|$ | $1.4705592903497426/0.796391597489073$ |

全部七个 R219 几何残差在这次网格上为零，未转借为连续几何证书。

最坏 metric 在 $s=0.8163906842065027,u=\pi/2$，分解为

$$
E-1=-0.991492290526681,\qquad F/a_*=-1.6383\times10^{-13},\qquad
G/a_*^2-1=0.0031022785685113075.
$$

最大曲率在同 $s$、$u=3\pi/2$。它是侧轴径向速度换号时的高度速度谷，当前常数内部控制没有给转弯处足够速度。先前 $33\times128$ 的独立几何采样只见曲率 $330.2193$；更密此次网格已实际推翻那个最大值，不能把粗值当统一上界。

新场基线数为 1，优化尝试及接受均为 0。固定 R233 前缀还含已登记的小非零 metric 误差；最终全域机器容差仍须另修前缀。后继工作可以在不改 $g$、$\rho$、$\Theta$、总高度增量和全部端迹的条件下，重新分配正的内部高度控制，针对这个已定位速度谷；本条不预报其结果。

## 5. 源码、准确复生与保存边界

源码位于本题 `scripts/`，各 SHA256：

| 文件 | SHA256 |
|---|---|
| `6a65-geometry-nonfold-polar-port-budget.py` | `8f8bb96603e97806bdf2d16571ce80cd52aafa9ac3a3b8d2ed20ecd398de4e4c` |
| `6a65-geometry-nonfold-polar-connector.py` | `eef82a0e7522a70762a4e44a265b86bbf67f6e7d6f5d94d84842ba55d3390002` |
| `6a65-geometry-nonfold-target-zero-definition.cjs` | `eb0fd7cd96b21c5fbd260c6741c58bd355df2db6d80a7549bdf2b3ffa9a2a5fa` |
| `6a65-geometry-nonfold-fixed-metric-value.py` | `e5ea3ada40f81d1eda8f0b90b4191c382adf84089a16fc9bbc34c7245679cb29` |

先用公开 `6a65-geometry-coupled-gap-prefix.py --scripts-dir SCRIPTS --output-prefix SCRATCH_PREFIX` 重生两份 master 并核上述 SHA。目标定义入口为：

```bash
node --expose-gc --max-old-space-size=128 \
  6a65-geometry-nonfold-target-zero-definition.cjs \
  SCRIPTS PUBLIC_CANDIDATE PUBLIC_CAUCHY_RECIPE SCRATCH_TARGET.json
```

完整新场入口为：

```bash
python 6a65-geometry-nonfold-fixed-metric-value.py \
  --scripts SCRIPTS --polar-source 6a65-geometry-nonfold-polar-connector.py \
  --candidate PUBLIC_CANDIDATE --target-definition SCRATCH_TARGET.json \
  --ramp-master SCRATCH_PREFIX-ramp-master.npz \
  --coast-master SCRATCH_PREFIX-coast-master.npz \
  --angles 128 --connector-radials 65 --output SCRATCH_REPORT.json
```

两个公开输入是 `notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json` 与 `ci-requests/6a65-cauchy-clock-recipe-20261126.json`。完整报告、数组及可重算审计输出不进入仓库、Artifacts 或 Release；本次只保存源码与本条实际结论摘要。
