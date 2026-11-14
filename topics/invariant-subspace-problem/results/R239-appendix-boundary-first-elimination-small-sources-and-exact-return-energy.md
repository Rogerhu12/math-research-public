# R239 附录：首段边界先消元、真实小源运输及准确返回能量

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c；AI 辅助：GPT-6 Astra Pro。
状态：已证明。以下等式与预算保持原联合旗、原窗口和原 Hilbert 范数；尚未给原末块能量的无权上界。

本稿继续 [真实返回源](../notes/2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md) 和 [嵌套出生旗的完整 Schur 缺陷](R271-appendix-nested-birth-flags-quotient-energy-and-complete-schur-defects.md)。新增的消元先满足首段边界方程：其首段源及低链最小源都由真实未来带控制，完整 $D_3$ 的源运输也有一个相同窗口内的廉价原像。最后证明新旧末块度量的差正好保留原返回费用，避免把新能量上界替代旧强制通量。

## 1. 同一个联合旗中的首段边界

固定
$$
m\ge5,\qquad d=2^m,\qquad 4d\le q\le e^{d^3/4}.
$$
沿用原 $A=A_m,D=D_m$ 和
$$
E_{h,p}=\ker D^h\cap\mathcal H_p^{\rm tail},\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
完整修复域、残量域和内部输出为
$$
\mathscr C_q=\bigoplus_{t=1}^d\mathscr C_{q,t},\qquad
\mathscr C_{q,t}=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t},
$$
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q},\qquad
\mathscr Y_q=\bigoplus_{t=1}^{d-1}
\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t}.
$$
定义
$$
F_qc=Dc_1,\qquad
S_qc=(Ac_t+Dc_{t+1})_{t=1}^{d-1}.
$$
本稿 $F_q$ 作用于整个 $\mathscr C_q$；后面将其限制到低链核时另写 $\mathsf F_q$。

[R271 同时右逆](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md) §2–3 已对 $(F_q,S_q)$ 的整个上述输出域构造右逆 $\mathcal Q_q$，范数
$$
\|\mathcal Q_q\|\le e^{d^4}.
\tag{1.1}
$$
特别，取首段源为零时，其构造有 $c_1=0$。所以
$$
S_q:\ker F_q\longrightarrow\mathscr Y_q
$$
满射，且有同样范数界的右逆。这不是只对实际残量的一次存在性声明。

记
$$
P_q=P_{\ker F_q},\qquad P_q^\perp=I-P_q.
$$
由 $F_q$ 只读取第一段，
$$
\ker F_q=
\left(\bigoplus_{i=0}^{d-1}e_iE_{1,q+1}\right)
\oplus\bigoplus_{t=2}^d\mathscr C_{q,t}.
\tag{1.2}
$$
因此 $P_q^\perp$ 只保留首段各头坐标的高度 $h\ge2$。此处所有投影都是原正交投影；没有把一个创建像投影与逆交换。

对 $r\in\mathscr R_q$，令
$$
b_q^\circ(r)=F_q^\dagger r.
$$
它只有第一段，且
$$
F_qb_q^\circ=r,\quad b_q^\circ\perp\ker F_q,\quad
\|b_q^\circ\|\le e^{d^4}\|r\|.
\tag{1.3}
$$
每个头坐标中的 $D^\dagger$ 自动保联合旗：若 $Dh=r_i$、$D^{d-i-1}r_i=0$，则 $D^{d-i}h=0$。

## 2. 边界先消元及同一个最优对偶

置
$$
\mathcal G_q^\circ=S_qP_qS_q^*.
\tag{2.1}
$$
由 (1.1)，
$$
\mathcal G_q^\circ\ge e^{-2d^4}I_{\mathscr Y_q}.
\tag{2.2}
$$
给定 $r$，记
$$
g_q^\circ=S_qb_q^\circ,\qquad
z_q^\circ=(\mathcal G_q^\circ)^{-1}g_q^\circ,
$$
$$
c_q=b_q^\circ-P_qS_q^*z_q^\circ.
\tag{2.3}
$$
则 $F_qc_q=r,S_qc_q=0$。对任意 $\delta\in\ker F_q\cap\ker S_q$，(2.3) 的两项都与 $\delta$ 正交，所以 $c_q$ 正是原完整最小修复，记
$$
\lambda_q(r)=\|c_q\|.
$$
正交性给
$$
\boxed{
\lambda_q(r)^2
=\|b_q^\circ(r)\|^2+
\langle\mathcal G_q^\circ z_q^\circ,z_q^\circ\rangle.
}
\tag{2.4}
$$

该 $z_q^\circ$ 等于旧最优对偶 $z_q$，不是替换了通量中的测试向量。确实，旧公式为
$$
c_q=b_q-S_q^*z_q,\qquad b_q\in\operatorname{Ran}F_q^*.
$$
将其投到 $\ker F_q$，并用 $P_q^\perp c_q=b_q^\circ(r)$，得到
$$
c_q=b_q^\circ-P_qS_q^*z_q.
$$
再施加 $S_q$，由 (2.2) 得 $z_q=z_q^\circ$。以下都写 $z_q$。

## 3. 出生层消元：准确的新末块与低链小源

按相对出生层 $a=t-h+1$ 写输入
$$
\mathscr C_q=\mathscr X_{L,q}\oplus\mathscr X_{H,q},
\quad
\mathscr X_{L,q}=\mathscr X_{\le0,q}\oplus\mathscr X_{1,q},
\quad
\mathscr X_{H,q}=\mathscr X_{\ge2,q},
$$
输出写
$$
\mathscr Y_q=\mathscr Y_{0,q}\oplus\mathscr Y_{1,q}\oplus\mathscr Y_{2,q},
$$
其中三项依次为 $a\le0,a=1,a\ge2$。首段没有高出生输入或输出。令
$$
S_{L,q}=P_{\mathscr Y_{0,q}\oplus\mathscr Y_{1,q}}
S_q|_{\mathscr X_{L,q}},\qquad Z_q=\ker S_{L,q},
$$
$$
S_{H,q}=S_q|_{\mathscr X_{H,q}},\qquad
A_{H,q}=S_{H,q}S_{H,q}^*>0,
$$
$$
B_q=P_{\mathscr Y_{2,q}}S_q|_{Z_q},\qquad
\mathsf F_q=F_q|_{Z_q},\qquad
\mathcal N_q=\ker\mathsf F_q.
\tag{3.1}
$$
这些是返回源笔记中的同一空间与算子。$S_{H,q}$ 的固定参数满射已由其 §1 的有限递推证明；$\mathsf F_q$ 满射，因为每个完整可行链的低分量属于 $Z_q$ 且具有相同首段残量。

令 $P_{\mathcal N_q}$ 是 $Z_q$ 内到 $\mathcal N_q$ 的正交投影，定义低链裸最小原像
$$
a_q(r)=\mathsf F_q^\dagger r.
\tag{3.2}
$$
由完整右逆取低分量，
$$
\|a_q(r)\|\le e^{d^4}\|r\|,\qquad
\|b_q^\circ(r)\|\le\|a_q(r)\|.
\tag{3.3}
$$

旧内部 Gram $\mathcal G_q=S_qS_q^*$ 的出生三块记为
$$
\mathcal G_q=
\begin{pmatrix}
B_{0,q}&V_{1,q}^*&0\\
V_{1,q}&B_{1,q}&V_{2,q}^*\\
0&V_{2,q}&B_{2,q}
\end{pmatrix}.
$$
由于 $S_qP_q^\perp$ 只有第一段输出、且高度至少2，$\mathcal G_q^\circ$ 仅改变其中第零个对角块：
$$
B_{0,q}^\circ
=B_{0,q}-S_qP_q^\perp S_q^*|_{\mathscr Y_{0,q}},
$$
其余 $V_1,V_2,B_1,B_2$ 完全保留。置
$$
Q_{1,q}^\circ=B_{1,q}-V_{1,q}(B_{0,q}^\circ)^{-1}V_{1,q}^*,
$$
$$
\boxed{
\mathcal H_{2,q}^\circ
=B_{2,q}-V_{2,q}(Q_{1,q}^\circ)^{-1}V_{2,q}^*.
}
\tag{3.4}
$$
所有这些逆均由 (2.2) 的正性保证；$B_0^\circ$ 不是旧 $B_0$。

$g_q^\circ$ 只有第零个出生块。定义
$$
\zeta_q^\circ=V_{1,q}(B_{0,q}^\circ)^{-1}g_q^\circ,\qquad
\sigma_q^\circ
=V_{2,q}(Q_{1,q}^\circ)^{-1}\zeta_q^\circ.
\tag{3.5}
$$
先消低块给
$$
z_{2,q}=(\mathcal H_{2,q}^\circ)^{-1}\sigma_q^\circ.
\tag{3.6}
$$

