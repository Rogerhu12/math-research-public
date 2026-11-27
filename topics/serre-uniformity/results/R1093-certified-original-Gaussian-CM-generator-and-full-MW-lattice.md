# R1093. 原 Gaussian CM 类生成 full47 的整 MW 格及全73维首对数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已证明，含公开精确有限域计算。**
这是固定 $p=47,q=4513$ 的原 Jacobian 整格结论；
没有宣称高度非零、原八盘内唯一或全素数 Serre 一致性。

## 1. 结论与实际对象

令
$$
X=X_{\rm ns}^+(47),\quad J=\operatorname{Jac}(X),\quad q=4513,\quad
u_4=23[y_{1728}]-C_\infty,\quad B_q=q+1-T_q.
$$
$y_{1728}$ 始终是 R1074/R1086 的同一原有理 Gaussian CM 点。
记
$$
\mathcal T=\mathbf Z_q[H_2],\qquad H_2=T_2+2T_3+4T_5,\qquad
M=(J(\mathbf Q)/J(\mathbf Q)_{\rm tors})\otimes\mathbf Z_q.
$$
R1081 已证明 $\mathcal T$ 是原最大未分歧整 Hecke 序；
此处没有经一个未知整同源搬换格。

本次实际计算给
$$
\lambda_4:=q^{-1}\log_J(B_qu_4)\pmod q
$$
在 $\mathcal T/q$ 的**全部28个域因子上均非零**。
因子次数为 $1^{16},2^6,3^4,11,22$，总维数73。
因此
$$
\boxed{\quad M=\mathcal T u_4=\mathcal T(B_qu_4),\qquad
\log_J(M)=q\,\operatorname{Lie}J(\mathbf Z_q).\quad}
\tag{1093.1}
$$
换言之，73个真实有理除子类
$$
u_4,H_2u_4,\ldots,H_2^{72}u_4
\tag{1093.2}
$$
给 $M$ 的一个 $\mathbf Z_q$ 基。
这是在4513处饱和的完整 MW 格，不是整个整数 MW 群的无条件全素数基。

## 2. 此次公开执行及未重复的输入

