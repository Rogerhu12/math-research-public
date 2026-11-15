# R150：剩余七个原来源方向的精确有理求解接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

状态：源码冻结，数学执行尚待实际回执。本程序不增加旧模 31 Dixon 位数、不重算旧正常形，也不重复 36 列候选恢复。它只解在 29 条真规范核已经闭合之后剩余的七列原有理图。

## 1. 已付输入和新的精确对象

同一所选来源矩阵为 $C_0\in\mathbb Z^{4367\times4354}$。由 [29 个规范真核](../results/R150-appendix-exact-twentynine-normalized-free-kernels-and-seven-direction-complement.md)，删去前 29 个自由来源列不改变有理列像，得到
$$
C_{\rm red}\in\mathbb Z^{4367\times4325}.
$$
被删列的真实关系来自原有理核；没有用模 31 的关系代替。

[唯一模 65521 计算](../results/R150-appendix-single-prime65521-rank-after-paid-twentynine.md) 已保存 4318 个原独立来源列和七个剩余列。其完整原矩阵及列 profile 在当前会话临时目录中：

| 输入 | 字节数 | SHA256 |
|---|---:|---|
| original-selected-columns-65521.bin | 37774570 | a9b89935d75f7c56fd8fe7becc142b7c84a7e1164b481170dc6d9790fe6d3fc3 |
| selected-65521-column-profile.json | 41202 | 523d3835e92d9a8747759c6fa5949c5aec1b452e6f78fc76db5a7455e4c5f66b |

新程序从原 17 式整数模型重新构造这些列的精确整数系数。新素数只负责选择原整数单位块，不能决定有理解。

## 2. 原输出 I 及单位块

由原 native 模型中的 3333 个输出主单项式和已存 1021 个原输出，准确恢复原 $I$，$|I|=4354$。程序同时核单项式键与原 4367 个输出编号一致。

令 $P$ 为已付的 4318 个来源列，$F$ 为剩余七列。先在 $C_{{\rm red},I,P}$ 的转置中模 65521 选取独立原行。若秩为 4318，则选出的单位行 $I_u$ 全属于原 $I$。如果这一限制秩不足，只允许改从完整 4367 行选单位行，并明确记录 unitRowsSubsetOriginalI=false；该分支不会把完整输出秩误写成原方阵秩。

在两种情况下，原整数方块
$$
B=C_{{\rm red},I_u,P}
$$
都有模 65521 非零行列式，因此在 $\mathbb Q$ 上可逆。记 $E=C_{{\rm red},I_u,F}$，唯一新的 native 有理任务为
$$
X=B^{-1}E
$$
的七个右端。FLINT 求解完成后先保存完整有理矩阵，再进入原乘回阶段。

## 3. 完整残差决定整个特征零补空间

原齐次来源在单位行上满足
$$
x_P=-Xx_F.
$$
因此以
$$
Z=\binom{-X}{I_7}
$$
表示完整七列有理图，按原来源位置恢复。各列清分母只乘非零常数，不改变图空间。

计算全部 4367 个原输出的残差
$$
R=C_{\rm red}Z.
$$
先核 $R_{I_u}=0$，这是原整数单位块的完整乘回。然后在所有七列上精确求 $\ker_{\mathbb Q}R$，不能只检查七个独立候选是否逐列为零。于是有双向参数化
$$
\ker_{\mathbb Q}C_{\rm red}=Z\ker_{\mathbb Q}R.
\tag{3.1}
$$
令 $r=\operatorname{rank}_{\mathbb Q}R$，则
$$
\dim\ker_{\mathbb Q}C_{\rm red}=7-r,\qquad
\operatorname{rank}_{\mathbb Q}C_0=4318+r.
\tag{3.2}
$$

如果 $I_u\subset I$，还可对同一 $R$ 限制到原 $I$，准确得到
$$
\operatorname{rank}_{\mathbb Q}B_0
=4318+\operatorname{rank}_{\mathbb Q}R_I.
\tag{3.3}
$$
否则程序只报告 $B_0$ 的已付上下界，不使用 (3.3)。

将 (3.1) 的每列恢复成完整 6188 维整数来源后，逐列核全部 4367 个原输出为零、全部 1834 个外来源为零，以及前 29 个自由坐标为零。最后核其尾部七个自由坐标的有理秩等于 $7-r$。所以它与已付 29 维空间直和，不会重复计数。

若 $R=0$，则七个新方向全成、两所选常块的秩都等于 4318。若 $R\ne0$，完整小核仍可能给部分真方向；程序将按实际秩精确报告，不把“七个单列各失败”误称为“所有组合失败”。

## 4. 单次执行、真实保存与接续

命令为：

~~~sh
python -B 2026-11-15-r150-seven-original-exact-rational-solve-789f.py \
  --helper PAID_HELPER \
  --point-model ORIGINAL_POINT \
  --native-model ORIGINAL_NATIVE_DICTIONARY \
  --prepared-model ACTUAL_EXACT_ORIGINAL_KOSZUL_MODEL \
  --prime-dir ACTUAL_SINGLE_PRIME65521_DIRECTORY \
  --out FRESH_OUTPUT_DIRECTORY \
  --seconds 600 --memory-mib 4096
~~~

数学共享 600 秒，每进程 4096 MiB。有限域转置选元、原整数输入构造、精确七列求解、全部来源乘回共用同一时钟。native 精确求解在受父进程墙钟约束的独立子进程中进行。

主回执为 seven-exact-rational-original-receipt.json。完整阶段按先后保存：

1. 原完整整数核心；
2. 原输出与单位行列 profile；
3. native 的完整精确有理解；
4. 原七列来源图；
5. 全 4367 行的完整残差；
6. 精确补空间的原来源基；
7. 每条完整原乘回证书及完整自由像。

同一输出目录加 --resume，可跳过所有已完整保存且绑定一致的阶段。native 尚未返回时没有虚构内部迭代检查点；该情况下保存的是真实输入及选元。数学源码、全部输入字节和映射参加绑定，恢复路径不参加绑定。

status=completed 才表示完整有理补空间已经认证；budget-exhausted 和 failed 保留真实完成点。大数组及完整来源只留当前任务临时目录，长期只保存源码、参数、运行号、小回执和哈希。

## 5. 适用范围

本次是同一物理无穷远常块的特征零问题。即使所有七个新核完成，也只先决定该常块秩；原所选子式的全部无穷远 Smith 厚度仍需真实高阶连接，原参数多项式目标的成员性也仍需独立来源。不能把常秩闭合写成整个 R150 或普通不变子空间问题已经完成。
