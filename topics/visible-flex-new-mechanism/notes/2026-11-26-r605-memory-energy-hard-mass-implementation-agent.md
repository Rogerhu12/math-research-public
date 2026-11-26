# R605 全程二维记忆输入与原 mass 精确边界坐标

日期：2026-11-26。**实现说明；尚无本包的科学输出。**
源码只在本公开仓库 GitHub Actions 执行。本地仅纸面推导、读源、AST 和文件身份检查。
入口是 $R,\theta,I$ 的全程新输入，随后求同一 R598 母的完整 R590 原方程。

## 1. 本次为什么改变输入和边界组织

直接前驱是 R603 首质量 run **45839778794** / job **139978074450**，
源提交 **8bed9c0efe6bdca745b65dba7eb8f8d702c3ed5e**。
原 stdout SHA-256 为
6400ae955e59cc55fc8c663d46208906cafec0dc7a90a85de2da0ec2a01491ae；
完整科学收据见 2026-11-26-r603-vtwo-first-mass-public-receipt-agent.md。
本包不重新下载该日志，不重做其中的九参数 fit 或五十步 mass。

该终态已说明两个具体问题。
一是中心 $h_{ss}=H,\ k_s=2$ 准备准确，但全程正势仍达到 $5.2985943391\times10^{14}$；
只有局部中心条件没有支付整个路径的规范兼容。
二是软边界 merit 的五十次接受把原 BC 最大值从约 $.04573$ 增至 $.68010$，
同时原 ruling 仍为 $6.2885\times10^{14}$。
末 Hermite 真几何的必要 focal/diameter 预算也只有约 $.024786<.03$。

本次因此同时改变：

- guide 的**整条轨道**：从 $R,\theta$ 与真实积分 I 构造，并拟合两侧全程最高能量；
- guide 的紧凑范围：$H\in(.9,1.2),\ L\in(2.1,5.8)$，高度全程小于 3；
- 原 mass 的**边界坐标**：准确消元原 29 条 BC，使它们不能在降低其它 merit 时漂移。

原十九条微分方程、两条 ruling、完整正平方、两侧全部 rho、固定 $\chi$、
原十个真实中心参数及完整末几何读出保持。

## 2. 同一个全程记忆积分

十一参数按
$$
(H,a_0,a_1,a_2,a_3,b_1,\ldots,b_5,L)
$$
排列。置 $\vartheta=\pi x/2,\ s=Lx$，
$$
q=\sin\vartheta\exp\left(\sum_{j=0}^3a_j\cos j\pi x\right),\qquad
z=q^4\cos^2\vartheta,\qquad
R=H\left(1+\frac z{1+z}\right),
$$
$$
\theta=\frac35\tanh\left(c_1\sin\vartheta+
 \sum_{j=1}^5 b_j\sin((2j+1)\vartheta)\right),\qquad
c_1=-\frac{2L}{\pi(3/5)}-\sum_{j=1}^5(2j+1)b_j.
$$
这里 $c_1$ 是准确从属系数，没有每点控制。
同一个真记忆定义为
$$
I(x)=\int_0^x\frac{\theta_x(t)}{R(t)^2}\,dt.
$$
代码在每个 x 用固定 64 点正 Gauss 对这个从 0 到 x 的积分求值。
因此同一 x 的结果不依赖本次同时求值的其它节点，
frame 的单点调用和矩的整网调用使用同一个积分定义。
Gauss 值仍是近似；本包不宣连续积分误差界或准确运动学认证。

从 R605 的准确逆恢复
$$
h=R\sec\theta,\quad \eta=-hI,\quad k=-\tan\theta-h^2I.
$$
速度与两加速度使用 R605 的原链式式(5)–(8)，全部带物理时间因子 L。
它们是上述准确积分定义的真实导数的数值求值，
不是在不同空间点独立指定 $\eta$，也不是截掉最高能量。

准确连续定义满足
$$
h(0)=H,\quad h_s(0)=0,\quad h_{ss}(0)=H,\quad
k(0)=\eta(0)=0,\quad k_s(0)=2,\quad k_{ss}(0)=0,
$$
以及末 $h_s=k_s=0$。在全部 $0<x<1$，
$$
m=h^2-H^2(1+d^2)=\sec^2\theta(R^2-H^2)>0 .
$$
两端准确 $R=H$，中心以四阶离开，末点以二阶返回；
内部 $H<R<2H,\ |\theta|<3/5$，所以整个解析高度
$$
.9<h<120/41<3.
$$
$k,\eta$ 和速度仍需另外支付，不由此自动保证。

