# R856：原 P0 与 cusp 加 P0 的完整两图理想基

**状态：已证明，实际准确计算已完成。** 2026-11-16，serre-public-astra-20261115。公开 run **43805659598** / compute job **133095773462**，source commit **ebdb4e512bb3cb8f8fadbb3bf2b9e69f11127051**。本结果只闭合原固定支撑块；原 $B,D$ 函数坐标、Riemann–Roch、$\eta$ 和高度仍未完成。

## 1. 实际结果

沿用原 $K=\mathbf Q(\zeta)$，$\zeta^2+\zeta+1=0$。原两图为 $\tau\ne0$、$\sigma\ne0$，变量分别 $z=\sigma/\tau$、$v=\tau/\sigma$，原正规基次数为 $0,1^{144},2^{127}$，秩272。原 $\mathscr C$ 是已成 R820 的二十个约化 cusp 的理想；$P_0=\phi(c_0)$ 是 R837 已成的同一原点。

实际运行完成：

1. 两图全部272个正规基在原 $P_0$ 的准确 $K$ 值，原 $\tau(P_0)$、$\sigma(P_0)$ 均非零；全部比值和两图尺度运输准确乘回。
2. 两图原点理想 $\mathfrak m_{P_0}$ 的完整272列多项式基，每图余长1。
3. 两图 $\mathscr C\mathfrak m_{P_0}=\mathscr C\cap\mathfrak m_{P_0}$ 的完整272列多项式基，每图余长21；其行列式为同图 $(x-x_0)P_{20}(x)$。
4. 两图原 cusp 完整基在 $P_0$ 的实际第一非零评价列都为 **$k=0$**。这个 pivot 来自新准确评价，未事先填作输入。

两张图均输出全部原列序0到271。新增固定理想列每16列原子保存；每图17组。总计42个完整数学阶段，原 core 记时 **29.229620816999983秒**。输出中的完成旗标为完整两图点理想、完整两图固定支撑理想及同一全局理想；$B/D$ 坐标、一般乘法表、$\eta$ 与高度旗标为 false。

## 2. 原输入、尺度和复用边界

数学证明及全部尺度见 [R856 固定支撑及三标量入口](../notes/R856-original-fixed-branch-ideal-and-three-scalar-pole-source.md)，SHA256
e2f61908c8e17d8c16113c5c85eccabe71b4c0b7fd057b01daee9081d391b4e2。
执行规则见 [确定性执行契约](../notes/R856-original-fixed-branch-ideal-bases-method.md)，SHA256
9a89c865989cdeeb6a18e2b180f76cfd6be425c7be615838c55c4106fffeea0d。

实际使用的原文件共569件：

| producer | 原 run / source | 原件数 |
|---|---|---:|
| R820 完整 cusp 两图基 | 43721747750 / 7890fde180ffabee056de2ce8dd241b189a893a2 | 554 |
| R805 原 free-basis 与 pencil | 43705580592 / 9f960b8e0b2fa825ab1391e86db4e1383ffdd700 | 7 |
| R837 原 V1/V2 的 P0 值 | 43770995901 / fa17c77fe36fddd9df06677569984d1ea71a6b41 | 8 |

R820 的544条原 cusp 列逐字读取；R805 经 R820 原载体运输时全部289成员逐 SHA 核后，只保所需七件。R837 的127个所选 V2 项逐项与原 free-basis 的 R786 source spec 匹配，不只对下标。

原 V1 值已经带 $82^2$，原 V2 值已经带 $82^4$。本次只依次形成 $e_i(P_0)/\tau(P_0)$ 或 $V_{2,d_j}(P_0)/\tau(P_0)^2$，没有再施82尺度。另一图用原 $v_0^{\epsilon_i}\beta_i(P_0)$ 运输。原 cusp 核、Fourier、秩、primitive 和已成原 P0 值不重算；新运算仅为上述准确比值、评价及固定理想列。

## 3. 完整性证明

在任一图记 $R$ 为原坐标环，$x$ 为其基变量，$x_0=x(P_0)$。设原正规基为 $e_0=1,e_1,\ldots,e_{271}$，$b_i=e_i(P_0)$。评价 $R\to K$ 是 $K$ 代数满射。

原点理想的以下272列完整：
$$
G_0=(x-x_0)e_0,\qquad G_i=e_i-b_i e_0\quad(1\le i\le271).
\tag{R856.1}
$$
所有列评价零。若 $\sum_i a_i(x)e_i$ 评价零，先减去 $\sum_{i>0}a_i(x)G_i$，余项为
$\bigl(a_0(x)+\sum_{i>0}a_i(x)b_i\bigr)e_0$；
其系数在 $x_0$ 为零，故被 $x-x_0$ 整除。这同时证明完整生成和线性独立；其行列式为 $x-x_0$，余长1。

