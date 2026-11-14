# R239 附录：原两下降 Schur 常数、第三尾桥与可支付的短 jet 锚

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文在原连续尾的完整固定孔层证明精确两下降恒等式，给出原合法窗口上的显式 $O_m(q^4)$ 费用。它支付普通三阶次数算子及同源裸费二阶锚；没有把环境伴随下界当成受限伴随下界，没有证明完整源图上的无权比较。普通 ISP 与边界 $N=M$ 仍为 OPEN。

本文接[顺次 jet 次数算子与真幂 Schur 比较](R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md)。其中的 $C_*(p)$ 是**顺次两次单步 MP**与**真正 $D^2$ 最小原像**之间的准确比例；本稿把它接到原第二下降的 $D_3$ 桥，并利用已付的 primitive 原像界给出实际费用。

## 1. 真实源层、正交旗与逆

固定 $m\ge1$，令
$$
D=D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2},
$$
$$
D_p=D|_{\mathcal H_p}:\mathcal H_p\longrightarrow\mathcal H_{p-1},
\qquad K_p=\ker D_p,
$$
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\quad E_{0,p}=\{0\},
\qquad U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
\tag{1.1}
$$
所有正交性均指原物理 Hilbert 内积；特别 $U_{1,p}=K_p$。固定以下 $p\ge3$，不使用孔层直和上的有界 MP 逆。原固定孔层满射保证 $D_p^\dagger$ 及各有限真幂的 MP 逆有界。

定义
$$
R_{1,p}=D_p^\dagger|_{K_{p-1}},
\qquad
R_{2,p}=(D_{p-1}D_p)^\dagger|_{K_{p-2}}.
\tag{1.2}
$$
则
$$
R_{1,p}:K_{p-1}\overset{\sim}{\longrightarrow}U_{2,p},
\qquad
R_{2,p}:K_{p-2}\overset{\sim}{\longrightarrow}U_{3,p}
\tag{1.3}
$$
是有界双射。

证明如下。对 primitive $f\in K_{p-1}$，$DR_{1,p}f=f$，故 $D^2R_{1,p}f=0$；单步最小性又给 $R_{1,p}f\perp K_p$，所以输出在 $U_{2,p}$。反向任意 $u\in U_{2,p}$ 的 $Du$ primitive，而 $u\perp\ker D$，所以 $R_{1,p}Du=u$。真幂二步完全同理：$D^2R_{2,p}f=f$、$Df=0$ 使输出在 $E_{3,p}$，真幂最小性使其正交于整个 $E_{2,p}$，故恰在 $U_{3,p}$。反向由同一最小性得到。这里没有把顺次 MP 的像认成 $U_{3,p}$。

令
$$
A_{1,p}=D_p|_{U_{2,p}}:U_{2,p}\longrightarrow K_{p-1},
$$
$$
B_{2,p}=P_{K_{p-1}}D_p|_{U_{3,p}}:
U_{3,p}\longrightarrow K_{p-1}.
\tag{1.4}
$$
于是
$$
\boxed{A_{1,p}^{-1}=R_{1,p}.}
\tag{1.5}
$$
$B_{2,p}$ 是真正第二下降的 primitive 回返块。另一个分量
$P_{U_{2,p-1}}D_p|_{U_{3,p}}$ 到 $U_{2,p-1}$ 同样为双射，因为与 $D_{p-1}|_{U_{2,p-1}}$ 复合恰为 $D^2|_{U_{3,p}}$。后文不把这个分量与 $B_{2,p}$ 混同。

## 2. 顺次二步的准确正交分裂

记
$$
Q_{2,p}=D_p^\dagger D_{p-1}^\dagger|_{K_{p-2}},
$$
$$
\Gamma_{1,p}=R_{1,p}^*R_{1,p},\qquad
\Gamma_{2,p}=R_{2,p}^*R_{2,p},\qquad
T_p=Q_{2,p}^*Q_{2,p}.
\tag{2.1}
$$
$\Gamma_{1,p}$ 作用在 $K_{p-1}$，$\Gamma_{2,p},T_p$ 作用在 $K_{p-2}$；固定参数下均严格正且有界可逆。

