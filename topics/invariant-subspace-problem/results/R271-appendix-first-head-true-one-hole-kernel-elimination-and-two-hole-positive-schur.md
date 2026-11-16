# R271 附录：首头真一远孔核消去、物理两孔正 Schur 与完整匹配返回

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原 N/Y 偶数强位段，本稿先投掉首头 forcing 的完整一远孔真核，再用真实低 forcing 伴随像作两孔最小化。得到的代表与原首头在全部相关 $P_V-P_K$、匹配完整源及真实帽运输上相同；其平方费用是一个保完整 $\ker C^*$ 自由的正 Schur。该费用尚无移动参数上界，本稿不证明 $N=M$。

内积对第一变量线性。依据：

- [原偶段可达核与首头第二逆](R271-appendix-even-strong-prefix-reachable-kernel-and-first-head-second-green-schur.md)，§§2–5。
- [强尾联块的原顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§§2–6。
- [匹配完整 Schur 与第一远孔](R271-appendix-matched-full-resolvent-first-far-hole-and-native-mean-feedback.md)，§§1–3、6。
- [移动第一远孔整行](R271-appendix-moving-first-far-coherent-row-bessel-and-matched-source-cost.md)。

## 1. 原对象与全部自然域

取 $m\ge1$、$d=2^m$、偶数 $R\ge0$、$x=m+R\ge5$，并保原有限头
$$
C=A_m+D_{[m,x)},\qquad h=d+R,\qquad C^h=0.
$$
原远尾为
$$
D=D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
S=\sum_{i\ge x}b_i^2.
$$
$C+D$ 就是原 $L_m$ 的物理重分组，没有更换或线性化 $A_m$。
设
$$
K=\ker C,\quad Z=\ker C^*,\quad P=P_K,\quad
G=(CC^*)^\dagger,\quad \Gamma=P G|_K.
\tag{1.1}
$$
父稿已证原偶段 $K\perp Z$，即 $K\subset\operatorname{Ran}C$；
因而 $\Gamma$ 在 $K$ 上严格正。

$e_0,e_1$ 均含全部强位真空，满足
$$
Ce_1=e_0,\qquad Ce_0=0,\qquad
(C^*)^\dagger e_1=Ge_0,\qquad
\langle e_0,\Gamma e_0\rangle\le1.
\tag{1.2}
$$
记原首头 forcing 为 $f_1=e_1\otimes\Omega$。真实远孔 coherent 列是
$$
\omega_1=D^*\Omega,\qquad \omega_2=(D^*)^2\Omega,\qquad
\|\omega_1\|^2=S,
$$
$$
\sigma_2^2=\|\omega_2\|^2
=2\left(S^2-\sum_{i\ge x}b_i^4\right)>0.
\tag{1.3}
$$
定义整个头空间上的两条行
$$
\beta_{x,1}=S^{-1/2}D P_{\{N_{>}=1\}},\qquad
\beta_{x,2}=\sigma_2^{-1}D^2P_{\{N_{>}=2\}}.
\tag{1.4}
$$
这里 $P_{\{N_{>}=j\}}$ 表示“远孔数恰为 $j$”的物理正交投影；
下文另用 $P_{\{N_> >j\}}$ 表示严格大于 $j$，两者不混同。
删除后的远真空按原物理等距识别为头空间。
两行的伴随分别为 $a\mapsto a\otimes\omega_1/\sqrt S$、
$a\mapsto a\otimes\omega_2/\sigma_2$，所以范数均为一。

当前头有限维，全部头 MP 均在原完整度量中取。
$D$ 由 $\sum b_i<\infty$ 在原 Hilbert 空间上有界；
本稿新增向量只占远孔 $0,1,2$，所有伴随像和等式都在真实 Hilbert 域中。
原 $U_n,J_{b,n},J_{f,n}$ 的域则沿用父稿固定参数的完整源和全部 $h$ 段，
不假设全孔直和上的 $D^\dagger$ 有界。

## 2. 完整一远孔真核的正交投影

置
$$
v=(I+S\Gamma)^{-1}e_0,\qquad
F^{(1)}=C^\dagger v\otimes\Omega+\Gamma v\otimes\omega_1 .
\tag{2.1}
$$
令
$$
\mathscr K_1^C=\ker(C+D)\cap\{N_>\le1\}.
$$
则
$$
\boxed{F^{(1)}=(I-P_{\mathscr K_1^C})f_1.}
\tag{2.2}
$$

这里的核是完整物理核。具体地，令
$\mathcal H_{1,\perp}=\{\xi\in\mathcal H_1^>:\langle\xi,\omega_1\rangle=0\}$，
有准确正交分解
$$
\mathscr K_1^C
=(K\otimes\Omega)\ \oplus^\perp\
 (K\otimes\mathcal H_{1,\perp})\ \oplus^\perp\ \mathcal J K,
$$
$$
\mathcal J a
=-\sqrt S\,C^\dagger a\otimes\Omega+
 a\otimes\omega_1/\sqrt S,\qquad
\mathcal J^*\mathcal J=I+S\Gamma.
\tag{2.3}
$$
证明：最高行迫使一孔分量在 $K\otimes\mathcal H_1^>$。
把它分成 coherent 部分及 $D$ 核部分，后者就是第二项；
前者经 $D$ 输出 $\sqrt S\,a\in K\subset\operatorname{Ran}C$，
故全部零孔前像为 $-\sqrt S C^\dagger a+k$。
三项的正交性分别来自 $C^\dagger a\perp K$ 及两个远一孔方向正交。
因此没有删掉任何非 coherent primitive 来源。

又
$$
f_1-F^{(1)}
=P_Ke_1\otimes\Omega+\mathcal J(-\sqrt S\,\Gamma v).
$$
它属于 (2.3)，而 $F^{(1)}$ 正交该完整核，得到 (2.2)。
特别
$$
\boxed{
a_1:=\|F^{(1)}\|^2
=\langle e_0,\Gamma(I+S\Gamma)^{-1}e_0\rangle\le1,\qquad
S\|\Gamma v\|^2\le\tfrac14.
}
\tag{2.4}
$$
最后一式逐谱使用 $t/(1+t)^2\le1/4$，并保留 (1.2) 的完整第一逆能量。

## 3. 真低伴随像实现物理两孔正 Schur

置
$$
r=(I-P)Gv,\qquad q=(C^*)^\dagger r,\qquad
\mathcal A=(C^*)^\dagger|_Z,\qquad
\lambda=\frac{\sigma_2^2}{S},
$$
$$
q^\sharp=(I+\lambda\mathcal A\mathcal A^*)^{-1}q,\qquad
z^\sharp=\mathcal A^*q^\sharp\in Z.
\tag{3.1}
$$
因 $Z\subset K^\perp=\operatorname{Ran}C^*$，
$$
C^*\mathcal A z=z\quad(z\in Z),\qquad C^*q=r.
\tag{3.2}
$$
定义实际物理两孔向量
$$
\boxed{
F^{(2)}=q^\sharp\otimes\omega_2-\lambda z^\sharp\otimes\omega_1.
}
\tag{3.3}
$$
其准确源身份为
$$
\boxed{
F^{(1)}-F^{(2)}
=(C+D)^*\big(Gv\otimes\Omega-q^\sharp\otimes\omega_1\big).
}
\tag{3.4}
$$
验证：$C^*Gv=C^\dagger v$，而
$q=q^\sharp+\lambda\mathcal A z^\sharp$ 给
$r=C^*q^\sharp+\lambda z^\sharp$。
将 (3.4) 按远孔 $0,1,2$ 展开，就分别得到 (2.1) 与 (3.3)。

正度量来自真实低伴随像，而非把一虚拟 Boolean 位当成全部远尾。
对任意 $z\in Z$，
$$
\zeta(z)=z\otimes\omega_1+\mathcal A z\otimes\omega_2
=(C+D)^*(\mathcal A z\otimes\omega_1).
\tag{3.5}
$$
所以在 $q\otimes\omega_2$ 模去这个指定的实际伴随像族后，
其真正物理最小范数代表就是 $F^{(2)}$：
$$
\boxed{
\begin{aligned}
\gamma_2^2:=\|F^{(2)}\|^2
&=\min_{z\in Z}
 \big\{S\|z\|^2+\sigma_2^2\|q+\mathcal A z\|^2\big\}\\
&=\sigma_2^2
 \left\langle q,(I+\lambda\mathcal A\mathcal A^*)^{-1}q\right\rangle\\
&=\sigma_2^2\|q^\sharp\|^2+
 \lambda^2S\|z^\sharp\|^2.
\end{aligned}}
\tag{3.6}
$$
极小者为 $z=-\lambda z^\sharp$；这是正二次型的完整 Woodbury 极小化。
(3.6) 仅声称在 (3.5) 的整个 $Z$ 族中最小，
不把它冒称原全 $P_V/P_K$ 或完整返回空间的环境 MP。

还可把同一个准确费用写成首端带余核质量的单正逆。令
$
p=C^\dagger q^\sharp\in K^\perp,\qquad
Q_\lambda=(C^*C+\lambda P_Z)|_{K^\perp}.
$
由于 $q,\operatorname{Ran}\mathcal A\subseteq\operatorname{Ran}C$，
也有 $q^\sharp\in\operatorname{Ran}C$，从而 $Cp=q^\sharp$。
而 $\mathcal A^*=P_ZC^\dagger$，所以 $z^\sharp=P_Zp$。
将 (3.1) 的方程作用 $C^*$，得到
$
Q_\lambda p=r.
$
这里 $Z\subset K^\perp$，$C$ 在 $K^\perp$ 上单射；
故 $Q_\lambda$ 是该有限维原物理空间上的严格正算子。准确地，
$
\boxed{\gamma_2^2
=\sigma_2^2\langle r,Q_\lambda^{-1}r\rangle,
\qquad r=(I-P)Gv.}
\tag{3.6a}
$
等式来自 $\langle q,Cp\rangle=\langle C^*q,p\rangle=\langle r,p\rangle$。
此式保留原 $Gv$ 来源，只重新表达同一个正费用；它没有支付
$Q_\lambda^{-1}$ 在该来源上的移动上界。

原连续权还给
$$
S\ge\frac1{3(x+1)^3},\qquad
\sum b_i^4\le (x+1)^{-4}S.
$$
故 $x\ge5$ 时 $S^2\le\sigma_2^2\le2S^2$，即 $S\le\lambda\le2S$。
用父稿的有限头真一位对象
$C_{\sqrt S}=\left(\begin{smallmatrix}C&\sqrt S I\\0&C\end{smallmatrix}\right)$
只作费用比较，得到
$$
\boxed{
\gamma_2^2
\le\frac{\sigma_2^2}{S}
 \left[\|(C_{\sqrt S}C_{\sqrt S}^*)^\dagger(e_0,0)\|^2-\|Gv\|^2\right].
}
\tag{3.7}
$$
右侧括号准确是父稿第二逆公式的返回正项。
(3.3)–(3.6) 已先在真实无限远尾成立，(3.7) 不承担物理替换。

还有一个原度量的正交性：
$$
F^{(1)}\perp F^{(2)}.
\tag{3.8}
$$
唯一可能重叠是一孔层，但其中头方向分别为
$\Gamma v\in K$ 与 $z^\sharp\in Z$，由 $K\perp Z$ 得零。

## 4. 同一个原 forcing、完整匹配源和两孔恒等式

取同一个原实际母窗口 $Q$、同一个 $w\in W$，
$$
u=(P_{V_Q}-P_{K_Q})w,\qquad
\|u-P_{\mathcal N\le Q}w\|\le2\eta_m\|w\|,\quad
\eta_m=e^{-6d^4}.
\tag{4.1}
$$
$\mathcal N$ 是原 $m$ 后总孔，$N_>$ 是 $x$ 后远孔，
$N_>\le\mathcal N\le N_>+R$。
假设 $Q\ge R+2$。式 (2.2) 的差属于原 $K_Q$；
式 (3.4) 括号内的低 forcing 总孔数至多 $R+1<Q$，
所以原 $V_Q$ 的全部低方程及 $K_Q$ 真核方程准确杀掉该伴随像。
因此
$$
\boxed{
(P_{V_Q}-P_{K_Q})f_1
=(P_{V_Q}-P_{K_Q})F^{(1)}
=(P_{V_Q}-P_{K_Q})F^{(2)}.
}
\tag{4.2}
$$
没有假设 $C^*$、$P_V$、$P_K$ 或 MP 互相交换。

结合 (2.4)、(3.8)，同一个实际投影还满足
$$
\boxed{
\|(P_{V_Q}-P_{K_Q})f_1\|^2
\le\frac{a_1\gamma_2^2}{a_1+\gamma_2^2}.
}
\tag{4.3}
$$
它是两个正交同 forcing 代表的最优 affine 组合费用；
若 $\gamma_2=0$，结论按零理解。它没有给 $\gamma_2$ 上界。

现取原 cut $n\ge2$、$n+h+R<Q$，保持全部 $h$ 段：
$$
r_n=Cu_n,\quad L_n=U_n^*U_n,\quad
H_n=J_{f,n}^*J_{f,n},\quad B_n=J_{b,n}^*J_{b,n},
$$
$$
s_{f,n}[F]=(L_n+H_n)^{-1}U_n^*F,\qquad
\mathfrak M_n=\langle(H_n-B_n)r_n,s_{f,n}[f_1]\rangle.
$$
$F$ 在这个公式中位于原物理左侧，故对头 forcing $g$ 它就是 $F=i_0g$。
写
$$
\mathcal P_n=(L_n+H_n)^{-1}(H_n-B_n),\quad
a_n=r_n-\mathcal P_nr_n,\quad
\widetilde v_n=U_n\mathcal P_nr_n=u_{\le n}-U_na_n.
$$
父稿给
$$
\mathfrak M_n=\langle\widetilde v_n,f_1\rangle,\qquad
\|a_n\|_{L_n+H_n}\le\|Y_n\|,\quad
Y_n=(u_{n+1},\ldots,u_{n+h}).
\tag{4.4}
$$
这里 $\mathcal P_n$ 只已知在 $L_n+B_n$ 度量中自伴正收缩；
(4.4) 的另一度量估计来自物理核投影，不是任意换度量。

$\widetilde v_n\perp\mathscr K_n^C$，且其前两条真实低行均为零。
因而 (2.2)、(3.4) 分别给
$$
U_n^*f_1=U_n^*F^{(1)}=U_n^*F^{(2)}.
$$
特别完整源本身准确相同，所有左零源和右零源均已保留。
由此
$$
\boxed{
\mathfrak M_n
=\sigma_2\langle\beta_{x,2}\widetilde v_n,q^\sharp\rangle
-\lambda\sqrt S\langle P_Z\beta_{x,1}\widetilde v_n,z^\sharp\rangle.
}
\tag{4.5}
$$
也可先读到 primitive 相消的原式
$$
\mathfrak M_n
=-\sqrt S\langle\beta_{x,1}\widetilde v_n,(I-P)Gv\rangle
=\sigma_2\langle\beta_{x,2}\widetilde v_n,q\rangle.
\tag{4.6}
$$
第二步使用真实
$C\beta_{x,1}\widetilde v_n=-\sigma_2\beta_{x,2}\widetilde v_n/\sqrt S$。
(4.5) 进一步保留了 (3.6) 的物理正 Schur。

## 5. 同一 $w$ 的误差、全 cut 与非零锚

$F^{(2)}$ 的远孔支撑至多二，故 $Q\ge R+2$ 时
$P_{\mathcal N\le Q}F^{(2)}=F^{(2)}$。从 (4.1)、(4.4) 得
$$
\boxed{
|\mathfrak M_n-\langle w,F^{(2)}\rangle|
\le\gamma_2\big(\|Y_n\|+2\eta_m\|w\|\big).
}
\tag{5.1}
$$
与此同时，使用原单位首头而非新代表，
$$
|\mathfrak M_n-\langle w,f_1\rangle|
\le\|Y_n\|+2\eta_m\|w\|.
\tag{5.2}
$$
因此非零锚并没有被新高源范数替换。

令 $\mathcal I=\{n:n_0\le n\le Q-R-h-1\}$、$n_0\ge2$、
$N=|\mathcal I|>0$，
$$
b_w=\|P_{\{N_> >n_0\}}u\|,\qquad
e=2\eta_m\|w\|+\sqrt{h/N}\,b_w,\qquad
\Phi=N^{-1}\sum_{n\in\mathcal I}\mathfrak M_n.
$$
每个远孔层在 $Y_n$ 中至多重复 $h$ 次，故
$$
\boxed{
|\Phi-\langle w,F^{(2)}\rangle|\le\gamma_2 e,\qquad
|\Phi-\langle w,f_1\rangle|\le e.
}
\tag{5.3}
$$
先选定原参数和 (3.1) 的同一源，再对全部 cut 平均；
没有在不同 cut 重取较便宜的 $q^\sharp$。

为说明整行范围，取几何增长 $x_{\ell+1}\ge a(x_\ell+1)$、$a>1$。
令 $J_{x,y}$ 为中间位真空等距。与第一远孔相同的物理支撑计算给
$$
\beta_{x,2}\beta_{y,2}^*
=\frac{\sigma_2(y)}{\sigma_2(x)}J_{x,y}^*\qquad(x<y).
\tag{5.4}
$$
因为从 $y$ 创建两孔后，$x$ 的恰二孔门强制中间位全真空。
以 $S^2\le\sigma_2^2\le2S^2$ 及原积分比较估计，
第二行的 Bessel 常数可取
$$
B_2(a)=1+\frac{2\sqrt2\,a^{-3}}{1-a^{-3}}.
$$
第一行的已付常数为
$B_1(a)=(1+a^{-3/2})/(1-a^{-3/2})$。
故整个移动头来源满足
$$
\sum_\ell\big(\|\beta_{x_\ell,2}w\|^2+
               \|P_{Z_\ell}\beta_{x_\ell,1}w\|^2\big)
\le(B_1+B_2)\|w\|^2.
\tag{5.5}
$$
这没有把随 $\ell$ 变化的头投影升成固定有限维来源。

若 $\sum_\ell e_\ell^2<\infty$，由 (3.6)、(5.3)、(5.5) 得
$$
\boxed{
\left(\sum_{\ell:\gamma_{2,\ell}>0}
       \frac{|\Phi_\ell|^2}{\gamma_{2,\ell}^2}\right)^{1/2}
\le\sqrt{B_1+B_2}\,\|w\|+
   \left(\sum_\ell e_\ell^2\right)^{1/2}.
}
\tag{5.6}
$$
例如原 $R_m=d_m$、$h_m=2d_m$、$Q_m=4h_m^2$、
$n_{0,m}=2h_m^2$ 从充分大 $m$ 起给该可和性。
若固定原首头锚 $\langle w,f_1\rangle\ne0$，(5.2) 因而迫使
$\sum_\ell\gamma_{2,\ell}^{-2}<\infty$。
这是对 (3.6) 的必要费用条件；未证明它与原模型矛盾。

## 6. 真正帽逆伴随及全部端点

本节仅在已付 Riordan 正反映射的原参数条件下使用
$$
\|K_{n,\rm amb}\|,\ \|K_{n,\rm amb}^{-1}\|\le\mathcal C_0,
\qquad n+2h+R<Q.
$$
不能仅由 §5 的 $R=d$ 实例自动调用这一条件。
记 $\mathcal R_n=J_{f,n}-J_{b,n}$，
$$
z_n=\mathcal R_ns_{f,n}[f_1]
=\mathcal R_ns_{f,n}[F^{(2)}],\qquad
\widehat z_n=P_{\widehat{\mathscr E}_n}K_{n,\rm amb}^{-*}z_n .
\tag{6.1}
$$
真正逆伴随后仍保外投影。父稿的完整混合身份准确为
$$
\langle\widehat{\mathcal R}_n(g_{\rm R}(C_{\rm s})r_n),\widehat z_n\rangle
-\mathfrak M_n
=\langle K_{n,\rm amb}J_{b,n}r_n,\widehat z_n\rangle.
\tag{6.2}
$$
绝对误差不超过
$\mathcal C_0^2\alpha_n(r_n)\lambda_n(s_{f,n}[f_1])$。

对同一 cut 集，完整物理核增量既可用固定 $f_1$，也可用同一个 $F^{(2)}$：
$$
\mathcal T_{f,n}s_{f,n}[f_1]
=(P_{\mathscr K_{n+h}^C}-P_{\mathscr K_n^C})f_1
=(P_{\mathscr K_{n+h}^C}-P_{\mathscr K_n^C})F^{(2)}.
$$
故真实 Bessel 计数给
$$
\sum_n\lambda_n(s_{f,n}[f_1])^2
\le h\min(1,\gamma_2^2),\qquad
\sum_n\alpha_n(r_n)^2\le h b_w^2.
\tag{6.3}
$$
于是帽均值与 $\Phi$ 的差至多
$$
\boxed{
\mathcal C_0^2\frac hN\,b_w\min(1,\gamma_2).
}
\tag{6.4}
$$
归一到 $\gamma_2$ 后仅需把 (5.6) 的 $e_\ell$
替换为 $e_\ell+\mathcal C_0^2(h_\ell/N_\ell)b_{w,\ell}$。
只有在这个误差平方可和时，才声称相应整行结论。
全部 $h$ 段、完整高旗、裸端、完整端和真正帽测试都未删去。

## 7. 已付范围与下一真实费用

本稿新增的是：原首头经过完整真一远孔核投影后，
其 primitive 第一行准确消失；余项有 (3.3) 的真正物理两孔代表，
且完整 $Z=\ker C^*$ 自由以 (3.6) 的正 Schur 保留。
(3.4) 是实际低伴随像身份，不把该自由错称为两孔真核。

费用 $\gamma_2$ 仍由原有限强头的核外第二逆来源决定。
(3.7) 把它只接到第二逆的返回正项，没有支付该项的移动参数上界。
本稿不使用一般 head 的 Green 常数替代原来源，
不将第一逆标量 $\le1$ 升成第二逆界，也不把条件 Bessel 矛盾当成普通 ISP 完成。
