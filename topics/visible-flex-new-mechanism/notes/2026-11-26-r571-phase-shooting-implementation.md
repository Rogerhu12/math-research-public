# 2026-11-26：R571 真实相位 shooting 与核心归一 C2 计算入口

状态：源码与请求完成，尚未科学执行；只做静态解析和 SHA 绑定。使用 [R571](../results/R571-milder-phase-tail-flat-kernel-and-core-shooting-zero.md) 的新固定输入，未修改正在计算的 R566/hard 候选。

## 1. 本次单 job 实际做什么

入口是 scripts/r571_phase_core_shooting_20261126.py，调用独立的 scripts/r571_milder_seed_outer_jets_20261126.py。两源与 workflow SHA 在 computations/request-r571-phase-core-shooting-20261126.json 中绑定。仍由已发布的 stdlib runner 先实际 pull 公私仓库、检查两份 README 和 QUEUE、清掉凭据后执行。

固定尾为 $w_\varphi=0.8\exp[-(2-\sin(\delta^{-1}+\varphi))/\delta]$，
$\delta=(r-0.22)/0.2$。先在 $\varphi=0$ 做 M=25、同 M 容差紧8倍、M+1紧容差三份传递；归一点是 $\alpha_{17}$，有限条件准确为 $\rho_{M+1}=0$。这与旧 R569 的 M168/alpha160 是不同输入，不是重跑其加密。

随后用 $\varphi\in[0,2\pi]$ 实际求核心条件 $C_{\rm core}=0$，计算相位导数的两个步长并在同一根重做容差/末端比较。求根后把**同一个真场**除以有符号 $A_{\rm core}$，报告 $A_{\rm core}=1$ 下的尾和连接体二阶代价。模式4、6、8随后只作有限数值核探针，不授全频率逆。

三份数据、迭代中间表均只在内存中使用；stdout 只给小标量、峰位置、成本与可重算表的哈希。不保存 raw/表到仓库或 blob。

## 2. 明确且 C2 的真实圆柱连接头

本次不用尚未调好的任意径向 spline。固定
$$
R=0.38,\quad r_0=0.30,\quad d=R-r_0=0.08,\quad
\alpha=0.55,\quad\beta=1.1,\quad\lambda=1.
$$
在 $r_0<r<R$ 令 $t=(r-r_0)/d$，
$$
w_{\rm conn,\varphi}(r)=w_\varphi(r)+
       \lambda\frac{t^\beta}{(1-t^2)^\alpha}. \tag{1}
$$
在 $r\le r_0$ 第二项准确为零。从核心向平帽走时，半径减小而高度上升；曲面是否满足目标曲率仍须本次实际检查。

以
$$
m=(1-\alpha)^{-1}=20/9,\qquad r(x)=R-dx^m,\qquad 0\le x\le1
$$
消除核心图斜率的发散。连接体的准确位置 jets 为
$$
a_x=-dmx^{m-1},\quad a_{xx}=-dm(m-1)x^{m-2},
$$
$$
z_x=dm\lambda\frac{(1-x^m)^\beta}{(2-x^m)^\alpha}
       -a_x w_\varphi(a(x)). \tag{2}
$$
因 $m(1-\alpha)=1$，(2) 在 $x=0$ 的第一项是正有限常数，且
$a_x=a_{xx}=z_{xx}=0$，所以接开垂直圆柱是 C2。因 $\beta>1$，
额外的 $z_x,z_{xx}$ 在 $x=1$ 都为零，故与同一尾在 $r=r_0$ 准确 C2 相容。后续尾仍可用同一单调 r(x) 参数延伸，避免把材料重参数造成的二阶差误当接缝。

本输入是固定的 C2 连接头，未宣称 C-infinity。根的存在所需连续周期参数和正 $z_x$ 仍满足 R571 的普通微分方程论证。

## 3. 真正的匹配、归一和几何观测

角模 j 在连接体满足
$$
A_x=-(j^2-1)\frac{a_x}{a}A-j^2\frac{z_x}{a}C,\qquad
C_x=-\frac{a_x}{z_x}A_x.
$$
从真实尾口 $(A,C)=(a_V,f)$ 反向积分至核心。求根用
$C_{\rm core}/\sqrt{A_{\rm core}^2+C_{\rm core}^2}$，保留相位绕圈时的符号；没有用会在 $A_{\rm core}=0$ 产生极点的比值冒充全程连续函数。根处再给 $C_{\rm core}/A_{\rm core}$，并报告它对相位的一阶数值导数，作为后续 Lyapunov–Schmidt 幅度条件的实际入口。

同一根上的容差加密与 M/M+1 比较采用相同容差配对，不把数值误差和准确 DtN 截断界混在一起。固定核心归一后的场报告
$V,V_s,V_{ss},V_\theta/a,V_{s\theta}/a,V_{\theta\theta}/a^2$ 的已声明节点峰；s 是 meridional arc length。它们是明确坐标下的二阶代价观察，非连续 C2 证书。

连接体曲率用实际 $a,z$ 的解析二 jets 计算；除4097个均匀 x 节点，还取距两端 $10^{-k}$、$k=1,\ldots,12$ 的节点。仍明确标为有限采样。帽高还用
$$
h_{\rm cap}=z_{\rm core}+\int_{r_c}^{R}w_\varphi(r)\,dr+
 \frac{\lambda d}{2}B((\beta+1)/2,1-\alpha)
$$
计算，$z_{\rm core}=0.04$。本次不宣称跨块 reach 或完整闭面门已经支付。

## 4. 高次谐波与有限分支的边界

seed helper 的一般 j 变换是
$$
p=(A/\ell)u^2r^{2j^2}e^{-u(2-\sin(u+\varphi))},\quad
\varepsilon=\frac{j^2(j^2-1)\ell^2}{r^2u^4},\quad f=r^{j^2}y.
$$
模式2由 R571 证明。模式4、6、8在本次只给有限末端数值传递，理论截断界字段为空，未将 j=2 的常数套给它们。即使三个核心响应远离0，也不等于全频率小分母或 tame inverse 已支付。

若根的两个步长导数不稳定或接近零，应调整一个明确连接头控制（例如 lambda）重新求根；若核心归一 C2 仍很大，应换更慢相位或共同设计末段振荡与连接头，不能只把场缩得看不见。若实际根简单且代价可用，下一步才是在选定静态 metric/profile 上求完整非线性等距方程；设计参数 phi(epsilon) 的变化不冒充课题要求的同 g 弯曲。
