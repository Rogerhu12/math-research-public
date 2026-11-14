# R271 附录：逐列低高度泄漏与扩大的三次对数共同费用前缀

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；短核泄漏观察：Astra-ISP-1cf8c51d / root。AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文把原短核两带性质与已有逐列完整候选结合，直接估计候选在同一个真幂底项之上的正交补量。对前 $K$ 个物理源头，新的平方误差是
$2(K-1)S_m[\sum_{j<K}j\|V_me_j\|\nu_m^{j-1}]^2$，
其中 $S_m=O(m^{-3})$。另外，由 R249 的单侧平衡相似范数得到同一个归一链基的列界 $\|V_me_j\|\le e^{134j^4}$，不支付整个条件数。

这使 $K\asymp(\log m)^{1/3}$ 的全尾前缀获得 $O(Km^{-3})$ 的共同费用平方误差；允许较慢的误差下降时，还可取明确更宽的
$K=1+\lfloor(\log m/134)^{1/3}\rfloor$，平方误差为 $O((\log m)/m)$。
两种界均以同源真幂底项为基准，并支付真正裸、完整最小链之差。

[已有逐列稿](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md) 已证明三次对数增长前缀及 $O(m^{-2})$ 的共同费用平方误差。本文不是首次证明该增长阶；新增的是低高度泄漏、单侧真实列成本及上述定量改善。普通 ISP、原 $N=M$ 和一般高头实际余流仍 OPEN。

依赖：[原逐列完整候选](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md)、[全尾低头源带](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)、[原短核泄漏与真正链逼近](R271-appendix-fixed-original-heads-asymptotic-common-right-cost-and-minimal-chain-closeness.md)、[R249 真实平衡相似](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)。

## 1. 同一个原全尾源和真幂底项

固定原 $m\ge5,d=2^m$、$A=A_m,D=D_m$ 和全部合法 $q$，记
$$
E_{\ell,p}=\ker D^\ell\cap\mathcal H_p,\qquad
U_{\ell,p}=E_{\ell,p}\ominus E_{\ell-1,p},
$$
$$
\nu_m=\|D_m\|\le m^{-1},\qquad
S_m=\sum_{a\ge m}(a+1)^{-4}\le(3m^3)^{-1}.
\tag{1.1}
$$
对任意整数 $2\le K\le d$，使用原全尾物理前缀
$$
\mathscr X_{K,q}
=\bigoplus_{i=0}^{\min(K-1,d-2)}e_iE_{d-i-1,q}.
\tag{1.2}
$$
源尾阶保持原 $d$，没有改成小头数 $K$。

对同一个 $r\in\mathscr X_{K,q}$，记真正裸、完整最小链为
$a(r),c(r)$，范数为 $\alpha(r),\lambda(r)$。
真幂链为
$$
b_t=(-1)^{t-1}(D^t:\mathcal H_{q+t}\to\mathcal H_q)^\dagger
A^{t-1}r,\qquad 1\le t\le K,
\tag{1.3}
$$
其余段为零。原真幂投影身份给
$$
\|b\|^2\le\alpha(r)^2\le\lambda(r)^2.
\tag{1.4}
$$

令 $V_m$ 为原一致、未缩放且首行列归一的 Jordan 链基：
$$
A_mV_m=V_mJ_d,\qquad
V_me_0=e_0,\qquad e_0^*V_m=e_0^*.
\tag{1.5}
$$
等价地，若 $\mathcal K_me_j=(A_m^*)^je_0$，则
$V_m=\mathcal K_m^{-*}$。这些上三角矩阵在共同前缀上严格一致，
且 $V_me_1=e_1$。

置
$$
u_i=e_0^*(D^{i+1})^\dagger A^ir,\qquad 0\le i<K.
\tag{1.6}
$$
当 $K=d$ 时最后一项为零。由 (1.3)，
$$
u_i=(-1)^i e_0^*b_{i+1},\qquad
u_i\perp E_{i+1,q+i+1},\qquad
\sum_i\|u_i\|^2\le\|b\|^2.
\tag{1.7}
$$
这里最后一个界比仅用 $\alpha^2$ 更强，并且仍来自同一个实际源。

