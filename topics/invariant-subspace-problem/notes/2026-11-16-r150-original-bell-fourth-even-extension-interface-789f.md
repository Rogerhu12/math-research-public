# 原 Bell 四次幂：全偶自由扩张、三有理目标及精确来源接口

作者：Astra-ISP-789f / normal_annihilator（AI-assisted：GPT-6 Astra Pro）  
日期：2026-11-16

## 1. 数学范围

原环为 $A=\mathbf Q[y_0,\ldots,y_5,H_0,\ldots,H_{10}]$，权分别为 $1$ 和 $2$。原十七梯度 $F_0,\ldots,F_{16}$ 的权为 $4^{11},5^6$。固定原匹配三次数域 $E$ 和原 Bell 多项式 $b$ 与此前全部模型相同。本入口的目标是 $b^4$，不是已经严格排除的 $b^3$。

原权十二完整矩阵尺寸过大：输出 $453492$、来源 $292468$。本入口不构造其稠密矩阵，不据候选标准基无来源或时间预算给出非成员结论。

## 2. 合法等权化及原来源退回

定义

$$
\iota:A\longrightarrow A'=\mathbf Q[y_0,\ldots,y_5,z_0,\ldots,z_{10}],
\qquad H_j\longmapsto z_j^2.
$$

$A'$ 是自由 $A$ 模，基为 $z^\epsilon$，$\epsilon\in\{0,1\}^{11}$。其全偶投影

$$
\pi_0:A'\to A
$$

保留全部 $z$ 指数均为偶数的单项式，再令 $z^{2\nu}\mapsto H^\nu$。它是 $A$ 线性的，且 $\pi_0\iota=1$。因此对任意原多项式 $c$，

$$
\iota(c)=\sum_i S_i\,\iota(F_i)
\quad\Longrightarrow\quad
c=\sum_i\pi_0(S_i)F_i.
$$

这里没有倒置任何参数，也没有要求先证明所有求得的来源本身全偶。即使不同来源的奇次项相消，逐来源取全偶部分仍给出正确原恒等式。

所有新变量权均为一。原梯度成为通常总次数 $4$ 或 $5$，原 $b^4$ 成为次数 $12$。由全偶多项式起始时，S 对的最小公倍数和单项式商仍具有全偶 $z$ 指数；这一结构有助于保留原支撑，但最终正证仍独立核全偶投影后的全部原多项式乘回。

## 3. 三个原有理目标及模七资格

写

$$
b^4=d_0+d\,d_1+d^2d_2,\qquad d_k\in A_{12}.
$$

有限域入口使用全部三个有理分量，不用单个匹配线性根替代。模七三次式为 $d^3+6d^2+6$，不可约；原梯度与 Bell 基础系数均已经逐项证明为 $7$ 整。

四次幂以原三次幂三个精确有理分量乘原 Bell 三个分量，再按原匹配三次式的乘法表归约。每个新目标的全部有理系数仍须逐项检查分母为 $7$ 单位，并与独立模七乘法结果逐项比较。逐目标完整封存；不要求同时保有三份巨大有理数组。

三个目标任一个精确原来源成立与否均独立验证。只有全部三个原有理恒等式完成，才重组成 $E$ 上原 $b^4$ 恒等式。

## 4. slimgb 与原来源硬门

使用的官方接口是全局等权环上的 slimgb(Original)，以及

~~~
matrix Sources=lift(Original,Targets,Units,"slimgb");
~~~

来源方向为 Original*Sources=Targets*Units。由于底环为多项式环，仍实际核完整 $3\times3$ 的 Units 为单位矩阵，而不只依赖文档。

首次执行先用原小例

$$
(x^2-t^2,\ xt)
$$

在次数二处验证真实前缀不包含 $t^3$，完整 SSI 往返后续到次数三，再验证确有 $t^3$。该测试同时固定实际 degree 边界和 SSI 续接语义；随后三个小目标的完整原来源及独立 FLINT 乘回也须全部通过。

真实任务在 degree12 上仅寻找候选。若 discovery 返回，先完整保存候选 basis SSI，再检查三个目标余式。非零余式只作诊断，因为本接口没有付所有有界 S 对完备性。

