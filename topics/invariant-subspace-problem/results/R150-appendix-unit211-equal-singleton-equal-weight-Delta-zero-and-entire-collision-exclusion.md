# R150 附录：等单点值、等权的 Delta 零面完整原返回及整个等权碰撞排除

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 结论

原 unit211 非零孤立 mean 图中，整个 $h=k,\ b=c$ 碰撞支为空。这里的物理 $D=0$，结论由该碰撞图自己的原方程得到。

此前 $h=k=1$ 已排除；[等权 Delta 非零整支](R150-appendix-unit211-equal-singleton-equal-weight-Delta-nonzero-complete-exclusion.md)已完成。本稿补齐唯一互补的 $\Delta=0$ 支：在[原相容式给出的完整二十次常数代数](R150-appendix-unit211-equal-singleton-equal-weight-Delta-zero-original-compatibility-20-cover.md)中，保所有 $\lambda$ 嵌入，恢复原 $Q$，保自由 Gram 参数 $f$，重新返回全部原方程，并实际得到两个原 mean 行的 Bézout 恒等式 $1$。

因此现在可以在**整个 $h=k$ 原碰撞图**支付 $b-c\ne0$，等价地支付 $u-\ell\ne0$。本稿不需要、也不引用旧 $D\ne0$ 权图的等权排除；一般不等权碰撞及普通 ISP 继续开放。

## 1. 完整常数代数与真实原相容 Q 纤维

沿用前稿
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad \ell=u=A^3/B^2,
\quad T=A^2/B,\quad w=\lambda-1-T.
$$
令 $K=\mathbb Q[\lambda]/(\phi_{20})$，其中 $\phi_{20}$ 是前稿完整整系数多项式。**不先选一个根，不假设所有系数都是单位**。实际每个系数逆都用 QQ 扩展 gcd 证明与 $\phi_{20}$ 互素，并在 $K$ 中乘回。如果出现非单位，源码会按真实 gcd 把常数多项式分为两支、保留两边；本次完整执行没有遇到这种分裂。

前稿三原必要式 $\Delta,F,T_{\rm num}$ 的 primitive 多项式在 $K[Q]$ 中逐次扩展 gcd。全部三个原行的标签乘回，最终恰为
$$
Q-Q_*(\lambda).
\tag{1.1}
$$
首一一次 gcd 的完整升幂系数 JSON 为 485 字节，SHA-256
$$
\texttt{e52006f386b4529b924a88e420e550280e1f3940dfb9c0d64beb6b9bc0b0ab31}.
$$
完整 $Q_*$ 系数保存在小回执。源码还把三个原相容式在 $Q_*$ 上全部代回为零。因为 (1.1) 是原三行的实际 Bézout 组合，所有原点都落在这个 $Q$ 纤维；没有按一般参数的首项忽略特殊 $\lambda$。

在同一个完整 $K$ 中，原已付单位 $A,B,Q,d=1-Q,\lambda,bc,P_{02},S$ 及后续分母全部真实返回可逆；每次都验证逆的乘积。此处可逆性是完整常数代数中的事实，未从“某个原点非零”推断其范数非零。

## 2. 不倒 Delta，保自由 f 的原 Gram 重建

记
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
G_0=\lambda P_{02}-(1-u)T_0,
$$
$$
S=2\xi+3-2\lambda,\quad\eta=\xi+3-2\lambda,
$$
$$
P_f=T_0(J-Q),\quad P_c=QP_{02}(\ell+T)-G_0T_0,
$$
$$
N_f=(3-4\lambda)Q+J\xi\eta,\quad
N_c=\eta(-G_0\xi+Qwu).
$$
原第二仿射行的 $t$ 系数 $bcQS\xi$ 已付，所以在 $K[f]$ 中准确取
$$
t=-\frac{N_f f+N_c}{bcQS\xi}.
\tag{2.1}
$$
$f$ 始终是自由多项式变量，没有把它或 $N_f$ 当单位。源把两条原仿射行同时代回为零；第二条由 (2.1)，第一条使用同一纤维的 $\Delta=F=0$。未倒置 $\Delta,T_0,P_f$ 或未付范数。

