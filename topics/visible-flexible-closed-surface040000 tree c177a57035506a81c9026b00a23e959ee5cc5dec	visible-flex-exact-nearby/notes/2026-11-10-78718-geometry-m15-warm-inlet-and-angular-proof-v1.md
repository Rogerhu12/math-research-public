# M15 原初猜入口：实际参数诊断与严格全角 G 上界

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**已证明的有限对象结论：** 原有、未求解的 M15 初猜在整个入口圆周满足
$$
\left\|\frac G{a^2}-1\right\|_\infty
\le \frac{1302437783}{10^{18}}
=1.302437783\cdot10^{-9}<\frac1{500000000}.
\tag{1}
$$
该界用准确有理 Fourier 代数和显式无穷尾给出，不是采样 FFT 最大值。
它不证明这份初猜满足完整 BVP，也不预言已经启动的真 M15 联解将保留
同一入口参数。本稿没有改变任何参数、曲线或运行中的 solver。

## 1. 实际对象及有限诊断

输入为
`notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz`，27524 B，SHA256
`cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`。
其状态准确为 `UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS`，
`solver_success=false`，2633个原节点、15个参数、46个位置状态。
两件原 PP 分片的内容未变；下面严格结论仅取首块常数系数。

原参数给15项 support core，实际主振幅为
$0.09999976661892393$；gauge 与固定 warp reference 均为所保存的
binary $0.1$。本诊断回放字面保存参数，确认原 `pscale` 与保存的
`central_correction_scales` 逐位一致，不把 loader 重算的 log 首参数
替代这一字面向量，也不把主振幅与 gauge 混同。

真实 **5d9303 自然 exit0**，约0.600秒，比较保存首 PP 值与原
`initial(saved_p)`，再用相同 core 做一次 $N=4096$ 的同阶重新投影。
结果如下；本表全角列仍只是采样 FFT，严格界另由第2–4节证明。

| 入口表示 | 全角采样 FFT $\ell^1$ | 两轴中 $\psi=0$ 的准确分数近似 | $\psi=\pi/3$ 的准确分数近似 |
| --- | ---: | ---: | ---: |
| 保存首 PP 值 | $1.3024481970\cdot10^{-9}$ | $-1.3024377627\cdot10^{-9}$ | $-4.4184488845\cdot10^{-11}$ |
| 字面参数原 $N=2048$ 回调 | $1.3024564362\cdot10^{-9}$ | $-1.3024458677\cdot10^{-9}$ | $-4.4182210355\cdot10^{-11}$ |
| 同 core 的 $N=4096$ 重投影 | $1.3024655986\cdot10^{-9}$ | $-1.3024548886\cdot10^{-9}$ | $-4.4182872575\cdot10^{-11}$ |

保存首值与原回调的物理系数最大差为
$1.1285399857576922\cdot10^{-16}$；原回调与4096点重新投影的差为
$2.7755575615628914\cdot10^{-17}$。这些是浮点对照，不将不同有限对象
说成逐位相同。当前严格界(1)只针对第一行。

因此，本次 M15 初猜的入口比“固定旧 M14 core，再以 M15 表示”所得到的
约 $9.30\cdot10^{-9}$ 明显更好。两者的 support 参数和项数不同，后者
不构成对这个 M15 初猜的先验否决。仍不能将入口通过替代径向真联解、
完整公共图或全曲面 metric 检查。

上述小诊断程序为 `scripts/78718-geometry-m15-warm-inlet-v1.py`，6498 B，SHA256
`cd44ffcb92141d6be3192e519c9867893d1d82f9ddd4c05ff4f604d1697c2dcf`。
报告 `notes/2026-11-10-78718-geometry-m15-warm-inlet-v1.json`，6226 B，SHA256
`bb2f0092971ae8c4d850dc03a60e5534f87c5d6c1e8740b8b08df33a539fc902`。

## 2. 适用于任意有限入口系数的准确 Laurent 公式

