# R271 附录：对偶创建合成与共同来源的相邻原旗返回

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 旧实际来源的全对正 Gram 同时给删除与创建两种合成行。本稿保原源度量，先证明创建合成的完整块恒等式；再将并行一位 Schur 的增益和投影损失作同一参数积分，得到一个公共 coherent 代表的删除范数行。最后把原 $V_Q/K_Q$ 的删除准确送到相邻 $Q-1$ 旗，支付两个固定低 forcing 的一条真实双线性返回行。

主误差含两个真实缺陷的乘积及 $x^{-1/2}$ 的源范数项。本稿不把其中第二个有限 forcing 换成任意原无限向量 $w$，也不将标量弱行升为 $\sum_i\|E_i u\|^2$ 或完整 Moore--Penrose 返回的范数行。

依据：

- [实际低端 forcing 的全对正 Gram](R271-appendix-actual-low-end-forcing-positive-deletion-grams-and-compressed-adjoint-descendants.md)，§1(1.1)、§2(2.2)、§3b(3b.4)、§5(5.4)--(5.5)；
- [并行一位完整 Schur 与共同头恢复](R271-appendix-parallel-one-bit-schur-common-head-restoration-and-compressed-creation-row.md)，§§1--4；
- [一位真实核投影损失](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)；
- [完整 coherent 同源身份](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)。

## 1. 原空间、来源及指标

保持原物理模型的
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad d=2^m,\quad h=d+R,\quad C^h=0,
$$
$$
D=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
S=\sum_{i\ge x}z_i,\quad z_i=b_i^2 .
\tag{1.1}
$$
$E_i$ 是删除，$E_i^*$ 是创建，$n_i=E_i^*E_i$。$i_0:\mathcal F\to\mathcal H$ 是同一个原强头张量远尾真空的等距嵌入。所有物理总尾孔 cut 仍从原 $m$ 处开始计数，不是远位数值位置的 cut。

记原闭空间及其实际正交投影为
$$
K_Q\subset V_Q,\quad P_{U_Q}=P_{V_Q}-P_{K_Q},\quad
Z_{V,Q}=P_{V_Q}i_0,\quad Z_{K,Q}=P_{K_Q}i_0,\quad
Z_{e,Q}=(I-P_{V_Q})i_0 .
$$
对允许的 $a\in\mathcal F$，置
$$
u_{a,Q}=P_{U_Q}i_0a,\quad
G_{E,Q}=Z_{E,Q}^*Z_{E,Q},\quad
G_{\Delta,Q}=I-i_0^*P_{U_Q}i_0,
$$
$$
\Delta_{a,Q}^2=\langle G_{\Delta,Q}a,a\rangle
=\|i_0a-u_{a,Q}\|^2 .
\tag{1.2}
$$
原两缺陷互相正交，所以 $G_{\Delta,Q}=G_{e,Q}+G_{K,Q}$。

下文取
$$
x\ge1,\qquad Q\ge R+h+2 .
\tag{1.3}
$$
这保证并行一位的全部低 forcing 恒等式同时在原 $Q$ 与 $Q-1$ 两旗成立。标准 $R=d,x=m+d,h=2d$ 且 $m\ge1$ 时，$Q\ge4d$ 足够；仍须另外满足原母窗的其它合法条件。本文不扩大任何 carry 窗。

## 2. 创建合成的准确块 Gram

先固定同一 cut，并取
$Z\in\{Z_V,Z_K,Z_e\}$，$G=Z^*Z$、
$M_i=Z^*n_iZ$。旧全对原式给
$$
K_{ij}=Z^*E_i^*E_jZ=K_{ij}^*=K_{ji}\succeq0
\qquad(i\ne j).
\tag{2.1}
$$
旧 §3b 的投影行经 $\ker G=\ker Z$ 的源同余，准确给
$$
\left\|\sum_i\frac{E_iZ a_i}{\sqrt{i+1}}\right\|^2
\le\frac43\sum_i\langle Ga_i,a_i\rangle .
\tag{2.2}
$$
此处每个 $a_i$ 可不同，但全在同一个 $\mathcal F$；不要求 $G$ 可逆。

