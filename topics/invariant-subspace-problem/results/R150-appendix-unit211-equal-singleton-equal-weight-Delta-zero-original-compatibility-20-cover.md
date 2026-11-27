# R150 附录：等单点值、等权的 Delta 零面原相容式与完整二十次覆盖

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 结论与准确范围

在原 unit211 非零孤立 mean 图中，限制到 $h=k\ne1$、$b=c$、$\Delta=0$。此前整个 $S=0$ 原支已经排除。本稿从**两条原仿射值方程**推出三条相容多项式，再以固定阶 QQ Sylvester 行列式保留所有首项零纤维，得到必要条件
$$
\phi_{20}(\lambda)=0.
$$
其中按 $\lambda$ 升幂排列的完整整系数为
$$
(-3,52,-392,1470,-414,-29126,199932,-829326,2534173,
-6080694,11783324,-18678024,24316352,-25940944,22500320,
-15651136,8547840,-3547392,1058304,-202752,18432).
\tag{0.1}
$$
这是**原支的必要有限投影**，尚非该支排空；自由 Gram 参数仍须返回全部原 mean、N、P 方程。本稿没有除以 $\Delta$，没有用旧 $D\ne0$ 权图排除来处理这里的 $D=0$。

来源：[等值图原 Gram 与首一四次](R150-appendix-unit211-equal-singleton-values-full-original-Gram-and-Delta-quartic.md)、[完整权不变量原八式](R150-appendix-unit211-equal-singleton-invariant-weight-full-original-system.md)、[等权 Delta 非零整支](R150-appendix-unit211-equal-singleton-equal-weight-Delta-nonzero-complete-exclusion.md)。后者只处理互补的 $\Delta\ne0$ 图，并不替代本稿。

## 1. 在相容式之前固定原等权图

置
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad \ell=A^3/B^2,\quad
T=A^2/B,\quad w=\lambda-1-T.
$$
原 $h=k$ 的 moment 方程给 $h=k=1+\xi$。令
$$
p=1+\rho,\quad q=1-\rho,\quad Q=pq,\quad d=\rho^2=1-Q.
$$
本稿从一开始即置 $u=\ell,\ b=c=\ell/2,\ bc=\ell^2/4$。所有计算在 $\mathbb Q[\lambda,Q]$ 的有理函数域中重建，不是先对一个已删除退化面的消元式代入。

继续记
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
G_0=\lambda P_{02}-(1-u)T_0,
$$
$$
S=2\xi+3-2\lambda,\qquad \eta=\xi+3-2\lambda.
$$
原系数准确为
$$
P_f=T_0(J-Q),\quad
P_c=QP_{02}(\ell+T)-G_0T_0,
$$
$$
N_f=(3-4\lambda)Q+J\xi\eta,\qquad
N_c=\eta(-G_0\xi+Qwu).
\tag{1.1}
$$
自由 Gram 参数为 $f,t$。原仿射行是
$$
P_c+P_f f+bcQ\Phi t=0,\qquad
N_c+N_f f+bcQS\xi t=0.
\tag{1.2}
$$

## 2. 不作任何 Delta 逆的两条系数恒等式

定义
$$
\Delta=\Phi N_f-S\xi P_f,\quad
F=S\xi P_c-\Phi N_c,\quad
T_{\rm num}=P_fN_c-P_cN_f.
$$
把 (1.2) 的三系数行分别写作 $r_P,r_N$。源逐系数实际返回
$$
S\xi r_P-\Phi r_N=(F,-\Delta,0),\qquad
P_f r_N-N_f r_P=(T_{\rm num},0,-bcQ\Delta).
\tag{2.1}
$$
故每个原 $\Delta=0$ 点必满足
$$
\boxed{\Delta=F=T_{\rm num}=0.}
\tag{2.2}
$$
即使 $\Phi,P_f,N_f$ 的某些首项退化，(2.1) 仍是完整多项式恒等式；没有按非零 pivot 丢弃其中任何分支。

分母逐项审计，只含 $A,B,Q,d$。从三个分子剥离的因子只来自已付原单位 $A,B,Q,d,\lambda,bc,P_{02},S$；特别 $\Delta$ 不在剥离名单内。每步除法均回乘。得到的 primitive 多项式记 $D_*,F_*,T_*$：

