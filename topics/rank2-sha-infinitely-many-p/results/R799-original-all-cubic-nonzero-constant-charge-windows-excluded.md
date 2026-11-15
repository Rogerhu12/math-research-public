# R799 — 原常数 charge 非零的全部三次强窗口对所有素数排除

日期：2026-11-15。**状态：下述全窗口、全素数排除已证明。**

R792 把 $q(t,0)\ne0$ 的原窗口压到 $r=2,3,4$、$k_{\rm carry}=0$。
本篇完成这一范围的全部 $b=b_0=3$ 情形，包含每个原允许的 $\ell$，
不再只限 R788 的 $r=2,\ell=1,m_q=0$。
证明使用已经支付的同一五型最大子式和十九角几何；
新的公开计算只需三个实际九列非齐次系统，三者均不相容。

## 1. 定理及原强门

保持原 $\mathbf F_p$、primitive 不可约 F、几何整曲线 C，
以及
$$
P^{\rm fact}=qt^rF^3\in\overline{\mathcal W}_D,\qquad
q=d^{-C_D}Q,\quad d=1+8t,\quad f_D<p,
$$
$$
F(0,1)=0,\quad F_Y(0,1)q(0,1)\ne0,\quad
b=b_0=\deg_YF=\deg_YF(0,Y)=3,
\tag{1}
$$
$$
0\le k_{\rm carry}=2h+r-s<\ell\le r\le13<h,\qquad
b_0>4k_{\rm carry}+2,\qquad p=6s-1>101.
\tag{2}
$$
原强接触窗按 R750 保
$$
F(t,g(t))\in t^h\mathbf F_p[[t]],\qquad
T_M=s-r-13,\qquad T_M-h>\kappa,\qquad\kappa=C^2.
\tag{3}
$$
这里的 $\kappa$ 是原十九角自交数，不是普通分支的缩放参数。

**定理。** (1)–(3) 与
$$
\boxed{q(t,0)\ne0}
\tag{4}
$$
不能同时成立。

定理保同一个原来源及全部角帽。
它没有给任意辅助因子添加中央零，也不替换同一个首次修正 R。
常数 charge 为零的分支由 R797 另行处理，不属于本定理。

## 2. r/k 及原 p/h 关系

R792 直接给
$$
r\in\{2,3,4\},\qquad k_{\rm carry}=0,\qquad
F(t,0)=\lambda d^c .
\tag{5}
$$
因为 $b=b_0=3$，F 的每个系数在 t=0 正则，
其零角亏损准确为 $m_F=3$。
写 $G=F/(\lambda d^c)$，则 $G(t,0)=1$，
且 G 属于 R792 的完整系数格。

由 (2)、(5)，原相对接触深度准确满足
$$
\boxed{s=2h+r,\qquad p=12h+6r-1.}
\tag{6}
$$
因此 (3) 的强门变成
$$
T_M-h=h-13>\kappa,
\qquad
\boxed{h\ge\kappa+14.}
\tag{7}
$$
这与 $\ell$ 的具体值无关。
下面不使用 $\ell=1$ 的 Bockstein 或第三块公式，
所以没有把那些公式未经证明地推广到其他 $\ell$。

## 3. 同一原最大子式排除所有大 h

R788 在五个完整 factor 格上给出两组真实有理最大子式。
其共同坏素数全部不超过211，
在最高所用行以前的有理分母也都是这些 p 处的单位。

- r=2 可使用全部五格，最高所用行依次为25、24、25、27、25。
  因而当 $h\ge28$ 时，常数列和全部正 charge 列已线性独立。
- r=3 的 b=3 候选仅属于 mask 1（无穷远亏损降为0）
  或 mask $t-1$；这两个格分别包含于 R788 的对应格，
  最高所用行分别为25、24。
- r=4 的 b=3 候选只有 mask 1、全部其他亏损0，
  同样包含于 R788 的 mask 1 格。

在后两种情形，$h\ge26$ 已足够。
缩小允许列不可能使一个本来不在大列像中的常数右端进入像。
因此
$$
\boxed{
\begin{aligned}
&r=2,\ h\ge28 \quad\Longrightarrow\quad\text{无候选},\\
&r=3\text{ 或 }4,\ h\ge26
 \quad\Longrightarrow\quad\text{无候选},
\end{aligned}}
\tag{8}
$$
只要 $p>211$。

以下准确几何给 $h\ge23$；由 (6) 所有可能 p 已大于211。
所以 (8) 不留下一个未检查的小分母例外。
这里复用的是 R788 已证的全素数单位子式，不是重新采样更大的素数。

## 4. 准确小几何把有限部分压到三种系统

R788§3 的几何证明只使用
$b=b_0=3$、$F_0=\lambda d^c$ 和五格角帽，
没有使用 $m_q=0$ 或 $\ell=1$。
R792 已把这些前提全部付给当前候选，故仍有
$$
\boxed{\kappa\ge9.}
\tag{9}
$$
若 $\kappa\le11$，则原几何类唯一：
$$
c=u=0,\qquad
\boldsymbol\mu_h=(3,0,0,0),\qquad
\boldsymbol\mu_1=(3,0,0),
$$
$$
\boldsymbol\mu_d=\boldsymbol\mu_\infty=0,\qquad
\kappa=\chi=9,
\tag{10}
$$
两条 h7 共轭链相同，原 t=0 四步链均为零。

