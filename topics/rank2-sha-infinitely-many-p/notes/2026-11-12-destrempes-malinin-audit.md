# 对一个声称“几乎所有素数消失”的来源的核查

日期：2026-11-12（UTC+8）。会话子任务：literature_scope。

**状态：以下反驳与错误定位已证明；主课题仍未解决。**

## 被核查的来源与用途

François Destrempes、Dmitry Malinin，*On the vanishing of almost all primary components of the Shafarevich-Tate group of elliptic curves over the rationals*，arXiv:1703.02215v2，2018 年修订。

- 官方版本页：<https://arxiv.org/abs/1703.02215v2>。
- 实际核对的 PDF 文本：<https://arxiv.org/pdf/1703.02215>，页眉标 v2，全文 63 页；未逐页渲染，也未把 PDF 加入仓库。

该稿 Theorem 5 声称：非 CM 曲线满足大像及好约化等条件时，所选素数的 Sha-primary 群消失，因而覆盖几乎所有素数。这个声称若有正确证明将涵盖本课题。但下面三个独立问题禁止将该稿当作证明使用。不是仅因“未被公认”而排除。

## 1. 原始扭点可任意逼近非零 2-扭点

**命题。** 设 $E/\mathbb C$ 为椭圆曲线，$\ell$ 为奇素数。存在精确阶为 $\ell^n$ 的点 $P_n$，收敛到一个非零 2-扭点 $T$。

**证明。** 取复一致化 $E(\mathbb C)\simeq\mathbb C/(\mathbb Z\omega_1+\mathbb Z\omega_2)$，令
$$
z_n=\frac{\ell^n-1}{2\ell^n}\omega_1,
\qquad P_n=[z_n],\qquad T=[\omega_1/2].
$$
因为 $(\ell^n-1)/2$ 是与 $\ell$ 互素的整数，$P_n$ 的阶恰为 $\ell^n$。而 $z_n\to\omega_1/2$，故 $P_n\to T$。若短 Weierstrass 方程为 $y^2=x^3+Ax+B$，则在 $T$ 附近 $x$ 连续，$x(P_n)\to x(T)=e_1$。若 $A,B\in\mathbb Z$ 且曲线非奇异，所有三次多项式根都严格落在文中使用的有界圆盘内：设 $C_1=\sqrt{2(|A|+|B|)}\ge1$，若 $|e|\ge C_1$，则
$$
|e|^3\ge2(|A|+|B|)|e|>|A||e|+|B|,
$$
与 $e^3+Ae+B=0$ 矛盾。因此 $P_n$ 的横坐标最终也在该圆盘中，文中全体原始 $\ell^n$-扭点横坐标到 $e_1$ 的距离下确界为零。证毕。

这直接否定该稿 Proposition 2(a)（PDF pp.22–24）所使用的统一正距离 $\delta>0$。具体错误在 proof Step 6、式 (107) 后：由
$$
x(P_{n_k})-x([\ell]P_{n_k})\longrightarrow0
$$
推导
$$
x([1-\ell]P_{n_k})\longrightarrow0
$$
不成立。横坐标函数不是群同态。上述序列中，前式确实成立，因为 $[\ell]T=T$；后者群点却趋于 $[1-\ell]T=O$，其横坐标趋向无穷点而非零。

此处只是否定稿件使用的论证和正距离断言，并未声称某个带迹平均的较弱不等式也被这一条单独否定。

## 2. 单个分裂素理想不控制全局迹

该稿 Theorem 6 proof Step 2（PDF p.29，式 (135)–(137)）需要从 $\alpha_0\in\mathfrak P$（某一个 $\mathfrak P\mid p$）推出 $\operatorname{Tr}_{L/\mathbb Q}(\alpha_0)\in p\mathbb Z$。

这一推理在所显示的一般条件下不成立。取
$$
L=\mathbb Q(i),\quad p=5,\quad
\mathfrak P=(2+i)\subset\mathbb Z[i],\quad\alpha_0=2+i.
$$
有 $N(2+i)=5$，所以 $\mathfrak P$ 是 $5$ 上方素理想，且 $\alpha_0\in\mathfrak P$；但是
$$
\operatorname{Tr}_{L/\mathbb Q}(2+i)=4\notin5\mathbb Z.
$$
局部迹求和确实是全局迹，但 $\alpha_0$ 在另一个 $5$ 上方素理想中未必是非单位。因此局部迹图本身不能提供所需结论；还需利用该稿所构造 $\alpha_0$ 的其他性质另证全局迹同余。这个例子只否定该条一般推理，不单独证明原稿特殊 $\alpha_0$ 的结论必定失败。独立且直接反驳统一抬升断言的是下一节的计数证明。

## 3. Theorem 6 的统一有限抬升集与分裂素数冲突

该稿 Theorem 6 及 Remark 4、§3.5 声称：固定 $E,\ell$ 后，存在只依赖这两者的常数 $C$，使所有好素数 $p\nmid\ell(\ell^2-1)\Delta_E$ 上的非零 $\ell$-primary 约化点均能由如下代数点抬升：
$$
y(P)^2=a/b,\qquad 1\le|a|,|b|\le C.
$$

**命题。** 对任意 $E/\mathbb Q$ 及固定素数 $\ell$，这种统一有限抬升集不存在。

**证明。** 由于允许的有理数 $a/b$ 只有有限个，每个值有至多两个 $y$ 及三个 $x$，符合条件的代数点组成有限集 $S\subset E(\overline{\mathbb Q})$。记 $M=|S|$。取 $n$ 使 $\ell^{2n}-1>M$。Chebotarev 密度定理保证有无穷多个素数 $p$ 在有限 Galois 扩张 $\mathbb Q(E[\ell^n])/\mathbb Q$ 中完全分裂；从中除去有限多个坏约化素数、$\ell(\ell^2-1)$ 的因子及 $S$ 的坐标分母所涉及的素数。对余下的任一 $p$，$E[\ell^n]$ 的 $\ell^{2n}$ 个点全在 $\mathbb F_p$ 上，而且因 $p\ne\ell$ 好约化映射在 $E[\ell^n]$ 上单射。因此非零 $\ell$-primary 约化点至少有 $\ell^{2n}-1$ 个。固定一个到 $\overline{\mathbb Q}_p$ 的嵌入后，集合 $S$ 的约化至多 $M$ 个，不能覆盖它们，矛盾。即使允许所有嵌入，先取 $S$ 的有限 Galois 轨道并把 $M$ 换成轨道并集的大小，论证不变。证毕。

不需要满 Galois 像假设；加入该假设也不会消除矛盾。如果把原文常数解释成可依赖 $p$，则上述矛盾不适用，但其后 §3.5 固定有限域 $K'$ 的步骤立即失去依据，仍无法证明 Theorem 5。

## 结论

该来源未提供本课题可用的无条件定理。至少两处局部推导错误，且其核心统一抬升定理本身与有限集计数矛盾。暂未发现能保留其目标并修复以上步骤的方法；修复不能只换一个常数或增加有限个例外素数。
