# 同一原方阵第二左射流：小单位块与三十六个真实右端

作者：Astra-ISP-789f / normal_annihilator。AI-assisted；GPT-6 Astra Pro。  
日期：2026-11-15。状态：算法及范围证明已给出；源码仅作实际 AST 检查，尚未运行本次数学。

## 1. 已付输入和这一轮的目标

只接 run $43702348535$ 的已完成特征零第一层缓存。原所选 $B(u)=A^h(u)_{I,J}$ 满足
$\operatorname{rank}B_0=4318$，其完整常左核记为 $\Lambda$，维数 $36$。
本次之前已实际证明第一连接在 $\mathbb Q$ 和 $\mathbb F_{31}$ 中都恰有秩 $3$。

完整第一层证书给出整数矩阵
$$
X\in\mathbb Z^{1546\times33},\quad
C\in\mathbb Z^{36\times33},\quad
B_0^TEX+B_1^T\Lambda C=0.
$$
其中 $E$ 嵌入同一 $I$ 内、横向次数至多 $3$ 的 $1546$ 个规范校正坐标。全部第一射流准确为
$$
\lambda_0=\Lambda Cc,\qquad
\lambda_1=EXc+\Lambda d.
$$
这里 $c\in\mathbb Q^{33}$、$d\in\mathbb Q^{36}$；它们不是可任意省略的标签。

本轮先令第二校正也使用相同的 $1546$ 个坐标，尝试构造 $24$ 个独立二阶头。如果得到这些完整原证书，可由已付模 $31$ 第二层秩 $9$ 的下界夹逼特征零第二层秩恰为 $9$。不足时只表示此支撑的正证书不足，仍允许更高横向支撑。

## 2. 三十六个右端的完整来源

写
$$
M_0=B_0^TE,\qquad H=B_1^T\Lambda,\qquad
T=B_1^TEX+B_2^T\Lambda C.
$$
从已经保存的第一层 RREF，取三个枢轴头坐标的标准嵌入
$F:\mathbb Q^3\to\mathbb Q^{36}$。它与 $C$ 的三十三个自由头构成直和
$$
\mathbb Q^{36}=\operatorname{im}C\oplus\operatorname{im}F.
$$
对 $d=Cy+Ft$ 使用已付恒等式 $HC=-M_0X$，第二式变成
$$
M_0x_2'+HFt+Tc=0,\qquad x_2'=x_2-Xy.
\tag{2.1}
$$
因此只需新建 $3+33=36$ 个真实右端 $[HF,T]$。

没有删去 $y$。从 (2.1) 的任一实际解，完整源的回填是
$$
\begin{aligned}
\lambda_0&=\Lambda Cc,\\
\lambda_1&=EXc+\Lambda Ft+\Lambda Cy,\\
\lambda_2&=Ex_2'+EXy+\Lambda e,
\end{aligned}
\qquad y\in\mathbb Q^{33},\ e\in\mathbb Q^{36}.
\tag{2.2}
$$
程序保存已付 $X,C,\Lambda$ 的实际文件身份、三个头轴 $F$、每个新解的 $c,t,x_2'$，以及 (2.2) 的完整源配方。若随后求第三层，这些真实自由校正仍保留。

## 3. 先检查旧零行，避免不可能有用的大解

原第一层准备矩阵实际有 $2618$ 个保留行和 $1736$ 个严格零行。在这些旧零行上，$M_0=HF=0$，故本轮支撑必须满足
$$
T_{\mathrm{oldzero}}c=0.
$$
先对这个 $1736\times33$ 整数矩阵作精确有理行化简，保存完整小行化简和秩 $r$。

若 $r>9$，此支撑最多有 $33-r<24$ 个头，不可能给出本轮所需 $24$ 个正证书。程序即保存全部原 $T$ 并跳过单位块求解。它不称特征零第二层秩大于 $9$，因为横向次数 $4$ 的第二校正仍未加入。

若 $r\le9$，继续同一个共享时钟内的真实单位块及全部原行验证。

## 4. 原 $M_0$ 的单位块和行 content 运输

$M_0$ 的 $1546$ 列在 $\mathbb Q$ 上满列秩已付，但不能据此预填某个模 $31$ 单位块。

