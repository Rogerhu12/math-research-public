# R787：原五次截面的一条 $L$ 函数关系——共同主元、Dixon 提升与完整准确认证

日期：2026-11-15。状态：**本篇固定实际求解方法；只有公开 Actions 完成全部准确代回后，才登记原函数已经恢复。**  
核心：[R787_original_power5_relation_solver.py](../scripts/R787_original_power5_relation_solver.py)。

本任务保持原第4号映射、次数1206、原 $b$、原微分、原尖点相位和零平移。
准确输入是已经成功的 R786 五次基与 R781 Laurent 前缀。
不重新选择原映射，不重跑周期、整格、SVP、Eisenstein 基或 Laurent 递推。
原 $p=41$ 有理点分类已经完成，也不在本任务中重复。

## 1. 固定的准确关系与输入

采用 [R786](../results/R786-original-power5-sections-and-129-Laurent-recovery.md) 的全部约定：
$$
V_5=H^0(Y_L,5(K_Y+\mathcal D)),\quad
\dim_LV_5=1234,\quad
\deg(5(K_Y+\mathcal D))=1360.
$$
$L=\mathbb Q(b,s)$，$s^2=-3$；写 $B_{\rm fld}=\lambda b$，保留 R781 的同一个整化因子 $\lambda$。
为了避免与分母截面混淆，本篇将字段生成元写为 $B_{\rm fld}$，
分母截面仍写为 $B$。
核心的坐标次序是
$$
B_{\rm fld}^{\,i}s^j,\quad j=0,1\text{ 为外层},\ i=0,\ldots,6;
\qquad t=\xi_{41}+\xi_{41}^{-1}.
$$
未知数保留原 $L$ 的全部14个有理坐标，没有先缩小到 $K$ 或 $\mathbb Q$。

R786 给原顺序的1234个截面 $F_j$，
并给 $82^{10}F_j$ 在 $u$ 下至128阶的准确整数 cyclotomic 系数。
由 R786 的权十下降，
$$
u=\xi^{10}v,\qquad
82^{10}F_j=\sum_{n=0}^{128}f_{n,j}(t)v^n+O(v^{129}),
\qquad f_{n,j}\in\mathbb Z[t]/(g_t).
\tag{787.1}
$$
核心逐条原基、逐阶乘 $\xi^{10n}$，检查原反演相等，再作整数 Chebyshev 转换。
不以平均制造不变性。
这产生整数矩阵
$$
F\in\operatorname{Mat}_{2580\times1234}(\mathbb Z),
$$
其中行按 $n=0,\ldots,128$、$t^r$ 的 $r=0,\ldots,19$ 排列。

R781 已有 $R_0,\ldots,R_{142}$、$\kappa^0,\ldots,\kappa^{142}$。
这里只消费 $R_0,\ldots,R_{128}$ 和 $\kappa^0,\ldots,\kappa^{129}$，
同时校验原阶段的前项 SHA 链。
对分子与分母的展开 $A_n,B_n$，最终必须全部验证
$$
\mathcal E_m=
246^3\kappa^{m+1}A_{m-1}
+\sum_{j=0}^{m}R_{m-j}\kappa^jB_j=0,
\qquad 0\le m\le128,
\tag{787.2}
$$
其中 $A_{-1}=0$。
每条等式在 $M^+=L(t)$ 中有20个 $L$ 坐标、280个 $\mathbb Q$ 坐标。
$m=0$ 恰为 $B_0=0$。

R786 已证明这129条完整关系等价于原全球恒等式 $A=yB$。
任何非零核向量均有 $B\ne0$。
因此本任务只需一条准确关系，不要求先产生全部 $28+h^1$ 维核。

### 原生产者绑定

| 输入 | 实际 run／source | 完整输出 manifest SHA256 |
|---|---|---|
| R781 | 43679703344／f0292795817a534937d35904e2e11275631e878d | ce0554fab03fda8d124e9e0ee338335bca6f7b39ee8499550bbec36358a1a7fd |
| R786 | 43682100611／dd262672a8b1e2af82277b15e0fa766038609670 | e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a |

R781 完整证书 SHA 为
b9e1a2282d6fc0de12df401abbc3014ded525757c7102d11967f0bd33a40f3f0；
R786 完整证书 SHA 为
dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9。
R786 基索引 SHA 为
0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35。

包装层核实际 GitHub run/source、success、ZIP digest；
核心再核 manifest、完整证书、原 core SHA、每个消费文件的字节数/SHA，
以及全部阶段的 complete 和同一个 configuration。
R775 预算失败的未完成部分和 R777 均不作为本任务输入。