为完整返回原几何，令 $\rho^2=d$、$p=1+\rho,q=1-\rho$、$b=c=\ell/2,a=1-\ell$，置
$$
W_1=T_0/2+2uf,\quad
W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt,
$$
$$
X=\frac{cq(qW_1-W_2)}{bcQ(q-p)},\qquad
Y=\frac{bp(W_2-pW_1)}{bcQ(q-p)},
$$
$$
r=X-ap-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
\tag{2.2}
$$
原 Gram 行重建为
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
\tag{2.3}
$$
整个重建没有引入缩放 Gram。双点乘法仍为
$$
(z_0,z_1,z_B,z_C)(v_0,v_1,v_B,v_C)
=(z_0v_0,z_0v_1+z_1v_0,z_Bv_B,z_Cv_C),
$$
原迹为 $\tau(z)=az_0+z_1+bz_B+cz_C$。

源实际逐式验证原 $E_0,N_0,P_1,N_4(V)$ 及三个 moment 身份，并重建全部原八行。$B,C$ 两个单点的 N 目标均为 $2\lambda P_{02}(1+\xi)^2$，P 目标均为 $P_{02}(1+\xi)^3$。这保留原目标，没有使用更弱的替代方程。

## 3. 八原式的实际次数与完整 Bézout 单位

在形式二次代数 $\rho^2=d$ 中，两个单点原行互为 $\rho\mapsto-\rho$ 的共轭。由于两条原行都要求为零且原 $\rho\ne0$，它们同时为零等价于相应偶、奇系数为零。这一步依赖**两个实际单点原条件**，不是把任意扩张系数擅自分别视为零。

全八个必要行及自由 $f$ 次数为

| 原行 | $f$ 次数 |
|---|---:|
| $E_1,E_{B,e},E_{B,o},N_1$ | 各 2 |
| $N_{B,e},N_{B,o},P_{B,e},P_{B,o}$ | 各 3 |

在完整 $K[f]$ 中，源从 $E_1$ 开始，加入 $E_{B,e}$ 后即返回
$$
\boxed{A_f(\lambda,f)E_1+B_f(\lambda,f)E_{B,e}=1.}
\tag{3.1}
$$
所有多项式除法、系数逆及最终原行标签都实际乘回；没有只报告 gcd 次数而跳过原系数身份。证书的序列化内容包含常数多项式、原 $Q$、相容式标签、两个原 mean 多项式及其完整 $f$ 标签，总计 33013 字节，SHA-256
$$
\texttt{9ef6a10031e14076c9a97b7a410c6e87945dddf9044746f0f79117424ab0af57}.
$$
源可完整重建该对象；按仓库规则只保存源与小回执，不另存可重复的大展开。

因为 (3.1) 成立于整个 $K[f]$，它在 $\phi_{20}$ 的每个复根和任何 $f$ 处均成立。故不存在同时满足原 mean 的点；这排除整个 $\Delta=0$ 等权碰撞支。无需再增加其他原行来作排空门，也无需从数值样本或单个模根提升结论。

与此前完整 $\Delta\ne0$ 排除及 $h=k=1$ 排除相合，得到开头的整个等权碰撞结论。一般参数式
$$
b-c=\frac{u-\ell}{\rho}
$$
及原 $\rho\ne0$ 给新的合法单位 $u-\ell$，仅在已限定的原碰撞图内使用。

## 4. 实际执行与复算身份

- [完整原返回源](../notes/2026-11-27-unit211-equal-singleton-equal-weight-Delta-zero-full-original-QQ-return-8542.py)，git blob 3f511c4e5de8f1a68787f8d5b570ef7bd728d695。
- SHA-256：c2d6165ae5cee89666674c048e2474014b0f99539b24660fe61bfc12156a5388。
- [Actions run 46008309579](https://github.com/Rogerhu12/math-research-public/actions/runs/46008309579)，job 140537018591；inner exit 0，源 0.205941058 秒、驱动 0.288779024 秒，子进程峰值 41412 KiB。
- 完整常数系数逆 46 次、多项式除法 9 次，全部真实返回；常数非单位分裂数为 0。
- stdout 9734 字节，SHA-256 96387438d812257e6f6e294c196777d0060587a1e8254513868ab71c8f04985a。
- Python 3.12.14、python-flint 0.9.0、单线程，180 秒/4 GiB上限。
- 2026-11-27 13:34:54 UTC 实际 pull 到 35727a5a70895f451f9c521f7794560143115704，两 README 无变。
- [小执行回执](../notes/2026-11-27-unit211-equal-singleton-equal-weight-entire-Delta-zero-return-receipt-8542.json)保完整实际输出与准确执行状态。

这里只关闭原碰撞图中的等权支。原不等权 $h=k$ 的 $\Delta=0/\ne0$、其他原权边界、物理第五列、一般 unit211 与普通 ISP 均未由此关闭。
