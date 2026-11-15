# 第二物理头的真实一孔 Schur 校正与两列联合恢复

日期：2026-11-15。作者：literature_audit / 789f。

**状态：已证明的同源恒等式及明确正性范围。** 本稿用原尾完整 $DD^*$ 的真实一孔 Schur 补，将第二物理头恢复式中的 primitive 占据残量准确吸收入同一校正列。得到 $Du$、$D^2u$、$\|u\|^2$ 的完整公式，以及原 source、零源块和物理 gap 上同一两列式。

这没有支付两个变换列的联合远孔预算。消去裸残量不是原源已趋零，也不是 $N=M$ 或普通 Hilbert ISP 已完成。

接口：[固定头 Euler 与完整 inverse-gauge 列](2026-11-14-fixed-physical-head-euler-feedback-and-inverse-gauge-joint-column-budget-789f-next.md)、[第一物理头准确恢复与同 gap 缩放](2026-11-15-first-physical-head-exact-gauge-recovery-and-same-gap-scaling-789f-next.md)、[原 first-head joined 商 Gram](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、[同一物理 gap 的内在切口耗散](2026-11-14-same-physical-gap-intrinsic-cut-dissipation-and-fixed-test-pairing-789f-next.md)。

## 1. 原物理空间、权与低头记号

固定原 $N/Y$ 头 $A=A_m$，$d=2^m$，原尾
$$
 D=D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2}.
$$
$E_j$ 是物理平方自由删除，$\Omega$ 是尾真空。以下每个伴随和正交补都相对于原物理 Hilbert 内积。取 $m\ge11$；本稿给出的同源恒等式实际上只要求下文的逆存在。

记
$$
 S=\sum_{j\ge m}b_j^2,\qquad
 s_2=\sum_{j\ge m}b_j^4,\qquad
 s_3=\sum_{j\ge m}b_j^6,\qquad
 z_*=\max_{j\ge m}b_j^2,
$$
以及
$$
 \varepsilon=S^2-s_2,\qquad
 \mathbf b=D^*\Omega=\sum_{j\ge m}b_je_j.
\tag{1.1}
$$
这里 $\varepsilon$ 是标量，不是一个未付误差。由于尾有至少两个正权，$\varepsilon>0$。

在一孔层 $\mathcal H_1\simeq\ell^2(\{m,m+1,\ldots\})$ 中，置
$$
 Z=\operatorname{diag}(b_j^2),\qquad
 K=\mathbf b^\perp=\ker D|_{\mathcal H_1},\qquad
 P=P_K,
$$
$$
 r=Z\mathbf b-\frac{s_2}{S}\mathbf b\in K.
\tag{1.2}
$$
于是
$$
 \|r\|^2=s_3-\frac{s_2^2}{S}.
\tag{1.3}
$$

原加权后移的物理权为 $W_0=1$、$B_me_i=(W_i/W_{i-1})e_{i-1}$。原头满足
$$
 Ae_0=0,\qquad Ae_1=e_0,\qquad
 Ae_2=\alpha e_1+\beta e_0,
$$
$$
 \alpha=\frac{W_2}{W_1^2}>0.
\tag{1.4}
$$
$\beta$ 保留实际 $N/Y$ 头的值；不改成理想 Jordan 头。于是
$$
 c_1=\frac{e_2-\beta e_1}{\alpha},\qquad Ac_1=e_1.
\tag{1.5}
$$

## 2. 完整一孔 Gram 及其真实 Schur 补

从实际平方自由坐标直接计算
$$
 F_1=DD^*|_{\mathcal H_1}
    =S I-2Z+\mathbf b\mathbf b^*.
\tag{2.1}
$$
对角项是 $S-b_i^2$，不同坐标 $i,j$ 的项是 $b_ib_j$，所以 (2.1) 没有压缩后换逆。

定义真实 $K$ 块
$$
 H=P(SI-2Z)|_K=P F_1|_K.
