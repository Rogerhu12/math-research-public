# R150：原整数格内唯一 η8 第二方向的连续入口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

日期：2026-11-14。状态：**已证明的来源、范围和费用接口；新数学任务尚未执行。** 三个新 C++ 入口已作每次 30 秒／512 MiB 的有界编译，两个 Python 文件已作 AST 解析。实际回执另存 `2026-11-14-r150-eighth-second-build-receipt-789f.json`。编译成功不代替下面任何矩阵或原式身份。

## 1. 精确目标和已经保存的来源

仍使用原 primitive 整数 17 式的 Macaulay 矩阵 $A$，完整来源数 6188、输出坐标数 4367。令 $p=31$。目标仍是每个原 $j=2,\ldots,10$ 的

$$
AX_j=p^2h_0t_j\pmod {p^6},\qquad p^6=887503681.
$$

run `43634830833` 已给出九个成本 87 的实际原来源，满足上式模 $p^5$。run `43638830039` 在原整数模 $p^6$ 计算并保存了同一九来源的下一余量

$$
\rho_j=\frac{p^2h_0t_j-AX_j}{p^5}\pmod p,
$$

以及所有原正常形、商 $G$ 的除式和余式、3333 前基来源 trace、完整 315 维扭坐标。后一个 run 还证明 $F_9=[A,b_1,\ldots,b_9]$ 的**完整第一像为零**，这些九个余量在 $Q/U_9$ 中分别非零。

本入口只复用这些九来源、九余量和全部已成除式，不重新计算它们。原 p6 模型文件也直接复用此前的 38998 字节文本及其真实生成回执，SHA256 为 `5d418686b82665f7e988a0624440e70f44f0c6ba06c124b44fa85f7c17d04e7a`。新的唯一原 RHS 标签为 **9101**；此前标签 9001 只是所复用十列文件中的首列，本次最终九目标混合时其系数严格为零。

## 2. 整数格为什么只留下 η8

使用已发表的[原整数格引理](2026-11-14-r150-original-p2-integer-source-lattice-and-eighth-second-direction-789f.md)。真实除列写为