对每个原行 $i$，取仅由其 $M_0$ 系数决定的正 content $g_i$；零行取 $g_i=1$。程序对
$$
\widetilde M_{0,i}=M_{0,i}/g_i
$$
真实作 $\mathbb F_{31}$ 行选择，并对得到的 $1546$ 个原行 $R$ 重新计算实际方块行列式。只有
$$
\det\bigl(\widetilde M_0[R,:]\bigr)\not\equiv0\pmod{31}
$$
才进入该方块求解。若本次模 $31$ 行选择不足，保存这一实际结果，不换素数、不把它当作有理秩不足。

这里的单位块是除去行 content 后的真实整数矩阵
$U=\widetilde M_0[R,:]$。某些 $g_i$ 可以含 $31$；因此不得把这个计算冒称未除 content 的原 $M_0[R,:]$ 在 $\mathbb Z_{(31)}$ 上有单位行列式。

实际求解必须同时运输右端：
$$
U Y=-\operatorname{diag}(g_R^{-1})[HF,T]_R.
\tag{4.1}
$$
右端是精确有理矩阵。worker 使用 `fmpq_mat.solve(algorithm="dixon")`，并将完整三十六列解先按正公共分母保存：
$$
Y_j=N_j/D_j,\qquad D_j>0.
$$
保存完成之后，才对全部选中原行逐列检查
$$
M_{0,R}N_j+D_j[HF,T]_{R,j}=0.
\tag{4.2}
$$
这是原未除 $g_i$ 的整数恒等式，避免了只核缩放后方块的来源混淆。

worker 保留完整候选和逐列已验证游标。若 native solve 尚未返回，不声称存在候选或内部可恢复进度。

## 5. 全部原行的残差及真正二阶证书

外层为每一列计算
$$
S_j=M_0N_j+D_j[HF,T]_j
$$
在原全部 $4354$ 行上的完整整数值，每完成一列即保存真实数组及身份。单位行上的零全部核实。

对 $S=[S_1,\ldots,S_{36}]$ 作至多 $36$ 列的精确小行化简。若 $\gamma\in\ker S$，令
$$
x_2'=\sum_jN_j\gamma_j,\qquad
(t,c)=\operatorname{diag}(D_1,\ldots,D_{36})\gamma.
$$
这严格恢复 (2.1)，不是把原变量误认为 $\gamma$。每个完整候选先保存，再用原未缩放的 $M_0,HF,T$ 检查全部 $4354$ 个产品。

程序还核实 $S$ 的前三个头补空间列有秩 $3$，以及实际 $c$ 的自由坐标子矩阵非零对角。因此计数的是独立原头 $c$，不是仅小残差矩阵的零度数。

若独立头数为 $d_2$，则得到合法上界
$$
9\le\operatorname{rank}_{\mathbb Q}\beta_2\le33-d_2.
$$
当 $d_2=24$ 时才宣布第二层秩恰为 $9$。当 $d_2<24$ 时，只保存真实已有二阶头和来源；下一步可以加入 $1485$ 个横向次数 $4$ 的校正坐标。本入口不预填更高支撑无用。

模 $31$ 下界的运输依赖已完成的同一原 $B_0$ 与第一连接的有理/模 $31$ 秩相等，从而在 $\mathbb Z_{(31)}[[u]]$ 中先真实剥离常数单位块和三个 $u$ 单位因子。它不依赖本轮行 content 缩放是否为 $31$ 单位。

## 6. CLI、共享预算和完成范围

主入口：
`notes/2026-11-15-r150-selected-natural-second-left-unit-pipeline-789f.py`。

独立单位块 worker：
`notes/2026-11-15-r150-selected-second-left-unit-solve-worker-789f.py`。

精确调用：

```text
python -B {scripts}/2026-11-15-r150-selected-natural-second-left-unit-pipeline-789f.py
  --first-out {work}/selected-natural-first-left-envelope
  --rebuild-root {work}/selected-natural-u-rebuilt
  --primitive-equations {primitive}
  --unit-worker {scripts}/2026-11-15-r150-selected-second-left-unit-solve-worker-789f.py
  --out {work}/selected-natural-second-left-unit
  --seconds 300
  --memory-mib 2048
```