\tag{2.2}
$$
它不是此前 primitive 压缩逆的替代；本节将完整 $F_1$ 相对
$\mathbb C\mathbf b\oplus K$ 作一次准确 Schur 消去。

令
$$
 \delta=\frac{z_*}{S}.
$$
原尾积分界给
$$
 S\ge\frac1{3(m+1)^3},\qquad
 z_*=(m+1)^{-4},\qquad
 \delta\le\frac3{m+1}\le\frac14
 \quad(m\ge11).
\tag{2.3}
$$
因此
$$
 F_1\succeq(S-2z_*)I,\qquad
 H\succeq(S-2z_*)I\succeq \frac S2 I.
\tag{2.4}
$$
所有本节逆都是有界真逆。置
$$
 v=H^{-1}r,\qquad
 R=\langle r,H^{-1}r\rangle\ge0,\qquad
 D_0=\varepsilon-2R.
\tag{2.5}
$$

由于 $v\perp\mathbf b$，完整 $F_1$ 的两个实际块给
$$
 F_1\mathbf b=\frac{2\varepsilon}{S}\mathbf b-2r,
 \qquad
 F_1v=r-\frac{2R}{S}\mathbf b.
\tag{2.6}
$$
第一式由 (2.1) 直接得到。第二式的 $K$ 分量是 $Hv=r$；
其 $\mathbf b$ 分量由
$\langle \mathbf b,F_1v\rangle=\langle F_1\mathbf b,v\rangle=-2R$
得到。因此
$$
 \boxed{F_1(\mathbf b+2v)=\frac{2D_0}{S}\mathbf b.}
\tag{2.7}
$$
这是完整 $F_1$ 的 Schur 身份；不能把 $F_1^{-1}$ 预先换成 $H^{-1}$。

其正性还可以定量写出。由 $s_2\le z_*S$、$s_3\le z_*^2S$，
$$
 \varepsilon\ge(1-\delta)S^2,\qquad
 R\le\frac{\|r\|^2}{S-2z_*}
   \le\frac{\delta^2S^2}{1-2\delta}.
$$
故
$$
 \frac{2R}{\varepsilon}
 \le\frac{2\delta^2}{(1-2\delta)(1-\delta)}
 \le\frac13,
$$
以及
$$
 \boxed{\frac{S^2}{2}\le D_0\le\varepsilon\le S^2.}
\tag{2.8}
$$
最后一个中间上界使用 $R\ge0$。特别，$D_0$ 的分母在本稿范围中严格正，不靠数值检验。

## 3. 校正后的同一个二孔向量

定义
$$
 u=D^*(\mathbf b+2v)\in\mathcal H_2.
\tag{3.1}
$$
(2.7) 立即给
$$
 \boxed{
 Du=\frac{2D_0}{S}\mathbf b,\qquad
 D^2u=2D_0\Omega,\qquad
 D^3u=0.
 }
\tag{3.2}
$$
范数也由同一个完整 Gram 精确计算：
$$
 \begin{aligned}
 \|u\|^2
 &=\langle \mathbf b+2v,F_1(\mathbf b+2v)\rangle\\
 &=\frac{2D_0}{S}\langle \mathbf b+2v,\mathbf b\rangle
 =2D_0.
 \end{aligned}
$$
所以
$$
 \boxed{\|u\|^2=2D_0.}
\tag{3.3}
$$
还可写成真正一次最小原像
$$
 u=\frac{2D_0}{S}\,D^*F_1^{-1}\mathbf b
   =\frac{2D_0}{S}\,D^\dagger\mathbf b.
\tag{3.4}
$$
这里 $D^\dagger$ 仅指 $\mathcal H_2\to\mathcal H_1$ 这一完整层的 MP 逆。它不是 $(D^2)^\dagger$，也不是无限全孔删除逆。

校正前的准确式是
$$
 D(D^*)^2\Omega
 =\frac{2\varepsilon}{S}\mathbf b-2r.
\tag{3.5}
$$
(3.1) 正是用同一 $v=H^{-1}r$ 消去 (3.5) 的 primitive 分量；校正同时改变标量为 $D_0$，所以不得只加向量而仍沿用 $\varepsilon$。

