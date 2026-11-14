# 完整函数纯模式的准确代数入口：互反 bulk 与可达第三交换子

状态：**实现说明与待执行的准确代数实验**。本文件不报告实验已通过，不把右原函数的自由表达式基当作函数独立基。源码为 [literature_pure_bulk_exact_membership.py](../scripts/literature_pure_bulk_exact_membership.py)。

## 1. 本次要回答的确定问题

R71 已给真实第三整体响应控制以及纯模式的完整 $P_1$ 公式。本次只测试其中一个明确的函数身份：

$$
\frac{\mathcal P_{\mathrm{reciprocal}}[q]}{16}
+\sum_{i<j}c_{ij}\mathcal H_A\bigl([\Phi_i,\Phi_j]\bigr)[q]=0,
\qquad
\mathcal H_A(\tau)=\frac{D\tau(q)[A(q,q)]-2A(q,\tau(q))}{8}.
$$

这里 $q$ 是同一紧区间 $I\Subset(1,\infty)$ 上任意光滑复 profile，在共同右 collar 恒零；所有乘积是普通复双线性乘积。$\Phi_i$ 是 R69/R71 的八个真实矩阵方向，$[\Phi_i,\Phi_j](q)=\Phi_i(q,\Phi_j(q,q))-\Phi_j(q,\Phi_i(q,q))$。$A$ 为 $h=1,k=+1,\omega=+1$ 常态的二次算子，不含常段时长。正负两个常段的实际时长相同，已从整个等式除去。

若找到有理数 $c_{ij}$ 且从原始表达式复核成功，所需名义总参数为 $c_{ij}/2$。R71 的光滑 loop 族首先只在一个固定小参数区间成立；选充分大的有限整数 $m$，串接 $m$ 条参数 $t=c_{ij}/(2m)$ 的小 loop。因各 loop 的 $M=0$，第三响应准确相加，故任意有限 $c_{ij}$ 均可这样实现。在有界的系数邻域上预先固定同一个 $m$，连续控制族也保留。输出只记录 nominal_total_loop_parameter，不假称单条大参数已落在局部族内。这提供同一整函数层面的可达补偿方向。它**尚未加入真实不同 scalar 端口桥的基准 $T_B$**，也不支付其他 Fourier 模式、$P_0$、第四 ruling 或有限等距族。阴性输出更不排除固定 profile、其他第三可达空间，或尚未被本次正规化识别的函数恒等式。

## 2. 目标直接从真实恢复公式生成

依赖源码是 R56 的 literature_range_profile_algebra.py，绑定 git blob：

01c7424af3a96f2c2a0f0cb0c782b2037ff3ec74。

入口实际重算该文件的 git blob SHA-1 并核对，同时在回执记录 SHA-256。依赖变化须先审阅、明确更新绑定。

两个 constant compiler 共用同一个 profile/原函数代数，分别置

$$
(h,k,\omega)=(1,1,1),\qquad (1,-1,-1).
$$

故共享 $x=\xi=e$，而真实分母为 $z_+=x+1$、$z_-=x-1$；没有混用两者的物理 $u$ 导数。两状态依次编译

$$
B=\mathcal I H(Y_q,Y_q),\quad
U=\mathcal I H(Y_q,B),\quad
-\frac1{16}H(B,B)-\frac14H(Y_q,U).
$$

**先保留所有实际 history RHS 完成协变导数和恢复，再把入段二、三阶 history 的值置零**。这样 history 的导数仍留下正确局部 drift；不是在微分前删除 history，也没有把向量恢复的 mixed 项丢掉。两态 period_rhs 相加就是待测纯模式局部目标。它不运行几何 ODE，不取任何 profile 的数值。

## 3. 八个二次算子与正确原函数符号

矩阵方向采用 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$，且 $t_0=p_0/4+s_1/2$。令

$$
\begin{aligned}
A_0&=-p_1/2-p_2x,&A_1&=p_0+p_1x+p_2x^2,\\
A_2&=r_1+(s_1-p_0/2)x+(t_1-p_1/2)x^2-p_2x^3/2,\\
B_0&=r_0+r_1x-p_0x^2/4,\\
B_1&=s_0+s_1x-p_1x^2/4,\\
B_2&=t_0+t_1x-p_2x^2/4.
\end{aligned}
$$

$\Phi(f,g)=A_0fg+A_1(fg'+f'g)/2+A_2f'g'+B_0J_0+B_1J_1+B_2J_2^*$，其中

