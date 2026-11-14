# R133 补篇：最终 ac1 中心的完整 ν 源、5M 核与全部真实接口

2026-11-14。**已证明（实际完整原生计算）**。本篇消费恢复后的同一最终中心，不更换度量参数、Fourier 系数或径向插值。结论是完整参数源及伴随核的严格界；这里没有提供伴随解，也没有声称真实 ν Schur 非零或全 BVP 可逆。

## 1. 实际输入与范围

候选完整索引 SHA256 为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`。
其五个完整压缩分片已由六步真实重放恢复原字节；本次读取全部 M=32 的物理 moving 系数，未把 moving Fourier 当成物理角 Fourier。参数保持

$$
\alpha=\frac{6890507429876859}{9007199254740992},\qquad
\nu=-\frac{2572625729470897}{72057594037927936}.
$$

原目标的完整 affine 区间为原中心加减 $10^{-9}$，所有 primitive 尾仍使用原有向区间提供器。准确控制函数为

$$
w(r)=4096t^6(1-t)^6,\qquad
t=\frac{r-1/20}{13/100},\qquad 1/20<r<9/50,
$$

区间外为零。计算覆盖该支集的全部 1156 个共同闭盒，含候选 PPoly 节点和原目标 germ 节点；另外计算支集内部全部 864 个真实候选接口。不存在径向采样替代连续闭盒，也没有删掉均值。

本次使用未修改的 [完整核 producer](../scripts/fourfold_codazzi_nu_full_adjoint_kernel.py)，源 SHA256 为
`09807e405455b58c043a5ff26b7ff5e4e1569a96c81ecd860125552bfba95a3b`。

## 2. 被实际消费的完整恒等式

沿用 [完整 ν 伴随与双残差证明](R133-supplement-complete-nu-adjoint-and-dual-residual-Schur.md) 的物理未规范化方向和号数。令 $Q=(u,v)$、$m=\langle v\rangle$、$\mathcal D=\partial_r-D_QF$。目标 $E_\nu=E\exp(\nu w)$ 给出

$$
\partial_\nu\gamma=\frac{w\gamma}{2},\qquad
\partial_\nu K=-wK+Tw',\qquad T=\frac{\beta}{2E_\nu}.
$$

令 $I$ 为去均值原函数，$Q_\phi=(u_\phi,v_\phi)$，并置

$$
W=I(v^2)Q_\phi+v^2Q,
$$
$$
A=-\beta T W+(\gamma mT v_\phi,0),\qquad
B=\beta K W-\frac{\gamma m}{2}(K v_\phi,u_\phi),\qquad
G=B-\mathcal D A.
$$

则真正参数源准确为

$$
F_\nu=\partial_\nu F=w'A+wB.
\tag{N.1}
$$

这里 $\mathcal D A$ 包括全部局部矩阵、$I(uh_1+Kvh_2)$ 项和 $\langle h_2\rangle JQ_\phi$ 项。$A_r$ 使用真实保存 PPoly 的导数及原目标导数，不把中心当作已解 PDE。完整 $A,B,A_r$ 支持至 $3M$，$G$ 支持至 $5M=160$；512 点卷积网格容纳所有这些系数，代码核对支持，不作循环截断。有限 Fourier 系数的区间半径和原目标无限尾全进入界。

对连续的真正伴随 $\mathcal D^*\psi=0$，逐片分部积分、保留每个 $A$ 的右减左跳，得到

$$
\int_{1/20}^{9/50}\langle\psi,F_\nu\rangle\,dr
=\int_{1/20}^{9/50}w\langle\psi,G\rangle\,dr
-\sum_iw(r_i)\langle\psi(r_i),[A]_i\rangle.
\tag{N.2}
$$

外端项因 $w$ 在支集两端为零而准确消失。近似伴随仍需其完整体残差和自身跳量；本篇不把 (N.2) 免费应用给未认证的伴随提案。

## 3. 完整计算与严格数值界

每个闭盒先包全部实际有限系数及目标。把两分量 Wiener 范数的欧氏和作为真实向量 $L^2_\phi$ 的上界，代码按准确有理数积分 $w$，并准确计算每盒 $\int|w'|$。因此

$$
\begin{aligned}
\|F_\nu\|_{L^1_rL^2_\phi}
&\le\sum_J\left(\int_J|w'|\sup_J\|A\|_{A^0}
 +\int_Jw\sup_J\|B\|_{A^0}\right),\\
\int w\|G\|_{L^2_\phi}
&\le\sum_J\int_Jw\sup_J\|G\|_{A^0}.
\end{aligned}
$$

每个接口用同一目标值和真实左右 PPoly 构造完整 $[A]$，不以节点拟合误差代替真实跳。全部 1156 盒和 864 接口实际完成后，有严格界：

| 完整量 | 严格上界 |
|---|---:|
| $\|F_\nu\|_{L^1_rL^2_\phi}$ | $1.964956$ |
| $\int w\|G\|_{L^2_\phi}\,dr$ | $625.523019$ |
| $\sum_iw(r_i)\|[A]_i\|_{L^2_\phi}$ | $8.072489\cdot10^{-19}$ |
| 上述 $G$ 积分与全部跳费之和 | $625.523019$ |

最后一行来自先相加再有向比较，未把第三行舍为零。因而 (N.2) 的绝对值小于 $625.523019\|\psi\|_{L^\infty_rL^2_\phi}$；直接消费 (N.1) 另给更小的 $1.964956\|\psi\|_{L^\infty_rL^2_\phi}$。完整 $G$ 的保存用途是之后保留符号的伴随配对，当前粗绝对界没有被包装成改进或非零证明。

## 4. 可重算记录与边界

实际过程正常 exit 0，墙钟 994.33 秒、峰值 RSS 210412 KiB。完整 [原生报告](../notes/2026-11-14-R133-final-complete-nu-source-kernel-native.json.gz) 为 2924838 字节，SHA256
`281fa7c17d16b8f6823883df7ff61fc12f9c846c6b98bdd6951eed928d480848`；每个闭盒、有限核系数包络、真实目标 germ、每个接口、完整输入与依赖身份均保留。过程记录见同名前缀的 `-process.json`。

[小的有向消费器](../scripts/fourfold_codazzi_final_nu_kernel_readable.py) 再核同一原生身份、完整闭盒邻接和接口计数，并以 320-bit Arb 严格验证上述四个可读上界；其 [报告](../notes/2026-11-14-R133-final-complete-nu-source-kernel-readable.json) 不替代完整原生数据。

复算主计算：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python3 -u \
  scripts/fourfold_codazzi_nu_full_adjoint_kernel.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --out /tmp/full-nu-kernel.json.gz
```

这次 native 的完整性只指原目标、全部系数和控制支集的完整覆盖。实际响应、实际伴随、全边界误差、全频补逆、Schur 非零以及非线性问题仍分别以它们自己的证据消费，不从本表推得。
