# 原物理投影夹逼：同一增量支付测试差源的左误差、bare、flat 与负图

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本稿加强[物理 joined 递减投影稿](2026-11-14-physical-joined-decreasing-projections-and-fixed-test-bare-budget-789f-next.md)：同一个原固定测试产生的差源
\[
e_q=u_q^{\rm b}-u_q^{\rm f}
\]
满足真正的逐切口预算
\[
\boxed{\mu_q(t_q-e_q)^2+\tfrac12\Xi_q(e_q)^2
\le \Delta_q(f),}
\]
其中 \(\Delta_q(f)\) 正是原左投影下降与完整有限核投影上升的同一增量；全切口和至多 \(d\|f\|^2\)，步长 \(d\) 的网格和至多 \(\|f\|^2\)。差源自动属于原首头负图，并可沿已付联合旗作原两费用正交消元。主左配对仍未获得温和比较；本文不宣称 \(N=M\)。

以下不改变任何原测试、原 \(t_q\)、原源度量或可行旗。先前稿中“尚未支付 \(\mu(t-u^{\rm b})\)”由本稿 §2 的夹逼补齐；先前的较弱 Fourier 预算仍成立，但本稿不需要它。

## 1. 三个真正物理投影

固定原 \(A=A_m,D=D_m,d=2^m\)，置 \(C=A+D\)、\(\mathcal K=\ker C\)，使用原全部物理头和平方自由尾孔空间。原 \(b\in\ell^1\) 保证 \(C\) 有界。记
\[
\mathcal K_q=\mathcal K\cap\mathcal H_{\le q},\qquad
\mathcal W_q=\ker(P_{<q}C).
\]
由于 \(D\) 降一孔、\(A\) 保孔，
\[
\boxed{\mathcal W_q=V_q\oplus^\perp\mathcal H_{>q}.}
\tag{1.1}
\]
这里 \(V_q=\{v\in\mathcal H_{\le q}:P_{<q}Cv=0\}\) 恰是原完整左空间。其原逐头短核旗由左方程及上三角 \(A\) 自动保持，未另扩大左输入。

\(\mathcal W_q\) 是递减闭空间，\(\mathcal K_q\) 递增，且
\[
\mathcal K_q\subset\mathcal K\subset\mathcal W_q.
\]
沿前稿设
\[
\mathcal H_{{\rm hi},q}
=\mathbb C^d\otimes\bigoplus_{p\ge q+2}
(\ker D^{p-q-1}\cap\mathcal H_p),
\]
\[
\mathcal M_q=\mathcal K+\mathcal H_{{\rm hi},q}
=\ker(Q_qC),\qquad Q_q=P_{\mathcal H_{{\rm hi},q}^{\perp}}.
\]
代数和已闭、商核的首头提升以及最小代表支撑 \(\le q+d\) 均由前稿 §2 证明。因高旗在孔层 \(<q\) 为零，
\[
\boxed{\mathcal K_{q+d}\subset\mathcal M_q\subset\mathcal W_q.}
\tag{1.2}
\]

固定物理测试 \(f\in\mathcal H_{\le s}\)，以下 \(q\ge s\)。记
\[
q_q=P_{\mathcal W_q}f=P_{V_q}f,\qquad
k_q=P_{\mathcal K_q}f,\qquad z_q=P_{\mathcal M_q}f.
\tag{1.3}
\]
\(z_q\) 的高旗分量为零，支撑至多 \(q+d\)，故它正是原 joined left+bare Riesz 向量。

保留原源 \(t_q=E_qq_q\)，原左最小逆 \(U_q=E_q^\dagger\)，以及同一个原源上的
\[
L_q=U_q^*U_q,\quad B_q=\mathcal A_q^*\mathcal A_q,\quad
G_q^{-1}=(\mathcal C_q^{\min})^*\mathcal C_q^{\min}.
\]
\(\mathcal A_q\) 是真正 bare 最小链，\(\mathcal C_q^{\min}\) 是真正完整右最小链，\(\Xi_q^2=\alpha_q^2+\lambda_{{\rm flat},q}^2\)。

