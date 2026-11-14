# R133 补篇：完整 regular 边界、两条均值和全部试解跳的实际消费

2026-11-14。**已证明并已实际完成本文的独立端点和接口预算。**
体内响应/伴随残差、完整连续逆以及真正参数 Schur 的非零性不由本篇推出。

## 1. 同一实际对象与两条真正均值

本篇使用原完整 ac1 中心、原准确 $\alpha,\nu$ 和
$\eta=\eta_0+\delta\eta$、$|\delta\eta|\le10^{-9}$。
响应为物理、未按 $\alpha$ 缩放的 moving 变分，约定
$Dq_\nu=+F_\nu$；全部外 regular 行包含物理第四模。
伴随采用真实圈上 $L^2$ Gram：mean 权1，非零 sine/cosine 幅度权 $1/2$。
原始全响应、全伴随 Hermite 数据及其全部单侧导数保持不变。

为明确本文不靠尚未完成的体残差，写

$$
q=(w_1,w_2+z),\qquad \psi=(\lambda_1,\lambda_2+\mu),
\qquad \langle w_2\rangle=\langle\lambda_2\rangle=0.
\tag{B.1}
$$

定义 $D=\partial_r-A$、$c_m=\langle(Ae_2)_2\rangle$。
原完整均值 Green 定理准确给出

$$
z'=c_mz+\langle F_{\nu,2}\rangle-B[w],\qquad
\mu'=-c_m\mu-g[\lambda].
\tag{B.2}
$$

响应的右 mean 是真实 nonlinear regular 行，伴随的左 mean 是完整
物理腰幅泛函的 mean 列，均不设为零。系数、正向伴随、反向响应三个数组
各含7721个真实闭区间，覆盖完整 $[0,25/8]$，保持所有原目标尾和接缝。
标量积分已在原 v2 作业中全部完成；该作业随后在第一条体残差的
`Finite / int` 调用失败。因此它原样保持 `complete=false` 与实际异常。

新 adapter 仅消费上述三个已经算完的数组。它核完整 cover、真实 germ、
正反方向、候选/参数/源和准确旧容器 SHA；不导入任何未算的体残差。
标量存在、唯一性和区间积分只依赖(B.2)，不依赖后面的体残差程序能否运行。
因此两端 $z,\mu$ 的已算包络可以独立用于真正边界。其身份与证明依据见
[均值回填](R133-supplement-mean-completed-head-and-adjoint-body-consumer.md)。

## 2. 全物理角微分与无限尾

在任一端点记 $m=\langle v\rangle$，
$\theta=\varphi+I(v-m)/m$，$I$ 是零 mean 原函数。对完整变分
$h=(h_1,h_2)$，$z=\langle h_2\rangle$，有

$$
\delta\theta={I(h_2-zv/m)\over m},\quad
C_k={\langle e^{-ik\theta}\rangle\over m},\quad
B_k={\langle u e^{-ik\theta}\rangle\over m},
\tag{B.3}
$$

$$
\delta C_k=-{z\over m}C_k-{ik\over m}
 \langle e^{-ik\theta}\delta\theta\rangle,
\quad
\delta B_k=-{z\over m}B_k+{1\over m}
 \langle e^{-ik\theta}(h_1-iku\delta\theta)\rangle.
\tag{B.4}
$$

这直接计算物理 Fourier 矩，未将 moving 有限头冒作物理有限头。
256个保留物理正模使用完整 Laurent 指数级数及其严格余项；更高的全部模
用已付解析域的轮廓界求和。有限模两符号的 $L^2$ 权是2，
$H^s$ 平方权是 $(1+k^2)^s$。mean 另按真实(B.2)计算。
真 $q_m$ 与提案 $q_m$ 的差、完整 nonlinear DN 导数、独立的外背景
$f_B$ 类均保留；本次响应列的方向为 $\delta f_B=0$，并未将背景 $f_B$ 清零。

真实边界的转置及其圈上权完全采用
[完整物理转置](R133-supplement-complete-physical-boundary-transpose-and-Schur-pairing.md)。
特别，外 mean 乘子和原物理第四乘子都保留。反射类给 $B$ mean 恰为零，
这是对称恒等式，不是删去偶 mean 方程。

## 3. 全部径向跳和有符号恒等式

两条显式非零试解各有6143个真实 PPoly 接口。每一跳用准确 dyadic 系数
和准确节点位移作有理 Horner 运算。回填的 $z,\mu$ 是同一个全局标量解，
故它们在接口连续。完整跳配对是

