# R781 — 大惰性素数下的原有理饱和前缀与实际首负层

日期：2026-11-15。**状态：以下实际单位子式门、原有理整数核的提升及 D=8、p=953 的精确负层已证明。**
本篇只用 R760 的同一三个固定函数和原单项式整格。
模 p 的核在完整前缀单位子式得到验证后才使用；
所得结论是原有序饱和层本身的范数，不是缩放矩阵的秩。

## 1. 原来源和需要支付的门

保原
\[
S=-t\Theta^{17}P_4,\quad
T=-t\Theta^{36}P_4V_0,\quad
U=-t^5(1-t)^3\Theta^{102}B^6,
\]
\[
P_4=(1-t)(1+8t)(1+4t/7+16t^2/7),\quad
V_0=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3),
\]
\[
B=34QP_4-6P_4-6tP_4'.
\tag{1}
\]
这是原物理正导数的六次方 U=(\partial_z\mathscr S)^6；
没有替换成旧算术来源 U136。
原实系数级数由
\[
Q=\sum_{j\ge1}q_jt^j,\qquad q_1=-2/5,\qquad
q_j=q_{j-1}\frac{6j-4}{6j-1},
\]
\[
\log\Theta=-\sum_{j\ge1}\frac{q_j}{3j}t^j
\tag{2}
\]
准确给出。

令 M_i 按总次数、再按 \nu、再按 b 递增排列
\[
S^aT^bU^\nu,\qquad a+b+\nu\le D.
\]
这是原整数格 E_D 的基，N_D=\binom{D+3}{3}。
令 r_j 为原 t 普通系数行，K_{D,k} 为其前 k 行的有理核与原整数格之交。

取 p=6s-1>7，令 k=s+1。只要前缀 r_0,\ldots,r_s 整，
将其完整矩阵记为 A。
本篇真正需要的门是：
\[
\boxed{\operatorname{rank}_{\mathbf F_p}\bar A=s+1.}
\tag{3}
\]
没有将一般的模 p 核认成原有理饱和核。

**单位子式引理。**
若 (3) 成立，则
\[
(K_{D,k}\otimes\mathbf Z_p)/p
=\ker_{\mathbf F_p}\bar A .
\tag{4}
\]
这里 (4) 作为原格模 p 中的子空间身份理解。

证明：选 A 的一个 (s+1) 阶 p 单位子式 A_I。
在 \mathbf Z_{(p)} 上，A_I 可逆，完整方程可唯一解为
x_I=-A_I^{-1}A_{I^c}x_{I^c}。
故其核是自由直和项，约化与取核交换。
有限个有理线性方程的整数核在局部化后仍是这个核，
再完成即得 (4)。
这还给一个全局整数见证：先用上述公式取有理解，
再乘一个与 p 互素的共同分母即可。

若某一后行 r_k 至多有一个 p 分母，
记 v=p r_k\bmod p。
在 (3) 下，若 [\bar A;v] 比 \bar A 多一秩，
就有
\[
\boxed{\|\varphi_D^k\|_p=p.}
\tag{5}
\]
上界来自整格上 r_k 的简单极；下界由 (4) 中 v 非零的核向量提升。
如果 (3) 未付，本篇的程序明确不作 (4) 或 (5) 的推论。

## 2. 原整个前缀确实整，极点行只有两项

在 (2) 中，q_1,\ldots,q_{s-1} 都 p 整；
第一次可能的 p 分母是 q_s，并且是简单的。
因为 j\le s<p，指数化涉及的其它整数分母也都是 p 单位。
由 (1) 中的 t 与 t^5 因子，所有原单项式在 r_0,\ldots,r_s 上均整。

更准确地，原单项式的最低阶为
K=a+b+5\nu。
非恒定原单项式的第一次 p 分母不早于 K+s。
故 r_{s+1} 的极点部分只有单独的 S 与 T 两列。
这里不需要把 R775 的 p>204D 定理外推到更小范围；
结论直接由完整原级数 (1)–(2) 和最低阶得出。

原实际首残数为
\[
p q_s\bmod p
=c_p=2(-1)^s\binom{3s-1}{s-1}\in\mathbf F_p^\times.
\tag{6}
\]
它也可由 (2) 的 q_{s-1}(6s-4) 直接读出；
两种表达在公开执行中独立核同。
因为 3s=1/2\bmod p，
\[
p[t^s]\log\Theta=-2c_p,\qquad
p[t^s]\Theta^n=-2nc_p.
\]
于是整个原极点行准确是
\[
\boxed{
v_i=
\begin{cases}
34c_p,&M_i=S,\\
72c_p,&M_i=T,\\
0,&\text{其它所有原列}.
\end{cases}}
\tag{7}
\]
所有 r_{s+1} 系数至多简单极，未删原 P_4、V_0 或 B 的任何系数。

