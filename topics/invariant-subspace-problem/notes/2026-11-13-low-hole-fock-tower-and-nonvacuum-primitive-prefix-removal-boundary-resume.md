# 低孔远尾的精确近等距 Fock 分解与非真空原始前缀消去

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。状态：以下精确分层同构、随层数累积的范数预算及真实源小修复已证明；完整剩余能量及普通 Hilbert ISP 仍开放。

本稿接续[完整首个三维块分解](../results/R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)和[移动原始窗口](../results/R239-appendix-moving-primitive-windows-and-double-width-repair.md)。这里把后尾真空原像推广到整个低孔后尾空间。关键是一个精确交织删除算子的分层同构，并且将它与逆的全部层数损失实际付清；单独的一层 $DD^*$ 下界并不代替这一步。

## 1. 低孔纯尾和准确交换子

固定起始物理位号 $J\ge1$，写
$$
D=D_J=\sum_{j\ge J}a_jE_j,\qquad a_j=(j+1)^{-2},
$$
$$
S=S_J=\sum_{j\ge J}a_j^2,\qquad
\epsilon=\frac{a_J^2}{S}\le\frac3{J+1}.
\tag{1.1}
$$
$\mathcal H_p$ 是此后尾的恰好 $p$ 孔层，$D_p:\mathcal H_p\to\mathcal H_{p-1}$。令
$$
W_p=\left.\sum_{j\ge J}a_j^2 n_j\right|_{\mathcal H_p},
\qquad 0\le W_p\le p a_J^2 I.
$$
准确交换子给
$$
\boxed{
D_pD_p^*=D_{p-1}^*D_{p-1}+S I-2W_{p-1}.
}
\tag{1.2}
$$
约定 $D_0=0$。特别，只要 $2(p-1)\epsilon<1$，
$$
D_pD_p^*\ge S(1-2(p-1)\epsilon)I>0.
\tag{1.3}
$$
所以 $D_p$ 满射，且可取真正的最小范数右逆
$$
R_p=D_p^*(D_pD_p^*)^{-1},\qquad D_pR_p=I,\qquad
\operatorname{Ran}R_p=(\ker D_p)^\perp.
\tag{1.4}
$$
这些 $R_p$ 是逐层的 canonical 右逆；本稿不要求它们等于 R254 的另一套相容构造，也不要求裸 $D^*$ 保删除核阶。

## 2. 精确 Fock 塔

记
$$
K_0=\mathcal H_0,\qquad K_b=\ker D_b\quad(b\ge1),\qquad
\mathfrak F_p=\bigoplus_{b=0}^p K_b
$$
为外部正交直和。同一个 $K_b$ 出现在每个 $p\ge b$ 的塔层，称 $b$ 为出生层，$t=p-b$ 为链高度。

定义标准降阶
$$
\mathfrak a_p:\mathfrak F_p\to\mathfrak F_{p-1},\qquad
(k_b)_{b\le p}\longmapsto
(\sqrt{(p-b)S}\,k_b)_{b<p}.
\tag{2.1}
$$
新生的 $K_p$ 分量被杀去。定义
$$
V_p(k_0,\ldots,k_p)=
\sum_{b=0}^p
 \sqrt{(p-b)!\,S^{p-b}}\,
 R_pR_{p-1}\cdots R_{b+1}k_b.
\tag{2.2}
$$
空乘积为恒等。由于
$\mathcal H_p=K_p\oplus^\perp R_p\mathcal H_{p-1}$，逐层归纳证明每个 $V_p$ 都是有界同构。由 $D_pR_p=I$ 逐项直接得到
$$
\boxed{D_pV_p=V_{p-1}\mathfrak a_p.}
\tag{2.3}
$$
这是准确等式，未留下需要用大头逆再吸收的算子误差。

## 3. 随全部层数累积的近等距界

给定最高层数 $P\ge1$，置
$$
T_P=32(P+1),\qquad
\Delta_P=\epsilon T_P^P.
\tag{3.1}
$$
假设
$$
\boxed{\Delta_P\le\frac1{100(P+1)}.}
\tag{3.2}
$$
这也保证 (1.3) 对全部 $p\le P$ 成立。

