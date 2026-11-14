# R229：高频反馈的完整低频读出与均值消元

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-14。

**已证明的条件工具；本条没有新增数值实例化。** 本文给 R220/R222 的完整 pure-low 源补上未知高频扰动的低频反馈。已知系数保留其全部 Fourier 频率；未知高频的二次及以上项保持真正的差频抑制。完整均值变化单独由原 mean 方程解出，随后作为零频量进入源，绝不把它当成高频支持。

所用完整 mean 变分是已有的 [R75](R75-complete-mean-transport-and-shear-constraint.md)(75.5)、(75.8)，无小 $z$ 相减的 mean 正规式是 [R44](R44-compatible-outer-height-and-continuous-defect.md)(44.12)。[R98](R98-mixed-density-low-middle-high-closure.md) 已有完整商、mean 和三材料整体导数。本条新增的是保频率的低读出、完整 mean 的高频反馈消元及可接现存源表的正预算，未重称上述恒等式为新发现。

## 1. 同一真实源片上的范数与支持

固定一个原真实径向源片 $J$，背景仍为
$$
s=r_x/r,\qquad \ell=w_x/w,\qquad z=w^2,\qquad E=1+z.
\tag{229.1}
$$
以下 $N$ 均为原 source-$x$ 单位；没有另乘 $r_x$ 或换一个 $w$ 规范。

取有界实角宽 $\tau(x)$，以及常数
$$
0\le\tau_-\le\tau(x)\le\tau_+\le\eta.
$$
采用径向先取上确界的完整 signed-Fourier 范数
$$
\|f\|_{a,\tau;J}
=\sum_{m\in\mathbb Z}(1+|m|)^a
 \sup_{x\in J}e^{|m|\tau(x)}|f_m(x)|,\qquad a=0,1.
\tag{229.2}
$$
常宽 $\eta$ 时写成 $\|f\|_{0,\eta;J}$。以下所有已知系数范数均为这一径向量词，不用点态总和的上确界冒充它。该空间是 Banach 代数；角微分由 $W^1_\tau$ 映到 $W^0_\tau$。

令 $M>0$，$0\le L<M$，未知高频对 $H=(p,k)$ 满足
$$
p_m=k_m=0\quad(|m|<M),\qquad
\|p\|_{1,\tau;J}\le h_P,\quad
\|k\|_{1,\tau;J}\le h_K.
\tag{229.3}
$$
这里 $M$ 是物理 Fourier 频率；若数组标签为 $m/2$，所有指数仍用 $m$。当前低46/非低接口可取 $L=92,M=94$。本引理不要求未知 $H$ 有宽度 $\eta$。

记 $\Pi_{\le L}$ 为包含零频的 $|m|\le L$ 投影。源最终的 $\Pi_\perp$ 可以随后施加；先保留零频只会扩大以下上界。

## 2. 完整已知系数乘高频的两个支持引理

**引理 229.1（一个高因子）。** 若 $A$ 保留全部 Fourier 频率，$\|A\|_{0,\eta;J}\le a$，$r\in\{0,1\}$，则对任意支持于 $|n|\ge M$ 的 $H$，
$$
\|\Pi_{\le L}(A\partial_\theta^r H)\|_{0,\tau;J}
\le
a\,e^{-(\eta+\tau_-)(M-L)}
\begin{cases}
\|H\|_{1,\tau;J}/(1+M),&r=0,\\
\|H\|_{1,\tau;J},&r=1.
\end{cases}
\tag{229.4}
$$

**证明。** 对每个卷积对 $a+n=m$，$|m|\le L$、$|n|\ge M$，有
$$
\eta|a|+\tau(x)|n|-\tau(x)|m|
\ge(\eta+\tau(x))(|n|-|m|)
\ge(\eta+\tau_-)(M-L).
$$
另有 $1/(1+|n|)\le1/(1+M)$ 及 $|n|/(1+|n|)\le1$。先对每个 Fourier 系数取径向上确界，再对允许的卷积对求和，受完整已知系数质量与完整未知质量的乘积控制。没有对每个低输出重新消费同一完整高质量。证毕。