全部 Riesz 身份是
\[
q_q=(k_q+U_qt_q,0),
\]
\[
z_q=(k_q+U_qu_q^{\rm b},-\mathcal A_qu_q^{\rm b}),
\qquad u_q^{\rm b}=(L_q+B_q)^{-1}L_qt_q,
\]
\[
k_{q+d}=(k_q+U_qu_q^{\rm f},-\mathcal C_q^{\min}u_q^{\rm f}),
\qquad u_q^{\rm f}=(L_q+G_q^{-1})^{-1}L_qt_q.
\tag{1.4}
\]
左右分块分别指物理孔层 \(\le q\) 与 \(>q\)。

## 2. 原左投影跨 \(d\) 层确实进入 joined 空间

对任意 \(v\in V_{q+d}\)，左方程给
\[
Dv_p=-Av_{p-1}\qquad(1\le p\le q+d).
\]
\(Cv\) 只可能在顶层 \(q+d\) 非零，其值为 \(Av_{q+d}\)。由于 \(A,D\) 交换，
\[
D^{d-1}Av_{q+d}
=(-1)^{d-1}A^dv_{q+1}=0.
\]
因此该顶输出属于高旗在 \(q+d\) 的真正分量
\(E_{d-1}^{(q+d)}\)，从而
\[
\boxed{V_{q+d}\subset\mathcal M_q,\qquad
q_{q+d}\in\mathcal M_q.}
\tag{2.1}
\]
这里没有声称整个 \(\mathcal W_{q+d}\subset\mathcal M_q\)：\(\mathcal W_{q+d}\) 中任意的更高孔部分未受这些短核旗限制。

由 (1.2)，
\[
x_q:=q_q-z_q\perp\mathcal M_q,\qquad
\|x_q\|^2=\|q_q\|^2-\|z_q\|^2.
\]
而 (2.1) 与两个真正投影给
\(\langle z_q,q_{q+d}\rangle=\|q_{q+d}\|^2\)，故
\[
\boxed{
\|x_q\|^2\le
\|q_q\|^2-\|q_{q+d}\|^2
=\|q_q-q_{q+d}\|^2.}
\tag{2.2}
\]
代入 (1.4) 得到此前未付的左误差：
\[
\boxed{
\mu_q(t_q-u_q^{\rm b})^2+\alpha_q(u_q^{\rm b})^2
\le\|q_q-q_{q+d}\|^2.}
\tag{2.3}
\]
这是实际投影夹逼，不是一般的 \(L\) 与 \(B\) 比较。

## 3. 两个正交增量及完整正配对

置
\[
y_q=k_{q+d}-k_q,\qquad
e_q=u_q^{\rm b}-u_q^{\rm f},\qquad
h_q=\mathcal A_qu_q^{\rm b}
       -\mathcal C_q^{\min}u_q^{\rm f}.
\tag{3.1}
\]
因为 \(y_q\in\mathcal K_{q+d}\subset\mathcal M_q\)，有 \(x_q\perp y_q\)。由 (1.4)，
\[
x_q+y_q=(U_q(t_q-e_q),h_q).
\]
故完整 Pythagoras 给
\[
\boxed{
\mu_q(t_q-e_q)^2+\|h_q\|^2
=\|x_q\|^2+\|y_q\|^2
\le\Delta_q(f),}
\tag{3.2}
\]
其中
\[
\Delta_q(f)=\|q_q-q_{q+d}\|^2
             +\|k_{q+d}-k_q\|^2.
\tag{3.3}
\]
特别
\[
\alpha_q(u_q^{\rm b})^2+\lambda_q(u_q^{\rm f})^2
\le\|x_q\|^2+\|y_q\|^2\le\Delta_q(f).
\tag{3.4}
\]

另定义两个真正的正交 gap 投影
\[
\mathsf R_q=P_{\mathcal W_q}-P_{\mathcal K_q},\qquad
\mathsf G_q=P_{\mathcal M_q}-P_{\mathcal K_{q+d}}.
\]
(1.2) 给 \(\operatorname{Ran}\mathsf G_q\subset
\operatorname{Ran}\mathsf R_q\)，并且
\[
\mathsf R_q-\mathsf G_q
=(P_{\mathcal W_q}-P_{\mathcal M_q})
 +(P_{\mathcal K_{q+d}}-P_{\mathcal K_q})
\]
是两正交投影之和。它在 \(f\) 上的值为 \(x_q+y_q\)，而
\[
\mathsf G_qf=z_q-k_{q+d}=(U_qe_q,-h_q).
\]
因此两向量正交，得到真正同源正配对
\[
\boxed{\langle L_qe_q,t_q-e_q\rangle=\|h_q\|^2\ge0,}
\tag{3.5}
\]
以及
\[
\boxed{
\mu_q(t_q)^2
=\mu_q(e_q)^2+\mu_q(t_q-e_q)^2+2\|h_q\|^2.}
\tag{3.6}
\]
这保留主 \(\mu_q(e_q)\)，没有将它改称已付增量。

