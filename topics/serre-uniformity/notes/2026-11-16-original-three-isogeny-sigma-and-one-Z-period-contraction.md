# 原三同源 sigma 标量、五方向一阶与一个原 Z 周期

日期：2026-11-16。会话：serre-public-astra-20261115。状态：**新的准确纸面恒等式和原来源收缩；尚未运行本篇的代数系数或41进周期计算。**

本篇接 [RF 原刚性化纤维](2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)、[SP 原 sigma](2026-11-16-original-CM-sigma-and-Poincare-period-inputs.md) 与 [41处真实输入](2026-11-16-original-41-adic-field-good-model-and-sigma-input.md)。新内容有三项：

1. 沿原三同源的规范 sigma 比较，准确消去 RF/SP 中同一原比较函数的贡献，并保留真正的 c0 范数常数。
2. 用原五次加法及真实 $\rho$ 运输，将五个椭圆一阶项写成七个原基点的 $\mathcal Z$ 值和代数项。
3. 在原41处唯一完成域中，利用真实 Galois 作用及 trace，将它们再写成**一个原 $\mathcal Z_b(f(c_1))$ 值**的五个线性泛函。

原 $Y$ 纤维、同一 Hecke 校准、全部非 $p$ 数据、原 splitting 运输与原 $C_h$ 始终保留。本文不是已经证明指定高度不相消，也不重登 UE 已证的抽象第二类修正相消。

## 1. 固定原对象和非实下降记号

继续取
$$
C_b:y^2=x^3+b,\quad \omega_b=\frac{dx}{2y},\quad \xi=-x/y,\qquad
\zeta^2+\zeta+1=0,\quad s=1+2\zeta,
$$
$$
\alpha=1-\zeta^2,\qquad \bar\alpha=1-\zeta,\qquad
\alpha\bar\alpha=3,\quad \alpha^3=3s.
\tag{ZA.1}
$$
这里 $\alpha$ 是原三同源标量，不是三次根 $\sqrt[3]4$。原
$f=f_4,\ g_j=(1+T^j)f$、$f_R=[\alpha]f,\ g_{R,j}=[\alpha]g_j$，
及五个次数比均保持 R791/R844/RF 的值：
$$
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134),
\qquad \delta_j=p_j-q_j.
\tag{ZA.2}
$$

设 $w$ 在原 $c_1$ 盘中，$z=a-1$ 是原粗参数。
写 $P_h(w)=h([w-c_0])$；不把 $w$ 或 $z$ 改成 $Y$ 的参数 $t=a^3$。
$\sigma$ 是原 $L/K$ 的七阶自同构，固定 $\zeta$。
在共同地方扩域 $E$ 中，对 $k=0,\ldots,6$ 定义
$$
P_{h,k}=\sigma^k P_h,\quad b_k=\sigma^k b,\qquad
P_{h,k}^*\omega_{b_k}=a_{h,k}(z)\,dz.
$$
所有点、切向、域作用和模型尺度都来自原 R844/R846。

为了区别 SP 使用的实下降点，本篇置
$$
\mathcal A_h^0(w)
 =\sum_{k=0}^6\operatorname{tr}_{\chi,E}
       \mathcal L_{b_k}(P_{h,k}(w)),
\qquad
\mathcal B_h^0
 =\sum_{k=0}^6\operatorname{tr}_{\chi,E}
       \bigl(\mathcal Z_{b_k}(P_{h,k}(c_1))a_{h,k}(0)\bigr).
\tag{ZA.3}
$$
则 $(\mathcal A_h^0)'(c_1)=\mathcal B_h^0$。上标 $R$ 表示同样定义作用于 $h_R$；所以 $\mathcal A_h^R,\mathcal B_h^R$ 正是 SP.29 的 $\mathcal A_h,\mathcal B_h$。

$\operatorname{tr}_{\chi,E}$ 和 $\chi_E$ 始终是 SP.6 的规范化扩张：
$$
\chi_E=\frac1{[E:\mathbf Q_p]}\chi_p\circ N_{E/\mathbf Q_p}
       =\operatorname{tr}_{\chi,E}\circ\log_E.
