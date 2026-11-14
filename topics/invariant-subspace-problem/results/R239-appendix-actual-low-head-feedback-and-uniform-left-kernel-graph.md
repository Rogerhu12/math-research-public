# R239 附录：真实低头反馈、统一左核图及原负前缀的剩余算子

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文在原物理基和原完整左空间中，只用前 $K$ 头的归一链基，准确写出高头对低头的反馈；导数部分的费用与窗口长度无关。完整低头零源核是一张近等距图，其投影和最小者观察均有显式界。对实际强极限族，全部非零极限必须由文中一个确定的高头反馈算子承载；这给出原 $L+B$ 负前缀余问题的充分比较接口，未证明该比较。普通 ISP 与无权 $N=M$ 仍 OPEN。

依赖：[完整左 primitive 坐标](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)、[真实归一链基](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)、[逐列头预算](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md)、[两头负图及原 Schur](R239-appendix-paid-two-head-negative-graph-and-coupled-two-descent-schur.md)。

## 1. 原低头观察矩阵与高头反馈

固定原 $m\ge5,d=2^m,4d\le q\le e^{d^3/4}$。写 $A=A_m,D=D_m$，$\nu=\|D\|\le1/m$。取任意 $2\le K\le d$，令
$$
H_K=\operatorname{span}\{e_0,\ldots,e_{K-1}\},\qquad
A_K=A|_{H_K},\qquad V_K=V_m|_{H_K}.
$$
原归一给
$$
A_K=V_KJ_KV_K^{-1},\qquad V_K=1\oplus V_{K,+},\qquad
e_0^*A_K^j=e_j^*V_K^{-1}\quad(0\le j<K).
$$
因此真正的观察矩阵为
$$
O_K=(e_0^*A_K^j)_{j=0}^{K-1}=V_K^{-1}.
\tag{1.1}
$$
定义同一个原头的高行
$$
g_j=e_0^*A^j|_{H_K^\perp}\quad(0\le j\le K),\qquad
G_Kh=(g_jh)_{j=0}^{K-1},\qquad
\mathcal R_K=V_KG_K.
\tag{1.2}
$$
这里 $g_0=0$，所以 $\mathcal R_K$ 的整个像在 $H_K\ominus\mathbb Ce_0$。$\mathcal R_K$ 是实际高头反馈，后文不假定其范数一致有界，也不以整个 $A$ 的逆替代它。

## 2. 原左向量的逐孔准确式

取任意原 $v\in\mathscr V_q$，即
$$
v\in P_{\le q}H,\qquad Av_p+Dv_{p+1}=0\quad(0\le p<q).
$$
写 $x_p=P_{H_K}v_p,h_p=P_{H_K^\perp}v_p,u_p=e_0^*v_p$。由头尾交换，逐次代入得
$$
A^jv_p=(-1)^jD^jv_{p+j}\quad(p+j\le q).
$$
取第零行并用 (1.1)，得到
$$
\boxed{
x_p=e_0u_p+\sum_{j=1}^{K-1}(V_Ke_j)(-D)^ju_{p+j}-\mathcal R_Kh_p,
\quad 0\le p\le q-K+1.
}
\tag{2.1}
$$
又因 $A^K|_{H_K}=0$，下一阶准确为
$$
\boxed{D^Ku_{p+K}=(-1)^Kg_Kh_p\quad(0\le p\le q-K).}
\tag{2.2}
$$
这是原高头 forcing 下的真正 $K$ 次下降方程，不是先把源投成 primitive 后的方程。若随后求最小原像，必须使用此实际 $D^K$ 及其真实自由核。

所有项都在原空间：$v_{i,p}\in\ker D^{d-i}$；高头 $h_p$ 的尾核阶至多 $d-K$；在 $V_Ke_j$ 的第 $i$ 行有 $i\le j$，而 $D^ju_{p+j}\in\ker D^{d-j}\subseteq\ker D^{d-i}$。因此 (2.1) 没有扩大原联合尾旗。