## 2. 原两带算子的有限次越界估计

原交换子关系给
$$
\operatorname{ad}_D^3(D^*)=0,\qquad
D^*E_{\ell,p}\subseteq E_{\ell+2,p+1},
$$
因而
$$
DU_{\ell,p}\subseteq
U_{\ell-1,p-1}\oplus U_{\ell-2,p-1}.
\tag{2.1}
$$
同时有原短核界
$$
\|D|_{E_{\ell,p}}\|^2\le(\ell-1)S_m.
\tag{2.2}
$$
这些事实的完整交换展开和归纳已在短核泄漏稿 §§2–3 给出；
它们不要求 $D^*$ 保持 $E_\ell$。

在有限核旗并集上，把 (2.1) 的两条正交高度带记为
$$
D_0=\sum_{\ell\ge2}P_{U_{\ell-1}}DP_{U_\ell},
\qquad
D_1=\sum_{\ell\ge3}P_{U_{\ell-2}}DP_{U_\ell}.
\tag{2.3}
$$
孔层随每次 $D$ 减少一，式中略去它以免重复。
不同输入高度在每条单带内进入不同输出高度，所以
$$
D=D_0+D_1,\quad
\|D_0\|\le\nu_m,\quad
\|D_1|_{E_L}\|\le\sqrt{(L-1)S_m}.
\tag{2.4}
$$
例如最后一式逐个 $U_\ell$ 用 (2.2)，再对正交输出平方求和。
不需要从一般三角截断推算范数。

**越界引理。** 对整数 $t,j\ge1$，
$$
\boxed{
\left\|P_{E_{t,q+t}}D^j
(I-P_{E_{t+j,q+t+j}})\right\|
\le j\nu_m^{j-1}\sqrt{(t+2j-1)S_m}.
}
\tag{2.5}
$$
只在实际有限核输入上使用此式，已足够覆盖本文所有 $u_i$。

证明如下。由 (2.1) 或反复使用 $D^*E_\ell\subseteq E_{\ell+2}$，
左端只读取 $E_{t+2j,q+t+j}$ 中的输入。因此可把输入限制为
$E_{t+2j}\ominus E_{t+j}$。$D_0^j$ 只下降 $j$ 个高度，
在这段输入上投到 $E_t$ 后为零。有限恒等式
$$
D^j-D_0^j
=\sum_{a=0}^{j-1}D^{j-1-a}D_1D_0^a
\tag{2.6}
$$
中每一项，由 (2.4) 的范数界不超过
$\nu_m^{j-1}\sqrt{(t+2j-1)S_m}$。
相加便得 (2.5)。这里只付一次低高度 $D_1$；
其前后的所有步数仍保原 $\nu_m$ 次幂。

## 3. 完整候选相对真幂底项的正交差

原逐列稿的真正完整候选为
$$
\widetilde c_t=(-1)^{t-1}
\left[e_0u_{t-1}
+\sum_{j=1}^{K-t}(V_me_j)D^ju_{t+j-1}\right],
\quad 1\le t\le K,
\tag{3.1}
$$
其余段为零。这里仍使用同一个 $V_m$，没有为不同列重选相似。

为记录合法域，若 $r'=V_m^{-1}r$，则
$r'_i\in E_{d-i-1,q}$，且 $u_i=(D^{i+1})^\dagger r'_i$。
于是 $D^du_i=0$，(3.1) 中第 $t$ 段、Jordan 头 $j$ 的尾属于
$E_{d-j,q+t}$；上三角的 $V_m$ 只把头降到较低位置，所需尾旗只会变宽。
直接相消给
$$
D\widetilde c_1=r,\qquad
A\widetilde c_t+D\widetilde c_{t+1}=0.
\tag{3.2}
$$
所以它是原全部联合旗中的完整链。