\tag{ZA.4}
$$
对 $K$ 中的量也按这个真正的扩张角色取值，不把复嵌入或单一任意地方代替原 $\mathbf Q_p$ 角色。最终等式从 RF 已有的 $\mathbf Q$ 三次纤维推出；未声称单个非实下降 theta 纤维自行成为 $\mathbf Q$ 纤维。

## 2. 原三同源的规范除法函数恰为 alpha x

$[\alpha]$ 的核为 $O$ 与 $x=0$ 的两个三挠点。因此
$$
\operatorname{div}(x)=[\alpha]^*[O]-3[O].
$$
又 $\xi([\alpha]P)=\alpha\xi(P)+O(\xi(P)^2)$。
SP 的原点帧为 $\xi^{-1}$，故唯一保持该刚性化的正乘函数是
$$
\boxed{\psi_\alpha(P)=\alpha x(P).}
\tag{ZA.5}
$$
确实 $\psi_\alpha\xi^2\to\alpha$，并将源帧
$\xi([\alpha]P)^{-1}\sim(\alpha\xi)^{-1}$
送到 $\xi^{-3}$。这里的标量 $\alpha$ 不能省去。

原加法公式给
$$
x([\alpha]P)=-\frac{\zeta}{3}\frac{x(P)^3+4b}{x(P)^2},
\qquad \alpha^2=-3\zeta^2.
$$
因此
$$
D_\omega^2\log(\alpha x)
 =2x-\frac{4b}{x^2}
 =3x-\alpha^2x([\alpha]P).
\tag{ZA.6}
$$
由 SP.11，形式比值
$\sigma_b([\alpha]P)/(\alpha x(P)\sigma_b(P)^3)$
的对数二阶导为零。该比值为偶函数，原点首常数为1，所以
$$
\boxed{\sigma_b([\alpha]P)=\alpha x(P)\sigma_b(P)^3.}
\tag{ZA.7}
$$

此式还给原 cubical 延拓的完整恒等式。可以不诉诸任何未固定的复积分路径：对正整数 $n$，原除子与首项给
$$
\psi_\alpha([n]P)\psi_n(P)^3
 =\psi_n([\alpha]P)\psi_\alpha(P)^{n^2}.
\tag{ZA.8}
$$
取 $n$ 使 $[n]P$、$[\alpha n]P$ 在 SP 形式盘内，将 (ZA.7)、(ZA.8) 与 SP.19 联用；所得误差被 $n^2$ 乘成零，故在特征零中误差就是零。于是对本次所有原非挠点，
$$
\boxed{\mathcal L_b([\alpha]P)
 =3\mathcal L_b(P)+\log_E(\alpha x(P)),}
\tag{ZA.9}
$$
$$
\boxed{\mathcal Z_b([\alpha]P)
 =\bar\alpha\,\mathcal Z_b(P)+\frac{2y(P)}{\alpha x(P)}.}
\tag{ZA.10}
$$
后式由对前式求导及 $[\alpha]^*\omega=\alpha\omega$ 得到。
R843 的原非挠性排除了本次 $x(P)=0$，因为它正是非零的三同源核。
这没有重新计算任何原点或核。

## 3. 比较函数完全抵消，但真实 c0 常数留下

保留 RF.3–4 的原函数，记 $N=N_{L/K}$：
$$
\mathcal R_j
 =\frac{N(y_{g_j}^2-b)^{q_j}}{N(y_f^2-b)^{p_j}}
 =\left(\frac{N(x_{g_j})^{q_j}}{N(x_f)^{p_j}}\right)^3,
$$
$$
M_h=N(\lambda_h^3),\qquad
M_j=\frac{M_f^{p_j}}{M_{g_j}^{q_j}},\qquad
\kappa_j=M_j^2,\qquad
\nu_j=\alpha^{21\delta_j}M_j.
\tag{ZA.11}
$$
$M_h$ 是原 $c_0$ Hodge 首项的真七次范数。
这里的 $\mathcal R_j$ **没有再除一个 $N(b)$**。
R848/R850 已把这些完整原标量固定；不能将主函数改成
$\mathcal R_j/(\kappa_jt^{14\delta_j})$ 后仍套用本式。

对七个原分量逐一应用 (ZA.9)：
$$
\mathcal A_h^R
 =3\mathcal A_h^0+\chi_E\bigl(\alpha^7N(x_h)\bigr).