**引理 229.2（至少两个高因子）。** 设 $q\ge2$，每个 $H_i$ 均支持于 $|n|\ge M$，$r_i\in\{0,1\}$，并允许 $L\le M$。则
$$
\left\|\Pi_{\le L}
 \left(A\prod_{i=1}^q\partial_\theta^{r_i}H_i\right)
\right\|_{0,\tau;J}
\le e^{-2M\tau_-}\|A\|_{0,\eta;J}
 \prod_{i=1}^q
 \begin{cases}
 \|H_i\|_{1,\tau;J}/(1+M),&r_i=0,\\
 \|H_i\|_{1,\tau;J},&r_i=1.
 \end{cases}
\tag{229.5}
$$

**证明。** 置 $S_n=\sum_i n_i$，$a=m-S_n$。若所有 $n_i$ 同号，则
$$
\eta|a|+\tau(x)\sum_i|n_i|-\tau(x)|m|
\ge2\tau(x)(|S_n|-|m|)
\ge2M\tau(x).
$$
若同时有正、负指标，则
$$
\sum_i|n_i|-|S_n|
=2\min\!\left(\sum_{n_i>0}n_i,\sum_{n_i<0}|n_i|\right)\ge2M.
$$
结合 $|a|+|S_n|\ge|m|$ 与 $\eta\ge\tau(x)$ 仍得到同一下界。余下按引理 229.1 求和。全部 $q$ 的级数因此可逐项用同一个 $e^{-2M\tau_-}$；不是把某个二次支撑规则擅自用于完整非线性。证毕。

两个引理对复 Fourier 系数同样成立，只使用绝对值和实际支持。实余弦的正负半幅已经包含于范数定义；不另加一个“pair 2”。

## 3. 完整已知系数的解析尾：可用正量计算的形式

设某个完整函数的独立 jet 展开为
$$
F(J_0+\xi)=\sum_{\alpha\in\mathbb N^d}A_\alpha\,\xi^\alpha.
$$
假设它对常数复参数 $|\zeta_i|\le r_i$ 在 $W^0_\eta(J)$ 中全纯，并有同一完整范数界 $B_F$。Banach 值 Cauchy 公式给
$$
\|A_\alpha\|_{0,\eta;J}
\le B_F\prod_i r_i^{-\alpha_i}.
\tag{229.6}
$$
这里的多圆盘是对已知基场的系数解析域；不要求真实未知高场位于 $W^1_\eta$。

若每个真实 $\xi_i$ 是一个高频场或其一次角导数，并在 $W^0_\tau$ 中有帽 $x_i<r_i$，置 $q_i=x_i/r_i$。则所有总次数至少2的完整余项满足
$$
\left\|\Pi_{\le L}\sum_{|\alpha|\ge2}
 A_\alpha\,\xi^\alpha\right\|_{0,\tau;J}
\le e^{-2M\tau_-}B_F\,\Psi_d(q_1,\ldots,q_d),
$$
$$
\Psi_d(q)=\prod_{i=1}^d(1-q_i)^{-1}-1-\sum_{i=1}^d q_i.
\tag{229.7}
$$
这是完整收敛级数的上界，不是有限 Taylor 多项式代替完整逆。实际算术可用完全正的递推
$$
S_0=T_0=0,\quad
T_{j+1}=\frac{T_j+S_jq_{j+1}+q_{j+1}^2}{1-q_{j+1}},
\quad S_{j+1}=S_j+q_{j+1},
\tag{229.8}
$$
最后 $T_d=\Psi_d$，避免从已舍入的大总值中相减提取小尾。

证明 (229.7) 时先对未折叠的完整 Laurent 系数使用 (229.6) 与引理 229.2，再求正级数。若实现使用正循环卷积，它只能提供这些完整系数或质量的上界；不能把 cyclic 数组自身当作无 alias 的 Fourier 多项式。

## 4. 固定 pure-low 完整根后的 mean 缺陷

