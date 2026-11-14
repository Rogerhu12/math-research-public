# R119 续篇：原标签对应的实际无限低尾两行与全部真高前缀

2026-11-14，visible-exact-astra-ac0d。

**状态：已证明。** 对第53束同一受控径向度量的齐次 Jacobi
允许列，本文把原中性层标签的一个泛函，提升为整个无限低尾
的完整物理两行。误差是相对于真实主振幅的统一小量，原有限
高前缀也由实际矩阵原样接入。没有改标签、权、度量或背景。

本文的线性算子是径向零解处的实际导数，参数
\(\Pi=(\Gamma,s,\Xi)\) 可在第53束原完整盒内变化；
不是非零非径向解处的导数。非零频率的两个 canonical 行均保留，
mean、独立高度及普通/weak 非齐次源不由本齐次结论消除。

## 1. 完整实际对象与同一个原标签

沿用[第53束全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
和[原中性层规范](R119-supplement-original-neutral-label-common-analytic-normalization.md)。
令 \(M=|m|\in4\mathbb N\)、\(M\ge M_*=2^{984}25^{1/8}\)；
原首次低层 \(n_0>8193\)，原中性标签层 \(b=b_m\ge n_0\)。
所有 \(j\ge n_0-1\) 使用同一个真实理想基
\[
 E=E_{m,\mathsf K,C},\quad \mathsf K=2^{128},\quad
 C=16\sqrt2,\quad
 \|E\|_\infty,\|E^{-1}\|_\infty<17/16 .
 \tag{L.1}
\]
这里 \(E\) 只用于坐标表示，实际传输始终是完整 \(B_{m,j}\)。
深段原规范与两个物理行满足
\[
 X_j=(-1)^j\zeta_j^{-1}e^{M\tau_j}V_j,\qquad
 \zeta_j=C_\zeta\delta_j^{131},\quad
 C_\zeta=\epsilon\delta_{8192}^{-485/4},\quad
 \delta_j=(2/25)2^{-j}.
 \tag{L.2}
\]
原物理齐次递推准确为 \(V_{j-1}=B_{m,j}V_j\)；
因此 \(Y_j=(-1)^jE^{-1}V_j\) 满足
\[
 Y_{j-1}=\bigl[\operatorname{diag}(\Lambda,\lambda)+R_j\bigr]Y_j,
 \quad R_j=-E^{-1}(B_{m,j}-B_m^\infty)E,\quad
 \lambda=(C\Lambda)^{-1}.
 \tag{L.3}
\]
没有以 \(B_m^\infty\) 替代 \(B_{m,j}\)。
原标签条件准确给
\[
 (Y_b)_1=N_M a_m^{\rm lab},\qquad
 N_M=\zeta_b e^{-M\tau_b}>0 .
 \tag{L.4}
\]
\(N_M\) 和 \(C_\zeta\) 不重设；前篇已证明其同一
\(\tau_\infty\) 与 \(M^{-33024},M^{-30960}\) 两侧有限幂界。

## 2. 相对于真实大根的可和全矩阵误差

第53束 (C.11) 在全部实际低窗给
\(\|B_{m,j}-B_m^\infty\|_\infty<2^{272}M^8\sqrt{\delta_j}\)。
由 \((17/16)^2<2\)、\(\Lambda>2^{124}M^4\)，置
\[
 e_j=R_j/\Lambda,\quad r=\lambda/\Lambda,\quad
 \varepsilon_j=2^{149}M^4\sqrt{\delta_j}.
 \tag{L.5}
\]
则对所有 \(j\ge n_0\)
\[
 \|e_j\|_\infty<\varepsilon_j,\quad
 0<r<2^{-268}<2^{-16},\quad
 \varepsilon_{n_0}\le2^{-11},\quad
 \varepsilon_{j+1}=2^{-1/2}\varepsilon_j .
 \tag{L.6}
\]
最后两式是原低窗
\(\delta_{n_0}\le2^{-320}M^{-8}\) 的直接结果。
尤其
\[
 \sum_{j=n_0}^\infty\varepsilon_j
 <4\varepsilon_{n_0}\le2^{-9}.
 \tag{L.7}
\]
整个 \(M^8\sqrt\delta\) 误差已相对于真实 \(\Lambda\)
支付；不能把未除大根的绝对误差用于本结论。

## 3. 真无限未来允许线：不删第二行

记 \(Y_j=u_j(1,s_j)^T\)、\(\gamma=2^{-9}\)。
完整 Möbius 递推为
\[
 s_{j-1}=f_j(s_j):=
 \frac{(e_j)_{21}+[r+(e_j)_{22}]s_j}
 {1+(e_j)_{11}+(e_j)_{12}s_j}.
 \tag{L.8}
\]
令 \(\varepsilon_*=2^{-11},r_*=2^{-16}\)。
在复圆盘 \(|s|\le\gamma\) 上，分母模至少
\(d=1-\varepsilon_*(1+\gamma)>0\)，且
\[
 \frac{\varepsilon_*+(r_*+\varepsilon_*)\gamma}{d}<\gamma,
 \qquad
 \sup|f'_j|
 \le\frac{(1+\varepsilon_*)(r_*+\varepsilon_*)+
                    \varepsilon_*^2}{d^2}<\frac14 .
 \tag{L.9}
\]
这是完整二行矩阵的行列式公式，并不假设误差矩阵对角。
在任意未来层 \(J\) 置 \(s_J=0\)，逆向迭代后令 \(J\to\infty\)。
两种未来截断在固定层的差至多 \(2\gamma4^{-(J-j)}\)，
故得到唯一处于该管中的无限未来线，且在完整复参数盒上局部
一致收敛。原固定段端点矩阵的全纯性因此也保留。

更准确地，由
\[
 \frac{1+2(r_*+\varepsilon_*)}{d}<2
 \tag{L.10}
\]
及逆向归纳，有限未来线满足
\(|s_{j-1}|\le2\varepsilon_j\)，极限也满足。于是
\[
 |s_j|\le2\varepsilon_{j+1}<\gamma,\qquad j\ge n_0-1.
 \tag{L.11}
\]
第二分量是实际存在且已估计的分量，并未置零。

## 4. 原标签固定后的完整相对主振幅

将 (L.8) 的真实 \(s_j\) 代第一行，得到
\[
 u_{j-1}=\Lambda(1+z_j)u_j,\quad
 z_j=(e_j)_{11}+(e_j)_{12}s_j,\quad
 |z_j|<2\varepsilon_j,\quad
 \sum_{j\ge n_0}|z_j|<2^{-8}.
 \tag{L.12}
\]
对这些因子的任意有限连续子积 \(P\)，展开完整乘积，
用初等对称和不大于总和的各幂，得
\[
 |P-1|<1/255,\qquad 255/256<|P|<256/255 .
 \tag{L.13}
\]
下界也直接来自
\(\prod(1-|z_j|)\ge1-\sum|z_j|>255/256\)。
因此所有所需逆积同样满足上述模上下界，且
\[
 |P^{-1}-1|<256/65025<1/254 .
 \tag{L.14}
\]
由准确的 (L.4)，对整个无限低尾
\[
 \boxed{\quad
 Y_j=N_M a_m^{\rm lab}\Lambda^{b-j}
                  (1+\theta_j)(1,s_j)^T,\qquad
 |\theta_j|<1/254,\quad j\ge n_0-1 .\quad}
 \tag{L.15}
\]
\(\theta_b=0\)；当 \(j<b\) 使用 \(j+1,\ldots,b\) 的正积，
当 \(j>b\) 使用 \(b+1,\ldots,j\) 的逆积。
这里没有把可能指数小的 \(N_M\Lambda^{b-j}\) 换成绝对误差。

由于 \(|s_j|<1\)，(L.1)、(L.13) 给两个完整物理行的统一界
\[
 \boxed{\quad
 \frac{255}{272}N_M|a_m^{\rm lab}|\Lambda^{b-j}
 <\|V_j\|_\infty
 <\frac{272}{255}N_M|a_m^{\rm lab}|\Lambda^{b-j}.
 \quad} \tag{L.16}
\]
对零标签，真实解为零；上式的严格不等式按非零标签陈述。
这比只控制原取值泛函多出了另一行和全部无限径向层。

## 5. 真实高前缀、原规范空间与允许列身份

恢复原 \(X_j\)，其准确参考标量为
\[
 W_j=D_M^{b-j}e^{M(\tau_j-\tau_b)},\qquad
 D_M=2^{-131}\Lambda .
 \tag{L.17}
\]
在 \(n_0-1\le j<b\)，它是原
\(a_k=D_Me^{-Mh_k}<1\)、\(k=j+1,\ldots,b\) 的乘积；
在 \(j>b\)，它是原 \(a_k\ge1\) 的乘积之逆。
所以 \(0<W_j\le1\)，且 \(W_j\to0\)：
\(\tau_j\) 收敛而 \(D_M>1\)。由 (L.15)
\[
 \sup_{j\ge n_0-1}\|X_j\|_\infty
 <\frac{272}{255}|a_m^{\rm lab}|.
 \tag{L.18}
\]

在每个更浅层 \(128\le j<n_0-1\)，使用实际有序乘积
\[
 V_j=B_{m,j+1}\cdots B_{m,n_0-1}V_{n_0-1}.
 \tag{L.19}
\]
这一有限但随频率增长的前缀没有换成理想矩阵，也没有跳过
4097或8193的真实段。原首次低层定义保证这些全是实际高块；
第53束继承的完整高块门 \(\|A_{m,k}\|_\infty<1/4\) 给
\[
 \|X_j\|_\infty
 <4^{-(n_0-1-j)}\frac{272}{255}|a_m^{\rm lab}|.
 \tag{L.20}
\]
因而构造确实属于原全尾规范空间，满足原方程、原固定标签，
且在平端衰减。第53束已证唯一性遂将其识别为原
\(\mathcal H_\Pi\) 的该模齐次允许列；不是另外选择的一条线。
逐模相加可用明确的正 majorant
\[
 \sum_{|m|\ge M_*}e^{\beta|m|}
       \sup_{j\ge128}\|X_{m,j}\|_\infty
 <\frac{272}{255}
       \sum_{|m|\ge M_*}e^{\beta|m|}|a_m^{\rm lab}|
 \tag{L.21}
\]
（非零有限和或绝对收敛序列）。这避免交换未经证明的
\(\sup\) 与和；完整实共轭条件可原样施加。

## 6. 下一步仍须支付的真正项

本结论已经保留整个真高前缀和无限低尾的两个 homogeneous 行，
但未估计任意物理 ordinary/weak 源的全部 Green 核，也不控制
非径向非零背景上不同频率之间的耦合。两 mean、独立高度、
端点电荷及实际 \(\Gamma^*\) 参数响应仍按各自完整方程消费。

\(M<M_*\) 的大有限频段不能以本结论免费省去。
已选径向 middle 的次指数逆还须与原 source 权、实际非径向
谱簇和最终 nonlinear 方程联立；本文不声称全 \(\mathcal F=0\)。

[必要精确算术程序](../scripts/fourfold_original_label_complete_low_tail.mjs)
和[实际运行门记录](../notes/2026-11-14-R119-original-label-complete-low-tail-rational.json)
保存分母、锥、乘积和双侧物理常数。无限未来极限及原允许列
身份由上面的证明给出，不由有限数值采样替代。
