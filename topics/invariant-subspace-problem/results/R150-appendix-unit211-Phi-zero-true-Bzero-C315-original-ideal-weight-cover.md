# R150 补充：正确整 B 的原理想 C315 二十二次幂返回与有限权支持

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：GPT-6 Astra Pro（AI-assisted）。

## 1. 新结论与范围

保持[正确整 B 的完整 I6 十二行两列](R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)的全部原范围与单位。即
$$
u=\frac{(x+1)^2}{3x},\quad Q=\frac{4(x^2-x+1)}3,
$$
$$
A=\mathbb Q[x,1/(xF(x+1)H\beta JC_2)],\qquad R=A[\lambda],
$$
其中 $F=x^2-x+1,\ H=2x-1,\ \beta=5x-1,\ J=7x^2-4x+1,\ C_2=23x^2-11x+2$。物理图仍是正确 Phi、$Q(1-Q)P_fP_{02}bcD\ne0$。

本次从相同十二个原行得到一个明确可再生的非零
$$
C(x)\in\mathbb Q[x],\qquad\deg C=315,
$$
并严格返回
$$
\boxed{C(x)^{22}\in I_6.}
\tag{1}
$$
所以当前整 B 的原权参数必须满足 $C(x)=0$。由于有理参数图双向且 $x=Q/[4(u-1)]$，不同 $(u,Q)$ 权点至多 315 个。

这里保留 C 的全部零纤维。没有以 QQ(x) 上的单位返回直接声称整 B 排空，也没有给这些权点上的完整 $\lambda,f,t$ 原纤维点数上界。

## 2. 固定原模与新计算

前篇给出首一
$$
q(\omega)=\omega^2+q_1(\lambda)\omega+q_0(\lambda)
$$
及六条原线性余式和各自真实 $\omega$ 倍。十二行作为 R 子模 $\mathcal M\subset R^2$，精确表示原 $I_6$ 在 $R[\omega]/(q)$ 中的理想像。最终商不假自由。

本次只构造这些必要定义；在旧三个 $\lambda$ 标量 cofactor 的代码之前截断，没有重算它们。到 $K=\mathbb Q(x)$ 后，用同十二行形成 $K[\lambda]^2$ 中的弱 Popov 基。

每个种子先用实际 pure-x 分母整化，再除全两列的共同 pure-x 内容。两个相同 leading position 的原来源行之间，每一步是
$$
g(x)r_{\rm new}
=b(x)r_{\rm old}-a(x)\lambda^j r_{\rm pivot}.
\tag{2}
$$
源码返回 (2) 的完整两列，并保父节点。$g,a,b$ 只依赖 x，且每次 leading degree/position 严格下降。选择过程中不把这些新权多项式当物理单位；它们只在函数域内用于求原来源组合。

实际共建立 97 个节点、95 次 leading 消去。两个最终 leading position 不同，行次数为
$$
(0,0).
\tag{3}
$$
因此泛型余商维数为零。这一步仍只是寻找证书；全原权域结论由下一节的实际分母清回给出。

## 3. 常数目标及精确 DAG 清分母

原计划按同一首一 q 测试
$$
(\lambda tD_{\rm val})^n,\qquad
D_{\rm val}=\ell(2\lambda^2-2\lambda+1)-T^2.
$$
同点原两矩给 $D_{\rm val}=bc(h-k)^2$，其非零范围仅是当前物理 D 图。本次没有倒 D 或其范数。

实际在第一个目标 $n=0$ 已经得到
$$
e_0=(1,0)=\sum_j a_j(\lambda)r_j
\quad\text{于 }K[\lambda]^2.
\tag{4}
$$
(4) 的两列全部乘回；所以最终结论不需要任何正幂目标，也没有新增关于 $\lambda,t,D$ 的单位前提。

只取 (4) 实际可达的 24 个 DAG 节点。令 $\delta(x)$ 为这些边、种子尺度、终端组合与已付坐标恢复系数的实际约分后分母的 LCM。它由冻结源唯一重建，并且
$$
\deg\delta=344,\qquad
\delta=\delta_{\rm paid}C,\qquad \deg C=315.
\tag{5}
$$
这里 $\delta_{\rm paid}$ 只含 A 中已有的单位；(5) 完整多项式乘回。C 的精确来源是这一 LCM 逐次剥已付支持，不是模因子重建、未执行因式猜测或所选数值点。

每个种子仅需一次 $\delta$，每个 (2) 的边再增加至多一次；终端组合再增加一次。实际可达深度给指数 22，故
$$
\delta^{22}e_0\in\mathcal M.
\tag{6}
$$
所有分母都已逐边纳入 (5)，所以 (6) 在原已付系数环 A 的多项式模中成立，保留中间主元的零集。再由首一 q 与原双向坐标身份，把 (6) 返回同一原 I6。除去 A 内单位 $\delta_{\rm paid}^{22}$ 即得 (1)。

这项原组合由有限 DAG 逐边完整两列恒等式构成；无须为登记它另展开可能庞大的十二个终端原乘子。

## 4. 完整边界

- C 的 315 次是精确 QQ 多项式次数，不是模估计。
- 本次没有计算 C 的平方自由次数或不可约因子，不把 315 当不同根的精确数。
- $C^{22}\in I_6$ 给全部原权点的必要支持；不把 C 的任何零纤维删除。
- 每个固定权的原表示仍是首一 q 后的两列模，但未据此自动得到 $\lambda$ 的首一多项式，因此没有完整原点数界。
- 当前原两列来源已纠正 germ 乘法；不恢复被撤旧 $R_{\rm bad}$ 链的任何结果。

## 5. 实际证据

[冻结源](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-original-unit-two-column-module-8542.py)的 SHA256 为
`d92d18281bc185205073c600e588f99cd7f8d53ac2d2aaf0833fc738a7683e63`，10017 B。

唯一实际运行为 46116342060 / job 140890933158，正常退出 0；用时 1.547025334 秒，峰值 43412 KiB，限额 120 秒、1 GiB。源提交 `7bf3f16bc523bca10b395570a1bb632916b8966c`；2026-11-28 06:23:14.630325 UTC 实际 pull 到 `ba9c766f01c2b90166a7f5c0b86c058e490f4a89`，两 README blob 无变化。

实际共返回 24 个种子坐标、170 个非零边坐标、20 个零行坐标、2 个终端坐标，304 次完整多项式精除；原 q 的两个新乘法短除也完整返回。$\delta$ 有 339 项，C 有 316 项，仅保定义及哈希：

- $\delta$：`e4e0d4f52477c7b7cb5eb8f5a8ebfc0626bd93901dda3dae9a10826bf86e1b6c`；
- C：`f9d865032e9c7e22851ca083b939729970e6d57a3c285d4edc010eeb29636b4f`。

stdout 为 4931 B，SHA256 `9b22881f84ab3fb438033f355b15f8e61ed8e083cfd64141429e66fe3682156d`。[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-original-unit-two-column-module-8542-execution.json)保留真实完整范围；不存入可重算的 C 系数或矩阵缓存。
