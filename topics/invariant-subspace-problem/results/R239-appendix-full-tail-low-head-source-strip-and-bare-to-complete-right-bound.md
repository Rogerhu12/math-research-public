# R239 附录：全尾低头源带的裸到完整右界及真实宽对角带支付

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文对原完整裸链证明一个真幂恒等式，并由此给出全尾低头源的完整右费上界。源只限制物理头位置，其尾核阶仍是原宽度 $d$ 的全部核阶；这严格区别于此前随小头宽度缩短尾阶的低三角源旗。前两物理头不支付任何头条件数，得到 $\lambda\le\sqrt{1+\nu^2}\alpha$；一般前 $K$ 头只支付一次小前缀 Jordan 条件数。其完整左费用通过同一原平坦配对控制。最后给出真实负图中的 $\mathfrak M$ 投影与多数窗口支付，不把余图条件改成坐标零。普通 ISP 与无权 $N=M$ 仍为 OPEN。

依赖：[原完整源与顺次链](R271-appendix-source-primitive-jets-and-sequential-right-chain.md)、[真正小头 Jordan 成本](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)、[既有短尾低三角](R239-appendix-growing-low-head-flags-bare-left-control-and-short-jet-filtering.md)、[原负源流与实际窗](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)。下文保留原完整域和物理度量。

## 1. 范围及这次真正加宽的源空间

固定原 $T_N$ 或 $T_Y$ 边界有限头 $A=A_m$、纯尾 $D=D_m$，以及
$$
m\ge5,\qquad d=2^m,\qquad 4d\le q\le e^{d^3/4},
\qquad \nu=\|D\|\le1/m<1.
$$
这里边界 $T_N=\sum_j(j+1)^{-2}\mathsf N_j$ 位于负边界表示；它不是原 Haar 空间中的另一个二次式 $X^2-B_0+Y$。

记 $E_{h,p}=\ker D^h\cap\mathcal H_p$。原完整源为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q}.
$$
对 $1\le K\le d$，定义完整尾阶的物理低头源带
$$
\boxed{
\mathscr X_{K,q}
=\mathscr R_q\cap
\left(\operatorname{span}\{e_0,\ldots,e_{K-1}\}\otimes\mathcal H_q\right)
=\bigoplus_{i=0}^{\min(K-1,d-2)}e_iE_{d-i-1,q}.
}
\tag{1.1}
$$
即使 $K\ll d$，首头尾阶仍是 $d-1$，不是 $K-1$。旧低三角
$\bigoplus_{i=0}^{K-2}e_iE_{K-i-1,q}$ 只是 (1.1) 的子空间。

原费用为
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,
$$
$$
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,
\qquad \chi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2.
\tag{1.2}
$$
其中裸和完整最小者始终在原整个 $d$ 头／$d$ 段空间中取，不预先禁止高头零源自由量。

## 2. 任意原裸链的真正幂约束

令 $a=(a_1,\ldots,a_d)$ 是任意源为 $r$ 的合法裸低链。则
$$
Da_1=r,
\qquad Aa_{j-1}+Da_j\in E_{j-2,q+j-1}
\quad(2\le j\le d),
\tag{2.1}
$$
每个尾核陈述逐头理解。第二式正是内部低输出为零，保留的高输出位于该核旗。

由 $A$ 与 $D$ 交换，归纳得
$$
\boxed{D^ja_j=(-A)^{j-1}r\quad(1\le j\le d).}
\tag{2.2}
$$
基步为首输出；从 $j-1$ 到 $j$ 时将 (2.1) 乘 $D^{j-1}$，其残差被准确杀掉，再用归纳假设即可。

令
$$
P_j^\perp=P_{(\ker D^j\cap\mathcal H_{q+j})^\perp},
\qquad
Q_j=(D^j:\mathcal H_{q+j}\to\mathcal H_q)^\dagger.
$$
$Q_j$ 是这个真幂的真正 MP 逆，固定参数下有界。式 (2.2) 给准确向量身份
$$
\boxed{Q_jA^{j-1}r=(-1)^{j-1}P_j^\perp a_j.}
\tag{2.3}
$$
特别，对真正裸最小链，
$$
\boxed{
\sum_{j=1}^{d}\|Q_jA^{j-1}r\|^2\le\alpha(r)^2.
}
\tag{2.4}
$$
这一步没有控制 $Q_j$ 的全层范数。整个真幂原像是裸链的实际正交投影，所以已经由同一个裸费用支付。

