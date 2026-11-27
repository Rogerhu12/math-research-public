# Phi=0 第一二次头开图：原 D 六次必要式不可约与整首项零权曲线

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 精确结论

沿用
[R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md](R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)
的第一原二次头非零图。其由实际原 D 目标返回得到的必要多项式记为
$$
P=P(u,Q,\lambda).
$$
它具有参数分次 $(39,20,6)$、3101 项。新输入只读取此前保存的精确 P，不重算原均值、交换歧义或 D-cofactor。

本次完整 QQ 因式分解证明：P 在 $\mathbb Q[u,Q,\lambda]$ 上不可约。其真正 $\lambda^6$ 系数满足
$$
[\lambda^6]P
=c\,u(u-1)^2Q(1-Q)
  [Q-2(u-1)(u-2)]^6\,H(u,Q),
\qquad c\in\mathbb Q^\times,
$$
其中 H 是 QQ 不可约多项式，分次为 $(19,11)$，恰有 137 项。各次完整多项式除法以及最终因式乘积均实际乘回。

这些结论没有把 H 当作单位。原第一二次头零曲线和整个 H=0 权曲线均保留。

## 2. 原图和已经支付的因子

本图仍由
$$
\ell=1-\frac{2(u-1)(u-2)}{Q}
$$
定义。原物理图已经支付
$$
u(u-1)Q(1-Q)\ell\ne0.
$$
所以
$$
Q-2(u-1)(u-2)=Q\ell
$$
是该图上的单位。

源先逐次从实际 $[\lambda^6]P$ 剥除原单位因子。实际出现的次数为：

| 原单位因子 | 实际次数 |
|---|---:|
| u | 1 |
| u−1 | 2 |
| Q | 1 |
| 1−Q | 1 |
| Qell | 6 |

每步使用真实 QQ gcd 和精确商，核对商乘因子恰等于上一步多项式。剩余多项式的完整 QQ 因式分解只有一个非恒定因子，重数为 1，即 H。原首项、剩余首项、H 的完整系数分别保存于小 JSON，不依赖日志摘要恢复多项式。

在第一二次头非零且 $H\ne0$ 的图，P 对 $\lambda$ 确为六次，故每个固定权点至多有六个不同 $\lambda$ 候选。这个陈述保留重根和实际原方程的进一步限制；它不把候选当成原解。

在 $H=0$ 上，P 的真正次数可能下降，不能继续除以该首项。该整权曲线仍是下一原返回必须覆盖的分支。P 不可约并不意味着它在复数域没有零点，也不提供新的物理单位。

## 3. 新输入的精确身份

P 的唯一输入文件是：

[2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json)

其文件 SHA-256 为：

7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b

源核对文件字节、解压后载荷及全部系数重建身份。原保存系数指纹使用 $(u,Q,\lambda,T,z)$ 五变量上下文；本次读取后给最后两位补零，再核对该原指纹，避免把上下文不同造成的指纹差异当成多项式变更。

新增 H 和原首项精确文件：

[2026-11-27-unit211-Phi-zero-first-head-D-lambda-six-leading-weight-curve-exact-input-8542.json](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-first-head-D-lambda-six-leading-weight-curve-exact-input-8542.json)

H 的规范整数系数版本以 $\lambda$ 指数全零保存在三变量上下文中，其系数指纹为：

7c05e2ecea3e017666d254936ff56f1a7fd61046c90e20315e8d92bc395a2e6d

解压后完整系数载荷 SHA-256：

52aa676c40827c798ccae390774a4ee40728208ee090390f2e8b92106e86e638

## 4. 实际执行

唯一新源：

[2026-11-27-unit211-Phi-zero-first-head-actual-D-core-factor-lambda-head-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-first-head-actual-D-core-factor-lambda-head-input-8542.py)

SHA-256：

6caada58cce3cd46f81b85c2ec21981635cf2ce70a1904ecc20b2c94768c7960

实际 run 46035511714，job 140629804758：

| 项目 | 实际返回 |
|---|---:|
| 总时间 | 0.175493409 秒 |
| 峰值子进程 RSS | 43116 KiB |
| 内层退出码 | 0 |
| 原首项分次／项数 | (34,19)／387 |
| 单位剥除后首项分次／项数 | (19,11)／137 |
| 整个 P 的非恒定 QQ 因子 | 1 个，重数 1 |
| 剩余首项的非恒定 QQ 因子 | 1 个，重数 1 |

本次结果只细化原必要式和保留分支。整个 $\Phi=0$ 面及普通 Hilbert ISP 均未在这里宣告完成。