## 4. 同一个未来差的 bare 与 flat 两个真投影

所有右空间放在同一个原物理未来直和。记 \(P_{\rm f}\) 为完整右核的正交投影，\(P_{\rm b,min}\) 为 bare 核中零源正交补的正交投影。

完整右链的低出生投影是同源 bare 可行链。因此对于完整最小链，
\[
P_{\rm b,min}\mathcal C_q^{\min}u
=\mathcal A_qu.
\]
于是
\[
\boxed{P_{\rm b,min}h_q=\mathcal A_qe_q.}
\tag{4.1}
\]
此处不能把整个低出生投影误认为 bare 最小者；第二次真实最小投影保留在 \(P_{\rm b,min}\) 中。

原源读出记为 \(F_{\rm b},F_{\rm f}\)。完整投影恒等
\(P_{\rm f}F_{\rm b}^*=F_{\rm f}^*\)，结合 (1.4) 的两个源正规方程，给
\[
L_qe_q=G_q^{-1}u_q^{\rm f}-B_qu_q^{\rm b},
\]
\[
\boxed{
P_{\rm f}h_q
=F_{\rm f}^*B_qu_q^{\rm b}
  -F_{\rm f}^*G_q^{-1}u_q^{\rm f}
=-F_{\rm f}^*L_qe_q.}
\tag{4.2}
\]
右边准确是原 flat 链，未以普通右最小费替代。

两个正交投影各自收缩，所以
\[
\Xi_q(e_q)^2
=\|P_{\rm b,min}h_q\|^2+\|P_{\rm f}h_q\|^2
\le2\|h_q\|^2.
\]
与 (3.2) 合并，得到
\[
\boxed{
\mu_q(t_q-e_q)^2+\tfrac12\Xi_q(e_q)^2
\le\Delta_q(f).}
\tag{4.3}
\]
不假设这两个投影互相正交。

对任意同切口原源 \(r\)，同一个 \(t_q\) 的精确配对误差仍为
\[
\langle L_qr,t_q-e_q\rangle
=\langle B_qr,u_q^{\rm b}\rangle
 +\langle L_qr,u_q^{\rm f}\rangle.
\]
原 bare 与 flat／ordinary Cauchy 联同 (3.4) 给
\[
\boxed{
|\langle L_qr,t_q-e_q\rangle|
\le\Xi_q(r)\sqrt{\Delta_q(f)}.}
\tag{4.4}
\]
此外 (4.3) 也给 \(\mu_q(r)\sqrt{\Delta_q(f)}\) 的另一合法上界。

## 5. 完全复用原投影增量与同窗总预算

\(\mathsf R_q=P_{\mathcal W_q}-P_{\mathcal K_q}\) 是递减正交投影。其跨 \(d\) 层差为
\[
\mathsf R_q-\mathsf R_{q+d}
=(P_{\mathcal W_q}-P_{\mathcal W_{q+d}})
 +(P_{\mathcal K_{q+d}}-P_{\mathcal K_q}).
\]
第一项的像正交于整个 \(\mathcal K\)，第二项的像属于 \(\mathcal K\)；两项正交。因此
\[
\boxed{\Delta_q(f)=
\langle f,(\mathsf R_q-\mathsf R_{q+d})f\rangle.}
\tag{5.1}
\]
这是原下降左投影和上升有限核投影的同一个真实增量，不增加一个新的独立好窗筛选条件。

