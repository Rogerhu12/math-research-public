# R239 附录：退化有限头的完整负源流与同一模型顶部的合法窗预算

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文完整刻画任意严格降头有限 nilpotent 头的真正左源流像，保留全部核头及其天然短核旗。共同的裸/完整右最小链给出正确的裸度量归一负图；不要求这些核头在物理源内积中约化两个右 Gram。最后从一个原顶部最小者出发，只运输一次天然四块模型顶部，再由它的全部前缀得到进入模型完整负图的实际子窗族及累计两费用。所需余比较仍未证明；普通 ISP 与无权 $N=M$ 仍为 OPEN。

依赖：[原左最小者截断](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)、[原实际顶部与全部窗预算](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)、[四块天然零源旗运输](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md)、[正 resolvent 缺陷校正](R239-appendix-positive-resolvent-negative-source-defect-correction.md)。本文在退化模型中重做完整源流证明，不把 regular 原头的单首头结论直接外推。

## 1. 退化有限头的天然顶输入旗与源空间

暂取任意严格降头 $T$ 作用于物理头 $\mathbb C^d$，所以 $T^d=0$。尾为同一个 $D_m$，以下固定孔数 $q\ge d$。定义
$$
V_{T,q}=\mathcal H_{\le q}\cap
\ker[P_{\le q-1}(T+D)],\qquad
E_{T,q}v=T v_q.
\tag{1.1}
$$

只为准确描述空间，选一个有限维相似
$$
T=S_J\left(\bigoplus_{\beta}J_{\ell_\beta}\right)S_J^{-1}.
$$
没有把 $S_J$ 当成等距，也不会使用未经支付的相似范数估计。令
$E_{k,q}=\ker D^k\cap\mathcal H_q$，其中 $E_{0,q}=\{0\}$。真正天然顶输入旗与源空间为
$$
\boxed{
\mathscr X_{T,q}
=S_J\!\left[
\bigoplus_{\beta}\bigoplus_{i=0}^{\ell_\beta-1}
e_{\beta,i}\otimes E_{\ell_\beta-i,q}\right],
}
\tag{1.2}
$$
$$
\boxed{
\mathscr R_{T,q}
=S_J\!\left[
\bigoplus_{\beta}\bigoplus_{i=0}^{\ell_\beta-1}
e_{\beta,i}\otimes E_{\ell_\beta-i-1,q}\right].
}
\tag{1.3}
$$
这些空间及定义都与选择的 Jordan 相似无关；它们分别是 $V_{T,q}$ 的真实顶层像和 $E_{T,q}$ 的真实源像。

说明 (1.2)–(1.3)。在单个 Jordan 串中，低输出方程反复给
$D^k(v_q)_i=(-1)^k(J^kv_{q-k})_i$，故
$D^{\ell-i}(v_q)_i=0$。反向给定具有这些短核阶的顶向量 $x$，下方各层可选
$(-1)^j(J^*)^jD^jx$；短核条件恰使每次 $JJ^*$ 的端点合法，最后自动终止。变回 $S_J$ 即得 (1.2)。对其施加 $T$ 就给 (1.3)，且满射。固定参数下的这些显式有限原像有界，所以 $E_{T,q}$ 有有界最小逆。

记同一个完整尾层 MP 逆为
$$
R_q=(D:\mathcal H_{q+1}\to\mathcal H_q)^\dagger.
$$
尾删除在固定孔层满射，故 $DR_q=I$；并且
$R_qE_{k,q}\subseteq E_{k+1,q+1}$。由于它只作用于尾并与 $S_J$ 交换，
$$
\boxed{
D:\mathscr X_{T,q+1}\to\mathscr R_{T,q}
\ \text{满射},\qquad
D^\dagger|_{\mathscr R_{T,q}}=R_q|_{\mathscr R_{T,q}}.
}
\tag{1.4}
$$
这里右端已经属于天然顶输入旗，且正交于全部 primitive，故也是受限映射的真正 MP 逆。没有采用顺次幂逆。

一般零源核仍准确为
$\ker E_{T,q}=\ker(T+D)\cap\mathcal H_{\le q}$。它们随 $q$ 嵌套，因此每个较低截断仍为同一顶部最小者诱导源的真正最小者；此事实不要求第一上对角非零。

