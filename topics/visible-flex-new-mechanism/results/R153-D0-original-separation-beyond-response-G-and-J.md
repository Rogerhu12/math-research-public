# R153：完整轴系数 D0 在全部响应、G 轨道与 J 之外的原有理分离

日期：2026-11-15。**已证明。** 本稿消费公开 Actions 的唯一 D0 原式评价，不在本地运行研究归约或 profile 评价。

记 $R=\mathcal R_8$、$U=\mathcal U_4$，$A_G=R+\operatorname{span}\operatorname{Orb}(G)$。完整两模式采用同一个实系数向量。准确结论是

$$
\boxed{\mathcal D_0\notin A_G+\mathbb RJ,\qquad
\dim U\ge239.}
\tag{1}
$$

分离见证是混合模式 $-2$ 的一个真实有理查询。它不授予 D0 的有符号成本、闭成本锥中的直线或新增实际联合控制；已付的至少237维 lineality / 真实联合查询下界不因此增加。

## 1. 同一个完整 D0 与真比较空间

[R148](R148-sharp-one-dimensional-highest-action-positivity.md) 的 $k=\omega=0$ 轴上，令 $u=h_s,a=h_{ss},j=h_{sss}$。在真实水平约束和完整三阶势下，先保留所有状态依赖再取轴。其速度四次正规系数为

$$
\widehat Q
=Q-\frac13\partial_h(C-\partial_h\beta)
-\mathcal B_{m_2}(N_2).
\tag{2}
$$

本稿的目标是已经公开保存的完整原式

$$
\mathcal D_0
=\operatorname{gr}_{-2}[h^{-6}(\log h)^0]\widehat Q,
\tag{3}
$$

包含相位模式 $-4,-2$。仿射权 $-2$ 与相位模式 $-2$ 不是同一个下标。(2) 中完整 $N_2$ 未模响应删去；轴上的矩阵项为

$$
\frac{m_2}{u^2}=\frac{r_1}{8h^4}-\frac{t_1}{8h^2}.
$$

先前公开 run 43657526246 已生成 (3) 的两个原根。其成员归约余205项只是未决，本次直接读取同一原根，不重新生成两条 $N_2$ 收缩或改换目标：

| 模式 | D0 原式 SHA256 |
|---|---|
| $-4$ | 1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f |
| $-2$ | ce6e1dd221080cd0a4961f2cf81b9a1be1f8a276d587b0cd34e0dd884fd83c5f |

