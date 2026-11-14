# 当前 projected core 的准确轴点与完整相对 G 输运分解

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：恒等式与有限有理轴点待独审；实际沿程积分是浮点诊断。** 本文不改变
当前 M14 图、原度量、core 参数、warp、数值计划或 M15 入口。没有新 BVP、
优化、tail 请求或流积分来生成候选；只读取已经成功保存的当前曲线。

这里把三件事分开：完整材料坐标下的严格输运恒等式；当前 CP 入口处可由
Fraction 精确核验的相对 $G$ 缺陷；固定曲线的两档浮点积分分解。
后者不冒充全区间误差证书。本文也不自动把 CP 点转移成最终 common 图的
新证书；该对象绑定仍需按其实际生产链验证。

## 1. 真实输入及原源绑定

当前 CP 为
`notes/2026-11-10-78718-numerical-m14-restart8000-02.json.gz`，SHA256
`4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a`。
脚本在终端内核对其各 PP 系数分片的字节数与 SHA；没有将数组读入对话。
完整原 source route 沿用
`scripts/db6f-prefix-flat-geometry-source.py::source`，并对实际导入的原 Python
源逐件核对既有已绑定诊断中的身份，运行结束再复核。

既有诊断是
`notes/2026-11-10-78718-numerical-fixed-state-projection-01.json`，208191 B，SHA256
`53641e7e8ceb2ea822794a9df5404807a5162aa704aa9ee35be99b3c2d86dbfe`。
其原完整方法见 numerical 的
[误差来源分析](2026-11-10-78718-numerical-fixed-state-projection-analysis.md)。
本文只取当前 CP、M14/N512 的几个标量，并重新计算入口/轴线；不是凭旧表
外推新计算结果。

这条真实 source route 使用原全部14个 support 系数、原 frozen chart 和
原 M14/N512 RHS。不能将初值简化成单一 $1+q\cos3\phi$；`initial()` 确实先
反解法向角，再把 exact core 与 untruncated round background 的差投到有限
warped basis。保存入口与重算原 callback 的物理系数最大差仅约
$2.7886\times10^{-17}$；本文没有把两者改成相等。

## 2. 材料导数、convective 项与完整 Frenet 恒等式

设实际固定角图为
$$
u=\Theta(s,\psi),\qquad \rho=\Theta_\psi>0,
\qquad b=\frac{\Theta_s}{\rho}.
\tag{1}
$$
对 Cartesian 向量函数 $F(s,\psi)$，真正的材料导数为
$$
D_s=\partial_s-b\partial_\psi,\qquad
D_u=\rho^{-1}\partial_\psi.
\tag{2}
$$
它们可交换。直接计算的 $\partial_\psi$ 系数为
$$
[D_s,D_u]=\frac{-\rho_s+b\rho_\psi+\rho b_\psi}{\rho^2}\partial_\psi=0,
\tag{3}
$$
因为 $\rho b=\Theta_s$，而 $\rho_s=\partial_\psi\Theta_s$。
因此不能把固定 $\psi$ 导数一般当作固定材料 $u$ 导数；后文两个轴点才因
$\Theta_s=0$ 有这一简化。

记角曲线的 $d=F_\psi$、$\lambda=|d|$、单位切向 $\tau=d/\lambda$。
令 $\nu$ 为主法向、$\eta=\tau\times\nu$，曲率为
$\kappa=|(I-\tau\otimes\tau)F_{\psi\psi}|/\lambda^2>0$。
原 `Flow.frame` 使用的 raw **物理**速度是
$$
V=-\frac{\mu}{\kappa}\nu+
\sqrt{1-\frac{\mu^2}{\kappa^2}}\,\eta,
\qquad \mu=\frac{a_s}{a},
\tag{4}
$$
在程序声明的正根域 $1-\mu^2/\kappa^2>0$ 取该根。
原 raw **固定图**速度则是
$$
W=V+bF_\psi.
\tag{5}
$$
它包含原源码中的 convective 项，不能遗漏后再声称仍是同一 RHS。

令 $T=D_uF$、$G=|T|^2$。无需先假设 $G=a^2$，(4) 直接给
$$
|V|=1,\qquad V\cdot T=0,\qquad
V\cdot D_uT=-\mu G.
\tag{6}
$$
最后一个等式的证明是
$D_uT=\rho^{-2}F_{\psi\psi}-\rho_\psi\rho^{-3}F_\psi$；第二项与 $V$
正交，而第一项的主法向分量为 $\kappa\lambda^2/\rho^2=\kappa G$。
原程序的 $\alpha=-a_s/(a\kappa)$ 因而给 (6)。