## 2. 全部核头的共同单段右最小者

在天然源空间上定义闭子空间
$$
\boxed{\mathscr S_{0,q}=\ker T\cap\mathscr R_{T,q}.}
\tag{2.1}
$$
由 (1.2)–(1.4)，
$$
D(\ker T\cap\mathscr X_{T,q+1})=\mathscr S_{0,q},
\qquad
R_q\mathscr S_{0,q}\subseteq\ker T.
\tag{2.2}
$$

使用原物理宽度 $d$ 的完整右旗与低出生裸旗，并只将源限制到天然空间 $\mathscr R_{T,q}$。它们的真正右度量记为 $G_q^{-1}$、$B_q$；左度量为 $L_q=(E_{T,q}E_{T,q}^*)^{-1}$。

相应费用始终为 $\mu(r)^2=\langle L_qr,r\rangle$、
$\alpha(r)^2=\langle B_qr,r\rangle$、
$\lambda(r)^2=\langle G_q^{-1}r,r\rangle$，以及
$\chi(r)^2=\langle B_qr,r\rangle+\langle G_qL_qr,L_qr\rangle$。

对 $s\in\mathscr S_{0,q}$，单段链
$$
c_s=(R_qs,0,\ldots,0)
\tag{2.3}
$$
是合法完整右链：$DR_qs=s$，$TR_qs=R_qTs=0$。其物理第一段短核旗合法，是因为任何严格降头 $T$ 的天然源包含在原最大源旗
$\bigoplus_i e_iE_{d-i-1,q}$ 内；施加 $R_q$ 恰把每项核阶提高一。该包含也可从 primitive Taylor 源表示中直接看到：第 $t$ 项的头不超过 $d-t-2$，尾核阶不超过 $t+1$。

任意同源完整或裸可行链的第一段与 $R_qs$ 相差一个 $D$ 核，故 (2.3) 同时是两种真正最小者。定义源上的实际压缩
$$
K_q^{\rm tail}
=P_{\mathscr R_{T,q}}\,(I\otimes R_q^*R_q)|_{\mathscr R_{T,q}}.
$$
对任意 $r\in\mathscr R_{T,q}$，其可行第一段都经 $D$ 映到 $r$，所以
$$
\boxed{K_q^{\rm tail}\preceq B_q\preceq G_q^{-1}.}
\tag{2.4}
$$
与 (2.3) 作交叉内积还给更强的向量身份
$$
\boxed{B_qs=G_q^{-1}s=K_q^{\rm tail}s
\quad(s\in\mathscr S_{0,q}).}
\tag{2.5}
$$
例如对裸最小者 $a_b(r)$，
$\langle c_s,a_b(r)\rangle=\langle R_qs,R_qr\rangle$，完整最小者同理。

(2.5) 不声称 $\mathscr S_{0,q}$ 约化 $B_q$、$G_q$ 或 $K_q^{\rm tail}$。非正交的核头和不同的尾短旗仍可使这些算子具有真实交叉块。

## 3. 真正完整左源流的准确像

对一个上层真正最小者 $w=E_{T,q+1}^\dagger r_{\rm up}$，令
$$
r=-Dw_{q+1}=T w_q.
$$
同源截断说明 $P_{\le q}w=E_{T,q}^\dagger r$。定义此实际源流为
$\mathcal T_{q+1}r_{\rm up}=r$。则
$$
\boxed{
\operatorname{Ran}\mathcal T_{q+1}
=\mathscr N_{T,q}
:=\{r\in\mathscr R_{T,q}:
\langle(L_q+B_q)r,s\rangle=0
\ \forall s\in\mathscr S_{0,q}\}.
}
\tag{3.1}
$$

