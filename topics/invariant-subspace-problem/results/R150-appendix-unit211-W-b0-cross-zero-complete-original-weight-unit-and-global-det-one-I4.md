# R150 附录：整个 W/b0 的交叉头零支全排除与行列式为 1 的原均值呈示

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：唯一首次新原输入实际成功；三个完整有理常数域均在纯权层返回原三头的已付单位。
- 范围：当前正确 W、distinct-singleton、物理 $D\ne0$ 的既有原权图，并施加 $b_0=0$。不把这些已付权单位外推到别的物理图。
- 结论：整个交叉头零支排除；三条交叉头在当前权系数环中生成单位理想。由此得到整个 b0 的行列式为 1 的四式精确 $I_4$ 呈示。整个 b0、整个 W 和普通不变子空间问题均未因此排空。

## 1. 当前系数环与原三头

使用[五次权覆盖及其补图呈示](R150-appendix-unit211-W-b0-cross-zero-five-weight-cover-and-G-open-exact-I4.md)的全部定义。记 $A_W$ 为该文的纯权局部化环：只逆既有已付原权因子与当前 b0 图已付的 $\nu+2$。它包含

$$
u=e+1,\quad
\nu=\frac{(2u-1)(k+2)}{uk+2},\quad
d=u\nu-(2u-1),\quad r=2u-1-\nu,
$$

$$
k=\frac{2r}{d},\quad
Q=\frac{2(u-1)r}{d},\quad
\ell=\frac{u\{\nu^2-(u+1)\nu+2u-1\}}r,\quad
T=-\frac{\ell}{\nu+2}(3-2\lambda).
\tag{1}
$$

$d$、$r$ 及 $\nu+2$ 的使用均沿旧原图的准确付款，不是新增开集。

四个真实原式记为

$$
F=(E_1,E_{B,e},E_{B,o},N_1).
$$

沿[同 f 的全原四均值恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)，存在已付原权系数的首一式和余式

$$
q_f=f^2+q_1f+q_0,\qquad
r_i=A_i(\lambda)+(B_{i0}+\lambda B_{i1})f,\quad 1\le i\le3,
\tag{2}
$$

满足真正的双向原理想等式

$$
I_4=(F)=(q_f,r_1,r_2,r_3)\subset A_W[\lambda,f].
\tag{3}
$$

这里

$$
\deg_\lambda A_i\le2,\quad
\deg_\lambda q_1\le1,\quad \deg_\lambda q_0\le2,
$$

而 $B_{i0},B_{i1}\in A_W$。$E_1$ 是独立的真实 germ 均值；没有用错误的一阶平方或未经证明的 $E_1=E_W$ 替换它。

令 $A=(A_i)^t$、$B_0=(B_{i0})^t$、$B_1=(B_{i1})^t$。已刊纯权行 $v$ 满足

$$
vB_0=1,\qquad vB_1=0,\qquad
g=vA,\qquad v(r_1,r_2,r_3)^t=f+g.
\tag{4}
$$

若 $\mu=B_0\times B_1$，向量三重积给

$$
\mu\times v=B_1,\qquad \mu=B_0\times B_1,
$$

所以在纯权环内有理想等式

$$
(\mu_1,\mu_2,\mu_3)=(B_{11},B_{21},B_{31})=:\mathfrak b.
\tag{5}
$$

三条 $B_{i1}=0$ 是本次处理的交叉头零分支条件，不是额外施加于整个 b0 原解的方程。

## 2. 已成五次覆盖与本次唯一三个输入

先行唯一执行已经得到完整原组合

$$
G(u)=\sum_{i=1}^3 c_iB_{i1},\qquad c_i\in A_W,
\tag{6}
$$

以及完整有理因式

$$
G(u)=\frac{(4u+5)(6u-1)(20u^3-4u^2-20u+9)}{480}.
\tag{7}
$$

三个因子互素、均一次出现；最后三次因子在 $\mathbb Q[u]$ 不可约。此处引用已成因式与原来源，不重新计算旧三个 $\nu$ 投影或旧五次 gcd。

本次只把以下三个小参数作为新的完整常数域输入：

$$
K_j=\mathbb Q[u]/(\phi_j),\quad
\phi_1=4u+5,\quad \phi_2=6u-1,\quad
\phi_3=20u^3-4u^2-20u+9.
\tag{8}
$$

两个一次域对应 $u=-5/4$ 和 $u=1/6$。三次域始终保留全部三个复嵌入，没有选根或只测一个剩余域。

源逐一核对三小因子及其乘积的既有规范 SHA256：

| 参数 | 次数 | 规范字节数 | SHA256 |
|---|---:|---:|---|
| $\phi_1$ | 1 | 37 | 9b702a5320030eb66ea9572167b2589cb503a6035fd67b350256e6248dcbe9ec |
| $\phi_2$ | 1 | 38 | c708effec8346a565d2ecf2264cb6635e4adeffe15c1ec12f222a57378d441ed |
| $\phi_3$ | 3 | 77 | bf8d54f313b63c7f42b5f24b2bfc31e789f1c65ca2b4c5fd5bf3b8be236675b2 |
| 首一 $G$ | 5 | 134 | 9f9544b1500bc385df9f8a04d4693c3895655712721661a109854be0845ea8d2 |