- 全部新数学共享 $300$ 秒，每个进程地址空间上限 $2048$ MiB。
- 不编译 native，不装新依赖；使用该会话已安装的 Python、python-flint $0.9.0$ 与标准库。
- 不重第一层 RREF、不重 $585$ 余空间、不重旧大正常形、不新增原 Dixon 位数。
- 主入口核全部已付输入的完整 bytes/SHA，再运行新阶段。语义绑定不包含临时路径、预算或恢复目录。
- 原生单位解阶段为保存完整返回解预留至多 $20$ 秒的共享时钟内宽限；收到停止信号只在安全边界停。未返回的 native 调用没有伪检查点。
- 所有 gzip 使用 `compresslevel=1`；所有大数组仅在当前 job 临时目录。永久只保存源码、参数、run、小回执和散列。

主回执：
`selected-natural-second-left-unit-pipeline-receipt.json`。

完成结果枚举：

| outcome | 严格含义 |
|---|---|
| `same-selected-second-rank-nine-proved` | 已付 $24$ 个独立头及全部原二阶恒等式；同一原第二层秩恰为 $9$ |
| `restricted-second-left-support-only` | 此支撑已完整算完，但头不足 $24$；更高支撑仍开放 |
| `same-support-obstruction-before-unit-solve` | 旧零行限制秩大于 $9$；已保存真实 $T$，跳过不可能闭合的单位解 |
| `mod31-unit-profile-incomplete` | 本次 content 后模 $31$ 行选择不足；未宣布有理秩不足 |
| `checkpointed-time-budget` | 已保存真实完成阶段；未完成的 native 内部进度不作计数 |
| `failed-or-incomplete` | 具体输入、算术或实现错误；保实际阶段和错误日志 |

仅第一种完成结果使
`selectedSecondConnectionRankExactly9=true`。
全局目标成员性、原参数 leading-unit 及特征零完整长度 $243$ 始终不由本轮预填。

## 7. 检查点和继续点

临时目录分为：

1. `prepared/`：完整原 $[HF,T]$、旧零行有理行化简、真实 $31$ 单位选行及未缩放原系统。
2. `unit-solve/`：完整 $D_j,N_j$ 候选及逐列原单位产品游标。
3. `full-products/`：三十六个全原残差列、完整小 RREF、逐个真实二阶候选和已核原产品小回执。

继续时，完成阶段先逐文件核 SHA。单位解已返回则不再求解；完整残差列、RREF、候选及逐候选产品也分别复用。若仅某个未返回 RREF 或 native solve 被中止，明确只保其输入，没有伪造可继续的内部消元状态。

第一层的 $33$ 维 $y$ 与末校正的 $36$ 维 $e$ 不合并成“无影响的自由核”：它们有 (2.2) 给出的原伴随坐标，将在第三层产生实际项。

## 8. 冻结源身份与已付输入

主入口：$29556$ 字节，SHA-256
`7bceace52b388011b0a3bd90e056e47d7cbea5712f093318bf519c94257052e1`，
Git blob `4e0a2cebdf45be98c271bf125796d31b35ae2063`。

worker：$16244$ 字节，SHA-256
`a706713bb49b292c7256aa67b5cb1d75b81003175ef0b87e094e4f0efc03a8a9`，
Git blob `3caf55504906b0d6f7240c5f54e55f675dde488a`。

主入口实际 AST 已通过，worker 的 AST 由 literature_audit 实际通过；两者均未运行本次数学。

所有输入都来自当前临时会话和已付原文件，主源码列有九项实际数据 pin，并另行锁定 worker 的 bytes/SHA：

- 原第一层准备系统、完整 $36$ 头、RREF、$33$ 个第一射流及完成 worker 回执；
- 同一原自然常数/第一系数；
- 同一原 $I,J$ 字典；
- 原 primitive 整系数参数多项式。

核心旧绑定是
`717dd4bfc621d633c40c01ffd0e35345828ffc98b9edf25b10989153ece49d91`。
本轮自然 $B_2$ 直接从同一原参数多项式取系数，同时逐项与已付 $B_0,B_1$ 核对；不使用共动二阶矩阵替代。

数学基础参见
[已付特征零第一层完整证明](../results/R150-appendix-selected-natural-first-connection-exact-rank-three.md)
及其实际 run $43702348535$ 的续算小回执。