上述源还有更直接、保全全部投影的表达式：
$$
\boxed{
\mathcal H_{2,q}^\circ
=A_{H,q}+B_qP_{\mathcal N_q}B_q^*,
\qquad
\sigma_q^\circ(r)=B_qa_q(r).
}
\tag{3.7}
$$
证明：所有低链可行首段源写成 $a_q(r)+n$，$n\in\mathcal N_q$。高链补全要求
$$
B_qn+S_{H,q}c_H=-B_qa_q(r).
$$
因为 $a_q(r)\perp\mathcal N_q$，完整极小值就是这个方程在
$\mathcal N_q\oplus\mathscr X_{H,q}$ 中的极小值，再加 $\|a_q(r)\|^2$。其 Gram 正是 (3.7) 的第一式；最小链为
$$
c_L=a_q(r)-P_{\mathcal N_q}B_q^*z_{2,q},\qquad
c_H=-S_{H,q}^*z_{2,q}.
\tag{3.8}
$$
代入方程即得第二式。也可用 Schur 补的结合律将它与 (3.4) 逐项匹配。

记新三个 LDU 正能量为
$$
\mathcal E_{0,q}^\circ=\|g_q^\circ\|_{(B_{0,q}^\circ)^{-1}}^2,\qquad
\mathcal E_{1,q}^\circ=\|\zeta_q^\circ\|_{(Q_{1,q}^\circ)^{-1}}^2,\qquad
\mathcal E_{2,q}^\circ=\|\sigma_q^\circ\|_{(\mathcal H_{2,q}^\circ)^{-1}}^2.
$$
(2.4)、(3.8) 准确给
$$
\boxed{
\mathcal E_{2,q}^\circ
=\lambda_q(r)^2-\|a_q(r)\|^2,
\qquad
\mathcal E_{0,q}^\circ+\mathcal E_{1,q}^\circ
=\|a_q(r)\|^2-\|b_q^\circ(r)\|^2.
}
\tag{3.9}
$$
这里新末块能量至多为 $\lambda^2$；它尚未被认成旧通量使用的末块能量。

## 4. 真正未来带支付整个低链源

取 $w\in M=\ker T$，令
$$
v=P_{V_{m,q}}w,\qquad r=A v_q,\qquad
\widehat v=P_{V_{m,q+d}}w,\qquad \widehat r=A\widehat v_q.
$$
原低输出投影及 [R271 联合旗稿 §5](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md) 给
$$
\|v-P_{\le q}w\|,\ 
\|\widehat v-P_{\le q+d}w\|
\le\delta_m\|w\|,\qquad \delta_m=e^{-74d^4}.
\tag{4.1}
$$
引用稿 §5 已单独在原 $q\le e^{d^3/4}$ 下核对 $Q=q+d$ 的宽截断误差：其右逆参数以 $q+2d$ 估计，仍有 $\log(2+R)\le d^3$；这里没有把 $Q$ 偷换到原窗口假设中。对下一节的相邻层，同样使用已声明的 $q+1\le e^{d^3/4}$。

置
$$
u_t=P_{W_{d-t+1}}\widehat v_{q+t},\qquad
f_t=H_t\widehat v_{q+t}.
$$
原证明已经逐头支付
$$
u\in\mathscr C_q,\qquad
S_qu=-f,\quad f\in\mathscr Y_{2,q},\qquad
F_qu=-\widehat r.
\tag{4.2}
$$
最后一式直接来自第一段低输出方程；第一段的头投影是整个 $W_d$。

将 $u=u_L+u_H$ 分成出生低、高部分。因为 (4.2) 的内部输出没有低出生部分，
$$
u_L\in Z_q,\qquad \mathsf F_qu_L=-\widehat r.
$$
所以
$$
\|a_q(\widehat r)\|\le\|u_L\|
\le\beta_q(w)+\delta_m\|w\|,
\quad
\beta_q(w)=\|P_{[q+1,q+d]}^{(m)}w\|.
$$
又由 $\|A\|\le6$ 和 (4.1)，
$$
\|r-\widehat r\|\le12\delta_m\|w\|.
$$
结合 (3.3)，$d\ge32$ 给
$$
\boxed{
\|a_q(r_{m,q}(w))\|
\le \beta_q(w)+e^{-72d^4}\|w\|.
}
\tag{4.3}
$$
这个预算适用于整个 $M$，未使用 $w\perp N$。

同时只用第一段可得
$$
\boxed{
\|b_q^\circ(r_{m,q}(w))\|
\le\|P_{q+1}^{(m)}w\|+e^{-72d^4}\|w\|.
}
\tag{4.4}
$$
因此新前两块正能量被真实未来带的平方控制，且沿合法全整数头趋零：
$$
\mathcal E_{0,q}^\circ+\mathcal E_{1,q}^\circ
\le\bigl(\beta_q(w)+e^{-72d^4}\|w\|\bigr)^2.
\tag{4.5}
$$
这一步没有以旧 $\|b_q\|$ 替代最小修复范数。

## 5. 完整第三矩的准确源运输及廉价原像

现在相邻 $q,q+1$ 使用同一头，并要求
$$
q+1\le e^{d^3/4}.
$$
记完整第三矩
$$
C=D_{3,m},\qquad s_3=\sum_{j\ge m}(j+1)^{-6}\le(5m^5)^{-1}.
$$
它在输入、残量、输出上的逐段限制分别写
$C_{\mathscr C,q},C_{\mathscr R,q},C_{\mathscr Y,q}$。全部范数至多 $s_3$，且
$$
F_qC_{\mathscr C,q}=C_{\mathscr R,q}F_{q+1},\qquad
S_qC_{\mathscr C,q}=C_{\mathscr Y,q}S_{q+1}.
\tag{5.1}
$$
由于 $C$ 与 $D$ 交换，出生层不能下降。特别，$C$ 保高输入、高输出旗，也把 $\ker F_{q+1}$ 送入 $\ker F_q$。故新的内部 Gram 同样有真实收缩
$$
C_{\mathscr Y,q}^*(\mathcal G_q^\circ)^{-1}C_{\mathscr Y,q}
\le s_3^2(\mathcal G_{q+1}^\circ)^{-1}.
\tag{5.2}
$$
证明仅需将一个最小的 $\ker F_{q+1}$ 内部原像逐段乘 $C$；无需让 $P_q$ 与 $C$ 交换。将 (5.2) 限制到高输出，得到
$$
C_{22,q}^*(\mathcal H_{2,q}^\circ)^{-1}C_{22,q}
\le s_3^2(\mathcal H_{2,q+1}^\circ)^{-1},
\quad C_{22,q}=C_{\mathscr Y,q}|_{\mathscr Y_{2,q+1}}.
\tag{5.3}
$$

对 $a=a_{q+1}(r)\in Z_{q+1}$，写
$$
C_{\mathscr C,q}a=C_La+C_Ha
$$
为低、高输入分量。由 (5.1) 以及 $S_{q+1}a=B_{q+1}a$ 只有高输出，
$$
C_La\in Z_q,\qquad
\mathsf F_q C_La=C_{\mathscr R,q}r.
$$
因此准确的正交分解为
$$
C_La=a_q(C_{\mathscr R,q}r)+n,\qquad n\in\mathcal N_q.
\tag{5.4}
$$
再用 (5.1) 的高输出行和 (3.7)，得到
$$
\boxed{
\sigma_q^\circ(C_{\mathscr R,q}r)
-C_{22,q}\sigma_{q+1}^\circ(r)
=-B_qn-S_{H,q}C_Ha.
}
\tag{5.5}
$$
右边保留完整跨出生项。它具有同一旧窗口内、首段边界为零的明确原像
$$
-(n+C_Ha)\in\ker F_q,
$$
其低内部输出为零。$n$ 与 $C_Ha$ 在原范数中正交，故由 (5.4)
$$
\|n+C_Ha\|^2
=\|C_{\mathscr C,q}a\|^2-\|a_q(C_{\mathscr R,q}r)\|^2.
$$
以新 Schur 度量取最小值，严格得到
$$
\boxed{
\begin{aligned}
&\|\sigma_q^\circ(C_{\mathscr R,q}r)
-C_{22,q}\sigma_{q+1}^\circ(r)\|_{(\mathcal H_{2,q}^\circ)^{-1}}^2\\
&\quad\le s_3^2\|a_{q+1}(r)\|^2
-\|a_q(C_{\mathscr R,q}r)\|^2.
\end{aligned}
}
\tag{5.6}
$$
右端非负，因为 (5.4) 本身给低链裸最小原像的收缩。这里没有单独删掉 $C_{21}$，也没有交换任一 Schur 逆；所有缺陷合成成了实际输入 $n+C_Ha$。

### 5.1 首段源本身也闭于完整降孔