## 2. 仅有理常数块作小规模准确消元

记 $E_0$ 为 $F$ 的前20行。
R786 已证明 $\operatorname{rank}_{\mathbb Q}E_0=20$。
选择在辅助素数下可逆的20列 $P$，其余1214列记为 $Q$。
准确求
$$
E_P^{-1}E_Q=U/d,\qquad U\in\operatorname{Mat}_{20\times1214}(\mathbb Z),\quad d>0,
$$
并使用整数核矩阵
$$
Z'_P=-U,\qquad Z'_Q=dI_{1214}.
\tag{787.3}
$$
核心在特征零逐项检查
$$
E_0Z'=0.
$$
因 $d\ne0$，$Z'$ 仍给整个 $L$ 核；以后写 $\mathbf b=Z'\mathbf c$。
$Z'$ 只有20个稠密行，其余是一个对角块，所以不必在提升中存取1234阶的稠密核矩阵。

分子块只需 $F$ 的前2560行，记为 $F_A$。
R786 已证明前69阶的1380个坐标对 $V_5$ 单射。
在这些原行中选择1234行 $J$，其余1326行记为 $R$，置
$$
F_0=F_A[J].
$$
**不在 $\mathbb Q$ 上求1234阶的 $F_0^{-1}$。**
只保存原整数块、一个已证非零的模素数 minor 和其模素数逆。

