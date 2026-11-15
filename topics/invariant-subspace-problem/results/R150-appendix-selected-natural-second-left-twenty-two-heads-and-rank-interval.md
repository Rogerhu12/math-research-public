# 同一所选自然参数第二左 jet 的 22 个精确头与秩区间 $[9,11]$

作者：Astra-ISP-789f / normal_annihilator。  
AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

## 1. 结论与实际范围

在原自然参数 $u$、原行列集合 $I,J$ 所给的 $4354$ 阶方阵 $B(u)$ 上，现已构造 **22 个头独立的真有理第二左 jet**。每个候选均在全部原 $4354$ 个来源上完成第二系数恒等式的整数乘回，合计 $4354\cdot22=95\,788$ 个产品为零。

结合已付同一常数单位模型及第一连接的特征零、模 31 秩均为 $3$，本次给出

$$
9\leq\operatorname{rank}_{\mathbb Q}\beta_2(B)\leq11.
$$

更精确地说，在第二校正仅允许 normal 次数至多 $3$ 的支持内，完整可延二阶的头空间维数**恰为 22**。本次未排除 normal 次数 $4$ 或 $5$ 的校正；因此不能把上界 $11$ 写成完整第二连接的确切秩，也不能写成预期的 $9$。

本次是有限规范更换后得到的完整结果。此前旧规范的模 31 秩 $1545$ 已被实际新单位块取代；没有换素数，没有重算旧第一 RREF，也没有重算完整第二右端。

## 2. 已付第一阶来源

沿用以下正式结果与实际记录：

- `results/R150-appendix-selected-natural-first-connection-exact-rank-three.md`；
- `notes/r150-infinity-remote-session-789f/43702348535-selected-natural-first-characteristic-zero-left-envelope-continue180.json`；
- `notes/r150-infinity-remote-session-789f/43702348535-selected-natural-u-minimal-rebuild32.json`。

原常数方阵秩为 $4318$，常数左核维数为 $36$。其完整头矩阵记作 $\Lambda$。已付第一连接秩为 $3$，33 个完整第一左 jet 写作

$$
V_{1,0}=\Lambda C,\qquad V_{1,1}=E_{\rm old}X,
$$

并逐原列满足

$$
B_0^TE_{\rm old}X+B_1^T\Lambda C=0.
$$

令 $F$ 是补齐 $C$ 的三个原头坐标。任意第一左 jet 唯一按其头及常核自由度表示为

$$
\lambda_0=\Lambda Cc,\qquad
\lambda_1=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy,
$$

其中 $c,y\in\mathbb Q^{33}$，$t\in\mathbb Q^3$。此前实际完整构造的第二右端为

$$
R=[HF,T],\qquad
HF=B_1^T\Lambda F,\qquad
T=B_1^TE_{\rm old}X+B_2^T\Lambda C.
$$

它保留全部 $4354$ 个原来源，而非仅保一个秩剖面。

## 3. 实际只更换一个规范坐标

旧第二入口实际记录于

`notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-unit-pipeline.json`。

旧 $M_0$ 的有理满列秩 $1546$ 已付，但把其每行除以该行系数最大公因子后，模 31 秩仅为 $1545$，故该入口在求解前停止。其全部 4354 行右端已保存；旧校正矩阵恒零的 1736 行上的 $T_{\rm high}$ 有理秩为 $0$。

新入口使用同一原模型的完整模 31 常数低余空间 $L_S$，从 1572 个 normal 次数 $1$ 至 $3$ 的允许输出坐标中选择新的 26 个规范坐标 $G'$。实际结果是：

| 实际量 | 结果 |
|---|---:|
| 旧、新校正坐标交换数 | 1 |
| $L_S$ 的独立列数 | 26 |
| $G'$ 处取值行列式，模 31 | 11 |
| 新未缩放 $M'_0=B_0^TE_{\rm new}$ 的模 31 秩 | 1546 |
| 选中行除系数公因子后的单位块行列式，模 31 | 5 |
| 完整原来源对 $L_S$ 的产品数 | $4354\cdot26=113\,204$ |
| 上述产品是否全部为零 | 是 |

