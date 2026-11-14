# R271 附录：原左源流的准确像、首头负图与最小向上延拓

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2116。

状态：**已证明。** 本文完整刻画[同源左截断稿](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)中一次向下源流的像和每条纤维。它们是原左最小前驱真正产生的源；无需先修改原源或支付运输误差。像由完整左度量与原首头右度量共同给出的负图确定。每条纤维还给准确最小向上延拓费，以及原头权下全部 primitive 自由量的累计能量。

此负图不同于[两费用消元稿](R239-appendix-paid-head-elimination-and-filtered-left-cross-tests.md)的 \(M=B+LGL\) 正交补。本文不将两者混同，也没有给中间带放大的统一上界。

## 1. 同一个原头和相邻两孔

固定原 \(m,d=2^m,A=A_m,D=D_m\)，取 \(p,p+1\) 均为原合法孔层。采用前稿的
\[
\mathscr R_p=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,p},\qquad
\mathscr X_{p+1}=\bigoplus_{i=0}^{d-1}e_iE_{d-i,p+1},
\quad E_{h,n}=\ker D^h\cap\mathcal H_n.
\tag{1.1}
\]
记 \(L_p=J_p^{-1}\) 为真正左最小源度量，\(X_{p+1}s\) 为源 \(s\) 的最小左前驱的第 \(p+1\) 层，
\[
T_{p+1}s=-D X_{p+1}s.
\tag{1.2}
\]
原完整左最小者的截断仍是真正最小者，所以 (1.2) 是同一个前驱诱导的下一源。

以下将首源头的等距嵌入记为
\[
\iota_0:E_{d-1,p}\longrightarrow\mathscr R_p,\qquad
P=\iota_0\iota_0^*,\quad Q=I-P.
\]
首头坐标写 \(r_0=\iota_0^*r\)，不把它与全源 \(r\) 混同。令
\[
R_p=(D:\mathcal H_{p+1}\to\mathcal H_p)^\dagger,\qquad
K_p=(R_p|_{E_{d-1,p}})^*R_p|_{E_{d-1,p}}.
\tag{1.3}
\]
这里 \(R_p\) 是整个孔层的真 MP 逆，不是顺次核旗逆。对 \(h\in E_{a,p}\)，
\[
D^{a+1}R_ph=D^ah=0,
\]
所以它保持所需的原短核旗。

记
\[
\mathcal D_{p+1}=D|_{\mathscr X_{p+1}}:
\mathscr X_{p+1}\longrightarrow\mathscr R_p.
\]
该算子满射，其真正 MP 逆恰为逐头的 \(R_p\)：
\[
\mathcal D_{p+1}^\dagger r
=\sum_{i=0}^{d-2}e_iR_pr_i,\qquad
\ker\mathcal D_{p+1}
=\bigoplus_{i=0}^{d-1}e_iK_{p+1}^{\rm prim},
\quad K_n^{\rm prim}=\ker D\cap\mathcal H_n.
\tag{1.4}
\]
原因是每个 \(R_pr_i\) 在正确的短核旗中且与整个 \(\ker D\) 正交；末头 \(e_{d-1}E_{1,p+1}\) 全在核内。

## 2. 一次真实源流的像是准确负图

定义闭子空间
\[
\boxed{\mathscr N_p
=\{r\in\mathscr R_p:\ \iota_0^*L_pr=-K_pr_0\}.}
\tag{2.1}
\]
则
\[
\boxed{\operatorname{Ran}T_{p+1}=\mathscr N_p.}
\tag{2.2}
\]
此外，如果 \(B_p=J_{b,p}^{-1}\) 是原裸源度量，[首头分裂稿](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)的
\([B_p,P]=0\)、\(B_p|_{P\mathscr R_p}=K_p\) 给等价式
\[
\boxed{\mathscr N_p=\ker\bigl[\iota_0^*(L_p+B_p)\bigr].}
\tag{2.3}
\]

先证必要性。若 \(r=T_{p+1}s\)，置 \(x=X_{p+1}s\)。前稿的真正顶层最小化为
\[
\min_{Ay=s}\left(\|y\|^2+\langle L_pDy,Dy\rangle\right),
\qquad x\in\mathscr X_{p+1},\quad Dx=-r.
\tag{2.4}
\]
全部可变方向准确为 \(e_0f\)，\(f\in E_{d,p+1}\)。其中 \(f\in K_{p+1}^{\rm prim}\) 时第二项不变，故最优 \(x_0\) 的 primitive 部分为零。结合 \(Dx_0=-r_0\)，得到
\[
x_0=-R_pr_0.
\tag{2.5}
\]
再沿 \(f=R_pz\)、\(z\in E_{d-1,p}\) 变分。由 \(Dx=-r\)，(2.4) 的一阶条件是
\[
0=-\langle K_pr_0,z\rangle-\langle\iota_0^*L_pr,z\rangle.
\]
所有 \(z\) 都允许，便得 (2.1)。