\tag{ZA.12}
$$
所以
$$
q_j(\mathcal A_{g_j}^R-3\mathcal A_{g_j}^0)
-p_j(\mathcal A_f^R-3\mathcal A_f^0)
=-7\delta_j\chi_E(\alpha)+\frac13\chi_E(\mathcal R_j).
\tag{ZA.13}
$$
这一步保留完整七次范数与原 $\sigma(b)$；没有把 $N(b)$ 写成 $b^7$。

把 (ZA.13) 代入 SP.32：
$$
\lambda_{p,h_j}
=\mathcal A_{g_j}^R-\frac{p_j}{q_j}\mathcal A_f^R
 +\frac1{3q_j}\chi_E(\nu_j\kappa_j/\mathcal R_j)
 +\frac1{q_j}\tau_{Y,p}(v_j).
$$
$\mathcal R_j$ 的项相消，而
$-21\delta_j\chi_E(\alpha)+\chi_E(\nu_j)+\chi_E(\kappa_j)
=3\chi_E(M_j)$。得到
$$
\boxed{
\lambda_{p,h_j}(w)
 =3\left(\mathcal A_{g_j}^0(w)
         -\frac{p_j}{q_j}\mathcal A_f^0(w)\right)
  +\frac{\chi_E(M_j)+\tau_{Y,p}(v_j(w))}{q_j}.
}
\tag{ZA.14}
$$
这是原 $c_0$ 规范确定的等式，不是只比较导数后任设积分常数。
原 $M_j$ 及 $v_j$ 的刚性化仍完整出现。
原 $Y$ 因子未消失，完整 Corr 中的 theta 二挠与 Picard 反因子也没有被改写。

对原 $z=a-1$ 求一次，令
$u_Y=(d/dz)\log P_Y|_{c_1}$，有
$$
\boxed{
\Lambda'_{h_j}(c_1)
 =3\left(\mathcal B_{g_j}^0-\frac{p_j}{q_j}\mathcal B_f^0\right)
  +\frac1{q_j}\tau'_{Y,p}(v_j)-2\ell_{h_j}(u_Y).
}
\tag{ZA.15}
$$
这说明 SP.33 的显式 $\mathcal R_j'/\mathcal R_j$ 与三同源产生的代数导数准确相消；不表示它们各自为零。若仍保一个未经 SP.5 运输的旧 $A$ splitting，须减同一个原 $\Delta_h$ 及其导数，不能将其省为零。

## 4. 原 Z 的加法公式及其全盘定号

对同一 $C_b$ 上的 $P=(x,y)$、$Q=(X,Y)$，$x\ne X$ 时，置
$$
m(P,Q)=\frac{Y-y}{X-x}.
$$
在原 $\omega=dx/(2y)$ 规范中，有
$$
\boxed{\mathcal Z_b(P+Q)
 =\mathcal Z_b(P)+\mathcal Z_b(Q)+m(P,Q).}
\tag{ZA.16}
$$
特别是斜率的系数为1，符号为正。

纸面证明如下。原加法给 $x(P+Q)=m^2-x-X$，直接微分有
$$
D_{\omega,P}m=2x+X-m^2=x-x(P+Q).
$$
故 (ZA.16) 两边之差对 $P$ 的导数为零。
令 $P$ 在原点形式邻域趋近 $O$，在 Abel 参数 $\mathfrak z$ 中
$\mathcal Z_b(P)=\mathfrak z^{-1}+O(\mathfrak z)$、
$m(P,Q)=-\mathfrak z^{-1}+O(\mathfrak z)$，零常数确定差为0。
在两个形式变量中也得到相同的准确形式恒等式。

为说明没有跨 residue disk 的未知局部常数，置
$F_n=D_\omega\log\psi_n$。
由 SP.22 得
$\mathcal Z_b([n]P)=n\mathcal Z_b(P)+F_n(P)/n$。
形式盘上的 (ZA.16) 因而给有理恒等式
$$
m([n]P,[n]Q)
 =n\,m(P,Q)+
   \frac{F_n(P+Q)-F_n(P)-F_n(Q)}n.
