# Bertrand 与 2026 年 11 月 rank-two Heegner 新文的假设核对

日期：2026-11-14。**状态：下列文献适用范围已核；未获得无穷素数结论。** 这是一份窄范围排重记录，不新增结果编号。

## 1. 单点高度非零没有支付 rank-two 行列式

Agboola–Howard 论文的 Rubin 附录 A，Theorem A.1，陈述 Bertrand 对 CM 曲线非挠代数点的指定 $\mathfrak p$-adic 高度非零。附录开头明确区分此断言与整个高度配对非退化。Burungale–Disegni 的 AIF 2020 论文第 2078 页也保留这个区别；其一般非零结果沿反圆分字符变化，并非固定秩二曲线随 $p$ 变化的行列式结论。

原始可读来源：

- [Agboola–Howard，含 Rubin 附录 A，PDF](https://web.math.ucsb.edu/~agboola/papers/cm1-final.pdf)，附录第 32–33 页，Theorem A.1。
- [Burungale–Disegni，AIF 70 (2020)，PDF](https://www.numdam.org/item/10.5802/aif.3381.pdf)，第 2078 页及 §1.4。

下面的纯线性代数说明缺口不能由量词省略填上。取 $\tau\in\mathbf Q_p\setminus\mathbf Q$，
$$
H=\begin{pmatrix}1&\tau\\\tau&\tau^2\end{pmatrix}.
$$
对每个非零 $(a,b)\in\mathbf Q^2$，
$$
(a,b)H(a,b)^t=(a+\tau b)^2\ne0,
$$
但 $\det H=0$，其 $\mathbf Q_p$ 核由 $(-\tau,1)$ 张成。
因此“每个非挠有理组合的高度非零”本身仍不能排除一条不定义于 $\mathbf Q$ 的退化线。这个例子只分清逻辑范围，不声称它是任何实际椭圆高度矩阵。

## 2. 最新 derived-Heegner 恒等式已经假设目标非零

核读 Miquel Calonge Fabregat，
[arXiv:2611.09192v1，官方全文](https://arxiv.org/html/2611.09192v1)，提交日期 2026-11-06。

其 §3.1 将 $c_2(p)\ne0$ 与该素数的完整 $\Sha[p^\infty]$ 有限及 cyclotomic regulator 非零联立；Theorem 3.5 的二次 Katz 形式先假设 $\Sha(E/K)[p^\infty]$ 有限，读取 $q_p$ 的公式另要求 $\det H\ne0$。

更直接地，Hypotheses 5.1(H5) 就是 $c_2(p)\ne0$。所以 Theorem 5.9 的 derived-Heegner 精确平方身份及 Theorem 6.2 的平方类结论不能反过来充当本课题的原非零输入。§9.1 仍把 $q_p=q_\infty$ 留为猜想，并说明现有身份对 $q_p$ 是齐次的。全文只处理 $K=\mathbf Q(i)$；不能直接移植到当前 $j=0$ 三来源。

这次核对只覆盖这些显示假设和结论，没有独立复核论文全部常数或一般化其结论。未从数值验证、摘要或条件性恒等式推出本课题完成。

## 3. 继续接口

当前实际缺项仍是原完整中央行的跨 $p$ 非零，或满足 R418 全量词的真实饱和 jet 改善。原一般首核、十九角来源、两条十三行 carry 和完整 forcing 的比较继续进行；上述两类文献不替代这个缺项。
