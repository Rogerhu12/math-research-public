# 下一幅度设计的完整核心预算、既有成果归属与实际候选分账

作者：/root、strong_recovery（GPT-6 Astra Pro，AI辅助），2026-11-14。

**状态：设计笔记；下列条件推论给出完整代数推导，实际 A 的数值沿用已保存计算。没有新的 BVP、ODE、Node、Jacobian 或运行器计算。** 原离线稿暂称 R225，核对旧文后不将其大部分内容重新登记为新结果。C²入口、球排除和优化四次谐波射线分别已有 R7/R1；R12已有更强的三谐波最优结论。本笔记保留可用设计推论、一个静态比较例和当前真实缺口，不改变现有半正幅原循环。

## 1. 任务的量与当前差距

采用母题的定义：
$$
\delta_{\rm hold}=\max_t d_H(F_t(M),F_0(M)),\qquad
\delta_E=\max_t\inf_{A\in E(3)}d_H(AF_t(M),F_0(M)).
$$
$E(3)$ 包含反射；$D$ 为完整闭面 $F_0(M)$ 的直径。材料点位移的上确界不是这里的距离。固定 $H$ 的闭性、内点、逐点固定和直径条件仍须分别验证。

真接受 A 的完整32模核心轴支撑差为
$$G=0.2506381129076958.$$
连续前缀的 $D$ 下界已为 $3.976755157289288$，所以完整闭面所需的 $0.2D$ 至少约 $0.7953510315$。当前没有达到该门槛的像集合见证。半正幅候选的 $G\approx0.254638112977$ 即使通过原数值终验，也不会独自解决这个振幅差距。

对偶余弦完整核心，
$$G=h(0)-h(\pi/2)=2\sum_{m\equiv2\pmod4}c_m.$$
因此所有中性控制、高模和真实谱尾都必须计入，不能用 $2q_1$ 替换完整轴差。以下 $G/D$ 是为寻找一个实际见证设定的预算。只有证明另一张**整面**没有更近的部位，这个轴差才可能成为所选核心点的距离下界；$\delta_E$ 还须另付刚体控制。

## 2. 已有核心公式和当前真 A

[R1](../results/R1-two-mode-core-phase-gap.md)、[R7](../results/R7-core-witness-initial-acceleration.md)已经证明：对中心对称严格凸支持函数 $h$，
$$
n=(\cos\theta,\sin\theta),\quad
t=(-\sin\theta,\cos\theta),\quad
C=hn+h't,\quad \rho=h+h''>0,
$$
有 $C'=\rho t$。若 $\langle h\rangle=1$，周长为 $2\pi$；核心自身直径 $D_C=2\max h$。任何包含核心的闭面有 $D\ge D_C$。

若核心实现为精确旋转度量 $ds^2+a(s)^2d\phi^2$ 的 $s=0$ 测地线，$a(0)=1,a'(0)=0$，并满足反射入口 $X_s=e_z$，则 R7 在仅 C² 正则性下给出
$$X_{ss}=k_0\rho n,\qquad k_0=a''(0).$$
核心的两主曲率为 $k_0\rho$、$-1/\rho$，混合项为零。因此
$\kappa_{\max}\ge1/\min\rho$。本笔记直接引用 R7 的弱导数论证，不能把形式上的三阶求导当成 C² 证明。

远端小 manifest 已确认实际 A 的前三核心系数：
$$(0.12599999803539827,-0.009256552462686113,-0.0006450302499718777).$$
完整32模轴差的准确二进制有理数为
$$\frac{151501443036800030164955}{604462909807314587353088}.$$
实际 $\rho_{\rm short}=1.5026607568385948$，$k_0\rho_{\rm short}G=0.232735389837827$；它们不是下面 $q=.4$ 的理想核心数据。来源是 [完整核心预算](2026-11-13-strong-q126-m32-nine-full-core-budget-r1.json)及其 manifest。

A 的完整均值物理审计记录 $\kappa\approx8.345514341083943$，位于
$s=2.6336433085309867,\psi=\pi/2$，原字段为 **loop outward turn**。早先离线消息写作 inward turn；这是标签错误，已在此更正，样本数值不变。完整 flex 均值半高为 $1.9614959811661763$，不等于背景分段高度之和。

