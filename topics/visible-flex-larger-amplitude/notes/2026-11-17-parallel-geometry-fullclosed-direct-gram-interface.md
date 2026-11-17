# 当前 Hold 固定度量的全闭 direct-Gram 接口：157 旧右行、解析圆端口与共享二 jet

2026-11-17，geometry_amplification。**纯数学／实现规格，未启动新求解或几何扫描。** 当前短区间 LM 的原域门、变量、预算和接受定义均不改。本稿定义另一个真正包含整个尾段及圆盘的有限 C² 最小二乘问题，不声称它已有可行解。

## 1. 旧 157 行实际做了什么

当前 `5b965b9c…` 的 `Problem` 使用 M=160、N=2048、n=482、602 节点，区间 `[0,1.03]`。其边界仅为

\[
B_A Y_0+B_B Y_{J-1}=b.
\]

前 325 行在入口固定 R₀=1、原前三个 core 系数、全部 `T_j+2jR_j=0` 和全部 Z 系数为零。后 157 行仅为

\[
L Y(1.03)=L y_{\rm ref}(1.03).\tag{1}
\]

实际 prepare 源 `30a899fd…` 从真实变化型界面
`s*=1.0283496328972757` 的保存位置／速度／加速度作二次参考
`y_ref(s)=y*+(s−s*)u*+(s−s*)²a*/2`，外推长度
`0.0016503671027243705`。在 1.03 的这个参考上构造移动标架矩阵
`B=(T J+T_s)T^{-1}`，选实部位于截口
`(2.1436656214181653, 2.8714812492318424)` 右侧的完整 157 维左实 Schur 子空间，再冻结 `L=L_B T` 及非零目标。prepare 报告的 `max|L y_ref|=0.10083343752490748`。这些是已有真实准备读数，本稿未重算。

因此 (1) **没有规定末端 U 或 A，没有规定平面、圆、全部材料角端口或帽；1.03 也不是 Hold 的平 cuff。** 它是一个冻结有限参考边界，不是准确非线性全尾 DN。现有短求解即使通过该边界，也仍缺 1.03 到真 cuff 的实际场及完整接缝。

依赖身份如下；报告／warm 中还保存完整标量定义和原输入身份。

| 对象 | SHA256 |
|---|---|
| `scripts/parallel_20261117_implicit_frenet_newton.py` | `5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac` |
| 实际 scratch `parallel-hold-short-bvp-prepared-source.py` | `30a899fd199092197f5cd7dd7c2c1f0f09652e13e267016554a14907d6b55c92` |
| `scripts/parallel_20261117_hold_short_bvp_generate.py` | `b796d6ce10f547eee361714dba4d210925e16bfff92c5e1b33bcec2320f117b5` |
| 其冻结 base prepare | `fe6bbefb8cc0411ab6018376b6fde6c957acbe4f57bb24c4a10ce7acecdc9104` |
| `parallel-hold-m160-short-bvp-warm.json.gz` | `1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057` |
| `parallel-hold-m160-short-bvp-prepare.json` | `88766cbbd645253bbcf5df490ed307fc2060698b2f8e1fbebb1fd43ad4433ef1` |
| 真界面输入 | `a425e38ed4caeebf4d1f96629721c2ba1f54d72eef863ac278e7fb64f0327ba8` |
| Hold 源 `scripts/parallel_20261117_negative_hold_profile_ivp.py` | `ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1` |
| 移动 Schur helper | `426635e625e3f80b2b7eea238df1a7f9ac9285fafa5f87a79fd0e2c3d645cd6b` |

## 2. 消费已有结论与同一个固定 g

[R18](../results/R18-computable-exact-tail-trace-and-robin-envelope.md) 是其 R15/R17 特定 profile 的 F224 完整解析尾和有误差包络的 Robin 接口；它没有把上述 157 行变成当前 Hold 全尾。[R240](../results/R240-canonical-material-metric-and-refinement.md) 已证明共同材料度量与 core 变化的关系；[R257](../results/R257-finite-unit-speed-Fourier-and-material-circle-Jacobian.md) 及旧 `uniform-material-angle-representation-option` 已说明解析 lift 与有限截频的区别。本稿不重证它们，只给当前 direct-Gram 的末端实现。

