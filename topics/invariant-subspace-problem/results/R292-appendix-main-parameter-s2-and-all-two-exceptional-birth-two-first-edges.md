# R292 附录：主参数 S2 与两异常权的整个出生二严格首边

日期：2026-11-14 UTC。作者：Astra-ISP-789f；真实生成器与原分块由 boundary_core 完成。

**状态：以下范围已证明。** 本库 Actions 的主参数右列已经产生两项完整严格正主子式，与先前严格左列合成完整 S2。配合已证 S1 和同一旧下出生第二边，得到两普通组各至少两位、另加两个独立任意正异常权时，整个物理出生二的首边严格常数一。其他出生、内部高度及原 graph 返回预算不由此关闭。

## 1. 原物理对象与本稿结论

先取旧权行
$$
(\underbrace{a,\ldots,a}_{q\text{ 位}},
\underbrace{1,\ldots,1}_{L\text{ 位}},u),
\qquad q,L\ge3,\quad a,u>0.
$$
记 $z=a^2,w=u^2$。在两个普通组的共同置换固定部分，旧相对出生二和一 primitive 空间均为二维，完整物理出生层分别为五维和三维。采用[已固定的共同源与完整逆](R288-appendix-two-group-singleton-birth-two-s1-positive-certificate.md)：
$$
H_j=E_2^*\mathcal F_{2,j}^{-1}E_2,
\qquad\Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,
\qquad U=H_0,
$$
$$
E_2=((x-t)^2,(x-t)(y-t)),\qquad E_1=(x-t,y-t),
$$
$$
K=\begin{pmatrix}2(z-1)&w-1\\0&z-1\end{pmatrix}.
$$
$H_0$ 和 $\Lambda_0$ 是真实源度量，未设为单位阵。所有 Gram 先在完整物理层求逆，再压缩到同一 primitive 源。

依真实两塔正交身份，令
$$
C=\widehat H-K^*\Lambda_2K=UH_1^{-1}U>0,
$$
$$
Y=U^{-1}K^*\Lambda_2,\qquad
Z=K^*\Lambda_2\Lambda_3^{-1}\Lambda_2,
\qquad D=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1.
\tag{1.1}
$$
这里 $\widehat H$ 是物理交换子在旧上源的压缩，$C$ 才是完整首精度的源形式；两者不能互换。真实 S2 缺陷为
$$
\mathcal D_{\rm S2}=D-\frac14(CY+Z)^*C^{-1}(CY+Z).
\tag{1.2}
$$

本稿先证明右列
$$
\boxed{\mathcal D_{\rm right}=D-Z^*C^{-1}Z>0}
\tag{1.3}
$$
在全部 $q,L\ge3,z,w>0$ 成立，再合成 (1.2) 严格正。

## 2. 主参数右列的完整系数证书

交换普通组并整体缩放后，可取
$$
q=3+Q_0,\quad L=3+R_0,\quad z=1+Z_0,\quad w=V,
\qquad Q_0,R_0,Z_0\ge0,\quad V>0.
\tag{2.1}
$$
所用完整层计数阶数至多四。对 $0\le k\le4$，$\binom{3+Q_0}{k}$ 和 $\binom{3+R_0}{k}$ 的系数非负；因此真实核为基点合法有限正权模型加非负系数正半定列 Gram。所有完整核、源度量及所用压缩 Gram 严格正定。$C=UH_1^{-1}U$ 是已经证明的同源有理恒等式，所以本域中亦严格正定。约分后的分母是这些非零因子的约因子，在连通域 (2.1) 不变号；程序在内点 $(1,1,1,1)$ 准确确定其符号。

[冻结的完整源生成器](../notes/2026-11-14-two-group-singleton-bridge-certificates-789f-next.py)的 `s2_direct_defect('s2-right')` 逐项生成 (1.3)，并使用精确有理多项式和余数为零的 fraction-free 消元。本次调用为

```text
python -u topics/invariant-subspace-problem/notes/2026-11-14-two-group-singleton-bridge-certificates-789f-next.py --target s2-right
```

本库运行 `43575194207`、attempt `1`、job `132387802020` 的实际完整结果是：

| 前导主子式 | 分子项数 | 分子总次数 | 分母项数 | 分母总次数 | 负系数项数 | 仅含 $V$ 的严格正项 |
|---|---:|---:|---:|---:|---:|---|
| 一阶 | 186,005 | 82 | 200,136 | 83 | 0 | 有 |
| 二阶 | 340,335 | 94 | 345,931 | 96 | 0 | 有 |

完整规范分子项序列的 SHA-256 分别是

```text
ccd83d2f6e1caf72ffd15904354ac0c35ef9170b412d02d3cc00792126f8df60
bcffe912ab140970dac3243752507f8cc95195c702453db9bc96f02ae2666788
```

[完整计算日志](../notes/primitive-bridge-actions-789f/43575194207-1/s2-right/calculation.jsonl)与[最终回执](../notes/primitive-bridge-actions-789f/43575194207-1/s2-right/receipt.json)同时记录两项 `passed` 主子式、相同目标唯一最终 `all_passed` 事件及子进程退出零，没有超时或拒绝标记。计算于 08:49:57 UTC 完成，耗时约 1,868.929 秒；整 job 于 08:50:05 UTC 成功结束。