\tag{ZA.17}
$$
它作为 $C_b\times C_b$ 上的有理函数等式，由形式恒等式全局成立。
于是加法式误差 $\mathcal E(P,Q)$ 满足
$\mathcal E([n]P,[n]Q)=n\mathcal E(P,Q)$。
选择 $n$ 将三个所需点送入形式盘后，左边为0，故原误差为0。
实际五个 secant 分母已由 R843/R844 的真实 Hom 点分离认证；无需重做数值零判。
相同恒等式的可去极限给 doubling 斜率 $3x^2/(2y)$，本篇五条原加法只用已成 secant 分支。

## 5. 真实 rho 运输及七个基点周期

若
$$
D_u:C_b\longrightarrow C_{u^6b},\qquad
(x,y)\longmapsto(u^2x,u^3y),
$$
则原参数与微分满足
$\xi_{\rm target}=u^{-1}\xi_{\rm source}$、
$D_u^*\omega_{\rm target}=u^{-1}\omega_{\rm source}$。
SP 的唯一规范立即给
$$
\mathcal L_{u^6b}(D_uP)=\mathcal L_b(P)-\log_Eu,\qquad
\mathcal Z_{u^6b}(D_uP)=u\,\mathcal Z_b(P).
\tag{ZA.18}
$$
这些是原帧的准确缩放；不是自由更换微分。

现在在 $c_1$ 置
$$
P_k=\sigma^k f(c_1),\quad
a_k=a_{f,k}(0),\quad
Z_k=\mathcal Z_{b_k}(P_k).
$$
对 $1\le j\le5$、$0\le k\le6$，记 $r=k+j\bmod7$，
$$
\eta_{k,j}=\sigma^k(\rho_j),\qquad
Q_{k,j}=D_{\eta_{k,j}^{-1}}P_r.
\tag{ZA.19}
$$
原 R791/R844 给
$T^jf=D_{\rho_j^{-1}}\sigma^jf$，所以
$\sigma^kg_j=P_k+Q_{k,j}$，两项都在原 $C_{b_k}$ 上。
其切向和 Z 值为
$$
a(Q_{k,j})=\eta_{k,j}a_r,\qquad
\mathcal Z_{b_k}(Q_{k,j})=\eta_{k,j}^{-1}Z_r.
\tag{ZA.20}
$$
这里把下标 $r$ 按7取余只用了 $\sigma^7=1$。
$\rho_j$ 仍是原完整迭代；**不将 $T^7=[\zeta^2]$ 改成 $1$**，
也不以漏掉环绕相位的比值代替 $\eta_{k,j}$。

令原五个 secant 及其共轭为
$$
c_{k,j}
=\frac{y(Q_{k,j})-y(P_k)}{x(Q_{k,j})-x(P_k)}.
\tag{ZA.21}
$$
这些是 R844 已成加法的原斜率，不需再次作点加法。
由 (ZA.16)、(ZA.20)：
$$
\mathcal B_{g_j}^0
=\sum_{k=0}^6\operatorname{tr}_{\chi,E}
 \left[(Z_k+\eta_{k,j}^{-1}Z_{k+j}+c_{k,j})
              (a_k+\eta_{k,j}a_{k+j})\right].
\tag{ZA.22}
$$

重新排列同一有限和，得到
$$
\boxed{
3\left(\mathcal B_{g_j}^0-\frac{p_j}{q_j}\mathcal B_f^0\right)
=\operatorname{tr}_{\chi,E}
 \left(\sum_{\ell=0}^6 C_{j,\ell}Z_\ell+D_j\right),
}
\tag{ZA.23}
$$
其中
$$
C_{j,\ell}
=3\left[
 \left(2-\frac{p_j}{q_j}\right)a_\ell
 +\eta_{\ell,j}a_{\ell+j}
 +\eta_{\ell-j,j}^{-1}a_{\ell-j}\right],
$$
$$
D_j=3\sum_{k=0}^6c_{k,j}(a_k+\eta_{k,j}a_{k+j}).
\tag{ZA.24}
$$
所有下标按7取余，$\eta$ 的定义始终是 (ZA.19) 的真实 $\sigma$。
$C_{j,\ell},D_j$ 是原有限代数表达式。
trace 作用于整个乘积；不能把 $C_{j,\ell}\in E$ 当作有理数从 trace 外提出。
本式没有声称 $Z_\ell$ 线性独立或任何 $C$ 子式非零。

## 6. 原41处直接留在14坐标域