对任意 $f\in K_{p-2}$，$D R_{2,p}f$ 属于 $E_{2,p-1}$，并且
$$
D R_{2,p}f
=D_{p-1}^\dagger f+B_{2,p}R_{2,p}f.
\tag{2.2}
$$
因为第一项正交于 $K_{p-1}$，第二项是完整 primitive 投影；两者的 $D$ 像合计为 $f$。两个两步原像都正交于 $K_p$，故
$$
\boxed{
Q_{2,p}f
=R_{2,p}f-R_{1,p}B_{2,p}R_{2,p}f.
}
\tag{2.3}
$$
右侧第一项在 $U_{3,p}$，第二项在 $U_{2,p}$，两者真正正交。因此
$$
\boxed{
T_p=\Gamma_{2,p}
+R_{2,p}^*B_{2,p}^*\Gamma_{1,p}B_{2,p}R_{2,p}.
}
\tag{2.4}
$$

定义最优比例
$$
C_*(p)=
\|\Gamma_{2,p}^{-1/2}T_p\Gamma_{2,p}^{-1/2}\|.
\tag{2.5}
$$
由于 $R_{2,p}\Gamma_{2,p}^{-1/2}$ 是从 $K_{p-2}$ 到整个 $U_{3,p}$ 的酉同构，(2.4) 给
$$
\boxed{
C_*(p)=1+\|A_{1,p}^{-1}B_{2,p}\|^2.
}
\tag{2.6}
$$
它准确计入第二下降回到低高度所产生的额外顺次费用，而非只给一个形式 Schur 下界。

## 3. $D^*$ 作用于 primitive 不混入更高高度

定义原有的第三尾及占据权
$$
D_3=\sum_{j\ge m}b_j^3E_j,\qquad
S_m=\sum_{j\ge m}b_j^2,\qquad
W_m=\sum_{j\ge m}b_j^2n_j,\quad n_j=E_j^*E_j.
\tag{3.1}
$$
全部级数在算子范数中收敛。不同位交换，单个位给
$$
[D,D^*]=S_mI-2W_m,\qquad [D,W_m]=D_3,\qquad DD_3=D_3D.
\tag{3.2}
$$
这些原尾交换子已用于[全孔层环境能量稿](R239-appendix-all-hole-environment-energy-gap-and-actual-tail-stability.md)和[实际外出生桥稿](R239-appendix-actual-outer-birth-source-factorization-and-vandermonde-orthogonality.md)。

对 $f\in K_{p-1}$，
$$
D^2D^*f=D(S_mI-2W_m)f=-2D_3f,
\qquad D^3D^*f=-2D_3Df=0.
\tag{3.3}
$$
又对于 $k\in K_p$，
$\langle D_p^*f,k\rangle=\langle f,D_pk\rangle=0$。所以准确有
$$
\boxed{D_p^*f\in U_{2,p}\oplus U_{3,p}.}
\tag{3.4}
$$
这是完整高度断言；没有遗漏 $U_{j,p}$、$j\ge4$ 分量。

从 (1.4) 取伴随，
$$
P_{U_{2,p}}D_p^*f=A_{1,p}^*f,\qquad
P_{U_{3,p}}D_p^*f=B_{2,p}^*f.
$$
对第二式施加 $D^2$，第一块被消去；结合 (3.3) 和 $R_{2,p}$ 在 $U_{3,p}$ 上的真逆性质得到
$$
\boxed{B_{2,p}^*=-2R_{2,p}D_3|_{K_{p-1}}.}
\tag{3.5}
$$
这里 $D_3:K_{p-1}\to K_{p-2}$ 的源域是完整原 primitive 层。式 (3.5) 使用真幂 $R_{2,p}$，不能换成 $Q_{2,p}$。

## 4. 两个完整的第三尾 Gram 恒等式

由 $R_{1,p}=U\Gamma_{1,p}^{1/2}$ 的极分解，$U$ 到 $U_{2,p}$ 为酉同构。结合 (2.6)、(3.5)，
$$
\begin{aligned}
\|A_{1,p}^{-1}B_{2,p}\|^2
&=\|\Gamma_{1,p}^{1/2}B_{2,p}\|^2\\
&=4\|R_{2,p}D_3\Gamma_{1,p}^{1/2}\|^2\\
&=4\|\Gamma_{2,p}^{1/2}D_3\Gamma_{1,p}^{1/2}\|^2.
\end{aligned}
$$
所以
$$
\boxed{
C_*(p)=
1+4\|\Gamma_{2,p}^{1/2}D_3\Gamma_{1,p}^{1/2}\|^2.
}
\tag{4.1}
$$

