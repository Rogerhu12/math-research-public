# R647 正密度因子的实际有限输入范围

2026-11-28。本范围使用 [R647](../results/R647-positive-liouville-gauge-finite-morse-profile.md) 新的准确有理谱 $(s,\eta^2,B_M)=(11/5,37/100,3/100)$，指定 $(j,N)=(2,3),(3,5)$ 两个径向激发核。它们不同于 R630 的旧核对。四个 profile 使用新证明的 $\sigma=Ae^{\eta X}+Be^{-\eta X}$ 自由度，保留这个新背景自己的同一个左正规 $\psi_1$、同一两核与完整 Morse 谱。源为 `scripts/r647_positive_liouville_finite_profile_20261128.py`。发布本文件时尚未执行，以下均是实际输入定义，不是结果。

## 明确输入

令 $u_R=\psi_1'(X_R)/\psi_1(X_R)$、$a_{\max}=\min(\eta,u_R)$，依次使用准确有理数 $\tau=0,1/2,4/5,19/20$，取

$$
a_R=-\eta+\tau(\eta+a_{\max}),\qquad \nu_R=u_R-a_R.
$$

R647 已证明这些有限参数的 $r_X>0$ 于整条实线，且给 $u+\eta\ge st+(\sqrt{37}-6)/10>0$ 的准确下界。两指定核分别有一、二个节点，全部在同一个负组件中且严格交错。全部 profile 使用 $r(X_R)=1$，$f_2(0)=f_3(0)=1$，负组件实际高度为 $1/2$；高度尺度 $\lambda$ 由该组件的真实积分确定。每支输出其全部精确参数定义、实际数值 $a_R,\nu_R,\lambda$、mode scales，以及 $X_L-1/4$、$X_R+1/4$ 两个真实 cut 上的完整 $\sigma,\sigma_X,\psi_1,\psi_{1,X},r,r_X,w,w_X,f_j,\partial_rf_j,K$ 数据，作为下一有限连接/非线性输入。该新有理谱还有其它整数零模；后续 R639 式统一修复必须实际支付，不能在数值输出中假定只剩两核。

对每支评价负组件和增加两侧固定 $1/4$ buffer 后的半径比、实际高度、两主曲率，以及线性高度 $h+q\Phi$ 的 $Q,D$ 余量。每区域为 512 个等距 $X$ 区间；coarse 仅读取同一已付点中的偶下标，没有另开一轮求值。曲率 extrema 和线性余量都只标为有限采样，没有连续曲率/reach 或非线性存在半径资格。

四条新支的参考 $\beta_0$ 在 $t\in[1/1048576,16]$ 上用 50 位普通 quadrature 评价，按两真实 cuts、两 type roots 和三个核节点拆成固定段。完整有限 buffer 核心的 $w^2$ 边界项按 R635 准确保留。无限遗漏尾尚不做球包围，真正平尾尚未接上；因此数值只作此 profile 自己的参考/核心数据，不借 R637 的严格区间。

$\tau=0$ 是本新有理核对的单指数密度，仍是一个新输入；它不是 R630/R637 的旧单指数参考，所以自己的端口同样从新两核实际计算。旧参考不在本范围中重跑。

## 科学运行和边界

使用已有非 stdin 公开 runner `run_inverse_rotational_metric_20261126.py`，先实 pull 并检查根/题 README 和私库根规则，再回 source commit 核对全部绑定。Python 3.12.14，mpmath 1.3.0，50 位；科学墙钟 240 秒、实际 reference 公式最多 100000 次；job 上限 15 分钟。源码另设公开 Actions/repository/run id guard。时间和实际 `hyperu`、reference、candidate、physical profile、quadrature callback、port 与采样余量调用分别由真实函数入口计数；共享 $\psi_1$ 缓存不重复记底层 special-function 调用。

日志只输出有限参数、标量 extrema、取得点、段积分和实际调用/时间，不存可重算大数组。不允许本地运行科学求值。

[R630 原实际结果](2026-11-28-r630-morse-port-actions.md)完整保留：run46121291838 的科学 5.675849416999995 秒、4160 次真实 `hyperu` 调用及四个原有限 Cauchy 分支的全部高度/截断数据均不删除、不重跑。该原分支改变了 $\psi_1$，本输入改变的是 $\sigma$，不会因二者都叫“小 $\nu$”而混用结论。[R637](../results/R637-certified-morse-port-and-true-flat-tail-transfer.md) 的球证和 22.998496100000004 秒费用同样保留。

本范围没有声称取得真平尾连接、有限非线性倾角、同一个 $g$ 的宏观族或 README 完成。实际输出之后必须据同一个新 profile 的低矮程度、曲率及端数据选择并完成下一连接，而不是继续只积累形式 $\beta$ 增益。