旧本地同点背景记录的总半高为 $1.9662561532954768$，其中初始 Hermite 为 $.8568372540430386$（约43.58%）、两个 loop turn 为 $.5372886011928984$（约27.33%）、首 descending turn 为 $.2848560143660040$、descending coast 为 $.16982156075550744$、boost 为 $.09810213004075483$、同步段为 $.00271737852067105$。这张分账需要在环境恢复后绑定原 accepted-binary-background-C2-r1.json 的完整 SHA；本次仅沿用已读本地记录，不声称远端重新核算。它提示降高的主要费用在首段与 loops；同步段的主要用途仍是避免局部退化和曲率峰，不能把它当作主要高度来源。

## 3. 两条明确的必要设计窗

这里假设使用轴差 $G$ 作为未来整面见证，要求 $G/D\ge1/5$，并采用必要局部曲率预算 $\kappa_{\max}D\le100/3$。两者都只是给定核心路线的必要预算，不是闭面充分条件，也不是一般核心上界。

### 3.1 纯二模

取 $h=1+q\cos2\theta$，则
$$G=2q,\quad D_C=2(1+q),\quad \rho_{\min}=1-3q.$$
由 $D\ge D_C$ 及 $G\ge D/5$ 得 $q\ge1/4$。由
$$\frac{2(1+q)}{1-3q}\le\frac{100}{3}$$
得 $q\le47/153$。故必要窗为
$$\boxed{\frac14\le q\le\frac{47}{153}.}$$
$q=1/4$ 已无新增整面直径的余量，不能把它当充分目标。

### 3.2 R1 已有的优化四次射线

取
$$h=1+q\cos2\theta-a\cos4\theta,\qquad
a=\frac{q}{10\sqrt2},\qquad c=1-\frac1{10\sqrt2}.$$
由 $4a<q$，最大/最小支持位于两轴：
$$G=2q,\quad D_C=2(1+cq),\quad \rho_{\rm short}=1+3q+15a.$$
令 $u=\cos2\theta$，则
$$\rho=30au^2-3qu+1-15a,$$
顶点为 $u=1/\sqrt2$，故
$$\rho_{\min}=1-\frac{3q}{\sqrt2}.$$
同样消去 $D$ 得
$$
\boxed{\frac1{5-c}\le q\le
\frac{94}{6c+150\sqrt2}},
$$
即约 $.24565735054\le q\le.43177145159$。上界来自
$6(1+cq)\le100(1-3q/\sqrt2)$，没有数值外推。

$q=.4$ 的代入给
$$
G=.8,\quad D_C=2.743431457505076,\quad
\rho_{\min}=.15147186257614287,\quad
1/\rho_{\min}=6.601886205085208,\quad
\rho_{\rm short}=2.6242640687119287.
$$
这些是明确理想族的显示近似。当前实际 BVP 只固定前三个低模，其余真实核心模式及整个非线性轮廓仍会响应，不能把上述系数宣布为下一真解。

## 4. 必须同时使用 R12 的更强既有目标

[R12](../results/R12-three-harmonic-core-optimization.md)已经在
$h=1+a\cos2\phi+b\cos4\phi+c\cos6\phi$
的完整三维族中，给出双边曲率半径及入口见证约束下的准确全局最优值和唯一达到者。$c<0$ 时保留 $a+9c\ge0$，以保证准确核心相位距离 $d=2(a+c)$。不能把这里只分析的四次射线包装成此前没有的大幅路线。

[既有设计笔记](geometric-three-harmonic-core.md)的有理内点 P26：
$$(a,b,c)=(.4,-.0257,+.00035)$$
具有 $d=.8007$、$\rho_{\min}>.152036$、$\rho_{\max}=2.59775$、$D_C=2.7493$；在 $k_0=.45$ 时入口乘积为 $.93600829125<1$，未来距离预算 $5d=4.0035$。N15 保留负 $c_6$，Pgate 给 $d=.81464$ 但局部余量更窄。它们全部是理想核心；P26 的正 $c_6$ 不能覆盖实际 A 的负 $c_6$ 及其余29个模。