任意这样的完整链均满足
$D^t\widetilde c_t=(-1)^{t-1}A^{t-1}r$。
真正 MP 投影因而准确给
$$
b_t=P_{E_{t,q+t}^{\perp}}\widetilde c_t,\qquad
\widetilde c_t-b_t=P_{E_{t,q+t}}\widetilde c_t.
\tag{3.3}
$$
由 (1.7)，无 $D$ 的第一项在 (3.1) 投到 $E_t$ 后消失。因此
$$
\widetilde c_t-b_t
=(-1)^{t-1}\sum_{j=1}^{K-t}
(V_me_j)P_{E_{t,q+t}}D^ju_{t+j-1}.
\tag{3.4}
$$
输入 $u_{t+j-1}$ 正交于 $E_{t+j}$，所以 (2.5) 正好适用。

定义真实逐列量
$$
\Phi_{K,m}=\sum_{j=1}^{K-1}
j\|V_me_j\|\nu_m^{j-1},\qquad
\delta_{K,m}^2=2(K-1)S_m\Phi_{K,m}^2.
\tag{3.5}
$$
当 $t+j\le K$ 时，
$t+2j-1\le2(K-1)$。对每个固定 $j$，
映射 $(u_i)_i\mapsto(P_{E_t}D^ju_{t+j-1})_t$
中，每个输入只使用一次。先在整链 Hilbert 直和中按该 $j$
取范数，再对 $j$ 相加，得到
$$
\|\widetilde c-b\|
\le\sqrt{2(K-1)S_m}\,\Phi_{K,m}
\left(\sum_i\|u_i\|^2\right)^{1/2}
\le\delta_{K,m}\|b\|.
\tag{3.6}
$$
由 (3.3) 的逐段正交性，主估计为
$$
\boxed{
\lambda(r)^2
\le\|\widetilde c\|^2
=\|b\|^2+\|\widetilde c-b\|^2
\le(1+\delta_{K,m}^2)\|b\|^2
\le(1+\delta_{K,m}^2)\alpha(r)^2.
}
\tag{3.7}
$$
它对原全部合法 $q$ 和 (1.2) 的全部尾核阶统一。

特别 $K=2$ 时 $\Phi_{2,m}=1$，直接恢复
$\lambda^2\le(1+2S_m)\|b\|^2$。
原逐列界只估计所有正次 $D$ 项；
(3.4) 则只估计它们越过真幂正交补的部分，这正是平方尾权出现的原因。

## 4. 同一个归一链基的单侧真实列界

以下证明
$$
\boxed{
V_me_1=e_1,\qquad
\|V_me_j\|\le\exp(134j^4)
\quad(2\le j\le d-1).
}
\tag{4.1}
$$
它改进原逐列稿使用整个条件数所得的 $e^{3536j^4}$。

先处理 $j\ge4$。令 $H=2^n$ 为不小于 $j+1$ 的最小二进制维数。
则 $8\le H\le2j$，且 $H\le d$。
R249 §4 对该实际小头给出
$$
A_n=\Sigma_n(\gamma_nJ_H)\Sigma_n^{-1},\qquad
\gamma_n=e^{20-\mathcal L_n},\qquad
\mathcal L_n=\frac{25H^4}{2(H-2)},
$$
$$
\|\Sigma_n\|\le H6^H.
\tag{4.2}
$$
R249 的明确式
$\Sigma_n=\operatorname{diag}(e^{-F(k)})C_{\widetilde h}^{\mathsf T}$
还有
$\Sigma_ne_0=e_0$、$e_0^*\Sigma_n=e_0^*$：
常数换元列与常数行均只有第零项，且 $F(0)=0$。

因此
$$
\widehat V_n=\Sigma_n
\operatorname{diag}(1,\gamma_n^{-1},\ldots,\gamma_n^{-(H-1)})
\tag{4.3}
$$
满足 $A_n\widehat V_n=\widehat V_nJ_H$ 和 (1.5) 的首行列归一。
这种上三角基是唯一的：第 $j$ 列由
$Av_j=v_{j-1}$、$e_0^*v_j=0$ 在 $F_{j+1}$ 中唯一确定，
因为 $A:F_{j+1}\cap e_0^\perp\to F_j$ 为三角同构。
故 (4.3) 正是原 $V_m$ 在该前缀的限制。