反之，若 \(r\in\mathscr N_p\)，取
\[
x=-\mathcal D_{p+1}^\dagger r,\qquad
s=Ax=-A\mathcal D_{p+1}^\dagger r.
\tag{2.6}
\]
这保留原联合旗，且 \(Dx=-r\)。每个首头变分唯一分解为
\[
f=R_pz+k,\qquad z\in E_{d-1,p},\quad k\in K_{p+1}^{\rm prim}.
\]
对 \(k\) 的一阶配对因 (1.4) 为零；对 \(R_pz\) 的配对正是
\(-\langle K_pr_0+\iota_0^*L_pr,z\rangle=0\)。故 \(x\) 满足 (2.4) 的完整 Euler 条件。其二次型含单位项，严格正，因而 \(x=X_{p+1}s\)。遂有 \(T_{p+1}s=r\)，证明 (2.2)。

特别，一次向下源流的像闭，并且
\[
\boxed{\mathcal U_pr:=-A\mathcal D_{p+1}^\dagger r,\qquad
T_{p+1}\mathcal U_p=I_{\mathscr N_p}}
\tag{2.7}
\]
给固定原参数下的明确有界右逆。这里没有给其参数一致范数。

## 3. 每条纤维的全部自由度和准确能量

令
\[
\mathscr P_{p+1}^+
=\bigoplus_{i=1}^{d-1}e_iK_{p+1}^{\rm prim}.
\tag{3.1}
\]
对任意 \(r\in\mathscr N_p\)，源流的完整纤维为
\[
\boxed{
T_{p+1}^{-1}\{r\}
=\{-A\mathcal D_{p+1}^\dagger r+Ag:\ g\in\mathscr P_{p+1}^+\}.
}
\tag{3.2}
\]
对应的真正最小顶向量和总费用恰为
\[
\boxed{
X_{p+1}s=-\mathcal D_{p+1}^\dagger r+g,\qquad
\mu_{p+1}(s)^2
=\mu_p(r)^2+\|\mathcal D_{p+1}^\dagger r\|^2+\|g\|^2.
}
\tag{3.3}
\]

证明：任何 \(Dx=-r\) 的 \(x\) 按 (1.4) 唯一写成
\(-\mathcal D^\dagger r+g\)，其中 \(g\in\ker\mathcal D\)。§2 的 primitive 首头变分准确迫 \(g_0=0\)，于是 \(g\in\mathscr P^+\)。反向加入任意这样的 \(g\) 都不改变 \(Dx\) 或任何首头 Euler 配对，仍是真正最小顶向量。\(A|_{e_0^\perp}\) 是原头同构，所以不同 \(g\) 给不同 \(s=Ax\)。前稿的正能量递推和 (1.4) 的正交性给 (3.3)。

因而 \(\mathcal U_pr\) 是纤维中使真正左费最小的唯一源，且
\[
\boxed{
\min_{T_{p+1}s=r}\mu_{p+1}(s)^2
=\mu_p(r)^2+\|\mathcal D_{p+1}^\dagger r\|^2.
}
\tag{3.4}
\]
注意这是在实际源流纤维内最小化 \(\mu_{p+1}\)，不是普通源范数的 MP 断言。

取 \(r=0\)，还得到完整核
\[
\boxed{
\ker T_{p+1}=A\mathscr P_{p+1}^+
=\bigoplus_{i=0}^{d-2}e_iK_{p+1}^{\rm prim}.
}
\tag{3.5}
\]
最后的等号使用同一个原 \(A|_{e_0^\perp}\)，没有换成等权 Jordan 模型。

## 4. 负图上的完整左 Schur 能量

按首头和其余源头将 \(L_p\) 写成 \((L_{ij})\)，并置
\[
N_0=K_p+L_{00}>0,\qquad
S_p^-=L_{11}-L_{10}N_0^{-1}L_{01}.
\tag{4.1}
\]
式 (2.1) 给准确图参数化
\[
r=\mathcal R_p^-x=(-N_0^{-1}L_{01}x,x),
\qquad x\in Q\mathscr R_p.
\tag{4.2}
\]
代回完整二次型而不删交叉，得到
\[
\boxed{
\langle L_pr,r\rangle+\langle K_pr_0,r_0\rangle
=\langle S_p^-x,x\rangle.
}
\tag{4.3}
\]
等价地，
\[
(\mathcal R_p^-)^*L_p\mathcal R_p^-
=S_p^--L_{10}N_0^{-1}K_pN_0^{-1}L_{01}.
\tag{4.4}
\]
式 (4.3) 的左边严格正，所以 \(S_p^-\) 的正性有真实能量含义；不能将它误认成未修正的 \(L_{11}\) 或通常仅消 \(L_{00}\) 的 Schur 补。

