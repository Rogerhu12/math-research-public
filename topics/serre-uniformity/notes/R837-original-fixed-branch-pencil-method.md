# R837：原 P1 到 P0 的准确反射评价与固定21点铅笔

日期：2026-11-15。状态：完整证明与执行契约；尚未预填新的 P0 值、固定21点空间或铅笔秩。

本稿执行 R836 的固定 $\mathcal B=\mathcal D_{\rm cusp}+P_0$ 小输入。全部新算术仅在公开仓库 Actions。原 R790 的146个 P1 值及 R786 的旧权1、2、3前缀原字节复用，不再计算挠点、域迹、CM 变形或旧 Fourier 系数。

## 1. 反射是原几何作用，没有第二次 CM 相位

按 R767/R802，整数矩阵
$$
T^{41}=\begin{pmatrix}1&41\\0&1\end{pmatrix}
\tag{A1}
$$
在 mod41 为恒等、在 mod2 为 transposition，正规化原 level82 群。经原 $\theta$ 运输，它给 $Y_K$ 上的同一 involution $\iota$，并且
$$
\iota^*t_Y=1-t_Y,\qquad \iota(P_1)=P_0,\qquad
q_Y\longmapsto-q_Y.
\tag{A2}
$$
它不是把原全局算术共轭误当成逐系数共轭。R802 已分别保留 $c_0$ 与 $\iota$；本稿只用几何 $\iota$。

所有原偶权的 automorphy factor 在(A1)下为1。$E_4,E_6$ 均对该整数平移不变，故对原普通权2截面 $F_i=82^2T_i$，
$$
\Phi_i=F_iE_6/E_4^2,\qquad
\Phi_i(P_0)=(\iota^*\Phi_i)(P_1).
\tag{A3}
$$
R790 的 `value_K_1_zeta` 正是 $\Phi_i(P_1)$，已经带完整 $82^2=6724$。本式不再乘 $82^2$，不翻 $E_6=-c_6$ 的原符号，不重乘 $g_*$ 相位，也不把 eta 的符号变化带入一个没有 eta 的分母。

在 $P_0,P_1$，$F_i$ 的上半平面零阶及 $E_4^2$ 的零阶相配，所以(A3)是原 $H$ 局部框架的正则评价。框架在两点由同一 $E_4^2/E_6$ 给出。其乘法继续给原 $V_2$ 的框架平方，不能独立改变 $P_0$ 的标量。

## 2. 不构造146阶反射矩阵的两个有理右端

读取旧 R786 全部146条 power1 行的 $q_Y^0,\ldots,q_Y^{13}$，仍用原 $1,\xi,\ldots,\xi^{39}$ 坐标。设 $S$ 为560行、146列整数矩阵，列为原 $F_i$。二十 cusp 单轨道及 $20\cdot14>\deg H=272$ 保证该前缀对原 $V_{1,K}$ 单射。

记 $J$ 为第 $(n,r)$ 行乘 $(-1)^n$ 的对角矩阵。原 $\iota$ 保持 $V_{1,K}$，而旧原基的系数在 $\mathbf Q(\xi)$；其矩阵实际在 $\mathbf Q$。例如把 $K$ 的两坐标分开，$S C=JS$ 的非有理分量被 $S$ 的列独立性迫为零。这里没有把原扭曲后的截面误称为 $\mathbf Q$-定义。

真实选择146个独立行 $I$，保存一个非零模 minor，置 $A=S_I$。将原 P1 评价拆成两个有理行 $e_1^{(0)},e_1^{(1)}$，基仍是 $1,\zeta$。只解
$$
\ell^{(c)}A=e_1^{(c)},\qquad c=0,1,
\tag{A4}
$$
再置
$$
\boxed{e_0^{(c)}=\ell^{(c)}J_IA.}
\tag{A5}
$$
$A:V_1\to K^{146}$ 是实际坐标同构，且 $A\iota=J_IA$。因此(A5)就是原 P0 评价，不是任意延长一个局部泛函。保存并准确核回(A4)的全部146列和(A5)全部146项。无需物化整个 $A^{-1}J_IA$，也无需重新取得任何 CM 周期。

## 3. 原 V2 上的固定21点空间

读取旧418条 power2 行，逐 recipe 核其两因子都是同一原 M2 行；它们的实际整数尺度为 $82^4$。由(A3)的乘法性，若 $G_j=F_lF_r$，则
$$
G_j(P_0)=e_{0,l}e_{0,r}
\tag{A6}
$$
是在同一平方框架中的真实值，不能再插入 $82^4$。

原 $q_Y^0$ 的40个整数坐标同时为零，当且仅当该原截面在完整20-cusp闭点上消失。将它们组成40行、418列的有理矩阵 $C$。Riemann--Roch 给
$$
\dim H^0(2H-\mathcal D_{\rm cusp})=398,\qquad \operatorname{rank}C=20.
\tag{A7}
$$
用一个真实20阶 minor 解原有理 cusp 核，并对全部40行准确代回；不重新生成 R820 的 normal cusp 理想或有限域。