**这里右端是 $-\mu G$，不是在所有状态下都等于 $-aa_s$。** 后一种写法
只在已经等距的 $G=a^2$ 子集成立；先前口头讨论的未归一式不能用于当前
有入口误差的保存曲线。

定义实际物理速度缺口
$$
e=D_sF-V=F_s-W,
\qquad \Gamma=\frac{G}{a^2}-1.
\tag{7}
$$
用 (3)–(6) 得
$$
D_sG=2T\cdot D_u(V+e)=2\mu G+2T\cdot D_ue,
$$
从而准确的全状态恒等式是
$$
\boxed{\quad D_s\Gamma=\frac2{a^2}T\cdot D_ue.\quad}
\tag{8}
$$
同时，两个其它物理 metric 分量满足
$$
|D_sF|^2-1=2V\cdot e+|e|^2,
\qquad (D_sF)\cdot T=e\cdot T.
\tag{9}
$$

这没有给全题增加 $C^3$ 要求。对 $C^2$ 的 $F,\Theta$，正根域内 $V$ 至少
连续；将 $T\cdot D_uV$ 定义为
$D_u(T\cdot V)-(D_uT)\cdot V$，上述乘积法则在分布意义仍成立，并由 (6)
化为连续函数。当前有限 Fourier/PP 曲线在每个原分段内具有更多正则性，
数值积分使用普通函数；跨节点按其原 $C^2$ 接合，不另加奇点源。

若保存曲线真正满足未投影 raw 流 $e=0$，则 (8) 说明每条材料线的
**相对**角向缺陷 $\Gamma$ 恒定。原 raw 流不会自动把一个非零初始
$\Gamma(0,u)$ 消掉；它也不是一般保持绝对差 $G-a^2$ 不变。

## 3. 实际有限投影与不容省略的交换子

