# R239 附录：单高块 primitive 三角带的真正源图支付

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本稿证明一个包含全部首源头的新闭源旗满足常数接近 $1/2$ 的原两费用比较，并给出合法的 $M$ 正交投影与真实源运输。它保留全部实际头、原尾、原平坦源和图交叉块。未覆盖的三角上角及带外头方向明确保留；普通 ISP 与边界 $N=M$ 仍为 OPEN。

本稿直接使用[单 dyadic 块导数交织稿](R239-appendix-single-dyadic-block-derivative-intertwiner-and-exact-jet-anchor.md)中已经完整支付的算子、联合旗和修正。它不再只估计低锚单独的费用，而是一次支付“全首源头加单高块图”的真实源子空间。

## 1. 原空间与全部参数

固定
$$
m\ge5,\qquad d=2^m,\qquad
4d\le q\le e^{d^3/4},
$$
$$
p=d/2,\qquad s=m-1,\qquad
K=2^r,\quad 2\le r\le m-2.
\tag{1.1}
$$
特别 $4\le K\le d/4$。$A=A_m,D=D_m$ 均为原实际算子，所有头和孔层使用原物理内积。

源空间是
$$
\mathscr R_q
=\bigoplus_{j=0}^{d-2}e_jE_{d-j-1,q}.
$$
沿用完整左最小逆、裸与完整右费用：
$$
L=J_q^{-1},\qquad B=J_{b,q}^{-1},\qquad G=G_q,
$$
$$
\mu(r_0)^2=\langle Lr_0,r_0\rangle,\quad
\alpha(r_0)^2=\langle Br_0,r_0\rangle,\quad
\lambda(r_0)^2=\langle G^{-1}r_0,r_0\rangle,
$$
$$
c^\flat(r_0)=F_{\rm flag}^*Lr_0,\qquad
\lambda_{\rm flat}(r_0)^2
=\|c^\flat(r_0)\|^2=\langle LGLr_0,r_0\rangle.
\tag{1.2}
$$
真正两费用为
$$
M=B+LGL,\qquad
\chi(r_0)^2=\alpha(r_0)^2+\lambda_{\rm flat}(r_0)^2.
\tag{1.3}
$$

完整强制 primitive 坐标及其逆记为
$$
\Gamma_q:\mathscr R_q\overset{\sim}{\longrightarrow}\mathscr U_q,
\qquad B_U=\Gamma_q^{-1},
$$
$$
\mathscr U_q
=\bigoplus_{t=0}^{d-2}H_{\ge t+1}\otimes K_{q-t}.
\tag{1.4}
$$
完整自由变量消元后的左 Gram 为 $\mathcal G_q\succeq I$，因此
$$
\mu(r_0)^2
=\langle\mathcal G_q\Gamma_qr_0,\Gamma_qr_0\rangle
\ge\|\Gamma_qr_0\|^2.
\tag{1.5}
$$

令 $P$ 为物理首源头投影，$Q=I-P$。首头稿证明
$$
[B,P]=[G,P]=0,\qquad B|_{P\mathscr R_q}=W,\quad
G|_{P\mathscr R_q}=W^{-1}.
\tag{1.6}
$$
其坐标像为完整最小头对角
$$
\boxed{
\Delta=\Gamma_q(P\mathscr R_q)
=\bigoplus_{t=0}^{d-2}\mathbb Ce_{t+1}\otimes K_{q-t}.
}
\tag{1.7}
$$
这里 $\Delta$ 包含全部允许的短核阶，并不是只有顶层 primitive。

## 2. 单高块给出的已付源图

模型完整核空间为
$$
\mathscr Z=\ker(A_r+D_m)\cap
\bigl(H_K\otimes P_{\le q}\mathcal H^{(m)}\bigr).
\tag{2.1}
$$
单高块稿构造了实际
$$
H^\partial=U_p-b_sB_{m,r},
$$
其中 $B_{m,r}$ 使用加宽到 $2K$ 的真实 Jordan 相似和数值升阶算子；包含最后一列所需的 $e_K$，不是在 $K$ 内虚构导数交换子。