选中的每个行系数公因子都与 31 互素，矩阵与右端按同一有理比例运输。旧 $HF,T$ 的每个数字保持不变；旧 $X$ 始终嵌入 $E_{\rm old}$。

设 $x'_2$ 是新规范中的第二校正变量，则实际方程为

$$
M'_0x'_2+HFt+Tc=0.
$$

它对应真实完整来源族

$$
\begin{aligned}
\lambda_0&=\Lambda Cc,\\
\lambda_1&=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy,\\
\lambda_2&=E_{\rm new}x'_2+E_{\rm old}Xy+\Lambda e,
\end{aligned}
$$

其中 $y\in\mathbb Q^{33}$、$e\in\mathbb Q^{36}$ 均保留。第二式中的 $y$ 来项由已付第一恒等式精确抵消；这里不能把 $E_{\rm old}Xy$ 改放到 $E_{\rm new}$。

新 $M'_0$ 的满列秩还证明，此规范在同一个 normal 次数至多 $3$ 支持内确为完整补空间。若一个该支持内的左向量要转入此规范，所差是完整常核 $\Lambda e$，不会丢掉真实低阶歧义。

## 4. 完整残差计算与 22 维的证明

在上述真实单位块上同时求 36 个右端。设各列保存的有理解为 $N_j/D_j$，其中 $D_j>0$，则实际先保存完整分子分母，再在原未除公因子的 1546 行上核

$$
M'_{0,R}N_j+D_jR_{R,j}=0.
$$

全部 $1546\cdot36=55\,656$ 个原单位行产品已通过。随后在全部原 4354 行形成

$$
S_j=M'_0N_j+D_jR_j.
$$

所得全残差矩阵 $S$ 的精确有理秩为 **14**。前三个第一失败轴对应的残差类独立，秩为 **3**。因此 $\ker S$ 的维数为 $36-14=22$；每个核向量 $\gamma$ 产生的原变量是

$$
x'_2=N\gamma,\qquad
(t,c)=\operatorname{diag}(D_1,\ldots,D_{36})\gamma.
$$

不能用残差核向量 $\gamma$ 直接替换有不同分母的原变量。本次逐候选保存了这项精确运输。

还须证明这 22 个核方向给出 22 个独立头，而非仅仅给出零头校正。若一个 reduced 解满足 $c=0$，则在 $\operatorname{coker}B_0^T$ 中由三个第一失败轴的独立性得到 $t=0$；随后由 $M'_0$ 满列秩得到 $x'_2=0$。因此 reduced 解向 $c$ 的投影单射。实际代码还逐列核其独立自由坐标非零及其余自由坐标为零，故全部 22 个 $\Lambda Cc$ 独立。

最后对每个候选重新核

$$
M'_0x'_2+HFt+Tc=0
$$

的全部原 4354 个整数坐标。结合已付第一族恒等式与常核，这正是三层完整左 jet

$$
B_0^T\lambda_0=0,\quad
B_0^T\lambda_1+B_1^T\lambda_0=0,\quad
B_0^T\lambda_2+B_1^T\lambda_1+B_2^T\lambda_0=0.
$$

新阶段的 95,788 个二阶产品全部为零；其余两层由相同已付实际来源的精确整数线性组合继承。

## 5. 为何只得到完整秩区间

第一连接之后的头空间维数为 33。本次 22 个真第二头给

$$
\dim\ker\beta_2\geq22,\qquad
\operatorname{rank}_{\mathbb Q}\beta_2\leq33-22=11.
$$

另一方面，同一原常数块有 31 单位秩 $4318$，第一连接在特征零与模 31 中都为 $3$。可在 $\mathbb Z_{(31)}[[u]]$ 中先消去这些单位块和三个第一层单位主元，保持相同自然 $u$。剩余第二层矩阵的模 31 秩已付为 $9$，所以其特征零秩至少为 $9$。这只是对第二层的合法秩下界，不把更高阶模 31 Smith 指数自动提升到特征零。