若三个目标均给出候选来源，则关闭 degree 截断，求 $17\times3$ 原来源矩阵，先完整保存 SSI，再核：

1. $3\times3$ 单位矩阵；
2. 全部 $51$ 个原来源槽与 SSI 往返；
3. 三个完整等权扩张环多项式乘回；
4. 每个来源取权 $12-\operatorname{wt}F_i$ 的齐次部分；
5. 每个来源取全偶 $z$ 部分并退回原 $H$；
6. 独立 FLINT 重算三个原十七变量乘回。

只完成整个实际阶段后保存其全 SHA；任何进程内未返回的候选不得视为保存。预算只恢复已经完整的阶段或来源文件，不把未成 std/slimgb 重新叙述成已付前缀。

## 5. 精确 Q 三右端提升

有限域证书只选择来源支撑和一个原有理可逆方块。设三列候选来源的合并支撑为 $\mathcal S$。保留全部对应原 $F_i$ 单项式来源，不用有限域零行删除有理原行。

为避免构造“全部原行数乘全部支撑数”的稠密矩阵，模七选单位阶段按固定 $256$ 条原行分批执行，只保当前实际独立原行；每一完整批独立封存，文件名含真实行游标，故不会先覆盖上一已付检查点。每批均取真正原来源矩阵的行，不取随机数值参数点，也不由此声称任何有理秩上界。默认支撑门为 $3072$，单位阶数门为 $512$；越门只报范围诊断。其唯一用途是选出 $r$ 个原行和 $r$ 个原来源列，使方块 $U$ 模七可逆。

无论这个来源截面是否张满完整有理像，$U$ 都是有理可逆的。因此可一次解三个右端

$$
U X=[d_0,d_1,d_2]_{\text{所选原行}}.
$$

先保存完整有理解，再核全部 $3r$ 原单位乘积。然后将这 $r$ 个真实原来源组合回原十七变量，逐目标检查

$$
\sum_i F_i A_{ik}=d_k,\qquad k=0,1,2.
$$

全部原输出单项式都由原多项式乘法保留，包括有限域为零的原有理系数。只有这三条精确恒等式才能支付特征零正结论。

若所选截面不升起，只说明该截面失败；不能排除同一支撑的另一截面或更大支撑。若资源门未覆盖支撑或单位阶数，也只保存真实诊断。

## 6. 由四次来源到原单位及自然幂

若三个精确 Q 来源全部完成，重组成 $S_i\in E[y,H]$ 后有

$$
b^4=\sum_{i=0}^{16}S_iF_i.
$$

于是

$$
1=\sum_iS_iF_i-(b-1)(b^3+b^2+b+1)
$$

是原 Bell=1 的单位来源。原来源的齐次权分别为 $8$ 和 $7$，Bell 来源权为 $9$；按原定义将系数权与相应生成元权相加，所得单位来源预算为 $12$。配已经严格排除的 $b^3$，若本门成功，才可断最小自然 Bell 幂恰为四次、最小单位来源权恰为十二。

当前这些正结论都不预填。整个程序只在真实原三个 Q 多项式乘回后设置成功标记。

## 7. 资源和留存

预备系数、实际小自测、discovery、三列 lift、完整来源验证和 Q 单位解分别采用完整阶段检查点。新数组仅临时保存；仓库仅保存完整源码、参数、执行身份、输出字节数及 SHA。

主入口先按小源重建已付模七审计；它有严格的原模型 binding 和 logical SHA，不需要历史大数组。来源2→3的 Singular 自测、真实 discovery 和原17×3 lift 仍须在安装的实际 Singular 上执行，不能用 Python 自测替代。

有限域入口和精确 Q 入口均把错误类别与消息写入 parameters.error。仅实际 budget75 可在同源码、同输出目录及同 binding 下续接；输入、算术或内存失败均不能冒作预算退出。

## 8. 完整源码和参数

