# R149 补充：同点共轭缺陷的单标量整盒与 parent 复用

会话：visible-exact-astra-198c63d-20261126。此为纯解析及纯算法补充；没有运行新科学，也没有把条件门登记成成功。主结果为 [R149 signed loop](R149-signed-Green-loop-and-symmetric-part-coercivity.md)。

## 1. 同一实际缺陷；只在准确乘积中消去 S

沿用 R141/R142 的完整比较模型与真正长度。一个 parent 的归一化常矩阵是 $H_p$，真正长度是 $h_p>0$，均分成 $n_p$ 个 cell 后
$$
 H_i=H_p/n_p,\qquad h_i=h_p/n_p,\qquad
 \Delta(r)=A_L^c(r)-H_i/h_i=A_L^c(r)-H_p/h_p .
 \tag{HC.1}
$$
这里的 $\Delta(r)$ 一般随 $r$ 变化。母格整包络
$\boldsymbol\Delta_p$ 只断言每个实际点的 $\Delta(r)$ 属于该矩阵球；
不得把它当成一个常值未知函数而使用常源积分公式。完整 mean 行、97/96 两端条件和193维度仍保留。

在 cell $i$ 的准确原节点框架写
$L_i,R_i,\ell_i,\rho_i$。对归一化位置 $\tau\in[0,1]$，主文的交叉矩阵是
$$
 \begin{split}
 A_i(r)&=\rho_i e^{-\tau H_i}\Delta(r)e^{\tau H_i}L_i,\\
 B_i(r)&=\ell_i e^{-\tau H_i}\Delta(r)e^{\tau H_i}R_i.
 \end{split}
 \tag{HC.2}
$$
这来自原物理因子 $IR\cdot OL$ 和 $IL\cdot OR$；相邻的 $S^{-1}S$ 已在准确代数中消去。式 (HC.2) 没有改变定义 $K=S\bar G\Delta S^{-1}$ 的 Hilbert 空间，也没有把 $S$ 改成别的权重。

任选此前已经固定的正 dyadic 内部平衡矩阵
$$
 T_p=\operatorname{diag}(I_{96},q_p I_{97}).
$$
令 $\widehat H=T_pH_iT_p^{-1}$，
$\widehat\Delta=T_p\Delta T_p^{-1}$，并把节点框架相应左右乘 $T_p,T_p^{-1}$。这样只改变式 (HC.2) 的内部表示。所有实际子格继续使用自己完整且独立的节点框架。

## 2. 对同一个标量的共轭级数

令 $D=\widehat H/2$，$t=2\tau-1$。对任意固定矩阵
$\delta\in\widehat{\boldsymbol\Delta}_p$，置
$$
 C(\delta)=e^{-D}\delta e^D,\qquad
 {\cal A}_D(X)=XD-DX.
$$
则准确恒等式为
$$
 e^{-\tau\widehat H}\delta e^{\tau\widehat H}
   =e^{-tD}C(\delta)e^{tD}
   =\sum_{k=0}^{\infty}t^k P_k(\delta),
 \qquad
 P_0=C,\quad P_k=\frac{P_{k-1}D-DP_{k-1}}k .
 \tag{HC.3}
$$
导数 $d(e^{-tD}Ce^{tD})/dt={\cal A}_D(e^{-tD}Ce^{tD})$ 给出该式和符号。两侧指数中的自变量是同一 $t$。

用向外矩阵球先包住 $C$，再按 (HC.3) 完整递推到次数 $d$。这对每个可能的 $\delta$ 都成立。即使实际 $\delta=\widehat\Delta(r)$ 随 $\tau$ 变化，逐点取值仍在同一包络里。因此下面的整盒结论没有冻结实际系数。

## 3. 完整尾界

设
$$
 q\ge 2\|D\|_\infty,\qquad c\ge\|C\|_\infty ,
$$
其中 $\|\cdot\|_\infty$ 是矩阵最大绝对行和。由次乘性，
$$
 \|{\cal A}_D(X)\|_\infty\le 2\|D\|_\infty\|X\|_\infty,\qquad
 \|P_k\|_\infty\le c\,q^k/k!.