由 (7)、(9)，$h\ge23$。
结合 (6)、(8)，有限候选如下：

| r | 需要检查的 h | 对应 p | 剩余素数 |
|---|---|---|---|
| 2 | 23、24、25、26、27 | 287、299、311、323、335 | 311，h=25 |
| 3 | 23、24、25 | 293、305、317 | 293，h=23；317，h=25 |
| 4 | 23、24、25 | 299、311、323 | 311，h=24 |

表中非素数的分解为
$287=7\cdot41$、$299=13\cdot23$、$305=5\cdot61$、
$323=17\cdot19$、$335=5\cdot67$。
所有剩余候选的 h 至多25，故 (7) 强制 $\kappa\le11$，
于是必须是 (10)。

整个 (10) 来源经一个非零常数归一后为
$$
\boxed{
F=1+\sum_{n=1}^3
 \bigl(h_7(t)(t-1)Y\bigr)^n p_n(t),
\qquad \deg p_n\le n,}
\tag{11}
$$
其中 $h_7=7+4t+16t^2$。
这含全部九个非恒定系数，不是只检查若干代表。

## 5. 三个真实非齐次系统均不相容

沿同一个原低轴
$$
\rho=d\Theta^{17},\qquad g\equiv\rho\bmod t^s,
$$
式 (11) 的完整非恒定列为
$$
t^j[h_7(t)(t-1)]^n d(t)^n\Theta(t)^{17n},
\qquad 1\le n\le3,\quad0\le j\le n .
\tag{12}
$$
右端准确为 $(-1,0,\ldots,0)$。
因为 $h<s$，没有用 $\rho$ 替代任何未经支付的真实高尾。

公开精确执行读取全部列、全部原有理系数并在目标特征逐行消元：

| p | h | 原非恒定列数 | 原矩阵秩 | 添真实右端后的秩 | 结论 |
|---:|---:|---:|---:|---:|---|
| 293 | 23 | 9 | 9 | 10 | 不相容 |
| 311 | 24 | 9 | 9 | 10 | 不相容 |
| 317 | 25 | 9 | 9 | 10 | 不相容 |

p=311 的前24行已经不相容，
所以同一系统再增加第24行、要求 h=25 时仍不相容。
这同时覆盖上表中的 r=4 和 r=2。
于是所有有限候选均被排除，联 (8) 证明定理。$\square$

这些消元甚至不需要再施加不可约和原点光滑；
对整个必要线性包络无解已足够。
没有把有限个素数本身外推为无限结论：
全部其他素数由 (8)、(9) 和完整 p/h 分类先行覆盖。

## 6. 公共执行与复现

producer：
[check-r799-original-b3-remaining-windows.py](../scripts/check-r799-original-b3-remaining-windows.py)。

它通过 SHA256 固定原 R788 producer，
只 import 其 Fraction 级数、有限域和精确消元函数。
新的执行没有重新运行五格的大素数证书，也不写任何输出数据文件。

- 源提交：6de3892a333e211e2ac4297f3a426489cca21b99。
- 公开 [run43738777466](https://github.com/Rogerhu12/math-research-public/actions/runs/43738777466)，job132887136518；状态 success。
- 命令：python3 topics/rank2-sha-infinitely-many-p/scripts/check-r799-original-b3-remaining-windows.py；无参数、仅 Python 标准库。
- 脚本 SHA256：73582a7581a64143e4f0ac10c7322bc9e8c0499e55055884eca7de67d1bd5cc6。
- 原 R788 helper SHA256：f729371aa6867a84e1a4de18abdcd6d2451987e7174809a0a19269631c68da0e。
- stdout 1082 bytes，SHA256：2316656ed7c73a748522afabcf84928e65e000229ea808fed076aab95c37c31c。
- 完整25行有理输入矩阵 SHA256：a72cb1699c01a3b6b378bc28c153537419796fabba6c1c04a6ec1086bffa3ea9。

每个实际有限域输入及 RHS 的 hash 由同一公开日志给出：
p293 为 3bbf10ba42fc5f3ded076ff5350faf4da43ea910364aeef46e77921307a82a0a；
p311 为 e905d83e408fb328e35238672f87e4f461ff0ad420c9faaa69167776765a2d86；
p317 为 ec64212652da647b8c14445548dee472be0a42fbd5373952c50c2e6952ccd851。
不另把可重算矩阵、RREF 或输出 JSON 写进仓库。

## 7. 剩余范围

当前结论是：在原强窗与 $b_0>4k_{\rm carry}+2$ 下，
若 $q(t,0)\ne0$，任何原因子都必须有 $b\ge4$。
它覆盖全部原允许的 r、k、ell，
而不是只在一个特别选择的 scalar 乘子上排除。

若 $q(t,0)=0$，本篇不把 (9)、(10) 原封不动搬过去；
该支的移动 H 和全部额外 Y 角成本由 R797 保留。
更高 b、原全 $\mathcal W_D$ 的指定 Bockstein 配对、
同一个 R 的下一位及原中央问题继续开放。

依赖：
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R788](R788-original-cubic-factor-all-prime-exclusion.md)；
[R792](R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)。
