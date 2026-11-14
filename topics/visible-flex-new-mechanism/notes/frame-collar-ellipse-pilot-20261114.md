# R28 单位正交框架：准确椭圆端口与有限维连接试算器

日期：2026-11-14。性质：**可运行的表示、解析参数 Jacobian、人工开发检查与公开 Actions 试算接口**。本记录没有在本地评价或求解 \(A=1,B=0.28\) 的研究候选，更没有证明非旋转闭合连接器存在。

独占文件为 `../scripts/ellipse_frame_port.py`、`../scripts/frame_collar_bvp.py`。径向度量复用独立 `cosine_connector_radial_seed.py`；该历史文件名不限制对称阶数。R28 的数学重构与连续误差命题仍是表示的依据，有限网格不是连续证书。

## 1. 准确 m=2 椭圆柱入口

取准确有理数 \(A\ge B>0,w\ge0\)，空间核心为

\[
 \gamma(\phi)=(A\cos\phi,B\sin\phi,0),\qquad
 X(s,\theta)=\gamma(\phi(\theta))+s e_z.
\]

材料角由准确弧长定义：

\[
 \ell(\phi)=\int_0^\phi\sqrt{A^2\sin^2t+B^2\cos^2t}\,dt,
 \quad a_0=\ell(2\pi)/(2\pi),\quad \ell(\phi)=a_0\theta.
\]

程序用同一不完全椭圆积分和单调标量反解评价该模型，不重新拟合曲线。准确积分可写为

\[
 \ell(\phi)=A\,E(\phi-\pi/2,1-B^2/A^2)
             +A\,E(\pi/2,1-B^2/A^2).
\]

`EllipticCylinderPort` 保存准确 \(A,B,w\)、完整物理身份和 SHA256。相同模型的 \(a_0\) 是上述积分的定义，不被数值评价所得的 binary64 常数替代。

侧号 \(\sigma=\pm1\) 的向外变量为 \(s=\sigma(w+t)\)。单位目标框架满足

\[
 V=\sigma e_z,\qquad v=0,\qquad \beta=-\sigma\pi/2,
\]

且所有径向标量 jet 均为零。准确水平角为

\[
 \psi(\phi)=\phi+\arctan
 \frac{(A-B)\sin\phi\cos\phi}{A\sin^2\phi+B\cos^2\phi},
 \quad u=\psi-\theta.
\]

分母严格正，因此这是连续实分支。令 \(v_\phi=|\gamma_\phi|\)，则

\[
 \psi_\theta=\frac{a_0AB}{v_\phi^3},\qquad
 \psi_{\theta\theta}
 =-\frac{3ABa_0^2(A^2-B^2)\sin\phi\cos\phi}{v_\phi^6}.
\]

这给完整位置二 jet、标量二 jet，并额外给径向二 jet 的角导数（本例恒零），所以椭圆 pilot 的 \(V_\theta\) 和全部参数 Jacobian 均能直接解析评价，不必谱差分强核心的角函数。

公开 API：

```python
port = EllipticCylinderPort(major, minor, half_width, side=+1)
port.scalar_jets(t, theta)
port.position_jets(t, theta)
# A_exact, B_exact, width_exact, a0, identity, identity_sha256
# fold=2, angular_derivative_mode='analytic'
```

准确椭圆柱可继续沿 \(z\) 挤出，因此初始开放核心缓冲区也有真正准确的模型，不只是把端口 Taylor 多项式当作已证延拓。

## 2. 独立长度、负 K 区与开放平领

由独立 `NegativeKRadialSeed.from_core(port,L,rc,config)` 给出严格正的参考半径。\(a_0\) 绑定当前核心的准确周长定义；\(L,r_c\) 与分段过渡参数为明确冻结参数。首轮采用 `negative-K-open-port-radial-metric-v2`：前两个变化段为 S5，最后一个变化段为 S11，身份显式保存 `transition_orders` 及准确多项式。旧全 S5 模型仍可显式重放，但与此不是同一度量。