另一个直接核对是
$$
b_q^\circ(C_{\mathscr R,q}r)
=P_q^\perp C_{\mathscr C,q}b_{q+1}^\circ(r).
\tag{5.7}
$$
余项 $k=P_qC_{\mathscr C,q}b_{q+1}^\circ(r)$ 只有第一段 primitive 高度，且
$$
\|k\|^2
=\|C_{\mathscr C,q}b_{q+1}^\circ(r)\|^2
-\|b_q^\circ(C_{\mathscr R,q}r)\|^2.
$$
若按原三个输出出生块写完整 $C$，则
$$
C_{00}g_{q+1}^\circ(r)
=g_q^\circ(C_{\mathscr R,q}r),\qquad
C_{10}g_{q+1}^\circ(r)=S_qk,\qquad
C_{20}g_{q+1}^\circ(r)=0.
\tag{5.8}
$$
$k$ 只在首段且尾高度为1，所以 $S_qk$ 全部落在 $\mathscr Y_{1,q}$，(5.8) 的中式是完整输出等式。

这说明旧嵌套旗稿中尚未匹配的首段源，在当前消元中有准确匹配；其 primitive 项由真实 $b^\circ$ 支付。(5.6) 则直接合成所有低链校正，优于分别估计各个缺陷后相加。

## 6. 接到真正 $X_{3,m}w\in N$ 的相邻源

[实际尾理想](../notes/2026-11-13-actual-tail-ideal-defect-compression-and-preimage-distance-boundary.md) §2 已证
$$
X=X_{3,m}=\sum_{j\ge m}(j+1)^{-6}N_j,\qquad
XM\subset N,
$$
$$
\|X\|,\|C\|\le s_3,\qquad
\|X-C\|\le s_3e^{-770d^4}.
\tag{6.1}
$$
对 $w\in M$，$C$ 恰降低一个孔层，且 $C$ 与 $L=A+D$ 交换。用两个真实低投影的 (4.1)，有
$$
\|Cv_{m,q+1}(w)-v_{m,q}(Xw)\|
\le3s_3e^{-74d^4}\|w\|.
$$
其中三项分别是 $C$ 乘原低投影误差、$C-X$ 的实际 carry，以及 $Xw\in M$ 的低投影误差。取顶层再乘 $A$ 得
$$
\boxed{
\|C_{\mathscr R,q}r_{m,q+1}(w)-r_{m,q}(Xw)\|
\le18s_3e^{-74d^4}\|w\|.
}
\tag{6.2}
$$
由 (3.9) 和完整右逆，
$$
\|\sigma_q^\circ(h)\|_{(\mathcal H_{2,q}^\circ)^{-1}}
\le\lambda_q(h)\le e^{d^4}\|h\|.
$$
因此 (5.6)、(4.3)、(6.2) 给真正的相邻源运输
$$
\boxed{
\begin{aligned}
&\|\sigma_q^\circ(r_{m,q}(Xw))
-C_{22,q}\sigma_{q+1}^\circ(r_{m,q+1}(w))
\|_{(\mathcal H_{2,q}^\circ)^{-1}}\\
&\quad\le
s_3\bigl(\beta_{q+1}(w)+e^{-72d^4}\|w\|\bigr)
+18s_3e^{-73d^4}\|w\|.
\end{aligned}
}
\tag{6.3}
$$
这里 $\beta_{q+1}(w)=\|P_{[q+2,q+d+1]}^{(m)}w\|$，相邻窗口仍使用同一个 $m$。左边第一个源确实来自 $Xw\in N$，不是把纯 $Cw$ 免费称作 $M$ 中向量。

式 (6.3) 支付的是新度量中的运输缺陷。它没有给 $N$ 中所有向量的修复范数一个统一界，也没有把 $C_{22}$ 的正向收缩改成右逆上界。

## 7. 原返回费用准确留在新旧度量之间

以下回到同一个 $m,q,r$。省略下标，令原完整最小链为 $c_L+c_H$，原返回源笔记的
$$
K=B^*A_H^{-1}B,\qquad Q=I_Z+K.
$$
则
$$
z_2=A_H^{-1}Bc_L,\qquad B^*z_2=Kc_L,\qquad
Qc_L\perp\mathcal N.
$$
旧末块是
$$
\mathcal H_2=A_H+BB^*,
$$
而 (3.7) 给
$$
\boxed{
\mathcal H_2-\mathcal H_2^\circ
=B(I_Z-P_{\mathcal N})B^*\ge0.
}
\tag{7.1}
$$
记
$$
r_{\rm ret}=\mathsf F Kc_L.
$$
因为 $(I-P_{\mathcal N})Kc_L$ 是 $r_{\rm ret}$ 在 $Z$ 中的裸最小原像，得到
$$
\boxed{
\mathcal E_2-\mathcal E_2^\circ
=\|(I-P_{\mathcal N})Kc_L\|^2
=\|\mathsf F^\dagger r_{\rm ret}\|^2,
}
\tag{7.2}
$$
其中旧 $\mathcal E_2=\langle\mathcal H_2z_2,z_2\rangle$，新
$\mathcal E_2^\circ=\langle\mathcal H_2^\circ z_2,z_2\rangle$。
所以 $\mathcal E_2^\circ\le\lambda^2$ 绝不能代替旧 $\mathcal E_2$ 的上界。

还可在逆度量中给出完整修复费的准确等式。对任意
$f\in\mathscr Y_{2,q}$，把它嵌入整个内部输出，令
$$
u_f=S_q^*\mathcal G_q^{-1}f,\qquad h_f=F_qu_f.
$$
$u_f$ 是所有内部原像的最小者，故 $u_f\perp\ker S_q$。
要再满足首段边界为零，必须加一个 $v\in\ker S_q$ 且
$F_qv=-h_f$。这两个向量正交，最小的 $v$ 正是原完整修复
$-c_q(h_f)$。因此
$$
\boxed{
\|f\|_{(\mathcal H_{2,q}^\circ)^{-1}}^2
=\|f\|_{\mathcal H_{2,q}^{-1}}^2+\lambda_q(h_f)^2.
}
\tag{7.3}
$$
所有量都在同一个原宽度 $d$ 的窗口内；没有加长支持，也没有使用无限尾逆。

特别，对旧有效源 $\sigma=\mathcal H_2z_2$，
内部最小原像的低分量恰为 $B^*z_2$，所以 $h_\sigma=r_{\rm ret}$。
式 (7.3) 成为
$$
\boxed{
\|\sigma\|_{(\mathcal H_2^\circ)^{-1}}^2
=\mathcal E_2+\lambda_q(r_{\rm ret})^2.
}
\tag{7.4}
$$
这正是原返回笔记尚未支付的同窗完整修复费用，未被新的小源运输消去。

## 8. 与真实通量的剩余接口

对 $w\in W=M\ominus N$，旧正通量及宽未来原像仍给
$$
\|v\|^2+\lambda^2-\text{已付 carry}
\le\beta_+\sqrt{\mathcal E_2},
$$
其中必须保留旧 $\mathcal E_2$ 和旧 $\mathcal H_2$。
本稿新前两块能量由真实未来带控制，(6.3) 也把完整第三矩运输接到真正 $Xw\in N$ 的相邻源；但是 (7.2) 的
$\|\mathsf F^\dagger r_{\rm ret}\|$ 尚无上界。

等价地，在新逆度量里测试旧高源会按 (7.3) 自动添加首段边界校正的完整能量。真实未来 $u$ 的边界是
$F_qu=-\widehat r$，一般不为零；因此不能把它当成新
$\mathcal G_q^\circ$ 或新 $\mathcal H_2^\circ$ 的廉价原像。
当前仍须控制这个准确返回项，或利用 (6.3) 及实际 $N$ 源取得额外估计。无权 $N=M$ 和普通 ISP 尚未完成。


## 9. 有效正算子、对偶运输及去掉共同低源后的真实几何

本节仅补全上述接口的状态坐标、对偶预算与实际未来带几何；不另计无权能量上界。

### 9.1 低链状态上的有效正算子

固定 $m,q$，记
$$
\mathcal U_q=Z_q\ominus\mathcal N_q,\qquad
B_{A,q}=B_q|_{\mathcal U_q},
$$
$$
\mathcal R_q=(B_q|_{\mathcal N_q},\,S_{H,q}):
\mathcal N_q\oplus\mathscr X_{H,q}\longrightarrow\mathscr Y_{2,q}.
$$
$\mathcal R_q$ 满射，因为其第二项满射。由 (3.7)
$$
\mathcal H_{2,q}^\circ=\mathcal R_q\mathcal R_q^*.
$$
定义固定参数下有界的正算子
$$
\boxed{
\mathscr L_q
=B_{A,q}^*(\mathcal H_{2,q}^\circ)^{-1}B_{A,q}
\quad\text{作用于 }\mathcal U_q.
}
\tag{9.1}
$$
它不是原纯边界 $L=A+D$。不假设 $\mathscr L_q$ 严格正，也不对其取逆。