令 $C_0,\ldots,C_{271}$ 为同图 R820 **已经准确完成的完整** cusp 基，$r_i=C_i(P_0)$。本次实际计算给 $r_0\ne0$，并核了 $r_0^{-1}$ 和全部 $r_i/r_0$ 的准确乘回。因此
$$
H_0=(x-x_0)C_0,\qquad
H_i=C_i-\frac{r_i}{r_0}C_0\quad(1\le i\le271)
\tag{R856.2}
$$
都在 $\mathscr C\cap\mathfrak m_{P_0}$ 内。

若 $\sum_i a_i(x)C_i$ 在 $P_0$ 为零，减去所有 $i>0$ 的 $a_iH_i$ 后，余下
$$
\left(a_0(x)+\sum_{i>0}a_i(x)\frac{r_i}{r_0}\right)C_0.
$$
括号在 $x_0$ 的值为零，故它是 $x-x_0$ 的倍数。于是 (R856.2) 正是完整交理想基。它与原 $C$ 基间的变换行列式为 $x-x_0$，因此
$$
\det H=(x-x_0)\det C=(x-x_0)P_{20}(x).
\tag{R856.3}
$$
不存在另一个272阶行列式或 Hermite 求解假设。

$r_0\ne0$ 也给
$$
1=\frac{C_0}{r_0}+\left(1-\frac{C_0}{r_0}\right)
\in\mathscr C+\mathfrak m_{P_0}.
$$
两个理想互素，故其交等于积。两图使用同一原 $\mathscr C$ 和同一原 $P_0$，并有已核的272个值的准确重叠运输，故以上基给同一全局固定支撑理想。无需主张两图基逐列相同。证明完成。

实际 core 对每条新列核 P0 评价为零、原列准确乘回；pivot列另核所有逐系数线性因子递推。全部列包含在输出中，完整性由上述多项式除法和原完整 $C$ 基证明，而非由有限域秩或预计余长替代。

## 4. 可重现的公开计算记录

脚本为 [core](../scripts/R856_original_fixed_branch_ideal_bases.py) 和 [公开 wrapper](../scripts/R856_original_fixed_branch_ideal_bases_public.py)，参数为 [实际 request](../notes/R856-fixed-branch-ideal-bases-public-request.json)。

| 项目 | SHA256 |
|---|---|
| core | 80c4e508cd0ddc15bcc3f8a5b3a4053ce141233fd3d259c1bcf0935db6a6311b |
| wrapper | 3b722b5bd794913d78c06351a66b795b293634f0043ef7d9e4bee5c44e6c58aa |
| request | 5d18d1d06a183544de71697b2e23a577bb0df31a5b3a4e2587b1b2335e171fc0 |
| workflow | c834e7635f47813331ab985325437cf146d79cb8d76eaf2e91afbd2e696e9ae2 |
| 成功 FINAL，6533字节 | a80fb42e807e0368e6249a56901ef5f391bb5b2326b5f3f29372fcc6866b4383 |
| stage manifest，4212字节/42阶段 | ce02bb694664cd3b0bcec8eb6035ece638a80515bb4741405bdc7274ab2846ca |
| core receipt | 4cc7648c178eb236b8bd4c75a365a51a09fad758839f24150a5d4b8bc953dc95 |
| 原来源 inventory，115028字节 | df1c712d4e5caec933cc1e46ff7a56e35972d541edd1fd8873de2d51a5f56f38 |
| 必要569件原来源载体，13406926字节 | fd6329bd17f2d729a3c3834e78fe7b4b626be84b692e77d0e51bbdf205f01e41 |

该公开 [run](https://github.com/Rogerhu12/math-research-public/actions/runs/43805659598) 的 core、完整输出 IO 和来源核均成功，2026-11-16 04:43:01.780919 UTC 完成。预算300分钟、resume=null；成功只用29.23秒原数学时间，不把预算记作计算时长。

输出 artifact **14198217155**：
serre-global-R856-original-fixed-branch-ideal-bases-43805659598-1，
47,922,521字节，平台 ZIP digest
125c93efac847e7b14ba8a256897f6e6c362b3fd060a87bc5befd43ba38b7c25，
到期2026-11-17 04:43:02 UTC。full manifest 含52个产物；全部机器输出和可重算数据不进 Git/Release，必要输入与断点只保一日 artifact。

## 5. 接续范围

本次完整固定支撑基可直接供原有限 RR membership 及后继固定点理想幂，不必再重求原 cusp 核。原 [R856 方法 §5](../notes/R856-original-fixed-branch-ideal-and-three-scalar-pole-source.md) 对同一 canonical $f=B/\tau^5$ 的三标量理想 $(f,\delta f,\delta^2f)$，仍需实际原 $B$ 及导数坐标才进入后续计算；该部分沿原 $K\to L$ 扩张，不能用本次 $K$ 固定支撑块冒充。

本结果没有给出 R854 的41进响应、一个 $Z$、原 $\eta$ 或指定高度多项式的非零性；不改变 README 的全 $p$ 完成标准。
