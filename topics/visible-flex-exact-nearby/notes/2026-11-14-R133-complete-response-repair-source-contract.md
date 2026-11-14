# 原完整响应在连续修补背景下的逐格源差

本篇固定原物理 eta0、原 nu 和原完整 ac1 候选。原连续修补为
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`；
其准确完整 native 为
`6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc`。
本篇给新的完整源差消费者。数值预算只在本公开仓库 Actions 实际完成
全部 7721 格后登记；下面的代数不把任何尚未付的逆或响应误差当作已证。

## 1. 保留主部和独立 mean 的算子差

设 Q=(u,v)，m=〈v〉，e=(e_u,e_v) 是该原片上的准确修补，e0=〈e_v〉。
参数、目标和 reference s 不变。完整 moving 向量场为

$$
 F(Q)=dQ_\phi+\gamma mJQ_\phi+\beta(-u,v)-\beta S Q,\quad
 S=u^2+Kv^2,\quad d=-\beta I S,\quad
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
 \tag{E.1}
$$

I 是零 mean 原函数，在四重对称圈上 A0 和 L2 范数均为 1/4。
对任意完整方向 h，准确线性化为

$$
 DF(Q)h=d h_\phi+\gamma mJh_\phi
 -2\beta Q_\phi I(uh_1+Kvh_2)
 +\gamma\langle h_2\rangle JQ_\phi
 +\beta(-h_1,h_2)-\beta S h
 -2\beta Q(uh_1+Kvh_2).
 \tag{E.2}
$$

第二分量的 mean 与秩一列都保留。令 Q0、Q1 分别界 Q、Q_phi 的完整
pair A0 范数；E0、E1 分别界 e、e_phi 的同一范数。所有 pair 范数在本节
取两分量范数之和。记 K*=max(1,|K|) 和

$$
 \Delta S=K_*(2Q_0E_0+E_0^2).
$$

逐项相减 (E.2)，再用真实 I 范数，得到

$$
 \|[DF(Q+e)-DF(Q)]h\|_{L^2,\mathrm{pair}}
 \le M_1\|h_\phi\|_{L^2,\mathrm{pair}}
       +M_0\|h\|_{L^2,\mathrm{pair}},
 \tag{E.3}
$$
$$
\begin{aligned}
 M_1&=|\beta|\Delta S/4+|\gamma|K_*|e_0|,\\
 M_0&=3|\beta|\Delta S+
 \frac{|\beta|K_*}{2}\{E_0Q_1+(Q_0+E_0)E_1\}
 +|\gamma|K_*E_1 .
\end{aligned}\tag{E.4}
$$

这里 3|beta|DeltaS 来自 -beta S h 和完整乘法秩一项之差。两项 I 源
分别给 E0 Q1/4 与 (Q0+E0)E1/4，外面乘 2|beta|K*。mean 秩一列给
最后的 |gamma|K*E1，而真实主部 mean 变化留在 M1 中。
这是 H1→L2 门；不能由于 e 很小而把它说成未知无限 h 的有界 L2 扰动。

对已知完整 q_star=q_raw+e_z e2，则

$$
 \|q_\star\|_{A^0,\mathrm{pair}}
 \le\|q_{\rm raw}\|_{A^0,\mathrm{pair}}+|e_z|,\qquad
 (q_\star)_\phi=(q_{\rm raw})_\phi .
 \tag{E.5}
$$

e_z 是原完整标量 Green 解与原 trial mean 的差，不是删除 mean。
因此 (E.3) 是可直接支付的已知源；没有对一个未知解假定有限支持。

## 2. 真参数列之差，及紧支撑外的准确零

原物理参数列的完整公式就是原
`fourfold_codazzi_correlated_head_residual_rows.py:parameter_source`。
在紧支撑 [1/20,9/50] 内，令

$$
 w=4096[t(1-t)]^6,\quad
 K_\nu=-Kw+T w_r,\quad T=\frac{\beta}{2\gamma^2a^2},\quad
 J_\nu=\begin{pmatrix}0&Kw/2+K_\nu\\-w/2&0\end{pmatrix}.
$$

则在固定物理 Q 下

$$
 F_\nu(Q)
 =-\beta K_\nu\{I(v^2)Q_\phi+v^2Q\}
       +\gamma mJ_\nu Q_\phi .
 \tag{E.6}
$$

没有再加一个 reference s_nu 方向。紧支撑外该列准确为零。
区间消费者使用完整原 scalar whole jets，保留 gamma、a 的正分母；
准确的全片界 |w|≤1、|w_r|≤24/(9/50-1/20) 已足够，
不需要重新求目标 primitive 或抽样寻找极值。

令 B=2Q0E0+E0²、V=(Q0+E0)²，m_*≥|m|，
Cnu≥max(|Kw/2+Knu|,|w|/2)。直接相减 (E.6) 给

$$
 \|\Delta F_\nu\|_{A^0,\mathrm{pair}}
 \le |\beta K_\nu|
    \{BQ_1/4+VE_1/4+BQ_0+VE_0\}
 +|\gamma|C_\nu\{|e_0|Q_1+(m_*+|e_0|)E_1\}.
 \tag{E.7}
$$

程序分别保存 (E.3) 的已知响应费与 (E.7) 的参数列费，不依靠它们之间
未经证明的符号抵消。原准确 control 接缝必须属于公共划分，不能跨缝
使用“紧支撑外零”的判断。

## 3. 原 cubic 的完整闭片范数

全部背景 65 系数与物理响应 193 系数都来自原已验证 SHA 的完整 cubic。
对原节点偏移 x=r-knot，将闭片 [left,right] 归一化为 t∈[0,1]。
若 p=a0+a1 t+a2 t²+a3 t³，其四个准确 Bernstein 系数是

$$
 a_0,\quad a_0+a_1/3,\quad
 a_0+2a_1/3+a_2/3,\quad a_0+a_1+a_2+a_3.
 \tag{E.8}
$$

它们的有向凸包包住完整闭片的每个原实振幅。全部振幅的绝对上界相加
给完整 A0；乘真实频率 4j 再相加给普通角导 A0。mean 权重为1，
角导 mean 权重为0。背景另加原真实 s 的 whole 区间。
物理响应不乘背景 alpha；只有原归一化背景乘其准确 alpha。

原完整 repair native 的准确最大 A0、A1 和 mean 修补界分别供
E0、E1、|e0| 使用；A1 支配普通角导范数。它们消费同一次全6143接口的
准确结果，不再生成或改写任何修补数组。

## 4. 新残差和全部接口

令 D=partial_r-DF(Q)、Dbar=partial_r-DF(Q+e)。在每个真实片内

$$
 \bar Dq_\star-\bar F_\nu
 =(Dq_\star-F_\nu)
  -[DF(Q+e)-DF(Q)]q_\star
  -[\bar F_\nu-F_\nu].
 \tag{E.9}
$$

原 complete body/mean native
`a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870`
给第一项。新消费者给后两项，按原7721片分别保存，包含整帽 [9/10,25/8]。
原第一项的 mean 残差为零；新算子下的 mean 残差不因此设为零。

这些都是已知有限函数：背景及修补有32模，q_star 的非均值有96模，
其余是完整径向 scalar mean。故 (E.9) 的新差源最多160模。完整 A0
上界支配普通 pair L2；H1/3、H1 可分别乘
(1+640²)^(1/6)、sqrt(1+640²)。
这个160只作用于已知差源，绝不截断未知 PDE 方向。

每格源费的平方乘准确片长后累加，给全径向有向 L2 预算；新 residual
与原每格 L2_radial 作三角相加。全部6143个原 nonmean q_star 跳保持
原状，完成的 mean 连续；没有把它们隐藏进一个普通源。

## 5. 公开执行和范围

新 workflow 只下载公开原 body run 43583838026 的成功 prepared bundle
及8份完整 row artifacts，以及 run 43586413510 的完整 body/mean。
原 `CompleteMeanWorker` 的两个输入审计函数核原字节、canonical alias、
40-part 完整覆盖和真实过程；不调用其 mean 流或任何残差 producer。
新的消费者在公开 Actions 算 (E.3)--(E.9)，保存真实退出码、每格预算
及全部失败前缀，并每10分钟实际 pull/检查 README。

该结果支付 ac1→连续修补背景的已知 q_star 源变化。完整高输入反馈、
真实 regular/cut 边界源、外帽 Green 传递、真正 q_nu 响应误差和
非线性背景移动仍须在自己的合同中证明。当前完整有限 Green 的冻结源、
manifest 和正在运行的5970矩阵格均不修改。