取同一基场 $(P_0,\bar K_0)$，$\langle\bar K_0\rangle=0$，其**完整**小根为 $c_0$。记
$$
K_0=c_0+\bar K_0,\quad T_0=P_{0,\theta},\quad
V_0=\bar K_{0,\theta},\quad U_0=V_0-P_0,
$$
$$
S_0=1-zP_0^2,\quad
D_0=1-z(2K_0+K_0^2+EP_0^2),\quad
L_0=1+K_0+ET_0.
\tag{229.9}
$$
基场可以遍历 R219 的整个低模盒；所有下列帽必须对该盒统一成立。它不是把内侧辅助场 $C_S$ 重标为外侧有限低场。

先把 $c$ 固定为 $c_0$。完整 mean 正规式为
$$
\mathcal F(P,K,T)
=\mathfrak a C_1(z\mathfrak a)
+\frac{(1+K)T}{1-zP^2}\,C(z\mathfrak a),
$$
$$
\mathfrak a=2K+K^2+EP^2,\qquad
C(u)=(1-u)^{-1/2},\qquad
C_1(u)=\frac1{\sqrt{1-u}\,(1+\sqrt{1-u})},
\qquad \mathcal M=\langle\mathcal F\rangle .
\tag{229.10}
$$
全部平方根与原实正支相连；此式没有小 $z$ 除法。

对独立 jet $(P,K,T)$ 取半径 $(r_P,r_K,r_T)$。一个明确的完整系数域充分条件如下。若
$$
P_*=\|P_0\|_{0,\eta;J}+r_P,\quad
K_*=\|K_0\|_{0,\eta;J}+r_K,\quad
T_*=\|T_0\|_{0,\eta;J}+r_T,
$$
$$
\mathfrak a_*=2K_*+K_*^2+E_*P_*^2,\qquad
u_*=z_*\mathfrak a_*<1,\qquad v_*=z_*P_*^2<1,
\tag{229.11}
$$
其中 $z_*,E_*$ 为同片真实背景上界，则
$$
B_{\mathcal M}
=\frac{\mathfrak a_*}{\sqrt{1-u_*}(1+\sqrt{1-u_*})}
+\frac{(1+K_*)T_*}{(1-v_*)\sqrt{1-u_*}}
\tag{229.12}
$$
上包 (229.10) 在整个复多圆盘的 $W^0_\eta(J)$ 范数。证明只用正级数与 Banach 代数乘法，故给完整 $S^{-1}$、$D^{-1/2}$；也可用更紧且已证明的完整系数域代替这些充分帽。

这些是**新宽度 $\eta$ 的 mean 分母门**。R220/R222 某个宽度下的有理源 $L^{-1}$ 门本身不推出 (229.11)，实角 $S,D>0$ 也不推出其复条带范数门。

令
$$
x_P=\frac{h_P}{1+M},\quad
x_K=\frac{h_K}{1+M},\quad x_T=h_P,\qquad
q_i=x_i/r_i<1.
\tag{229.13}
$$
R75(75.5) 的完整周期分部积分准确给出
$$
D\mathcal M_0[p,k]
=\left\langle A_P^{\mathcal M}p+
 A_K^{\mathcal M}k\right\rangle,\qquad
A_P^{\mathcal M}=-EU_0D_0^{-3/2},\quad
A_K^{\mathcal M}=L_0D_0^{-3/2}.
\tag{229.14}
$$
这一步保留完整 mean，且把变分中的 $p_\theta$ 精确移到已知系数；不是删除该角导数。设两完整系数范数上界为 $a_P^{\mathcal M},a_K^{\mathcal M}$。由引理 229.1 的 $L=0$ 及 (229.7)，固定 $c_0$ 的完整缺陷满足
$$
\left|\mathcal M(P_0+p,\bar K_0+k,c_0)
      -\mathcal M(P_0,\bar K_0,c_0)\right|
\le B_{\rm fixM},
$$
$$
B_{\rm fixM}
=\frac{e^{-(\eta+\tau_-)M}}{1+M}
 \left(a_P^{\mathcal M}h_P+a_K^{\mathcal M}h_K\right)
+e^{-2M\tau_-}B_{\mathcal M}\Psi_3(q_P,q_K,q_T).
\tag{229.15}
$$
左边的帽对整个径向片取上确界。第一项可用完整系数的真实高尾进一步收紧，但不能把这些系数擅自截断成有限低模。