对每条步长 \(d\) 的网格 \(q=q_0+\ell d\)、\(q_0\ge s\)，望远镜给
\[
\sum_{\ell\ge0}\Delta_{q_0+\ell d}(f)\le\|f\|^2.
\]
每个单步增量在全部切口中至多被计数 \(d\) 次，故
\[
\boxed{\sum_{q\ge s}\Delta_q(f)\le d\|f\|^2.}
\tag{5.2}
\]
由 (2.3)、(3.4)、(4.3)，同一网格同时有
\[
\sum\{\mu(t-u^{\rm b})^2+\alpha(u^{\rm b})^2\}
\le\|f\|^2,
\]
\[
\sum\{\alpha(u^{\rm b})^2+\lambda(u^{\rm f})^2\}
\le\|f\|^2,
\]
\[
\boxed{\sum\{\mu(t-e)^2+\tfrac12\Xi(e)^2\}\le\|f\|^2.}
\tag{5.3}
\]
全切口版本的右边均为 \(d\|f\|^2\)。
以上对同一固定有限维测试空间是二次型不等式，故可直接对一组正交测试取迹，与原算子好窗条件共同使用。
没有 \(C_m\)、Jordan 相似条件数、额外 \(\log d\) 或另一个未知锚速率。

## 6. 差源自动在真正首头负图

令 \(P\) 为第零物理源头的原正交投影，\(S_q=L_q+B_q\)。已有
[首源头两右度量分裂](../results/R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md) §§1–2 证明
\[
[P,B_q]=[P,G_q]=0,\qquad
P(G_q^{-1}-B_q)=0.
\tag{6.1}
\]
它针对整个第零源头 \(e_0E_{d-1,q}\)，不只针对 primitive 输入。
同源 (1.4) 给
\[
S_qe_q=(G_q^{-1}-B_q)u_q^{\rm f},
\]
故
\[
\boxed{P S_qe_q=0,\qquad
e_q\in\mathscr N_q=\operatorname{Ran}T_{q+1}.}
\tag{6.2}
\]
最后的准确源流像等式见
[真正负源图和联合已付旗](../results/R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md) §1。

(6.2) 仅涉及第零物理源头；没有把它自动升级为前 \(K\) 个源头的负图条件。

在原合法参数中，沿该稿 §§3–4 取
\(\mathscr Z_q=\mathscr N_q\cap\mathscr X_q\)，并作真正两费用投影
\[
s_q=P_{\mathscr Z_q}^{\mathfrak M_q}e_q,\qquad
\widehat e_q=e_q-s_q,\qquad
\mathfrak M_q=B_q+L_qG_qL_q.
\]
已付结论原样给
\[
\widehat e_q\in\mathscr R_{{\rm rem},q},\qquad
\Xi_q(\widehat e_q)\le\Xi_q(e_q),\qquad
\mu_q(s_q)\le\delta_m\Xi_q(e_q).
\]
因此 (4.3) 的二维 Cauchy 形式给
\[
\boxed{
\mu_q(t_q-\widehat e_q)^2
\le(1+2\delta_m^2)\Delta_q(f),\qquad
\Xi_q(\widehat e_q)^2\le2\Delta_q(f).}
\tag{6.3}
\]
对任意实际剩余负图源 \(\widehat r_q\)，完整配对为
\[
\langle L_q\widehat r_q,t_q\rangle
=\langle L_q\widehat r_q,\widehat e_q\rangle+\mathcal E_q,
\]
\[
\boxed{
|\mathcal E_q|
\le
\{\Xi_q(\widehat r_q)
  +\sqrt2\,\delta_m\mu_q(\widehat r_q)\}
\sqrt{\Delta_q(f)}.}
\tag{6.4}
\]
双方确实属于同一个真实负图余空间，原固定测试功能被已付误差保持。
\(\mathfrak M_q\) 正交不能替代 \(L_q\) 正交；本文不因此删除主配对。

## 7. 已缩窄的缺口

当前已经同时支付：

- 原固定测试 \(f\) 与原 \(t_q\) 的身份；
- 真实 joined／完整投影差源及其 bare、flat 两费；
- 该差源与原 \(t_q\) 的左费误差；
- 首头负图条件及已付联合旗的真实两费用消元；
- 上述所有量的同一原投影增量预算。

仍欠的是 (6.4) 中
\(\langle L_q\widehat r_q,\widehat e_q\rangle\)
在原移动 \(m,q\) 窗口上的比较。两源的两费小没有被提升为该左配对小。
(3.5) 的正配对也只控制被减去的误差，不控制主
\(\mu_q(e_q)\)。固定 \(m\) 的强极限不能替代原合法窗口的联合速率。