(3.4) 的两个正交分量还给完整压缩恒等式
$$
\begin{aligned}
P_{K_{p-1}}D_pD_p^*|_{K_{p-1}}
&=A_{1,p}A_{1,p}^*+B_{2,p}B_{2,p}^*\\
&=\Gamma_{1,p}^{-1}+4D_3^*\Gamma_{2,p}D_3.
\end{aligned}
\tag{4.2}
$$
此处 $D_3^*$ 表示 $D_3:K_{p-1}\to K_{p-2}$ 的受限伴随，故包含正确的 primitive 压缩；不能删掉它所含的投影。

另一方面在 primitive 层上 $D^*D=0$，由 (3.2)，
$$
\boxed{
\Gamma_{1,p}^{-1}+4D_3^*\Gamma_{2,p}D_3
=S_mI-2P_{K_{p-1}}W_m|_{K_{p-1}}.
}
\tag{4.3}
$$
因此还有相同 $C_*(p)$ 的准确写法
$$
\boxed{
C_*(p)=
\left\|
\Gamma_{1,p}^{1/2}
\bigl(P_{K_{p-1}}D_pD_p^*|_{K_{p-1}}\bigr)
\Gamma_{1,p}^{1/2}
\right\|.
}
\tag{4.4}
$$
由 $W_m\succeq0$ 立即得到
$$
\boxed{1\le C_*(p)\le S_m\|\Gamma_{1,p}\|.}
\tag{4.5}
$$
这个上界尚需要真正 $\Gamma_{1,p}$ 的成本；下一节使用已经支付的原 primitive 原像，而不从环境 gap 反推受限逆。

## 5. 原连续尾的显式多项式费用

[高孔笔记 §14.1–14.2](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)从 R254 同一个相容族证明
$$
\|D_p^\dagger f\|
\le L_{m,p-1,1}\|f\|,
\qquad f\in K_{p-1},
$$
其中
$$
\boxed{
L_{m,p-1,1}
=512\sqrt{p+2}\,(m+p+2)^{3/2}.
}
\tag{5.1}
$$
具体域检查：在该文取其 $q=p-1,T=1$，共同输入上界 $P=p$；primitive $f$ 的孔数为 $p-1\le P-1$，正规化 $Q_1$ 恰为这里的 $D_p^\dagger$。头尾重编号只发生在 R254 的尾权，不改变物理 $A_m$。

于是
$$
\|\Gamma_{1,p}\|
\le512^2(p+2)(m+p+2)^3,
$$
结合 (4.5) 得
$$
\boxed{
C_*(p)\le
512^2S_m(p+2)(m+p+2)^3.
}
\tag{5.2}
$$
这是原全部固定孔层的实际 $O_m(p^4)$ 上界，没有低占据假设。对 $m\ge1$，
$$
S_m=\sum_{j\ge m}(j+1)^{-4}\le\frac1{3m^3}.
\tag{5.3}
$$

原应用取
$$
m\ge5,\quad d=2^m,\quad4d\le q\le e^{d^3/4},
\quad p\in\{q,q+1\}.
\tag{5.4}
$$
此时 $p+2\le q+3\le\frac54q$，以及
$m+p+2\le m+q+3\le\frac32q$。所以
$$
L_{m,p-1,1}
\le512\sqrt{\tfrac54q}\,(\tfrac32q)^{3/2}
<2048q^2.
$$
因此可直接使用
$$
\boxed{
C_*(p)\le 2^{22}S_mq^4
\le\frac{2^{22}}{3m^3}q^4
\le2^{22}q^4,
\qquad p=q,q+1.
}
\tag{5.5}
$$
特别 $\log C_*(p)\le d^3+22\log2$。

这里没有采用候选 $\|\Gamma_{1,p}\|\le S_{m+2p}^{-1}$。旧暗态的
$\|D^*x\|^2=S_{m+2p}$ 是特定向量的值，不是原完整受限逆的下界证明；[纯创建指数奇异界](R239-appendix-pure-tail-creation-exponential-singular-bounds.md)还说明不能把这个数当作完整环境创建的普遍 gap。本稿的 (5.2) 来自真正 primitive 原像估计，足以支付本节用途。

## 6. 普通三阶与同源裸费二阶锚