[R2](../results/R2-rational-curvature-power-cores.md)还已有有理有限谱大幅核心。下一设计应比较这些既有目标、较低 $k_0$ 和完整实际谱，而不是只追求 $q_1+.004$。

## 5. R7 见证条件如何约束降高

此节引用 R7/R1 的已有结论，不新增结果编号。令初始长轴点
$W=(h_{\rm major},0,0)$，另一相位的短轴入口为
$(h_{\rm minor},0,0)$，$G=h_{\rm major}-h_{\rm minor}>0$。在第2节的准确入口假设下，
$$
|X(s)-W|^2=G^2+(1-k_0\rho_{\rm short}G)s^2+o(s^2).
$$
系数负时该指定见证立即被邻近点逼近；严格正时结合角向系数
$\rho_{\rm short}^2+G\rho_{\rm short}>0$ 和零混合项给短入口二维严格局部极小。等号不能用二阶判断。

在 $0\le z<G$ 的同一对称支线上，连续留在见证球左侧要求
$$x(s)\le h_{\rm major}-\sqrt{G^2-z(s)^2}.$$
全表面最终要证明
$$(h_{\rm major}-X_x)^2+X_y^2+X_z^2\ge G^2$$
或有严格余量的较小半径版本，并支付连续误差。单线通过不是全表面通过；单线失败仅否定这一特定见证。

frontload 能减小高度，也可能让横向增长太快而进入该球，所以“更矮”不自动增大集合 Hausdorff 距离。已严格满足 $|Z|\ge G$ 的片自动在球外，可把工作集中于近核心区；这仍是已有 R1/R7 分区策略。首段末真实最小高度大于 $G$ 是方便的充分分区方案，不是新增 BVP 接受门。旧 A 的背景首段高度约 $.8568$ 与未来 $G\approx.8$ 已同量级，不能不看真实均值和这项余量就激进降高。

## 6. 圆盘加椭圆：仅作额外静态参照

取
$$
\epsilon=\frac3{10},\quad A=\frac87,\quad
f(\theta)=\sqrt{\cos^2\theta+\epsilon^2\sin^2\theta},\quad
\mu=\langle f\rangle,\quad b=1-A\mu,\quad h=b+Af.
$$
$f\ge|\cos\theta|$ 给 $\mu\ge2/\pi>7/11$；Cauchy–Schwarz 给
$\mu\le\sqrt{\langle f^2\rangle}=\sqrt{109/200}<3/4$，所以
$$\frac17<b<\frac3{11}.$$
这个支持函数是圆盘与椭圆的 Minkowski 和，解析、严格凸、均值1，轴差恰为
$A(1-\epsilon)=4/5$。直接求导得到 $f+f''=\epsilon^2/f^3$，因此
$$
\rho=b+\frac{A\epsilon^2}{f^3},\qquad
\frac{43}{175}<\rho<\frac{943}{231}.
$$
上下界只用 $\epsilon\le f\le1$ 与前述 $b$ 界。故
$$D_C<\frac{218}{77},\qquad \kappa_C<\frac{175}{43}.$$
在准确反射入口且 $0<k_0\le.3$ 的额外假设下，
$k_0\rho_{\max}<.3(943/231)<175/43$，于是**核心处**两主曲率绝对值亦小于 $175/43$。若最终整面 $D\le4$，核心强制的曲率费用至多 $700/43$；这里没有整面曲率界。

例如 $k_0=.1$ 时
$$k_0G\rho_{\rm short}<\frac{1886}{5775}<1.$$
这些代数不等式有完整证明，但只描述静态核心。它有无限 Fourier 谱，必须另付全谱尾、入口分辨率、材料角映射、全局非线性匹配与尾闭合。本次已读 R1/R2/R7/R12 未见同一具体例，并不构成全仓库新颖性证明；也不足以证明它比 R12 的有限谱路线更适合计算。

## 7. 实际参数接口与恢复的先后