## 5. 用完整 scalar mean 解出 $\delta c$

令 $c_1$ 是加入 $H$ 后同一完整小根，$\delta c=c_1-c_0$。若该根与整个连接段已经在统一实分支域内，并且
$$
\mathcal M_c(P_0+p,\bar K_0+k,c_0+t\delta c)
=\left\langle L D^{-3/2}\right\rangle\ge\mu>0
\quad(0\le t\le1),
\tag{229.16}
$$
则准确恒等式
$$
0=\mathcal M(P_0+p,\bar K_0+k,c_0)
+\delta c\int_0^1
 \mathcal M_c(P_0+p,\bar K_0+k,c_0+t\delta c)\,dt
$$
与基场 $\mathcal M_0=0$ 给
$$
\boxed{\quad |\delta c|\le d_c^{\rm new}:=B_{\rm fixM}/\mu.\quad}
\tag{229.17}
$$
这个零模变化并没有高频支持。其小性来自完整平均方程的高频配对和标量逆门。

也可以不先假设 $c_1$ 存在：取一个完整实区间 $|c-c_0|\le d_c$，在其上支付所有原分支门及 (229.16)，并核
$$
B_{\rm fixM}<\mu d_c.
\tag{229.18}
$$
则两端异号、严格单调性给唯一同支实根及 (229.17)。这个 $c$ 区间必须属于原 small-mean 域；不能只扩大半径而不重新付分支门。

复参数情形须加强为同一个角度 $\phi$ 下的**统一 sector 门**
$$
\operatorname{Re}\!\left(e^{-i\phi}\mathcal M_c\right)\ge\mu>0
\tag{229.19}
$$
于整个 $c$ 圆盘及全部相关非均值数据。仅有逐点 $|\mathcal M_c|\ge\mu$ 不足以控制其线段积分。若 (229.19) 与 (229.18) 成立，则
$F(c)-F(c_0)=(c-c_0)\int_0^1F'(c_0+t(c-c_0))dt$
在圆周的模至少为 $\mu d_c$，且 $F-F(c_0)$ 在凸圆盘内只有 $c_0$ 一个简单零点；Rouché 定理给完整 $F$ 唯一零点。由同一积分式得到 (229.17)。实际已有的 $|\mathcal M_c-1|\le1-\mu$ 是 $\phi=0$ 的一个充分条件。

## 6. 完整两材料源的一阶系数与所有高阶项

保持 R75(75.9)/R98(98.6) 的完整有理源：
$$
\mathcal N=sN_s+\ell N_\ell,\qquad
N_s=\frac{E(V-P)^2}{L},\qquad
N_\ell=\frac{K^2+2EKT+ET^2-zP^2}{L},\qquad
L=1+K+ET .
\tag{229.20}
$$
这里 $K$ 含完整 mean，$T=P_\theta,V=\bar K_\theta$；不是只取某个 $N_4$ 截断。

在 $c=c_0$ 固定时对四 jet $(P,K,T,V)$ 展开。令
$A_{\ell,0}=K_0^2+2EK_0T_0+ET_0^2-zP_0^2$。其完整一阶系数为
$$
\begin{array}{c|cccc}
 &p&k&p_\theta&k_\theta\\ \hline
N_s&
-2EU_0/L_0&
-EU_0^2/L_0^2&
-E^2U_0^2/L_0^2&
2EU_0/L_0\\
N_\ell&
-2zP_0/L_0&
(2K_0+2ET_0)/L_0-A_{\ell,0}/L_0^2&
2E(K_0+T_0)/L_0-EA_{\ell,0}/L_0^2&
0 .
\end{array}
\tag{229.21}
$$
这些是完整已知系数，包含 $L_0^{-1}$ 的无限频谱。

