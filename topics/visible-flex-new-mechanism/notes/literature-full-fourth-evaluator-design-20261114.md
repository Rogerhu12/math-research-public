# 真实完整第四阶函数的数值接口：三角历史、全局 profile 与未投影缺陷

日期：2026-11-14。源码与精确积分结构说明。尚未执行本接口的真实 profile/几何积分；研究执行入口只允许本公开仓库 Actions。

## 1. 输入身份与实际输出

两个新脚本为

- `scripts/literature_range_numeric_engine.py`：有理系数 DAG 的 long double 解释器和三角积分；
- `scripts/literature_full_fourth_evaluate.py`：冻结新 R45 单 P、冻结 R52 profile，再评价完整四块的函数。

入口强制一个 `R45-single-P-instance-v1` 文件和其 SHA256，核对其中控制定义的身份 hash，拒绝旧 Klein 八块 schema。还要求产生输入的 single-P 源码与底层 control 源码 SHA 分别等于本次实际导入模块，输出四个被导入源文件的 hash。真实框架/位置残差会从输入摘要一并带入输出。这里不是把数值近零 P 当成准确 R45 曲线。

固定目标是 $g_X+\epsilon^2(dY_f)^2$。本脚本不选择一个非零 epsilon，更不把形式第四阶系数的大小冒充课题要求的最终度量误差。

输出直接包含：

1. 三个独立第四谐波的**整个 period 函数的数值 L2 与采样最大值**，其余由共轭给出；
2. 同时实际计算的单 P period，以及完整四块减四倍单 P 的函数差；
3. 完整四块逐 ruling 函数到同一个全局三维 w 空间的数值商残差；
4. 三复总矩、B/U/V 的真实段末函数及原始低阶 ruling 缺陷；
5. 准确种子相位的 period/ruling 组合应为零的数值消差诊断。

没有把非零低阶函数投影掉，没有把单个正奇异值当作无限维独立性证明。有限网格的近零仍只作数值证据。

## 2. 732 个真实历史的严格三角结构

公开 Actions 43615655870 的准确编译产生 27 个 B 历史、318 个 U 历史、387 个 V 历史。重新编译后，本接口逐 DAG 节点检查以下结构，而不只依赖计数：

$$b_s=F(s),\qquad c_s=G(s)+A(s)b,$$

其中 b 为前 27 个实历史，c 为后 705 个。第二 RHS 只含真实 h、k、omega 及其导数；第三 RHS 对 b 仿射，不含自身 c。

把 b 赋权 1、c 赋权 2，则每个第四 period/ruling 系数至多权 2。节点不含任何历史变量分母。这个性质来自二次 forcing 的真实分层：第二场对 b 线性，第三 forcing 对第二场线性，第四 forcing 只含第二场平方或第一与第三场的双线性积。

系数解释器只处理实数。q 与 bar q 的复值均留在固定 profile 函数端；共同几何/历史系数保持一致。一个很小的人工 DAG toy 已核 C 接口，包括有理系数、h 的负整数幂、合成状态和加乘；没有在本地运行完整目标。

## 3. 真实 ramp 的分层 Gauss 原函数

令 t_i、w_i 为 [0,1] 上 n 点 Gauss 节点、权重，ell_j 为其基数多项式，

$$Q_{ij}=\int_0^{t_i}\ell_j(t)\,dt.$$

Q 用 Legendre 基的准确积分公式组装，不用单项式 Vandermonde 逆。对一个真实长度 Delta 的 segment，顺次计算

$$b_i=b_{\rm in}+\Delta\sum_jQ_{ij}F_j,$$

$$c_i=c_{\rm in}+\Delta\sum_jQ_{ij}\{G_j+A_jb_j\},$$

再在这同一批真实历史节点上评价全部第四系数，沿 Gauss 权重积分。段末值用相应权重求出并完整传给下一段。

这是三角初值积分，没有迭代一个非线性 collocation 方程，也没有按段或按 P 清零 primitive。全四块都实际传播，浮点 P 的二阶 period 缺陷会影响之后的第三、第四数据，恰应保留。

几何使用冻结 ramp 的同一个平坦 S、k 和 $h=1/(2b)$，通过显式链式求到 h、k 的三阶导数。omega 由同一个三次原函数和自然携带偏移得到；高阶 omega 导数继续由编译器的 $\omega_s=k_s/(2h)$ 关系产生。

## 4. 任意长常段只需三个节点

在真实常 k、h、omega 段，F、G、A 都为常系数，所以 b 是 s 的一次多项式，c 是二次多项式。第四 period/ruling 系数因权次数界至多为 s 的二次多项式。

因此三个 Gauss 节点在精确算术下：

- 准确恢复该段 b、c 节点与末值；
- 准确积分第四 period；
- 准确积分第四 ruling 的模平方及其到常 w 空间的平方残差，后两者次数至多 4。

这包括每个 N 次完整圈的整段，不随 N 逐圈积分。几何旋转框架已在点积和协变导数中准确消去；没有忽略一个仍须积分的快速旋转因子。真实 frame/位置闭合另由输入实例的验证处理。

小型人工 ODE $b'=2,c'=3+5b$ 和二次观测量已检验三角积分与多项式公式。它不是一次真实几何试算。