原 provider/initial-laws 可调前三实际低模目标、delta/boost_length/boost_speed，以及已有九控中的 vu、descending_turn_curvature、start_acceleration、initial_speed_frontload、vd、descending_sync_curvature。loop_radius/loop_ratio/loop_speed/loop_curvature/coast_outward/terminal_peak_fraction 等还有真实接口，但旧九列响应没有这些列；用它们必须新点实际响应或续解，不能借旧导数。

原物理域保速度严格在 $(0,1)$、正半径/长度、loop_ratio>1、coast_outward及真实coast长度非负，全部 Bernstein 控制合法。增强类保 delta∈(.002,1) 和 vu<boost_speed<1。frontload 与 pulse 不同时非零，degree22 的原定义保持；改变 degree 是新族，不是同参数导数。已付正 frontload 的定义域构造不等于实际 core-held BVP 或几何接受。小范围中心差分域也不是整个非线性信赖域。

当前仍先续同一 half-positive 原循环：iteration2、next_back8，原 H0、J1/QR1、35权 merit、原8/24/32/21预算与全部最终 H/RMS/BC/audit 门不变。r7尚无科学 producer，旧容量 hold 已真实释放，必须 fresh 预付，不能使用旧未finished receipt。

真正接受后继续同固定g视图、完整均值/物理审计和原精化，再以实际全谱 $G$、尺寸、曲率、入口谱尾、同步长度及球排除共同引导大幅设计。旧 full-release 暖态的低 $\kappa S$ 后来原 r8 solver_success=false；half-positive 暖态亦未整体接受，均不能替换真 A。历史 vd 较大组合曾把同步段压短并使实际暖态曲率约233，线性预测及 vd<1 不能替代真实非线性计算。

## 8. 来源身份与尚未绑定的文件

以下小文本在提交 c2efbb20c47a84adbc76fdca62b250c178d0d7fe 实际读取；完整UTF-8 SHA256由strong代理记录：
- R1：acd27925c9265dd4927e02bdb06b75ff9b188f901d398c1379eac41b4aa60582。
- R2：ad5fb0b81c64ed73e589c85d8fed5846c2d82a6b697bd4859426033fadb0ea17。
- R7：2f1879daf29cc7eeff4c1457f47b6076547c9ff43aab41d339f411c5d9eaadd1。
- R12：eb50d2a32c396a5884ea12472f899437b354f5ca5dfe43e700ddf703e5c939e6。
- geometric-three-harmonic-core.md：62ccdb0036821b518da56cc5c429e7be574e42d43d4be0049c3f2edbf027881a。
- accepted-recovery-manifest-r1.json：3e13322c21e0fcd5cb3b09b7b483260e8433632ef8828d3092dd595697795ecb。
- nine-full-core-budget-manifest-r1.json：3c353346c34a88826bd6391a78e2ea6d94340c49dcee7d9253931d7192e67b9f。
- nine-full-core-budget-r1.json：22816b8cac25e3f2d14f1f967bd6d841d4df771fd3cf13bc8fdd9b9cce87ed57。
- nine-initial-law-tail-pair-manifest-r1.json：5184a078b54f7cc22a4593575ba2d86224bfbff732b97dd152f17f16afcc0644。
- fixed-view-fullmean-audit-r1.json：0b85d08fb636ef483c60a17daada57c7ffc09ae6f675c5753f635f240e7b89c1。
- fixed-view-fullmean-audit-archive-r1.json：9bab0b0436ffaf518a8e4c20304c774b4233131b316414d28eaae70c9bed4d71。

上述 manifest/audit 文件均为 notes/2026-11-13-strong-q126-m32- 前缀。root随后直接读了R12、accepted manifest、fullmean audit：Git blob分别25092b2b3b30719239589fde635a61dd151e5983、66414d8f44dba8c25139ce25852750782f315bbc、7699ba3ec5c505bdfa8f1a4ae3997b8ef425dff6。

本次两个精确路径返回404：2026-11-13-strong-frontload-positive-domain-manifest-r1.json、2026-11-13-strong-A32-half-positive-gap-complete-warm-r1-manifest.json。只能说此远端快照没有找到，不据此断言本地丢失。实际背景12段完整SHA、这两个本地包及历史失败screen须环境恢复后绑定；本次不伪造替代文件或新数值。