全部当前支持内的解都由上述完整残差核得到，所以该支持内头维数恰为 22。但允许 $\lambda_2$ 含 normal 次数 $4$ 或 $5$ 时，可能增加至 23 或 24 维。故以下说法均未由本次得到：

- 完整第二连接秩等于 11；
- 完整第二连接秩等于 9；
- 特征零无穷远长度等于已付模 31 的 243；
- 所选参数行列式最高系数为 31 单位；
- 原九目标存在特征零多项式来源。

## 6. 实际执行与可复现绑定

实际主线回执：

`notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-regauged.json`。

| 项目 | 实际值 |
|---|---|
| Actions run | `43702348535` |
| 步骤 | `selected-natural-second-left-regauged` |
| 执行源码提交 | `2cbfa8d0680e08ea57f202a4ab7091e767485666` |
| 状态、退出码 | `completed`，0 |
| outcome | `restricted-second-left-support-only` |
| 数学时间 | 103.8691627989997 秒 |
| 墙钟 | 103.92458264300012 秒 |
| 准备 / 单位解 / 完整原乘回内部时间 | 1.9363147770000069 / 95.5420168820001 / 6.076465318000373 秒 |
| 每进程内存限额 | 2048 MiB |
| 完整来源变量最大整数位数 | 9628 bits |
| 数学绑定 | `c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e` |

主程序为 `notes/2026-11-15-r150-selected-natural-second-left-regauged-runner-789f.py`，29,455 B，SHA256 `785da98d3114adf28b6d85b7f67937e8e277f2fc627bda0427f96a960d72651e`。单位 worker 字节未变，SHA256 `a706713bb49b292c7256aa67b5cb1d75b81003175ef0b87e094e4f0efc03a8a9`。

重要临时完成对象如下；它们只在实际会话存活，不作为永久数据上传：

| 临时相对路径 | 字节数 | SHA256 |
|---|---:|---|
| `prepared/same-support-field-unit-gauge.json.gz` | 4,271 | `d4cd90b0a7e1a790fa1892bf60044b73795d6394cdb0ba5e4e96a9dde004c8b4` |
| `prepared/second-left-m0-unit-input.json.gz` | 9,008,513 | `c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe` |
| `unit-solve/complete-m0-unit-solution.json.gz` | 18,124,389 | `9c3b02d2674af645ffcfd5297cf5c9ac287fe314d0c40f49c8bb99be9396352d` |
| `full-products/complete-small-second-residual-rref.json.gz` | 17,625 | `de7bb03e76ca2dee0221d4f89e1de5db190b6c5b64fc4df70a67e13f405a7941` |
| `full-products/second-left-full-products-receipt.json` | 12,690 | `b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70` |

完整小主回执的临时原字节数为 20,323，SHA256 为 `2343123363d6c38a871c66770afb67b37a1b3a6b882baa7aed040134914a345b`。主线小记录列出全部 36 个残差和 22 个候选及逐列产品回执的 SHA。下一支持扩展可直接复用这些真实对象，不重做本次约 96 秒的单位求解。

最小后继是检查新增 normal 次数 4 的原常数校正列，先在旧 $M'_0$ 恒零且旧全部右端恒零的行上求其真实核，再把实际可进入的方向投到已保存的完整残差商。这个后继尚未执行；它不能以一个有限域核代替有理校正来源。

## 7. 同一原子式的无穷远阶 $91/88$ 与条件来源费 $8627$

上述 22 个真第二头还给出直接的子式次数改进，不需要先将第二连接秩夹到 $9$。在 $\mathbb Q[[u]]$ 上记同一非零方阵 $B(u)$ 的 Smith 指数为
$\alpha_1\le\cdots\le\alpha_{4354}$。已付常核 36 维、第一可延头 33 维及本次第二可延头至少 22 维，分别给

$$
\#\{\alpha_i\ge1\}=36,\qquad
\#\{\alpha_i\ge2\}=33,\qquad
\#\{\alpha_i\ge3\}\ge22.
$$

因此

$$
\boxed{\operatorname{ord}_\infty D
=\sum_i\alpha_i\ge36+33+22=91.}
$$

对最小的 $4353$ 个指数，每一个阈值计数最多少一，故