这个末形状有原方程依据：如果八个末 A 与 gamma/up 都为零，
则末 $C_A=e_s=V_2=B_\pm=0$。
同一个 $\lambda>0$ 的两条首层方程必须因而有末 $m=0$。
所以不能把 R605 的通用 $R>H$ 输入（包括末点）直接用作完整首层返回初猜。
本包的 $\cos^2\vartheta$ 因子准确修复这条末端失配；
保留真正二阶末接近，并未把所有末能量导数人为设零。
这不是额外 imposed 的原 mass 边界：完整 mass 的末 h/k/eta 仍原样自由。

初始输入完全显式：
$H=1.1,\ L=4,\ (a_0,a_1,a_2,a_3)=(.4,0,0,0)$，
$b_1=-L/(\pi(3/5))$，其它四个 b 为零。
此时角函数含一个真正的负角出发、随后转向正角的段，
而 R 在变化，允许 I 与当前角度异号；
不是重复 R605 已说明不能消 $p_1$ 的单值 $R(\theta)$ 叶。

## 3. 八矩与两侧共同的最高能量常数

每次 guide 求值由真实
$$
A(x)=A_c+L\int_0^x M(h,k,\eta,\gamma,\upsilon)\,dt
$$
取得完整八个历史；$A_c$ 是同一 $v=2$ 的 prepared 中心。
旧九族的单调 c 已取消，**包括 $p_2$ 在内的全部八矩**进入这次目标。
不把旧母、旧轨道或旧末矩转入。

在 R598 的六个正参考中心与正权上，直接计算 R605 的
$$
B_\pm(x)=\sum_i w_i Q(\pm c_i)V_2(\pm c_i)^2.
$$
负侧由原 JPAR 与几何反射读取，不移动实际正窗口内的母。
整个轨道只拟合一个共同常数：
$$
\lambda=
 \frac{\sum_xm(x)(B_+(x)+B_-(x))}
      {2\sum_xm(x)^2}>0.
$$
于是能量目标是两条完整函数 $B_\pm-\lambda m$；
不会按每个 x 重配 $\lambda$。

这只是寻找更合适的**原方程初猜**。
$\lambda$ 没有加入 mass 的新自由参数，不代替原固定 $\chi$，
也没有把有限微宽的 C² 余项、rho 或正势替换为首层方程。

guide 在 257 节点积分全部 M，能量目标取每第四节点（含两端，共65节点）。
八矩的固定倍率为 $(2,1,2,8,8,4,4,8)/L$。
两侧能量目标共同乘 $2/\sqrt{65}$，再除以初始新 guide 的固定
$\max(1,\max B_\pm)$；该单位一经取得不随迭代改变。
原 $B_\pm$、共同 $\lambda$、$B_\pm/m$ 范围、
全部原八末矩与原能量差同时输出。

guide 采用 TRF / 三点差分，最多 300 nfev；
实际 residual、全部 Gauss integrand 点数、shape 点数与耗时单独输出。
每次参数迭代都计算真实的同一积分/history；没有本地预拟合。

## 4. 宏观空间费用也进入这个新输入

guide 对 $|k|<1.94,\ |\eta|<.94,\ |\gamma|,|\upsilon|<5.7$
的采样越界加固定罚项，保持随后原 atan 物理盒所需余量。
这些采样不冒充连续盒证书。

另从原 collar 形算子读取两个侧、两个边的最大主曲率采样 $\kappa$。
对这两条反射片的路径有几何包络
$$
D_{\rm enclosure}=2L\int_0^1h(x)^2\,dx+2u_{\max}.
$$
guide 目标加入 $\max(0,\kappa D_{\rm enclosure}/30-1)$。
这是使输入更紧凑的启发式目标；$\kappa$ 当前只有采样，
这个包络也只覆盖两条反射片，不授最终四片闭合后的全局 reach。

完成 guide 后，原 frame/位置 ODE 仍独立读取实际采样直径、
collar 曲率/focal cap、两 pose 数和原母的一阶场量。
完成 mass 后，再对**实际最终 Hermite 插值**读取同样预算；
最终 $h_s,k_s$ 由插值导数乘原 chart/L 计算，
与尚未满足的速度状态之差单独输出。
不能用 guide 的预算替代最后质量状态，也不能用 merit 下降略过 $.03D$ 门。