写保存的 Cartesian 曲线为
$$
F=X_0(s,\psi)+q\sum_iY_i(s)B_i(\psi)+\bar z(s)e_z,
\quad X_0=a(s)e_r(\Theta(s,\psi)).
\tag{10}
$$
$B_i$ 是原 `CylindricalPrefix.basis` 的完整向量基，而不是固定不动的
Cartesian 标量基。令 $\Pi_{M,N}$ 表示程序在原 $N$ 个角点上计算系数后
重构到这些 $B_i$、并补入竖直 mean 的采样投影。原系数 RHS $R_{M,N}(Y)$
满足
$$
q\sum_i(R_{M,N}(Y))_iB_i
=\Pi_{M,N}(W-X_{0,s})-\langle W_z\rangle_N e_z.
\tag{11}
$$
据此，完整缺口分成
$$
\begin{aligned}
e_{\rm proj}&=(\Pi_{M,N}-I)(W-X_{0,s}),\\
e_{\rm interp}&=q\sum_i(Y_i'-R_{M,N}(Y)_i)B_i,\\
e_{\rm mean}&=(\bar z'-\langle W_z\rangle_N)e_z,
\qquad e=e_{\rm proj}+e_{\rm interp}+e_{\rm mean}.
\end{aligned}
\tag{12}
$$
$D_ue_{\rm mean}=0$，所以任意纯径向 mean-height 重构误差不进入 (8)。
其它两项都保留在相同的材料坐标下。

尤其，没有使用错误的交换关系 $D_u\Pi_{M,N}=\Pi_{M,N}D_u$。
实际要取的是
$$
D_ue_{\rm proj}=\rho^{-1}\partial_\psi
\big[(\Pi_{M,N}-I)(W-X_{0,s})\big],
\tag{13}
$$
而 $\rho^{-1}$ 依赖 $\psi$，向量基也随 $\psi$ 旋转。
即使无限精度计算采样系数，仍不能删去这个交换子。
下文直接对投影后重构的向量基求导，包含该项；没有用“对原 RHS 求导后再
投影”代替它。

## 4. 两条实际固定材料轴与 Cartesian 旋转换基

当前图确为
$$
\Theta(s,\psi)=\psi-\frac{e(s)}3\sin3\psi,
\quad e(s)=8q_{\rm ref}\,h(s/s_{\rm end})\,\chi(s/s_{\rm end}),
\tag{14}
$$
此处原源记为 $e(s)$ 的标量是角 warp，区别于 (7) 的速度缺口向量。
其中 $h$ 是冻结原 spline，$\chi$ 是原末端五次 cutoff。未删去 cutoff
或 spline 的导数。取 $\psi=0,\pi/3$，记 $\sigma=\cos3\psi=1,-1$。
这些点对所有 $s$ 都有 $u=\psi$、$b=0$，所以是固定材料线；但
$$
\rho=1-\sigma e(s),\qquad \rho_s=-\sigma e_s(s)
\tag{15}
$$
通常仍不为常数，不能把 $\rho_s$ 省略。

原基的水平扰动写为
$$
R=Y_0+\sum_{j=1}^M R_j\cos(3j\psi),\quad
T_\theta=\sum_{j=1}^M T_j\sin(3j\psi),
\qquad R e_r(\psi)+T_\theta e_\theta(\psi).
$$
由于 $e_r'=e_\theta$、$e_\theta'=-e_r$，完整 Cartesian 导数是
$$
\partial_\psi(R e_r+T_\theta e_\theta)
=(R_\psi-T_\theta)e_r+(R+(T_\theta)_\psi)e_\theta.
\tag{16}
$$
在上述轴点，竖直导数及 (16) 的径向项都为零。设
$$
B_\sigma(s)=Y_0(s)+\sum_{j=1}^M\sigma^j
\big(R_j(s)+3jT_j(s)\big).
\tag{17}
$$
于是
$$
F_\psi=(a\rho+qB_\sigma)e_\theta,\qquad
r_\sigma=\frac{qB_\sigma}{a\rho},\qquad
\boxed{\quad\Gamma_\sigma=2r_\sigma+r_\sigma^2.\quad}
\tag{18}
$$
式 (17) 中的 $Y_0$、每个 $R_j$ 正是旋转基导数贡献，不是可省的“低阶项”。
同理，轴点虽然 $b=0$，其角导数可不为零；(15) 保留的 $\rho_s/\rho$ 正是
这一 convective 换基在最终标量公式中的必要部分。

对任意系数导数 $Z_i$，记 $\mathcal B_\sigma(Z)$ 为 (17) 的同一线性组合。
从 (18) 的实际 $s$ 导数直接得到
$$
\mathcal D_\sigma(Y,Z)
=\frac{2(1+r_\sigma)q}{a\rho}
\left[\mathcal B_\sigma(Z)
-B_\sigma\left(\frac{a_s}{a}+\frac{\rho_s}{\rho}\right)\right].
\tag{19}
$$
其三个准确用途是
$$
\begin{aligned}
\partial_s\Gamma_\sigma&=\mathcal D_\sigma(Y,Y'),\\
\frac2{a^2}T\cdot D_ue_{\rm proj}
&=\mathcal D_\sigma(Y,R_{M,N}(Y)),\\
\frac2{a^2}T\cdot D_ue_{\rm interp}
&=\frac{2(1+r_\sigma)q}{a\rho}
\mathcal B_\sigma(Y'-R_{M,N}(Y)).
\end{aligned}
\tag{20}
$$
第二式是对原投影后重构速度使用同一个 (18)–(19)，再用 (8)；没有把
投影和角导数交换。三式对同一当前状态成立，不要求这个状态解原 Galerkin
ODE。因而能严格区分有限投影源与保存 PP 导数不满足 RHS 的残差。

## 5. 当前入口的两个精确有限有理点

在 $s=0$，原 flat profile 有 $a=1$，冻结 chart 的首节点和值恰为0和1，
所以 $e(0)=8q_{\rm ref}$。保存 PP 第一个区间的常数系数就是原节点值；
程序实际核对这一逐浮点位相等关系。

将所有保存 binary 浮点解释成准确有理数，(17)–(18) 只需有理加乘除。
三角函数在两轴均按精确的 $\sin(j\pi)=0$、$\cos(j\pi)=(-1)^j$ 消去；
没有用浮点 $\pi$ 采样来制造有理结论。$e_\theta$ 的单位长度也在数学上
准确，因此 $\psi=\pi/3$ 的 $\sqrt3$ 分量不进入最终范数。

冻结程序
`scripts/78718-geometry-core-g-transport-v1.py`，SHA256
`9c4cba0e1b9f60a4d826a26ffc1d59ffaf19a54471abd17aee76cd909e3da77f`，
以 `--orders` 空列表只做端点，真实 **780182 自然 exit0**，约0.616秒。
输出 `notes/2026-11-10-78718-geometry-core-g-endpoints-v1.json`，11973 B，SHA256
`121b62724cbc3161e36d11f90eac873af7897b8a2c62d1d994aa16314a833d31`。
它保留两个轴的完整分数、原 callback 对照、全部输入/源码身份。

该准确有理值在 $\psi=0$ 满足
$$
-1.34\cdot10^{-8}<\Gamma(0,0)<-1.33\cdot10^{-8},
\qquad |\Gamma(0,0)|>\frac1{500000000}.
\tag{21}
$$
十进小数区间端点也按有理数比较；报告中的数值近似为
$-1.3311421121020634\times10^{-8}$。在 $\psi=\pi/3$，近似值为
$+5.087810850200969\times10^{-11}$，这一轴不超原门。
对保存原 callback 的另一组明确有限 binary 系数，同样公式在 $\psi=0$
给近似 $-1.3311430989441333\times10^{-8}$。
因此主要入口缺陷不是因为保存曲线没有满足其有限初始 BC；是该有限
projected-core 曲线本身具有该角向 metric 缺陷。

未投影的 support 源是按弧长反解后的真实曲线，在其正则域有
$F_u=e_\theta(\phi)$、$|F_u|=1$。有限 warped 投影改变了这个几何事实。
本文没有据此否定该 exact support core，也没有说所有频率加密都保留同一
入口缺陷；这里的准确对象只是当前明确存储的有限曲线。

同一程序还复核原绑定报告的几个标量：当前 M14/N512 的 core $G/a^2-1$
FFT-l1 为 $1.331142867031318\times10^{-8}$，恰为原10点全部 $G$ 诊断最大值；
native node1518、$s\simeq .27472985991302756$ 的相应 FFT-l1 约
$2.0882933276118818\times10^{-9}$。这两个 FFT 数仍只是原有限角诊断，
与 (21) 的精确单点证明分开。

## 6. 同一保存曲线的真实沿程分解

同一冻结程序的另一调用使用 `--orders 4 8`，真实启动
**da4902 / session95561**，由 **98958b** 观察到**自然 exit0**，约30.560秒。
报告为 `notes/2026-11-10-78718-geometry-core-g-transport-v1.json`，15042 B，SHA256
`69afb89bcfd7e63c89bcce9e1c2f59519503bb5520876087ec5a287e6e70c523`。

积分区间是原 $s=0$ 到 native node1518，保持原1518个 PP 区间，同时保留
所有位于其中的真实 profile/chart 分段点；没有移动节点或改变插值。
4点和8点 Gauss–Legendre 两档真算，细档12144个径向点；每处以原 N512
完整 frame/RHS 求 $R_{M,N}(Y)$。它不是只对采样速度外推，也没有重新求
曲线。报告记录原全部动态导入源并逐件与第1节原绑定来源相等。

细档得到以下固定曲线诊断：

| 材料轴 | $\Gamma(s_{1518})-\Gamma(0)$ | 投影源积分 | 保存 PP 导数减 RHS 的积分 |
|---|---:|---:|---:|
| $u=0$ | $1.2905521071890081\cdot10^{-8}$ | $1.2905521114944536\cdot10^{-8}$ | $-4.045472099937402\cdot10^{-17}$ |
| $u=\pi/3$ | $3.6733935524619177\cdot10^{-10}$ | $3.673393566569391\cdot10^{-10}$ | $-1.392246109509222\cdot10^{-18}$ |

第一列端点的 $\Gamma(s_{1518})$ 分别约
$-4.0590004922576363\times10^{-10}$ 和
$+4.1821746374498706\times10^{-10}$。
总导数积分与端点差的浮点闭合差分别约 $2.60\times10^{-18}$ 和
$1.85\times10^{-20}$。两档投影源积分之差分别约
$5.89\times10^{-19}$ 和 $9.49\times10^{-19}$。

这些小差给实际浮点重算的内部一致性，不是对积分或整个连续曲面的区间
包围。它们不能提升 (21) 之外的部分为严格数值证书。
零新 BVP、零 tail 请求、零非线性流积分、零新候选都由实际程序路径保持。

值得区分方向：在 $u=0$，当前 Galerkin 沿程变化 **抵消了大部分初始负的
相对 $G$ 误差**；它不是这条轴上初始误差的来源。原未投影 raw 流反而会
保持入口的非零相对误差。仅提高固定曲线上的速度投影阶数既不会改正已经
保存的 $F_u$，也不能被当成一张已修正的几何。

## 7. 对当前 G5 的具体用途与范围

本稿将实际终门问题定位到两项需要分别受控的数值逼近：真实 core 经有限
warped 投影后的入口 metric，以及沿程有限速度投影。当前 M14 的径向容差
和保存 PP 残差不是这里 $G$ 主尺度的解释；这一点有原源码恒等式和实际
固定曲线计算支持，不只是由全局最大误差猜测。

M15 的真正重求仍按已冻结方案进行。本稿没有调整其物理参数、core 自由度、
tail、RHS 或初猜，也没有把当前 core 在更大空间的重新表示当作新曲面。
新曲线仍须重新计算其自有的入口、prefix、尾、共同图、全域全时 metric
及其它原门，不能继承这张旧曲线的近似数。

以上不是一般不可能性结论。随着真实曲线和入口频率共同加密，有限投影
缺陷可以改变；本稿不说明它是否按所需速度下降。CP 点与最终 common map
的身份转移，也不因同一文件名或同一背景就自动完成。精确存在、严格无限尾
和 README/G5 仍按原题标准另行支付。

