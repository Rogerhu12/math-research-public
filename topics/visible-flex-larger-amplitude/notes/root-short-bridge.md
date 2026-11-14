# 更小尾口的 C² 短连接

2026-11-10，visible-larger-astra-20261110。

**状态：连接 profile 的公式与 C² 性已证明；前缀仅有有限 linear-DN 数值解，未有闭图。**

## 原三次角桥的失效范围

原式 $\phi(u)=p_t(3u^2-2u^3)+Lp_s(u^3-u^2)$ 在新的 $(r,w)=(.35,.08)$、$(.30,.08)$ 上分别达到约 $1.5786742$、$1.6138867$，均超过 $\pi/2$。这里的 extrema 用三次式的准确临界点计算，长度仍按给定求积计算。保持原正 binormal 表示时不能直接采用这些桥。脚本 `root_profile_scan.py` 已加入相应检查，避免在越界点把 $\sqrt{1-a'^2}=0$ 送入线性方程。

这只排除了该三次连接公式，不排除这些 tail cut；tail 本身的线性及非线性数据仍有意义。

## 分段角函数

给定内向 cut $0<r_t<1,w_t>0,w'_t<0$，设

$$
p_t=\arctan(1/w_t),\quad p_s=w'_t/(1+w_t^2)^{3/2}<0,
\quad p_*=p_t+\eta(\pi/2-p_t),\quad0<\eta<1.
$$

设 $\varepsilon=p_*-p_t$，选择转角速度上界 $K>0$，令

$$
L_1=\frac{3p_*}{2K},\qquad L_3=\frac{2\varepsilon}{-p_s}.
$$

第一段用 $p_*(3u^2-2u^3)$ 升角；第二段保持 $p_*$；第三段用 $p_*-\varepsilon u^2$ 降至 $p_t$。三段分别长 $L_1,L_2,L_3$。令第一和第三段的 $\int\sin\phi\,ds$ 为 $R_1,R_3$，并定义

$$
L_2=\frac{1-r_t-R_1-R_3}{\sin p_*}.
$$

只接受 $L_2\ge0$。于是

$$
a(s)=1-\int_0^s\sin\phi(\sigma)\,d\sigma,
\quad z(s)=\int_0^s\cos\phi(\sigma)\,d\sigma
$$

满足 $a(L)=r_t$、$a'(0)=a''(0)=0$，且末端

$$
a'(L)=-\frac1{\sqrt{1+w_t^2}},\qquad
a''(L)=-\frac{w_t w'_t}{(1+w_t^2)^2},
$$

与原 physical cut 的二 jet 相同。

**证明。** 第一段和 plateau 接点的角速度均为零，plateau 和第三段接点也如此，故 $\phi$ 为 $C^1$。第三段末角速度 $-2\varepsilon/L_3=p_s$，第一段初角速度为零。积分定义给出 $a,z\in C^2$ 及上述端点式。所有角值属于 $[0,p_*]$，严格小于 $\pi/2$，所以 $z'>0$。对应旋转背景的子午主曲率绝对值为 $|\phi'|\le\max(K,|p_s|)$，纬向主曲率为 $\cos\phi/a\le1/r_t$。这些是背景界，不是非轴对称实际前缀的曲率界。证毕。

实现 `computations/root_short_bridge.py` 用64点 Gauss 积分计算这些解析积分。定义本身不依赖求积近似。tagged dispatch 只改变明确记录 `prefix_bridge` 的候选，旧 checkpoint 仍按原桥重建。其内部节点同时加入实际流和 BVP 网格；checkpoint 的 profile 记录完整桥参数。

## 实际计算

新 cut $r=.30,w=.08,w_r=-1.866666\ldots$，$\eta=.5$：

| 背景转角界 K | 连接长度 | 连接高度 | 最小 $\cos\phi$ |
|---:|---:|---:|---:|
| 4 | .9312223193 | .3719762007 | .0399043949 |
| 8 | .8159050651 | .2002532048 | .0399043949 |

K4、vu=.55、vd=.6 的 m2 线性根 $\delta\approx.1718058081$。真实 q=.02/M8 natural-core BVP 随后收敛至 $\delta=.17180423817742066$；实际采样 metric约 $1.2198\times10^{-8}$、曲率约4.18907、高度1.28603，terminal H最大约 $.00026635261$，Frenet root margin最小约 $.00127121$。数据为 `notes/root-smallcut30-k4-q02-m8*`。这是 finite **linear** DN 前缀，不是实际 tail 联解。

K8/vu=.55 与 K4/vu=.35 的 m2/m4 双共振局部初搜均未得到根，失败数值已保存；这不是不存在双根的证明。下一步优先实际 tail 接合和有限 neck 衰减结构，不把背景高度或小 BVP 残差当完成条件。