沿用顺次 Taylor 次数算子
$$
\mathfrak N_{K,q}h
=\sum_{t=0}^{K-1}(t+1)Q_tP_0D^th,\qquad h\in E_{K,q}.
\tag{6.1}
$$
前稿已完整证明
$$
\|\mathfrak N_{3,q}\|^2
=6+\frac{C_*(q)}2
\left(1+\sqrt{1+\frac{24}{C_*(q)}}\right)
\le C_*(q)+12,
\tag{6.2}
$$
以及对于真正同一首头裸度量
$$
W_{2,q}=(D_{q+1}^\dagger|_{E_{2,q}})^*
(D_{q+1}^\dagger|_{E_{2,q}}),
$$
$$
\|\mathfrak N_{2,q}\|_{W_{2,q}}^2
=2+\frac{C_*(q+1)}2
\left(1+\sqrt{1+\frac8{C_*(q+1)}}\right)
\le C_*(q+1)+4.
\tag{6.3}
$$
(6.2) 与 (6.3) 是不同域、不同度量；普通 $\|\mathfrak N_{2,q}\|=2$ 并没有被误用于 (6.3)。

在 (5.4) 的全部原窗口里，(5.5) 给
$$
\boxed{
\|\mathfrak N_{3,q}\|\le4096q^2,\qquad
\|\mathfrak N_{2,q}\|_{W_{2,q}}\le4096q^2.
}
\tag{6.4}
$$
故对同一个 $h\in E_{2,q}$，真正裸与完整右最小费用均满足
$$
\boxed{
\alpha_q(e_0\mathfrak N_{2,q}h)
\le4096q^2\,\alpha_q(e_0h),
}
\tag{6.5}
$$
$$
\lambda_q(e_0\mathfrak N_{2,q}h)
\le4096q^2\,\lambda_q(e_0h).
\tag{6.6}
$$
原因是两个首头源的完整右最小链都为只有首段的
$e_0D_{q+1}^\dagger(\cdot)$；裸最小链与它相同。

对于任意另一个原实际源 $r$，令 $P$ 为物理首源头投影，
$y=J_q^{-1}r$。首头右约化的同源配对给
$$
\boxed{
|\langle e_0\mathfrak N_{2,q}h,Py\rangle|
\le4096q^2\,\alpha_q(e_0h)\,
\|G_q^{1/2}Py\|.
}
\tag{6.7}
$$
右边仍是**原同一个 $h$** 的裸费和**原同一个 $r$** 的平坦对偶分量。没有改换 $r$，没有把普通 $\lambda$ 当成 $\lambda_{\rm flat}$。

若单 dyadic 块测试的顶源满足 $h\in E_{2,q}$，则任意更大的次数截断均有
$\mathfrak N_{K,q}h=\mathfrak N_{2,q}h$，故 (6.5)–(6.7) 对该原高块锚直接适用。

## 7. 与原极小交织误差的预算及尚未支付之处

单块导数交织稿给在同一个 (5.4) 窗口内的
$$
\varepsilon_{m,q}\le e^{-9d^4/2}.
$$
凡某一已证明的误差项确实包含乘积
$\varepsilon_{m,q}\|\mathfrak N_{2,q}\|_{W_{2,q}}$
或 $\varepsilon_{m,q}\|\mathfrak N_{3,q}\|$，(6.4) 给
$$
\varepsilon_{m,q}\,4096q^2
\le
\exp\!\left(-\frac92d^4+\frac12d^3+12\log2\right)
\le e^{-4d^4}\quad(m\ge5).
\tag{7.1}
$$
最后一步因为 $d\ge32$ 时
$\frac12d^3+12\log2\le\frac12d^4$。
所以这一实际锚费用能够由已付单块误差余量容纳。

(7.1) 只是一条精确可代入的预算；它不制造原本不存在的 $\varepsilon$ 因子。尤其没有证明：

- 物理低锚的实际左最小原像属于原 $M$，或任意尾逆与 $P_M$ 交换；
- 在 $M=B+J_q^{-1}G_qJ_q^{-1}$ 度量投影以后，裸锚仍由同一个源的 $\chi^2$ 免费控制；
- 原整个低旗的 $c(C)\chi^2$ 费用自动被小误差吸收；
- 原无 $\varepsilon$ 的全左费用比较只需可求和阈值 $O(e^{d^3/4}/d)$。

本文关闭的是二下降／三阶普通次数以及二阶同源裸锚的实际费用接口，并将此前只给条件的 $C_*(p)$ 变为原全窗口显式界。完整源图与更一般非primitive 实际源仍需继续。
