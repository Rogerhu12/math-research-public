# 同一物理 gap 的全源正滤波：真实负图、左近似与两费用的统一控制

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 这是[原物理夹逼／三费稿](2026-11-14-physical-joined-sandwich-and-same-increment-three-fee-fixed-test-budget-789f-next.md)的全源推论。对任意原实际源，不先假定负图或给定顶部前驱，定义
\[
\boxed{\mathcal E=(L+B)^{-1}L-(L+G^{-1})^{-1}L.}
\]
则
\[
\boxed{\mu(r-\mathcal Er)^2+\tfrac12\Xi(\mathcal Er)^2
\le\Xi(r)^2,}
\]
而 \(\mathcal Er\) 自动属于真实首头负图，事实上属于全部 bare／完整共同费用方向的负图。
此算子不是原两费用正交投影，不据此迭代声称统一费用，也不消去未付主左配对。

## 1. 原空间和正滤波

固定一组原合法参数，在同一个原源空间使用
\[
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,
\quad \Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2.
\]
\(L,B,G\) 是固定参数下有界严格正算子，且真正可行集给
\[
B\preceq G^{-1}.
\]
记 \(S=L+B\)、\(H=G^{-1}-B\succeq0\)。对任意 \(r\)，令
\[
u_{\rm b}=S^{-1}Lr,\qquad
u_{\rm f}=(L+G^{-1})^{-1}Lr,\qquad
e=u_{\rm b}-u_{\rm f}=\mathcal Er.
\tag{1.1}
\]

作 \(L\) 度量的单位化：
\[
X=L^{-1/2}BL^{-1/2},\qquad
Y=L^{1/2}GL^{1/2}.
\]
有 \(X\preceq Y^{-1}\)，以及
\[
\widetilde{\mathcal E}
=L^{1/2}\mathcal EL^{-1/2}
=(I+X)^{-1}-(I+Y^{-1})^{-1}
\]
\[
\boxed{\widetilde{\mathcal E}
=I-X(I+X)^{-1}-Y(I+Y)^{-1}.}
\tag{1.2}
\]
保留整个非交换算子，仅在各自的谱演算内改写。由 \(B\preceq G^{-1}\)，
\[
\boxed{0\preceq\widetilde{\mathcal E}\preceq I,\qquad
0\preceq I-\widetilde{\mathcal E}\preceq X+Y.}
\tag{1.3}
\]
故 \(\mathcal E\) 是原 \(L\) 内积中的正收缩；特别
\[
\mu((I-\mathcal E)r)^2
\le\langle L(I-\mathcal E)r,r\rangle
\le\Xi(r)^2.
\tag{1.4}
\]
下面的物理论证另支付 \(\mathcal Er\) 的两费用，不能仅由 (1.3) 免费声称任意不同度量中的收缩。

## 2. 同一个原物理 gap 与完整能量身份

取真实左最小向量 \(f=U_qr\)。它支持在 \(\le q\)，与 \(\mathcal K_q\) 正交，所以夹逼稿中的 \(t_q=r,k_q=0,q_q=f\)。

令
\[
z=P_{\mathcal M_q}f
=(U_qu_{\rm b},-\mathcal A_qu_{\rm b}),
\]
\[
y=P_{\mathcal K_{q+d}}f
=(U_qu_{\rm f},-\mathcal C_q^{\min}u_{\rm f}),
\qquad x=f-z.
\]
\(x\perp\mathcal M_q\)、\(y\in\mathcal M_q\)，故 \(x\perp y\)。其范数为
\[
\|x\|^2
=\langle Lr,r\rangle
-\langle Lr,(L+B)^{-1}Lr\rangle
\le\alpha(r)^2,
\tag{2.1}
\]
\[
\|y\|^2
=\langle Lr,(L+G^{-1})^{-1}Lr\rangle
\le\lambda_{\rm flat}(r)^2.
\tag{2.2}
\]
(2.1) 可在 (1.2) 的 \(X\) 坐标中用
\(X(I+X)^{-1}\preceq X\)；(2.2) 直接用
\((L+G^{-1})^{-1}\preceq G\)。

置同一个未来差
\[
h=\mathcal A_qu_{\rm b}-\mathcal C_q^{\min}u_{\rm f}.
\]
则
\[
x+y=(U_q(r-e),h),
\]
所以
\[
\boxed{
\mu(r-e)^2+\|h\|^2
=\|x\|^2+\|y\|^2
=\langle L(I-\mathcal E)r,r\rangle.}
\tag{2.3}
\]