## 5. 全部29条原边界的精确嵌入

设 N 是 Lobatto stage 数。原未知为 $21N+10$：
每点19态加两个原加速度，共10个真中心参数。

原19条左边界令几何等于参数给定的中心、A等于原
prepared 加四个自由奇修正、六个 rho 为零。
它们在新坐标中直接用原 coordinates.center(p) 填入；
左 h/up 的 encoded 值分别就是原参数 $p_0,p_1$。
原10条右边界直接令八个 A 和 gamma/up 的 encoded 值为零。
两端加速度都保持自由。

因此新自由未知数是
$$
21N+10-29=21N-19.
$$
余下原方程数正好是
$$
19(N-1)+2N=21N-19.
$$
原 BC 不再作为可漂移的 merit 项，但每个状态仍用原
rhs.boundary 计算并输出全部29个数值。
浮点装配中 A 中心转换可有舍入量，不把它隐去。

若 E 表示这个非线性嵌入，实际 Jacobian 是
$$
J_{\rm reduced}
 =J_{\rm original,\;without\ BC}\,DE .
$$
所有内部和自由端 stage 的列为准确单位列；
中心 h/up 的参数列是准确单位列；
中心八个 A 的所有参数导数由原10变量 Jet 求取。
**不能冻结 H、v 对 prepared 中心 A 的导数**，源码没有这样做。
原十参数、固定 gauge 单位、状态 guard 单位与原质量行单位都保持。

这个正则边界坐标消元不授全端图 rank，也不保证 Newton 根存在。

## 6. 初猜投影、真实历史和原缺陷分开

首先仍用原 make_seed 积分新 guide 的全部真实 A、
两侧完整 C² rho，求实际正平方和一次全局规范 LS，
并输出这个完整输入。

进入新边界坐标前，用
$$
A_{\rm guess}(x)=A_{\rm true}(x)
 -(10x^3-15x^4+6x^5)A_{\rm true}(1)
$$
作平滑的八个末矩初猜投影。
这个操作保中心与其前二阶 jet，末 A 准确为零，
但**不保持 $A_s=M$**。
对应原 rho seed 仍来自未投影的真 guide，
所以它也不会被宣称已经支付投影后的完整历史。

代码分别输出：

- 原准确积分定义的数值八末矩；
- A 投影的大小与投影后原29BC；
- 投影后的完整 mass 初态；
- 每一步原十九条流、两条 ruling、全部 BC；
- 原 sigma 历史缺陷、真实规范恢复和当前完整正势。

最终只有原方程残差及加密能解决这个投影的费用。
它不登记为消矩证明，不偷换 history。

## 7. 实际求解、预算和范围

原全质量 RHS 仍为 R598 的31变量 AD，完整正平方系数为1。
所有19个微分 merit 行单位仍为1；
两 ruling merit 行仍只用该新真 guide 的一次固定能量单位。
原单位残差门仍为 flow/ruling $10^{-7}$，BC $10^{-10}$。
完整负侧 rho 的总反号、固定中心参数链和原 sigma 回付未改。

使用同一阻尼/信赖域 LSMR，但 Jacobian 现在是上述真实 reduced Jacobian。
最多50个新原 mass 迭代；每轮最多12个实际试探，
每次线性求解最多1600步。
每个接受态在 stdout 保完整21行/10参数/固定单位/原缺陷，
保最后完整有限态；没有 state、table、raw、artifact 或 Release 入库。

原192阶母系数与正 Gram 必须为本次新求解再生，
其成本真实计入；不重做旧 identity、方向导数或求积门。
guide、真正history、Jacobian/LSMR、物理检查、frame 的所有实际费用都会留在本次原输出。

只有原全部门同时满足才作一次129-stage加密；
即使某个离散门满足，也不直接授连续精确根、全部period、pose、
同13、有限等距族、全域reach或README完成。

## 8. 文件

- scripts/r605_memory_energy_hard_boundary_mass_agent.py
- computations/request-r605-memory-energy-hard-mass-20261126.json
- .github/workflows/visible-r605-memory-energy-hard-mass-20261126.yml

源码依赖已发布 R603 的逐列原 chart 适配器和最终真插值几何读出，
以及 R598/R590 原方程；不会调用 R603 的九参数 guide 或 main。
本说明依赖正式 results/R605-real-memory-coordinates-and-leading-energy-local-flow.md，
不依赖后续可选的中心更高阶短补充。