对每材料 $r\in\{s,\ell\}$，记四个系数的 $W^0_\eta(J)$ 帽为 $a_{r,P},a_{r,K},a_{r,T},a_{r,V}$。为第四 jet 取半径 $r_V>h_K$，置 $q_V=h_K/r_V$；其余 $q$ 用 (229.13)。假设整个四 jet 复多圆盘的完整 $N_r$ 范数上界为 $B_r$。例如若已付完整 $L^{-1}$ 范数 $\Lambda_*$，并置
$V_*=\|V_0\|_{0,\eta;J}+r_V$，则可取
$$
B_s=E_*(V_*+P_*)^2\Lambda_*,
$$
$$
B_\ell=
(K_*^2+2E_*K_*T_*+E_*T_*^2+z_*P_*^2)\Lambda_* .
\tag{229.22}
$$
一个可直接计算的充分逆门是
$$
a_0:=\inf_{x\in J}|1+c_0(x)|>0,\qquad
g_L=a_0-\|\bar K_0+ET_0\|_{0,\eta;J}-r_K-E_*r_T>0,
\quad \Lambda_*=g_L^{-1}.
\tag{229.23}
$$
更紧的完整逆系数包也可替代它。所有门必须覆盖整个多圆盘；不能只检查基点。

因此固定 $c_0$ 的低输出帽为
$$
B_{r,\rm fix}(L)=
e^{-(\eta+\tau_-)(M-L)}
\left[
 \left(\frac{a_{r,P}}{1+M}+a_{r,T}\right)h_P+
 \left(\frac{a_{r,K}}{1+M}+a_{r,V}\right)h_K
\right]
+e^{-2M\tau_-}B_r\Psi_4(q_P,q_K,q_T,q_V).
\tag{229.24}
$$
证明是一阶逐项用引理 229.1，其余完整级数用 (229.7)。它同时包含高频与已知系数的全部和频、差频，以及任意阶高频相互作用。

## 7. 必须保留的零模反馈与最终低读出

完整变化按两个准确差分分解：
$$
\begin{aligned}
&N_r(P_0+p,\bar K_0+k,c_1)-N_r(P_0,\bar K_0,c_0)\\
={}&[N_r(P_0+p,\bar K_0+k,c_0)-N_r(P_0,\bar K_0,c_0)]\\
&+\delta c\int_0^1
 \partial_cN_r(P_0+p,\bar K_0+k,c_0+t\delta c)\,dt .
\end{aligned}
\tag{229.25}
$$
原完整导数为
$$
\partial_cN_s=-\frac{EU^2}{L^2},\qquad
\partial_cN_\ell=\frac{2K+2ET}{L}
-\frac{K^2+2EKT+ET^2-zP^2}{L^2}.
\tag{229.26}
$$
这里 $c_\theta=0$，但 $\partial_cN_r$ 一般具有全部 Fourier 频率；不能因 $\delta c$ 是标量就删去其非零输出。

在**加入高频之后的整个真实 $c_0\to c_1$ 管**中，若按 $W^0_\tau(J)$ 统一支付
$$
\|P\|\le P^\dagger,\quad \|K\|\le K^\dagger,\quad
\|T\|\le T^\dagger,\quad \|U\|\le U^\dagger,\quad
\|L^{-1}\|\le\Lambda^\dagger,
$$
则充分的完整导数帽为
$$
J_{c,s}=E_*(U^\dagger)^2(\Lambda^\dagger)^2,
$$
$$
J_{c,\ell}=2(K^\dagger+E_*T^\dagger)\Lambda^\dagger
+\bigl((K^\dagger)^2+2E_*K^\dagger T^\dagger
 +E_*(T^\dagger)^2+z_*(P^\dagger)^2\bigr)
 (\Lambda^\dagger)^2.
\tag{229.27}
$$
这里不需要未知高频有宽度 $\eta$；必须支付其实际 $\tau$ 管及完整 inverse/mean 域。

**定理 229.3（消去完整 mean 的高到低反馈）。** 在上述全部门下，
$$
\boxed{
\|\Pi_{\le L}\Delta N_r\|_{0,\tau;J}
\le B_{r,\rm fix}(L)+J_{c,r}\frac{B_{\rm fixM}}{\mu}
=:B_{r,\rm low}(L).}
\tag{229.28}
$$
因此原两材料合成的非线性 source-$x$ 低输出满足
$$
\|\Pi_{\le L}\Delta\mathcal N\|_{0,\tau;J}
\le s_*B_{s,\rm low}(L)+|\ell|_*B_{\ell,\rm low}(L)
=:B_{\rm low}(L).
\tag{229.29}
$$
证明由 (229.24)—(229.27) 的准确差分和三角不等式直接得到。完整零频、全部逆尾和 mean 标量反馈均保留。