对有限指标族，把创建合成与删除合成的块 Gram 分别记为
$\mathscr C^*\mathscr C$、$\mathscr D^*\mathscr D$。当 $i\ne j$，
不同物理位交换，故
$$
Z^*E_iE_j^*Z=Z^*E_j^*E_iZ=K_{ji}=K_{ij}.
$$
对角则是 $Z^*E_iE_i^*Z=G-M_i$，而删除对角是 $M_i$。所以整个源块严格满足
$$
\boxed{
\mathscr C^*\mathscr C
=\mathscr D^*\mathscr D+
\operatorname{diag}_i\left(\frac{G-2M_i}{i+1}\right).
}
\tag{2.3}
$$
特别，令
$$
c_x=\frac43+\frac1{x+1},
$$
由 (2.2)、$M_i\succeq0$ 得
$$
\boxed{
\left\|\sum_i\frac{E_i^*Za_i}{\sqrt{i+1}}\right\|^2
\le c_x\sum_i\langle Ga_i,a_i\rangle .
}
\tag{2.4}
$$
这是真创建算子 $E_i^*$ 的合成界，保原 $G$；没有把它替成补 Gram，也没有维数或孔数损失。

对无限族，先用有限部分和证明，再在
$\sum_i\langle Ga_i,a_i\rangle<\infty$
的半范数空间去掉核并完成。由于 $Za_i=0$ 当 $Ga_i=0$，该完成上的合成无歧义。每个 $E_i,E_i^*$ 本身都是原物理有界算子。

## 3. 原双缺陷来源的创建弱行

真空创建列 $E_i^*i_0$ 在不同 $i$ 的物理像互相正交，因此
$$
\left\|\sum_i\frac{E_i^*i_0a_i}{\sqrt{i+1}}\right\|^2
=\sum_i\frac{\|a_i\|^2}{i+1}.
\tag{3.1}
$$
用 $Z_U=i_0-Z_e-Z_K$，对两个实际缺陷分别应用 (2.4)，再在两项来源上使用 Cauchy，得到
$$
\begin{split}
\left\|\sum_i\frac{E_i^*Z_Ua_i}{\sqrt{i+1}}\right\|
\le{}&
\left(\sum_i\frac{\|a_i\|^2}{i+1}\right)^{1/2}\\
&+\sqrt{2c_x}
\left(\sum_i\langle G_\Delta a_i,a_i\rangle\right)^{1/2}.
\end{split}
\tag{3.2}
$$
这保两个真实缺陷的共同源合同，未丢掉 $V/K$ 混合。

特别，固定 $a$，在 (3.2) 中令 $a_i=\lambda_i a$，对
$\sum|\lambda_i|^2\le1$ 取上确界。对任意物理 $y$，得
$$
\boxed{
\left(\sum_{i\ge x}
\frac{|\langle y,E_i^*u_{a,Q}\rangle|^2}{i+1}\right)^{1/2}
\le
\left[
\frac{\|a\|}{\sqrt{x+1}}
+\sqrt{2c_x}\,\Delta_{a,Q}
\right]\|y\|.
}
\tag{3.3}
$$
$y$ 可有任意合法孔支持；这里并不要求它是一个真空 forcing。
(3.3) 是创建方向的弱行，和旧
$\sum_i|\langle E_i u_{a,Q},y\rangle|^2/(i+1)$
的删除方向有别。额外真空项必须保留。

## 4. 同一 Fock 中合付全部并行损失和增益

固定第一 forcing $f=i_0g$。对 $s>0$，定义
$$
H_C(s)=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{s^j j!},
\qquad q_g(s)=\langle g,H_C(s)^{-1}g\rangle .
$$
在同一全远尾 bosonic Fock 空间再加方差 $t\in[S,2S]$ 的辅助 mode。记未硬化远位的完整闭核为 $\mathscr M_0(t)$，只额外限制第 $i$ 位占据 $\le1$ 的闭核为 $\mathscr M_i(t)$。真实包含
$\mathscr M_i(t)\subset\mathscr M_0(t)$
和完整新头 Schur 给
$$
q_0(t)=q_g(S+t),\quad
q_i(t)=\|P_{\mathscr M_i(t)}f\|^2,\quad
s_i=S+t-z_i,
$$
$$
\ell_i(t)=q_0(t)-q_i(t)\ge0,\qquad
\gamma_i(t)=q_i(t)-q_g(s_i)\ge0 .
$$
两者准确相加为同一短差：
$$
\boxed{\ell_i(t)+\gamma_i(t)=q_g(S+t)-q_g(S+t-z_i).}
\tag{4.1}
$$
令
$$
V_g=q_g(3S)-q_g(2S-z_x)\ge0 .
\tag{4.2}
$$
旧非负 Fubini 和 $\sum_i z_i=S$ 于是直接给
$$
\boxed{
\frac1S\int_S^{2S}\sum_{i\ge x}
[\ell_i(t)+\gamma_i(t)]\,dt\le V_g.
}
\tag{4.3}
$$
取一个共同 $t_*\in[S,2S]$，使被积的全行不超过 $V_g$。非负无穷和可测、积分有限；这个选择在所有后续 $Q$ 之前，且不为每个远位另外取参数。

