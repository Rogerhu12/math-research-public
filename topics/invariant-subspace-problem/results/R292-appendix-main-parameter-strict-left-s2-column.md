# R292 附录：两普通组加一异常位：出生二 S2 左列的严格主参数定理

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：本稿的严格左列估计已证明。** 它是 R275 的 S2 的两个更强充分列估计之一；单独这一列不等于完整 S2。当前结论由本库 Actions 的两项完整主子式证书得到，保留原共同源和物理度量。

## 1. 实际命题与共同源

取 $q$ 个权 $a>0$ 的物理位、$L$ 个权 $1$ 的物理位和一个权 $u>0$ 的异常位，其中 $q,L\ge3$。记
$$
z=a^2,\quad w=u^2,\quad d=\sum_i b_iE_i,\quad C=\sum_i b_i^3E_i.
$$
在两个普通组的共同置换固定部分中，令 $K_2,K_1$ 分别为相对出生二和一的 primitive 空间，均为二维。完整出生层分别为五维和三维。按照[真实源和完整逆定义](R288-appendix-two-group-singleton-birth-two-s1-positive-certificate.md)，取
$$
G_j=\Gamma_{j,2},\quad L_j=\Gamma_{j,1},\quad
C_1=G_1^{-1},\quad B=C|_{K_2}:K_2\longrightarrow K_1.
$$
这些 $\Gamma$ 始终先在完整物理层取逆再压缩到 primitive 源。置 $Q=B^*L_2$，其中 $B^*$ 是原 Hilbert 伴随。

**定理。** 对全部上述整数 $q,L\ge3$ 和任意 $a,u>0$，在整个实际 $K_1$ 上严格有
$$
\boxed{Q^*C_1Q+L_1L_2^{-1}L_1<I_{K_1}.}
\tag{1.1}
$$
旧上高度为 $q+L-3\ge3$，旧下高度为 $q+L-1\ge5$，所以本式所用的 $G_1,L_1,L_2$ 以及生成器使用的 $L_3$ 均合法。

在去权后聚合源
$$
E_2=((x-t)^2,(x-t)(y-t)),\qquad E_1=(x-t,y-t)
$$
中写
$$
H_j=E_2^*\mathcal F_{2,j}^{-1}E_2,\quad
\Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,\quad U=H_0,
$$
$$
K=\begin{pmatrix}2(z-1)&w-1\\0&z-1\end{pmatrix},\qquad
\widehat H=E_{2,\rm phys}^*[d,d^*]E_{2,\rm phys}.
$$
真实两塔正交身份给出
$$
C_{\rm form}=\widehat H-K^*\Lambda_2K=UH_1^{-1}U>0.
\tag{1.2}
$$
特别 $C_{\rm form}$ 是 $C_1$ 的物理二次型，不能用粗压缩 $\widehat H$ 替代。令
$$
Y=U^{-1}K^*\Lambda_2,\qquad
D_{\rm low}=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1.
$$
则 (1.1) 的准确同源坐标缺陷为
$$
\boxed{\mathcal D_{\rm left}
=D_{\rm low}-Y^*C_{\rm form}Y>0.}
\tag{1.3}
$$
$H_0,\Lambda_0$ 均保留真实物理源度量；(1.3) 没有将它们置为单位阵，也没有把普通转置误当作非正交源的物理伴随。

## 2. 全参数的精确系数证书

交换两个普通组并整体缩放，可取 $z\ge1$。物理式 (1.1) 在整体缩放 $b_i\mapsto cb_i$ 下不变：$C_1$ 乘 $c^2$、$Q$ 乘 $c^{-1}$，且 $L_1L_2^{-1}L_1$ 不变。因此只须证明
$$
q=3+Q_0,\quad L=3+R_0,\quad z=1+Z_0,\quad w=V,
\qquad Q_0,R_0,Z_0\ge0,\quad V>0.
\tag{2.1}
$$
下标用来区分辅助实参数与 (1.1) 的算子 $Q$。冻结源码中的变量名是 $Q,R,Z,V$，另一个未使用的代数变量 $U$ 不影响任何结果。