令
$$
\Psi_{K,m}=\sum_{j=1}^{K-1}\|V_Ke_j\|\nu^j,
\qquad I_{K,q}=P_{\le q-K+1}.
$$
把 $j$ 固定后在全部输出孔层作直和，再用 Minkowski，(2.1) 给
$$
\boxed{
\|P_{H_K\ominus e_0}I_{K,q}v+\mathcal R_KI_{K,q}h\|
\le\Psi_{K,m}\|P_{[1,q]}u\|.
}
\tag{2.3}
$$
因此另有不付 $\|\mathcal R_K\|$ 的实际向量界
$$
\boxed{
\|\mathcal R_KI_{K,q}h\|
\le\sqrt{1+\Psi_{K,m}^2}\,\|v\|.
}
\tag{2.4}
$$
最后一步用头正交性：$P_{H_K\ominus e_0}I_{K,q}v$ 与整个 $e_0u$ 正交。这是对给定真实解的反馈值的上界，绝非 $\mathcal R_K$ 在任意高头输入上的算子范数上界。

## 3. 完整低头零源核的近等距图

在整个 $\le q$ 尾直和中置
$$
\mathcal E_{K,q}=\ker D^K\cap\mathcal H_{\le q},\qquad
\mathcal T_Kf=\sum_{j=0}^{K-1}(V_Ke_j)(-D)^jf.
\tag{3.1}
$$
这里 $D^j$ 降孔，不作任何向上原像。望远镜恒等式为
$$
(A+D)\mathcal T_Kf=(-1)^{K-1}(V_Ke_{K-1})D^Kf.
$$
故
$$
\boxed{
\operatorname{Ran}\mathcal T_K
=\ker(A+D)\cap(H_K\otimes\mathcal H_{\le q})
\subseteq\ker E_q.
}
\tag{3.2}
$$
反向等号也准确：对该低头完整核取 $f=e_0^*z$，在有限支撑之外补零，核方程逐行给 $V_K^{-1}z=\sum_j e_j(-D)^jf$，最后一行给 $D^Kf=0$。

写 $\mathcal T_K=e_0I+S_K$，其中 $S_K$ 的像正交于第零物理头。整链逐列估计给
$$
\|S_K\|\le\Psi_{K,m},\qquad
\mathcal T_K^*\mathcal T_K=I+S_K^*S_K.
\tag{3.3}
$$
这同时证明 (3.2) 的像闭，并给其真正正交投影
$$
P_{Z_K}=\mathcal T_K(I+S_K^*S_K)^{-1}\mathcal T_K^*.
\tag{3.4}
$$
若 $P_{0,K}$ 为到 $e_0\mathcal E_{K,q}$ 的物理正交投影，则
$$
\boxed{
\|P_{Z_K}-P_{0,K}\|
=\frac{\|S_K\|}{\sqrt{1+\|S_K\|^2}}
\le\frac{\Psi_{K,m}}{\sqrt{1+\Psi_{K,m}^2}}.
}
\tag{3.5}
$$
可直接核验：以 $R=(I+S_K^*S_K)^{-1}$ 写图投影的四块，投影差的平方为对角块 $I-R$ 和 $S_KRS_K^*$，两块的范数都由 $t/(1+t)$ 给出。这里不要求 $S_K$ 有闭像。

对任意真正左最小者 $v=E_q^\dagger r$，有 $v\perp Z_K$，故
$$
\boxed{
P_{\mathcal E_{K,q}}e_0^*v=-S_K^*P_{H_K\ominus e_0}v,
\qquad
\|P_{0,K}v\|
\le\frac{\Psi_{K,m}}{\sqrt{1+\Psi_{K,m}^2}}\,\mu_q(r).
}
\tag{3.6}
$$
这些界对 $q$ 一致，并适用于一般非primitive 源。右端是原完整左费，不能将 (3.6) 当作该左费已经由裸费或平坦费支付。

## 4. 增长前缀的真实极限：反馈承载而非坐标消失

取逐列稿的
$$
K_m=\max\left\{2,1+\left\lfloor(\log m/7072)^{1/3}\right\rfloor\right\},
\qquad \Psi_{K_m,m}\le\frac{2}{m(1-m^{-1/2})}\to0.
$$
设 $v_{m,q}=E_q^\dagger r_{m,q}$ 为同一个原 $w$ 的实际族，并在所取窗口上一致趋于 $w$。这包括已付负前缀校正后的族；不要求新族仍是一个共同顶部的源流。