对任意 $r$，令 $a=a_q(r)$、$z_2=(\mathcal H_2^\circ)^{-1}B_Aa$。按正交直和
$\mathcal U_q\oplus\mathcal N_q\oplus\mathscr X_{H,q}$，
$$
c_q(r)=a-\mathcal R_q^*z_2.
$$
于是
$$
\boxed{
\lambda_q(r)^2=\|a\|^2+\langle\mathscr L_qa,a\rangle,
\qquad
\mathcal E_{2,q}^\circ=\langle\mathscr L_qa,a\rangle.
}
\tag{9.2}
$$
原返回向量及原末块能量准确为
$$
\boxed{
P_{\mathcal U_q}Kc_L=\mathscr L_qa,\qquad
\mathcal E_{2,q}
=\langle\mathscr L_qa,a\rangle+\|\mathscr L_qa\|^2.
}
\tag{9.3}
$$
由 $r_{\rm ret}=\mathsf F_q\mathscr L_qa$，
$$
a_q(r_{\rm ret})=\mathscr L_qa,
$$
故完整返回费还可写成
$$
\boxed{
\lambda_q(r_{\rm ret})^2
=\|\mathscr L_qa\|^2+
\langle\mathscr L_q(\mathscr L_qa),\mathscr L_qa\rangle.
}
\tag{9.4}
$$
这些等式只重写已存在的极小值；(4.3) 支付 $\|a\|$，未支付
$\|\mathscr L_qa\|$。

### 9.2 完整降孔的正缺陷与准确对偶

仍用同头相邻 $q,q+1$ 的完整 $C=D_{3,m}$。对
$a\in\mathcal U_{q+1}$，定义
$$
\mathsf U_qa=P_{\mathcal U_q}C_La,\qquad
\mathsf J_qa=(P_{\mathcal N_q}C_La,\,C_Ha)
\in\mathcal N_q\oplus\mathscr X_{H,q}.
$$
由完整输入的正交分解，
$$
\boxed{
\mathsf U_q^*\mathsf U_q+\mathsf J_q^*\mathsf J_q
\le s_3^2 I_{\mathcal U_{q+1}}.
}
\tag{9.5}
$$
式 (5.5) 在状态坐标中恰为
$$
\boxed{
B_{A,q}\mathsf U_q-C_{22,q}B_{A,q+1}
=-\mathcal R_q\mathsf J_q.
}
\tag{9.6}
$$
取真正的 Hilbert 伴随，不交换任何逆，得到
$$
\mathsf U_q^*B_{A,q}^*
-B_{A,q+1}^*C_{22,q}^*
=-\mathsf J_q^*\mathcal R_q^*.
$$
所以对 $z\in\mathscr Y_{2,q}$、$a\in\mathcal U_{q+1}$，
$$
\boxed{
\begin{aligned}
&\left|
\left\langle
(\mathsf U_q^*B_{A,q}^*
-B_{A,q+1}^*C_{22,q}^*)z,a
\right\rangle\right|^2\\
&\quad\le
\left\langle(s_3^2I-\mathsf U_q^*\mathsf U_q)a,a\right\rangle
\left\langle\mathcal H_{2,q}^\circ z,z\right\rangle .
\end{aligned}
}
\tag{9.7}
$$
证明是将左边写成
$|\langle\mathcal R_q^*z,\mathsf J_qa\rangle|^2$，
再用 Cauchy--Schwarz、(9.5) 以及
$\|\mathcal R_q^*z\|^2=\langle\mathcal H_2^\circ z,z\rangle$。

对原实际最优 $z=z_{2,q}$，(9.2) 给
$$
\boxed{
\|\mathsf U_q^*\mathscr L_qa_q
-B_{A,q+1}^*C_{22,q}^*z_{2,q}\|
\le s_3\sqrt{\lambda_q^2-\|a_q\|^2}.
}
\tag{9.8}
$$
第二项仍使用 $C_{22,q}^*z_{2,q}$。它未被认成第 $q+1$ 层某个实际源的最优对偶，因此 (9.8) 不是两个实际返回向量之间的无条件交换式。

### 9.3 实际源提取的有界交织与正交性的准确位置

定义原核上的线性算子
$$
\mathcal A_q:M\longrightarrow\mathcal U_q,\qquad
\mathcal A_qw=a_q(r_{m,q}(w)).
$$
(4.3) 给
$$
\|\mathcal A_qw\|
\le\|P_{[q+1,q+d]}^{(m)}w\|+e^{-72d^4}\|w\|,
\qquad
\|\mathcal A_q\|\le1+e^{-72d^4}.
\tag{9.9}
$$
由 (5.4)、(6.2) 和 (3.3)，对实际 $X=X_{3,m}$ 有
$$
\boxed{
\mathcal A_qX|_M
=\mathsf U_q\mathcal A_{q+1}+\mathcal E_q,\qquad
\|\mathcal E_q\|\le18s_3e^{-73d^4}.
}
\tag{9.10}
$$
这里两侧所有算子都定义在 $M$ 上；$X|_M$ 确实把 $M$ 送入 $N$。

令 $X_M=X|_M$，其伴随为 $M$ 内的伴随。取 (9.10) 的伴随后，
$$
X_M^*\mathcal A_q^*
=\mathcal A_{q+1}^*\mathsf U_q^*+\mathcal E_q^*.
\tag{9.11}
$$
旧联合旗对偶预算是 $\|z_q\|\le e^{2d^4}\lambda_q$；
$\|B_{A,q}\|\le\|S_q\|\le7$，故
$$
\|\mathscr L_qa_q\|\le7e^{2d^4}\lambda_q.
$$
因此，即使对真实返回向量，(9.11) 的误差也已经支付：
$$
\boxed{
\|\mathcal E_q^*\mathscr L_q\mathcal A_qw\|
\le126s_3e^{-71d^4}\lambda_q
\le s_3e^{-70d^4}\lambda_q.
}
\tag{9.12}
$$

真正 $w\in W=M\ominus N$ 满足 $X_M^*w=0$。但是
$\mathcal A_q^*\mathscr L_q\mathcal A_qw$ 一般只是 $M$ 中另一个向量，
未证明它属于 $W$，也未证明它接近 $w$ 或 $w$ 的标量倍数。
所以不能把
$$
X_M^*\mathcal A_q^*\mathscr L_q\mathcal A_qw
$$
直接宣布为零。这是把 (9.8)–(9.12) 接到真实正交条件时必须保留的项；已付小误差不能替代该主项。

### 9.4 去掉共同低源的真实未来几何

以下重新取 $w\in W$，并使用 §4 的真正宽低投影
$\widehat v$、未来输入 $u$、$\widehat r$ 和高通量源 $f$。
设
$$
r=r_{m,q}(w),\quad a=a_q(r),\quad
\widehat a=a_q(\widehat r),\quad
v=v_{m,q}(w),\quad \lambda=\lambda_q(r).
$$
由 $u_L\in Z_q$、$\mathsf F_qu_L=-\widehat r$，
$$
u_L=-\widehat a+n,\qquad n\in\mathcal N_q.
$$
因此
$$
g:=u+\widehat a=n+u_H
\in\mathcal N_q\oplus\mathscr X_{H,q}\subset\ker F_q,
$$
$$
g\perp\mathcal U_q,\qquad
\|g\|^2=\|u\|^2-\|\widehat a\|^2,
$$
$$
\boxed{
S_qg=\sigma_q^\circ(\widehat r)-f.
}
\tag{9.13}
$$
这将去掉共同低源后的未来质量准确放在零首段边界中，而没有把原 $u$ 免费当作零边界输入。

为与原 $r$ 的最优链配对，置
$$
\overline u=u+\widehat a-a=-a+g,\qquad
\overline f=f-B_q(\widehat a-a).
$$
于是
$$
F_q\overline u=-r,\quad
S_q\overline u=-\overline f,\quad
\overline u+a=g,\quad
S_qg=\sigma_q^\circ(r)-\overline f.
\tag{9.14}
$$
从 (3.8) 或 (9.1)，
$$
c_q(r)=a-\mathcal R_q^*z_{2,q}.
$$
$g\perp a$，所以准确的配对是
$$
\boxed{
\langle\overline u,c_q(r)\rangle
=-\|a\|^2+
\langle\overline f-\sigma_q^\circ(r),z_{2,q}\rangle.
}
\tag{9.15}
$$
同时
$$
\|\overline f-\sigma_q^\circ(r)\|_{(\mathcal H_2^\circ)^{-1}}
\le\|g\|
=\sqrt{\|u\|^2-\|\widehat a\|^2}.
\tag{9.16}
$$
这里没有多付一个 $\sqrt d$，也没有用粗略的 $2\beta$ 来替代正交差。