先证明必要性。由 (1.4)，上层向量唯一写成
$$
w_{q+1}=-R_qr+g,\qquad
g\in\mathbb C^d\otimes K_{q+1}.
$$
上层 pure primitive 零源核是 $\ker T\otimes K_{q+1}$；真正最小性迫
$$
g\in(\ker T)^\perp\otimes K_{q+1}.
\tag{3.2}
$$
对任意 $s\in\mathscr S_{0,q}$，由 (2.2)，拼合
$$
z=E_{T,q}^\dagger(-s)\ \oplus\ R_qs
$$
是支持于 $\le q+1$ 的真零源核。与 $w$ 配对，primitive 部分正交消去，得到
$$
0=-\langle L_qr,s\rangle-\langle R_qr,R_qs\rangle
=-\langle(L_q+B_q)r,s\rangle,
$$
最后一步使用 (2.5)。这证明像包含于右端。

反向取满足 (3.1) 的 $r$ 和任意 (3.2) 的 $g$，令
$$
\boxed{
w=E_{T,q}^\dagger r\ \oplus\ (-R_qr+g),
\qquad
r_{\rm up}=-TR_qr+Tg.
}
\tag{3.3}
$$
它是源 $r_{\rm up}$ 的可行左向量。任意顶部为 $k$ 的上层零源核满足
$k\in\ker T\cap\mathscr X_{T,q+1}$。置 $s=Dk\in\mathscr S_{0,q}$，则
$k=R_qs+k_{\rm prim}$，其中 $k_{\rm prim}\in\ker T\otimes K_{q+1}$。
其低部分等于 $E_{T,q}^\dagger(-s)$ 加一个低零源核。与 (3.3) 配对，低零源核、primitive 和 nonprimitive 的交叉都正交消去，余下
$-\langle(L_q+B_q)r,s\rangle=0$。因此 (3.3) 是真正上层最小者，证明满射。

每条纤维准确由 (3.2)–(3.3) 参数化，且
$$
\boxed{
\mu_{T,q+1}(r_{\rm up})^2
=\mu_{T,q}(r)^2+\|R_qr\|^2+\|g\|^2.
}
\tag{3.4}
$$
有限头的非正交相似未用于此范数式；它只使用真实物理孔层以及尾 primitive 的正交性。

## 4. 裸度量归一的全部核头负图及其物理缺陷

省略 $q$ 下标，置
$$
u=B^{1/2}r,\qquad H=B^{-1/2}LB^{-1/2}\succeq0,
\qquad C=B^{1/2}GB^{1/2}\preceq I.
$$
定义
$$
\boxed{\mathscr W_0=B^{1/2}\mathscr S_0,\qquad
P_0=P_{\mathscr W_0}.}
\tag{4.1}
$$
由 (2.5)，$GBs=s$ 对 $s\in\mathscr S_0$ 成立，所以
$$
\boxed{C|_{\mathscr W_0}=I.}
\tag{4.2}
$$
因 $C$ 自伴，$\mathscr W_0$ 在这个归一空间中约化 $C$。这并不等于物理源核头约化原 $B,G$。

完整负图 (3.1) 在正确归一中就是
$$
\boxed{r\in\mathscr N_T
\ \Longleftrightarrow\
P_0(I+H)u=0.}
\tag{4.3}
$$
令
$$
\mathscr V_0=\{(R_qs,0,\ldots,0):s\in\mathscr S_0\}
$$
嵌入同一物理右带。映射
$$
W_0(B^{1/2}s)=(R_qs,0,\ldots,0)
$$
由 (2.5) 是 $\mathscr W_0$ 到 $\mathscr V_0$ 的等距同构。对原裸最小链 $a_b(r)$ 及原平坦链 $c^\flat(r)$，与每个 $s$ 配对分别得到
$$
\langle a_b(r),c_s\rangle=\langle Br,s\rangle,\qquad
\langle c^\flat(r),c_s\rangle=\langle Lr,s\rangle.
$$
故全部核头的实际缺陷正是
$$
\boxed{
P_{\mathscr V_0}(a_b(r)+c^\flat(r))
=W_0P_0(I+H)u.
}
\tag{4.4}
$$
它使用全裸最小链在共同单段空间中的投影，不以任意头坐标投影替代。

