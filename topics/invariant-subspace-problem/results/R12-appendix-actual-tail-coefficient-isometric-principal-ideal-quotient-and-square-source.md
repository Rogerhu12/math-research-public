# R12 后续：实际零阶尾块、主理想闭包的完全等距商及平方来源的四阶必要条件

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

本稿给原完整交换子的一条范数闭包恒等式，并把同分母四次费用转成该商上的准确必要条件。没有把商中四次方为零改成原算子为零，也不排除既有全部整数幂共同分母。

## 1. 同一原有限头

固定原 Haar 尾 $C=A^{(m_0)}$，记 $\mathscr A=\{C\}'$，$w_j=\alpha_{m_0+j}$，$D=2^L$，$B_L=A^{(m_0+L)}$。沿用[完整尾系数分解](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)的真实物理基：
$$
C=J_L\otimes I+e_{0,D-1}\otimes B_L,\qquad
C^D=b_L I_D\otimes B_L,\qquad
b_L=\beta_{D-1}.
$$
这里 $\beta_r=\prod_{h=1}^r w_{v_2(h)}$。每个 $X\in\mathscr A$ 唯一写成
$$
X=\sum_{r=0}^{D-1}C^r(I_D\otimes X_{r,L}),\qquad
X_{r,L}\in\{B_L\}',\qquad
\|X_{r,L}\|\le\beta_r^{-1}\|X\|.
\tag{1}
$$
定义实际零阶尾块
$$
\Phi_L(X)=X_{0,L}=X_{00}^{\mathrm{block}}.
\tag{2}
$$
它是物理正交压缩，故完全收缩；此时没有施加任何尾字符。