**引理 3.1。** 在 (3.2) 下，全部 $0\le p\le P$ 同时满足
$$
\boxed{
\|V_p^*V_p-I\|\le\Delta_P,\qquad
\|V_p\|\le\sqrt{1+\Delta_P},\qquad
\|V_p^{-1}\|\le(1-\Delta_P)^{-1/2}.
}
\tag{3.3}
$$

**证明。** 写 $G_p=V_p^*V_p$。$G_0=I$。$D_1D_1^*=S I$ 使
$\sqrt S R_1$ 是等距映射，且其像正交于 $K_1$，所以 $G_1=I$。

对 $p\ge2$，在 $\mathfrak F_{p-1}$ 上令 $M_p$ 在出生分量 $K_b$ 上取值 $p-b$，故 $I\le M_p\le pI$。记
$\mathfrak a=\mathfrak a_{p-1}$、$V=V_{p-1}$、$G=G_{p-1}$。于是
$$
\mathfrak a^*\mathfrak a=S(M_p-I).
$$
令 $X=D_pD_p^*$。由 (1.2)、(2.3)，
$$
V^*XV
=\mathfrak a^*G_{p-2}\mathfrak a+SG-2V^*W_{p-1}V.
\tag{3.4}
$$
定义
$$
C_p=(SM_p)^{-1/2}(V^*XV)(SM_p)^{-1/2},\qquad
H_p=M_p^{-1/2}GM_p^{1/2}.
$$
由于 $K_p\perp R_p\mathcal H_{p-1}$，$G_p$ 相对于新生分量和旧塔的分解是块对角。其旧塔块由 (2.2) 和 $R_p^*R_p=X^{-1}$ 给出。再用
$V^*X^{-1}V=G(V^*XV)^{-1}G$，得到准确公式
$$
\boxed{(G_p)_{\rm old}=H_p^*C_p^{-1}H_p.}
\tag{3.5}
$$

设此前两个 Gram 的误差均不超过 $\delta$。由 (3.4)，
$$
\|C_p-I\|
\le2\delta+2(p-1)\epsilon(1+\delta)
\le2\delta+4P\epsilon=:a,
$$
$$
\|H_p-I\|\le\sqrt p\,\delta\le\sqrt P\,\delta=:b.
\tag{3.6}
$$
在下面的归纳中 $\delta\le\Delta_P$，(3.2) 保证 $a,b<1/4$。若
$\|C-I\|\le a$、$\|H-I\|\le b$ 且 $a,b\le1/4$，则
$$
\|H^*C^{-1}H-I\|
\le(1+b)^2\frac a{1-a}+2b+b^2
\le3a+3b.
$$
由 (3.5)--(3.6)，
$$
\|G_p-I\|
\le(6+3\sqrt P)\delta+12P\epsilon.
\tag{3.7}
$$
从 $G_0=G_1=I$ 归纳。若此前误差不超过
$\epsilon T_P^{p-1}$，则 (3.7) 和
$6+3\sqrt P+12P<T_P$ 给
$$
\|G_p-I\|\le\epsilon T_P^p.
$$
这也不超过 $\Delta_P$，故每步小量假设自洽。由正 Gram 的上下界即得 (3.3)。证毕。

将各 $V_p$ 正交直和为 $V_{\le P}$，其范数和逆范数仍分别满足 (3.3)，不会再乘层数。置
$$
\kappa_P=
\sqrt{\frac{1+\Delta_P}{1-\Delta_P}}.
\tag{3.8}
$$
这是整个有限塔的条件数上界。

这个粗界已经足够：如果 $J\asymp q$、$P=O((\log q)^{1/3})$，则
$\Delta_P=q^{-1+o(1)}$。更一般地，若
$$
P=(c+o(1))\frac{\log q}{\log\log q},\qquad 0<c<1,
$$
则 $\Delta_P\le q^{c-1+o(1)}\to0$。全部层数的累积已包含在
$[32(P+1)]^P$ 中。