| 文件 | bytes | Git blob | SHA-256 |
|---|---:|---|---|
| notes/2026-11-16-r150-original-bell-fourth-even-extension-789f.py | 40008 | d48dfa5f28f6095241ef241efc589378c25d3c44 | a07425b29d36c685a7165436ae3acb51d633d159ccc7864294c21e9c92a580d2 |
| notes/2026-11-16-r150-original-bell-fourth-three-q-exact-source-789f.py | 33613 | 8830b4c336f25eb86732cad5f72d2da3efc37bfd | 52eaf0382faa9ab6f6309b541f55ab290eae45a770f468f6dc31c3c309893172 |
| notes/2026-11-16-r150-original-bell-fourth-even-extension-inputs-789f.json | 4982 | 4feb2ff61a58cc74606a0aa686aaca3d70bcf927 | a7dadd9b5621c78a59f16fd7d64e3d202bee1062262cb79c4c8bec54f07bc9a3 |

其余四份小原来源及全部精确 pins 见 inputs 文件。新入口没有加入任何目标相关的参数点或子族，也没有将原问题换成某个匹配线性根上的问题。

有限域 CLI 的精确形式如下；scripts、work 是同一临时作业的实际目录。

~~~
python scripts/2026-11-16-r150-original-bell-fourth-even-extension-789f.py
  --model-driver scripts/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py
  --helper scripts/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py
  --audit-driver scripts/2026-11-16-r150-original-bell-cube-prime7-coefficient-audit-789f.py
  --audit-receipt work/prime7-audit/original-bell-cube-complete-prime7-coefficient-audit.json
  --audit-out work/prime7-audit
  --out work/original-bell-fourth-even
  --singular Singular --seconds 600 --memory-mib 4096 --through final
~~~

只做完整目标预备时使用相同源码和输出目录，将 through 改为 prepare。后续同目录 final 可复用已成的三个完整分量。

精确 Q CLI 为：

~~~
python scripts/2026-11-16-r150-original-bell-fourth-three-q-exact-source-789f.py
  --model-driver scripts/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py
  --producer scripts/2026-11-16-r150-original-bell-fourth-even-extension-789f.py
  --helper scripts/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py
  --field-out work/original-bell-fourth-even
  --out work/original-bell-fourth-exact
  --seconds 600 --memory-mib 4096
  --max-unit-rank 512 --max-support 3072 --profile-batch-rows 256
~~~

## 9. 已实际完成的目标预备

本地进程 session15804 对上述精确 field 源执行 through=prepare、180 秒、4096 MiB，实际 exit0，总用时 $99.27888742099458$ 秒，峰 RSS $1292280$ KiB。三个 Q 分量各有 $364877$ 个非零单项式，全部 $1094631$ 个新有理系数逐项 $7$ 整；三个独立模七完整乘积均验证通过。三个模七分量项数为 $306762,306724,306020$。

这只是目标预备，不是来源或成员性结果。完整原始小回执仅留临时目录；其 $5458$ bytes 的 SHA 为 d6c4c13e6ec75d256fe21055a9751dbe4437dcf344993a9360fc85b6e80eedef。语义 binding 为 99564113529d2a6ee2e6ef494ecfe162ba5c0fcc4810035173580fed4f78b899。执行身份及各完整输出 SHA 另登记在 notes/r150-bell-fourth-even-execution-789f/local-20261116-prepare.json。

新 field 源与 Q 源的实际 Python AST 检查已经通过；独立奇来源相消/全偶投影小例和分批原行选单位小矩阵乘回亦已通过。真实 Singular 的两级自测和后续数学任务尚未执行。

## 10. 官方接口依据

Singular Team，Singular 官方手册，slimgb、lift、degBound 各节；本次实际读过官方项目 doc/reference.doc 的 Git blob 67a64ee0438e7349d9fe2a1d53bcc1ddc98ca7dd。公开手册见 [Singular manual](https://www.singular.uni-kl.de/index.php/singular.pdf)。

该文档说明 slimgb 要求全局单项式序，degBound 对 slimgb 使用全等权总次数；lift 的第四参数允许 slimgb，来源方向为本文所列。程序仍以实际小例和全部原乘回核验本次安装的行为，不从文档直接填数学成功标记。