现在明确全部误差。置
$$
\delta=e^{-74d^4},\qquad \epsilon=e^{-75d^4},\qquad
\delta_r=12e^{-73d^4}.
$$
由 §4 和完整右逆，
$$
\|\widehat a-a\|,\ 
\|c_q(\widehat r)-c_q(r)\|
\le\delta_r\|w\|.
\tag{9.17}
$$
原实际核 lift 应用于 $v-c_q(r)$，给
$$
|\langle w,c_q(r)\rangle-\|v\|^2|
\le\epsilon\|w\|\sqrt{\|v\|^2+\lambda^2}.
$$
$u$ 是 $\widehat v$ 在原修复域中的未来分量，所以
$$
|\langle u-w,c_q(r)\rangle|\le\delta\|w\|\lambda.
$$
又因 $\widehat a-a\in\mathcal U_q$，它与 $c_q(r)-a$ 正交，
$$
|\langle\widehat a-a,c_q(r)\rangle|
\le\delta_r\|w\|\|a\|.
$$
合起来得到
$$
\left|\langle\overline u,c_q(r)\rangle-\|v\|^2\right|
\le\varepsilon_{\rm geom},
$$
$$
\varepsilon_{\rm geom}:=
\epsilon\|w\|\sqrt{\|v\|^2+\lambda^2}
+\delta\|w\|\lambda+\delta_r\|w\|\|a\|.
\tag{9.18}
$$
设
$$
\beta^\circ=\beta_q(w)+e^{-72d^4}\|w\|.
$$
因 $\|u\|\le\beta_q+\delta\|w\|$ 及 (9.17)，
$\|\overline u\|\le\beta^\circ$；并且
$$
\|g\|^2=\|\overline u\|^2-\|a\|^2
\le(\beta^\circ)^2-\|a\|^2.
$$
$d\ge32$、$\|v\|\le\|w\|$ 与 $\|a\|\le\beta^\circ\le2\|w\|$ 还给
$$
\varepsilon_{\rm geom}
\le e^{-72d^4}\|w\|(\|w\|+\lambda).
\tag{9.19}
$$
由 (9.15)–(9.18) 和 (9.2) 的 Cauchy--Schwarz，最终为
$$
\boxed{
\bigl(\|v\|^2+\|a\|^2-\varepsilon_{\rm geom}\bigr)_+^2
\le
\bigl(\|u\|^2-\|\widehat a\|^2\bigr)
\bigl(\lambda^2-\|a\|^2\bigr)
\le
\bigl((\beta^\circ)^2-\|a\|^2\bigr)
\bigl(\lambda^2-\|a\|^2\bigr).
}
\tag{9.20}
$$
所有平方根和右侧因子非负，来自上述正交分解；左边取正部避免小误差下的符号假设。

式 (9.20) 准确去掉共同低源，保留全部真实 carry。它仍与大的
$\|\mathscr L_qa\|$ 相容，不构成返回费用上界；后续须继续处理 (9.3)、(9.8) 中的真实返回向量及 (9.11) 中不能被 $w\perp N$ 直接杀掉的主项。


### 9.5 真正 $W$ 正交使零边界未来近乎极小

继续用 §9.4 的同一个 $g=u+\widehat a=\overline u+a$，并令
$$
\mathcal K_q=\ker\mathcal R_q
\subset\mathcal N_q\oplus\mathscr X_{H,q}.
$$
按原输入空间嵌入，
$$
\mathcal K_q=\ker F_q\cap\ker S_q.
\tag{9.21}
$$
确实，$\ker F_q\cap\ker S_q$ 的低分量属于
$Z_q\cap\ker\mathsf F_q=\mathcal N_q$，高分量属于
$\mathscr X_{H,q}$；其唯一剩余内部方程就是
$\mathcal R_q(n,c_H)=0$。反向包含直接由定义得到。

令
$$
k=P_{\mathcal K_q}g.
$$
$k$ 是支撑在原带 $[q+1,q+d]$ 中的完整 $L=A+D$ 核向量：
$F_qk=0$ 给最低输出，$S_qk=0$ 给全部内部输出，
$Ak_d=0$ 已由联合旗自动满足。因此原实际核 lift 给
$$
\Lambda k\in N,\qquad
\|\Lambda k-k\|\le\epsilon\|k\|,\qquad \epsilon=e^{-75d^4}.
$$
这里仍是原合法窗口中的有限孔核 lift，没有放宽支持或调用未知的全局投影稳定性。对真正 $w\in W=M\ominus N$，
$$
|\langle w,k\rangle|\le\epsilon\|w\|\,\|k\|.
$$
另一方面，$\widehat a\in\mathcal U_q$ 与 $\mathcal K_q$ 正交，所以
$$
\langle u,k\rangle=\langle g,k\rangle=\|k\|^2.
$$
$u$ 是宽低投影 $\widehat v$ 的原修复域未来分量，而 $k\in\mathscr C_q$。由 (4.1)，
$$
|\langle u-w,k\rangle|\le\delta\|w\|\,\|k\|,
\qquad \delta=e^{-74d^4}.
$$
合并并在 $\|k\|\ne0$ 时约去它，严格得到
$$
\boxed{
\|P_{\mathcal K_q}g\|
\le(\delta+\epsilon)\|w\|.
}
\tag{9.22}
$$

由于 $\mathcal R_q$ 满射，$\operatorname{Ran}\mathcal R_q^*$
闭且等于 $\mathcal K_q^\perp$。因此 $g$ 对其实际内部输出的最小原像是
$$
g_{\min}
=\mathcal R_q^*(\mathcal H_{2,q}^\circ)^{-1}
\bigl(\sigma_q^\circ(\widehat r)-f\bigr)
=g-P_{\mathcal K_q}g.
$$
用 (9.14)，同一个向量也可把括号写成
$\sigma_q^\circ(r)-\overline f$。于是
$$
\boxed{
\operatorname{dist}(g,\operatorname{Ran}\mathcal R_q^*)
=\|g-g_{\min}\|
\le(\delta+\epsilon)\|w\|.
}
\tag{9.23}
$$
原正交 Pythagoras 还给精确平方范数差
$$
\boxed{
\begin{aligned}
0\le{}&
\|u\|^2-\|\widehat a\|^2
-\|\sigma_q^\circ(\widehat r)-f\|_{(\mathcal H_{2,q}^\circ)^{-1}}^2\\
={}&\|P_{\mathcal K_q}g\|^2
\le(\delta+\epsilon)^2\|w\|^2.
\end{aligned}
}
\tag{9.24}
$$
等式同样适用于 $(\overline u,a,\sigma_q^\circ(r)-\overline f)$。
所以 (9.16) 的损失确实只有已经支付的 carry。

本节直接使用原 $w$ 与实际 $N$ 的正交，没有对
$\mathcal A_q^*\mathscr L_q\mathcal A_qw$ 施加这种正交。
它约束的是去共同低源后的真实未来向量，尚未把该近乎极小的向量与
$\mathscr L_qa_q(w)$ 的大小联系起来，因而仍不提供原返回费用上界。



### 9.6 由原 W 向量产生的廉价协向量和真正伴随约束

本节内积对第一变量线性，伴随满足
$\langle Tx,y\rangle=\langle x,T^*y\rangle$。
保持 §9.1 的原输入正交分解，并记
$$
\mathcal T_q
=\mathcal R_q^*(\mathcal H_{2,q}^\circ)^{-1}B_{A,q}:
\mathcal U_q\longrightarrow
\mathcal N_q\oplus\mathscr X_{H,q},
\qquad
\mathcal T_q^*\mathcal T_q=\mathscr L_q.
\tag{9.25}
$$
这里 $\mathcal T_q$ 不是原算子 $T$。定义有闭像的图嵌入
$$
\mathcal J_q a=a-\mathcal T_q a,\qquad
\mathcal P_q=I_{\mathcal U_q}+\mathscr L_q
=\mathcal J_q^*\mathcal J_q\ge I.
\tag{9.26}
$$
因此只对严格正的 $\mathcal P_q$ 取逆，不对可能有核的
$\mathscr L_q$ 取逆。由 (9.2)，$\mathcal J_q a$ 正是源
$\mathsf F_q a$ 的完整最小修复链。

固定原 $w\in W=M\ominus N$。以下仍用 §9.4 的同一个实际宽窗向量
$u$、$\widehat a$，及
$$
a=\mathcal A_qw,\qquad
g=u+\widehat a,\qquad
\overline u=-a+g=u+\widehat a-a.
$$
它们属于原联合输入；$a\in\mathcal U_q$，
$g\in\mathcal N_q\oplus\mathscr X_{H,q}$。置
$$
\boxed{
\eta_q
=\mathcal J_q^*\overline u
=-a-\mathcal T_q^*g
\in\mathcal U_q.
}
\tag{9.27}
$$
因为 $\mathcal T_q^*(\ker\mathcal R_q)=0$，(9.27) 中的 $g$
可以精确换成 §9.5 的 $g_{\min}$，不增加误差。
$\eta_q$ 是从原 $w$ 构造的协向量；它不是
$\mathscr L_q\mathcal A_qw$。

