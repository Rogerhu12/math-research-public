# p47：完整原 p-local cuspidal 标签的有限计算

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

## 新输入与准确范围

本请求消费 R1062、R1069、R1070 和 R1071 的原来源。
它计算完整原曲线 $X_{\rm ns}^+(47)$ 的全部 $\mathbf Q_{47}$ smooth
圆盘的 cuspidal Kummer 标签及完整向量的碰撞，不作有理点分类。

这不是 R1054 的条件 $K_{15}$ 检查，也不是 R1057 的原最低泛函、
指定 CM 正赋值深盘结果；不读取或重新计算它们。
R707 的固定 $p=41$ 全盘结果及已登记 scalar 窗口也不重开。

固定 $p=47$、同一 $\mathbf F_{p^2}=\mathbf F_p(s)$、$s^2=5$，
以及原 smoothing integer $c=5$。
程序核 $5$ 的 primitive 性，而不任意逐点改变 Cartan norm 标记。

## 实际角色和唯一全局坐标

对每个偶数 $2\le R\le44$，取 $\chi=\omega^R$、$\psi=\chi^{-1}$。
使用 R1062 的真实特征值
$$
S_\psi=-J(\psi,\eta)B_{2,\psi^2}/4.
$$
模 $p$ 非零的 $S_\psi$ 不属于实际 $V$。
Jacobi 因子模 $p$ 为零、广义 Bernoulli 整时则属于实际 $V$。
对其余角色直接读模 $p$ 的广义 Bernoulli，保留全部可能额外角色。

具体以 $a^p\bmod p^2$ 取真实 Teichmuller lift，读取
$$
B_{2,\psi^2}\equiv
\frac{\sum a^2\widetilde a^{-2R}}p-\sum a^{1-2R}\pmod p.
$$
在 $R=24$ 处第一分子不被 $p$ 整除，不能先模 $p$ 再除 $p$；
该 pole 角色按 R1070 的已付原消去单独处理。
程序同时完整计算所需普通 $B_R\bmod p$。
只有实际角色全部 Bernoulli-good 才报告全 $V$ 的唯一 global 向量；
不预先假设 $47$ regular。

取同一个 circular unit $\eta_5$，其原角色基的系数是
$$
b_\chi=
\frac{B_R(5^R-1)}{R\,R!}\gamma^R.
$$
每个模型的 $\gamma$ 必须由原 Weil pairing 计算；
不将它归一为一，不只检查其 $(p-1)$ 次幂。

## 原 first lift、有限系数与真实相位

逐个枚举 $\mathbf F_{47}$ 上 supersingular $j$，以原 Hasse coefficient
判定并以实际点计数核 trace zero。
一般 $j$ 取 $A=3j/(1728-j)$、$B=2j/(1728-j)$；
$j=0$ 取 $(A,B)=(0,1)$；$j=1728$ 同时取 $(1,0)$ 和 $(5,0)$。

