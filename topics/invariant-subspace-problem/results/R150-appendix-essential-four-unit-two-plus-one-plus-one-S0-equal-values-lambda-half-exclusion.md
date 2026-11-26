# R150 附录：S=0、h=k、lambda=1/2 的原 mean 短证排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：已完整证明 $S=h+k+1-2\lambda=0,h=k,\lambda=1/2$ 分支没有原物理临界点。$t\ne0$ 由四个原多项式的短恒等式排除；$t=0$ 是确实存在的抽象必要族，必须补回原第五列，用同一物理配对的秩下界排除。没有把抽象族删成单位理想，也没有宣布另外两个 $2\lambda^2=1$ 的值碰撞已经解决。

## 1. 原值与原 Gram 的完整形式

沿用原单位 2+1+1 模型及其同一长度五物理除子 $2A+B+C+Z$。在已付的非零不同基点配对图，共同规范 $p=1$，保

$$
bcq(q-1)\ne0,\qquad P_0\ne0.
$$

由 $S=0,h=k,\lambda=1/2$ 得 $h=k=0$。前两个原 U 矩立即给

$$
w=0,\quad a=1/2,\quad b+c=1/2,\qquad
U=U_0(1,0,0,0),\quad U_0\ne0.
\tag{1}
$$

原孤立点第二梯度 $N(V)=0$，$V=U/U_0=(1,0,0,0)$，恰为

$$
4N(V)=A_1=0.
$$

记

$$
\delta=q-1,\quad \sigma=q+1,\quad
u=b+cq,\quad V_2=b+cq^2,\quad T_0=V_2-2u^2.
$$

原最高基值有精确因子身份

$$
2P_0=(\sigma-u)T_0.
\tag{2}
$$

因 $P_0\ne0$，T0 非零。由原 $E_0=0,N_0=P_0/2$ 的完整线性图，

$$
A_1=\frac{T_0}{q}(u-2f).
$$

所以原 $A_1=0$ 全局迫 $f=u/2$，没有另加分母零例外。原 r,s 随之为

$$
r=\frac{ct}{\delta},\qquad s_1=-\frac{bqt}{\delta}.
$$

因此每个本分支原点的活跃 Gram 都严格属于

$$
K=
\begin{pmatrix}
0&0&1&q\\
0&0&ct/\delta&-bqt/\delta\\
1&ct/\delta&0&t\\
q&-bqt/\delta&t&0
\end{pmatrix}.
\tag{3}
$$

这是同一个原 K 的必要表达，包含 t=0 和所有非零 t；没有独立改变其中的配对。

## 2. 非零 t 的四个原恒等式

为清掉唯一分母，用 $\widehat K=\delta K$ 计算。原 mean 乘 $\delta^2$，原最高 jet 乘 $\delta^3$；delta 非零。令 $\widehat E_1,\widehat E_B,\widehat E_C$ 表示这种缩放后的原 mean，令 $\widehat\Pi_1=2\delta^3P_1$ 为原最高一阶 jet。直接从原 Frobenius 乘法和原迹得到

$$
\widehat E_1
=bct\,[\delta^2(2u-\sigma)-qt],
\tag{4}
$$

$$
\widehat E_B
=ct\left[-2\delta^2(2c+bq)
+t(\delta^2+2b\delta-2cq^2)\right],
\tag{5}
$$

$$
\widehat E_C
=bt\left[-2\delta^2(c+2bq)
+t(\delta^2-2cq\delta-2b)\right].
\tag{6}
$$

设

$$
W=2(c+bq),\qquad
G=W^2+(q+1)W-q.
$$

由 $b+c=1/2$ 有 $2u-\sigma=-W$，且原最高 jet 精确为

$$
\widehat\Pi_1=-\frac32\delta^3bct\,G.
\tag{7}
$$

原要求 $P_1=3wP_0=0$；因 (1) 中 w=0，所以 (7) 必为零。

现在只在 $t\ne0$ 分支使用它为单位。由 (4)，

$$
t=-\frac{\delta^2W}{q}. \tag{8}
$$

把 (8) 代入 (5)、(6)，仅乘除已付的 b,c,q,delta,t，得到