若 $d_0=P_0(I+H)u$，同一个正 resolvent
$$
t=B^{-1/2}(I+H)^{-1}d_0
$$
给出
$$
\boxed{
r-t\in\mathscr N_T,\qquad
\chi(t)^2+2\mu(t)^2\le\|d_0\|^2,\qquad
\mu(t)\le\tfrac12\|d_0\|.
}
\tag{4.5}
$$
证明逐字来自 $C\preceq I$ 和 $H(I+H)^{-2}\preceq I/4$；无需 $\mathscr S_0$ 约化两个右度量。若没有先支付 (4.4) 中全部物理缺陷，就不能把 (4.5) 当免费全核头归约。普通完整右费仍未由此控制。

## 5. 四块头的真实四个核头短旗

对本课题 $T=A_\square$、$h=d/4$，已有有限头代数给
$$
A_\square=S_J(J_{h+2}\oplus J_h\oplus J_{h-2}\oplus J_h)S_J^{-1}.
$$
这里仅用于精确识别空间，$S_J$ 不被当作等距。因此全部核头源空间为
$$
\boxed{
\mathscr S_{0,q}
=S_J\!\left[
e_{1,0}E_{h+1,q}\oplus
e_{2,0}E_{h-1,q}\oplus
e_{3,0}E_{h-3,q}\oplus
e_{4,0}E_{h-1,q}\right].
}
\tag{5.1}
$$
四个 head 方向及其不同尾核阶都保留。它包含先前物理首头的 $e_0E_{h+1,q}$，但一般不是四个物理头的正交直和。

模型完整源流像由 (3.1) 对整个 (5.1) 配对决定。先前模型“首头负图运输”只给其中物理 $e_0E_{h+1,q}$ 的条件；不能据此省去另外三个核头条件。本节则为所有实际模型前缀源自动提供完整像条件。

## 6. 单个模型顶部的全部真实子窗

令 $v_\square=E_{\square,q}^\dagger g$ 是任意一个天然模型顶部最小者。对每个 $s\le q$ 定义
$$
r_s=A_\square(v_\square)_s,\qquad
v_s=P_{\le s}v_\square.
$$
由嵌套零源核，
$$
\boxed{v_s=E_{\square,s}^\dagger r_s.}
\tag{6.1}
$$
若 $s+1\le q$，应用 (3.1) 于同一个更高前缀，准确有
$$
\boxed{r_s\in\mathscr N_{\square,s}}
\tag{6.2}
$$
——这次是包含全部四个模型核头条件的完整源流像。

若还 $s+d\le q$，取宽度 $d$ 的物理完整右测试，拼接其左最小者与右最小链得到支持 $\le s+d$ 的模型真零源核。它与 $v_\square$ 正交，所以与 R271 相同的完整测试证明给
$$
c_{\square,s}^\flat
=P_{f,\square,s}P_{[s+1,s+d]}v_\square.
\tag{6.3}
$$
物理低出生投影同样合法：$A_\square$ 严格降头，故全部逐头最大短核旗保持；高出生部分不产生低输出。因此
$$
a_{\square,s}(r_s)
=-P_{b,\square,s}P_{L,s}P_{[s+1,s+d]}v_\square.
\tag{6.4}
$$
这里没有将不等距的 Jordan 坐标用于右带投影。两个投影未被假设正交，正确合计为
$$
\boxed{
\chi_{\square,s}(r_s)^2
\le2\|P_{[s+1,s+d]}v_\square\|^2.
}
\tag{6.5}
$$
故对 $4d\le a\le b\le q-d$，
$$
\boxed{
\sum_{s=a}^{b}\chi_{\square,s}(r_s)^2
\le2d\|P_{[a+1,b+d]}v_\square\|^2.
}
\tag{6.6}
$$
整个族由这个同一模型顶部向量产生，不逐窗重选来源。

## 7. 从同一个原实际顶部只运输一次模型顶部

回到 $0\ne w\in W=M\ominus\overline{BM}$ 的假设缺陷来源。原实际顶部预算给
$$
Q=\lfloor e^{d^3/4}\rfloor,\qquad
u_A=E_{A,Q}^\dagger r_Q,\qquad
\|u_A-P_{\le Q}^{(m)}w\|\le\eta_m\|w\|,
$$
$$
\eta_m=e^{-74d^4}+e^{-75d^4}.
\tag{7.1}
$$
令
$$
q=Q-d,\qquad v=P_{\le q}^{(m)}u_A.
$$
它是同一原源流中真正的左最小者。由于 $q+d=Q$，原完整未来窗身份给
$$
\lambda_{{\rm flat},A,q}\le
\|P_{[q+1,Q]}^{(m)}u_A\|.
\tag{7.2}
$$