同稿的正规化相容修正给
$$
\mathcal C_L:\mathscr Z\to P_{\le q}H,\qquad
\mathcal C_R:\mathscr Z\to\ker S_{\rm flag},
$$
$$
P_0\mathcal C_L=0,\qquad
\|\mathcal C_L\|,\|\mathcal C_R\|
\le\varepsilon,\qquad
\varepsilon\le e^{-9d^4/2}.
\tag{2.2}
$$
全部右链都在原完整联合旗内。对于 $z\in\mathscr Z$，定义
$$
s_z=F_{\rm flag}\mathcal C_Rz,\qquad
a_{\rm hi}(z)=P_{\mathscr U_q}U_pP_0z,\qquad
a_{\rm anc}(z)=P_{\mathscr U_q}B_{m,r}P_0z.
$$
准确有
$$
\boxed{
\Gamma_qs_z=a_{\rm hi}(z)-b_sa_{\rm anc}(z),\qquad
a_{\rm anc}(z)\in\Delta.
}
\tag{2.3}
$$
锚实际上只用 $\Delta$ 的前 $K$ 个孔位置，但下面允许完整 $\Delta$。

因为 $\mathcal C_Rz$ 是源 $s_z$ 的真实完整可行右链，
$$
\boxed{\lambda(s_z)\le\varepsilon\|z\|.}
\tag{2.4}
$$
没有把物理 $B_{m,r}z$ 当成左可行向量；(2.3)–(2.4) 仅使用已经构造的准确源和完整右链。

## 3. 被观察的高块范围及必须删掉的对角

模型 primitive 坐标 $p_z=P_0z$ 的第 $q-t$ 孔层满足
$$
(p_z)_{q-t}\in\ker A_r^{t+1}
=\operatorname{span}\{e_0,\ldots,e_{\min(t,K-1)}\}.
\tag{3.1}
$$
移到高块后，$e_i$ 成为 $e_{p+i}$；落在强制坐标中的条件又是
$p+i\ge t+1$。因此高坐标的准确可能范围为
$$
0\le i<K,\qquad i\le t\le p+i-1.
\tag{3.2}
$$
最下端 $t=p+i-1$ 恰为 $\Delta$。为了保留可由 $\Gamma_qr_0$ 直接读取的正交分量，定义
$$
\boxed{
\mathscr A_{p,K,q}
=\bigoplus_{i=0}^{K-1}\ \bigoplus_{t=i}^{p+i-2}
\mathbb Ce_{p+i}\otimes K_{q-t}.
}
\tag{3.3}
$$
它是 $\mathscr U_q$ 的闭子空间，且
$$
\mathscr A_{p,K,q}\perp\Delta.
\tag{3.4}
$$
孔层下端至少为 $q-p-K+3>0$，所有旗及尾核都在原合法范围。

这条带不包含 $t<i$ 的上角。对于头 $j=p+i$，它覆盖的恰为
$$
i\le t\le j-2;
$$
$t=j-1$ 已由完整首源头支付，$0\le t<i$ 尚未被本稿支付。

## 4. 每个带坐标的真实模型核选择

任取 $a\in\mathscr A_{p,K,q}$。将其平移回模型低头，记
$$
p_a=U_p^*a.
$$
按 (3.3)，它满足 (3.1)，且 $\|p_a\|=\|a\|$。

使用原尾的正规化 primitive 顺次 MP 族，定义
$$
\boxed{
z_a=\sum_{j=0}^{K-1}(-A_r)^jQ_jp_a.
}
\tag{4.1}
$$
这里按孔层作用：$Q_j$ 增加 $j$ 个孔，$A_r^j$ 只作用模型头；两者交换。

每个非零输入 $e_i f\subset(p_a)_{q-t}$ 满足 $i\le t$。若 $A_r^je_i\ne0$，则 $j\le i\le t$，所以输出孔数 $q-t+j\le q$。因此 (4.1) 确在 $P_{\le q}$，不存在未付的顶层截断误差。

由 $DQ_j=Q_{j-1}$、$DP_0=0$，相邻项准确相消，最后项由 $A_r^K=0$ 消失，所以
$$
(A_r+D_m)z_a=0,\qquad P_0z_a=p_a.
\tag{4.2}
$$
因此 $z_a\in\mathscr Z$，并且
$$
a_{\rm hi}(z_a)=a.
\tag{4.3}
$$
这给出整个闭带 (3.3) 的有界线性选择，没有使用任意核投影与逆的交换。

为给出统一账本，在高孔笔记 §14 取共同输出孔数上界 $P=q$、最大原像阶 $T=K-1$。可用共同常数为
$$
\mathcal L=512\sqrt{q+K}\,(m+q+K)^{3/2}
\le2048q^2.
\tag{4.4}
$$
每个实际非零 $Q_j$ 输入都在 $\mathcal H_{\le q-j}$，故
$\|Q_j\|\le2^{j-1}\mathcal L^j$ 合法适用。原 $\|A_r\|\le6$ 给
$$
\|z_a\|
\le\left(1+\frac12\sum_{j=1}^{K-1}(12\mathcal L)^j\right)\|a\|
\le\mathcal T\,\|a\|,
$$
$$
\boxed{\mathcal T=K(12\mathcal L)^{K-1}.}
\tag{4.5}
$$