这也给最直接的首头配对：
\[
\boxed{\langle\iota_0^*L_pr,r_0\rangle
=-\|K_p^{1/2}r_0\|^2.}
\tag{4.5}
\]
它是实际延拓源的准确负号，不是一般源的符号假设。

## 5. 同源首头的 flat 与 bare 链准确相反

令 \(k_h\) 为原首头零返回链，其唯一非零段为 \(e_0R_ph\)，并记
\(\mathscr K_{0,p}=\{k_h:h\in E_{d-1,p}\}\)。沿首头分裂稿，裸最小链 \(a_p(r)\) 与平坦链 \(c_p^\flat=F_p^*L_pr\) 满足
\[
P_{\mathscr K_{0,p}}a_p(r)=k_{r_0},\qquad
P_{\mathscr K_{0,p}}c_p^\flat
=k_{K_p^{-1}\iota_0^*L_pr}.
\tag{5.1}
\]
第一式来自裸度量对首头的约化；第二式来自完整右 Gram 同一首头块为 \(K_p^{-1}\)。因此，对每个 \(r\in\mathscr N_p\)，
\[
\boxed{
P_{\mathscr K_{0,p}}c_p^\flat
=-P_{\mathscr K_{0,p}}a_p(r)=-k_{r_0}.
}
\tag{5.2}
\]
此处两个链保留同一个 \(r\)，没有投影后重选源。尤其
\[
\alpha_p(r)^2+\lambda_{{\rm flat},p}(r)^2
\ge2\langle K_pr_0,r_0\rangle.
\tag{5.3}
\]
式 (5.2) 只处理这一个真实首头子空间，未断言整个两条链互为相反数。

## 6. 同一原源族的 primitive 控制量及头权预算

固定 \(v=E_q^\dagger r_q\)，对合法 \(s\le p<q\) 取前稿的
\(r_p=Av_p\)。由真实截断最小性，每个 \(r_p\in\mathscr N_p\)。令
\[
g_{p+1}=P_{\ker D}v_{p+1}.
\]
则 §3 给
\[
\boxed{
g_{p+1}\in\mathscr P_{p+1}^+,\quad
v_{p+1}=-\mathcal D_{p+1}^\dagger r_p+g_{p+1},\quad
r_{p+1}=-A\mathcal D_{p+1}^\dagger r_p+Ag_{p+1}.
}
\tag{6.1}
\]
全部源是一个原 \(r_q\) 的后代；\(g_{p+1}\) 不是独立任意选取后即可仍保持所有下一层负图的自由数据。

定义真实源增量
\[
\tau_{p+1}
=r_{p+1}+A\mathcal D_{p+1}^\dagger r_p=Ag_{p+1}.
\]
它位于 (3.5) 的原 primitive 源空间。若
\(A_0=A|_{e_0^\perp}\)，则
\[
\boxed{
\sum_{p=s}^{q-1}\left[
\|\mathcal D_{p+1}^\dagger r_p\|^2+
\|A_0^{-1}\tau_{p+1}\|^2\right]
=\mu_q(r_q)^2-\mu_s(r_s)^2.
}
\tag{6.2}
\]
证明只是将 (3.3) 沿同一源族相加，并用 \(A_0^{-1}\tau=g\)。这样原 \(A\) 的全部头权保留在准确费用里，未把 \(A_0^{-1}\) 的条件数隐去。

更精确地，对任意一组两两正交的实际输入头投影 \(P_I\)，
\[
\boxed{
\sum_{p=s}^{q-1}\sum_I
\|P_IA_0^{-1}\tau_{p+1}\|^2
\le\mu_q(r_q)^2-\mu_s(r_s)^2.
}
\tag{6.3}
\]
若这些投影分解全部非零头，左边恰是 (6.2) 的 primitive 项。对头切口 \(H\)，上三角性还给
\[
P_{\ge H}\tau_{p+1}
=P_{\ge H}AP_{\ge H+1}g_{p+1},
\]
故有完全保原矩阵的估计
\[
\sum_{p=s}^{q-1}\|P_{\ge H}\tau_{p+1}\|^2
\le \|P_{\ge H}AP_{\ge H+1}\|^2
\bigl[\mu_q(r_q)^2-\mu_s(r_s)^2\bigr].
\tag{6.4}
\]
本文没有假定这个头块范数随 \(H\) 小；具体原头块必须按其真实权估计。

式 (6.2)–(6.4) 为后续中间自由坐标保留原源、原头权和累计能量。仍须控制含真尾逆的传播项
\(-A\mathcal D_{p+1}^\dagger r_p\)，并同时保持每个后续源的负图条件。单凭这些正预算不推出统一耗散率、全部中间带上界或 \(N=M\)。
