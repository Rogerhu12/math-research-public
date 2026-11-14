# 开平曲率段 provider-v2 的完整独立数学审查

日期：2026-11-10。审者 independent_audit；会话 Astra-visible-flex-78718bd0。审者未参与该公式构造、主 M14 初猜或参数优化。

## 1. 结论和准确适用范围

**全文证明通过。** 在稿中给定的闭入口曲线/周期正交标架、C0≠0、b0∈C1，以及平方根和特征 Jacobian 两个严格全宽度条件下，显式位置公式确实给整个圆周和整个宽度上的真实 C² 等距浸入。它不限于 Fourier 截断或有限法向 jet。主曲率、条件唯一性、实域充分界、C² 参数依赖与接合的陈述均在各自所写范围成立。

第 6 节 v2 使用冻结二进参数作为精确实常数。本人除读 ramp/installer 原码外，另核原解析目标 Target 实现：其头部和构造函数明确把主参数解释为 exact binary rationals，并用 Fraction 重新计算 Tu/Td。这直接确认 v2 对应当前解析目标的同一度量，没有将四个冻结值改为方便的十进有理数，也没有把数值求值的舍入差清零。

若实际入口满足 C0≠0、|b0|≤1、|b0'|≤1，则上升/下降两个真实中段的全宽度确有 J>4/5。这是有条件的统一充分界。**本审没有验证当前候选的实际完整入口条件，没有声称全宽条带全局嵌入或 reach，也没有穿过非平 ramp、得到闭面/精确全族或支付目标幅度。** 原 v1 的参数解释错误由另版 v2 纠正，v1 不作为此结论的正式文本。

冻结稿：[geometry-flat-strip-provider-v2](2026-11-10-78718-geometry-flat-strip-provider-v2.md)，12,558 B，SHA256 cc26cf6685ec4a26f4c8b612c64d1af598cc4f8e223d6cd2c1b0a87e99af23d4。

以下记 a=a0+cs、B=1+b0²、t0=a0/√B、k=a0 b0/√B。下标 u 是物理圆参数，ξ 是入口标号；C、M、L 始终是坐标第二基本形式，不能把 C 换成正交分量 C/a²。

## 2. 入口框架与归一化直纹方向

给定 γ0'=a0T0、N0=d0×T0 和稿中式(2)。由 b0=a0M0/C0，定义

\[
e_0=(d_0-b_0T_0)/\sqrt B,
\qquad w_0=(b_0d_0+T_0)/\sqrt B.
\]

这是同一个定向正交平面内的旋转，所以 e0×w0=N0，并且

\[
d_0=(e_0+b_0w_0)/\sqrt B,
\quad T_0=(-b_0e_0+w_0)/\sqrt B,
\quad \gamma_0'=-ke_0+t_0w_0.
\]

对 e0 求导，其法向项为 (M0−b0C0/a0)/√B=0。切平面内旋转角的导数为 b0'/B，因此准确得到

\[
e_0'=q w_0,\qquad
w_0'=-q e_0+(C_0/t_0)N_0,\qquad
N_0'=-(C_0/t_0)w_0,
\quad q=c-b_0'/B.
\]

这一步没有漏一个 √B。由 k=a0 b0/√B 和 t0²+k²=a0²，另有

\[
k'=a_0b_0'/B^{3/2}=t_0b_0'/B,
\qquad t_0'=-kk'/t_0.
\]

全部只用 b0 的一次导数、标架的一次导数。C0/M0 由标架关系可仅连续；构造没有在这里对 C0 求导。

## 3. Gauss–Codazzi 和特征方程逐式核验

对 g=ds²+a²du²，非零相关 Christoffel 符号为 Γu_su=c/a、Γs_uu=−ac。两条 Codazzi 和 Gauss 因而是

\[
M_s=L_u-(c/a)M,
\quad C_s=M_u+(c/a)C+acL,
\quad LC-M^2=0.
\]

在 C≠0 下，M=bC/a、L=b²C/a²。直接计算 b=aM/C 的 s 导数，先消去前两项中的 cM/C，得

\[
b_s={aL_u\over C}-{bM_u\over C}-{cb\over a}-{abcL\over C}.
\]

前两个项化为 bb_u/a，最后一项为 −cb³/a，故

\[
b_s-(b/a)b_u=-(c/a)b(1+b^2).
\]

第二条同样化为

\[
C_s-(b/a)C_u=\{b_u+c(1+b^2)\}C/a.
\]

沿特征 du/ds=−b/a，记 D=∂s−(b/a)∂u。于是

\[
D\{ab/\sqrt{1+b^2}\}
={cb\over\sqrt{1+b^2}}+
{a\,Db\over(1+b^2)^{3/2}}=0.
\]