[41处输入](2026-11-16-original-41-adic-field-good-model-and-sigma-input.md) 已证明
$$
L_{41}=\mathbf Q_{41}(b,s),\quad [L_{41}:\mathbf Q_{41}]=14,
\quad e=7,\ f=2,
$$
及扩域 $E=L_{41}(r)$ 的 $e=42,f=2$。它还证明对所有本次原非挠点
$$
v_{41}\bigl(\xi_b([42]P)\bigr)\ge0,\quad
v_{41}(b)+6v_{41}\bigl(\xi_b([42]P)\bigr)\ge1/7,\quad
\xi_b([42]P)^2x([42]P)\equiv1\pmod{\mathfrak m_E}.
\tag{ZA.25}
$$
但 $P,[42]P,\xi_b([42]P),\psi_{42}(P)$ 本身全部属于原 $L_{41}$。
SP 的原坏约化模型公式只需要 (ZA.25)，不需要其参数的赋值严格为正。
所以实际数值求值可以直接在 $L_{41}$ 内按
$$
\boxed{
Z=\mathcal Z_b(f(c_1))
 =\frac{\mathcal Z_b([42]f(c_1))}{42}
   -\frac{D_\omega\log\psi_{42}(f(c_1))}{42^2}
}
\tag{ZA.26}
$$
及 SP 的 $b,\xi$ 全尾公式进行。

84次域用于证明所有点落入正确形式分支；
**数值消费者无需先把14坐标扩成84坐标**。
直接保原模型与原帧时，不产生一个应另扣的 $\log r$。
若实现另选好模型，仍须逐项用 41S.19–23 运输，不得因本段而删去该标量。

原 $L/K$ 的每个 $\sigma^k$ 保持41处唯一素理想，故延拓为 $L_{41}$ 的连续等距自同构。
SP 中的 $H_n$ 及所有形式有理系数属于 $\mathbf Q$；
原分支 $u\equiv1$、除法函数和 $D_\omega$ 也随真实模型相容。
对 (ZA.26) 逐项作用 $\sigma^k$，收敛及其全尾界保持，因而
$$
\boxed{Z_k=\sigma^k Z.}
\tag{ZA.27}
$$
这不是在未知积分上任取七个相位；它直接来自原除法函数和收敛形式式。
全部共轭 Z 球可由**一个原14坐标 Z 球**运输，不需七次独立级数求值。
准确原点仍须从 U.1 或以后已接受的 A.1 获得；辅助518位及未接受短候选不能进入这里。

## 7. 一个 Z 的五个原 trace 泛函

在41处令 $a=a_0$、$\rho=\rho_j$、$c_j=c_{0,j}$，
并使用原 $L_{41}$ 的规范化角色
$$
\operatorname{tr}_{\chi,L}
 =\frac{c_\chi}{14}\operatorname{Tr}_{L_{41}/\mathbf Q_{41}},
\qquad \chi_{41}=c_\chi\log_{41}.
$$
它是 (ZA.4) 在原子域上的限制，不能用未规范化 trace 替换。
所有七个分量是原 $\sigma$ 共轭，因此
$$
\mathcal B_f^0=7\operatorname{tr}_{\chi,L}(Za),
$$
$$
\mathcal B_{g_j}^0
 =7\operatorname{tr}_{\chi,L}
   \left[(Z+\rho_j^{-1}\sigma^jZ+c_j)
                   (a+\rho_j\sigma^ja)\right].
\tag{ZA.28}
$$
用 trace 对 $\sigma$ 不变，特别是
$$
\operatorname{tr}_{\chi,L}\bigl(\sigma^jZ\,\rho_j^{-1}a\bigr)
 =\operatorname{tr}_{\chi,L}
    \bigl(Z\,\sigma^{-j}(\rho_j^{-1}a)\bigr),
$$
得到
$$
\boxed{
3\left(\mathcal B_{g_j}^0-\frac{p_j}{q_j}\mathcal B_f^0\right)
 =7\operatorname{tr}_{\chi,L}(\mathscr C_j Z+\mathscr D_j),
}
\tag{ZA.29}
$$
$$
\boxed{
\begin{aligned}
\mathscr C_j
 &=3\left[
    \left(2-\frac{p_j}{q_j}\right)a
    +\rho_j\sigma^j(a)
    +\sigma^{-j}(\rho_j^{-1}a)\right],\\
\mathscr D_j
 &=3c_j\bigl(a+\rho_j\sigma^j(a)\bigr).
\end{aligned}}
\tag{ZA.30}
$$
外面的7来自原七个 Weil 分量，没有额外把 trace 除以7。
$\sigma^{-j}$ 是同一个原七阶自同构的逆，
仍不改变 $T^7=[\zeta^2]$。
$\mathscr D_j$ 不等于 R848 的 c0 首项 $d_j$，符号区别明确。