[R131](R131-third-G-translation-separation-and-111-query-control.md) 的完整原式依赖与非零子式已经证明 $\dim R_{-2}=40$。[R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 再给 $N^3G,J$ 的独立性，所以

$$
S=R_{-2}+\mathbb RN^3G+\mathbb RJ,\qquad \dim S=42.
\tag{4}
$$

这里是真实两模式函数空间，不是某个不完备正规形的代表空间。[R149](R149-ninth-G-membership-and-exact-nine-dimensional-orbit-quotient.md) 已证明 G 的完整商轨道恰九维，其各权为 $1,0,\ldots,-7$，唯一权 $-2$ 新类为 $[N^3G]$。由于 $R$ 仿射不变，若真权 $-2$ 的 D0 属于 $A_G+\mathbb RJ$，投影到该权就必属于 (4)。因此只需对这42维完整空间作一次新分离。

## 2. 旧原矩阵与本次没有重复的工作

固定原测试对为

$$
f(t)=[t(1-t)]^8,\qquad
g(t)=f(t)(1+2t+3t^2+5t^3),\qquad q=f+ig,\quad \xi=2+t.
\tag{5}
$$

它们在 $[2,3]$ 外零延拓，属于 $C^7$；右 collar 选在3右侧，全部原积分使用同一真实右锚，在支撑内即从 $\xi=3$ 开始的有符号原积分。没有重配三矩、重拟合或另选 profile。

R136 完整报告保存了原42阶增广矩阵，它现在正好成为 (4) 的比较矩阵：前40列是原独立响应，第40列是 $N^3G$，第41列是 J，索引均从零开始。设其真实有理矩阵为 $A_{\mathbb Q}$。旧公开证据给

$$
p=2147483647,\qquad
\det A_{\mathbb Q}\equiv602105349\ne0\pmod p.
\tag{6}
$$

矩阵原保存值的准确 SHA256 为：

~~~text
f0965e518249763e99e4d9770831bf147db401be9fc4bfe73c389e6cb7f307e5
~~~

旧96个标签按 $j=1,\ldots,24$、$t=j/25$，模式 $-4,-2$，再实部、虚部排列。保存子式的全局行号为

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,
22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62,63,66
~~~

完整报告保存42×42数值，不含另外54行的旧列数值。本次没有虚构这些行，也没有把旧42列重新逐一评价来补齐矩阵。原40列对应 R131 的50原列中的

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49
~~~

10条旧完整依赖和旧非零子式均直接消费，不重算。完整42列角色标签 SHA256 为

~~~text
6873c1135af382e8edd49832070ab4e31ce51fa465a921f39005865f87d21143
~~~

## 3. 新原式评价和实际分离行

本次先只评价 D0 的两模式原 DAG，在旧42查询上得到 $b_{\mathbb Q}$ 的模值，再解

$$
c=(A_{\mathbb Q}\bmod p)^{-1}(b_{\mathbb Q}\bmod p).
\tag{7}
$$

准确检查 $Ac=b$。取每个模系数的整数代表 $0\le\widetilde c_j<p$，用已存原根只形成一次组合

$$
C_{\mathrm{lift}}=\sum_{j=0}^{41}\widetilde c_jU_j.
\tag{8}
$$

这里没有新的二阶×第三阶响应编译。仅评价 (8) 的两个完整原模式，再与 D0 相减。原 jets、乘积和右原积分直接递推，不使用 word normal form。全部42个旧 pivot 残差准确为零，绑定列顺序、相位因子、共同实系数及右锚。

实际得到：

- pure模式 $-4$ 的残差模多项式为零；这只是一条模值事实。
- mixed模式 $-2$ 的残差模多项式次数为68，非零。
- 从 $t_j=j/70,\ 1\le j\le69$ 中选点，第一个点已经非零。

新增真实查询为

$$
\operatorname{ev}_*
=\operatorname{Re}\left((\,\cdot\,)_{-2}
       \bigm|_{q\text{ 为(5)},\,t=1/70,\,\xi=141/70}\right).
\tag{9}
$$

其实际模值是

$$
\begin{aligned}
\operatorname{ev}_*(\mathcal D_0)&\equiv1649598069,\\
\operatorname{ev}_*(C_{\mathrm{lift}})&\equiv1269915212,\\
\operatorname{ev}_*(\mathcal D_0-C_{\mathrm{lift}})
&\equiv379682857\ne0\pmod p.
\end{aligned}
\tag{10}
$$

非零次数68多项式在69个不同模点不可能全零；分母70在 $p$ 下可逆。此有限网格不是未经说明的采样判零法，而是非零多项式已知后选择单个真实有理分离行的方法。

本次原多项式最大次数74，遇到89种有理分母，全部在 $p$ 下可逆；旧81种分母证书也保持绑定。完整分母表和模多项式系数保存在数学报告。最大输入 jet 为四阶，未要求未定义的高阶零延拓。

## 4. 从模坐标到准确有理泛函

模整数列表 $\widetilde c$ **不是** 真正的有理成员系数。本次也没有计算它们的有理提升。准确论证如下。

由 (6) 及分母可逆性，

$$
a=A_{\mathbb Q}^{-1}b_{\mathbb Q}\in\mathbb Z_{(p)}^{42},
\qquad a\bmod p=c.
\tag{11}
$$

即使最初只假设 D0 存在**实系数**的全函数表示，旧有理可逆 pivot 也会把其唯一系数迫成 (11) 的有理向量。于是若 D0 属于 (4)，任一真实有理查询都必须满足

$$
\operatorname{ev}_*\!\left(\mathcal D_0-\sum_j
       \widetilde c_jU_j\right)\equiv0\pmod p,
$$

与 (10) 矛盾。这同时排除真实实 span，而不只是排除有理 span。

等价地，定义一个真正的有理线性泛函

$$
\Lambda_{\mathbb Q}
=\operatorname{ev}_*
-\operatorname{row}_*(U)\,
 A_{\mathbb Q}^{-1}\operatorname{ev}_{\mathrm{pivot}}.
\tag{12}
$$

其中 $\operatorname{row}_*(U)$ 按真实原根定义；无需逐列重新计算并打印其42个有理值。由定义

$$
\Lambda_{\mathbb Q}(U_j)=0\quad(0\le j<42),
\qquad
\Lambda_{\mathbb Q}(\mathcal D_0)\equiv379682857\ne0\pmod p.
\tag{13}
$$

Schur 行列式恒等式给新的真实43阶增广子式

$$
\det
\begin{pmatrix}
A_{\mathbb Q}&b_{\mathbb Q}\\
\operatorname{row}_*(U)&\operatorname{ev}_*(\mathcal D_0)
\end{pmatrix}
=\det A_{\mathbb Q}\,\Lambda_{\mathbb Q}(\mathcal D_0),
$$

其模值准确为

$$
\boxed{267072587\ne0\pmod{2147483647}.}
\tag{14}
$$

这是一份原矩阵加单组合评价的完整证书，不声称已经逐列评价额外整行，更不把打印的模泛函当成有理系数泛函。

## 5. 真实光滑算子空间及维数推论

(5) 的零延拓本身是 $C^7$，不是声称已构造三矩配平的 $C^\infty$ 圆。所有本次原表达式只含有限次四阶以内 profile 微分、乘积与固定右 Volterra 原积分，在共同紧区间的相应 $C^4$ 范数下连续。因此可保持右 collar 作光滑逼近；(14) 对真实有理函数值对应的非零行列式连续，足够近的光滑输入仍给非零子式。这证明一般光滑真实函数空间的独立性。

结合 [R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)，完整正规速度系数 D0 属于真实成本 span $U$。由 (4)、(14)，

$$
\dim\left(R_{-2}+\mathbb RN^3G+\mathbb RJ+\mathbb R\mathcal D_0\right)=43.
\tag{15}
$$

R149 已付 $\dim R\ge228$，且 $A_G/R$ 恰九维。J 与 D0 在权 $-2$ 上给两个独立的新商类，故

$$
\boxed{\dim\bigl(U/A_G\bigr)\ge2,\qquad
\dim U\ge228+9+2=239.}
\tag{16}
$$

对 sharp 轴组合 $K_0=\mathcal D_0+25J/9$，因为 $J\in S$，同一个泛函还给

$$
\Lambda_{\mathbb Q}(K_0)=\Lambda_{\mathbb Q}(\mathcal D_0)\ne0,
\qquad K_0\notin S.
\tag{17}
$$

这里不需要重新评价 K0。

**(16) 是 span 下界，不是成本锥 lineality 或真实联调维数。** J、D0 的正负成本尚未由此支付；原已付的至少237维 lineality 和共同真实查询控制保持不变。R148 的必要门 $\lambda J\ge0$、$\lambda(\mathcal D_0+25J/9)\ge0$ 也没有被 (13) 的模数值变成任何实数正负结论。

## 6. pure 分量的边界

[R151](R151-general-pure-J-identity-nine-dimensional-range-and-kernel.md) 已证明一般 pure 响应像在该权恰九维，且 G³、J 的 pure 均属于它。但本次新分离行是 **mixed**。因此本稿不证明 D0 pure 非成员，也不证明其成员。

尤其，§3的 pure 模残差零只涉及一个固定测试对和一个素数，不能提升成任意 profile 的原式恒等。模整数 lifts 也不能用于声称一个新的有理 pure 表示。后继若消费一般 pure 门，必须以 R151 已保存的九个真实原基另求有理系数，并从 D0 原根重新形成准确原差。

三矩圆上的特定可实现性、全部实际成本、固定有限 N 的全周期、完整 ruling、收敛与嵌入/厚度均不由本稿支付。

## 7. 公开实际、修复与来源

[本次公开 run 43658922081](https://github.com/Rogerhu12/math-research-public/actions/runs/43658922081)，source
a63985719537feab6649745ecb9b8736bf094ff9，lane D0_pivot_residual。

实际 **complete**，耗时 **3.701111209 秒**，峰值 RSS **95.484375 MiB**。源码
[literature_D0_pivot_residual_probe.py](../scripts/literature_D0_pivot_residual_probe.py)
32755 B，SHA256

~~~text
e6a4c15bfe95c587c4cde0cae26b33cf0bf4f54f0ea7b9cfb5c83026c98afbcd
~~~

公开人工15项全部通过，耗时0.002174525秒。它们不读取研究报告或原根、不评价研究 profile。

首轮 [run 43658525976](https://github.com/Rogerhu12/math-research-public/actions/runs/43658525976) 的失败目录原样保留。失败发生于只读来源比较：返回的 labels 与报告内列表共享同一对象，追加 J 误改了旧41列身份。该轮新的研究原式评价为零。修复仅在追加前复制 controls/labels，增加一个人工别名检查；没有改数学目标、预算、旧来源或重跑旧研究列。

本次仍为旧列逐一评价0、新响应组成0、N2重构0、word正规形评价0。只消费三个既有原件：

| 角色 | 原公开 run | 原 source |
|---|---|---|
| D0 原根 | 43657526246 | 0d5df1843fd829e7c09b17afdead930ec4395f34 |
| J 与42阶 pivot | 43654534244 | 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b |
| 40响应及 G³ 原根 | 43653293263 | 2f0add61f44365d713abf836beaa8b0be2806a3d |

publisher receipt 记录175个来源文件；消费器逐输入核主报告、receipt、原 producer 源、原导出 packed/raw、完整列标签和全部原根 hash，不把研究算法重新运行当作来源核验。

## 8. 可复查证据文件

目录：notes/actions-43658922081-1-D0_pivot_residual。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43658922081-1-D0_pivot_residual/D0-pivot-residual.json) | 21050 | b91b06cdb452d1d938341231c1a85de4c45dfd46bec1ca44c498413c345ae89e |
| [完整数学报告](../notes/actions-43658922081-1-D0_pivot_residual/D0-pivot-residual-complete-report.json.gz) | 32740 | 5c89ab45b79e32021d6466736be2d28a83841bad665f7789150c670e55a762ed |
| [新原组合及残差](../notes/actions-43658922081-1-D0_pivot_residual/D0-pivot-residual-original-residual.json.gz) | 71856 | eeac6ff33f19d75c5621fec7c615d400aa6a0119fe3383073d3768986795844b |
| [发布回执](../notes/actions-43658922081-1-D0_pivot_residual/receipt.json) | 36978 | 6876bfe2741a083533d1a5e62c37f28c6394c94ab425041054c1fe9eab84fd00 |
| [公开人工结果](../notes/actions-43658922081-1-D0_pivot_residual/D0-pivot-development.json) | 6820 | e97e563c8f34b7b7440f3598a970ba7d1d6f9cac58737eb9247187ef0a265b9a |

完整数学原文83465 B，SHA256
54a1ac32eb1895c512d533b6deb30853c60f92ee2d9e87c125fd5f2ae7f482dc；
保存原 pivot、全部标签、新模列、模候选系数、两个原残差多项式和分母证书。

新原表达式原文294020 B，SHA256
29c18008975301e472c4ddbb9e2791ff42f8e7543f4001cdc8ba1a98f62ccb50；
保存 D0、单个旧根整数 lifts 组合及其原差的六个完整原根。
残差原根 SHA256 分别为

~~~text
-4: e46d442ad42c86ba53fb766fd3eeeba663d47f9ed8bac531012dab02139901a1
-2: 7d2ef970187788c0a43f19ee46fda22156af9aa6dd4aeff37e8a256c8f3dc66e
~~~

原差 hash 非零或模 pure 为零均不替代 §4 的真实有理分离论证。