令
$$
s(a)=F_{\rm flag}\mathcal C_Rz_a.
$$
则
$$
\boxed{
\Gamma_qs(a)=a-b_sa_{\rm anc}(z_a),\qquad
a_{\rm anc}(z_a)\in\Delta,\qquad
\lambda(s(a))\le\delta\|a\|,
}
\tag{4.6}
$$
其中
$$
\delta=\varepsilon\mathcal T.
\tag{4.7}
$$
这一步没有估计锚单独的裸费，也不需要先把图空间换成物理高块。

## 5. 在原全窗口核对 δ

由 (4.4) 及 $\log24576<11$，
$$
\begin{aligned}
\log\mathcal T
&\le\log K+(K-1)\bigl(\log24576+2\log q\bigr)\\
&\le\frac18d^4+\frac{11}{4}d+\log d\\
&\le\frac18d^4+4d
\le\frac17d^4.
\end{aligned}
\tag{5.1}
$$
最后两步用 $d\ge32$、$\log d\le d/2$ 和 $4d\le d^4/56$。所以
$$
\boxed{
\delta\le e^{-61d^4/14}\le e^{-4d^4}<1.
}
\tag{5.2}
$$
指数中保留了模型全核重建的全部 $K$ 阶费用；没有把 $p_a$ 的范数误当成 $z_a$ 的范数。

## 6. 全首源头加高块图的准确闭源旗

定义
$$
\boxed{
\mathscr X_{p,K,q}
=\Gamma_q^{-1}\bigl(\Delta\oplus\mathscr A_{p,K,q}\bigr).
}
\tag{6.1}
$$
由于 $\Gamma_q$ 为固定参数下的有界同构，它是原源空间中的闭子空间。

由 (4.6) 及 $\Gamma_q^{-1}\Delta=P\mathscr R_q$，
$$
\mathscr X_{p,K,q}
=P\mathscr R_q+\operatorname{Ran}s.
\tag{6.2}
$$
和式在源坐标中是一个真实带低锚的图；这里没有声称两个源子空间在 $B,G,L$ 或 $M$ 中正交。

任取 $r_0\in\mathscr X_{p,K,q}$。唯一的带分量为
$$
a=P_{\mathscr A_{p,K,q}}\Gamma_qr_0.
\tag{6.3}
$$
由于 (3.4)、(4.6)，
$$
r_0-s(a)\in P\mathscr R_q,\qquad Qr_0=Qs(a).
\tag{6.4}
$$
同时 (1.5) 给 $\|a\|\le\mu(r_0)$。因为 $Q$ 约化 $G^{-1}$，(4.6) 因而给
$$
\boxed{
\lambda(Qr_0)\le\lambda(s(a))
\le\delta\|a\|\le\delta\mu(r_0).
}
\tag{6.5}
$$
这是实际全右最小费用的上界，来自真正可行的右链。它没有更换原 $r_0$ 的平坦源。

## 7. 全部左交叉项均保留的两费用估计

记
$$
\alpha_0=\|W^{1/2}Pr_0\|,\qquad
\lambda_0=\|G^{1/2}PLr_0\|,\qquad
\lambda_1=\|G^{1/2}QLr_0\|.
\tag{7.1}
$$
由 (1.6)，$\alpha_0\le\alpha(r_0)$，并且
$$
\lambda_0^2+\lambda_1^2=\lambda_{\rm flat}(r_0)^2.
\tag{7.2}
$$
将 $\langle r_0,Lr_0\rangle$ 仅按物理源头拆开，完整 $Lr_0$ 从未被截断或替换。Cauchy 与 (6.5) 给
$$
\begin{aligned}
\mu(r_0)^2
&=\langle Pr_0,PLr_0\rangle
 +\langle Qr_0,QLr_0\rangle\\
&\le\alpha_0\lambda_0+
 \lambda(Qr_0)\lambda_1\\
&\le\alpha_0\lambda_0+
 \delta\mu(r_0)\lambda_1.
\end{aligned}
\tag{7.3}
$$
因此所有真实左交叉块都保存在同一个 $Lr_0$ 中，没有要求 $P$ 约化 $L$。