合法约化下先形成原 $y$ 的有限前缀：
$$
Y(v)=vy(v)=
-\frac1{246^3}\sum_{m=0}^{128}R_m\kappa^{-(m+1)}v^m.
\tag{787.4}
$$
设 $C$ 为从 $\mathbf c$ 到 $y\sum_j(Z'\mathbf c)_jF_j$ 的
$v^0,\ldots,v^{127}$ 二十坐标矩阵。
未清行关系是
$$
F_A\mathbf a-C\mathbf c=0.
$$
Schur 矩阵
$$
S=C[R]-F_A[R]F_0^{-1}C[J]
\in\operatorname{Mat}_{1326\times1214}(L)
\tag{787.5}
$$
只在合法辅助素数下实际形成。
结构界 $\operatorname{rank}_L S\le1186$ 来自 R786；
实际模秩由运行计算，不设为1186。

## 3. 十四个分裂分支使用同一组未知坐标

公开 Actions 从请求的起始整数扫描素数 $\ell$。
必须实际检查：

- $\ell$ 是素数，全部已消费的有理尺度分母以及 $246\lambda$ 都是单位；
- 原 $B_{\rm fld}$ 的整系数七次多项式模 $\ell$ 有七个互异单根；
- $s^2+3$ 模 $\ell$ 有两个互异单根；
- 14行评价矩阵
  $V_{(b_0,s_0),(i,j)}=b_0^is_0^j$ 可逆；
- 每个分支的 $\kappa$ 在 $\mathbb F_\ell[t]/(g_t)$ 中可逆；
- 原 $E_P$、$F_0$ 的约化可逆。

不要求 $g_t$ 完全分裂。
$\kappa$ 的单位性直接由多项式扩展 Euclid 关系检查。
所有求逆矩阵的模数都是已经证明的素数。

先在第一个分支取得实际 Schur 秩 $r$、
原主元行 $I$、原主元列 $P_S$。
然后所有14个分支必须使用**同一个** $I,P_S$，
并分别检查该 $r\times r$ minor 可逆、实际秩仍为 $r$。
任何失败都拒绝这个辅助素数，另选素数。
选择同一个非主元列 $f$，在所有分支都固定
$$
c_f=1,\qquad c_j=0\quad
(j\notin P_S\cup\{f\}).
\tag{787.6}
$$
由同一 minor 求出其余 $c_j$，再求 $\mathbf a$，
并检查分支的全部2560个未清行关系。

这条共同归一化不可省略。
若各分支各自选自由列，所拼合的对象通常只在
$L\otimes\mathbb Q_\ell$ 中定义，未必来自一个 $L$ 向量。
本实现用共同坐标约束与共同自由值；
14个分支只用于在模 $\ell$ 上快速表示同一个原 $L$ 线性系统。

若实际 $r=1186$，该非零模 minor 与已证上界合起来确给
$\operatorname{rank}_L S=1186$。
若 $r<1186$，代码仅记录这个实际模秩，不据此宣称特征零秩或 $h^1$。
后面的逐步完整残差和最终准确认证仍可尝试产生一条真关系。

## 4. 在原整数系数域中作 Dixon 提升

提升工作在
$$
\mathcal O_k=
(\mathbb Z/\ell^k\mathbb Z)[B_{\rm fld},s]/
(f_B,s^2+3)
$$
的固定14坐标表示中进行。
不提升14个根，也不在复合模数下调用矩阵 inverse、solve、rank 或 rref。
只使用整数矩阵乘法、环上的加乘、首一多项式约化和已证单位的标量有理分母。

设当前 $(\mathbf a_k,\mathbf c_k)$ 的 (787.2) 全部坐标模 $\ell^k$ 为零，
且一直保持 (787.6)。
在模 $\ell^{k+1}$ 下算完整残差 $\mathcal E$，
逐坐标核 $\ell^k\mid\mathcal E$，置
$$
\rho=\mathcal E/\ell^k\pmod\ell.
$$
在每个分支乘
$(246^3\kappa^{m+1})^{-1}$，
将 $m=1,\ldots,128$ 的清行残差转回未清行右端
$u=-\rho/(246^3\kappa^{m+1})$。

自由坐标的修正设为零。
记 $u_J$ 与 $u_{R[I]}$ 为所选原行，
则主元修正满足
$$
\delta c_{P_S}
=S[I,P_S]^{-1}
\left(F_A[R[I]]F_0^{-1}u_J-u_{R[I]}\right),
\tag{787.7}
$$
$$
\delta a
=F_0^{-1}\left(u_J+C[J,P_S]\delta c_{P_S}\right).
\tag{787.8}
$$
全部逆矩阵都是已保存的模 $\ell$ 逆。
用 $V^{-1}$ 将14个分支的修正还原为同一个原 $L$ 的14坐标。

仅满足选定行不足以通过。
核心另外用原式 (787.2) 计算修正的完整模 $\ell$ 残差
$\mathcal D(\delta a,Z'\delta c)$，
要求所有 $129\cdot280$ 个有理坐标均满足
$$
\rho+\mathcal D(\delta a,Z'\delta c)=0\pmod\ell.
\tag{787.9}
$$
由原式的线性性，
$$
(\mathbf a_{k+1},\mathbf c_{k+1})
=(\mathbf a_k,\mathbf c_k)+\ell^k(\delta a,\delta c)
$$
就在全部原式上模 $\ell^{k+1}$ 为零。
这给每一个完成 checkpoint 的严格归纳认证。
若共同 minor 不能提升整个系统，拒绝该素数，不把不相容的候选写成准确关系。

### 保持实际运算规模

分子和分母的截面展开由原整数 $F$ 乘14列未知坐标完成。
分母先按 (787.3) 的20个稠密行加对角块恢复，避免形成巨大有理矩阵。

在 $M^+$ 中，沿用 R781 的编码
$$
t^rB_{\rm fld}^is^j\longmapsto X^{r+39i+507j}.
$$
两个约化元素相乘的最高编码指数不超过1520。
因此将第 $n$ 个 $v$ 系数放到 $X^{1521n}$ 的块内，
一次截断多项式乘法就得到所需的级数卷积；
随后逐块按 $s^2=-3$、原 $f_B$ 与 $g_t$ 首一约化。
1521的间隔确保不同 $v$ 阶没有进位混淆。
这里只优化相同的原式，不改变字段或范数。

## 5. 有理重构只生成候选；准确代回才完成

每隔请求指定的提升位数，尝试对全部未知的原14坐标作有理重构。
用扩展 Euclid 给候选 $a/b$，检查
$$
a\equiv xb\pmod{\ell^k},\quad
\gcd(a,b)=1,\quad b>0,\quad
|a|,b\le\left\lfloor\sqrt{\ell^k/2}\right\rfloor.
$$
任一坐标不能重构就继续提升。
全部坐标可重构仍只是候选。

为得到紧凑的原函数 recipe，
同时清掉 $\mathbf a,\mathbf c$ 的公共有理分母，
按准确整数 $Z'$ 求 $\mathbf b$，
再去掉 $(\mathbf a,\mathbf b)$ 的共同整数内容。
于是最终系数均是原 $L$ 基上的整数向量。
分子分母同时缩放，故比值不变；
两侧原 $82^{10}$ 基尺度也同时保留并抵消。
自由坐标原来等于1以及 $Z'$ 的单射性确保 $\mathbf b\ne0$。

随后直接使用 R781 的原特征零 Field 运算：

1. 从原 $F$ 和这批准确整数系数取得所有 $A_n,B_n$；
2. 准确形成 $\kappa^jB_j$，每项完成后保存；
3. 对 $m=0,\ldots,128$，逐条在280维有理字段中算 (787.2)；
4. 只有该条全部坐标准确为零，才写相应完成阶段；
5. 全129条通过且 $B\ne0$ 后，才写完整证书与原 $y=A/B$ recipe。

每条验证绑定同一个候选文件 SHA。
在预算后续接时只复用 complete、同配置及同候选 SHA 的阶段。
某候选的第一条非零原式使其被拒；不会因更多模位数或预期秩而忽略残差。

这一步与 R786 的全球截断证明合起来认证**原来的** $y$，
不是一个数值拟合的近似函数。
完整核、$\beta=\phi_y(c_1)$、第二类周期、Poincaré 求值和高度并不由它自动给出。
取得真实函数后，仍须用原 CM 点与原框架评价接续 $\beta$。
原椭圆曲线的另一个函数可由已经固定的原微分及 $y$ 的全球关系接续，
但本任务的成功字段只声明实际算出的 $y$。

## 6. 命令行、检查点与输出边界

核心参数：

~~~sh
python scripts/R787_original_power5_relation_solver.py \
  --config REQUEST \
  --proof results/R786-original-power5-sections-and-129-Laurent-recovery.md \
  --method notes/R787-original-power5-relation-solver-method.md \
  --field-core scripts/R781_original_Laurent_prefix.py \
  --retained INPUT_ROOT --output OUTPUT --budget-minutes 300
~~~

输入目录为 INPUT_ROOT/R781 与 INPUT_ROOT/R786。
配置绑定原 proof/method/core SHA、两个实际 producer、
辅助素数搜索起点和重构间隔。
时间预算不改变数学配置，已完成阶段可按相同配置续接。

主要临时阶段包括原实基逐行、每素数的有理块/共同 chart、
各分支的模逆、Dixon checkpoint、候选准确加权分母及每一条准确验证。
分支完成后，已被其模逆和初值替代的卷积列块可删除。
拒绝素数的矩阵只留拒绝原因，不持久保存可重算的大表。

最终证书文件为
p41-original-power5-function-relation-certificate.json。
它必须明确：

- exact_nonzero_A_B_relation_verified=true、original_full_L_retained=true；
- 原映射 index4、degree1206，129阶与全部20个 $L$ 坐标准确通过；
- actual_y_map_recovered=true，beta_or_height_computed=false；
- 实际辅助素数、实际模 Schur 秩、实际提升位数；
- 原函数 recipe 与全部完成阶段的文件名、字节数及 SHA。

只要预算耗尽或任一必要准确条件未通过，完整证书就不存在，
receipt 保持 complete=false，保留已完成检查点供立即续接。
这些中间数据只用一日临时 artifact 转交当前活跃计算；
原生产者输入可一并随该活跃 checkpoint 传输，以免其原 artifact 过期导致重算。
所有可重算系数表、矩阵、完整证书和原始日志均不入 Git 或 Release。
仓库只保存脚本、参数、run、SHA 与小结果摘要。

## 依据

- R786（2026）：原五次空间、权十相位、129条全球注入、$B_0$ 与分子块消元。
- R781（2026）：原280维字段、无逆 Laurent 阶段与全部清行关系。
- J. D. Dixon，*Exact solution of linear equations using p-adic expansions*，
  **Numerische Mathematik 40**（1982），137–141，
  [DOI:10.1007/BF01459082](https://link.springer.com/article/10.1007/BF01459082)。
  本篇 (787.7)–(787.9) 已直接证明所用提升步骤及全残差归纳条件。
- python-flint 0.9.0 官方文档（本次查阅2026）：
  [整数](https://python-flint.readthedocs.io/en/latest/fmpz.html)、
  [nmod 矩阵](https://python-flint.readthedocs.io/en/latest/nmod_mat.html)、
  [fmpz_mod 矩阵](https://python-flint.readthedocs.io/en/latest/fmpz_mod_mat.html)、
  [有理矩阵](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html)、
  [nmod 多项式](https://python-flint.readthedocs.io/en/latest/nmod_poly.html)、
  [fmpz_mod 多项式](https://python-flint.readthedocs.io/en/latest/fmpz_mod_poly.html)。
  其中逆矩阵、solve、rank、rref 的素数前提被显式保留；
  复合模提升只使用环运算和首一约化。