仅对第 $j$ 列使用 (4.2)，
$$
\log\|V_me_j\|
\le j(\mathcal L_n-20)+H\log6+\log H.
\tag{4.4}
$$
$H\ge8$ 给
$$
\mathcal L_n
=\frac{25}{2}\frac{H}{H-2}H^3
\le\frac{50}{3}H^3\le\frac{400}{3}j^3.
$$
又 $H\log6+\log H\le(2\log6+1)j<20j$，
所以 (4.4) 不超过 $(400/3)j^4<134j^4$。
没有支付 $\|\Sigma_n^{-1}\|$，且目标 $\gamma_n$ 的全部负幂已经逐列明付。

为免小维度回退破坏常数，直接核 $j=2,3$。
令 $\eta=\eta_0=e^{-1070}$、$b=1/4$。
两个原模型的首四头均可写为
$$
Ae_1=e_0,\quad
Ae_2=\theta e_0+\eta e_1,\quad
Ae_3=\xi e_0+\theta e_1+e_2,
\tag{4.5}
$$
其中 $N$ 型 $(\theta,\xi)=(b,0)$，
$Y$ 型 $(\theta,\xi)=(b-\eta,\eta)$。
这是原递归或原 $f_{N/Y}(B)$ 的精确展开，不丢弃 Cayley 项。
于是归一列准确为
$$
V_me_2=\eta^{-1}(e_2-\theta e_1),
$$
$$
V_me_3=
(2\theta^2\eta^{-2}-\xi\eta^{-1})e_1
-2\theta\eta^{-2}e_2+\eta^{-1}e_3.
\tag{4.6}
$$
因 $|\theta|\le1/4$、$0\le\xi\le\eta$，
$$
\|V_me_2\|\le2e^{1070},\qquad
\|V_me_3\|\le3e^{2140}.
$$
它们分别小于 $e^{134\cdot2^4}$、$e^{134\cdot3^4}$。
这补全 (4.1)，且仍是同一个一致链基。

## 5. 三次对数宽度与 O(K/m³) 的平方误差

定义
$$
J_m^{\rm fast}=
\max\left\{1,\left\lfloor
\left(\frac{\log m}{268}\right)^{1/3}
\right\rfloor\right\},\qquad
K_m^{\rm fast}=J_m^{\rm fast}+1.
\tag{5.1}
$$
对 $m\ge5$，$K_m^{\rm fast}\le m\le d$，并且
$K_m^{\rm fast}\asymp(\log m)^{1/3}$、趋于无穷。

若 $2\le j\le J_m^{\rm fast}$，则
$134j^4\le(j/2)\log m$。由 (4.1) 和 $\nu_m\le1/m$，
$$
\begin{aligned}
\Phi_{K_m^{\rm fast},m}
&\le1+\sum_{j=2}^{J_m^{\rm fast}}j\,m^{1-j/2}\\
&\le1+\frac{2-m^{-1/2}}{(1-m^{-1/2})^2}.
\end{aligned}
\tag{5.2}
$$
若 $J_m^{\rm fast}=1$，左边就是 $1$，同一上界仍成立。
$m\ge16$ 时右边小于 $5$，故
$$
\boxed{
\delta_{K_m^{\rm fast},m}^2
\le\frac{50J_m^{\rm fast}}{3m^3}
=O\!\left(\frac{(\log m)^{1/3}}{m^3}\right).
}
\tag{5.3}
$$
把它代入 (3.7)，即在这整个增长全尾前缀上，
完整、裸及真幂底项的费用比例统一趋于 $1$。

原逐列稿的宽度为
$1+\lfloor(\log m/7072)^{1/3}\rfloor$，
平方误差为 $O(m^{-2})$。
(5.1) 扩大其明确宽度常数，(5.3) 同时改善平方误差；
增长幂次本身没有改变。

## 6. 更宽临界选择仍一致趋于共同费用