计算 \bar A 只用 q_j、\log\Theta_j 的 j<s 部分。
由于 S、T 已有 t，U 已有 t^5，
前缀没有读到非整的 q_s 或 \log\Theta_s。
程序不是任取这些共振项的模 p 值再宣称所得是原前缀。

## 3. 一个支付全部原核门的具体结果

取
\[
\boxed{D=8,\quad N_D=165,\quad p=953,\quad
s=159,\quad k=160.}
\tag{8}
\]
953 为惰性素数，并满足 p>119D=952；
所有正 charge n\le102D 以及 n+17\nu\le119D 都小于 p。
本篇只使用上一节的直接首极公式，不借用尚未证明的全旗标估值。

公开精确执行给：
\[
\boxed{
\operatorname{rank}\bar A=160,\qquad
\det\bar A_{\{0,\ldots,159\}}=328\pmod{953},}
\tag{9}
\]
\[
\boxed{\operatorname{rank}[\bar A;v]=161.}
\tag{10}
\]
首残数 c_p=601，(7) 的两个非零值分别为
\[
v_S=421,\qquad v_T=387.
\]
用前160列化行后，最后五列的极点残数准确为
\[
(210,227,522,147,766).
\tag{11}
\]
这些列依次是
\[
STU^6,\quad T^2U^6,\quad SU^7,\quad TU^7,\quad U^8.
\]

特别可以明确写出一个真正的有理前缀核元素，
而不打印巨大的有理系数：
\[
P_*=
M_{160}-
\sum_{i=0}^{159}
\bigl(A_{\{0,\ldots,159\}}^{-1}A_{\{160\}}\bigr)_iM_i .
\tag{12}
\]
它是原次数8来源，前160个系数严格为零，
其全部系数都 p 整且 M160 系数为1。
由 (9)–(11)，
\[
p\,r_{160}(P_*)\equiv210\ne0\pmod{953}.
\]
乘一个与953互素的整数清去其它分母，
便得到原全局整数格中的 P，同样前缀严格为零、p-adic 系数范数为1，
且 v953(r160(P))=-1。

结合 (5)，得到原实际层的精确结论
\[
\boxed{\|\varphi_8^{160}\|_{953}=953.}
\tag{13}
\]
R769 已付原 w/t 前缀的有理核完全相同，
其首行相差 (-1)^k；
在此 k=160，甚至符号也相同。
故 (13) 同时是原物理 w 有序旗标的结论。

## 4. 公开复现记录

唯一 producer：
[scripts/check-r781-original-large-p-prefix-gate.py](../scripts/check-r781-original-large-p-prefix-gate.py)。

- 命令参数：--pairs=8:953；仅 Python 标准库，全部数学执行在公开 Actions。
- 源提交：83b80cdc8ff62010f4230c5cb60cf7a8af5cbb44。
- [公开 run 43730703294](https://github.com/Rogerhu12/math-research-public/actions/runs/43730703294)，job132862257431，成功。
- producer SHA256：c8c4b048eca7ee15f19cfaa2009f33c7e4fff87a734f3d99f888f2d16b9e9149。
- stdout4170B，SHA256：4c1b0f68a7c0691262150a20b73e77cb680f5b39ffed70e3013479778afff411。
- 整个160×165原前缀矩阵的规范紧凑JSON SHA256：
  e86ae62b54be2a97fc681fe775f91d618b0178cffbb39c0024aa9caa3cf5c311。

程序完整生成 (1)–(2) 的原列，逐行有限域消元记录单位子式，
直接检查核见证杀全部160行且极点值为210。
其模 p 核仅在 (3) 成立的分支被解释为原有理核；
失败分支明确保留未付门。
可重算矩阵、见证清单和运行输出均不存入仓库或 Release。

## 5. 对主路径的准确作用

R779 的 D1–4 负素数都落在较小的 charge 范围内。
(13) 现在在 p>119D 的范围给出了一个完全原生的负层，
说明原抽象曲率的单项式首项单位可以在某个实际饱和层中存活。

它不把一个有限 D,p 结果推广为任意 D 的范数公式，
也不推出任何原中央导数非零。
R760 的无条件大惰性负层定理和严格门
a_I+3b_I<6 仍按原量词保留；
要利用新增三格完成主目标，仍须证明原中央失败对同一格的真实影响。
后续不能只以 p-曲率的抽象单射或不带单位子式的模 p 核替代这一步。

依赖：[R760](R760-positive-derivative-three-coordinate-grid-and-full-slope-threshold.md)；
[R769](R769-original-confluent-theta-return-for-positive-derivative-grid.md)；
[R775](R775-original-affine-inert-p-curvature-and-native-first-resonance.md)；
[R779](R779-original-small-degree-complete-rational-saturated-flags.md)。