| 原相容式 | $(\deg_\lambda,\deg_Q)$ | 项数 | primitive SHA-256 |
|---|---:|---:|---|
| $\Delta$ | $(14,2)$ | 43 | 7a33688c2669612d2d0b98bf7cd63850518cddafc324b3a5ab460d76607e0e42 |
| $F$ | $(18,2)$ | 53 | d14b44d30da163799bd4723db5af36a20f29b948a89910743d5c646f7ae0eb98 |
| $T_{\rm num}$ | $(16,2)$ | 47 | 0293f8bc3f16220835ebdf212d69aba399cb9a60d741a01a17ed1067c9f24ae3 |

三者完整 QQ 分解及乘回均返回。三元多项式 gcd 为 1 只说明无共同曲线因子，**不据此宣称点集空**。

## 3. 固定四阶原投影及二十次 QQ gcd

对三对原二次 $Q$ 多项式构造固定 $4\times4$ Sylvester 矩阵。在任何共同有限 $Q$ 根，矩阵均奇异，即使其名义二次首项同时为零，行列式必要条件也仍成立。源重建全部原矩阵行，没有把参数首项当单位。

| 原对 | 固定矩阵阶数 | 原行列式 $\lambda$ 次数 | 仅付原单位后的次数 |
|---|---:|---:|---:|
| $(D_*,F_*)$ | 4 | 61 | 26 |
| $(D_*,T_*)$ | 4 | 53 | 23 |
| $(F_*,T_*)$ | 4 | 63 | 32 |

对这三个真实 QQ 一元多项式依次计算扩展 gcd，全部 Bézout 乘积实际返回，次数依次为 $26,20,20$。最终 monic gcd 是 $\phi_{20}/18432$，其完整升幂有理系数 JSON 为 252 字节，SHA-256
$$
\texttt{611a05de6351205acf2f03a4d8155d14c5cd0701f90a4c00fe6607cac2b3fbcc}.
$$
完整 QQ 因子乘回给 (0.1)，重数为 1。该整系数数组 JSON 为 199 字节，SHA-256
$$
\texttt{bcb9f71ec6331465d70af44bdc090b78740c5ab2dfac45f19f5ddea8af3e69b5}.
$$
因每个原点使三个投影同时为零，Bézout 恒等式即得 (0.1)。这个推导只用必要投影，无须假设投影充分，也不从模素数的点数作 QQ 纤维排空。

## 4. 实际执行与后续原输入

实际源：[原相容源](../notes/2026-11-27-unit211-equal-singleton-equal-weight-Delta-zero-original-compatibility-8542.py)。

- 源 git blob：6f3b6287c9de304c1207eeb97c499e7bd7a06d2c。
- SHA-256：05660258ea899a7efa008c2673a9f28141852029bbf15980a660758827fd632e。
- [Actions run 46006075459](https://github.com/Rogerhu12/math-research-public/actions/runs/46006075459)，job 140529457924，inner exit 0；源 0.017395393 秒，驱动 0.088116707 秒，子进程峰值 40020 KiB。
- Python 3.12.14、python-flint 0.9.0、单线程，180 秒/4 GiB上限；实际 stdout 18365 字节，SHA-256 fa1dbd93f8db8df3a0d5b5823ca1d78d07f990bcbb732dd8670f1a39e9345e26。
- [小回执](../notes/2026-11-27-unit211-equal-singleton-equal-weight-Delta-zero-20-cover-receipt-8542.json)保存全部已成相容式、投影与 gcd 返回；不保存可重算大对象。
- 该执行于 2026-11-27 13:19:24 UTC 实际 pull 到 c1bd68ef5987d6c735b8b36e5a42711454773415，两 README 无差异。

接续输入是在完整 $\mathbb Q[\lambda]/(\phi_{20})$ 中返回三相容式的 $Q$ gcd；每个系数逆用 QQ 扩展 gcd 回乘，若非单位则保留两条常数分支。只有在真实恢复的 $Q$ 图上，才用原已付系数 $bcQS\xi$ 从第二原行解 $t$，保留自由 $f$ 并重建全部原 Gram 方程。此输入已另存，不把尚未执行的结果写成本稿结论。一般不等权 $h=k$、其他原面、物理第五列与普通 ISP 继续开放。