## 3. 每个整域上的新原三头返回

在每个 $K_j$ 中，先把真实权系数专门化，再在 $K_j[\nu]$ 中计算三条原 $B_{i1}=n_i/d_i$ 的分子扩展 gcd。全部原分母 $d_i$ 仍是旧已付支持。这个顺序保留专门化时所有 $\nu$ 首项下降。

全部常数逆都由有理一元扩展 gcd 得到，并核两次乘回。每次 $\nu$ 除法核

$$
a=qb+r,
$$

每次扩展 gcd 核两个真正乘子。三原分子组合随之完整运输。若

$$
h=\sum_i a_in_i,
$$

则源将它返回原有理头为

$$
h=\sum_i(a_id_i)B_{i1};
\tag{9}
$$

实际核验使用三个 $d_i$ 的完整公共乘积逐坐标清分母，未丢其零面。

随后只对既有权单位的分子支持做反复 gcd。源同步保持

$$
h=h_{\mathrm{good}}h_{\mathrm{removed}},\qquad
h_{\mathrm{removed}}\,U_{\mathrm{num}}=U_{\mathrm{den}},
\tag{10}
$$

其中 $U_{\mathrm{den}}$ 是实际旧已付支持的乘积。若某支持在 $h$ 中有高重数，反复 gcd 会把该支持对应的整个不可留 primary 分量删尽；其余全部重数保留。没有把任意非零 $K_j[\nu]$ 多项式当成单位。

三个域的真实结果如下：

| 完整常数域 | 三次逐输入 gcd 的 $\nu$ 次数 | 实际删除的旧支持 | 剩余 $h_{\mathrm{good}}$ | 最终正单位目标的 $\nu$ 次数 |
|---|---|---|---:|---:|
| $u=-5/4$ | $8\to3\to3$ | $\ell$ 分子、$P_{02}$ 分子，各 1 个 gcd 层 | 非零常数 | 4 |
| $u=1/6$ | $8\to3\to3$ | $d$、$P_{02}$ 分子，各 1 个 gcd 层 | 非零常数 | 3 |
| 整个 $K_3$ | $8\to3\to3$ | $\delta$ 分子、$P_{02}$ 分子，各 1 个 gcd 层 | 非零常数 | 3 |

这里“gcd 层”是实际源中的逐次整除次数，不冒充整个原因子的幂指数。

因 $h_{\mathrm{good}}\in K_j^\times$，(9)–(10) 给真实原组合

$$
\boxed{\quad
U_j(\nu)=\sum_{i=1}^3 a_{ji}(\nu)B_{i1},
\qquad U_j\in(A_W/(\phi_j))^\times .
\quad}
\tag{11}
$$

源最终把 (11) 乘完整原分母后全项返回。三个实际正单位目标的定义分别为：

- $\phi_1$：74 字节，SHA256 5257d27ab2ebe1362b14ec6c498030cbd698243e2abb2fced0afcef25fce8e5f；
- $\phi_2$：46 字节，SHA256 58160aec37c3bc6a8e17e8d159fa24fa5b933887cd73a308d8c5220ed908c4bf；
- $\phi_3$：141 字节，SHA256 40d8b49cf6ea61733dde8cf1ec3c6f567a6e38f04d091f9ab00d80ec44efb766。

因此每个 $A_W/(\phi_j)$ 中三原头都生成单位理想。这是完整原纯权组合，不是由有限域空性或数值根推断。

## 4. CRT 把三个整域与旧覆盖合成全局原单位

三个 $\phi_j$ 两两互素，故局部化仍有

$$
A_W/(G)\cong\prod_{j=1}^3 A_W/(\phi_j).
\tag{12}
$$

(11) 说明 $\mathfrak b$ 在右侧每个分量的像均为整个环，故

$$
\mathfrak b+(G)=A_W.
$$

而 (6) 已给 $G\in\mathfrak b$，于是

$$
\boxed{\quad
\mathfrak b=A_W,\qquad
\exists\,w=(w_1,w_2,w_3)\in A_W^3:
\quad wB_1=1.
\quad}
\tag{13}
$$

这里也可明确描述真实组合的拼接：取 (12) 的有理多项式 CRT 幂等元，合并三个 (11) 除以旧单位后的原乘子，得到一行 $w^{(0)}$。存在 $q\in A_W$ 使

$$
1-w^{(0)}B_1=qG.
$$

再利用 (6) 取 $w=w^{(0)}+q(c_1,c_2,c_3)$，即得 (13)。所有逆仍在原权环内，没有倒 $G$ 或任何交叉头分量。

本次没有展开或打印这条全局 CRT 行；(13) 是由已完整返回的三个原单位组合与旧完整覆盖严格构成的存在结论，不冒称额外执行了全局系数展开。