本节只要求入口半径 $a=1$，固定图
$$
u=\psi-\frac w3\sin3\psi,\qquad 0<w<1,
\tag{2}
$$
以及原有限位置表示
$$
F(\psi)=e_r(u)+q\bigl(R(\psi)e_r(\psi)
+T(\psi)e_\theta(\psi)+Z(\psi)e_z\bigr)+\bar z e_z,
\tag{3}
$$
其中
$$
R=Y_0+\sum_{j=1}^M Y_{R,j}\cos3j\psi,\quad
T=\sum_{j=1}^M Y_{T,j}\sin3j\psi,\quad
Z=\sum_{j=1}^M Y_{Z,j}\cos3j\psi.
$$
全部 $Y,q,w$ 暂取有理数。令 $\theta=3\psi$、$z=e^{i\theta}$，
$\delta=u-\psi=-(w/3)\sin\theta$、
$\rho=1-w\cos\theta$。定义三个实系数 Laurent 多项式
$$
\begin{aligned}
A(z)&=\sum_{j=1}^M\frac{3jY_{R,j}+Y_{T,j}}2(z^j-z^{-j}),\\
B(z)&=Y_0+\sum_{j=1}^M\frac{Y_{R,j}+3jY_{T,j}}2(z^j+z^{-j}),\\
C(z)&=\sum_{j=1}^M\frac{3jY_{Z,j}}2(z^j-z^{-j}).
\end{aligned}
\tag{4}
$$
按 R82 的完整旋转基求导，扰动导数在
$(e_r(\psi),e_\theta(\psi),e_z)$ 中是 $(iA,B,iC)$。
圆背景导数在同一基中为 $\rho(-\sin\delta,\cos\delta,0)$。

令
$$
E(z)=\exp\left[-\frac w6(z-z^{-1})\right]=e^{i\delta},
\quad E^*(z)=E(z^{-1}).
\tag{5}
$$
在单位圆上 $E^*=e^{-i\delta}$，故
$\cos\delta=(E+E^*)/2$、$\sin\delta=(E-E^*)/(2i)$。
于是角向相对误差 $\Gamma=|F_\psi|^2/\rho^2-1$ 满足准确恒等式
$$
\Gamma=\frac{H}{\rho^2},
\tag{6}
$$
$$
H=2q\rho\left[-A\frac{E-E^*}2+B\frac{E+E^*}2\right]
+q^2(-A^2+B^2-C^2).
\tag{7}
$$
这里 $A,C$ 在单位圆上为纯虚，因而 $-A^2,-C^2$ 正是相应真实导数的
平方。式(7)是实值偶函数，不在中间步骤丢掉 Cartesian 旋转项或竖直
导数。均值 $\bar z$ 的角导数为零。

## 3. 两个显式尾界及严格全角上界

对绝对可和 Laurent 系数定义 Banach 代数范数
$$
\|P\|_{\mathcal A}=\sum_{k\in\mathbb Z}|p_k|.
$$
它满足 $\|PQ\|_{\mathcal A}\le\|P\|_{\mathcal A}\|Q\|_{\mathcal A}$
及单位圆上 $\|P\|_\infty\le\|P\|_{\mathcal A}$。
置 $P=-(w/6)(z-z^{-1})$，则 $\|P\|_{\mathcal A}=x=w/3<1$。
取
$$
E_N=\sum_{j=0}^{N}\frac{P^j}{j!},\qquad E_N^*(z)=E_N(z^{-1}).
$$
幂级数绝对收敛及范数乘法给
$$
\|E-E_N\|_{\mathcal A}
\le\sum_{j=N+1}^{\infty}\frac{x^j}{j!}
\le\varepsilon_E:=\frac{x^{N+1}}{(N+1)!(1-x)}.
\tag{8}
$$
最后一步把每项除以首项后粗界为 $x$ 的几何级数。反转系数不改变
$\mathcal A$ 范数，故用 $E_N,E_N^*$ 替代(7)得到的有理 Laurent
多项式 $H_N$ 满足
$$
\|H-H_N\|_{\mathcal A}
\le\varepsilon_H
:=2|q|(1+w)(\|A\|_{\mathcal A}+\|B\|_{\mathcal A})\varepsilon_E.
\tag{9}
$$
有限平方项没有截断误差。