$$
J_q=\sum_i\langle\psi(r_i^+),q(r_i^+)-q(r_i^-)\rangle,
\quad
J_\psi=\sum_i\langle\psi(r_i^+)-\psi(r_i^-),q(r_i^-)\rangle.
\tag{B.5}
$$

代码逐个保存准确有理值；两种单侧约定不能互换或省略其中一项。
若 $T_R$ 是已固定符号的负外 regular 配对，$T_0$ 是腰 Dirichlet 配对，
本篇直接计算的是

$$
S_{\rm end}=\ell_{\rm amp}(q)+T_R-T_0-J_q.
\tag{B.6}
$$

完整双残差公式中的修正量仍为

$$
S_0=S_{\rm end}-\int_0^R\langle\psi,Dq-F_\nu\rangle\,dr.
\tag{B.7}
$$

本篇不把该尚未合并的积分设为零，也不把 $S_{\rm end}$ 称为 $S_0$。
从 $S_0$ 到真正 Schur 还须付伴随残差、响应残差与完整连续逆的乘积费，
见[完整有符号参数公式](R133-supplement-actual-signed-nu-pairing-and-all-product-jumps.md)。

## 4. 实际完整结果

v5 独立消费者正常返回0，12.006828秒，最大 RSS399992 KiB。
完整256物理矩、两个端点和两组6143个准确接口均已消费；没有重复求解
响应或伴随。主要严格界如下。

| 完整量 | 严格上界或包络 |
|---|---:|
| 外背景 $Z$ 的全部物理 $A^0$ | $2.5329850\,10^{-13}$ |
| 响应外 $\delta Z$，$L^2$ | $2.465198\,10^{-12}$ |
| 同量，$H^{1/6}$ | $3.121686\,10^{-12}$ |
| 同量，$H^1$ | $1.016428\,10^{-11}$ |
| 全部真实 regular Robin，$L^2$ | $1.454039\,10^{-17}$ |
| 同量，$H^{1/6}$ | $3.465074\,10^{-17}$ |
| 同量，$H^1$ | $2.541068\,10^{-15}$ |
| 腰 Dirichlet 原始残差，$L^2$ | $8.922944\,10^{-16}$ |
| 腰非零完整转置残差，$L^2$ | $2.733977\,10^{-8}$ |
| 真外非零完整转置残差，$L^2$ | $3.049647\,10^{-16}$ |
| 真外 mean 伴随乘子绝对值 | $1.378684\,10^{-8}$ |
| 保留物理第四 Robin 残差 | $[-2.056322,2.056322]\,10^{-17}$ |
| $S_{\rm end}$ | $[8.167929616818,\ 8.194927720677]$ |

背景真 $Z<10^{-12}$ 已进入所消费的完整 nonlinear DN 导数域。
响应真正 mean 行准确满足(B.2)的末端条件。
表中腰幅区间的宽度保留了真实均值积分的区间费用，没有偷用有限提案的
单个 $8.181474\ldots$ 数字替代。

## 5. 实际失败、修复和完整存储

v3 原生过程正常记录退出1：接近零的 Arb 绝对值球先平方再开方可能含一个
负的区间下端，形成非有限数；JSON 明确拒绝该输出。v4 将 Laurent 范数改为
$\sqrt{\sum |c_j|_{\rm upper}^2}$，完成全部数学行后，在最后物理矩汇总的
同类写法再次拒绝非有限数，保持实际失败报告。

v5 在最后两组正平方和也使用准确非负的上端点平方。它明确验证 v4 的原
kind/source/全部输入和完整行数，复用已完成的同一行，随后实际完成汇总。
这不是把原失败标志改为成功。原 v4 的完整容器可由 v5 中逐字相同的四组行
及轻量旧模板恢复；实际复原已与原 gzip 字节完全相同。

原 v2 的三个完整均值数组只存一次，按原 gzip 容器的直接二进制段无损压缩；
全部原失败信息和 SHA 保留，单件不超过5MB。旧粗体残差 v3 另保523行断点，
在已确认区间相关性损失后主动停止；该宽上界不是一个数学不可能性证明。
下一消费者须在同一径向多项式中直接消去 $q'-Aq$，并单独推进 mean 误差。
本文既不需要等待该实现，也不把它尚未完成的范围归入本篇结论。