#### A. 原 M 中的伴随重建，保留所有正交压缩

记
$$
\delta=e^{-74d^4},\qquad
\epsilon=e^{-75d^4},\qquad
\rho=e^{-72d^4}.
$$
令 $V_{m,q}$ 为原低输出约束空间，使用它在整个环境 Hilbert
空间中的正交投影 $P_{V_{m,q}}$。对 $\xi\in M$，写
$$
v(\xi)=P_{V_{m,q}}\xi,\qquad
r(\xi)=A_m v_q(\xi),\qquad
a(\xi)=\mathcal A_q\xi,\qquad
c(\xi)=\mathcal J_q a(\xi).
$$
这里 $\mathcal A_q^*:\mathcal U_q\to M$ 是
$\mathcal A_q:M\to\mathcal U_q$ 的实际受限伴随。

由原同时右逆及 $\|A_m\|\le6$，
$$
\|c(\xi)\|\le e^{d^4}\|r(\xi)\|
\le6e^{d^4}\|\xi\|.
\tag{9.28}
$$
$v(\xi)-c(\xi)$ 是原 $L_m=A_m+D_m$ 的有限核向量，
支持不超过 $q+d$，且两部分在孔层上正交。因此
$$
\|v(\xi)-c(\xi)\|
\le\sqrt{1+36e^{2d^4}}\,\|\xi\|
\le7e^{d^4}\|\xi\|.
$$
本稿已经使用的原有限核 lift 给
$\Lambda(v(\xi)-c(\xi))\in N$，与原向量的距离不超过
$\epsilon\|v(\xi)-c(\xi)\|$。原 $w\perp N$ 因而给
$$
|\langle w,c(\xi)\rangle-\langle w,v(\xi)\rangle|
\le7e^{-74d^4}\|w\|\,\|\xi\|.
\tag{9.29}
$$
这里对全部 $\xi\in M$ 同时成立；没有把 $\xi$ 限在 $W$。

原宽窗投影及 §9.4 的同源校正分别给
$$
\|u-P_{\mathscr C_q}w\|\le\delta\|w\|,
\qquad
\|\widehat a-a\|\le12e^{-73d^4}\|w\|.
\tag{9.30}
$$
此外由 (4.3)，
$$
\|a(\xi)\|\le(1+\rho)\|\xi\|\le2\|\xi\|.
$$
最重要的正交性是
$$
\langle\widehat a-a,c(\xi)\rangle
=\langle\widehat a-a,a(\xi)\rangle,
\tag{9.31}
$$
因为左因子属于 $\mathcal U_q$，而
$c(\xi)-a(\xi)\in\mathcal N_q\oplus\mathscr X_{H,q}$。
所以这一步不再乘 (9.28) 中的大完整链常数。

由 (9.27) 和上述内积约定，
$$
\langle\mathcal A_q^*\eta_q,\xi\rangle
=\langle\eta_q,\mathcal A_q\xi\rangle
=\langle\overline u,c(\xi)\rangle.
$$
结合 (9.28)—(9.31)，以及正交投影的自伴性
$$
\langle w,v(\xi)\rangle
=\langle P_Mv(w),\xi\rangle
\quad(\xi\in M),
$$
得到
$$
\begin{aligned}
|\langle\mathcal A_q^*\eta_q-P_Mv(w),\xi\rangle|
&\le
\bigl(6e^{-73d^4}+24e^{-73d^4}+7e^{-74d^4}\bigr)
\|w\|\,\|\xi\|\\
&\le \rho\|w\|\,\|\xi\|.
\end{aligned}
$$
最后一步对原 $m\ge5$ 成立。取 $M$ 内单位向量的上确界，得到
$$
\boxed{
\|\mathcal A_q^*\eta_q-P_Mv(w)\|
\le\rho\|w\|.
}
\tag{9.32}
$$
定义与当前头 $m$ 相应的原孔数尾
$$
\tau_q(w)=\|P_{>q}^{(m)}w\|.
$$
原低投影误差给
$\|v(w)-P_{\le q}^{(m)}w\|\le\delta\|w\|$。由于
$w\in M$，
$$
\boxed{
\|\mathcal A_q^*\eta_q-w\|
\le\tau_q(w)+2\rho\|w\|.
}
\tag{9.33}
$$
(9.32) 是 $M$ 中的范数结论，不只是与 $w$ 自身的一个标量配对；
其中 $P_M$ 和 $P_{V_{m,q}}$ 均未删除。

#### B. 图的正交投影和真实未来带的逆度量预算

由 $\mathcal J_q^*\mathcal J_q=\mathcal P_q\ge I$，
$\mathcal J_q\mathcal P_q^{-1}\mathcal J_q^*$ 正是
$\operatorname{Ran}\mathcal J_q$ 的正交投影。故有精确等式
$$
\boxed{
\|\mathcal P_q^{-1/2}\eta_q\|^2
=\|P_{\operatorname{Ran}\mathcal J_q}\overline u\|^2
\le\|\overline u\|^2
\le\bigl(\beta_q^\circ(w)\bigr)^2,
}
\tag{9.34}
$$
其中沿用 §9.4
$$
\beta_q^\circ(w)
=\|P_{[q+1,q+d]}^{(m)}w\|+\rho\|w\|.
$$
这是原 Hilbert 空间的图极分解/正交投影等式，不是将新度量当作
普通范数，也不要求 $\mathscr L_q$ 可逆。

更明确地，令
$$
\vartheta_q=\mathcal P_q^{-1}\eta_q,\qquad
r_q^{\rm small}=\mathsf F_q\vartheta_q.
$$
则 $\vartheta_q\in\mathcal U_q$，
$r_q^{\rm small}\in\mathscr R_q$，且
$$
\boxed{
c_q(r_q^{\rm small})
=\mathcal J_q\vartheta_q
=P_{\operatorname{Ran}\mathcal J_q}\overline u,
\qquad
\lambda_q(r_q^{\rm small})\le\beta_q^\circ(w).
}
\tag{9.35}
$$
因此 $\eta_q=\mathcal P_q\vartheta_q$ 是一个确切廉价修复源的
能量协向量。这里的 $r_q^{\rm small}$ 尚未被识别为原返回源。
又因
$$
\ker S_q
=\operatorname{Ran}\mathcal J_q
\mathbin{\oplus^\perp}
(\ker\mathsf F_q\cap\ker S_q),
$$
(9.35) 与 $P_{\ker S_q}\overline u$ 的差恰为
$P_{\ker\mathcal R_q}g$，其范数已由 (9.22) 支付。

#### C. 由原 w 的正交得到的合法相邻伴随约束

这一段再假设同头相邻层合法，即 $q+1\le e^{d^3/4}$。
§9.3 的实际源交织是
$$
\mathcal A_q X_M
=\mathsf U_q\mathcal A_{q+1}+\mathcal E_q,
\qquad
\|\mathcal E_q\|\le18s_3e^{-73d^4}.
\tag{9.36}
$$
其中 $X_M=X_3|_M$，$X_3M\subset N$，
$\|X_M\|\le s_3$，所以原 $w\in W$ 确实满足
$X_M^*w=0$。

先付 (9.36) 对 $\eta_q$ 的 carry。由
$\mathcal H_2^\circ\ge e^{-2d^4}I$、
$\|B_A\|\le\|S_q\|\le7$，
$$
\|\mathcal T_q\|
=\|(\mathcal H_2^\circ)^{-1/2}B_A\|
\le7e^{d^4}.
$$
于是
$$
\|\eta_q\|
\le\|\mathcal J_q\|\,\|\overline u\|
\le8e^{d^4}\beta_q^\circ(w)
\le16e^{d^4}\|w\|.
\tag{9.37}
$$
对 (9.36) 取受限伴随，并在此处实际使用 $X_M^*w=0$：
$$
\mathcal A_{q+1}^*\mathsf U_q^*\eta_q
=X_M^*(\mathcal A_q^*\eta_q-w)-\mathcal E_q^*\eta_q.
$$
由 (9.33)、(9.37)，
$$
\boxed{
\|\mathcal A_{q+1}^*\mathsf U_q^*\eta_q\|
\le s_3\bigl(\tau_q(w)+e^{-71d^4}\|w\|\bigr).
}
\tag{9.38}
$$
这里 $288s_3e^{-72d^4}\|w\|$ 的误差与
$2s_3\rho\|w\|$ 一起被右侧吸收。
这给出真正由原 $W$ 正交性支付的伴随主项。