## 4. 真低层核列及完整环境身份

固定任何有限切口 $q\ge2$。使用原 first-head joined 参数化 $T$，其第一物理头为恒等，$\Gamma=T^*T\succeq I$。由于 $\mathcal H_2\subset\ker D^d$ 且整个次数二输入在左侧，实际商删除在此没有损失。对任意 $z\in\mathcal H_2$，
$$
 Tz=e_0\otimes z-e_1\otimes Dz+c_1\otimes D^2z.
\tag{4.1}
$$
该向量是真实 $(A+D)$ 核，支撑于尾孔数不超过二。

令
$$
 f_j=e_j\otimes\Omega,\qquad
 h_2=\frac{(A^*)^2e_0\otimes\Omega}{W_2},
 \qquad
 h_{21}=\frac{W_1}{W_2}(A^*e_1)\otimes\Omega,
$$
再定义
$$
 h_{1,v}=\frac{A^*e_0\otimes v}{W_1},\qquad
 \widetilde h_2=h_2-\frac{2W_1}{W_2}h_{1,v},\qquad
 z=\frac{u}{W_2}.
\tag{4.2}
$$
$h_{21}$ 是对 $f_2$ 的一次 inverse-gauge 列，$h_2$ 是其两次列；
$h_{1,v}$ 与它们使用同一个原尾及同一个 $v$，不是另选测试源。

由 (3.2)、(4.1)，
$$
 Tz=\frac1{W_2}
 \left[e_0\otimes u-\frac{2D_0}{S}e_1\otimes\mathbf b
                    +2D_0c_1\otimes\Omega\right].
\tag{4.3}
$$
记 $C=A+D$，作用于原头尾张量空间。令
$$
 \eta=\frac1{W_2}
 \left[e_0\otimes(\mathbf b+2v)
       -(A^*e_0)\otimes\Omega-\frac{2D_0}{S}f_1\right].
\tag{4.4}
$$
则有完整环境恒等式
$$
 \boxed{
 Tz=\widetilde h_2
       +\frac{2D_0}{SW_1}h_{21}
       +\frac{2D_0}{\alpha W_2}(f_2-\beta f_1)
       +C^*\eta.
 }
\tag{4.5}
$$
证明只用 $A^*$ 与 $D^*$ 对易：
$$
 (A^*+D^*)(D^*-A^*)=(D^*)^2-(A^*)^2,
$$
以及 $e_1\otimes\mathbf b=C^*f_1-(A^*e_1)\otimes\Omega$。
代入 (4.4) 后，所有头与尾项逐项恢复 (4.3)。

$\eta$ 的尾孔支撑不超过一。故对 $q\ge2$，$C^*\eta$ 在原 joined 低输出关系的正交补中：这使用真正保留的低输出方程，不假设 joined 核在所有高输出上也是真核。

## 5. 原 $\Gamma$、源块和零源块中的同一公式

在次数二无商损失的范围，原真核方程给
$$
 T^*h_2=\frac{(D^*)^2\Omega}{W_2},
 \qquad
 T^*h_{1,v}=-\frac{D^*v}{W_1}.
$$
所以
$$
 \boxed{T^*\widetilde h_2=z.}
\tag{5.1}
$$
将 $T^*$ 作用于 (4.5)，得到准确输入 Gram 身份
$$
 \boxed{
 \Gamma z-z
 =\frac{2D_0}{SW_1}T^*h_{21}
  +\frac{2D_0}{\alpha W_2}T^*(f_2-\beta f_1).
 }
\tag{5.2}
$$

保原全部零源空间 $\mathcal C=\ker\mathcal B$、欧氏补 $\mathcal U$，以及
$$
 B_0=\Gamma_{CC}^{-1}\Gamma_{CU},\qquad
 R_{\mathcal U}x=(-B_0x,x),\qquad
 \mathcal S=R_{\mathcal U}^*\Gamma R_{\mathcal U},
