# 同一 phase 候选的三 jet、R37 主图与目标参数口径

2026-11-12，constructive-route。

本记录固定输入为 data/fourfold_phase_m24n201_q256_checkpoint.npz，
SHA256 为 63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e。
它是有限径向样条及有限切向角系数定义的 R33 无限角场，
不是精确闭等距面。全部计算保持此对象和保存的 circumference-radius
shift；不迁移旧 n101 位置图的 action、曲率类型或返回数。

## 1. 一个共同有限原函数的全部三 jet

脚本 fourfold_phase_geometry.py 从保存的实 beta/gamma 样条直接读
三阶径向导数。权重仍是原 base 半径的三次、二次幂，参数变化中
保存的 radius shift 固定。每条材料圆使用与 PhaseNewton.geometry
相同的 Q256 quarter FFT 原函数，丢掉 quarter Nyquist；所有
$F,F_x,F_\theta,F_{xx},F_{x\theta},F_{\theta\theta}$ 及四个三阶 jet
都由**同一个有限原函数**微分得到。

因此这些数值 jet 内部一致。它们与 R33 无限角定义的差另外用解析
条带尾和混叠界记账，不能把有限原函数的导数直接命名为无限定义
中的 $aT$。所用 Cartesian 截止为 $|n|\le2Q-3$，
等价全圈 FFT 节点数 $4Q$。

若各相位的径向第 $j$ 阶导数条带界为 $b_j,p_j$，令
$$
M=e^{p_0}\{2e^{\sigma+b_0}+1\},\qquad d_j=b_j+p_j.
$$
球面角表达的所有角坐标偏导至三阶都被同一 $M$ 控制，所以
$$
\|T\|_\sigma\le M,\quad
\|T_x\|_\sigma\le Md_1,\quad
\|T_{xx}\|_\sigma\le M(d_2+d_1^2),\quad
\|T_{xxx}\|_\sigma\le M(d_3+3d_1d_2+d_1^3).
$$
对每个输入使用 R33 §5 的原函数尾界；第三角导的新增级数是
$$
2M\sum_{n>N}n^2q^n
=2Mq^{N+1}\left[
\frac{(N+1)^2}{1-q}
+\frac{2(N+1)q}{(1-q)^2}
+\frac{q(1+q)}{(1-q)^3}\right],\quad q=e^{-\sigma}.
$$
保留模的混叠费再加
$4M(1-q^{4Q})^{-1}\sum_{n=1}^N n^2q^{4Q-n}$。
最后用
$$
\partial_x^j F=z_0^{(j)}e_z+
\sum_{k=0}^j\binom jk a^{(k)}\mathcal P(T_{x^{j-k}})
$$
恢复全部混合三 jet 误差。脚本打印的这些界仍以普通浮点计算，
**不含向外舍入证书**。

## 2. 当前候选的实际初检

同一 Q256 原函数在 $x\in[0,.6]$ 的121径向点、每点128角点上：

- 腰部实际 $\det\mathrm{II}\in[-1.59817813,-.95260428]$；
- 腰部实际 $N\in[-8.15823038,-.42713817]$；
- 采样中 $x\le.23$ 仍为全角双曲，$x=.24$ 已为全角椭圆；
- 所采全部 $N$ 严格为负。

六个明确径向点 $0,.1,.2,.24,.3,.5$ 上，选择条带后，
全部三 jet 的解析截断加混叠费最大约 $3.41\,10^{-9}$。
这不是整个径向连续区间的包络，也不证明转折唯一性。
完整数据见 2026-11-12-phase24-actual-type.json。

后续全窗口型别扫描发现，不能把这里的中央双曲分量称为全半面的
唯一双曲区。正侧目标曲率有三个根，约为
$0.23545711,0.42772698,0.45671793$；
后两个根围出额外负曲率环。真实有限原函数也有同样的附加环：
例如 $x=.445$ 的实际 $K$ 约为 $-.504$，全角严格为负。
因此当前对中央分量计算的返回映射只属于其中央散射块，
全局还须消除附加环或将其纳入多分量散射网络。
三根的真实逐角根、根导数、$N$ 及非特征因子另见
2026-11-12-phase24-three-root-mean-control.json。

独立 preflight 与原冻结 geometry 的六个二 jet 相差至多
$3.7\,10^{-11}$。三阶径向有限差分核对误差为
$5.1\,10^{-6}$、两混合项为 $1.2\,10^{-7}$ 和 $2.4\,10^{-8}$；
原 mean 参数的实际判别式导数有限差分误差至多 $2.6\,10^{-8}$。
这些是实现诊断，不是严格余项证书。

## 3. R37 中两个度量行列式不能混用

对当前候选，记
$$
C=F_\theta\times F_x,\quad A=|C|,\quad G_{\rm actual}=A^2,
$$
$$
l=C\cdot F_{xx},\quad m=C\cdot F_{x\theta},\quad
n=C\cdot F_{\theta\theta}.
$$
真实曲面的主判别式是 $m^2-ln$。