## 5. 首次 profile 是 R52，未冒称 R53

初次定义为 R52 的偶四模空间

$$\eta(x)\operatorname{span}\{1,x^2,x^4,x^6\},\qquad
\eta=e^{-1/(1-x^2)}\quad(|x|<1).$$

仅在预设 256 点积分上建立两个真实二次型、取广义特征向量并形成三矩圆的数值 f、g。随后冻结这组多项式系数，绝不在验证档重新求谱或配平。

八个 packet 的中心为 $10j$，幅度按签名整数 $(-1)^j\binom7j$ 的**实立方根**定义，使用 long double 评价。全局共同平移缩放放在物理 xi 区间内部，保留两侧开放 collar；共同归一幅度也只选一次。f、g 的整个内区支撑重叠，未换回旧不交平面。

这不是 R53 已由隐函数定理支付一个常状态最高门的那个修正族；输出明确 `R53_fourth_leading_gate_claimed=false`。本轮目的是真正完整函数、低阶缺陷和尺度诊断，然后才据结果在同一完整目标上设计 profile。

## 6. profile 原函数覆盖全部 gap 与 collar

固定活动区间分为 17 个面板：8 个 bump 区间、7 个中间 gap、2 个外 collar。每个验证档在所有面板采用同一节点数。

每个 `int_right` 生成元都从全局右端向左累计，面板内由同一 Gauss 原函数矩阵评价；进入 gap 或下一个 packet 时保留真实累计值。没有假定第三、第四字段逐 packet 局部化。bar q 的 jet 和原函数由共同实积分的复共轭得到。

q 的四阶导数直接来自光滑 bump 与已冻结多项式的 Leibniz 公式；不会对采样数据四次数值差分。验证重新评价同一 q，未重新拟合 profile。

## 7. 整体函数及同一个全局 w 商空间

完整 period 表示为 $\sum_a\mu_a\psi_a(\xi)$。程序保留原表达式实际依赖，将真实积分系数和真实 profile 原函数相乘后评价整个函数，不要求每个冗余生成元系数各自为零。

第四 ruling 在所有四块的真实 s 节点上评价。只解一个全局三维最小二乘问题

$$\min_v\int_0^L|K(s)-w(s)\cdot v|^2ds,$$

不按段独立拟合 v。报告全局 Gram 奇异值、残差 L2 和采样最大值；最小二乘相对截断值固定为 $10^{-13}$，并报告数值 rank。该数值 rank 不认证真实函数空间的准确维数；截秩也不是一个已证明的无限维正交投影。这个诊断不修改周期缺陷或任何已生成场。

由于近似输入不是准确零算子，full period 与四倍单 P 的差也真实计算。R58 的准确约简没有被强加给数值数据。

报告的表示 L1 majorant 只是冗余表达式的数值尺度，不能据“相对于这个可能很大的上界很小”接受 range；原始 L2、最大值、低阶缺陷和固定参数加密结果必须一同解释。

## 8. 资源与公开执行

默认两档为几何节点 32/64、profile 每面板节点 64/96；profile 谱只在 256 点准备一次。三角 evaluator 只执行所需节点的 DAG 前驱闭包。数值 coefficient buffer 使用 long double；profile atoms 使用 clongdouble，并通过共轭复用约一半原函数积分。

profile 原子表在两档约为 221/332 MB。另有最多 512 项的 profile 单项式缓存，防止缓存所有展开项；几何最高档 coefficient buffer 约 274 MB。大中间表仅在 Actions 进程内，摘要限制 1 MB。输出记录实际原子字节、精度和全部源 hash。

新 P 已由公开 Actions 43617085278 产生，127033 字节文件的实际 SHA256 为
`feb72a8e01f9a2aa0a925f7173e0bb53e1d81224481ad3a01afbeea4c6f2d6c0`，控制身份为
`79501ce96f224138311a43c49b2b3a29865d9f660c67b22124f9d2c1fb57d04f`。
它的三档单 P 矩阵范数约为 $5.25$–$5.29\cdot10^{-10}$，自然全四块位置残差从 $3.03\cdot10^{-9}$ 变为 $5.57\cdot10^{-7}$，没有据此认证准确闭合。以下是完整第四接口的具体新输入，不是旧 Klein 实例。

```sh
python topics/visible-flex-new-mechanism/scripts/literature_full_fourth_evaluate.py \
  --geometry topics/visible-flex-new-mechanism/notes/actions-43617085278-1-single_P_instance/single-P-frozen-instance.json \
  --geometry-sha256 feb72a8e01f9a2aa0a925f7173e0bb53e1d81224481ad3a01afbeea4c6f2d6c0 \
  --geometry-nodes 32 64 --profile-nodes 64 96 --profile-fit-n 256 \
  --max-seconds 1200 --progress --out topics/visible-flex-new-mechanism/notes/full-fourth-function-evaluation.json
```

若预算或数值条件导致中断，输出 `incomplete` 及已经完成的验证档；不把预算耗尽解释为数学障碍，也不改变用户任务状态。本接口仍未构造第四阶准确解、有限连续族、闭面嵌入或宏观 reach。