固定原 Hold 的**精确积分标量** a(s)，不优化其控制、区间长度或尺度。旧段／`.99` 到 `.995` 的初值运输按 R636、R646；不能把 `hold_scalar_profile.alpha0/kappa0` 的浮点记录换成另一精确初值。令 K 为该准确运输曲率，αc 为准确 cut 角，f=binary(.002)，h=r=o=binary(.02)，kn=−5/2，kp=3/2。原 Hold 的正平台长度是

\[
p={\alpha_c+\pi/2-[f(K+k_n)/2+h k_n+r(k_n+k_p)/2+o k_p/2]\over k_p},
\quad S=s_c+f+h+r+p+o,\quad R=a(S).\tag{2}
\]

沿用同一 quintic curvature ramps 及 `a'=sin α, α'=−κ`，故端点恒等式在精确数学定义中为
`a(S)=R, a'(S)=−1, a''(S)=0`。本全闭模型还明确要求正平台p>0、R>0以及整个活动区a>0；旧浮点参考不支付这些完整严格界。旧普通浮点评价报告约 `S=2.371299871729827, R=.5647341753868044`，这些近似数不是本稿重新钉死的端口，也不是全尾的严格积分证书。未来实现须把 S、R 及中间 a 的同一 oracle 身份／误差一并保存；若把 rounded `profile.end` 当准确端点并硬置 a′=−1，会产生另一个需付差量的定义。

对 νj=2j、qj=1−νj²，定义

\[
\rho(\phi)=1+\sum q_j c_j\cos\nu_j\phi>0,
\qquad \Theta(\phi)=\phi+\sum {q_jc_j\over\nu_j}\sin\nu_j\phi.
\tag{3}
\]

core 常数项保持 1。目标在 φ 图为 `ds²+a²ρ²dφ²`，在固定材料 θ=Θ(φ) 图仍为同一个 `g=ds²+a²dθ²`。c 与 s 无关；所有 core 导数均进入 (3) 及下文 lift。Hcap 是新场的**一个真实未知标量**，不是参考子午线高度、旧 φ 均值或 material 均值的替代值。

## 3. 紧局部解析圆端口 lift

本规格固定 `w=1/20`（先验证 `0<w<S`），令

\[
\chi(s)=\begin{cases}
0,&s\le S-w,\\
10u^3-15u^4+6u^5,&u=(s-S+w)/w\in[0,1],\\
1,&s\ge S.
\end{cases}
\]

χ 在两端的一、二导数准确为零。记 `b(s)=R+S−s`、`f(s)=χ(s)b(s)`、`z(s)=χ(s)Hcap`，取完整解析项

\[
L(s,\phi;c,H_{\rm cap})=f(s)e_r(\Theta(\phi))+z(s)e_z.\tag{4}
\]

在活动区 `[0,S]`，它支撑于末端宽 w；在 cuff 处

\[
L=R e_r(\Theta)+H_{\rm cap}e_z,\quad L_s=-e_r(\Theta),\quad L_{ss}=0.
\tag{5}
\]

这项在当前旋转 φ 标架的水平复分量是 `f exp(i(Θ−φ))`。它保留原 cos/sin/cos 对称性，但一般有无限角谱。**不可先截成 M 项再声称 (5) 是准确圆端口。** e_r、e_θ 在以下公式均取角 Θ。

真实六 jet 可直接评价，无角差分：

