# R133：同一临时运行内并行未来协方差、过去协方差与未归一右端图

2026-11-15。**已证明的代数重排；新的数值门仍由公开 Actions 运行。**
本合同不改变原 5970 个同 F 参考、原 6391 正 Green、全部真实接口、
固定物理 $\eta_0$、独立 even mean 和两端行。根 README 第 15 条的新存储规则只允许本次大中间量存在于同一 runner 的临时目录；最终仅登记脚本、参数、run、输出 SHA 和真实结论摘要。

## 1. 原准确三角端口与三条独立递推

沿腰到帽的正向，把原同 $Q,R$ 换基准确并入每格右端，
$$
 \binom{p_+}{q_+}
  =\begin{pmatrix}A_i&B_i\\0&D_i\end{pmatrix}
     \left\{\binom{p_-}{q_-}+\binom{\eta_p}{\eta_q}\right\}.
 \tag{E.1}
$$
$A_i$ 为 $96\times96$，$D_i$ 为 $97\times97$；所有矩阵使用原物理
weighted 状态，均值为 $q$ 的真实一维分量。两种 body 源各保完整
$193\times193$ signed Gram $H_i$，包括其交叉块。

写
$$
 p=Vq+w,\qquad
 H_{w,i}=[I,-V_i]H_i[I,-V_i]^*.
$$
从同一原公式直接消元，
$$
 \begin{split}
 Q_i&=D_i^{-1}Q_{i+1}D_i^{-*}+(H_i)_{qq},\\
 V_{i+1}^{\rm ex}&=(A_iV_i+B_i)D_i^{-1},\\
 W_{i+1}&=A_i(W_i+H_{w,i})A_i^*.
 \end{split}\tag{E.2}
$$
这里第一行从 cut 向腰传播，$Q_{\rm cut}=0$；后两行从腰向 cut
传播，$W_{\rm waist}=0$。$V_i$ 仍为准确的两份 binary64 dyadic 之和，
逐格与 $V_{i+1}^{\rm ex}$ 的差全留为真实 weighted 状态跳。

因此未来 $Q$ 和过去 $(V,W)$ 的递推彼此独立。原程序在 $V_0$ 之后
立即读取 $Q_0$，只是为了计算真实腰端缺陷，并非选择 $V_0$ 所必需：
$V_0$ 仍由同一完整腰帧的 $-U_Q^{-1}U_N$ 选点。腰端缺陷可以在
两条流完成后原样计算。不能把它删成零。

## 2. 第三条流：准确未归一右端传播

另令
$$
 E_{\rm cut}^{0}=I_{97},\qquad E_i^0=D_i^{-1}E_{i+1}^0.
 \tag{E.3}
$$
这条流也不依赖 $V,W,Q$。它只代表右端未来坐标 $q_{\rm cut}$ 的
准确传播，不代表原 source Green 的 $q_{\rm cut}=0$。

待 $V$ 全部产生后，在真实 cut 用原最后一格的
$$
 V_{\rm cut}^{\rm ex}=(A_{\rm last}V_{\rm last}+B_{\rm last})
                      D_{\rm last}^{-1}
$$
和原真实 $97$ 行的 nominal 矩阵构造 $P_{\rm cut}$。
按照原右 Poisson 合同，选出准确 dyadic 和 $C$ 近似
$P_{\rm cut}^{-1}$。完整 nominal 缺陷 $P_{\rm cut}C-I$ 及原
仅作用于 even97 的真边界误差都必须付；mean 行不删。

对于这个同一准确 $C$，
$$
 E_i=E_i^0C. \tag{E.4}
$$
若临时记录 $E_i^0$ 的中点 $E_i^{\rm app}$ 与 operator 半径 $e_i$，
则 $E_i^{\rm app}C$ 的误差为 $e_i\|C\|$。这只是准确乘积的包络，
不产生新的物理状态跳。等价地，先对未归一输出得到真正半定矩阵
$H_i^0$，末端再作 $C^*H_i^0C$。两种表达只选其一完整消费。

## 3. 每格独立消费，保同源的所有相关性