## 3. 小前缀的上三角 Jordan 化

设 $H_K=\operatorname{span}(e_0,\ldots,e_{K-1})$，$A^{[K]}=A|_{H_K}$。原严格降头矩阵的第一上对角均非零，因此存在上三角可逆矩阵 $S_K$ 满足
$$
A^{[K]}=S_KJ_KS_K^{-1},\qquad J_Ke_i=e_{i-1}\ (i\ge1).
\tag{3.1}
$$
例如选一个顶循环向量，按其逐次 $A$ 像排列链基，便得到上三角基矩阵；其对角非零。$S_K$ 和 $S_K^{-1}$ 都保持每个较低物理头旗。

记
$$
\kappa_K=\|S_K\|\,\|S_K^{-1}\|.
\tag{3.2}
$$
这里仅使用小前缀的相似，不用完整 $A_m$ 的巨大条件数。对 $K=2$，原 $Ae_1=e_0$，可直接取 $S_2=I$，故 $\kappa_2=1$；对 $K=1$ 同样成立。

若 $K=2^\ell$、$3\le\ell\le m$，原前缀准确是 $A_\ell$。既有真实无缩放 Jordan 稿给上三角 $S_K=V_\ell$，且
$$
\boxed{\kappa_K\le e^{221K^4/16}.}
\tag{3.3}
$$
无缩放 $J_K$ 已在 (3.1) 明列，因而没有漏付某个 Jordan 标量的负幂。

## 4. 对全部原尾核阶构造真正完整右链

固定任意 $r\in\mathscr X_{K,q}$，令
$$
r'=S_K^{-1}r=\sum_{i=0}^{K-1}e_ir'_i,
\qquad
u_i=Q_{i+1}r'_i.
\tag{4.1}
$$
若 $K=d$，$r'_{d-1}=0$，相应 $u_{d-1}=0$。因为 $S_K^{-1}$ 上三角，
$$
r'_i\in E_{d-i-1,q}.
\tag{4.2}
$$
于是 $D^{i+1}u_i=r'_i$，进一步有 $D^du_i=0$。定义 Jordan 坐标中的完整链
$$
\boxed{
c'_t=(-1)^{t-1}\sum_{i=t-1}^{K-1}
e_{i-t+1}D^{i+1-t}u_i
\quad(1\le t\le K),
\qquad c'_t=0\quad(t>K).
}
\tag{4.3}
$$