$$
J_0=\int_x^r f''g'',\qquad
J_1=\int_x^r \eta f''g'',\qquad
J_2^*=\int_x^r(\eta^2f''g''+2f'g').
$$

代码继承 R56 的有符号原函数 $I(F)=\int_r^xF$，所以所有 $J=-I$。它绝不设置左尾为零。

正 constant 算子是

$$
A=-\Phi_{p_0}/2-\Phi_{p_2}/2-\Phi_{r_0}/8,
$$

即 $A(q,q)=xq^2/2-(1+x^2)qq'/2+x(1+x^2)(q')^2/4+(x^2-1)J/8$，$J=\int_x^r((1+\eta^2)(q'')^2+2(q')^2)$。

## 4. 有效但不完备的 right-IBP

所有改写只使用

$$
I(D F)=F
$$

且每个 $F$ 具有正 profile 次数，因此在共同右 collar 恒零。不会把有非零右端值的常数或纯 $x$ 多项式套入此式。没有隐藏的左端或总矩假设。

实现的有限规则包括：唯一最高 jet 的分部积分；同一原函数的幂 shuffle；两个第一层右原函数的固定次序 shuffle。遇到无法识别或循环的表达式就原样保留。循环回退是准确 no-op，不是设零。于是每次输出都与原始函数相等，但所有真实函数关系未必都已识别。

先在重写后的自由表达式向量上做准确有理数消元。若出现候选关系，另起正规化器，从**未正规化的 R56 目标以及未正规化的原始二次交换子**重新构造完整残差并验证为零。只有这个原式复核也成功，才设置 verified_whole_function_identity=true。

rewritten_representative_rank 只是当前表达式代表的秩；不是实际函数独立性的证书。若余项不为零，结果仅为本次没有产生已复核的身份，不输出普遍不存在结论。

## 5. 小型准确检查与独立参照

--toy-only 不编译完整目标，只检查：

- 有符号右原函数求导；
- $I(qq')=q^2/2$ 与一次 jet 分部积分；
- 右原函数平方 shuffle；
- $P=\Phi_{r_0},Q=\Phi_{r_1}$ 的交换子
  $[P,Q](q)=I((q'')^3)/3=-\int_x^r(q'')^3/3$；
- 常态 $A$ 与独立公式一致；
- 该最简交换子的响应与 source 代理独立纸推、独立 BigInt formal-jet 核过的完整函数式一致。

独立参照的三项检查只通过准确导数身份与右 collar 决定原函数常数；不包含 profile 积分。该独立 MJS 源和回执另存，不能把它当成 28 方向 membership 已通过。

本稿及 producer 尚未在本机执行 Python 外壳；第一步由本公开仓库 Actions 执行 --toy-only。所有完整目标编译亦只在该仓库 Actions。

## 6. CLI、预算与失败回执

建议 lane 名 p1_bulk_exact，先运行：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_exact_membership.py --toy-only --out output/p1-bulk-exact-toy.json
~~~

toy 成功后再运行：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_exact_membership.py --max-seconds 240 --max-coefficient-nodes 500000 --max-profile-atoms 60000 --max-terms 80000 --max-IBP-calls 250000 --max-memory-mib 2048 --max-rational-bits 8192 --out output/p1-bulk-exact-membership.json
~~~

实际目标同时检查 GITHUB_ACTIONS=true 与 GITHUB_REPOSITORY=Rogerhu12/math-research-public。默认限制为 240 秒研究编译、50 万 coefficient DAG 节点、6 万 profile atoms、每表达式 8 万项、25 万 IBP primitive 调用、Linux RSS 轮询阈值 2 GiB（含继承 compiler 的检查点，并非操作系统硬内存限制）、仅线性消元有理数 8192 bit。toy 有独立较小预算；不存在自动扩大预算或重复研究计算。

输出为单个小 JSON，硬上限 95 KB，通常只需十几 KB。包括源与依赖哈希、GitHub 身份、阶段、实际规模、各方向表达式哈希、右 IBP 次数、秩与残差、以及阳性时可复核的全部有理系数。预算耗尽写 resource_budget_exceeded，保留已完成的阶段信息并 exit 2；实现检查失败写明确错误并 exit 1。这些退出都不作数学阴性结论。

研究范围仍是高阶算子机制。没有新几何参数拟合、没有虚构准确嵌入，没有为已被厚度门排除的旧长圈几何增加合格声明。