若只要求误差趋零，可再取
$$
J_m^{\rm wide}=
\max\left\{1,\left\lfloor
\left(\frac{\log m}{134}\right)^{1/3}
\right\rfloor\right\},\qquad
K_m^{\rm wide}=J_m^{\rm wide}+1.
\tag{6.1}
$$
设 $J=J_m^{\rm wide}\ge2$。对 $2\le j\le J$，
$$
134j^4-j\log m
\le-134j(J^3-j^3)
\le-268J^2(J-j).
\tag{6.2}
$$
所以
$$
\begin{aligned}
\Phi_{K_m^{\rm wide},m}
&\le1+m\sum_{j=2}^Jj
\exp[-268J^2(J-j)]\\
&\le1+\frac{mJ}{1-e^{-268J^2}}
\le3mJ.
\end{aligned}
\tag{6.3}
$$
代入 (3.5) 得
$$
\boxed{
\delta_{K_m^{\rm wide},m}^2
\le\frac{6J^3}{m}
\le\frac{3\log m}{67m}\longrightarrow0
\quad(J\ge2).
}
\tag{6.4}
$$
$J=1$ 时直接用 $\delta^2=2S_m\le2/(3m^3)$。

因此临界逐列项可以达到 $O(mJ)$，仍由
$S_m=O(m^{-3})$ 支付。这里保留了指数和在其最大端点附近的衰减，
没有把所有列粗放到同一个最大列范数。

## 7. 真正链、两道桥与实际负图接口

原真正最小者满足
$$
\|a-b\|^2=\alpha^2-\|b\|^2
=\|\mathcal G^\dagger\zeta(r)\|^2,
$$
$$
\|c-a\|^2=\lambda^2-\alpha^2.
\tag{7.1}
$$
第二式来自 $\langle a,c\rangle=\|a\|^2$：
完整链低投影与同源裸最小者之差位于零首源裸核，
而高输入与裸最小者正交。不是任意两条候选链的平方关系。

因此对 (3.5) 的每个 $K$，都有
$$
\boxed{
\|\mathcal G^\dagger\zeta(r)\|^2+\|c(r)-a(r)\|^2
\le\delta_{K,m}^2\|b(r)\|^2.
}
\tag{7.2}
$$
(5.3)、(6.4) 同时给增长前缀上的真正出生一不相容、
新 $H_2^\circ$ 完整高能量和两条真正最小链的相对逼近。
这里的 $\mathcal G^\dagger\zeta$ 是这个 $r$ 的真正 MP 结果，
没有任意指定一个坏 primitive 替代它。

此外，(3.7) 对同一个未来带的已有角恒等式可直接使用。
若 $B,L,G$ 是原三 Gram，$W_K=B^{1/2}\mathscr X_{K,q}$，
$u=B^{1/2}r$、$H=B^{-1/2}LB^{-1/2}$，则
$$
\|P_{W_K}(I+H)u\|\le\delta_{K,m}\|y\|.
\tag{7.3}
$$
沿已有正 resolvent 校正
$$
z=B^{-1/2}(I+H)^{-1}P_{W_K}(I+H)u
$$
就有
$$
\langle(L+B)(r-z),s\rangle=0
\quad(s\in\mathscr X_{K,q}),
$$
$$
\chi(z)^2+2\mu(z)^2\le\delta_{K,m}^2\|y\|^2,\qquad
\mu(z)\le\tfrac12\delta_{K,m}\|y\|.
\tag{7.4}
$$
这是已有全窗口负图构造使用新的已付系数；
不把它重复登记为新的投影定理。
原全部窗口的累计预算、同一强极限和完整平坦配对按同一既有证明保持。
这项逐窗校正不被宣称仍来自同一个相容顶部流。

最后，(7.2) 并不把源前缀传给
$\mathcal G^\dagger\zeta$ 的头支撑，也不控制固定裸链的纯
$S_H^\dagger\mathcal R\mathcal G^\dagger\zeta$：
完整修复允许低域零首源改动，其与纯高域逆的差别保留。
同样不能在 $\lambda_{\rm flat}^2=\langle GLr,Lr\rangle$
中用前缀上的压缩比较交换完整 Gram，因为 $Lr$ 可离开这个前缀。
固定物理测试的真实源 $t_f$ 仍需另付其局部逆和高头分量。