逐项核其原联合旗。第 $t$ 段位于孔层 $q+t$；项的头为 $j=i-t+1\le K-t\le d-t$，其尾满足
$$
D^{i+1-t}u_i\in E_{d-i-1+t,q+t}=E_{d-j,q+t}.
\tag{4.4}
$$
这正是原宽度 $d$ 的完整右旗。首输出和全部内部输出直接给
$$
Dc'_1=r',\qquad J_Kc'_t+Dc'_{t+1}=0,
\qquad J_Kc'_K=0.
\tag{4.5}
$$
因此
$$
\boxed{c_t=S_Kc'_t}
\tag{4.6}
$$
是一条真正原完整右链，源恰为 $r$。$S_K$ 只把头向更低位置混合，故 (4.4) 所需尾旗只会变宽，仍然合法。没有把 $S_K$ 当成等距。

## 5. 全尾低头源的裸到完整右界

不同 $i$ 在每个固定段 $t$ 落在不同物理 Jordan 头，故
$$
\begin{aligned}
\|c'\|^2
&=\sum_{i=0}^{K-1}\sum_{t=1}^{i+1}
\|D^{i+1-t}u_i\|^2\\
&\le\gamma_K(\nu)\sum_{i=0}^{K-1}\|u_i\|^2,
\qquad
\gamma_K(\nu)=\sum_{j=0}^{K-1}\nu^{2j}\le\frac1{1-\nu^2}.
\end{aligned}
\tag{5.1}
$$

另一方面，$u_i$ 是
$Q_{i+1}J_K^ir'=S_K^{-1}Q_{i+1}A^ir$
的第零头。每个 $A^ir$ 都仍在小前缀内，所以该同一个 $S_K^{-1}$ 合法适用。由 (2.4)，
$$
\boxed{
\sum_{i=0}^{K-1}\|u_i\|^2
\le\|S_K^{-1}\|^2
\sum_{j=1}^{K}\|Q_jA^{j-1}r\|^2
\le\|S_K^{-1}\|^2\alpha(r)^2.
}
\tag{5.2}
$$
真正完整最小者不贵于 (4.6)，从而
$$
\boxed{
\lambda(r)\le C_K\alpha(r)
\quad(r\in\mathscr X_{K,q}),
\qquad C_K=\kappa_K\sqrt{\gamma_K(\nu)}.
}
\tag{5.3}
$$
该常数与 $q$ 无关，对 (1.1) 中的全部非 primitive 尾核层成立。裸最小者可使用整个原高头空间；(2.3) 对它的全部分量有效，所以证明未把原裸费换成受限小头裸费。

特别，
$$
\boxed{
\lambda(r)\le\sqrt{1+\nu^2}\,\alpha(r)
\quad\left(r\in e_0E_{d-1,q}\oplus e_1E_{d-2,q}\right).
}
\tag{5.4}
$$
这是整个原首两源头，而不只是最浅尾层；没有原首两头外的长跳范数因子。

## 6. 同一个原平坦源支付完整左费

对任意原源，有准确的同源 Cauchy 配对
$$
\mu(r)^2=\langle G^{1/2}Lr,G^{-1/2}r\rangle
\le\lambda_{\rm flat}(r)\lambda(r).
$$
代入 (5.3)，得到
$$
\boxed{
\mu(r)^2\le C_K\alpha(r)\lambda_{\rm flat}(r)
\le\frac{C_K}{2}\chi(r)^2
\quad(r\in\mathscr X_{K,q}).
}
\tag{6.1}
$$
其中的 $G,L$ 都是原完整算子；从未以小前缀 Gram 替换 $G$，也没有由二次型近似反推平坦向量近似。

当 $K=2$，常数为 $\sqrt{1+\nu^2}/2$。一般 (6.1) 使用一次而非两次 $\kappa_K$，与此前直接左塔的裸费常数不同。

## 7. 完整 primitive 源坐标中的准确宽对角带

沿原源同构 $a=\Gamma_qr$，令
$$
\mathscr U_q=\bigoplus_{t=0}^{d-2}
H_{\ge t+1}\otimes K_{q-t},\qquad K_p=\ker D\cap\mathcal H_p.
$$
其准确源 jets 满足
$$
P_0D^tr=(-1)^tA^{t+1}a_t.
\tag{7.1}
$$
$A^{t+1}:H_{\ge t+1}\to H_{\le d-t-2}$ 的三角同构，按列头平移 $t+1$ 后是具有非零对角的上三角矩阵。因此
$$
\boxed{
\Gamma_q\mathscr X_{K,q}
=\bigoplus_{t=0}^{d-2}
\operatorname{span}\{e_{t+1},\ldots,e_{\min(t+K,d-1)}\}
\otimes K_{q-t}.
}
\tag{7.2}
$$
证明正向：物理源只在前 $K$ 头，所以每个 (7.1) 的输出只在
前 $\min(K,d-t-1)$ 头；上三角回代恰把它送进右端所列带。
反向：每个该带输入经 $A^{t+1}$ 只落在前 $K$ 头；原 Taylor 源公式的所有项因此都在 $\mathscr X_{K,q}$，尾核阶仍由原完整源旗保证。

当 $K=1$，(7.2) 是既有整条最小头对角。$K=2$ 已付其全深度宽二带；一般 $K$ 支付整条宽 $K$ 带，包含任意大 $t$，不是仅 $t\le K-2$ 的低三角。

## 8. 真正负图内的 M 投影

设 $\mathscr N_q=\ker P(L+B)$ 为原负源图，$P$ 是物理首源头投影，令
$$
\mathscr Z_{K,q}=\mathscr N_q\cap\mathscr X_{K,q},\qquad
\mathfrak M_q=B+LGL.
$$
固定参数下 $\mathfrak M_q$ 严格正且有界可逆。对 $r\in\mathscr N_q$，令 $z$ 为其到闭子空间 $\mathscr Z_{K,q}$ 的真实 $\mathfrak M_q$ 正交投影，$r'=r-z$。则
$$
\boxed{
r'\in\mathscr N_q,\qquad
\chi(r)^2=\chi(z)^2+\chi(r')^2,\qquad
\mu(z)^2\le(C_K/2)\chi(z)^2.
}
\tag{8.1}
$$
余源的准确条件是
$$
\langle\mathfrak M_qr',s\rangle=0
\quad(s\in\mathscr Z_{K,q}).
\tag{8.2}
$$
这不是 $r'$ 的低物理头为零，也不是 $\Gamma r'$ 在 (7.2) 中的坐标为零。

## 9. 增长宽带可在实际多数窗口同时支付

使用原实际顶部得到的共同窗口族。设
$$
Q=\lfloor e^{d^3/4}\rfloor,\qquad
I_m=\{4d,\ldots,Q-d\},\qquad n_m=|I_m|=Q-5d+1.
$$
对同一个假设缺陷 $0\ne w$，已有真正源 $r_q\in\mathscr N_q$、真正左向量
$v_q=E_q^\dagger r_q$，并有某个 $\beta_m\to0$ 满足
$$
\sup_{q\in I_m}\|v_q-w\|\le\beta_m\|w\|,
\qquad
\sum_{q\in I_m}\chi(r_q)^2\le2d\beta_m^2\|w\|^2.
\tag{9.1}
$$
例如可取既有实际尾量 $t_m$ 加顶部误差 $\eta_m$。

逐窗使用 §8 的投影 $z_q$。由 (8.1)，
$$
\sum_{q\in I_m}\mu(z_q)^2
\le C_Kd\beta_m^2\|w\|^2.
\tag{9.2}
$$
所以至少一半窗口组成集合 $J_m\subseteq I_m$，且对全部 $q\in J_m$，
$$
\mu(z_q)^2\le
\frac{2C_Kd}{n_m}\beta_m^2\|w\|^2.
\tag{9.3}
$$
令 $r'_q=r_q-z_q$，则该多数族仍在负源图内，并满足准确余图条件 (8.2)，以及
$$
\boxed{
\sup_{q\in J_m}\|E_q^\dagger r'_q-w\|
\le\left(1+\sqrt{\frac{2C_Kd}{n_m}}\right)
\beta_m\|w\|,
}
\tag{9.4}
$$
$$
\boxed{\sum_{q\in J_m}\chi(r'_q)^2
\le2d\beta_m^2\|w\|^2,\qquad |J_m|\ge n_m/2.}
\tag{9.5}
$$
这使用同一个旧顶部族的费用；新族不被宣称仍是逐孔相容源流。

当 $m\ge7$，取
$$
\ell_m=\lfloor3m/4\rfloor-2,\qquad K_m=2^{\ell_m},
\qquad \frac18d^{3/4}<K_m\le\frac14d^{3/4}.
$$
由 (3.3)、(5.1)，
$$
C_{K_m}\le
\frac{\exp(221d^3/4096)}{\sqrt{1-m^{-2}}}.
$$
又 $n_m\ge\tfrac12e^{d^3/4}$，所以
$$
\boxed{
\frac{C_{K_m}d}{n_m}
\le\frac{2d}{\sqrt{1-m^{-2}}}
\exp\!\left(-\frac{803}{4096}d^3\right)
\longrightarrow0.
}
\tag{9.6}
$$
因此可在保留至少一半合法窗口、同一强极限 $w$ 及原累计两费用上界（除以 $d$ 后趋零）的同时，删除这条全深度增长宽带在原负图中的真实 $\mathfrak M_q$ 分量。不需要假定 $\beta_m$ 有任何额外下降速度。

## 10. 未闭的实际余方向

本文的新支付范围是 (1.1)、(7.2) 的整个全尾低头源带，而不是小尾阶三角。其余源仍满足真实度量余图 (8.2)；不能据此断言其物理源前 $K_m$ 头或 primitive 带坐标消失。

尚需把这里的有费宽带与已付模型源旗、深层旗及实际两下降余源共同处理，控制剩余完整左费用。本文没有为一般高头源给出温和的 $\lambda/\alpha$ 界，也没有证明原 $N=M$ 或普通 ISP。