(229.28) 的意义是：固定 $c$ 的高频作用获得支持抑制，而 mean 先经过完整平均方程的小反馈，再由完整 $\partial_cN$ 返回低频。它没有把 $\delta c$ 当成高支持，也没有用 $N_4$ 或二次多项式替代完整 $N$。

## 8. 共享质量、逐模输出与已成 pure-low 源的接线

若另外知道同一高场的共享帽
$$
\|p\|_{1,\tau;J}+\|k\|_{1,\tau;J}\le h,
$$
一阶式中的 $a h_P+b h_K$ 可以与 $\max(a,b)h$ 取最小。不能只由共享 $h$ 就宣称两个分量各占 $h/2$。高阶正式可以在
$0\le x\le h_P,\ 0\le y\le h_K,\ x+y\le h$
上取严格正优化上界，也可以保留已证的分量帽；两者都是新计算中必须明确的选择。

(229.29) 是同一低频集的一份完整质量。对每个偶模 $0<m\le L$，可以独立令目标截止为 $m$ 得到合法单模上界
$$
|(\Delta\mathcal N)_m^{\cos}|
\le e^{-m\tau_-}B_{\rm low}(m).
\tag{229.30}
$$
此处是原相对 $(P,K)$ 方程的余弦 source-$x$ 幅度，未乘角权、$(1+m)$、$d_0=\sqrt{rw^3}$ 或 $r_x$。在原偶/余弦对称类中，正负 Fourier 半幅的绝对值和恰为余弦幅度，故没有新增因子2。

这些逐模帽与共享 $B_{\rm low}(L)$ 是同时有效的约束。若消费者使用逐模帽，可逐模收费；若使用共享质量，则应先把真实输出列合权后取 support 或 max 列，整份质量只用一次。不能把各输出的独立最优分配相加后又称为同一个最优共享分配。

令 $\widehat Y$ 为 R184/R215/R219 的同一候选，$E_{\rm lo}$ 遍历 R219 盒，$H$ 为真实高频误差。R222 已成表包的是
$$
N(\widehat Y+E_{\rm lo},c_0)-N(\widehat Y,c_{\widehat Y}),
$$
其中两个 mean 都是其完整小根。新表只需正向增加本条的
$$
N(\widehat Y+E_{\rm lo}+H,c_1)
 -N(\widehat Y+E_{\rm lo},c_0).
\tag{229.31}
$$
这就是完整误差源的准确 telescoping。旧 R222 字节及其 conditional pure-low 量词不改，新量词由新完整盒/门承担。若用 R220 加权源与 R222 无 twist 源相交，必须先保持它们原来已证的同场身份；本条不会令 cyclic alias 成为精确高频支持。

## 9. 可消费的最小真实数据 schema

建议新 producer 使用 schema
`complete-high-to-low-mean-eliminated-source-v1`，只生成新文件，不改 R220/R222 主件。

顶层应绑定：

- 同一 candidate、背景、R219 低盒、R220 完整 mean/尾、R222 pure-low 源及实际高盒的原 SHA；不借另一个 $C_S$ 或有限 shooting 场。
- `status="conditional_full_low_plus_high_source"`、实际参数域、物理频率 `M`、目标 `L`，以及原 source-$x$/余弦/strong-norm 单位。
- 完整 owned 资源状态与 source/argv；未经实际运行时不填 `all_gates=true`。

每个原径向 row 至少保留：