因 $e_0$ 乘尾真空属于 $\ker E_q$，每个 $v_{m,q}$ 在全局第零基向量的系数为零，所以 $w_0=0$。对固定 $w$，物理头 $\ge K_m$ 的投影由全局指标 $\ge K_m$ 的尾控制；尾孔数至少一的投影由全局指标 $\ge d$ 的尾控制。因此一致地
$$
\|h_{m,q}\|\to0,\qquad \|u_{m,q}\|\to0,
\qquad\|(I-I_{K_m,q})v_{m,q}\|\to0.
\tag{4.1}
$$
最后一步用 $q-K_m+2\ge1$。这里既没有给 $w$ 增添衰减率，也没有把变化的源坐标认成固定的物理尾。

将 (4.1) 代入 (2.3)，在原全局 Hilbert 空间的自然嵌入下得到
$$
\boxed{
\mathcal R_{K_m}I_{K_m,q}h_{m,q}\longrightarrow-w
\quad\text{一致于所取窗口。}
}
\tag{4.2}
$$
特别，如果 $w\ne0$，这些高头输入虽然趋零，反馈值的范数却趋于 $\|w\|$。这是准确记录原左反馈，绝非由高头输入趋零推出反馈趋零；对随 $K_m$ 改变的 $\mathcal R_{K_m}$，后一推论需要新的输入。

## 5. 原 L+B 负前缀余问题的一个明确充分估计

现在令源 $r$ 满足真正负前缀
$$
\langle(L+B)r,s\rangle=0\quad(s\in X_{K,q}),
$$
其中 $X_{K,q}$ 是前 $K$ 物理源头、保原全部尾阶的闭空间。以该源分解写 $\mathcal D=L+B$，令
$$
R^-_{K,q}y=
\left(-\mathcal D_{XX}^{-1}\mathcal D_{XR}y,y\right),
\qquad r=R^-_{K,q}y.
$$
这是真正的源 Schur 图，和 (1.2) 的物理反馈 $\mathcal R_K$ 是不同算子。定义
$$
\mathfrak M_{K,q}=(R^-_{K,q})^*(B+LGL)R^-_{K,q},
$$
$$
\mathcal F_{K,q}=
\mathcal R_KI_{K,q}P_{H_K^\perp}E_q^\dagger R^-_{K,q}.
\tag{5.1}
$$
因此对同一个原源，
$$
\chi(r)^2=\langle\mathfrak M_{K,q}y,y\rangle,
\qquad \mathcal F_{K,q}y=\mathcal R_KI_{K,q}h.
$$
所有 $L+B$ 左右交叉块、裸度量和原完整平坦度量都在 (5.1) 中。

一个足够关闭这条实际极限路线的估计是，在同一实际族上证明
$$
\boxed{\|\mathcal F_{K_m,q}y\|^2
\le C_m\langle\mathfrak M_{K_m,q}y,y\rangle,}
\tag{5.2}
$$
其中全原窗口 $I_m=\{4d,\ldots,Q_m-d\}$、$Q_m=\lfloor e^{d^3/4}\rfloor$，$n_m=|I_m|$ 上的常数满足 $C_md/n_m=O(1)$。固定参数下的形式有界性不是所需的这一温和上界。这里只需这个比值一致有界，无需它趋零：下文还有原实际 $\beta_m^2\to0$ 因子。

确实，已付负前缀族满足
$$
\sum_{q\in I_m}\chi(r_{m,q})^2
\le(\sqrt2+\Psi_{K_m,m})^2d\beta_m^2\|w\|^2,
\qquad\beta_m\to0.
$$
若 (5.2) 成立，至少一个原窗口给
$$
\|\mathcal F_{K_m,q}y_{m,q}\|^2
\le C_m(\sqrt2+\Psi_{K_m,m})^2(d/n_m)\beta_m^2\|w\|^2\to0,
$$
与 (4.2) 矛盾，除非 $w=0$。这一步不要求额外尾衰减率，也不通过不合法的坐标删带。

本文没有证明 (5.2)。新的已付部分是 (2.1)–(3.6) 的原物理公式及统一界，以及 (4.2) 对真实剩余承载机制的定位。它将下一步明确集中到 (5.1) 中的高头反馈和同原两费用，而不是重新猜测整个头逆的范数。

## 与原核方程的准确关系

(4.2) 记录非零极限的真实反馈承载，不单独提供新的排核信息：固定K的该身份与原核低行方程相容。新增已付的是全q一致的导数预算、完整左核图及(5.1)对同一原L+B图和M费用的准确保留。当前尚未证明左最小lift对固定物理测试的非平凡一致逼近，也尚未支付(5.2)；高头输入趋零不能替代这一界。