## 4. 留出 s 个低孔的原始前缀

回到两个原实际边界的原线性模型
$$
L_m=A_m+D_m,\quad d=2^m,\quad
A_m^d=0,\quad\|A_m\|\le6,
$$
$$
E_m=L_m-T,\quad
\|E_m\|\le26\eta_{m-1},\quad
\eta_{m-1}\le e^{-80d^4}.
\tag{4.1}
$$
取合法 $m\ge5$、$4d\le q\le e^{d^3/4}$。任选整数
$0\le s\le q/2$，置
$$
n=q-s,\qquad J=m+2n,\qquad P=s+d-1.
\tag{4.2}
$$
令 $\mathcal P_n=P_1\cdots P_n$ 为前 $2n$ 个旧尾位上的配对原始投影，在余尾上恒等。它的前缀输入/输出恰有 $n$ 孔，且
$$
\|\mathcal P_n\|=:C_n\le e^{2/(m+1)},\qquad
D_{[m,J-1]}\mathcal P_n
=\mathcal P_nD_{[m,J-1]}=0.
\tag{4.3}
$$
令 $\iota_n$ 表示把单位原始前缀
$h_1\otimes\cdots\otimes h_n$ 补回的等距嵌入。
以下通过 $\iota_n$ 把 $\operatorname{Ran}\mathcal P_n$ 与原头及远尾空间识别。在此识别下 $L_m=A_m+D_J$。

对真正 $w\in M=\ker T$，取原正交低输出
$$
v=v_{m,q}(w),\qquad r=L_mv=A_mv_q.
$$
已有
$$
\|v-P_{\le q}^{(m)}w\|\le\delta_m\|w\|,\qquad
\delta_m=e^{-74d^4},\qquad D_m^dv=0.
\tag{4.4}
$$
记
$$
v^\circ=\mathcal P_nv,\qquad w^\circ=\mathcal P_nw.
$$
去掉固定单位原始前缀后，$v^\circ$ 只有至多 $s$ 个远尾孔，并满足
$$
P_{\le s-1}^{(J)}(A_m+D_J)v^\circ=0,\qquad
\|v^\circ-P_{\le s}^{(J)}w^\circ\|
\le C_n\delta_m\|w\|.
\tag{4.5}
$$
真实误差准确为
$$
(A_m+D_J)w^\circ=\mathcal P_nE_mw.
\tag{4.6}
$$
不假设 $\mathcal P_n$ 与实际 $T$ 交换。

以下要求 (3.2) 对 (4.2) 的 $J,P$ 成立。$V_{\le P}$ 只作用于远尾，故与原头 $A_m$ 交换，也保远尾孔次数。

## 5. 精确核延伸和原宽 d 的合法修复

把 $v^\circ$ 的远尾层 $0,\ldots,s$ 经 $V_p^{-1}$ 写入 Fock 塔。对于每个出生层 $0\le b\le s$，令 $u_b$ 是其链高度 $0$ 的头系数，属于
$H_{\rm head}\otimes K_b$。由 (4.5) 和精确交织式 (2.3)，低部递推为
$$
x_{b,t}=\frac{(-A_m)^t u_b}{\sqrt{t!\,S_J^t}}
\quad(0\le t\le s-b).
\tag{5.1}
$$
当 $t\ge d$，右边准确为零。