$$
$$
 I_C=T|_{\mathcal C}\Gamma_{CC}^{-1/2},
 \qquad I_U=TR_{\mathcal U}\mathcal S^{-1/2}.
\tag{5.3}
$$
这些是原完整零源和同源最小 joined 源的正交物理等距。$z\in\mathcal C$，而 $Tz$ 是左零源真核列。

对任何物理向量 $g$，记
$$
 b(g)=I_U^*g,\qquad c(g)=I_C^*g.
$$
(4.5) 给
$$
 \boxed{
 b(\widetilde h_2)+\frac{2D_0}{SW_1}b(h_{21})
       +\frac{2D_0}{\alpha W_2}
                      [b(f_2)-\beta b(f_1)]=0.
 }
\tag{5.4}
$$
同时零源块没有被删除：
$$
 \boxed{
 c(\widetilde h_2)+\frac{2D_0}{SW_1}c(h_{21})
       +\frac{2D_0}{\alpha W_2}
                      [c(f_2)-\beta c(f_1)]
 =\Gamma_{CC}^{1/2}z.
 }
\tag{5.5}
$$
例如 (5.1) 还明确识别了真正源列
$$
 b(\widetilde h_2)
 =-\mathcal S^{-1/2}\Gamma_{UC}\Gamma_{CC}^{-1}z.
\tag{5.6}
$$
因此 (5.4) 保留了完整 $\Gamma_{CC}^{-1}$ 后的低 forcing 传播，没有把它换成一个未经支付的压缩逆。

## 6. 同一物理 gap 上的准确恢复

使用原物理 joined 子空间
$$
 \mathcal M_q=\ker(Q_{\mathrm{lo},q}C),
 \qquad
 G_q=P_{\mathcal M_q}-P_{\mathcal K_{q+d}},
$$
其中 $\mathcal K_{q+d}$ 是支撑不超过 $q+d$ 的真实 $C$ 核。已有的同源构造保证这是正交 gap 投影。

$Tz\in\mathcal K_2\subset\mathcal K_{q+d}$，故 $G_qTz=0$。
而 $\eta$ 只在低输出层，$C^*\eta\perp\mathcal M_q$，故 $G_qC^*\eta=0$。
于是
$$
 \boxed{
 G_q\widetilde h_2+\frac{2D_0}{SW_1}G_qh_{21}
       +\frac{2D_0}{\alpha W_2}
                         G_q(f_2-\beta f_1)=0.
 }
\tag{6.1}
$$
等价地，
$$
 \boxed{
 G_q(f_2-\beta f_1)
 =-\frac{\alpha W_2}{2D_0}G_q\widetilde h_2
  -\frac{\alpha W_2}{SW_1}G_qh_{21}.
 }
\tag{6.2}
$$
同一有序恢复式对 (5.4) 的实际 source 列也成立。没有变换原 $f_2$、重新选择切口或换一个右费用来源。

## 7. 已付内容与仍须支付的部分

校正 $u$ 同时保完整一孔逆、二孔物理范数和全部源 Schur；(2.8) 给了分母的原尾统一正性。原先显式出现的 $e_1\otimes r$ 已吸入 $\widetilde h_2$，它没有被估成零，也没有被扔掉。

单个校正列的投影界可以准确写为
$$
 \|P_{\rm jo}\widetilde h_2\|^2
 =\langle z,\Gamma^{-1}z\rangle
 \le\|z\|^2=\frac{2D_0}{W_2^2}.
\tag{7.1}
$$
但这类单列界乘 (6.2) 的恢复系数，并不提供所需联合远孔小量。真正剩余的是
$$
 G_q\widetilde h_2+\frac{2D_0}{SW_1}G_qh_{21}
$$
在同一个原测试、同一个 $q$ 和同一个完整 $\Gamma_{CC}^{-1}$ 后的定量控制；不能分别估两个大项后声称抵消已付。

本稿没有扩张旧联合旗的合法窗口，没有从一般源推断实际固定测试，也没有给移动 $m,q$ 的 gap 收敛率。