在同一准确 $V_i$ 上，记 $E_p=(I,0)^T$、$L_i=(V_i,I)^T$。
原 source Green 的整格协方差上界是
$$
 \Gamma_i\preceq E_p(W_i+H_{w,i})E_p^*+L_iQ_iL_i^*. \tag{E.5}
$$
这正是原证明的过去、当前两半、未来支集比较；不得宣称当前两份
完整 $H_i$ 对应的同一源独立。与原完整输出 Gram $J_i$ 收缩后，
signed off-diagonal 项直到完整 trace 才取上端。

未归一右 Poisson 每格各完整输出、ordinary body 缺陷和真实 $V$
跳的 $97$ Gram，只使用该格原 $J_i$、同一 $V_i$ 和
$E_i^0,E_{i+1}^0$。因此所有本地项在三条流到达对应索引后可以并行计算。
真实径向积分已在原 $J_i$ 内，不得再乘一次格长。
即使输出只要求固定完整负区，body 缺陷仍积全 $[0,9/10]$。

不同格的普通积分平方可以相加；不同跳作用于同一输入，必须保原
正权 Cauchy。例如选定任意严格正 dyadic $\alpha_i$ 后，
$$
 \left\|\sum_iT_i x\right\|^2
 \le\left(\sum_i\alpha_i\right)
       x^*\left(\sum_i\alpha_i^{-1}T_i^*T_i\right)x.
 \tag{E.6}
$$
每个 worker 只累加自己的完整矩阵和正权和，最终再将这些和相加。
这不引入额外正交假设。$C$ 的统一后置也保持 (E.6)。

## 4. 临时端口缓存只扩大区间包络

原 endpoint $Q,R$、同 F 的 $A_i,B_i,D_i$、输入与输出 Grams、
原 target 和连续 validator 完全不重算。新发生的是原准确换基逆及
(E.2)–(E.6) 的区间算术。

若为避免三条流重复求同一准确换基逆，把一个已算 Arb 矩阵 $T$
存为三份 dyadic 矩阵之和 $T_d$ 与 $\varepsilon\ge\|T-T_d\|$，
再按每 entry 的闭球 $[T_{d,kl}-\varepsilon,T_{d,kl}+\varepsilon]$
恢复，则每个真 entry 都仍包含。这只是 $T$ 的较宽计算包络，不能
将 $T_d$ 当作新的无误差端口。所有准确逆门、$Q/R$ 同一门以及
$V$ 选点跳都使用恢复后的完整球；不能因缓存删去误差。

新算术精度作为新脚本参数显式记录。任何降低工作精度都只能扩大
实际有向误差，并须仍通过原 $10^{-30}$ 准确逆和坐标门。旧 prefix
的原精度、原字节、原矩阵值与原 source SHA 始终保留，不重标成新结果。

## 5. 实际旧 prefix 与最终范围

只接受原 run 43672023585/1 的原完整 artifact
14146873569：原 ZIP 为 286134725 bytes，
SHA256 de4e8dbdde0e34f6cfbd00b643ed70544ddc55d5852e1654a400ec8d3eaf3773。
新的准备步骤必须实际读取原 process，核其唯一规则拒绝、原科学
身份、全部 chunk 连续索引及每个原 array receipt，之后才复用
其中完整的 backward 行。不能只据仓库早先的 1658 行快照猜最终数量。

新 runner 不上传任何新的可重算数学输出，所有缓存只在同一临时
工作目录使用。共同输入 SHA、各阶段输出 SHA、真实新行数、原行
复用数、所有门、末次真实 pull 和两 README 差异写入小运行记录。
最后的 Green、完整97右 Poisson 和原 same97 cap 合成在同一 runner
完成后，才登记真实有限193结论。原 cap signed97 矩阵必须一直保留
到与新 $H_Y$ 的同坐标 trace，不能先用 trace 排名代替方向合成。

完整负区高频 BVP 逆、全 low/high Schur、非线性解和参数真响应仍是
各自独立的未付义务。本合同不给它们任何新结论。