该式所需完整层计数阶数至多四；$\binom{3+Q_0}{k}$、$\binom{3+R_0}{k}$ 对 $0\le k\le4$ 有非负系数。因此完整核在 (2.1) 上都是基点合法正定模型加非负系数正半定列 Gram。所有物理对角、完整层逆、$U^{-1}$ 及 $\Lambda_2^{-1}$ 均合法。式 (1.2) 是一般的真实有理恒等式，在此同一表达式域仍成立。约分后分母是这些非零因子的约因子，故在连通域 (2.1) 上不变号，并可由一个内点定号。

本库工作流 `invariant-subspace-primitive-bridge.yml` 的 run `43575194207`、attempt `1`、job `132387801844` 实际执行冻结的[完整源生成器](../notes/2026-11-14-two-group-singleton-bridge-certificates-789f-next.py)：

```text
python -u topics/invariant-subspace-problem/notes/2026-11-14-two-group-singleton-bridge-certificates-789f-next.py --target s2-left
```

该路径的 `s2_direct_defect('s2-left')` 正是 (1.3)，完整物理表示已由原有有理校准核对。它使用精确有理多项式运算和逐次余数为零的 fraction-free 消元，没有浮点求逆或参数抽样。两个主子式按分母在 $(Q_0,R_0,Z_0,V)=(1,1,1,1)$ 的符号规范后，完整扫描结果为：

| 前导主子式 | 分子项数 | 分子总次数 | 分母项数 | 分母总次数 | 负系数项数 | 仅含 $V$ 的严格正项 |
|---|---:|---:|---:|---:|---:|---|
| 一阶 | 44,149 | 56 | 48,902 | 57 | 0 | 有 |
| 二阶 | 47,944 | 56 | 48,902 | 58 | 0 | 有 |

完整规范分子项序列的 SHA-256 分别为

```text
740e4a9a0c28d66c07ca6086bd8330bfdcd88c596a16fc44871a41f3c67a491f
b4a65d1fb3a25ea550f9731bfb89f1c2bb7295fe91f35b84beb74fd04b20f2bd
```

每个分子的全部系数非负，且在 $Q_0=R_0=Z_0=0,V>0$ 仍有严格正项。因此两个主子式在整个 (2.1) 上严格正。Sylvester 判据给 (1.3)，再按真实源同余恢复得到 (1.1)。

## 3. 完整运行凭据与准确范围

[输入及源码清单](../notes/primitive-bridge-actions-789f/43575194207-1/s2-left/provenance.json)记录实际源码提交 `73eb10623d1b4301431aab5586c4f1394642e3ee`、两份 README 指纹、全部参数及源码 SHA-256。所用主生成器的 SHA-256 为

```text
eacd0fecad94547a6d4469dbeddd42065e5bc45c6142ffbc8032811f5b056a8d
```

[完整小日志](../notes/primitive-bridge-actions-789f/43575194207-1/s2-left/calculation.jsonl)与[实际回执](../notes/primitive-bridge-actions-789f/43575194207-1/s2-left/receipt.json)同时包含两项 `passed` 主子式、相同目标的唯一最终 `all_passed` 事件和进程退出零；计算耗时约 26.984 秒。结论不只依赖进程退出零。

这个严格左列估计加强了同一旧下出生的普通首边，并支付了真实上出生桥的一项额外费用。完整 S2 还需要处理右列
$$
Z^*C_{\rm form}^{-1}Z\preceq D_{\rm low},\qquad
Z=K^*\Lambda_2\Lambda_3^{-1}\Lambda_2,
$$
或直接控制两列之和。本稿不把左列单独称为 S2，也不据此宣称主参数区加入第二异常位后的四维首边已经完成。已证短普通组的完整 S2 和四维首边仍由 [R292](R292-short-group-two-exceptional-weight-birth-two-strict-first-edge.md) 保持。
