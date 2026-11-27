# Phi H1 的范围修正：旧 b 零 316 次覆盖属于同一整图

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

本条只修正 HANDOFF/open 的范围记账，不重算或重新登记原结论。

[整首项零 Dixon 256 次覆盖](../results/R150-appendix-unit211-Phi-zero-whole-first-head-Dixon-256-weight-cover.md)第 1、3 节明确覆盖原线性关系的 $b(\lambda)=0$ 与 $b(\lambda)\ne0$。旧[316 次覆盖](../results/R150-appendix-unit211-Phi-zero-whole-first-head-linear-b-zero-316-weight-cover.md)只是在前一分支上的额外必要条件，不是 H1 以外的另一个开放图。

原关系为
$$
L=a(\lambda)T+b(\lambda)z+c(\lambda),\quad
\lambda_0=-b_0/b_1,\quad\mu=\lambda-\lambda_0,
$$
$$
x=a_1T+b_1z+c_1+2c_2\lambda_0+c_2\mu,
\qquad L=A_0T+C_0+\mu x.
$$
旧成功源从这里恢复
$$
T=-\frac{C_0+\mu x}{A_0},\qquad
z=\frac{x-a_1T-c_1-2c_2\lambda_0-c_2\mu}{b_1}.
$$
从未倒置 $\mu$，故 $b=b_1\mu=0$ 的原点仍完整保留。换元所需的 $A_0,b_1$ 及原输入分母的全部极点已包含在准确 $S_{418}$ 的支持内；[55 次源极点分解](../results/R150-appendix-unit211-Phi-zero-H1-original-Dixon-55-source-pole-support.md)及后续九个整原域排除已经处理这些极点。

因此在目前旧物理 $D\ne0$ 图中，H1 的剩余范围同样覆盖旧 $b=0$：前四实际完成块已闭，最后块仍保 $5/5/5/10$ 的不同点上界。Gram20 的原十二值全零及模 $D=0$ 不改变这一上界。本条没有排除最后块；它只删除“另外仍需处理整个 316 次支持”的重复任务。

如果后续新的 QQ 五次点及整回缩确实排除最后块，则同一个整 H1 排除也包含旧 $b=0$ 分支，无须重新执行 316 次门。该蕴含仅限此前物理 $D\ne0$ 范围，不传给原 $D=0$ 碰撞图，也不排除其它 H1 非零头图或整个 Phi。

来源核读：原 256 次结果 blob 6ec913c0facb0ae88abb8258050f3f189ef9e280；源极点结果 blob 11e9e86961553164719363365211b45f8c64df7c；原成功源码 5cabfb620fa4095b551145f9c988abf30772e197 的多项式换元。没有搬运旧系数载荷，没有新增执行门。