$$
b_i=A\kappa_i/p^{e_i},\qquad
(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
$$

自然来源运输是 $T_9(x,c)=x+\sum_i\kappa_ic_i/p^{e_i}$。对于原 $p^2$ 目标，其精确整数格为

$$
\Lambda_2=\{(x,c):p^2T_9(x,c)\text{ 是原整数来源}\}
 =\{c_8\in pD[s],\ c_9\in p^2D[s]\},\quad D=\mathbb Z_{(31)}.
$$

完整原来源模中 $\bar\kappa_8,\bar\kappa_9$ 的独立性已在该引理支付；不能在局部 Taylor 商中把 $s-2$ 当成单位来替代它。

保持当前 $F_9$ 初始来源模 $p$、同时保持 $\Lambda_2$ 的第一位改变，其完整核是

$$
\ker\bar A\ \oplus\ \sum_{i=1}^{8}\mathbb F_{31}[s]\eta_i.
$$

第九关系的第九除列坐标为 $s-2$，不能在这一步自由加入。旧 1632 个精确 Koszul 方向、旧四个已付扩增方向、旧 198 方向的相关第二像及 $\eta_1,\ldots,\eta_7$ 的相关第二像均已有来源或覆盖证明。在 $1/2$ 主分量模 $U_9$ 后，本次唯一尚未计算的方向是 $\eta_8$。本条不把旧 198 的第三像说成零，不排除更低初始来源，不排除一般有理来源。

## 3. 先实际核九余量的主分量

selector 读取 run `43638830039` 保存的完整矩阵和真实 $G$ 余式，重新逐项核对其 505 个自由观察与 315 坐标；它不重做原式乘积或正常形。

从 $J$ 的完整特征多项式取出根 1、2 的全部幂，实际重数必须为 7、32。用 CRT 得到首一余式次数至多 314 的投影多项式 $P$，并在整个 315 维空间核对

$$
P(J)^2=P(J),\qquad P(J)U_9=U_9.
$$

它随后实际检查每个 $P(J)\rho_j=\rho_j$，记录原九列及商九列所生成模的维数和最小湮灭多项式。**在新回执给出之前，不宣称这九个新余量已经满足支撑条件。** 若发现未付的其他主分量，真实 selector 回执完整保存，当前 pipeline 标为 `failed-or-incomplete`，不伪报完整否定结论；下一步须使用实际新支撑继续。

selector 同时重读已成真实系数

$$
C=(28,3,24,3,25,2,23,8,0)^T,
$$

其意义为原 $K4_{7003}$ 的第一除像 $AK4_{7003}/p^4$ 的完整 $U_9$ 坐标。第九系数 **确实是零**，因此这次构造不需要 $\kappa_9$ 补偿。

## 4. 唯一新的 q 和原 H5

先在真实原 $A\bmod p$ 中恢复一个来源 $q$，满足

$$
\bar A q=AK4_{7003}/p^4-\sum_{i=1}^{8}b_iC_i\pmod p.
$$

右边的全部正常形、$G$ 商和 trace 都来自此前保存文件。本次只把它们按上述固定系数合成，核全部 $GQ+\mathrm{rem}$，再恢复唯一一列新的 $VQ$。由实际 $B(J-HC)$ 运输和两个完整前基 DAG，得到原 6188 行的 $q$，不是只给 2195 商来源。

取这个真实原来源的标准整数代表，构造

$$
H_5=K4_{7003}-\sum_{i=1}^{8}p^{4-e_i}\kappa_iC_i-p^4q.
$$

程序在原整数模 $p^6$ 直接乘回全部 17 式并逐坐标检查 $AH_5$ 被 $p^5$ 整除；随后才形成真实

$$
d=AH_5/p^5\pmod p.
$$

这是 $\eta_8$ 的相关第二像来源。用整个原列重新乘回的作用，是固定所有整数代表和 carry；不能仅从前一模 $p$ 等式口称得到这一除像。本次不调用 $p^7$，也不更改旧 p6 程序的数值常量来假装支持更高模数。

## 5. 完整相关像、负 dual 和正来源

新列先保留全部自由检验及完整 315 坐标，再对 $P(J)d$ 在 $Q/U_9$ 中计算完整 Krylov 闭包。相关空间维数为 $39-9=30$，单列完整系数次数至多 29。

每个不相容目标保存一个真实 315 坐标的 dual。它由商 dual 与 $P(J)$ 复合，实际杀死 $U_9$ 和新列的整个多项式模；由第 2 节已证的完整相关覆盖，适用于全部允许的当前初始来源第一位改变，而非只杀本次列出的有限数值样本。其否定范围严格是：

> 保持当前 $F_9$ 来源模 $31$，同时保持原 $p^2$ 目标的整数格 $\Lambda_2$，不能将所列目标再提升一位。没有关于更低初始来源或一般有理来源的否定结论。

对相容目标，先尝试同一有限次数内不带 $P$ 的真实组合；若需要投影，则把 $P$ 乘到新列的实际来源多项式上。必须在**整个 315 维空间**核成

$$
\rho_j=f_j(J)d+U_9c_j.
$$

此处 $U_9$ 的每一列都有已保存的真实原预像 $\kappa_i$，不能免费引入无来源的旧列修正。随后恢复完整原来源 $w_j$，使

$$
\bar A w_j=\rho_j-f_jd-\sum_i b_i(c_j)_i.
$$

最终实际整数来源为

$$
X'_j=X_j+H_5f_j+\sum_{i=1}^{9}p^{5-e_i}\kappa_i(c_j)_i+p^5w_j.
$$

这些系数全部整数，且由第 2 节的自然运输对应保持 $\Lambda_2$ 的改变。最终程序再次逐行读取原 6188 来源、全部 4367 输出坐标，支付

$$
AX'_j=p^2h_0t_j\pmod{887503681}
$$

的完整 primitive 恒等式及到原 17 方程尺度的运输。任意部分相容都必须接这一步，不能仅报告仿射商相容；不相容槽的来源精确置零并验证。

## 6. 明确的次数和资源界

下表是已付上界，运行回执另报真实成本。

| 对象 | 参数或加权成本上界 | 依据 |
|---|---:|---|
| 唯一 q 的原 RHS | 88 | 原 K4 及旧除列实际来源 |
| 原 q 和 H5 来源 | 184 | 同一完整 T96 标准来源恢复增加至多 96 |
| 相关循环多项式 | 29 | 30 维相关商 |
| 完整 CRT 投影次数 | 314 | 原 315 次特征多项式 |
| 真正使用的来源多项式 $f_j$ | 343 | 两者之和 |
| 最后原 RHS | 527 | $184+343$ |
| 最后原来源 | 623 | 额外完整来源运输增加至多 96 |

本轮只在 Actions 中运行一次共享 **300 秒**数学软时钟，每个子进程 **512 MiB** 地址空间；`timeout --kill-after=10s` 只为真实 checkpoint 留终止宽限。六个 C++ 编译各自限 30 秒／512 MiB，编译、静态输入 SHA 核对在数学时钟之前，压缩和上传在其之后。编译没有运行数学。实际 clock、退出码、最后完整 marker 均写回执，退出 0 本身不构成完成。

原生一列／九列 $VQ$ 保存真实累计数组和下一图行；原式乘积保存真实输出数组、两个原来源前缀和下一原行。所有已完成阶段都有绑定实际输入 SHA 和源代码 SHA 的 cache。短的 image/normal/transport/matrix 阶段只缓存已完成结果；未完成输出同样保全，但不伪称可以从其内部位置续算。

## 7. 精确 CLI、输入、输出与续算

```bash
PYTHONDONTWRITEBYTECODE=1 python3 2026-11-14-r150-eighth-second-runner-789f.py \
  --notes-root NOTES \
  --t96-recovery T96 \
  --all198-recovery ALL198 \
  --seven-recovery SEVEN \
  --current-recovery CURRENT_43634830833 \
  --ninth-recovery NINTH_43638830039 \
  --out OUTPUT --math-seconds 300 --memory-mib 512 --compile-seconds 30
```

46 个输入逐文件 SHA 锁定；scope 数量为 `t96:5, all198:15, seven:5, current:6, ninth:13, notes:2`。五个旧 recovery artifact、准确路径、字节及 SHA 见 `2026-11-14-r150-eighth-second-contract-789f.json`。没有重建旧原矩阵或旧 200 方向的入口。

`OUTPUT/results/eighth-second-pipeline-receipt.json` 是唯一主回执。其 `status=completed` 必须同时具备：`newEighthSecondDirectionComputed=true`、`newDirectionOriginalDivisibilityVerified=true`、`integerAdmissibleRelatedSecondImageComplete=true`、`allCompatibleTargetsOriginalIdentityVerified=true`。合法完成分支为：

- `all-nine-full-original31squaredh0-mod887503681-certificates`；
- `complete-eighth-admissible-second-obstruction-with-positive-original-certificates`；
- `complete-eighth-admissible-second-obstruction-no-compatible-current-source`。

逐目标由 `individualTargetCompatible`、`compatibleTargetLabels`、`obstructedTargetLabels` 给出，不能从某一分支名称推断九列全正或全负。`finite_budget_verified=true` 只在九个目标都实际乘回时出现。所有分支的 `characteristicZeroIdentityAsserted=false`。

`OUTPUT/recovery` 包含 prepared 系统、真实新 q 的 image/source/原 transport、H5 的原来源和除后 RHS、新正常形/trace、完整相关系统、必要时的最终九列 image/source/原式，以及所有 stage cache。所有实际恢复文件都由 manifest 逐项记录；二进制无损 gzip 并按至多 **4,500,000 字节**分片，整体及每片 SHA 同存，小文本直接保全。不能只保存恢复数据的哈希。

续算给同一 runner 加 `--resume-recovery SAVED_RECOVERY`，从已完成 cache 和真实 source/product 数组继续。旧输入字节、来源多项式或程序若变，绑定失配，不能复用不相容的 checkpoint。本次既定目标与范围不因此改变。

## 8. 本结论的边界

本入口没有把 $\eta_9$ 的第二像纳入当前整数格，没有把旧 198 的第二像覆盖升级成第三像零，没有证明完整模 $p^6$ 初值自由已被穷尽。即使九原式全部成功，也只是新的有限精度真实来源；R150 的特征零有限异常集和整个 ISP 仍未据此完成。