定义完整有限核链
$$
z_{b,t}=\frac{(-A_m)^t u_b}{\sqrt{t!\,S_J^t}}
\quad(0\le b\le s,\ 0\le t<d),
\tag{5.2}
$$
其余出生/高度坐标为零。所有远尾层都至多 $s+d-1=P$。由
$A_m^d=0$，(5.2) 在标准塔上准确满足
$(A_m+\mathfrak a)z=0$。推回原 Hilbert 空间并补上原始前缀，记作
$$
k=\iota_n(I_{\rm head}\otimes V_{\le P})z.
$$
准确有
$$
L_mk=0,\qquad P_{\le q}^{(m)}k=v^\circ.
$$
令
$$
c=v^\circ-k.
$$
于是
$$
\boxed{
L_mc=\mathcal P_nr,\qquad
c\in\operatorname{Ran}\mathcal P_n
 \cap\mathcal H_{[q+1,q+d-1]}^{(m)},\qquad
D_m^dc=0.
}
\tag{5.3}
$$
最后一式使用 $D_m^dv^\circ=0$ 及 $D_m^dk=(-A_m)^dk=0$。与全真空情形不同，这里一般不能写 $D_mv^\circ=0$。

## 6. 真实未来层支付整个核延伸

令 $y=V_{\le P}^{-1}P_{\le P}^{(J)}w^\circ$。把 (4.6) 的低输出也经
$V^{-1}$ 转换为 $e$，则在全部可用的出生/高度坐标上
$$
A_my_{b,t}+\sqrt{(t+1)S_J}\,y_{b,t+1}=e_{b,t},
$$
$$
\|e\|\le(1-\Delta_P)^{-1/2}
           26 C_n\eta_{m-1}\|w\|
\le52C_n\eta_{m-1}\|w\|.
\tag{6.1}
$$
这里只使用远尾输出层 $0,\ldots,P-1$，其输入层仍在精确塔的范围内。

记 $\mathfrak R$ 为标准塔中保留 $b\le s$、$0\le t<d$ 的正交投影。若用真正 $y_{b,0}$ 代替 (5.2) 的初始数据，则反复使用 (6.1) 给
$$
y_{b,t}
=\frac{(-A_m)^t y_{b,0}}{\sqrt{t!\,S_J^t}}
 +\sum_{j=0}^{t-1}
 (-A_m)^{t-1-j}
 \sqrt{\frac{j!}{t!}}\,
 S_J^{-(t-j)/2}\,e_{b,j}.
\tag{6.2}
$$
各出生层是外直和；同一个 $e_{b,j}$ 只通过这一有限三角矩阵计入。其算子范数至多
$$
\Gamma_d=d\,6^d S_J^{-d/2}.
\tag{6.3}
$$
这可直接用每个矩阵条目的上界
$6^dS_J^{-d/2}$ 及行列各至多 $d$ 项的 Schur 界证明，不付出生层数 $s$。

从初始数据到 (5.2) 完整链的算子范数也至多 $\Gamma_d$。由 (4.5) 和 (3.3)，全部出生初始数据的误差满足
$$
\left(\sum_{b=0}^s\|u_b-y_{b,0}\|^2\right)^{1/2}
\le2C_n\delta_m\|w\|.
\tag{6.4}
$$
这是一次正交坐标抽取，没有 $\sqrt{s}$。

在 (4.2) 的范围中 $J+1\le3q$、$S_J\ge[3(J+1)^3]^{-1}$，故
$$
\Gamma_d\le d\,54^d q^{3d/2},\qquad
\log\Gamma_d
\le\log d+d\log54+\frac38d^4\le d^4.
\tag{6.5}
$$
结合 (4.1)、(6.1)--(6.5)，得到
$$
\|z-\mathfrak R y\|
\le2C_n\Gamma_d(26\eta_{m-1}+\delta_m)\|w\|.
\tag{6.6}
$$
经 $V_{\le P}$ 推回后，其范数不超过
$$
C_n e^{-72d^4}\|w\|.
\tag{6.7}
$$
常数 $4(26+1)$ 被 $d\ge32$ 的剩余指数余量吸收。

现在 $c$ 是 $-k$ 的远尾 $s+1,\ldots,P$ 部分。
$\mathfrak R$ 与远尾层投影交换，$V_{\le P}$ 也保远尾层。因此
$$
\|P_{[s+1,P]}^{(J)}
   V_{\le P}\mathfrak R V_{\le P}^{-1}w^\circ\|
\le\kappa_P C_n
 \|P_{[q+1,q+d-1]}^{(m)}w\|.