在该398维核上施加(A6)的一条 $K$ 线性评价。因为 $\deg(2H-\mathcal B)=523>252$，它非零，核维数准确为397。实际选一个非零评价坐标，作
$$
u_j=c_j-\frac{e_0(c_j)}{e_0(c_*)}c_*.
\tag{A8}
$$
全部397条同时核原40个 cusp 系数及 P0 值为零。它们是
$$
U=H^0(2H-\mathcal B)
\tag{A9}
$$
的完整原 $K$ 基，扩张到 $L$ 后不改变维数。保存其相对原 $V_2$ 的完整稀疏 $1,\zeta$ 坐标、原 pivot 和源 SHA。

## 4. 只作新组合乘积的1213阶充分认证

按 R836，$2H-\mathcal B$ 无基点。对候选 $u,v\in U$，若额外共同零为 $Z$，原 Koszul 核及 RR 给
$$
\operatorname{rank}[uV_3,vV_3]=1213-\deg Z.
\tag{A10}
$$
因此真实1213阶非零 minor 即证共同零恰 $\mathcal B$。不需要恢复整个 $V_5$ 坐标逆，也不需要 P0 的高阶 jets。

为保最小源，本任务在原 $\xi$ 坐标中直接消费已成 V3 前69项。在一个 $\ell\equiv1\pmod3$ 的真正素数及原选 $\zeta$ 根上约化候选，形成 $uF_j,vF_j$ 的前69项、每项40坐标矩阵。它有2760行、1380列。$20\cdot69>\deg5H=1360$ 给原全局乘积的注入；原非零 minor 是真实特征零乘法秩的充分证书。

约化乘积使用 stride79：两因子的 $\xi$ 次数各不超过39，积最高78，故没有相邻 q 项进位。先按 $\xi^{41}=1$ 折叠，再减第40项以使用 $\Phi_{41}=0$。模 p 的整个原坐标积精确保存；不使用某个 $\xi$ 数值根替代完整40坐标。

选出的 $u,v$ 在原 V2 基中至少有两个非零项，因而是本次新线性组合的乘积，不是重算一个已有单项式 recipe。旧 V2/V3 Fourier 行直接读原文件；没有重复旧 real-coordinate 转换。每个新乘积按17列一组原子保存，保原源、候选、素数和 $\zeta$ 根。

固定搜索顺序如下。先以 $u=u_0+c u_1$、$c=1,2,3$ 选第一条在原 V2 基中不只一项的非零截面，保实际整数清分母及 content。然后令 $v(a)=\sum_{j=0}^{396}a^ju_j$，$a=0,1,-1,2,-2,\ldots$；若某个 v 只有一项则仅登记该选择未使用。用素数索引和 a 索引的对角顺序公平推进。一个模低秩只记录该真实模结果，不能写成特征零共同零的否定结论。

运行时间和试次上限不进入数学身份；所有实际候选、全部原系数和原子阶段均进入来源绑定。再次提高上限从下一对开始，不重求 P0、U 或已成乘积/minor。

## 5. 输出、断点与真正未完成量

核心路径 `scripts/R837_original_branch_pencil.py`。

- RESULT：`R837-original-fixed-branch-pencil`。
- FINAL：`p41-original-fixed-branch-pencil-certificate.json`。
- CLI：`--config <expanded-job.json> --out <output> --budget-minutes 300`。
- 数学阶段仅根目录 `R837-*.json.gz`；每个完成阶段都有原 `configuration` 和 `complete:true`。
- `stage_manifest.files` 只列本次完整数学阶段，不列它自身。
- FINAL 明确给 `original_P0_evaluation_certified`、`complete_fixed_branch_space_certified`、`fixed_branch_pencil_certified`、`actual_pencil_rank`、`stage_manifest` 和 `seconds`。
- 只有三个目标全部准确完成且真实秩1213时 FINAL 才 `complete:true`。预算或试次停止仍保存已成 P0/U/乘积和准确模结果，不把部分任务称为完整铅笔。

expanded `sources.R790` 与 `sources.R786` 分别给真实目录、原 BASE 身份、configuration SHA、证书和阶段清单 plain spec，以及由完整 manifest 展开的所有选入 `file/bytes/SHA`。目录不进入数学 tag；选源 plain list 的指纹及所有原 producer 身份进入 tag。证明/方法路径也不进入 tag，只绑定它们的实际 SHA。

后继只消费真实 P0 评价、U 基和两锚，不需再次读取原 CM 变形产物。这个任务尚不提供原 $T'_m\subset H^0(mH-E_2)$、原 D、η 或高度。R836 的短 RR 核仍必须保那些真正的特征零包含来源。

## 来源

- R767（2026），原 level82 群、$P_0/P_1$ 标记、$E_6/\eta^{12}=24s(2t_Y-1)$ 与粗曲线框架。
- R802（2026），原 $T^{41}$、$q_Y\mapsto-q_Y$、偶权无额外因子、几何反射与算术共轭的区别。
- R790 的真实完成结果（2026），146个原 P1 值与统一 $82^2$ 尺度；本稿不重算旧算术。
- R786（2026），原 powers1/2/3 的准确旧前缀、recipe 和全部整数尺度。
- R836（2026），固定21点两锚、真实 rank1213 与约化 D 的短核消费者。

所有可重算新表只留一日活跃 artifact；Git 保存脚本、参数、来源 SHA、run 编号及准确结论。