$$
B_\ast=W^2(q^2+q-1)-2q^2W+q^2=0,
$$

$$
C_\ast=W^2(q^2-q-1)+2qW-q^2=0.
$$

这两式之差的原多项式身份是

$$
B_\ast-C_\ast
=2q\,[W^2-(q+1)W+q].
\tag{9}
$$

q 非零，而 (7) 给 G=0。将 G 与 (9) 的括号相加，得到 $2W^2=0$。于是 W=0，继而 G=0 给 q=0，矛盾。故所有非零 t 原点均已排除。

这是一组实际原式的完整点排除；没有从“没有公共曲线”推断没有孤立点，也没有需要再返回的数值根。

## 3. t=0 的真实抽象族及完整第五列

不能从 (4)–(7) 除 t 后忽略 t=0。当 t=0，(3) 确实退化成原抽象必要族

$$
A_1=r=s_1=t=0,\qquad f=u/2.
$$

必须使用 (1) 的原孤立点配对列补全 Gram。完整五列矩阵是

$$
G_{\mathrm{phys}}=
\begin{pmatrix}
0&0&1&q&U_0\\
0&0&0&0&0\\
1&0&0&0&0\\
q&0&0&0&0\\
U_0&0&0&0&0
\end{pmatrix}.
\tag{10}
$$

这里 U0 保留为原非零值，并未独立将其归一化。(10) 的秩恰为二：除第一行列外全零，而第一行第三列为 1。

沿用已经登记的同一物理接口：长度五除子 $2A+B+C+Z$ 的五个值/jet 列在原非退化六维空间中线性无关，包括无限远坐标图。令其张成空间为 Wphys，则

$$
\dim W_{\mathrm{phys}}=5,\qquad
\dim W_{\mathrm{phys}}^\perp=1.
$$

所以它的根空间维数至多一，限制 Gram 的秩至少为四。这与 (10) 的秩二矛盾。

该接口的完整既存例子见
[R150 零孤立点均值层排除，§6.1](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-base-highest-zero-isolated-mean-exclusion.md)；
此处只复用同一五列/六维物理事实，没有重做旧消元，也没有把四列活跃 Gram 秩二单独当作矛盾。这个几何排除不被改写为一个尚未构造的全局幂理想身份。

第 2、3 节覆盖全部 t，故本 lambda=1/2 碰撞完整关闭。

## 4. 精确小源码与实际执行

自含 JavaScript 源从原 $\widehat K$、原 Frobenius 乘法、原迹和完整 E/P/N 定义重建条件，再以 BigInt 有理数多项式运算核验 (4)–(9)。它也验证原 E0、P0、N0=P0/2、P(V)=N(V)=0，以及 trace 与缩放完全一致。

- 源码 Git blob：0f6fbabe15135c7408a8649fad551eab9b80039a。
- 源码 5345 字节；SHA-256：f0d97e71d86fafa8a41822c84d7dd89bb5aa28cb2471d5a5165734d68aaea735。
- 实际执行环境：本会话 functions V8；所有数值为 BigInt 约分有理数，未调用浮点近似。
- 实际执行 0.012 秒，15 条原有理多项式恒等式全通过，485 次多项式乘法。
- 四条原式 E1、EB、EC、最高 jet 的规范系数序列 SHA-256：29de45b73a30f2b8965fb9f7d133dd013d293e115f6848ffefd3e9d473008ee2。
- 实际小回执 blob：9bb4700caea9dfda75bf386d88f6a688d4e5af9f。
- 源为一个自含 JavaScript 表达式，执行其表达式返回精确检查结果；没有外部数据或软件包依赖。

早先公开 run 45827161540 / job 139934168089 在完成原 lambda=1/2 九式后，由于全部 t 结果式确实恒零，在“必要投影列表应非空”的入口断言处退出 1。该真实失败及其输入 6614c6831259dac637c76f5958effc002dafcc9710bb1d56194f582ebbe53a6b 保留在独立回执中。它促成了第 3 节必须补第五列的正确分层，不能当成该抽象族的代数排空证书。本条是另一次真正完成的原恒等式核验和物理秩证明。