守恒量为 k(ξ)，由初值即 b=k/√(a²−k²)。平方根的严格正门保证没有分支歧义。对 c≠0，

\[
{d\over ds}\arctan b=-{ck\over at},
\quad t=\sqrt{a^2-k^2},
\]

所以特征 lift 是 ξ+(arctan b−arctan b0)/c。对 ξ 求导时，∂ξ arctan b=k'/t，入口对应 k'/t0，因此 J=1+(k'/c)(1/t−1/t0)。当 c=0，a=a0、t=t0、b=b0，准确特征为 ξ−s b0/a0；J=1−s b0'/a0。稿中没有用除以 c 的式子直接处理零斜率。

由特征导数 J_s=−(b_u/a)J，以及 D log t=c(1+b²)/a，得到 D log(CJ)=D log t。因此 C=C0 t/(t0J)，再由 M=bC/a、L=b²C/a²即稿中式(11)。

这证明光滑特征描述中的唯一传播。若只假设一般 C² 浸入，其第二基本形式未必 C¹，不能直接以上述微分系统主张全部解的唯一性。原稿已明确把唯一性限于 C¹ 第二基本形式、C不为零且特征未交叠的解类；实际 C² 存在性由下一节显式位置给出，不依赖这个加强假设。

## 4. 显式位置在整个二维域给精确共同度量

定义 ℓ=(t−t0)/c，c=0 时 ℓ=s√B。分别用上述 k'/t0' 和 J，两个情况均有

\[
\ell_s=a/t,
\quad\Psi_s=-k/(at),
\quad\ell_\xi=k(1-J),
\quad t_0+\ell q=tJ.
\]

例如 c≠0 的第三式是

\[
\ell_\xi=(-kk'/t+kk'/t_0)/c=k(1-J),
\]

第四式为 t−ℓk'/t0=tJ。c=0 时直接代入 ℓ=s√B、J=1−s b0'/a0，结果相同。

由 X=γ0+ℓe0，全部一阶导数恰为

\[
X_s=(a/t)e_0,
\quad X_\xi=-kJ e_0+tJw_0.
\]

因此 Xs×Xξ=aJ N0。两个严格门加 a>0 给真正秩二，不是只有形式级数。又 t²+k²=a²，故

\[
|dX|^2={a^2\over t^2}ds^2-{2akJ\over t}ds\,d\xi
+a^2J^2d\xi^2.
\]

由 du=−k/(at)ds+Jdξ，右边正是 ds²+a²du²，因为 ds² 系数为 1+k²/t²=a²/t²。此等式在整个二维矩形和全角圆周逐点成立。

Ψ 的 lift 为 ξ 加真正周期函数，故次数为一；J在紧域上严格为正，保证每个 s 的 lift 严格递增且以 2π 平移。它因而是圆上的全局保向微分同胚，不仅是局部可逆。其逆 ξ=Ξ(s,u) 是共同二维域上的 C¹ 函数，有

\[
\Xi_u=1/J,\qquad\Xi_s=k/(atJ).
\]

于是 F=X(s,Ξ) 真正全角单值，N=N0(Ξ)。初边界 Ψ(0,ξ)=ξ、ℓ=0、J=1，恢复 F(0,u)=γ0(u)。没有额外假定一个未核的 SE(3) monodromy；闭合已由入口和显式周期公式支付。

## 5. 最低 C² 正则性与全部第二基本形式

若直接对 Xξ 再求一次 ξ 导，会出现 b0''，在假设中未给。原稿没有这样做，而先在物理坐标消去 J，得到

\[
F_s=(t/a)e_0+(k/a)w_0=:d,
\quad F_u/a=-(k/a)e_0+(t/a)w_0=:T.
\]

本人独立用 Xs+XξΞs 和 XξΞu 复算这两个式子。其右侧只含 b0、C¹ frame、a/t 和 C¹逆 Ξ；每一项都是 C¹。因此 F 的两一阶导数确实 C¹，即 F∈C²。没有暗加 b0∈C²，也没有把输入 C0/M0 连续升级为可微。

反变换是 e0=(t/a)d−(k/a)T、w0=(k/a)d+(t/a)T。对 N=N0(Ξ) 求导：

\[
N_s=-{C_0k\over a t t_0J}w_0,
\quad N_u=-{C_0\over t_0J}w_0.
\]

与 Ns=−Ld−(M/a)T、Nu=−Md−(C/a)T 比较得到

\[
C={C_0t\over t_0J},\quad
M={C_0k\over a t_0J},\quad
L={C_0k^2\over a^2t t_0J}.
\]

C0≠0 及 t,t0,J>0 保证 C 全域不过零，且 LC=M²。形状算子的一个特征值为零；另一个是迹

\[
L+C/a^2={C_0\over a^2t_0J}(k^2/t+t)
={C_0\over t_0tJ}.
\]

入口 t=t0、k/a0=b0/√B 恢复原 d0/T0，故 Fs(0,u)=d0。边界 Gauss 在 C0≠0 时给唯一相容 L0=M0²/C0；没有漏掉一个可独立指定的二阶入口自由量。

## 6. 全实域充分门及主曲率界

记 |b0|≤B0、|b0'|≤B1，a_min=min(a0,a0+cS)、a_max=max(...)。设

\[
h_*^2=a_{\min}^2-\max(a_0^2-a_{\min}^2,0)B_0^2.
\]

令 H=√B t，则 H²=a²+(a²−a0²)b0²。若 c≥0，第二项非负，H²≥a0²=h_*²；若 c<0，用 a≥a_min 及 b0²≤B0²，即得到稿中同一个下界。故 h_*²>0 时 t²≥h_*²/(1+B0²)。

令 ρ=ℓ/√B。由 ℓs=a/t 得 ρs=a/H，ρ(0)=0，故 0≤ρ≤S a_max/h_*。将 J 的式子改写：c≠0 时 J−1=−k'ℓ/(tt0)=−ρ b0'/H，c=0 时同样是 1−s b0'/a0。因此

\[
J\ge1-{S a_{\max}B_1\over h_*^2}=1-\eta_*.
\]

这是整域的实数不等式，不是若干角点或采样值。η*<1 同时给第一道根号门和第二道 Jacobian 门。再由 t0tJ=a0HJ/B，

\[
|\kappa|\le{\|C_0\|_\infty(1+B_0^2)
\over a_0h_*(1-\eta_*)}.
\]

这个界是局部第二基本形式界，不能给不同特征之间的距离，因此不能单独转成 reach。原稿正确保留该缺口。

## 7. 与固定解析 g 的实际同一性

完整读了 950f-prefix-flat-accel-screen.py 的 ramp/FlatFlow、db6f-prefix-flat-profile.py 的 installer；回看 notes/fixed_metric_mode3_flow.py 的四个主参数及 Tu/Td 定义。平中段的 normalized z∈[ε,1−ε] 满足 w=1、w'=0、I=z−ε/2，故是精确线性 a 段。

为了区分“程序一次浮点计算的 Tu”与“已认证解析目标的 Tu”，又直接读取 db6f-audit-metric-supplier.py：文件开头明言主参数 exact binary rationals；Target.__init__ 对 cfg.delta/vu/vd/ramp 先 q 转为 Fraction，再用精确式 Tu=δ/[vu(1−ε)]、Td=δ/[vd(1−ε)]；a_prefix_poly 的中段 k=3 确实以 I=z−ε/2 定义 polynomial。只有 bridge 的特定数值常数另有既定身份，本模块未涉及。

原冻结 profile 实物为 202 B，SHA256 bb55971c3463c27a10fcfddafd06a65e86f42d6c6d684adf2768e8dcd7d21b8e；其实际四值为 ramp=.4、vu=.17、vd=.18、delta=.07254443456654512，direction=outward、cycles=1、ramp_law=flat。故 v2 引用的四个二进常数确实是本题该解析目标的常数，不是另一张有理数近似设计。

以这些常数在实数域计算 qε=ε/[2(1−ε)]，上升中段从 a−=1+δqε 到 a+=1+δ(1−qε)，斜率 vu，宽度 (1−2ε)δ/[vu(1−ε)]；下降的入口/出口交换、斜率 −vd，宽度同式将 vu 换为 vd。物理圆坐标下度量就是本稿的 ds²+a²du²；主程序若使用已冻角 chart，其固定坐标拉回仍是同一 g，实际入口也须在相应坐标下提供。本审没有用一个未认证的数值入口完成这个转换。

单次数值 profile/求解/导出计算仍有舍入误差；精确 analytic target 已用包含性包围支付其原范围。本稿仅识别解析目标的实际线性段，不将任何浮点求值当精确 PDE 解。

## 8. 第 6 节全部有理界复算及实际检查

四个二进值的精确 Fraction 满足稿中 (25)。函数 ε/[2(1−ε)] 严格递增，所以

\[
399/1202<q_\varepsilon<401/1198,
\qquad33/100<q_\varepsilon<34/100.
\]

由 δ>0、qε<1/2 得 1<a−<a+；由 δ<3/40、1−qε<67/100 得 a+<1+(67/100)(3/40)<53/50。

函数 (1−2ε)/(1−ε) 的导数为 −1/(1−ε)²<0。上升/下降两段的速度均大于169/1000，因此两宽度都小于 (202/601)(3/40)/(169/1000)<3/20。没有把下降速度的较大下界用错到上升段。

在 B0=B1=1 的共同充分门下，上升 h_*²=a−²>1。下降 h_*²=2a−²−a+² 严格大于

\[
2(1+33\delta/100)^2-(1+67\delta/100)^2
=1-\delta/50-2311\delta^2/10000.
\]

用 δ<3/40，得下界 1−3/2000−20799/16000000>99/100。因此两段 η*<(3/20)(53/50)/(99/100)=53/330<1/5，J>4/5。更紧常数并非本模块必要；没有增加或调优数值参数。

本人全文阅读冻结脚本 78718-geometry-flat-strip-binary-gates.py；它使用 Fraction.from_float 恰好保二进位值，所有十个比较均是精确整数/有理运算，先钉 v2 证明 SHA。本人实际运行 **b7808a，自然 exit 0**：10/10 通过、pde_runs=0。独立输出 [binary gates 实跑](2026-11-10-78718-audit-flat-strip-binary-gates-01.json)，771 B，SHA256 **67776fc8235e18e011aad462624f80fcb0a94336636a0cd65a6926bc2af9cf33**；脚本 SHA256 904a48bab818343dd288ace9607542659a2788d999f24923bbd38397031ed50e。

这十个检查只验证有限参数和纸面充分界，未读取任何真实 PDE 入口 C0/M0/b0，更不证明其导数界。数学存在证明是上文完整推导，不用这十个布尔值替代。

## 9. 实解析性、连续族、C² 接合和嵌入范围

若入口实解析，严格正的 t 和 J 允许选择同一正实根及解析逆；公式的所有运算在紧实域附近解析。周期紧致性可选某个共同复角邻域并保持局部逆，周期 degree-one 身份给一致的全角分支。原稿只声称存在这样某个邻域，明确没有提供有效带宽、log 权或 Green 算子界；因此没有从实域余量虚构复域数值常数。

给定一族 γ0 的 C²、frame 的 C¹、b0 的 C¹ 连续输入并有统一严格门，Ψ 与 J、逆 Ξ 的 C¹ 范数连续依赖输入。物理一阶导数的两个显式式子和它们的一次导数因而一致连续依赖，给 F 的 C² 连续族。这里 a0/c/S 固定，所以参数族用同一个 g；没有要求输入关于族参数可微。

邻接片的完整两 jet 匹配时，Gauss 给相同 L0=M0²/C0。二阶位置导数由共同连接和 II 决定，具体为 Fss=L N、Fsu=(c/a)Fu+M N、Fuu=−ac Fs+C N。相同位置、frame 和 L/M/C 因而真的给全部二阶导数相同，形成 C² 接合。这里只支付已有邻接片在接口的接合，不预先提供非平 ramp 的存在。

若 γ0 嵌入，Fs=d0 与入口切线单位正交，紧致局部图与远离对角的核心分离给某个统一正薄宽度上的嵌入。它不能保证该薄宽度达到第 6 节整个物理 S；Jacobian 正不防不同直纹的空间自交，局部曲率界也不防自接近。原稿把全宽嵌入、跨片距离、reach 与最终闭合明确留待后续，范围正确。

## 10. 全文审查使用的实物身份

| 文件 | B | SHA256 |
| --- | ---: | --- |
| notes/2026-11-10-78718-geometry-flat-strip-provider-v2.md | 12558 | cc26cf6685ec4a26f4c8b612c64d1af598cc4f8e223d6cd2c1b0a87e99af23d4 |
| scripts/78718-geometry-flat-strip-binary-gates.py | 2308 | 904a48bab818343dd288ace9607542659a2788d999f24923bbd38397031ed50e |
| scripts/950f-prefix-flat-accel-screen.py | 6004 | dca3d7fdd5495f4eeeea923522b3001499f48f4b770d262b43e6f88a80b8f6ef |
| scripts/db6f-prefix-flat-profile.py | 2008 | 5066cd6d8f94d3b22c0450cc2016df6f90d04efb85d7a13bc833c11868eaaa4b |
| notes/fixed_metric_mode3_flow.py | 5131 | 0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5 |
| scripts/db6f-audit-metric-supplier.py | 17450 | de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0 |
| notes/2026-11-10-78718-audit-flat-strip-binary-gates-01.json | 771 | 67776fc8235e18e011aad462624f80fcb0a94336636a0cd65a6926bc2af9cf33 |

本次只运行冻结的十项纯有理检查，没有调用原 flow 的构造器或任何 BVP/DN/优化。不存在把已审模块范围升级成整个课题完成的结论。