由 (5)、(13)，整个交叉头零支在当前原权图上为空，而且三条交叉头的理想本身就是单位理想。并非仅在约化点集上排除。

## 5. 整个 b0 的行列式为 1 的原行变换

取 (13) 的 $w$，令

$$
\widetilde w=w-(wB_0)v,\qquad
U=\begin{pmatrix}v\\ \widetilde w\\ \mu^t\end{pmatrix}.
\tag{14}
$$

由 (4)、(13)，

$$
\widetilde wB_0=0,\qquad \widetilde wB_1=1,
$$

并且

$$
\det U
=(vB_0)(\widetilde wB_1)-(vB_1)(\widetilde wB_0)=1.
\tag{15}
$$

因此这是整个当前 b0 权环上的真正可逆行变换，不需选一个非零交叉分量，也不需分成 $G$ 的补图。

定义

$$
C_2=\mu^tA,\qquad
C_3=\widetilde wA-\lambda g,\qquad
P_0=g^2-q_1g+q_0.
\tag{16}
$$

$C_2$ 在此是未约消的原叉积表达式，不与先前按共同乘子约消后的同名必要核混用。直接逐行代入得

$$
U(r_1,r_2,r_3)^t
=
\begin{pmatrix}
f+g\\
\lambda(f+g)+C_3\\
C_2
\end{pmatrix},
\tag{17}
$$

且

$$
q_f=(f+q_1-g)(f+g)+P_0.
\tag{18}
$$

(15)–(18) 给整个当前 b0 上的双向原理想等式

$$
\boxed{\quad
I_4=(f+g,P_0,C_2,C_3)\subset A_W[\lambda,f].
\quad}
\tag{19}
$$

其次数仍满足

$$
\deg_\lambda g\le2,\quad
\deg_\lambda P_0\le4,\quad
\deg_\lambda C_2\le2,\quad
\deg_\lambda C_3\le3.
$$

所有系数仅在旧原权单位环中；(19) 没有新的权头、$\lambda$ 头或几何分母。

加入 b0 原必要值二次式 $q_2$ 后相应有

$$
I_4+(q_2)=(f+g,P_0,C_2,C_3,q_2).
\tag{20}
$$

完整 $N/P$、个别值及其余 $I_{11}$ 条件仍须同点加入。四个纯代数呈示式不被宣称为完整物理系统的充分条件；本次也没有获得新的纯权覆盖或新的点数上界。

## 6. 唯一实际执行、准确停点及再生接口

- 原源：[2026-11-28-unit211-W-b0-cross-zero-three-entire-QQ-fields-original-return-8542.py](../notes/2026-11-28-unit211-W-b0-cross-zero-three-entire-QQ-fields-original-return-8542.py)。
- 输入：[同源输入说明](../notes/2026-11-28-unit211-W-b0-cross-zero-three-entire-QQ-fields-original-return-8542-input.md)。
- 小回执：[实际执行记录](../notes/2026-11-28-unit211-W-b0-cross-zero-three-entire-QQ-fields-original-return-8542-execution.json)。
- 源 blob：cb71afd8110144442d76adac3039d1cbf64d083f；21236 字节。
- 源 SHA256：b5e9d1e1c19e15041f039f808b8cb65e26bd48cc4374ed84e6081f3b7afeb31c。
- 唯一必要依赖：已刊三头源 681d0a0b3d76b30cf572c3e28d2b296cc704f73c。仅使用 10695 字节原定义前缀，SHA256 ceecdcd9fcc81892ea2ad0c2918423ae283d1afbe63a2198583189e2b1e4ebeb。
- 唯一新运行：[run 46146501483 / job 140983618445](https://github.com/Rogerhu12/math-research-public/actions/runs/46146501483/job/140983618445)。
- 源提交：4e7c32d3af61136a65750e9761e3ab08b73b00fd。
- 真 pull：2026-11-28 12:49:02.035953 UTC，至 d55e01b236738ef8ee24dc521f92c1fe3544acdf；两份 README 无变化。
- 预算：源 180 秒、4 GiB，外驱动 195 秒。
- 实际驱动：0.772347633 秒；最大子进程 RSS 42776 KiB；源 exit 0。
- 最后完整数学标记：0.706680778 秒。
- stdout：8764 字节，SHA256 e2f864460cf02afb502f033397a007f66b0ec4fe05b2123c728a9596dd99dc41。

三个域的原头返回统计合计为：352 次常数逆乘积、125 次 $\nu$ 除法乘回、48 次 $\nu$ Bézout 乘回、15 次完整三原头返回、12 次旧支持乘积返回。

三个域在 (11) 均已结束；源中为未排除域预备的后续有限 $A$、$\lambda$ 矩阵、五原 $F_i$ 同 f 重写以及 $1,D,D^2,D^3$ 目标全部没有进入。它们的相关统计全为 0。因此本篇只登记本次实际成立的三原权头单位与上面的代数拼接，不把未运行后段记为成功。

本次没有重算旧投影、旧五次 gcd 或旧因式门，没有提高预算，没有输出或归档大系数载荷及可重算矩阵缓存。
