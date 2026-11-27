# R150 unit211：h=k、Q=1−u 的 Delta 零分支与整个碰撞面排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 1. 完整结论

**原 h=k 碰撞图上的整个 Q=1−u 面无解。** [Delta非零整面](R150-appendix-unit211-equal-singleton-Q1u-nonzero-Delta-complete-exclusion.md)已经在完整 C2/C6/C24 常数代数返回。本篇完成互补 Delta=0：完整 C6 由三条原相容式返回单位；完整 C24 恢复同一个 u，保留自由原 Gram 参数 f 后由原 E1/EBe 返回单位。

因此在剩余 h=k 原图中可以支付 u+Q−1。证明不调用旧 D≠0 值图的同名排除，不选择代数根，也不删除首项为零的纤维。整个 h=k 图及普通 Hilbert ISP 仍未完成。

## 2. 原相容与完整常数覆盖

采用[完整lambda覆盖](R150-appendix-unit211-equal-singleton-Q1u-complete-lambda-cover.md)中的同一原参数。令

$$
 A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad \ell=A^3/B^2,
$$
$$
 T=A^2/B,\quad h=k=1+\xi,\quad Q=1-u,\quad \rho^2=u.
$$

原两条仿射式为

$$
 P_c+P_f f+bcQ\Phi t=0,\qquad
 N_C+N_F f+bcQS\xi t=0.
$$

它们的完整消元身份给

$$
 \Delta=\Phi N_F-S\xi P_f,\quad
 F=S\xi P_c-\Phi N_C,\quad
 T_n=P_fN_C-P_cN_F,
$$
$$
 P_fF+\Phi T_n+P_c\Delta=0,\qquad
 N_FF+S\xi T_n+N_C\Delta=0.
$$

在 Delta=0 原解上，三个多项式 Delta、F、Tn 均为零。前页已经用固定原投影支付完整 QQ 覆盖 C6 C24；两因子的全部精确系数保在前页及冻结源。

本次分别取

$$
 K_6=\mathbb Q[\lambda]/(C_6),\qquad
 K_{24}=\mathbb Q[\lambda]/(C_{24}),
$$

将三条原相容式完整送入 K_j[u]。每个常数逆均由 QQ 扩展 Euclid 乘回；遇非单位时算法保留两个完整因子分支。实际均不需要分拆。全部原分母和剥除因子都从此前已支付的原单位取得，本次相容分子中实际剥除的非恒定 gcd 来源仅为 Q。没有倒置 Delta 或 N_F。

## 3. 完整 C6 原相容直接排空

在 K6[u] 中，剥除已付原单位后，Delta、F、Tn 的 u 次数分别为 1、2、2。真实扩展 Euclid 的全部原组合乘回给

$$
 a(u)\Delta_{\rm prim}
 +b(u)F_{\rm prim}
 +c(u)(T_n)_{\rm prim}=1.
$$

这里的 primitive 与原式之比都是逐次核回的原单位，故这条恒等式排除 C6 的全部复嵌入和全部 u。没有先挑某个 u 根再判断。

## 4. 完整 C24 恢复同一个 u，并保留自由 f

在 K24[u] 中，三个相容分子的 u 次数分别为 2、3、3，准确公共 gcd 为

$$
 u-u_0(\lambda).
$$

程序返回其全部24个有理系数，SHA256 为
3512281297b8a3bdb50775903b406c0bdf230fffea97738c966b9638aa420862。
该小多项式的完整系数在回执，不保存可重算的大矩阵。

在这个同一 u0 上逐式核回 Delta=F=Tn=0；原 Q、rho²、bc、Phi、Pf、S 及其余所用原单位都给真实常数逆。取自由 f，定义

$$
 t=-\frac{P_ff+P_c}{bcQ\Phi}.
$$

原 P1 与 NV 两条仿射式对整个自由 f 逐项等于零。这里 Phi 的合法性来自此前 h=k 的整个 Phi=0 排除；没有把 Delta=0 当作可除的量。

随后在 K24[f,rho]/(rho²−u0) 中重建同一原 Gram。其原权为

$$
 b=\frac{\ell}{2}+\frac{u_0-\ell}{2u_0}\rho,\qquad
 c=\frac{\ell}{2}-\frac{u_0-\ell}{2u_0}\rho,
\quad p=1+\rho,\ q=1-\rho.
$$

原均值、二三矩、E0/N0/P1/NV，以及两个孤立谱值的独立 N/P 目标全部乘回。偶奇系数等价使用两个实际 B/C 原式与 rho≠0，不以单条共轭式替代两个原条件。

完整八式的 f 次数依次为

| 原式 | E1 | EBe | EBo | N1 | NBe | NBo | PBe | PBo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| f次数 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 |

其中前两条就给准确恒等式

$$
 a(f)E_1(f)+b(f)E_{B,e}(f)=1
 \quad\hbox{于 }K_{24}[f].
$$

每一次除法、全部系数和最终组合均实际乘回。完整可再生证书82976字节，SHA256为
83560bf88007fe2d944910a378ebc352d6e24bfc2071e3c9091b4dab20a9f258。
按仓库规则只保存源、准确参数、摘要与小回执。

任一原解必须给 K24 的某个复嵌入，并使这两个原均值同时为零，与单位恒等式矛盾。结合第3节，Delta零整面排空；再结合此前 Delta非零定理，得到第1节整个 Q=1−u 面的结论。

## 5. 新输入与实际运行

[冻结原返回源](../notes/2026-11-27-unit211-equal-singleton-Q1u-Delta-zero-complete-finite-original-return-8542.py)：

- blob e314dbbd2e6c0e3762442ed03ae2e9783bf78a5f，16488字节；
- SHA256 54f9a5098986eb3c0f706b32ef3387b220b2b4d1f1aad2fc9c0ef4b77f67d114；
- 依赖2298源仅执行原相容构造前缀，不重算旧投影或因式分解；
- 实际 run46021956889 / job140583573322，内层退出0；
- 源0.827676439秒，驱动0.895036079秒，峰值42304KiB；
- 528个真实常数逆，325次多项式除法，无常数分拆；
- stdout10967字节，SHA256 5e60b5651bb8eaebcf210c3641aca5fea2d0aecf4ef757afc65ea972337eba1f；
- Python3.12.14、python-flint0.9.0、单线程，源限180秒/4GiB；
- 真实pull为2026-11-27 15:07:06.430280 UTC，提交e20a2cfce88602a32cc996c1b174850b49feae81，两README无差异。

[实际原返回与小回执](../notes/2026-11-27-unit211-equal-singleton-Q1u-Delta-zero-and-entire-face-exclusion-receipt-8542.json)。继续其余 h=k 原输入；本页不关闭别的未付碰撞或算子接口。