每一模型先取同一整数系数的 marked first lift 模 $p^2$。
R1071 §§11–12 支付实际 CM reference 与该 first lift 的关系。
置 $q=z^2$、$w=qx$，先在模 $p^2$ 解
$$
w^3-w^2+Aq^2w+Bq^3=0,\quad w(0)=1,
$$
然后由
$$
L(z)=zU(q),\qquad
U_n=\frac{[q^n](1-qw'/w)}{2n+1}
$$
读取原 eigen-$T$ 的有限数据。$p\mid 2n+1$ 时保留模 $p^2$ 后除 $p$，
不做不合法的 characteristic-$p$ 除法。
最高 log 次数是 $2113<p^2$；完整原 Weierstrass 方程和 differential
恒等式逐系数核验。

原 $\psi_5$ 用 R1071 (1071.41)，归一化
$V(q)=q^{12}\psi_5(w/q)/5$、$H=-24+2qV'/V$。
所有所需
$$
A_d=[q^{d/2}]H(q)U(q)^{-d}
$$
保留同一个原 differential、source 和 smoothing。
特别分别核低 $A_4,A_6$，并核每个用到的 $A_{pd}=A_d$。
不把任意 finite polynomial 的系数当作该原函数。

原 source 选 $u_*=[T^p][p](T)$，令 $t_*=u_*/p$。
R1071 已证明在同一实际 branch 上 $\beta_0=1$、$\lambda=-1$。
每个角色的完整坐标为
$$
c_{\chi,s}(t_*)=\frac1{2\kappa_\chi b_\chi}
\left(\frac{A_N}N+
\sum_{i=1}^{\min(R,p-R)}
 (-1)^i A_{N-(p-1)i}\frac{\binom{N-(p-1)i-1}{i-1}}i t_*^i
\right).
$$
被 Lucas 消去的其余项另核二项式为零，没有读取或猜测其 $A_d$。

为计算真实 $\gamma$，只将 $L$ 反演至 $p+2=49$ 次；
用实际 Laurent coordinates 在 $\mathbf F_{p^2}[[h]]/(h^{49})$
执行 normalized Miller unit products。
非竖直 line 为 $-y+y_A+\lambda(x-x_A)$，竖直 line 为 $x-x_A$，
最终 $[p]P=O$ 直接用竖直支路，最后取
$$
(-1)^p f_{p,P}(Q)/f_{p,Q}(P).
$$
原 curve equation、所有低于 $h^{48}$ 的消失、
$\gamma\ne0$、$\gamma^{46}=-1$ 和
$\gamma(P,2Q)=2\gamma(P,Q)$ 都核准。
这是同一实际相位的完整有限计算，不以根号或离散编号代替。

另有一个独立纸面校验，仍是本次新的原 cuspidal 输入：
对 $y^2=x^3+1$，原
$x(T)=T^{-2}+\sum c_nT^{6n-2}$ 的 ODE
$x''=6x^2$ 给
$c_1=-1/7$、$c_n=\sum_{a+b=n}c_ac_b/((n-1)(6n+1))$。
纸面递推得到 $c_7=39$，因此原 $A_{42}=31\bmod47$；
程序用 division-polynomial/residue 的独立路径核这个值。
它不计算旧 $f_N$、$g_N$ 或最低泛函。

## 全部原 coarse 圆盘

一般 $j$ 的 $t_*\in\mathbf F_p$ 全部保留。
$j=0$ 的 $\mu_3$ 只留 $t_*^3$，而 cube map 在本例为双射；
程序逐角色核自动同构要求的零系数。
$j=1728$ 两个 quartic twists 必须一起用，
各按 $t_*\sim-t_*$ 商，两个 $t_*=0$ 只计一次。
真实相位对齐后两个中心向量必须相等；
每个 supersingular $j$ 因而恰覆盖 $p$ 个原 coarse 圆盘。

程序只报告完整 global 向量的碰撞数量、纤维重数及哈希。
就算向量互异，也仅得到这些原圆盘的区分，
不将它提升为每盘有理点唯一性或全部 Serre 结论。
有效辅助素的同点标签筛选是下一独立消费。

## 执行、预算和保存

数学只在本公开仓库 GitHub Actions 执行。
consumer 在导入 FLINT 前检查真实 Actions 环境、仓库、
请求 SHA-256、源码及两 README 的 SHA-256；source commit 与
GITHUB_SHA 一致。依赖固定为 python-flint 0.9.0。

只用一个 job，数学总预算 600 秒，预留 30 秒收尾；
workflow 的 15 分钟只作为安装/调度外限。
若超时或任何断言失败，输出准确完成模型数量和失败回执，
不从失败推出数学负结论。

全部可重算 coefficients、vectors 和碰撞类只在 runner 临时目录。
不上传 artifact/Release，不把原数组或大报告提交进仓库。
仅在 stdout 保留紧凑方法回执、模型数、角色、degree、纤维重数、
来源/run/attempt、SHA-256 和预算。
后继结论引用真实 run/job/source 和这些哈希。