$$
\sum_{i=1}^{4353}\alpha_i\ge35+32+21=88.
$$

Smith 的 determinantal-ideal 身份由此给同一原归一方阵的**全部** cofactor 在无穷远至少消失 $88$ 阶。这里不使用额外 13 个输出，也没有把模 31 的 cofactor 阶 $222$ 当成特征零阶。

每个原来源列按自己的原权归一后都是正则的 $u$ 级数。将 $B$ 的一个来源列换成任意其他原来源列，按被换列作 Laplace 展开，所有项均含一个上述 cofactor，故

$$
\boxed{\operatorname{ord}_\infty D_{\rm replacement}\ge88.}
$$

这一步只给 $88$，不声称换列仍有 $90$ 或 $91$ 阶。对按真实目标权归一后的任意原目标列，同一个 cofactor 展开也给 $88$ 阶。

为保留实际原权，明确沿用
[原完整来源降度式](R150-appendix-common-minor-factor-conditional-source-cost8740.md)
及[原子式权定义](R150-appendix-original-projective-minor-conditional-source-cost8814.md)：

$$
a_\ell=
\begin{cases}
20+10|\gamma|,&m^\gamma N_i,\\
25+10|\gamma|,&m^\gamma\Gamma_i,
\end{cases}
\qquad
b_i=10|\beta_i|,\qquad
\delta_\ell=a_\ell-10.
$$

原来源乘子满足 $|\gamma|\le3$，所以
$\max a_\ell=55$、$\max\delta_\ell=45$，且同一 $I,J$ 的总权为

$$
H=\sum_{\ell\in J}a_\ell-\sum_{i\in I}b_i=8770.
$$

即 $B^h(u)=\operatorname{diag}(u^{-b_i})B(1/u)
\operatorname{diag}(u^{a_\ell})$ 是本次使用的同一自然归一矩阵，不另换参数或丢失列权。

[零点第五阶正式结果](R150-appendix-zero-seventeen-fifth-left-jets-factor99-and-cost8634.md)
已证明有限公共因子

$$
K_{99}=s^{53}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2
$$

的次数为 $99$，并整除所有原最大子式；此处不称它为完整 gcd。另由同一 $D$ 的完整模 31 无穷远长度 $243$，其非零约化次数为 $8770-243=8527$，所以 $\deg_{\mathbb Q}D\ge8527$。令 $d_*=D/K_{99}$、$q=\deg d_*$，本次得到

$$
\boxed{8428=8527-99\le q\le8770-91-99=8580.}
$$

对每个原来源列 $A_\ell$，取

$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{99}.
$$

它是多项式，并在**全部原 4367 个输出**上满足
$A_JP_\ell=d_*A_\ell$：这是原泛秩 $4354$ 下从 $I$ 单射到整个原像的已证伴随运输。由换列的 $88$ 阶界，

$$
\deg(P_\ell)_j\le H-a_j+a_\ell-88-99.
$$

明确假设原目标 $b_\nu=h_0t_\nu$ 已属于
$\operatorname{im}_{\mathbb Q[s]}A$，其中原目标权
$\tau_\nu=44+2\nu\le64$。成员性使

$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{99}
$$

为多项式；同 cofactor 界给
$\deg(T_\nu)_j\le H-a_j+\tau_\nu-88-99$。

对所有非基来源按 $d_*$ 作余式整理，保持原完整来源身份，原非基、基转移、基目标三个成本分支分别为

$$
\begin{aligned}
q-1+45&\le8624,\\
8770+55-88-99-11&=8627,\\
8770+64-88-99-10-8428&=209.
\end{aligned}
$$

于是本次已证明新的条件命题

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists x^{(\nu)}:\ 
Ax^{(\nu)}=h_0t_\nu,\qquad
\max_\ell(\deg x^{(\nu)}_\ell+\delta_\ell)\le8627.
}
$$

此改进已使用 22 个真实第二头，而不要求完整第二连接恰为 9。原目标成员性仍是前提；没有证明最高系数为 31 单位，也没有由有限模精度推出特征零身份。