公开 [run45947023569](https://github.com/Rogerhu12/math-research-public/actions/runs/45947023569)，
job140333947037，源提交
`282be088b6286c21e4ccedf79127c8a1f93e77df`，
状态 success，数学时间 **65.967186095 秒**。
固定官方 SageMath10.6 image digest 与1800秒总预算/60秒 reserve，
均见[完整方法](../notes/2026-11-27-full-p47-Gaussian-CM-log-method.md)
及[请求](../notes/full-p47-Gaussian-CM-log-request.json)。

本次只重建 R1090 的95个已认证来源并核五个实际hash；
没有重跑候选搜索、旧秩、$L'$、全标签图或原群阶证书。

新计算先在同一原73维 Hodge 基上构造
$T_2,T_3,T_5$，使用 R1090 的完整 Galois方向与degree835界；
实际坐标等式和算子交换成立。
其 $H_2$ 特征多项式 squarefree，
完整因子次数与16个一次根均和 R1081 一致。
所以后面的 CM 列与 Hecke 列在同一原整基中。

## 3. 原 CM 系数的来源与实际标记

原短族
$$
E_z:Y^2=X^3+343X+z,\qquad\omega=dX/(2Y)
$$
在 $z=0$ 使用实际点
$$
P=(653,525),\quad Q=(3860,232),\quad i=95,\quad Q=iP,
\qquad e_{47}(P,Q)=2.
\tag{1093.3}
$$
初始配对8经范数缩放 $(r,s)=(0,4)$ 精确变为2。
47挠点阶、独立性和配对均由实际群运算核准，
标记与 R1090 的标准 Weil 根同向。

对原 $\psi_{47}$ 的唯一 Hensel 根，只提升 $P(z)$，
再由同构 $E_{-z}\to E_z$ 得 $Q(z)$，
并用原加法式生成全部2208个非零挠点及 $e$ 值。
程序核每点曲线方程、互异常数、负号及 Gaussian 作用。
所有短模型斜率用 $+m_Y$，没有多余的 $1/2$。

R1091 的精确原公式给
$$
\lambda_4(\omega_F)
=\frac{23}{k(0)}[z^{4512}]F(z)k(z)I(z),\qquad
I(z)=\int_0^z k/H^2\,dz\pmod{z^{4513}}.
\tag{1093.4}
$$
此次实际 $H(0)=96$、$\deg H=752$、$k(0)=809$。
完整 $I$ 的导数、奇偶性及未除以4513的截断均通过。
95个形式保全两个 Reynolds 相位、全部46范数组、
纯虚 $\rho=2i$ 以及 descriptor 的 $d+ci$ 坐标。

95个原系数按同一 $73\times95$ 留数核投影，
得到真正整全纯 Hodge 基上的首log列。
原全纯整 lift 的存在已由 R1090 的单位22 minor支付；
这里没有用有尖点极的任意整数 lift 来定义 Jacobian 对数。

## 4. 全28块与16个一次块的实际值

对实际 $H_2$ 矩阵 $M_H$ 的每个不可约因子 $f$，
消费者以 $\chi=\chi_{M_H}$ 构造
$$
e_f=(\chi/f)\,(\chi/f)^{-1}\pmod f\pmod\chi
$$
并精确读取 $e_f(M_H)\lambda_4$。
28个投影全部非零，各自被 $f(M_H)$ 杀掉，
全部之和等于原73维列。
其规范因子和投影hash在公开回执
`actual_full_CM_blocks`，完整结果对象hash见 §6。
这包括度11和22的两个主系列块，不仅是16个一次块。

对一次根 $\alpha$，取实际左 eigenform
$vM_H=\alpha v$，把它在 R1090 原73维基中的首个非零坐标定为1。
以下是这一明确规范下的 $\lambda_4(v)$：

| $\alpha$ | $q^{-1}\log(B_qu_4)(v)\bmod4513$ |
|---:|---:|
| 434 | 3527 |
| 1054 | 1604 |
| 1615 | 1240 |
| 2250 | 725 |
| 2425 | 420 |
| 2472 | 3347 |
| 2604 | 1418 |
| 2838 | 3824 |
| 3030 | 3003 |
| 3112 | 1974 |
| 3531 | 3330 |
| 3560 | 4182 |
| 3639 | 3589 |
| 3645 | 3771 |
| 3786 | 3508 |
| 3795 | 3363 |

这些是保留 $B_q$ 后的准确值。
R1089 允许去掉 $B_q$ 比较深度和生成格，
不能在这张数值表中直接把它删掉。
这里的 $\alpha$ 是实际 $H_2$ 根，不是 R1088 角代数的 $G$ 根。

## 5. 从实际首矩到完整 MW 格的证明

先说明这一推论需要哪些既有输入。

R1089 的 $\#J(\mathbf F_q)\not\equiv0\pmod q$ 给
$$
\log J(\mathbf Q_q)\subset q\,\operatorname{Lie}J(\mathbf Z_q).
\tag{1093.5}
$$
事实上令 $n=\#J(\mathbf F_q)$，则 $nP$ 落在形式核，
$\log(nP)\in q\operatorname{Lie}$，而 $n$ 为 $\mathbf Z_q$ 单位。
形式群对数在 $qJ$ 邻域又给满的 $q\operatorname{Lie}$。
同篇证明 $B_q$ 在原整格上可逆。

R1081 的 squarefree 特征多项式说明
$\mathcal T/q$ 是28个有限域的积，
原 Lie 格的约化在每一域因子上都是一维。
因此一个列在所有因子均非零，当且仅当它是这个
$\mathcal T/q$ 模的生成元。
§4 的实际结果与 Nakayama 给
$$
\mathcal T\cdot q^{-1}\log(B_qu_4)
=\operatorname{Lie}J(\mathbf Z_q).
\tag{1093.6}
$$
$\mathcal T$ 的秩为73，而 Lie 格秩也是73，
所以这个生成映射是整同构。
等价地，$q^{-1}\log(H_2^jB_qu_4)$、$0\le j\le72$，
构成原 Lie 格的整基。

设 $N=\mathcal T(B_qu_4)\subset M$。
式 (1093.6) 证明 $N$ 的 $\mathbf Z_q$ 秩为73且
$\log N=q\operatorname{Lie}$。
R1080 已无条件证明 $\operatorname{rank}J(\mathbf Q)=73$，
故 $\log:M\otimes\mathbf Q_q\to\operatorname{Lie}J(\mathbf Q_q)$
为同构；在无挠的 $M$ 上尤其单射。
结合 (1093.5)，对任何 $x\in M$，
$\log x\in q\operatorname{Lie}=\log N$，
由单射得到 $x\in N$。所以 $M=N$。
最后 $B_q\in\mathcal T^\times$ 给
$\mathcal T(B_qu_4)=\mathcal T u_4$，证明 (1093.1)–(1093.2)。

这个证明直接在原格中进行，
不需要另一次整数点饱和搜索、不用 BSD，
也不以有理同源的次数为单位作未付假设。

### 5.1 两原 fixed classes 生成全部 cusp MW 块

记 $\mathcal T_c$ 为 R1087 的原 cusp 类型部分，
$M_c=e_cM$。
R1088 已给
$$
\mathcal T_c d_2+\mathcal T_c d_3
=\mathcal T_c u_4+\mathcal T_c u_0.
$$
现在 $\mathcal T_c u_4=M_c$，于是
$$
\boxed{\quad \mathcal T_c d_2+\mathcal T_c d_3=M_c.\quad}
\tag{1093.7}
$$
所以这两个实际迹零对应的 fixed classes
已经共同生成全部40维 cusp MW 格。

还可给一个有限的真存在结论：
cusp 部分有 $16+6+4=26$ 个剩余域因子。
每个因子中 $d_2,d_3$ 不同时为零；
至多一个 $t\in\mathbf F_{4513}$ 使 $d_2+t d_3$ 在该因子为零。
因此在 $t=0,\ldots,26$ 这27个不同整数中，至少一个满足
$$
\mathcal T_c(d_2+t d_3)=M_c.
\tag{1093.8}
$$
这是原迹零对应 $Z_2+tZ_3$ 的实际 fixed-class 族。
本次没有计算哪个 $t$，也没有给其高度值；
不能把这条整生成断言替代后继全局高度比较。

## 6. 复核入口及哈希

消费者：
[full_p47_Gaussian_CM_log.py](../scripts/full_p47_Gaussian_CM_log.py)。
请求固定全部95个原 descriptor、已有五个Hodge hash、
两README、R1090/R1091及同一 Sage image。

| 对象 | SHA-256 |
|---|---|
| CM消费者 | `f412bf532b09bec72d485f02d35a2c7b8b4b87cefc5c8ce4a159f299fe23f6b1` |
| 方法 | `386cf9502e3b1cd3d69049965ba5182ed22a729e8ace18f911a90e9e9f85b5bb` |
| 请求 | `469f9d05fe0e0b687f325977c2196acce30ce6ce59ebfb124969a64ab0a44810` |
| 实际原基 $H_2$ 矩阵 | `d943671a31934160b148d8396202ebe597a82d2a7336cc56cd6a182e1a66424f` |
| 原2208点与 $e$ grid | `627e076ae64de06332324f1bdf0a82e2888b493f4799af3b7211c6d7524d7c50` |
| 原权重 $23kI/k(0)$ | `4fbcfb0a1043f0814d718520eab485ac3697df11131257d58bc6fb88db6ef955` |
| 95个原矩 | `00b1d8296c97d0bec3716cfb8424c992b8b53d5806817d0456225a2e3996be84` |
| 原73维 Hodge首log列 | `489ab09b0e7bedae211e478938e687b51cd3d477438d9d47605d2cac0a4929dd` |
| 完整28块结果对象 | `3aca2663cf57032a02f6da59c3c5062f7b223c1e52108ea8b2c591a2a4c82627` |

原矩阵和长级数只在 runner 内存，没有保存 artifact、Release 或数据分块。
后继只重建必需输入并核这些实际hash，不重复已完成的认证。

## 7. 当前准确剩余任务

完整原 MW 格和全部整块的首log已付清。
仍需计算原 tracezero 对应的真实全局高度、
原 CM 残余盘上的局部高度差或首阶，并证明盘内排除。
纯对数的全格生成不推出这些高度条件。
本条只有 $p=47$ 的有限结论；
全 $p$ 完整非分裂正规化子及 README 的绝对一致性目标仍开放。

来源：R1080（原全J无条件rank73）、R1081（实际整Hecke序）、
R1088（原双CM整span）、R1089（原 $(B)_q$ 与整log范围）、
R1090（原完整整Hodge源）、R1091（同一Gaussian CM精确高矩）。