记总物理占据数为 $\mathcal N_{\rm tot}$，并置
$$
t_m=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|/\|w\|
\longrightarrow0.
$$
对所有 $s\ge4d$，旧尾孔数不超过总占据数，故
$\|P_{>s}^{(m)}w\|\le t_m\|w\|$。因此
$$
\lambda_{{\rm flat},A,q}\le(t_m+\eta_m)\|w\|,
\qquad \|v\|\le(1+\eta_m)\|w\|.
\tag{7.3}
$$

现在只在这个 $q$ 对 $v$ 作一次天然零源旗 Schur 及四块模型最小化，得到 $v_\square=E_{\square,q}^\dagger g$。用统一上界
$\rho_m=e^{-d^4/20}$，之前同源左运输给
$$
\|v-v_\square\|
\le\left[\rho_m(t_m+\eta_m)
+3\rho_m(1+\rho_m)(1+\eta_m)\right]\|w\|.
$$
定义
$$
\boxed{
\zeta_m=\eta_m+\rho_m(t_m+\eta_m)
+3\rho_m(1+\rho_m)(1+\eta_m)\longrightarrow0.
}
\tag{7.4}
$$
则
$$
\boxed{\|v_\square-P_{\le q}^{(m)}w\|
\le\zeta_m\|w\|.}
\tag{7.5}
$$
这里只使用一次顶部左运输及其同一个原平坦费用；没有把一个逐窗误差乘上指数多的窗数，也没有要求 $Q$ 顶部自身的平坦费用先有界。

## 8. 模型完整负图的实际窗口族与准确剩余门槛

令
$$
I_m^\square=\{4d,\ldots,Q-2d\},
\qquad |I_m^\square|=Q-6d+1.
$$
对每个 $s\in I_m^\square$，从上述同一个 $v_\square$ 取 (6.1) 的 $r_s$。它们满足全部模型核头负图条件 (6.2)，并有
$$
\boxed{
\mu_{\square,s}(r_s)\ge
\theta_m\|w\|,
\qquad
\theta_m=\sqrt{1-t_m^2}-\zeta_m\longrightarrow1,
}
\tag{8.1}
$$
$$
\boxed{
\sup_{s\in I_m^\square}
\|E_{\square,s}^\dagger r_s-w\|
\le(t_m+\zeta_m)\|w\|\longrightarrow0.
}
\tag{8.2}
$$
所有未来带都在模型顶部支持内。由 (6.6) 和 (7.5)，
$$
\boxed{
\sum_{s\in I_m^\square}\chi_{\square,s}(r_s)^2
\le2d(t_m+\zeta_m)^2\|w\|^2.
}
\tag{8.3}
$$

充分大 $m$ 时这些源非零。设
$$
C_{m,s}^{\square}(w)
=\frac{\mu_{\square,s}(r_s)^2}
{\chi_{\square,s}(r_s)^2}.
$$
则
$$
\boxed{
\frac1d\sum_{s\in I_m^\square}
\frac1{C_{m,s}^{\square}(w)}
\le\frac{2(t_m+\zeta_m)^2}{\theta_m^2}
\longrightarrow0.
}
\tag{8.4}
$$
因此只需在这个实际模型完整负图族上、沿无穷头子序列证明
$$
\sup_{s\in I_m^\square}C_{m,s}^{\square}(w)
=O(e^{d^3/4}/d),
\tag{8.5}
$$
便能排除该非零 $w$。这里只损失最顶部额外一个长度 $d$ 的窗，保留原三次指数窗数门槛。

本文没有证明 (8.5)。特别，通用四块 Jordan 条件数平方仍不够温和。新增的是：模型比较可以限定于同一个实际顶部产生的完整四核头负图来源，而不是任意天然模型源或仅满足一个首头条件的来源；全部左能量、两费用及窗数由同一个向量精确支付。另加源旗的 $\mathfrak M$ 正交条件没有被免费运输，也没有被换成坐标支撑消失。