(ZA.29) 可视为原数据上的精确线性泛函；
不要求分别知道一个 Z 的七个“独立周期”。
它不声称未知 $Z$ 已被代数量取代，也不从五个原斜率非零推出五个高度非零。

## 8. 同原 Y 一次列的完整连接

将 (ZA.29) 代回 (ZA.15)，已经得到
$$
\Lambda'_{h_j}(c_1)
 =7\operatorname{tr}_{\chi,L}(\mathscr C_j Z+\mathscr D_j)
   +\frac1{q_j}\tau'_{Y,41}(v_j)-2\ell_{h_j}(u_Y).
\tag{ZA.31}
$$
[YP 原 Y 连接和 Hecke 校准](2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md)
进一步给同一个最后两项的来源表达式：
$$
\boxed{
\Lambda'_{h_j}(c_1)
 =7\operatorname{tr}_{\chi,L}(\mathscr C_j Z+\mathscr D_j)
  +\frac{c_\chi}{Nq_j}
     \left[
      \left.\frac{\phi^*\alpha_j^e}{dz}\right|_{c_1}
         -U_jL_{\rm H}^{-1}e\,u_Y
     \right].
}
\tag{ZA.32}
$$
这里 $L_{\rm H}$ 表示 YP 的同一个实际 Hecke 对数矩阵，
用下标防止它与原数域 $L$ 混淆。
$e,f=de,N,\alpha_j^e$、实际 norm 纤维及全非 $p$ 行 $U_j$
均按 YP 原定义；它们仍待实际构造和求值。
$N$ 已进入原连接与第二槽，不在左侧重复乘一次。
本式没有反演一个高度矩阵，也没有新添高度非退化假设。

零阶仍用 (ZA.14) 的原 $M_j$ 与完整 $Y$ 纤维，
或 YP.37–38 的六个完整全球 line-height。
只把椭圆一次项收缩为一个 Z，不能据此删除原常数列、
原 $\ell$ 中的全球校准或六个因子的各自非 $p$ 项。
最后的指定 $\mathscr T_p$、其非零证与全尾共同根问题仍未解决。

## 9. 原来源消费者的准确范围

| 对象 | 真实旧源 | 本篇新消费 |
|---|---|---|
| $f,T^jf,g_j$ 坐标与五 secant | R844 的529节点及原非零义务 | 取旧节点；不重复作五次点加法 |
| 原 $a,\rho_j,\sigma$ | R791/R846 的733节点、真实域作用与切向 | (ZA.24)、(ZA.30) 的有限代数表达式 |
| $\nu,\kappa,M_j,\mathcal R_j$ | R848/R850 的原真范数与完整帧 | (ZA.11)–(ZA.15) 的准确运输与相消 |
| 原41输入 | R840 U.1 或未来实际通过的 A.1 | 同一14坐标域的四响应球；不读辅助518为41值 |
| 一个 $Z$ | 原 $f$、SP/41S 的固定42与全尾 | (ZA.26)，其七共轭只由真实 $\sigma$ 运输 |
| 原 Y 行及全部常数 | RF/YP、R724 原 Hecke 轨道和非 $p$ 数据 | (ZA.14)、(ZA.32)，不改基点或 splitting |

后继若生成 $\mathscr C_j,\mathscr D_j$ 的 DAG，
须同时绑定旧529/733节点、原真正 $L$ 自同构、五个旧分母和 source SHA；
表达式消费者不预称已有41值。
数值阶段需携整个原四响应误差证明、实际分母赋值和 SP 完整尾界。
一个确切矩阵残差没有逆算子赋值界时，不能单独充当41响应精度证明。
所有数值和机器证书只随一日 Actions artifact 保存；Git 只存源码、参数、证明与简明来源登记。

本篇的证明只作纸面代数、原形式恒等式和真实已成来源的推导；
没有执行新的点值、矩阵或周期算术。