1. `cell, segment, part, left, right, global_leaf_index`，原真实角宽的 `tau_lower,tau_upper`，所选 `known_coefficient_eta`。
2. 高场的真实整片 `high_P_W1_moving_upper, high_K_W1_moving_upper`，以及若已证明则保存的 `high_joint_W1_moving_upper`。入口必须是一般 $P+K$ 的真高迹及完整高响应；不能沿用旧 pure-K 假设。
3. $(r_P,r_K,r_T,r_V)$、所有 $q_i$、正递推 $\Psi_3,\Psi_4$；完整 mean 多圆盘的 $u_*,v_*,B_{\mathcal M}$，完整 $N_s,N_\ell$ 的逆门与 $B_s,B_\ell$。
4. R75 两个完整 mean 变分系数及 (229.21) 全部已知系数的 $\eta$ 范数帽；若从有限 Laurent 加完整尾获得，则两部分和原尾身份都保留。
5. 完整 scalar 域、$\mu$ 或复 sector、`fixed_c_mean_defect_upper`、`delta_c_upper`，实际全管 $(P^\dagger,K^\dagger,T^\dagger,U^\dagger,\Lambda^\dagger)$ 与两个 $J_c$。
6. 两材料的 `linear_high_to_low_upper`、`complete_nonlinear_high_remainder_upper`、`complete_mean_feedback_upper` 正分账；最后保存逐模 `complete_high_correction_mode_caps`、共享 `complete_high_correction_low_W0_moving_upper`。
7. 如输出 `complete_delta_N_mode_caps`，它必须是旧 R222 全源与新校正按 (229.31) 正向相加的完整结果。另明确 raw caps 是否已经合入 $s,|\ell|$，消费者不可再乘一次材料。

必须实际核的门包括：全部输入有限且非负；$0\le\tau_-\le\tau_+\le\eta$；真高支持与原分区一致；所有 $q_i<1$；完整 mean 的 $S,D$ 新宽门；完整 $L$ 逆门；真实 scalar 根/连接段或圆盘的统一导数门；完整物理/mean 原域；全部共享质量不重复消费。精确 dyadic 或有理数保存沿用原包规范。

所有 (229.11)—(229.29) 只需有限标量与已知系数/完整尾上界。可以先在一个实际源片上形成新门和正分账，找出具体瓶颈；本条不要求重跑任何已成功 ODE，也不把纯代数门尚未支付的状态改名为证书。

## 10. 已完成的逻辑与仍未支付的应用

本条已经完整证明：未知高频对低输出的线性反馈、任意阶反馈、完整 mean 的 scalar 消元及其返回低频的费用。它不依赖对完整 inverse 或 mean 进行有限截断。

当前应用仍须给出真实、位置相关、一般 $P+K$ 的高盒；在该盒上实际支付本条列出的新宽系数门和 scalar/源门；将新低像以及完整高像一起核入 R226 的因果管条件。R220/R222 的 pure-low 成功本身没有支付这些新高扰动。本文也没有免费宣称未知高场升宽、原外 $0,\ldots,6$ 延拓、完整非线性留管或最终闭面完成。

### 已实读的原结果与工作包身份

- R44：`results/R44-compatible-outer-height-and-continuous-defect.md`，Git blob `50be0cc3a7449de26c92d0c597e9bd4b562b56d4`；使用 (44.12)、(44.14) 的完整正规式与 mean 导数。
- R75：`results/R75-complete-mean-transport-and-shear-constraint.md`，Git blob `756ff2bad26e7b2cee83a211667ed027e96851c0`；使用 (75.5)、(75.8) 的完整周期变分，不重新包装为本条的新恒等式。
- R98：`results/R98-mixed-density-low-middle-high-closure.md`，Git blob `ee1595fbad1699bfff566e7e3416ce87e7e04a9a`；保持其完整 source-$x$、mean、inverse 与径向量词。
- 上述三个 blob 均在已实读提交 `e3b7f8f48244870fd7b902fc28168cfc7dcf937c` 下定位。
- R219 真实低盒主 SHA256：`55cb6c5b88c0d51b767699d24c31f3cad7a8d33f86c16c3c6b8b6219969b537e`。
- R220 完整 weighted 源主 SHA256：`627870138cd2642e4ef7163d185f74de9d9c4466b16f174c3f28691648aa991b`。
- R222 完整无 twist/min 源主 SHA256：`88b589bfbc162c8481d6437d3f52d0a08725229a5582a0db48d4eea1e33f5c1f`。这些科学包身份是新消费接口的绑定目标，不是声称本条的新标量门已经运行。