为明确其度量，旧完整最小链的降孔收缩还可在当前坐标重写为
$$
\boxed{
\mathsf U_q^*\mathcal P_q\mathsf U_q
\le s_3^2\mathcal P_{q+1}.
}
\tag{9.39}
$$
证明是对任意 $a'\in\mathcal U_{q+1}$：
$C\mathcal J_{q+1}a'$ 是降孔后源的可行完整链，
其真正最小链为 $\mathcal J_q\mathsf U_qa'$。于是
$\|\mathcal J_q\mathsf U_qa'\|
\le s_3\|\mathcal J_{q+1}a'\|$。
这是既有完整 $\lambda$ 收缩的坐标式，不是新的能量定理。
取对应有界算子的伴随，等价地
$$
\mathsf U_q\mathcal P_{q+1}^{-1}\mathsf U_q^*
\le s_3^2\mathcal P_q^{-1}.
$$
所以 (9.34) 还给
$$
\boxed{
\|\mathcal P_{q+1}^{-1/2}\mathsf U_q^*\eta_q\|
\le s_3\|\mathcal P_q^{-1/2}\eta_q\|
\le s_3\beta_q^\circ(w).
}
\tag{9.40}
$$

(9.32)—(9.40) 连接的是原 $w$、真实未来向量及其实际协向量
$\eta_q$。仍没有证明
$\eta_q=\mathscr L_q\mathcal A_qw$，也没有证明二者的差小。
尤其 (9.38) 不能改写成删除
$X_M^*\mathcal A_q^*\mathscr L_q\mathcal A_qw$。
原返回费用的上界仍须另付。



#### D. 廉价源与真正窄通量的同窗身份

本段保持同一个 $m,q,w$。用
$$
\mathcal G_q^{\rm old}=S_qS_q^*,\qquad
S_q^\dagger=S_q^*(\mathcal G_q^{\rm old})^{-1}
$$
表示原内部最小右逆，并明确区分旧末块
$$
\mathcal H_{2,q}^{\rm old}
=A_{H,q}+B_qB_q^*
=\mathcal H_{2,q}^{\circ}+B_{A,q}B_{A,q}^*
$$
与先消首段边界所得的新末块 $\mathcal H_{2,q}^{\circ}$。
§9.4 的 $\overline f$ 仍在真实高输出 $\mathscr Y_{2,q}$：
原 $f$ 在该空间，校正 $B_q(\widehat a-a)$ 也在该空间。

令
$$
k=P_{\ker\mathcal R_q}g,\qquad
x_f=S_q^\dagger\overline f.
$$
因为 $S_q\overline u=-\overline f$，而 §9.6.B 已识别其
$\ker S_q$ 投影，有准确正交分解
$$
\boxed{
\overline u=c_q(r_q^{\rm small})+k-x_f.
}
\tag{9.41}
$$
前两项在 $\ker S_q$ 中相互正交，末项在
$\operatorname{Ran}S_q^*=(\ker S_q)^\perp$。
$F_qk=0$，且 $F_q\overline u=-r$，所以
$$
\boxed{
r_q^{\rm small}=-r+F_qS_q^\dagger\overline f.
}
\tag{9.42}
$$
这里 $F_q$ 是完整输入上的首输出；没有只取某个低出生块代替它。

旧消元的原最小内部像给
$(x_f)_L=B_q^*(\mathcal H_{2,q}^{\rm old})^{-1}\overline f$。
取其 $\mathcal U_q$ 分量，再用 (9.42)，得到
$$
\boxed{
a+\vartheta_q
=B_{A,q}^*(\mathcal H_{2,q}^{\rm old})^{-1}\overline f.
}
\tag{9.43}
$$
同式也可由准确的有界 Woodbury 恒等式核对：
$$
\boxed{
\mathcal P_q^{-1}B_{A,q}^*(\mathcal H_{2,q}^{\circ})^{-1}
=B_{A,q}^*(\mathcal H_{2,q}^{\rm old})^{-1}.
}
\tag{9.44}
$$
事实上由 (9.27) 及
$g_{\min}=\mathcal R_q^*(\mathcal H_{2,q}^{\circ})^{-1}
(B_{A,q}a-\overline f)$，
有
$\eta_q=-\mathcal P_qa+
B_{A,q}^*(\mathcal H_{2,q}^{\circ})^{-1}\overline f$；
乘 $\mathcal P_q^{-1}$ 后即为 (9.43)。

最后，对 (9.41) 取原范数，使用高输出上旧完整逆的正确 Schur
压缩，得到
$$
\boxed{
\|\overline u\|^2
=\lambda_q(r_q^{\rm small})^2
+\|\overline f\|_{(\mathcal H_{2,q}^{\rm old})^{-1}}^2
+\|k\|^2.
}
\tag{9.45}
$$
$\|k\|$ 的 carry 已由 (9.22) 支付。这里把同一真实未来预算
准确分给三个正交项；没有将 $\overline f$ 换成旧有效源
$\sigma_q$。式 (9.42)—(9.45) 仍未识别
$r_q^{\rm small}$ 或 $F_qS_q^\dagger\overline f$
为原返回残量 $r_{\rm ret}$，也不提供后者的完整修复费用上界。


### 9.7 既有左源 Gram 的状态坐标复核及廉价源匹配

[既有左源 Gram 笔记](../notes/2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)
已经证明完整左最小前驱、$e^{20d^4}$ 预算、原零源核正交，
以及变换源 $G_qJ_q^{-1}r$ 的廉价右修复。本节 A–C 是这些接口在
本稿 $\mathcal U_q$ 状态坐标中的明确复核，不重计为新结果；
D 把该变换源与 §9.6 的真实未来投影源匹配。
全过程保持原范数、原低输出空间和同一个 $r=F_qa$；不将
$\mathcal P_q=I+\mathscr L_q$ 与下面的正 Gram 交换或比较。

#### A. 原低源映射的满射及明确下补塔

准确使用
$$
V_{m,q}
=\mathcal H_{\le q}^{(m)}
\cap\ker(P_{\le q-1}^{(m)}L_m),\qquad
L_m=A_m+D_m,
$$
以及
$$
\mathscr R_q
=\bigoplus_{i=0}^{d-2}e_i E_{d-i-1,q}.
$$
定义
$$
\mathsf A_q^-:V_{m,q}\longrightarrow\mathscr R_q,
\qquad
\mathsf A_q^-v=A_mv_q.
\tag{9.46}
$$
其值确在所写残量旗内：低输出方程逐次给
$$
D_m^k(A_mv_q)=(-1)^kA_m^{k+1}v_{q-k}
\in\operatorname{Ran}A_m^{k+1}
\quad(0\le k\le d-1).
$$
原头单链旗使这些条件等价于 $\mathscr R_q$ 的逐头短核条件。

用[完整核拼合稿](R239-appendix-full-l-kernel-completion-and-legal-m-tests.md)
§§3–4 的同一个头右移
$$
\mathcal J_m=S_m(\vartheta_m^{-1}J_d^*)S_m^{-1},
\qquad
\vartheta_m
=\exp\!\left(20-\frac{25d^4}{2(d-2)}\right),
$$
$$
\|\mathcal J_m^\ell\|\le\kappa_m\vartheta_m^{-\ell},
\qquad
\log\kappa_m\le7d^4.
$$
$\mathcal J_m$ 不是 Moore--Penrose 逆。它满足
$A_m\mathcal J_m=I$ 于 $\operatorname{Ran}A_m$，并将
$\operatorname{Ran}A_m^{\ell+1}$ 送入 $\operatorname{Ran}A_m^\ell$。

给定 $r\in\mathscr R_q$，定义只含低层的塔
$$
(\mathcal B_q^-r)_{q-k}
=(-1)^k\mathcal J_m^{k+1}D_m^kr
\quad(0\le k\le d-2),
\tag{9.47}
$$
其余孔层取零。由于
$D_m^kr\in\operatorname{Ran}A_m^{k+1}$，
每一步 $A_m\mathcal J_m=I$ 都在合法的头像上使用。
对相邻两层，
$$
A_m(\mathcal B_q^-r)_{q-k}
+D_m(\mathcal B_q^-r)_{q-k+1}=0
\quad(1\le k\le d-2).
$$
最底端由 $D_m^{d-1}r=0$ 封口；顶端
$A_m(\mathcal B_q^-r)_q=r$。因此
$$
\mathcal B_q^-r\in V_{m,q},\qquad
\mathsf A_q^-\mathcal B_q^-r=r.
$$
$q\ge4d$ 保证这里所有孔层非负。

不同塔项的孔层正交，且 $\|D_m\|\le1/m\le1$，所以
$$
\|\mathcal B_q^-r\|
\le\sqrt d\,\kappa_m\vartheta_m^{-(d-1)}\|r\|
\le e^{20d^4}\|r\|.
\tag{9.48}
$$
最后一个界可直接由 $d\ge32$ 核查：
$$
7+\frac{25}{2}\frac{d-1}{d-2}
\le\frac{239}{12}<20,
$$
剩余 $\tfrac12\log d$ 被严格余量吸收。
这里完整保留了 $\vartheta_m^{-(d-1)}$，没有只付头条件数。