另一方面，选径向目标度量
$$
g_0=E(x)\,dx^2+a(x)^2d\theta^2,\qquad E=\langle|F_x|^2\rangle,
$$
其中 $a$ 为该 phase 表示的周长半径。有限原函数的 $E$ 及其导数
由 Fourier Parseval 准确给出：
$$
E'=2\langle F_x,F_{xx}\rangle,\qquad
E''=2\langle |F_{xx}|^2+F_x\cdot F_{xxx}\rangle.
$$
令 $G_0=Ea^2$，则
$$
K_0=-\frac{a''}{aE}+\frac{a'E'}{2aE^2},\qquad
D_0=-K_0G_0=aa''-\frac{aa'E'}{2E}.                      \tag{3.1}
$$

R37 的密度选择使用的是 $G_{\rm actual}$。其准确速度为
$$
c_\pm=-M/N\ \pm\sqrt{-K_0G_{\rm actual}}/|N|.
$$
因此在未归一化的 $m,n$ 变量中必须采用
$$
\boxed{\widehat\Delta=(-K_0)G_{\rm actual}^2
       =A^4D_0/G_0,\qquad
c_\pm=(-m\pm\sqrt{\widehat\Delta})/n,}                  \tag{3.2}
$$
两支的正负命名可交换，几何两族不变。
最初准备代码曾拟使用 $A^2D_0$，audit 在运行前指出它把
$G_{\rm actual}$ 和 $G_0$ 混同；现已修正，没有采用那个不同算子的
返回数据。实际脚本和 JSON 均显式写出 (3.2)。

R37 转折是径向的 $K_0(x)=0$，而非当前真实曲面的移动转折图。
后者仍有独立诊断价值，但不能用它的返回映射作为 (3.2) 的 KAM 输入。

## 4. 本次计算的是同步目标族，选点之后才固定目标

Schur 提供的是同一 phase checkpoint 的三个完整方向：
phase 系数及 mean 同时变化，保持 $\delta\beta_4(0)=0$。
它们只是有限加权 $L^2$ 系统的补正方向，单列剩余不为零，
不冒称一个已存在精确解族的切向。

当前参数化取 $F_p$ 为这些实际 phase 系数方向产生的候选族，并同步取
$$
g_0(p)=E(p)\,dx^2+a(p)^2d\theta^2,\qquad
E(p)=\langle|F_{p,x}|^2\rangle.                         \tag{4.1}
$$
所以返回导数必须包含 $\delta g_0$。选定所需参数 $p$ 后，
modified Newton 才以该单个 $g_0(p)$ 为固定目标。
这两层用途不能混写成“同一固定度量下的 mean 核”。

写实际方向 $V=\partial_pF_p$，$A_0=\delta a$。有
$$
\delta E=2\langle F_x\cdot V_x\rangle,\qquad
\delta E'=2\langle F_{xx}\cdot V_x+F_x\cdot V_{xx}\rangle,
$$
$$
\begin{aligned}
\delta D_0={}&A_0a''+aA_0''
-\frac{(A_0a'+aA_0')E'+aa'\delta E'}{2E}
+\frac{aa'E'\delta E}{2E^2},\\
\delta G_0={}&a^2\delta E+2EaA_0,\\
\delta(-K_0)={}&\delta D_0/G_0-D_0\delta G_0/G_0^2.
\end{aligned}                                                   \tag{4.2}
$$
同时 $\delta A=C\cdot\delta C/A$，
$\delta C=V_\theta\times F_x+F_\theta\times V_x$，所以
$$
\boxed{\delta\widehat\Delta
=4A^3\delta A\,(-K_0)+A^4\delta(-K_0).}                 \tag{4.3}
$$
若正转折为 $x=t(p)$，则
$t_p=-\delta D_0(t)/D_0'(t)$，与角无关；
返回变分仍须加入这个真实移动端点项。

在 phase 表示中，裸 mean 方向准确是
$V=C_0e_z+A_0\mathcal PT$，而非旧位置 Fourier 图中的
$A_0e_r+C_0e_z$。若另有 phase 补正，
$$
V=C_0e_z+A_0\mathcal PT+a\mathcal P(\delta T),\qquad
\delta T=T_\phi\,\delta B+T_\psi\,\delta\psi.
$$
所有径向二 jet 都由这一相同公式求导，radius shift 不被暗中变化。

## 5. 径向重参只在其正确目标口径下是 gauge

若 $F_p(x,\theta)=F(h_p(x),\theta)$，
$\partial_ph_p|_0=\xi(x)$，则 $V=\xi F_x$，
且同步目标恰按同一径向坐标变化拉回。此时
$\delta a=\xi a'$、
$\delta E=\xi E'+2E\xi'$，真实及 R37 同步目标的主返回角都不变。
若 $\xi$ 奇且在两端为零，它还能保持腰反射和端高度等相应约束。

这个陈述不把 $V$ 归入**固定** $g_0$ 的齐次等距核。
也不能仅因某个有限 Schur 特征值小便认定它为重参：
需实际检查 $V-\xi F_x$、上述 mean/metric 拉回公式及返回导数。
数值代理另行计算该投影；本模块负责独立的完整返回灵敏度。