前稿的两个真正未来投影准确给
\[
P_{\rm b,min}h=\mathcal A_qe,\qquad
P_{\rm f}h=-F_{\rm f}^*Le.
\]
因此 \(\Xi(e)^2\le2\|h\|^2\)。结合 (2.1)--(2.3)，得到全源结论
\[
\boxed{
\mu(r-\mathcal Er)^2+\tfrac12\Xi(\mathcal Er)^2
\le
\langle L(I-\mathcal E)r,r\rangle
\le\Xi(r)^2.}
\tag{2.4}
\]
尤其
\[
\mu(r-\mathcal Er)\le\Xi(r),\qquad
\Xi(\mathcal Er)\le\sqrt2\,\Xi(r).
\tag{2.5}
\]

这也有精确正配对
\[
\langle L\mathcal Er,(I-\mathcal E)r\rangle=\|h\|^2\ge0,
\]
\[
\mu(r)^2=\mu(\mathcal Er)^2
+\mu((I-\mathcal E)r)^2+2\|h\|^2.
\tag{2.6}
\]
主左能量 \(\mu(\mathcal Er)^2\) 未被 (2.4) 支付。

令 \(V_L=U_qL^{-1/2}\) 为真实左最小像的等距映射。完整物理 gap 投影
\(\mathsf G_q=P_{\mathcal M_q}-P_{\mathcal K_{q+d}}\) 给
\[
\boxed{\widetilde{\mathcal E}=V_L^*\mathsf G_qV_L.}
\tag{2.7}
\]
所以这里的正性也来自原物理正交投影，不只是形式矩阵假设。

## 3. 全部共同费用方向的真实负图

两个正规方程给
\[
\boxed{S\mathcal Er=H u_{\rm f}.}
\tag{3.1}
\]
故对全部 \(s\in\ker H=\ker(G^{-1}-B)\)，
\[
\boxed{\langle S\mathcal Er,s\rangle=0.}
\tag{3.2}
\]
这正是[同未来带共同费用负图](../results/R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md) §4 使用的全部共同 bare／完整费用方向。原第零源头包含在 \(\ker H\)，所以
\[
\boxed{\mathcal Er\in\mathscr N_q
=\ker[P(L+B)]=\operatorname{Ran}T_{q+1}.}
\tag{3.3}
\]
不要求 \(H\) 有闭值域，也不反演 \(H\)。

更准确的范围说明是
\[
\overline{\operatorname{Ran}\mathcal E}^{\,L}
=\{u:\langle Su,s\rangle=0\ \forall s\in\ker H\}.
\tag{3.4}
\]
证明：由 (3.1)，
\(\ker\mathcal E=L^{-1}S(\ker H)\)；
\(\mathcal E\) 在 \(L\) 中自伴，其像闭包等于此核的 \(L\) 正交补。
这里的核身份使用 \(S s=(L+G^{-1})s\) 对 \(s\in\ker H\) 成立。
没有将闭包删掉，也没有声称 \(\mathcal E\) 是到该负图的幂等投影。

## 4. 可一次进入原联合余负图

沿[真正负源图和联合旗](../results/R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)取
\(\mathscr Z_q=\mathscr N_q\cap\mathscr X_q\)，在原
\(\mathfrak M_q=B+LGL\) 度量中令
\[
s=P_{\mathscr Z_q}^{\mathfrak M_q}\mathcal Er,\qquad
\widehat e=\mathcal Er-s.
\]
既有结论给
\[
\widehat e\in\mathscr R_{{\rm rem},q},\qquad
\Xi(\widehat e)\le\Xi(\mathcal Er),\qquad
\mu(s)\le\delta_m\Xi(\mathcal Er).
\]
对 (2.4) 的两项作一次二维 Cauchy，得到
\[
\boxed{
\mu(r-\widehat e)\le
\sqrt{1+2\delta_m^2}\,\Xi(r),\qquad
\Xi(\widehat e)\le\sqrt2\,\Xi(r).}
\tag{4.1}
\]
因此任何原小两费用来源都能经这个准确滤波与既有投影进入真实余负图，并保持同一个左向量极限。没有利用一个费用未知的任意首头投影。

本稿的联合旗投影只支付一次。后续[统一幂预算](2026-11-14-physical-gap-uniform-powers-and-high-spectrum-source-filter-789f-next.md)已进一步证明 \(\Xi(\mathcal E^n r)\le\sqrt2\,\Xi(r)\) 对全部 \(n\ge1\) 一致，并保留随 \(\sqrt n\) 增长的左误差；该结论不要求反复乘单步常数。操作后各窗口仍未被证明组成同一条源流。即使两边都在 \(\mathscr R_{\rm rem}\)，\(\mathfrak M_q\) 正交仍不能代替 \(L_q\) 正交；原剩余主左配对继续开放。