\[
\begin{array}{lll}
L=f e_r+\chi H_{\rm cap}e_z,&
L_s=f'e_r+\chi'H_{\rm cap}e_z,&
L_{ss}=f''e_r+\chi''H_{\rm cap}e_z,\\
L_\phi=f\rho e_\theta,&
L_{s\phi}=f'\rho e_\theta,&
L_{\phi\phi}=f(\rho'e_\theta-\rho^2e_r),
\end{array}\tag{6}
\]

其中 `f'=χ'b−χ, f''=χ''b−2χ'`。特别地，导数必须包含 χ 的导数；不能把已知 lift 当作不随 s 变化的附图。

## 4. 优化变量本身定义一个 C² 场

固定任意完整径向分割 `0=s0<…<s(J−1)=S`，包含原标量分界及 `S−w`。它的精确定义／oracle 也冻结；S 非 binary 时可用最终分段的有理局部坐标定义网格，不能默默挪动真实端点。选 M=160 起始表示，n=3M+2。每个节点存**剩余场 q** 的全部 Fourier 系数三 jet `(Y_i,U_i,A_i)`；每胞唯一共同 quintic 定义 q。物理场为

\[
F(s,\phi)=\mathcal S_M q(s,\phi)+L(s,\phi;c,H_{\rm cap}),\tag{7}
\]

这里 S_M 包含物理旋转 φ 标架；不是把 lift 先投影再加入未知量。给两端 jet、胞长 d，quintic 的局部幂系数为

\[
C_0=Y_i,\ C_1=dU_i,\ C_2=d^2A_i/2;
\quad b_0=Y_{i+1}-C_0-C_1-C_2,
\ b_1=dU_{i+1}-C_1-2C_2,
\ b_2=d^2A_{i+1}-2C_2,
\]
\[
C_3=10b_0-4b_1+b_2/2,\quad
C_4=-15b_0+7b_1-b_2,\quad
C_5=6b_0-3b_1+b_2/2.\tag{8}
\]

优化和读出都消费这同一个多项式的实际导数。A 是未知量，不是旧 Pr 的 `−CU^{-1}(CY U+Ck k')`，也不是在 C¹ 求解完成后另造的一组导数。已有 R227/R230 的 Hermite 原理仅被消费，不把它们冒作新场的数值误差证明。

用准确参数化施加以下条件，避免把有限 BC 容差当成准确接缝：

- 入口原 325 条位置条件保持，即 `R0=1, Rj=cj, Tj=−νjcj, Zj=0`，c1,c2,c3 保持原值；
- `U0=e_z` 准确固定，`(A0)_Z=0` 准确固定；A0 的所有水平槽保留自由；
- 末端剩余三 jet `Y(J−1)=U(J−1)=A(J−1)=0` 准确固定。

于是 core 的三个镜像条件和 cuff 的全部六 jet 恒等成立。原 157 条人工 Schur 行被真正圆端口替代，不能继续称为原短区间方阵；它们也不作为隐含的中间接受条件。

原始变量数是 `3Jn+1`（含 Hcap）。入口位置 `2M+K+2` 行、入口 U 的 n 行、入口 Az 的 M+1 行及末端 3n 行独立，合计 `15M+K+11`；M160、K3 时为 2414，剩余 `3Jn−2413` 个实自由度。该计数只确认此明确仿射空间，**不证明 Gram Jacobian 满秩或解存在**。

## 5. 完整角值 Gram 目标及域门

记 `V=F_s,d=F_φ`，对**整个** `(s,φ)∈[0,S]×S¹` 定义

\[
e_{ss}=|V|^2-1,\qquad
e_{s\phi}={V\cdot d\over a\rho},\qquad
e_{\phi\phi}={|d|^2\over a^2\rho^2}-1.\tag{9}
\]

它们就是目标正交标架中的全部相对 Gram 项。一个直接可实现的有限目标在每个共享节点和每胞**实际 quintic 中点**、固定 `φ_k=2πk/N`（可先 N=2048）保留三组全部角值，最小化预先冻结正权下的
`Σω(e_ss²+2e_sφ²+e_φφ²)`。节点／中点共 `3N(2J−1)` 行；核心和 cuff 的一些行因准确约束恒等为零也仍可记录。不能用 cubic 中点替代 (8)，也不能只保低频行。

这是新角值最小二乘；**N=2048 或任何有限 N 都不使它自动等价于完整解析角方程。** lift 非有限谱，因此旧“962 项完整二次谱／N>12M”证明不覆盖这里。独立连续验证必须使用完整 sin/cos(Θ) 及导数的区间包围、或明确的解析尾界；旧纯有限带宽 FFT 证书不可直接贴用。mesh／M／N 精化及 C² 六 jet 比较仍按 R240，在同一 a、S、w 下进行。

新模型的浸入域检查是 `a>0,ρ>0,|d×V|>0`（或实际 Gram 正定）；最终 `||e||op<1` 也能支付正定性。它不用 Frenet 显式平方根图作定义。准确 cuff 上，若 `Q=|d|²,W=|d×F_φφ|²,k=a'/a`，则

\[
Q=R^2\rho^2,\quad W=R^4\rho^6,\quad
\mathcal H_{\rm Fr}=W-k^2Q^3=0,
\quad |d\times V|=R\rho>0.\tag{10}
\]

原 binormal 正支量 `(d×F_φφ)·V` 此处也为零。因此把旧 strict-H 或 strict-binormal 门加到整个闭合模型会准确排除合法平盘。**当前短 LM 的 strict-H>0 门保留；(9)–(10) 是另一个新模型的域。** 不另把微分角长 r1 加作新接受门；连续等价／离散不等价已由 R647 的 direct-Gram 附节说明。

## 6. 完整 core→ρ→Θ→lift 正向微分

固定 g，故 δa=δS=δR=δw=0。记

\[
\beta_j(\phi)={q_j\over\nu_j}\sin\nu_j\phi,
\quad \gamma_j(\phi)=q_j\cos\nu_j\phi,
\quad \eta=\delta\Theta=\sum\beta_j\delta c_j,
\quad r=\delta\rho=\sum\gamma_j\delta c_j.
\tag{11}
\]

则 δρ′ 是 r 的真实角导。完整 lift 变分为

\[
\begin{aligned}
\delta L&=f e_\theta\eta+\chi\delta H_{\rm cap}e_z,\\
\delta L_s&=f'e_\theta\eta+\chi'\delta H_{\rm cap}e_z,\\
\delta L_{ss}&=f''e_\theta\eta+\chi''\delta H_{\rm cap}e_z,\\
\delta L_\phi&=f(r e_\theta-\rho\eta e_r),\\
\delta L_{s\phi}&=f'(r e_\theta-\rho\eta e_r),\\
\delta L_{\phi\phi}&=f[(r'-\rho^2\eta)e_\theta-(2\rho r+\rho'\eta)e_r].
\end{aligned}\tag{12}
\]

其中 δV、δd 还须加上共享 quintic／有限 Fourier 的普通线性导数。全部三组 Gram 微分是

\[
\begin{aligned}
\delta e_{ss}&=2V\cdot\delta V,\\
\delta e_{s\phi}&={d\cdot\delta V+V\cdot\delta d\over a\rho}
-{V\cdot d\over a\rho^2}\,r,\\
\delta e_{\phi\phi}&={2d\cdot\delta d\over a^2\rho^2}
-{2|d|^2\over a^2\rho^3}\,r.
\end{aligned}\tag{13}
\]

这同时保留原全局 ρ 链与新增的解析 lift 链，不能只复用旧 finite-Gram 的 core 列 G。

## 7. 原样角值空间的离散伴随

给每个实际评价点任意三残差余向量 `wss,wsφ,wφφ`；角／径向求积权及 Frobenius 权如有，先吸收入这三者。定义

\[
g_V=2w_{ss}V+{w_{s\phi}\over a\rho}d,\quad
g_d={w_{s\phi}\over a\rho}V+{2w_{\phi\phi}\over a^2\rho^2}d,
\quad g_\rho=-{w_{s\phi}(V\cdot d)\over a\rho^2}
-{2w_{\phi\phi}|d|^2\over a^2\rho^3}.\tag{14}
\]

先将 gV、gd 通过 (8) 的**实际**径向／角合成矩阵转置，回传所有 Y/U/A 槽。这是有限节点评价矩阵的精确转置；不要求未知的无限谱函数通过 FFT 分部积分，也没有旧系数投影的额外 cos 常数权。旋转 φ 基的角导必须包含连接项 `(R_φ−T,T_φ+R,Z_φ)`。

再将每点以下量累加到全部入口 core 槽：

\[
g_{c_j}^{\rm global}
=\bigl[f'g_V\cdot e_\theta-f\rho g_d\cdot e_r\bigr]\beta_j
 +\bigl[f g_d\cdot e_\theta+g_\rho\bigr]\gamma_j,
\qquad
g_H+=\chi' g_{V,z}.\tag{15}
\]

在独立 core 参数化中，还要把普通端点回传合并成
`g(Y0_Rj)−νj g(Y0_Tj)`，然后加 (15)，最后屏蔽原固定前三个 c。U0、A0Z、末三 jet 固定槽同样屏蔽。**不能把 (15) 当作普通 q 回传的替代或重复加两次。** 若将位置／曲率等另列目标，须再用 (12) 的对应 jet 链；本稿只规定 (9) 的 LS，不暗加这些目标。

由逐点恒等式 `w·δe=gV·δV+gd·δd+gρ r` 及 (12)，(15) 直接是所定义有限角值 J 的 Euclidean 转置，无需完整二次谱假设。它允许一次后续小 Jv／伴随核验；尚未核验或运行新实现。由于新 A 自由度和 (15) 的非恒定 core 项，旧 T／精确列尺度不能不改直接移植。

## 8. 平盘、镜像、相位及完成范围

在 `S≤s<S+R`，令 `a(s)=R−(s−S)`（同 Hold 已声明的平盘延伸），取
`F=(R−(s−S))e_r(Θ)+Hcap e_z`。其与 (5) 的完整六 jet 准确一致。到轴时改用盘的 Cartesian 图 `(x,y)↦(x,y,Hcap)`，不能把 φ↔Θ 的非线性圆坐标在极点冒作光滑 Cartesian 换图。该图册与固定材料 g 的兼容性消费 R240§6、R248§3；本稿不重复一般拼接定理。

上片关于 z=0 镜像，以 core 的准确 `Y0Z=0,U0XY=0,A0Z=0` 得 C² 中央接缝，两端各加盘，参数域为 S²。这只给闭 C² **映射**；实际全域 Gram／浸入、全局单射、reach、完整 D、held 见证和非全等仍须支付。之后若按 R248 构造相位族，必须在共同材料 θ 中做 `Rot_α F(s,θ−α)`；圆盘逐点不变。非轴标记及其诱导帽度量需作为一次明确固定设计加入，不能冒称仍等距旧未标记平盘。

R632 是从**向外**平 cuff 接半圆回头盖的组件；本新 cuff 的 Fs=−er 已向内，直接接盘即可。不能把 R632 的独立同盖 reach 当作本新活动体的全闭 reach；R650 的全闭加权支持路线若用，也须给同一完整候选的全部支持和曲率界。

若准备轴对称初猜 `F_ax=a(s)e_r(Θ)+z_ax(s)e_z`，至少先核实际 `|a'|≤1`，并选一致的 `z_ax'=sqrt(1−a'^2)` 分支及其 C¹ 正则性。Hold 精确角段可用 `z_ax'=cos α,z_ax''=κ sin α`，在 flat cuff 因 `α=−π/2,κ=0` 得两者为零，避免除以 vanishing sqrt；旧 scalar 段仍须独立满足同样条件。此轴对称参考在 core 是圆，**不满足指定非圆 core**，所以尚不能当作本新仿射空间的可行初猜。非轴 warm 的准备、完整节点／中点雅可比诊断和实际求解是后续明确任务，本稿均未执行。

当前新增内容止于：识别原 157 行的真实对象；给出同固定 Hold g 的紧局部解析圆端口、完整共享二 jet 未知空间、真实角值目标及全 core Jacobian／adjoint。没有删除当前 run 的门，没有把终点参考、有限残差或方程计数宣布为完成。

## 版本与核对范围

原规格fc0e3e49254fb9bcb39d9d941a7aabc4a839b106ce3f2ae42f9d660327c250a5经root完整阅读，model独立只读核端jet/式12–15与约束计数。发表版按作者指出的范围修正，将p/R/a的严格正性明确列为未付标量输入；没有新增数值试验。后续实现和真实非轴warm另行保存，不以本文规格声称已有闭合解。