令 $\mathcal P_{\rm phys}$ 是同一物理压缩：所有真实远位限制至硬核，辅助 mode 取真空。定义
$$
F_0=\mathcal P_{\rm phys}P_{\mathscr M_0(t_*)}f,\qquad
F_i=\mathcal P_{\rm phys}P_{\mathscr M_i(t_*)}f .
$$
只有在共同 Fock 中有
$$
\|P_{\mathscr M_i}f-P_{\mathscr M_0}f\|^2=\ell_i.
$$
物理压缩之后用的是收缩不等式
$$
\|F_i-F_0\|^2\le\ell_i .
\tag{4.4}
$$
完整新头 Schur 的新位占据源仍给
$$
\|E_iF_i\|^2\le\gamma_i.
\tag{4.5}
$$
因此同一选择同时支付
$$
\boxed{
\sum_i\bigl[\|F_i-F_0\|^2+\|E_iF_i\|^2\bigr]\le V_g,
\qquad
\sum_i\|E_iF_0\|^2\le2V_g .
}
\tag{4.6}
$$
后式只用 $E_iF_0=E_iF_i-E_i(F_i-F_0)$ 和 $\|E_i\|\le1$。
这里 $F_0$ 是单个公共物理代表；其完整形式为
$$
F_0=\sum_{j=0}^{h-1}
\frac{(-C)^jH_C(S+t_*)^{-1}g\otimes(D^*)^j\Omega}
     {(S+t_*)^j j!}.
\tag{4.7}
$$
它不是原模型的真核向量。

全部 Fock 核使用闭 annihilator 加有界 $C$ 的自然域。当前投影列分别在有限 Fock 次数 $\le h-1$、$\le h$，所以所用一次 annihilator 和物理压缩都有明确域；并未拿形式无穷列代替核投影。所有实际远位的求和由 (4.3) 的 Tonelli 正和控制。

## 5. 原相邻旗上的精确返回

原 $V_Q$ 的定义是支撑于总尾孔 $\le Q$，且
$\Pi_{<Q}L_m v=0$；$K_Q$ 还满足完整 $L_mk=0$。
由于 $E_i$ 与 $L_m$ 交换并降低总尾孔一层，
$$
\boxed{
E_iV_Q\subset V_{Q-1},\qquad E_iK_Q\subset K_{Q-1}.
}
\tag{5.1}
$$
第一式保顶端残量：$L_mv$ 只在第 $Q$ 层，删除后只在第 $Q-1$ 层，恰是新低行约束之外。并未声称 $V_{Q-1}\subset V_Q$。

由 (1.3) 和并行稿的真实低 forcing 恒等式，所有 $F_i$ 及 $F_0$ 在 $Q$ 和 $Q-1$ 上均代表同一个 $f$。特别
$$
P_{V_Q}F_i=P_{V_Q}F_0=v_{g,Q}:=P_{V_Q}f .
\tag{5.2}
$$
令
$$
e_{0,Q}=(I-P_{V_Q})F_0=F_0-v_{g,Q},\qquad
\zeta_{g,Q}=\|e_{0,Q}\|.
$$
取第二个允许 forcing $f'=i_0a$，目标是原相邻向量 $u_{a,Q-1}$。
由 (5.1)，$E_i k_{g,Q}\in K_{Q-1}$，故准确有
$$
\begin{split}
\langle E_i u_{g,Q},u_{a,Q-1}\rangle
&=\langle E_i v_{g,Q},u_{a,Q-1}\rangle\\
&=\langle E_iF_0,u_{a,Q-1}\rangle
-\langle e_{0,Q},E_i^*u_{a,Q-1}\rangle .
\end{split}
\tag{5.3}
$$
这里真 $K_{Q-1}$ 反馈只在这一个配对中正交消失；没有删除向量
$P_{K_{Q-1}}E_i u_{g,Q}$ 本身。