再令 $D=(w/2)(z+z^{-1})$，即 $D=w\cos\theta$。由于 $\|D\|_{\mathcal A}=w<1$，
$$
\rho^{-2}=(1-D)^{-2}=\sum_{k=0}^{\infty}(k+1)D^k.
\tag{10}
$$
每一项的全部 Laurent 系数非负，因此其范数等于在 $z=1$ 的值。
对 $S_K=\sum_{k=0}^K(k+1)D^k$，准确有
$$
\|\rho^{-2}\|_{\mathcal A}=\frac1{(1-w)^2},
\qquad
\|\rho^{-2}-S_K\|_{\mathcal A}
=T_K:=\frac{w^{K+1}((K+2)-(K+1)w)}{(1-w)^2}.
\tag{11}
$$
后一式是对 $\sum_{k\ge K+1}(k+1)w^k$ 求和，不是数值尾拟合。

将(6)减去完全有限的有理 Laurent 多项式 $H_NS_K$，准确拆成
$(H-H_N)\rho^{-2}+H_N(\rho^{-2}-S_K)$。于是
$$
\boxed{
\|\Gamma\|_\infty\le\|\Gamma\|_{\mathcal A}
\le \|H_NS_K\|_{\mathcal A}
+\frac{\varepsilon_H}{(1-w)^2}
+\|H_N\|_{\mathcal A}T_K.
}
\tag{12}
$$
右侧全部为有限有理运算，且保留了 $H_NS_K$ 内实际系数的抵消。
如果过早用 $\|H_N\|/(1-w)^2$，本例会得到约 $3.72\cdot10^{-9}$ 的
粗界，无法判断原门；因此(12)中的有限卷积有实际作用。

## 4. 代入当前 warm 的完整有理计算

脚本 `scripts/78718-geometry-inlet-angular-bound-v1.py` 直接读取第一节
输入各 PP 分片的第一个区间常数系数，以 `Fraction.from_float` 取得准确
dyadic 数。各分片逐件核对保存的字节数与 SHA，按 state 范围装配入口；
没有通过浮点插值或 FFT 来生成这里的有理系数。

当前 profile 的 $a(0)=1$，chart 首值为1；$q$ 与 $w=8q_{\rm ref}$
按保存的 binary 值解释。取 $N=24,K=96$，所有多项式加乘、阶乘、
系数绝对值求和及(8)–(12)均用有理数运算。

真实 **abc1a7 自然 exit0**，约3.205秒，给
$$
\|H_N\|_{\mathcal A}\simeq1.4882414699675756\cdot10^{-10},
$$
而(12)的显式两项尾总和约为
$3.0197592227664315\cdot10^{-17}$。完整右侧约为
$1.3024377823400951\cdot10^{-9}$。

这几个近似数仅帮助读者看量级；严格输出是把(12)的准确有理数向上取
$10^{-18}$ 网格，得到整数1302437783，故准确不等式(1)成立。
脚本同时直接比较未取整有理界与 $1/500000000$，结果为真。

报告
`notes/2026-11-10-78718-geometry-m15-warm-inlet-angular-bound-v1.json`，18842 B，SHA256
`124e239d0301a2db2c3f2d862c9b80bd596fc37601e22b59789d3b045a92383a`，
保存输入身份、脚本身份、两个截断阶数、各准确分数及向上整数网格值。
程序为零 BVP、零 tail、零流积分，未写回输入。

## 5. 适用范围及实际用途

现在能严格说，这一 M15 warm 的完整入口圆周已在原 $2\cdot10^{-9}$
角向误差门内，不只是两个轴点或一组 FFT 样点。它来自另一组15项 support
参数，不能用固定旧 M14 core 的静态 M15 重投影误差否决它。

这里没有证明原 warm 满足径向/混合 metric、实际非线性尾或全域接合，
也没有把它标为已解；启动后的 M15 真联解若改变参数，须对其实际输出
计算自己的指标。式(12)作为直接有限代数公式可以用于新的入口，无需
复制本对象的数值。原始 PP 的跨节点 $C^2$ 问题与此入口结论无关。