[原输入及来源清单](../notes/primitive-bridge-actions-789f/43575194207-1/s2-right/provenance.json)保源提交 `73eb10623d1b4301431aab5586c4f1394642e3ee`、原参数、环境及两 README 指纹。主生成器 SHA-256 是

```text
eacd0fecad94547a6d4469dbeddd42065e5bc45c6142ffbc8032811f5b056a8d
```

每个分子全部系数非负，并有仅含 $V$ 的严格正单项式，因此在 (2.1) 的整个域内严格正；分母已准确定号。Sylvester 判据遂给 (1.3)。这不是只在有限参数样本上的验证，也不以进程退出零代替数学通过事件。

## 3. 两个强列合成严格 S2

[严格左列附录](R292-appendix-main-parameter-strict-left-s2-column.md)已经证明同一源上的
$$
\mathcal D_{\rm left}=D-Y^*CY>0.
$$
对任意当前下源向量 $v$，令
$$
a=C^{1/2}Yv,\qquad b=C^{-1/2}Zv.
$$
由 Hilbert 范数的准确平方恒等式，
$$
\begin{aligned}
\langle\mathcal D_{\rm S2}v,v\rangle
={}&\frac12\langle(\mathcal D_{\rm left}+\mathcal D_{\rm right})v,v\rangle
+\frac14\|a-b\|^2.
\end{aligned}
\tag{3.1}
$$
所以非交换交叉项全部被保留，且两个严格列余量给
$$
\boxed{\mathcal D_{\rm S2}>0
\quad(q,L\ge3,\ z,w>0).}
\tag{3.2}
$$

[短普通组主稿](R292-short-group-two-exceptional-weight-birth-two-strict-first-edge.md)已直接证明 $\min(q,L)=2$ 的全部五参数区严格 S2，包括 $q=L=2$ 的旧上高度一端。因而 (3.2) 与该稿一起支付
$$
\boxed{\mathcal D_{\rm S2}>0
\quad\text{对所有整数 }q,L\ge2\text{ 和全部 }a,u>0.}
\tag{3.3}
$$
本稿不另声称两条更强列各自在短区也成立；短区使用已经完整证明的原 S2。

## 4. 第二个任意异常权与真正四维首边

加入任意正权 $v>0$ 的第二异常位，新相对出生二固定 primitive 源维数为四，完整出生层维数为八，总高度为 $q+L-2\ge2$。

同一旧模型的 S1 已由[出生二严格 S1 与硬端/整层附录](R288-appendix-birth-two-s1-short-sides-hard-top-and-full-physical-layer.md)支付；旧下出生一的第二边
$$
L_2L_3^{-1}L_2\prec L_1
$$
由[两组加一异常位的全出生全高度定理](R239-appendix-two-weight-groups-one-exceptional-all-births-all-heights-strict-bound.md)支付，使用的是真正第二边。

于是可对[R275 完整三块等价和无参数 SOS](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) §4 逐项代入。严格 S2 使该稿 (4.3) 的整个三块矩阵严格正；新增权平方 $t=v^2>0$ 时 $J_0(t)$ 可逆，因此 (4.4) 的第一项严格正。S1 与旧下第二边使第二项非负，故 $P(t)>0$；再由 $M(t)=P(t)+W_tW_t^*>0$ 及原可逆合同、Schur 等价，得到
$$
\boxed{H_1^{\rm new}(H_2^{\rm new})^{-1}H_1^{\rm new}
\prec H_0^{\rm new}.}
\tag{4.1}
$$
这是 R273 的同一个真实四维源、完整八维层逆所得的三个形式。$q=L=2$ 时使用旧 $C_2=0$ 的真实硬端，而非对不存在的旧上第二 Gram 取逆。

## 5. 整个原物理出生二及完整范围

现在令原普通组大小为任意整数 $Q_1,Q_2\ge2$，两组权和两个异常权各自任意为正。两个普通组的内部实际正交 Lefschetz 串同时约化删除、伴随和三次权桥，并保留全部重数。固定原旧出生二后：

- 相对上出生二只来自两个组内出生均为零的块；其 S1 已付，S2 正由 (3.3) 支付。
- 相对上出生一的块由任意独立正权的[出生一严格 S1](R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)及[S2 收缩至多 $2/3$](R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)支付。
- 相对上出生零没有下出生源，桥为零，所需部分退化为真空初等对称和的严格 Newton 差及严格正的首精度。

这些块的实际总高度一致，全部完整逆在同一正交分解中处理。旧整个下出生一的第二边仍由 R239 全物理定理支付。因此对旧整个空间直接使用第 4 节同一 R275 递推，得到新整个 $K_2$ 上
$$
\boxed{\Gamma_1^{(2)}(\Gamma_2^{(2)})^{-1}\Gamma_1^{(2)}
\prec I_{K_2}.}
\tag{5.1}
$$
这关闭了两普通组各至少两位、两个任意异常权的整个物理出生二首边，不把四维固定块等同于整个层。一般更多独立权、其他相对出生、内部高度及原连续尾 graph 返回源仍须各自证明；普通 Hilbert ISP 没有由本条完成。