#### B. 最小低前驱及双边正界

(9.48) 使 $\mathsf A_q^-$ 有有界的真正最小右逆。定义
$$
\mathcal J_{-,q}
=(\mathsf A_q^-)^\dagger F_q|_{\mathcal U_q}:
\mathcal U_q\longrightarrow V_{m,q},
\qquad
\mathcal Q_q^-=\mathcal J_{-,q}^*\mathcal J_{-,q}.
\tag{9.49}
$$
这里 $F_q$ 仍为完整联合输入的首输出，其在
$\mathcal U_q=Z_q\ominus\ker(F_q|_{Z_q})$ 上是到
$\mathscr R_q$ 的有界同构。原同时右逆已经给
$$
\|(F_q|_{\mathcal U_q})^{-1}\|\le e^{d^4},
\qquad
\|F_q\|\le\|D_m\|\le1/m.
$$
又 $\|\mathsf A_q^-\|\le6$。因此
$$
\boxed{
\frac{e^{-2d^4}}{36}I_{\mathcal U_q}
\le\mathcal Q_q^-
\le e^{40d^4}I_{\mathcal U_q}.
}
\tag{9.50}
$$
下界来自
$\|\mathcal J_{-,q}a'\|\ge\|F_qa'\|/6
\ge e^{-d^4}\|a'\|/6$；上界来自 (9.48)。
它是固定头原低前驱的正 Gram，并不等于未来修复的
$\mathcal P_q$。

记
$$
V_{0,q}=\ker\mathsf A_q^-\subset V_{m,q}.
$$
对原 $w\in W$，$v=v(w)$、$a=\mathcal A_qw$ 满足
$$
v=\mathcal J_{-,q}a+v_0,\qquad v_0\in V_{0,q},
\qquad
v_0\perp\operatorname{Ran}\mathcal J_{-,q}.
\tag{9.51}
$$
每个 $v_0\in V_{0,q}$ 是支持于 $\le q$ 的完整 $L_m$ 核；
原 lift 将它送入 $N$，误差至多
$\epsilon\|v_0\|$。因 $v=P_{V_{m,q}}w$，
$$
\|v_0\|^2=\langle w,v_0\rangle,
$$
故原 $w\perp N$ 直接给
$$
\boxed{
\|v-\mathcal J_{-,q}a\|
=\|v_0\|\le\epsilon\|w\|,
\qquad
0\le\|v\|^2-\langle\mathcal Q_q^-a,a\rangle
=\|v_0\|^2\le\epsilon^2\|w\|^2.
}
\tag{9.52}
$$

#### C. 对全部真实源测试后得到 η 的正算子身份

任取 $a'\in\mathcal U_q$，不先假定它是某个实际 $M$ 向量的
投影源。两个最小链
$\mathcal J_{-,q}a'$ 和 $\mathcal J_q a'$
具有同一个残量 $F_qa'$，分别支持于 $\le q$ 和 $>q$。
因此
$$
K(a')=\mathcal J_{-,q}a'-\mathcal J_qa'
$$
是支持于 $\le q+d$ 的完整 $L_m$ 核。原同时右逆给
$\|\mathcal J_qa'\|\le e^{d^4}\|F_qa'\|\le e^{d^4}\|a'\|$，
结合 (9.48)，
$$
\|K(a')\|\le2e^{20d^4}\|a'\|.
$$
原 lift 及 $w\perp N$ 于是给
$$
|\langle w,\mathcal J_qa'\rangle
-\langle w,\mathcal J_{-,q}a'\rangle|
\le2e^{-55d^4}\|w\|\,\|a'\|.
\tag{9.53}
$$
另一方面，(9.51) 的正交性和 $v=P_{V_{m,q}}w$ 给
$$
\langle w,\mathcal J_{-,q}a'\rangle
=\langle\mathcal Q_q^-a,a'\rangle.
$$
由 (9.27)，
$\langle\eta_q,a'\rangle=\langle\overline u,\mathcal J_qa'\rangle$。
使用 (9.30)，并再次只将 $\widehat a-a$ 配到低链 $a'$，
两者之差至多
$$
\bigl(e^{-73d^4}+12e^{-73d^4}\bigr)\|w\|\,\|a'\|.
$$
与 (9.53) 合并、对任意单位 $a'$ 取上确界，得到
$$
\boxed{
\|\eta_q-\mathcal Q_q^-a_q\|
\le e^{-54d^4}\|w\|.
}
\tag{9.54}
$$
因此原协向量满足一个额外的真实正性条件，而不是任意的
$\mathcal U_q$ 向量。由 $\mathcal P_q^{-1}\le I$ 及 (9.34)，
$$
\boxed{
\|\mathcal P_q^{-1/2}\mathcal Q_q^-a_q\|
\le\beta_q^\circ(w)+e^{-54d^4}\|w\|.
}
\tag{9.55}
$$
再与 (9.44) 前的确切式合并，
$$
\boxed{
\left\|
(\mathcal Q_q^-+\mathcal P_q)a_q
-B_{A,q}^*(\mathcal H_{2,q}^\circ)^{-1}\overline f
\right\|
\le e^{-54d^4}\|w\|.
}
\tag{9.56}
$$
(9.56) 使用真正的窄通量 $\overline f$，不把它改成 $\sigma_q$。

当相邻同头层合法时，完整 $C$ 同时保持低输出空间及其零源核。
对一个最小低前驱先乘 $C$，再取相同残量的真正低最小前驱，得到
$$
\boxed{
\mathsf U_q^*\mathcal Q_q^-\mathsf U_q
\le s_3^2\mathcal Q_{q+1}^-.
}
\tag{9.57}
$$
具体说，$C\mathcal J_{-,q+1}a'$ 是
$F_q\mathsf U_qa'=C_{\mathscr R,q}F_{q+1}a'$ 的合法低前驱，
其最小者是 $\mathcal J_{-,q}\mathsf U_qa'$。
所以 (9.57) 与 (9.39) 对同一个 $\mathsf U_q$ 成立。

#### D. 与原左、右 Gram 的准确字典

为避免同名，令 $J_q^{\rm left}=E_qE_q^*$ 为上述既有左源笔记的
Gram，其中 $E_q=\mathsf A_q^-$；令 $G_q^{\rm right}$ 为原右侧
$\ker S_q$ 中首输出的源 Gram。另记
$$
F_{U,q}=F_q|_{\mathcal U_q}:
\mathcal U_q\longrightarrow\mathscr R_q.
$$
它是 B 中的有界同构。左、右最小前驱在当前状态坐标中的准确字典为
$$
\boxed{
\mathcal P_q
=F_{U,q}^*(G_q^{\rm right})^{-1}F_{U,q},
\qquad
\mathcal Q_q^-
=F_{U,q}^*(J_q^{\rm left})^{-1}F_{U,q}.
}
\tag{9.58}
$$
这来自分别将原最小前驱作用于 $r=F_{U,q}a$；
是合同关系，不是相同 Gram 的普通压缩。

因此既有变换源
$$
r_q^\flat=G_q^{\rm right}(J_q^{\rm left})^{-1}r
$$
满足
$$
\boxed{
F_{U,q}\mathcal P_q^{-1}\mathcal Q_q^-a=r_q^\flat.
}
\tag{9.59}
$$
这里仅以有界同构 $F_{U,q}$ 和其伴随作准确消元，不交换两个
Gram 的逆。由
$r_q^{\rm small}=F_{U,q}\mathcal P_q^{-1}\eta_q$、
(9.54) 和 $\mathcal P_q\ge I$，还有原完整修复能量中的匹配：
$$
\boxed{
\begin{aligned}
\lambda_q(r_q^{\rm small}-r_q^\flat)
&=\|\mathcal P_q^{-1/2}(\eta_q-\mathcal Q_q^-a)\|\\
&\le e^{-54d^4}\|w\|.
\end{aligned}
}
\tag{9.60}
$$
与真正窄通量的 (9.42) 组合，得到
$$
\boxed{
\lambda_q\!\left(
F_qS_q^\dagger\overline f-r-r_q^\flat
\right)
\le e^{-54d^4}\|w\|.
}
\tag{9.61}
$$
这将两份笔记的廉价源对齐；它没有把
$F_qS_q^\dagger\overline f$ 换成
$F_qS_q^\dagger\sigma_q=r_{\rm ret}$。

(9.50)、(9.54)—(9.57) 没有推出
$\mathcal P_q\le C\mathcal Q_q^-$ 或反向的均匀比较，也没有
推出 $\|\mathscr L_qa_q\|$ 上界。实际剩余问题是在原源上比较
这两个正形式，或进一步使用 (9.56) 中 $\overline f$ 的窄来源；
不能只凭两者正性删除原返回费用。