$$
若 $q<d+2$，则对所有 $|t|\le1$：
$$
 \left\|\sum_{k=d+1}^{\infty}t^kP_k\right\|_\infty
 \le
 \frac{c\,q^{d+1}}{(d+1)!\,[1-q/(d+2)]}
 =:\varepsilon_{\rm tail}.
 \tag{HC.4}
$$
证明是第一项以后的比值均不大于 $q/(d+2)$；不存在抽样或未付的无限尾。这一无穷范数界同时给出每个矩阵条目的绝对误差界。

计算中 $q,c$ 取完整向上端点，分母取严格正的向下端点。分母非正时算法失败，不截断、不置零。所有幂、阶乘乘除和完整余项均用 directed ball 运算。默认 $d=24$，而实际 $q$ 仍由完整同模型矩阵计算和检查；旧粗浮点跨度不是认证尾界的输入。

对每个完整闭子盒 $J=[a,b]\subset[0,1]$，在同一标量球
$$
 t_J=[2a-1,2b-1]
$$
上用 Horner 算完整有限多项式，然后每个条目加
$[-\varepsilon_{\rm tail},\varepsilon_{\rm tail}]$，得到
$$
 Z_J\supset
 \left\{e^{-\tau\widehat H}\widehat\Delta(r)e^{\tau\widehat H}:
          \tau\in J,\ r\hbox{ 是对应实际点}\right\}.
 \tag{HC.5}
$$
有限多项式内部的 interval dependency 只可能放宽包络，不影响包含性。没有从旧 HS 上界反造有符号矩阵。

## 4. 可复用的对象与完整积分

同一 parent 中 $H_i$、内部 $T_p$、整母格缺陷球、归一化四子盒都相同，因此可以只保存这个 parent 的四个 $Z_J$。既有 R141 refined factor provider 已经按 parent 缓存短指数模板；本补充的额外收益是先共轭同一小缺陷、在同一标量多项式里保留左右相关，然后复用完整 $Z_J$。这里不声称原实现每个 refined cell 都重算指数模板。

每个实际子格再用自己的节点框架计算
$$
 \begin{split}
 {\bf A}_{i,J}&=(\rho_iT_p^{-1})Z_J(T_pL_i),\\
 {\bf B}_{i,J}&=(\ell_iT_p^{-1})Z_J(T_pR_i).
 \end{split}
 \tag{HC.6}
$$
将它们放入主文 (HL.13) 的完整子盒矩形和半三角公式。质量始终为实际完整球
$$
 \mu_{i,J}=h_i(b-a),
$$
并且先与有符号交叉迹相乘；不把质量换成上界。不同子盒按所有先后对累加，同盒保留真实半平方区域。接着调用原 R149 完整递推
$X_{i+1}=V_i^{-1}(X_i+a_i)U_i^{-1}$，最终取 $-2$ 倍完整有序循环和。

新纯模块
`scripts/fourfold_codazzi_low_centre_conjugated_defect_provider.py`
只产生主 R149 core 已约定的 cell packet。它不读旧结果、不产生逆、不修改 active 输入，也不执行科学入口。公开 owner 必须：

1. 只读取真实完成的 R142 整个 HS² 结果及执行对象，确认完整旧 false 门；
2. 核对同一原始比较链、真正长度、全部155 parents、全部1424 refined cells、全部细分数和193坐标；
3. 只为新的 signed trace 必要物化未公开的同定义载体，不把旧 Green 成功登记成新目标；
4. 完成整域 signed trace 后先保存并读回完整球，再与旧 HS² 上界组合；新 $\theta$ 也先保存读回；
5. 调用独立 resolvent binder，保留旧 $\epsilon$ 及 false 门，不用 $\theta$ 取代旧源、atoms 或 point receiver。

没有完整实际输出时，本补充只给定理和可执行定义。即使 $\theta<1$，后继四个源、全部193 traces、全径向 point 观测、完整 high feedback、原有限 $\rho$ 桥及真实几何家族仍要按各自原义完成。