继续分尾时，$\Phi_{L'}(X)$，$L'>L$，正好是 $\Phi_L(X)$ 的低 $L'-L$ 位零号对角块。确实，按 $r=t2^L$ 对较深的 (1) 分组，常数尾系数为这些项之和；再取其零号头对角块，只有 $t=0$ 留下。因此
$$
\|\Phi_{L'}(X)\|\le\|\Phi_L(X)\|,\qquad
q(X):=\lim_{L\to\infty}\|\Phi_L(X)\|
\tag{3}
$$
存在。

## 2. 到实际主理想闭包的准确距离

令
$$
\mathscr J_1=\overline{C\mathscr A}^{\,\|\cdot\|}.
$$
对每个 $L$，(1) 直接给
$$
X-I_D\otimes\Phi_L(X)
=C\sum_{r=1}^{D-1}C^{r-1}(I_D\otimes X_{r,L})
\in C\mathscr A.
\tag{4}
$$
所以 $\operatorname{dist}(X,\mathscr J_1)\le\|\Phi_L(X)\|$。

反向必须保留回绕。对 $R\in\mathscr A$，$CR$ 的常数尾项是
$$
\Phi_L(CR)=b_L B_L R_{D-1,L}.
$$
由 (1) 及 $\|B_L\|=w_L$，
$$
\|\Phi_L(CR)\|\le w_L\|R\|\longrightarrow0.
\tag{5}
$$
对任何 $R$，收缩性给
$$
q(X)\le\|X-CR\|.
$$
取下确界，结合 (4)，得到
$$
\boxed{\operatorname{dist}(X,\mathscr J_1)
=\lim_{L\to\infty}\|\Phi_L(X)\|.}
\tag{6}
$$
特别，
$$
\mathscr J_1=\{X\in\mathscr A:\|\Phi_L(X)\|\to0\}.
\tag{7}
$$

所有证明对固定有限矩阵放大逐项成立，且 (1)、(2)、(5) 的常数不增加。因此对每个 $d\ge1$，
$$
\operatorname{dist}\bigl(\mathbf X,M_d(\mathscr J_1)\bigr)
=\lim_{L\to\infty}\|\Phi_L^{(d)}(\mathbf X)\|.
\tag{8}
$$
这里闭包与距离都是原算子范数；没有使用弱或强闭包。

## 3. 真实乘法误差及完全等距商实现

实际乘法给
$$
\Phi_L(XY)-\Phi_L(X)\Phi_L(Y)
=b_L B_L\sum_{r=1}^{D-1}X_{r,L}Y_{D-r,L}.
\tag{9}
$$
原权反转身份为
$$
\frac{\beta_{D-1}}{\beta_r\beta_{D-r}}
=\frac1{w_{v_2(r)}}.
$$
所以
$$
\|\Phi_L(XY)-\Phi_L(X)\Phi_L(Y)\|
\le\tau_L\|X\|\|Y\|,\qquad
\tau_L=w_L\sum_{j=0}^{L-1}\frac{2^{L-j-1}}{w_j}\longrightarrow0.
\tag{10}
$$
这也是矩阵放大中的真实乘法估计。

将各尾 Hilbert 空间用其原 Haar 标准模型识别，令
$$
\mathscr B=
\prod_{L\ge1}\mathcal B(H_L)\big/
\{(T_L):\|T_L\|\to0\}.
$$
由 (9)、(10)，
$$
\Theta(X)=[(\Phi_L(X))_L]
\tag{11}
$$
是含单位的有界代数同态。由 (6)、(8)，其核正是 $\mathscr J_1$，且诱导
$$
\boxed{\mathscr A/\mathscr J_1\ \longrightarrow\ \mathscr B}
\tag{12}
$$
为完全等距代数嵌入。右侧是具体算子序列的商；没有把其像宣称为自伴代数或半单代数。

这与完整兼容喷射不同：喷射先在尾系数上施加字符，(6) 则直接记录同一实际尾算子的范数。

## 4. 同一平方分子的必要条件

设实际 $P,Y\in\mathscr A$ 满足
$$
Y^2=CP^2.
\tag{13}
$$
不预设 $P$ 单射或稠密像。记 $K=\|P\|$、$M=\|Y\|$、$c=w_0$，并设
$$
\rho_L=2w_L\sum_{j=1}^{L-1}\frac{2^{L-j-1}}{w_j},\qquad
e_L=\rho_LM^2/c+\tau_LK^2.
$$
空和取零。沿用[完整两列同源四次费用](R12-appendix-full-two-column-quartic-source-cost-and-accretive-denominator-exclusion.md)的原两个来源回绕项，得
$$
\|\Phi_L(P)^4\|
\le
\frac{4M^2}{c^2}\bigl(2^Lw_LK^2+\tau_LM^2\bigr)
+\frac{4M^2}{c}e_L+e_L^2
\longrightarrow0.
\tag{14}
$$
这里只控制四次方。另由 (10) 逐次乘法，
$$
\|\Phi_L(P^4)-\Phi_L(P)^4\|\le3\tau_LK^4\longrightarrow0.
\tag{15}
$$
(7)、(14)、(15) 给新必要条件
$$
\boxed{P^4\in\overline{C\mathscr A}^{\,\|\cdot\|}.}
\tag{16}
$$
等价地，原闭包商中
$$
\Theta(Y)^2=0,\qquad \Theta(P)^4=0.
\tag{17}
$$
第一式也直接来自 (13)，第二式需要保留下一真实头列及全部回绕来源，不能仅把 (13) 中 $C$ 在商里设零得到。

没有证明该商无非零幂零元，所以不把 (16) 改成 $P\in\mathscr J_1$；也没有把闭包成员改成 $P^4=CR$ 的有界实际除法。

## 5. 尚未排除的来源

此前[完整喷射平坦理想](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)与实际全部幂共同理想须继续区分。尤其
$$
\mathfrak F=\bigcap_{n\ge1}C^n\mathscr A
\subset C\mathscr A\subset\mathscr J_1,
$$
所以原 $Q_*$ 等共同整数幂分母自动满足 (16)。本稿没有支付其同一平方分子，也没有排除它。

同样，没有证明 $\mathscr A/\mathscr J_1$ 半单、没有识别全部平坦理想与各主理想闭包之交，也没有从实际尾块范数极限推普通不变子空间的存在。后续仍须构造真实 $Y^2=CP^2$，或支付另一条原来源桥。