也可以从各 $F_i$ 写出原未付项
$P_{U_{Q-1}}E_i(I-P_{V_Q})F_i$。
由于 $P_{V_Q}(F_i-F_0)=0$，其变化项与
$E_iF_i$ 中相同的变化项严格合并，正好得到 (5.3)，不是分别乘环境逆来估计。

## 6. 两个真实缺陷控制相邻配对弱行

(4.6) 先给
$$
\left(\sum_i
\frac{|\langle E_iF_0,u_{a,Q-1}\rangle|^2}{i+1}\right)^{1/2}
\le\sqrt{\frac{2V_g}{x+1}}\,\|u_{a,Q-1}\|.
$$
对 (5.3) 第二项使用 cut $Q-1$ 上的 (3.3)。所以得到完整界
$$
\boxed{
\begin{split}
&\left(\sum_{i\ge x}
\frac{|\langle E_i u_{g,Q},u_{a,Q-1}\rangle|^2}{i+1}
\right)^{1/2}\\
&\quad\le
\sqrt{\frac{2V_g}{x+1}}\,\|u_{a,Q-1}\|
+\left[
\frac{\|a\|}{\sqrt{x+1}}
+\sqrt{2c_x}\,\Delta_{a,Q-1}
\right]\zeta_{g,Q}.
\end{split}
}
\tag{6.1}
$$
这个界始终保同一个 $g$ 所选的公共 $t_*$、原两个 cut 和两个 forcing。

原物理投影与完整 coherent 范数给
$$
\begin{split}
\zeta_{g,Q}^2
&=\|F_0\|^2-\|v_{g,Q}\|^2\\
&\le q_g(S+t_*)-\|v_{g,Q}\|^2\\
&\le q_g(3S)-\|v_{g,Q}\|^2\\
&\le\|g\|^2-\|v_{g,Q}\|^2
=\|Z_{e,Q}g\|^2\le\Delta_{g,Q}^2 .
\end{split}
\tag{6.2}
$$
另由同源 Gram 上界，
$V_g\le\Delta_{g,Q}^2$。使用 $\|u_{a,Q-1}\|\le\|a\|$，
(6.1) 因此蕴含
$$
\boxed{
\begin{split}
&\left(\sum_{i\ge x}
\frac{|\langle E_i u_{g,Q},u_{a,Q-1}\rangle|^2}{i+1}
\right)^{1/2}\\
&\qquad\le
\sqrt{2c_x}\,\Delta_{g,Q}\Delta_{a,Q-1}
+\frac{1+\sqrt2}{\sqrt{x+1}}\,
\|a\|\,\Delta_{g,Q}.
\end{split}
}
\tag{6.3}
$$
因 $x\ge1$，可将 $\sqrt{2c_x}$ 放宽为 $2$。

这是比只保一个测试缺陷的旧弱行更具体的相邻原旗返回预算：主项保两个缺陷的乘积，另项明确带 $x^{-1/2}$。所有平方和首先在有限位集合上成立，再由非负极限得到整个无限移动行。不存在逐列强收敛再无界相加。

## 7. 量词与仍未支付的范围

同一强头的两个 forcing $g,a$ 可以不同。参数 $t_*$ 只依赖第一 forcing 及 $m,x,C$，在所有合法 $Q$ 之前选定；第二个 $u_{a,Q-1}$ 不依赖它。因此可以在原实际 cut 窗中逐项使用 (6.1)--(6.3)，不重新选择每个 cut 的来源。

本稿不把第二 forcing 默认替成任意无限原 $w$。若后续用随 $m$ 变化的强头投影逼近 $w$，须在原物理表示内证明该 forcing 投影强趋恒等，并在同一行度量下控制替换误差。原 Haar 参考与其它无限张量积真空不能仅凭名称互换。

(6.3) 仍是带 $1/(i+1)$ 的标量配对行，不是
$\sum_i\|E_i u_{g,Q}\|^2$；也没有证明所有返回测试均属于这些原相邻 $U$ 来源。完整高旗、顺次 Moore--Penrose 两端部分和与普通边界 $N=M$ 仍须后续真实预算。