默认配置是开核心占比 \(0.04\)、开平尾占比 \(0.06\)，活动段内比例 \((0.25,0.35,0.40)\)，中段斜率回落 \(\mu-\nu=0.30\)。其中 \(d=-a'\) 按

\[
 0\longrightarrow\mu\longrightarrow\nu\longrightarrow1
\]

变化，总半径降量准确决定 \(\mu,\nu\)。S5 和 S11 的区间均值都准确为 \(1/2\)，因此末段改阶不改变 \(\mu,\nu\)、第一段入口展开或中段负 K 积分。中间段有 \(a''>0\)，故 \(K=-a''/a<0\)。这些是参考度量的性质，不是已经找到实现它的曲面。

令

\[
 t_c=0.04L,\qquad t_f=0.94L.
\]

目标场在整个 \([0,t_c]\) 都使用准确柱核心，在整个 \([t_f,L]\) 都固定

\[
 u=v=0,\quad \beta=-\sigma\pi,\quad
 a(t)=r_c+L-t.
\]

于是尾部是准确开平圆领。正侧使用 \(-\pi\)，负侧使用 \(+\pi\)；这是一次全角统一分支选择，避免把正侧 \(-\pi/2\) 误桥到 \(+\pi\) 而人工多绕一圈。

例如后续准备的 \(L=0.9,r_c=0.22\) 模型，平领开始半径是 \(0.274\)。这里仅给定义代入值；完整场的投影和高度必须由实际审计支付。

## 3. 有限维未知量与强端口保留

活动段 \([t_c,t_f]\) 的基场对每个材料角使用九次 Hermite 插值，匹配准确入口的完整径向二 jet 与末端常值的完整二 jet，并将这部分基场两端的三、四阶径向 jet 取零。它随后叠加下述准确的局部必要 leading 项。入口角函数逐点调用准确 port，**没有投到少数自由角模后冒称同一核心**。

### 3.1 避免人工低阶入口项

令 \(x=t-t_c\)，\(\ell_1\) 为第一个 S5 变化段的物理长度。在该段准确地有

\[
 a'=-\mu\{10(x/\ell_1)^3-15(x/\ell_1)^4+6(x/\ell_1)^5\}
   =c_3x^3+O(x^4),\qquad c_3=-10\mu/\ell_1^3.
\]

记准确核心角函数的 \(k=\psi_\theta>0\)，侧号仍为 \(\sigma\)。将 R28 的三个标量积分性方程在 \(\beta_0=-\sigma\pi/2\)、\(v=0\) 附近逐阶展开，得到任何足够可微准确延拓必须满足

\[
 \beta-\beta_0=\beta_3(\theta)x^3+O(x^4),\qquad
 \beta_3=\frac{\sigma c_3}{k},
\]

\[
 u-u_0=u_4(\theta)x^4+O(x^5),\qquad
 u_4=-\frac{c_3}{4a_0}\partial_\theta(1/k)
     =\frac{c_3 k_\theta}{4a_0 k^2},\qquad v=O(x^7).
\]

例如令 \(\alpha=\arctan v\)、\(b=\beta-\beta_0\)，最低阶给
\(\sigma b k-\sigma\alpha_\theta=a'\)、
\(\alpha_t=b\psi_t\)、
\(\psi_t=-\sigma b_\theta/a_0+\cdots\)，即得上述两侧符号。

普通五次平滑衰减会让强核心 \(u_0(\theta)\) 人工产生一个全角 \(x^3\) 项；少数自由角模不能完整抵消它。新基场改用 S9 以去掉这一项，并叠加准确全角 \(\beta_3x^3\)、\(u_4x^4\)。它们分别乘以

\[
 \chi(x)=1-S_9(x/\delta),\quad 0\le x\le\delta,
 \qquad \delta=\ell_1/4,
\]

在 \(x\ge\delta\) 取零。\(\chi\) 的端点四阶平坦使修正不改变核心或尾部的位置二 jet；局部 Taylor 项也不会被盲目外推到整个长连接区。\(\beta_3,u_4\) 的角导数由椭圆的准确 \(k,k_\theta,k_{\theta\theta}\) 解析计算，保留了真实全角结构。

这是必要 leading 的初场修正，**不是完整 Cauchy 级数或已存在局部解的结论**。种子 \(a'\) 仍有 \(x^4\) 等更高项；自由场基仍只硬锁完整二 jet，后续候选必须靠实际积分性残差支付更高相容条件。

### 3.2 平领端的阶数相容

令 \(\delta=t_f-t\)、\(b=\beta+\sigma\pi\)、\(\alpha=\arctan v\)。当前有限维标量场在尾部满足 \(u,\alpha,b=O(\delta^3)\)。R28 的切向分量为

\[
 R_T=\cos\beta\cos\alpha\,(1+u_\theta)
       +\sin\beta\,\alpha_\theta-a'.
\]

由于 \(\cos\beta=-1+O(\delta^6)\)、\(\sin\beta\,\alpha_\theta=O(\delta^6)\)，且周期角平均 \(\langle u_\theta\rangle=0\)，准确地有阶数必要条件

\[
 \langle R_T\rangle=-(1+a')+O(\delta^6).
\]

旧末段 S5 在 \(\nu\ne1\) 时给 \(1+a'=10(1-\nu)(\delta/\ell_3)^3+O(\delta^4)\)，所以与这个标量 ansatz 的准确 \(R=0\) 不相容。它并非对所有位置 C2 解的排除：位置 C2 本来可能允许 \(b\sim\delta^{3/2}\)，只是当前 C2 标量空间未包含这种端部行为。

首轮在运行研究求解之前把末段改为

\[
 S_{11}(y)=462y^6-1980y^7+3465y^8-3080y^9
            +1386y^{10}-252y^{11}.
\]

该函数在两端的第一至第五阶导数为零，\(S_{11}(1-y)=1-S_{11}(y)\)，故 \(1+a'=O(\delta^6)\)。这只消除了上面的最低阶平均失配；真实 \(R_V,R_W\) 及更高阶条件仍须支付。自由 \(\beta\) 包含零角模，可表示常规尾分支所需的三阶常系数；S9 基场仍有更高阶全角余项，不能据此声称整个尾部 PDE 已满足。

自由修正使用 degree-five clamped B 样条。完整控制系数的首、末各三个省去，所以自由项在两个活动端点的值、一阶和二阶导数均为零；在活动段以外恒零。**这些场自由项仍从三阶开始，会改变基场的更高 Cauchy leading；全部候选硬锁的是完整二 jet，并没有全部硬锁 \(\beta_3,u_4\)。** 角向为

\[
 u,v:\ \sin(mk\theta),\quad 1\le k\le M;
 \qquad
 \beta:\ \cos(mk\theta),\quad 0\le k\le M.
\]

类接口从 `port.fold` 读取任意 \(m\ge2\)，水平角均值的对称论证同样成立。当前 CLI 优先提供 \(m=2\) 椭圆 pilot；其他 port 可通过通用类接口接入，若没有全部解析角数据则采用明确标记的周期谱导数分支。尚未对那个通用分支运行真实余弦研究候选。

径向自由数 \(J\)、角模数 \(M\) 时，场未知数为

\[
 J\{M+M+(M+1)\}=J(3M+1).
\]

默认 \(J=4,M=5\) 共 64 个场变量。每次只解一个侧号、一个配置、一个 case。对本次准确平面椭圆柱，若正侧已构造，可用 \((x,y,z)\mapsto(x,y,-z)\) 复制负侧，对应 \(u\mapsto u,v\mapsto-v,\beta\mapsto-\beta\)；准确中央柱及 C2 端口相容。因此首个 pilot 不重复求解负侧。这个反射不自动证明两个半带互不相交或满足整面 reach。一般非平面余弦核心仍不享有这条径向反射。

## 4. 始终单位正交的目标与真实重构

每个评价点直接设置

\[
 T=\frac{(-\sin(\theta+u),\cos(\theta+u),v)}{\sqrt{1+v^2}},\quad
 N_0=(\cos(\theta+u),\sin(\theta+u),0),
\]

\[
 V=\cos\beta N_0+\sin\beta(T\times N_0).
\]

因此 \(|T|=|V|=1,T\cdot V=0\) 是表示恒等式。主残差为三分量积分性

\[
 R=V_\theta-a'T-aT_t.
\]

椭圆 pilot 对 \(V_\theta,T_t\) 直接解析微分。全部自由系数的 Jacobian 由场偏导、B 样条和正弦余弦基链式得到。可选通用 port 的角谱导数也同样作用于参数变分，没有把它从 Jacobian 中漏掉。

位置按 R28 的真实公式评价：

\[
 X=z_c(t)e_z+a(t)\Pi T,
 \qquad z_c(0)=\sigma w,\qquad
 z_c'=\langle V_z\rangle.
\]

\(\Pi\) 是零平均周期原函数。数值主评价用 Fourier 反微分，\(z_c\) 用各径向小区间的固定 Gauss 积分。场的真实定义仍为上式积分；数值有限项只是一种评价方法。

实际一、二阶位置导数按

\[
 X_t=\langle V_z\rangle e_z+a'\Pi T+a\Pi T_t,
\]

\[
 X_{tt}=\langle(V_t)_z\rangle e_z
          +a''\Pi T+2a'\Pi T_t+a\Pi T_{tt},
\]

\[
 X_\theta=aT,\quad X_{t\theta}=a'T+aT_t,\quad
 X_{\theta\theta}=aT_\theta
\]

计算。目标框架单位正交不等于重构的位置已经等距；程序另算真正的 \(E,F,G\)、最小面积和诱导主曲率。也审计离散误差恒等式 \(X_t-V+\Pi R\)，从而暴露 \(\Pi\) 评价与角导数之间的误差。

## 5. 固定度量与设计严格分开

`--mode fixed` 固定独立参考 \(a(t)\)，只求场。`--mode design` 可另加少量活动段 B 样条，令

\[
 a(t)=a_{\rm seed}(t)\exp\left(\sum_j c_j\widetilde B_j(t)\right),
 \qquad\widetilde B_j=16y^2(1-y)^2B_j,
 \quad y=\frac{t-t_c}{t_f-t_c}.
\]

原 \(B_j\) 在端点为三阶消失，因此加权后为五阶消失。它自动保持 \(a>0\)、两个开放端口及完整二 jet，并保留入口种子的 \(c_3\)，不会让 metric 自由变量重新引入 \(a'\) 的人工 \(x^2\) 项。其 \(a,a',a''\) 和参数导数均使用解析乘积链式。设计后不能把改变的 \(a\) 叫作原固定 \(g\) 的精化；也不继承原 seed 中段的准确负 K 积分，只审计新 \(-a''/a\)。

`metric_model` 保存种子准确身份、B 样条定义、每个实际 binary64 \(c_j\) 的准确有理数及数学定义 hash。`--frozen-metric-from` 检查源文件、种子、准确系数和数学定义 hash，再重建同一个 \(a\)，关闭这些变量。可增大场基或积分精度，但不能重新解释旧 metric basis。\(a_0\) 仍绑定准确周长积分，诊断中的最后一位浮点变化不会重新定义数学度量。

当前没有自动热启动或隐含多阶段参数扫描。一个公开 lane 运行一个主 solve；冻结度量后的进一步精化是另一个明确请求的固定参数计算。

## 6. 形状目标与必要的独立审计

除 \(R\) 外，目标函数还可惩罚

\[
 (X_x/A)^2+(X_y/B)^2>1,\qquad |X_z|>H.
\]

对应位置参数 Jacobian 穿过了角原函数与径向中心积分，包括 \(\beta\) 对 \(z_c\) 的贡献；并非仅惩罚目标切向的某个代理量。默认 `shape-weight=2`、\(H=0.45\)。这些仍是取样软目标，不能替代连续包络证书。

每次实际输出包括：

- 全区采样的 \(|R|\)、真实相对度量矩阵算子范数、\(E,F/a,G/a^2\) 各项误差；
- 最小面积、真实诱导主曲率和 Gauss 曲率；
- 椭圆投影半径、三坐标各自最小/最大值、\(\min(\sigma X_z)-w\)、最大高度及两端完整位置二 jet 的误差；
- 相同物理系数下审计角数加倍，比较位置和各几何量；
- Fourier 原函数与独立复合 Gauss 公式在有限径向/角点的对照：

\[
 \Pi T(\theta)=\int_0^\theta T(\eta)d\eta
 -\frac1{2\pi}\int_0^{2\pi}(2\pi-\eta)T(\eta)d\eta.
\]

有限对照与固定参数加密都没有标成连续误差上界。所有输出保持 `continuous_metric_certificate`、`embedding_proved`、`whole_surface_reach_proved`、`closed_surface_constructed`、`task_complete` 为假。

## 7. 已实际执行的人工开发检查

两文件分别记录于 `ellipse-frame-port-check-20261114.json` 与 `frame-collar-development-check-20261114.json`。仅使用 \(A=0.9,B=0.72,w=0.02\) 的人工温和入口；没有对研究的强椭圆输入运行本地 solve，也没有运行任何非线性优化。

| 检查 | 实际结果 |
| --- | --- |
| 椭圆 port 标量/位置一、二 jet 差分 | 最大相对误差 \(2.22\times10^{-10}\) 以下 |
| m=2 周期与奇性 | \(1.12\times10^{-15}\) 以下 |
| 完整场、metric 和位置软目标的方向 Jacobian | 两侧分别 \(6.24\times10^{-9}\)、\(6.12\times10^{-9}\) 以下 |
| 目标框架单位/正交误差 | \(5.56\times10^{-16}\) 以下 |
| 重构入口位置全二 jet | \(2.71\times10^{-14}\) 以下 |
| 开平尾位置全二 jet | \(7.55\times10^{-16}\) 以下 |
| 独立 Gauss 原函数与 Fourier 原函数 | 有限检查点差 \(1.20\times10^{-14}\) 以下 |
| design metric 冻结回放 | 数学 hash 相同，\(a,a',a''\) 评价逐位一致 |
| 加入必要 leading 后的入口残差 | 入口距离减半时，两侧残差均约缩小 \(15.959\) 倍，符合尚未支付的四阶余项 |
| 第一 S5 段准确 \(a'\) 多项式 | 人工检查差 \(4.16\times10^{-20}\) 以下 |

Jacobian 检查人为把形状目标设置得较紧，以实际激活椭圆和高度残差，而不是仅核零惩罚分支。表中记录最终 S9/leading/加权 metric 与 S11 末段种子版本的结果，均为 `passed: true`；这些检查不对研究候选的存在、嵌入或幅度作任何结论。

独立只读复核：`repo_sources` 已逐项核对椭圆 port 的角分支、标量及位置 jet；主 solver 的全部 T/V 一二偏导、解析 R 参数链式、\(\Pi T\)/\(z_c\) 位置重构及 Jacobian、真实入口二 jet 与开平领；并独立推得两侧 \(\beta_3,u_4\) 符号。`geometry` 还明确拒绝首径向点不是零或非严格递增的网格，避免后续子 chart 不积分全程却误锚定中心高度。

## 8. 建议的首个公开单侧 pilot

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ellipse_frame_port.py \
  --check-only --out "$RUN_DIR/ellipse-frame-port-check.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_bvp.py \
  --check-only --out "$RUN_DIR/frame-collar-development-check.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_bvp.py \
  --major 1 --minor .28 --half-width .02 --side 1 \
  --length .9 --cut-radius .22 --negative-curvature-drop .3 \
  --radial-free 4 --angular-modes 5 --mode fixed \
  --radial-nodes 29 --angular-nodes 96 --quadrature-order 4 \
  --height-limit .45 --shape-weight 2 --max-nfev 200 \
  --audit-radial-nodes 121 --audit-angular-nodes 384 \
  --checkpoint-every 10 --checkpoint-seconds 60 \
  --out "$RUN_DIR/frame-ellipse-positive-fixed.json"
```

默认周期为 \(2\pi\)，对称阶从 port 读取。每十个评价或至多六十秒写一次当前 best 的小 checkpoint；每份实际报告都带代码 SHA256、运行和物理身份。\(\min(\sigma X_z)-w\) 仅是采样诊断，没有追加新罚项；如果出现负值，不能凭镜射组装就跳过跨半带相交及 reach 检查。

首轮先固定 \(g\)。只有实际残差显示需要设计径向度量，才另开明确的 `--mode design --metric-free 3` lane；不机械重复同一初值，也不在同一 lane 自动再跑第二 case。首轮的作用是检验强边值在新表示下是否出现积分性、度量和形状方面的实际改善。固定度量、连续误差、整面单射与 reach、封帽和真实像集位移的后续条件都仍需支付。