$$
结合 (6.7)，得到
$$
\boxed{
\|c\|\le
\kappa_P C_n\,
 \|P_{[q+1,q+d-1]}^{(m)}w\|
 +C_ne^{-72d^4}\|w\|.
}
\tag{6.8}
$$
这是原宽 $d$ 内、原 Hilbert 范数中的真实源修复，不借助更高的未控制尾部。

## 7. 可留出的剩余孔数远大于 d

沿原全部整数头长
$$
m(q)=\max\left\{5,
 \left\lceil\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right\},
\qquad d(q)=2^{m(q)}
$$
取任意固定 $0<c_0<1$，并对充分大的 $q$ 令
$$
s(q)=\left\lfloor
 c_0\,\frac{\log q}{\log\log q}
 \right\rfloor,\qquad n(q)=q-s(q).
\tag{7.1}
$$
此时 $s(q)\le q/2$，$d(q)=o(s(q))$，
$$
J=m(q)+2n(q)\sim2q,\qquad
P=s(q)+d(q)-1=(c_0+o(1))
                  \frac{\log q}{\log\log q}.
$$
由 (1.1)、(3.1)，
$$
\Delta_P\le q^{c_0-1+o(1)}\longrightarrow0.
\tag{7.2}
$$
因此 (3.2) 最终成立，并且 $C_n\to1$、$\kappa_P\to1$。从 (6.8)，对每个真正 $w\in M$，
$$
\boxed{
\|c_q\|\le(1+o(1))\tau_q(w)
             +e^{-71d(q)^4}\|w\|
\longrightarrow0.
}
\tag{7.3}
$$
这里 $\tau_q$ 为原全部孔尾，包含旧尾次数大于 $q$ 的部分。

故现在可以无权消去整个
$\mathcal P_{q-s(q)}r_q$ 分量。这一投影只固定前
$q-s(q)$ 个配对原始块，之后的整个尾空间保持自由；对局部源允许
$s(q)$ 个非真空剩余孔。没有将它重新限制成一个全真空秩一块。

## 8. 对完整首个三维分解的直接含义

使用前稿在前 $q$ 个相邻块上的完整分解
$$
I=T_\infty+\sum_{i=1}^qT_i.
$$
其准确望远镜关系给
$$
\mathcal P_{q-s}
=T_\infty+\sum_{i=q-s+1}^qT_i.
\tag{8.1}
$$
本稿 $c_q$ 位于 $\operatorname{Ran}\mathcal P_{q-s}$，所以
$T_ic_q=0$ 对 $i\le q-s$。把 $c_q$ 施加完整分解的分析界，并用各受限分支最小值 $\mu_i^{[h]}$ 的定义，得到
$$
\boxed{
\mu_\infty^{[h]}(r_q)^2+
\sum_{i=q-s(q)+1}^q\mu_i^{[h]}(r_q)^2
\le A_q^2\|c_q\|^2\longrightarrow0
\quad(h\ge d(q)).
}
\tag{8.2}
$$
这里同一个 $A_q=1+O(m(q)^{-1/2})$ 一次控制全部这些分支，没有额外
$\sqrt{s(q)}$。因此完整能量比较中，整个末段增长窗口都可删除。

同样，对原宽 $d$ 或明确定义的双宽 $2d$ 最小修复算子
$F_h^\dagger$，由线性与最小性，
$$
\left|
\|F_h^\dagger r_q\|-
\|F_h^\dagger(I-\mathcal P_{q-s(q)})r_q\|
\right|
\le\|c_q\|\longrightarrow0.
\tag{8.3}
$$
剩余的早期三维分支之和仍未得到足以触发全整数倒数发散准则的上界。
本稿已支付远尾近 CCR 结构的全部层数累积、原始出生层分解、真实进位和低投影微调，但没有控制这些更早分支的完整最小能量，也没有把逐分支真实方程当作逐分支缺陷正交性。
无权 $N=M$、真实头跃迁通量及普通 Hilbert ISP 继续开放。