若 $\mu(r_0)>0$，除以 $\mu(r_0)^2$，设
$x=\alpha_0/\mu$、$y=\lambda_0/\mu$、$z=\lambda_1/\mu$。有
$1\le xy+\delta z$，故
$$
\frac{\chi(r_0)^2}{\mu(r_0)^2}
\ge x^2+y^2+z^2
\ge2\max(1-\delta z,0)+z^2.
$$
当 $0\le\delta\le1$，右侧在 $z=\delta$ 处的最小值是 $2-\delta^2$；在 $z\ge1/\delta$ 的另一区间，最小值 $\delta^{-2}$ 不更小。$\delta=0$ 按连续值读取。因此
$$
\boxed{
\mu(r_0)^2
\le c_\delta\,\chi(r_0)^2,\qquad
c_\delta=\frac1{2-\delta^2},
\quad r_0\in\mathscr X_{p,K,q}.
}
\tag{7.4}
$$
结合 (5.2)，
$$
\frac12\le c_\delta
\le\frac1{2-e^{-8d^4}}<1.
\tag{7.5}
$$
这是原同一个源的两费用估计；不是给测试族单独的观测式后再假设一个未证的全图框架。

## 8. 真正 M 投影与实际来源运输

取 $\mathcal P_{\mathscr X}^{M}$ 为在完整正度量 $M=B+LGL$ 中到 (6.1) 的正交投影。对任意原源 $r$，写
$$
r_{\mathscr X}=\mathcal P_{\mathscr X}^{M}r,\qquad
\widehat r=r-r_{\mathscr X}.
$$
固定参数下这个投影有界，因为 $M$ 有界严格正。准确有
$$
\chi(r)^2=\chi(r_{\mathscr X})^2+\chi(\widehat r)^2,
\qquad
\widehat r\perp_M\mathscr X,
$$
$$
\boxed{
\mu(r_{\mathscr X})\le\sqrt{c_\delta}\,\chi(r),\qquad
\chi(\widehat r)\le\chi(r).
}
\tag{8.1}
$$

若原实际来源满足
$$
v_m=E_{q_m}^\dagger r_m\longrightarrow w,\qquad
\chi(r_m)\longrightarrow0,
$$
则同一个已付线性修正给
$$
\boxed{
E_{q_m}^\dagger\widehat r_m\longrightarrow w,\qquad
\chi(\widehat r_m)\longrightarrow0,\qquad
\widehat r_m\perp_{M_m}\mathscr X_{p_m,K_m,q_m}.
}
\tag{8.2}
$$
因为 $c_{\delta_m}<1$，这里不需另加任何随 $m$ 增长的预算。原物理强收敛、强制 primitive 坐标趋零等结论仍可依法应用于修正后的真实源。

但是 $\widehat r\perp_M\mathscr X$ 并不等于
$P_{\mathscr A}\Gamma_q\widehat r=0$。准确剩余条件为
$$
\boxed{
P_{\Delta\oplus\mathscr A}
\,\Gamma_q^{-*}M\,\widehat r=0.
}
\tag{8.3}
$$
或用 $\widehat a=\Gamma_q\widehat r$ 写成
$$
P_{\Delta\oplus\mathscr A}
\bigl(\mathcal F+\mathcal G_q\mathcal H_q\mathcal G_q\bigr)
\widehat a=0,
\tag{8.4}
$$
其中 $\mathcal F=B_U^*BB_U$、$\mathcal H_q=\Gamma_qG\Gamma_q^*$。
所有图交叉项均保留。

若剩余 $M$ 正交图上另证
$\mu(\widehat r)^2\le C_{\rm rem}\chi(\widehat r)^2$，三角不等式再作二元 Cauchy 给原全源常数至多 $C_{\rm rem}+c_\delta$。本稿没有预设这个剩余比较。

## 9. 准确覆盖与后续边界

本稿同时支付：

1. 所有物理首源头，即坐标 $\Delta$ 的全部尾短核阶；
2. 高头 $p+i$、$0\le i<K$ 上的 primitive 带 $i\le t\le p+i-2$，但以 (6.1) 的完整源旗和 (8.3) 的真实图条件读取。

它没有支付：

- 同一高头的 $0\le t<i$ 上角；
- 高头带 $[p,p+K)$ 以外、且不在 $\Delta$ 的 primitive 坐标；
- 把 (8.3) 简化成上述物理或 primitive 分量为零所需的额外 Schur 控制；
- 未证明的多高位块主耦合，或其它 $p$ 上与 (2.2) 相同的误差界。

可以把 (3.3) 与另外已经证明的孔带定位作集合交叉，但必须先辨明后者控制的是物理输出、primitive 坐标还是 $M$ 图残余。它们不是可直接互换的投影。本稿不以三角带覆盖图代替这些转换证明。
