# R249：经实二次诱导闭合实际 CM 中心值的秩零接口

日期：2026-11-13。状态：**已证明，仍保留准确中心值非零的前提。**
本篇处理 R181 §7 的阶四 CM 因子。它将实际四维张量改写为实二次域上
一个平行权二、平凡中心角色 Hilbert CM 形式的诱导，应用 Nekovář
已刊 Theorem B(c)。这闭合 CM 因子的算术接口；R181 对原 KLZ
Hyp(BI) 不成立的证明仍正确。

## 1. 结论与规范

保持 R166/R181 的实际小惯性分支，设 $p>37$、$\theta$ 阶为四，

$$F=\mathbb Q(\sqrt{-p}),\qquad
\Xi=(\theta\vartheta^{\pm1})\circ\lambda,\qquad
\rho=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\Xi.$$

这里 $K$ 为实际非分裂 Cartan 商域，$p$ 在 $K$ 未分歧且惰性，
故 $F\ne K$；$\Xi$ 阶为十二，$\Xi^c=\Xi^{-1}$，且

$$\Xi^6=\chi_F|_{G_K}. \tag{249.1}$$

令 $f$ 为 R181 §5 的任一个权二、平凡 nebentype、水平 $p^2$ 的
CM 新形式；其 CM 域恰为 $F$。辅助系数素数记 $\ell$，避免与水平
$p$ 混淆。$V_{f,\eta}$ 始终采用**协变 Tate 规范**；它是
Nekovář 的 $V_\eta(f)(1)$，行列式为 $\ell$ 进圆分角色 $\epsilon_\ell$。

**定理 249.1。** 若

$$L\!\left(\tfrac12,\pi_{f,K}\otimes\Xi\right)\ne0, \tag{249.2}$$

则存在辅助系数素数 $\eta\mid\ell$ 使

$$\boxed{H_f^1\!\left(\mathbb Q,
 V_{f,\eta}\otimes\rho\right)=0.} \tag{249.3}$$

准确地说，$\ell$ 可取于下文指定的完全分裂素数集，删去有限多个
坏素数；不声称对每个 $\ell$，或对本题的水平素数 $p$，有同一结论。
由 R172 §7 的真实中央数域 Kummer 拼接，属于这个实际完整有理
Hecke/有限角色轨道的商 $B$ 满足 $B(\mathbb Q)$ 有限；每个实际
连通分支上的投影像 $B_\alpha$ 也有有限有理点群。若指定整行是
单位，则它同时保证 $B_\alpha\ne0$，并给 R181 §4 的形式浸入。

因此在 R213 的非消失输出中，可以保留 CM 形式。阶四的准确可用
中心值门槛恢复为未经筛选的

$$\boxed{
p>\frac{a_D^2\,4^{\omega(D)}16^{\omega(a_0)}
\mathcal T(Da^2)^2Da^2}{h(\mathcal O_a)\mathcal L_a^2},
} \tag{249.4}$$

其中各符号与 R213 相同，$a=c$ 或 $bc$ 是这个实际角色的准确
prime-to-$p$ 环类导子。R236/R238 的非 CM 投影仍是独立成立的
更强谱结论；为取得有限商，不再需要其额外因子二。

## 2. 实际四维系统的第二种诱导

置

$$L=KF,\qquad R=L^+.$$

$L/\mathbb Q$ 是双二次 CM 扩张，$R$ 是其中唯一实二次子域。
在足够大的有限系数域中，CM 分解给

$$V_{f,\eta}=\operatorname{Ind}_{G_F}^{G_{\mathbb Q}}\psi_\eta,
\qquad \psi_\eta\psi_\eta^c=\epsilon_\ell|_{G_F}.$$

设 $\Psi_\eta=(\psi_\eta|_{G_L})(\Xi|_{G_L})$。两个二次子群
$G_F,G_K$ 乘积为 $G_{\mathbb Q}$，交为 $G_L$，故 Mackey 的
张量诱导恒等式和诱导传递性给

$$\begin{aligned}
W_\eta:=V_{f,\eta}\otimes\rho
&\simeq\operatorname{Ind}_{G_L}^{G_{\mathbb Q}}\Psi_\eta\\
&\simeq\operatorname{Ind}_{G_R}^{G_{\mathbb Q}}U_\eta,
\qquad U_\eta:=\operatorname{Ind}_{G_L}^{G_R}\Psi_\eta.
\end{aligned} \tag{249.5}$$

这不是把 $K$ 改成另一个可自由选择的原始 Cartan 商域；$K$ 和
$\Xi$ 始终保留。$R$ 是用来实现同一个 $W_\eta$ 的另一底域。

设 $c\in G_R$ 为任一真实复共轭；它在 $L$ 上同时非平凡地作用于
$F$ 和 $K$。于是

$$\Psi_\eta\Psi_\eta^c=\epsilon_\ell|_{G_L}. \tag{249.6}$$

由此 $\det U_\eta/\epsilon_\ell$ 在 $G_L$ 上平凡，至多为
$L/R$ 的二次字符。而在 $c^2=1$ 处，诱导的陪集矩阵有行列式
$-\Psi_\eta(c^2)=-1=\epsilon_\ell(c)$。因此

$$\boxed{\det U_\eta=\epsilon_\ell|_{G_R}.} \tag{249.7}$$

特别没有一个未追踪的二次 nebentype。

## 3. $U$ 是平行权二的 Hilbert CM 系统

令 $\psi$ 为产生 $f$ 的代数 Hecke 角色，取与上述 Tate 实现相配的
互反规范。其无穷型为 $(1,0)$，在 $F$ 的共轭嵌入上交换。
对应 $\Psi_\eta$ 的代数 Hecke 角色为

$$\Psi=(\psi\circ N_{L/F})(\Xi\circ N_{L/K}). \tag{249.8}$$

第二因子有限阶。$R$ 的两个实嵌入各在 $L$ 中延拓为一对共轭
复嵌入；在每一对上，$\Psi$ 的无穷指数恰为 $1,0$。
因此 Hecke 的 CM theta 构造给 $R$ 上平行权二的 Hilbert 形式
$g=\theta_{L/R}(\Psi)$。这里使用角色自身的准确导子，取对应的
primitive 新形式；没有要求该导子平方自由或与 $D_R$ 互素。

因为 $\Psi/\Psi^c$ 在无穷处非平凡，它不可能是平凡角色；故
这个 theta 形式为尖点形式。其 Galois 系统满足

$$V_\eta(g)(1)\simeq U_\eta.$$ 

这项对应可直接在未分歧素数比较诱导的迹与 theta 系数，再由
Chebotarev 和半单性识别。它是 Hilbert theta 构造本身的 Galois
实现，不以 $g$ 对应某个尚待构造的 $R$ 上阿贝尔簇为前提。

由 (249.7)，$g$ 的 nebentype 为平凡角色。相同的 Hecke/Weil
诱导在全部有限处和无穷处给准确 Euler 因子等式，因而

$$\boxed{L(g,1)=L(f_K,\Xi,1),\qquad
L(g,1)\ne0\ \Longleftrightarrow
L\!\left(\tfrac12,\pi_{f,K}\otimes\Xi\right)\ne0.}
\tag{249.9}$$

式中第一项与中项使用经典中心 $1$；最后一项使用酉中心 $1/2$。
若最后一项包含无穷 Gamma 因子，等式只差该中心处有限非零的
Gamma 因子。没有删除共同坏处 Euler 因子，也没有另加 Tate 扭曲。

为核准实际系统没有分裂成漏记的更小块，(249.1) 给
$\Xi|_{G_L}$ 恰有阶六。$\operatorname{Gal}(L/\mathbb Q)$ 中只翻转
$K$ 的元素把 $\Psi$ 乘以非平凡的 $\Xi^{-2}|_{G_L}$，其阶为三；
翻转 $F$ 的元素则改变无穷型。故 $\Psi$ 的四个共轭两两不同，
Mackey 不可约判据给 $W_\eta$ 绝对不可约。

## 4. 明确实现 Nekovář 的无限阶条件

Nekovář 的 Theorem B(c)，发表于 *Canadian Journal of Mathematics*
**64** (2012), p.593，适用于平行权二、平凡 nebentype 的 Hilbert
尖点形式。除 $L(g,1)\ne0$ 外，它要求一个 $s_\eta\in G_R$，在
$V_\eta(g)(1)$ 上有本征值 $\lambda_1,\lambda_2$，满足
$\lambda_1^2=1\ne\lambda_2^2$；CM 情形另要求 $\lambda_2$ 为无限阶。
其结论为 $H_f^1(R,V_\eta(g)(1))=0$。

这正是该文 Theorem A 的 (A1)、(A2)；因中心角色平凡，(A1)
自动满足。Theorem B(c) 不要求此处的 $s_\eta$ 满足针对一个已指定
CM 扩张的 (A3)。原文 §2.10.5(c)，p.641，另选独立辅助 CM 扩张
并应用 Theorem A；所以不能把原问题中 $F\subset K(\Xi)$ 的障碍
误加回这个 Theorem B。

现在明确构造 $s_\eta$。选有限 Galois 数域 $Z$，包含 $L$、
$g,f,\psi$ 的系数域，以及 $\Xi$ 的有限角色域。取 $\ell\ge5$
完全分裂于 $Z$，且避开上述全部准确导子。这样的 $\ell$ 有无穷多个。
固定一个 $v\mid\ell$ 的 $R$ 素数及其 $L$ 上的素数 $w$；有

$$R_v=L_w=\mathbb Q_\ell.$$

相应分解群 $G_{R_v}$ 是固定嵌入下的 $G_R$ 子群；因为 $L/R$
在 $v$ 完全分裂，它也落在 $G_L$ 中。在惯性群 $I_v$ 上，
$\Xi$ 为平凡角色。CM Hecke 角色在这个完全分裂好素数处的两个
$\ell$ 进分量，无穷指数分别为 $0,1$；局部互反公式在单位上给
平凡角色与圆分角色。因此

$$\left.U_\eta\right|_{I_v}
\simeq 1\oplus\epsilon_\ell|_{I_v}. \tag{249.10}$$

更直接地，有限导子部分在 $\mathbb Z_\ell^\times$ 上平凡，
指数零的分量为一，另一分量由行列式 (249.7) 强制为
$\epsilon_\ell$。这也固定了互反规范可能导致的表观逆号。

$\epsilon_\ell(I_v)=\mathbb Z_\ell^\times$，故可取
$s_\eta\in I_v\subset G_R$ 使

$$U_\eta(s_\eta)\sim
\begin{pmatrix}1&0\\0&1+\ell\end{pmatrix}. \tag{249.11}$$

$1+\ell$ 在 $\mathbb Q_\ell^\times$ 中为无限阶，所以全部所需
条件成立。特别 $\lambda_2\equiv1\pmod\ell$ 并不构成问题：
Theorem B(c) 在此要求的是**特征零本征值**条件，未要求
$\lambda_2-1$ 为整单位。我们不从 (249.11) 推出任何 KLZ 的
自由秩一整余核条件。

由 (249.2)、(249.9) 和这个已核输入，得到

$$\boxed{H_f^1(R,U_\eta)=0.} \tag{249.12}$$

这里只使用原文的有理 Selmer 消失。原文进一步的挠系数消失有
额外有限例外集；本文不将该有限例外集省略，也不声称任意整格
或全部辅助素数同时消失。

## 5. Bloch–Kato 条件与 Shapiro

由 (249.5)，全局 Shapiro 给

$$H^1(\mathbb Q,W_\eta)\simeq H^1(R,U_\eta).$$

它保持这里的所有 Bloch–Kato 局部条件，理由如下。

在有理素数 $q\ne\ell$，局部分解是对 $v\mid q$ 的诱导直和；
进一步限制到惯性后，Mackey 分解和局部 Shapiro 将惯性限制映射
对应到各个 $I_v$ 的限制映射。因此“不分歧上同调类”，即到
惯性一阶上同调映射的核，恰好相互对应。这对 $R/\mathbb Q$
在 $q$ 分歧也成立，不要求所有扩张未分歧。

在 $q=\ell$，我们已特意使 $\ell$ 完全分裂于 $R$。于是局部
分解仅为两份 $G_{\mathbb Q_\ell}$ 模的直和，$B_{\rm cris}$
定义的局部有限条件逐份相同。无穷处因 $\ell\ne2$ 无一阶
上同调障碍。

故

$$H_f^1(\mathbb Q,W_\eta)
\simeq H_f^1(R,U_\eta)=0. \tag{249.13}$$

这证明 (249.3)。同样，也可经 $K$ 的诱导写成
$H_f^1(K,V_{f,\eta}|_{G_K}\otimes\Xi)=0$；两种 Shapiro
表达式描述的是同一个实际系统。

## 6. 接回真实商与所有指定整行

R166/R181 在完整实际不连通曲线上给 Hecke 代数和有限中心的
交换半单有理作用。取实际配对轨道的原始有理幂等元 $e$，
令 $B=e\mathscr J$，$A=e\mathcal A$ 为其中央数域。
在对应 $W_\eta$ 的系数嵌入 $\iota:A\hookrightarrow\overline{\mathbb Q}_\ell$
处，实际等变分解给

$$e_\iota(V_\ell B\otimes\overline{\mathbb Q}_\ell)
\simeq W_\eta^{\oplus m}.$$

由 (249.13)，这一分量的 $H_f^1$ 为零。若
$B(\mathbb Q)\otimes\mathbb Q$ 非零，它作为 $A$ 向量空间在每个
系数嵌入处分量均非零；$A$ 等变的 Kummer 注入与上述消失矛盾。
故 $B(\mathbb Q)$ 有限，$B_\alpha\subset B$ 的有理点也有限。

本证明不要求重新假定 $B$ 为 $\mathrm{GL}_2$ 型，亦不需要
假定不同复共轭的中心值均已非零；一个实际中央嵌入的 Selmer
消失已足够。可能的 Schur 指数按 R172 §7 的同一除环/Kummer
论证处理。

阶四 CM 形式在一个连通分支上可能只保留一个 PSL$_2$ 半型。
R181 §4 的整行证明已经允许限制映射有核：所有实际拉回、平均
投影及指定 Whittaker 泛函先在完整有限 $R_\theta$ 模上进行，
再限制到指定分支。故此处不由 CM 秩零额外声称两个半型都非零；
只使用该文已证的准确充分方向：**一个实际单位行给该分支上的
非零有限商和形式浸入。**

## 7. 无 CM 筛的有效共同导子整性门槛

R213 的相对迹谱和为非负项之和，且 (249.4) 使主项严格超过
误差，故至少有一个准确 $\theta,\Xi$ 的非零中心值。若其形式
非 CM，用 R172；若有 CM，用定理 249.1。两个三次方向和所需
Mellin 阶分别照此选择，完整有理轨道及整行仍按 R173/R181
保留。旧三次 Steinberg 行沿用 R87/R72。

于是 R177 的全类型共同单位理想给与 R238 相同的整性结论，
而常数可降回 R213 的

$$\boxed{C_\epsilon^{\rm CM}=
2592X_{\epsilon/4}T_{\epsilon/8}^{\,2}\beta_{\epsilon/2}^{-2}.}
\tag{249.14}$$

确切地，令 $M^*=D(bc)^2$；则

$$\boxed{
p\ge C_\epsilon^{\rm CM}
\frac{(M^*)^{1+\epsilon}}{h(\mathcal O_{bc})}
\quad\Longrightarrow\quad j(E)\in\mathbb Z.
} \tag{249.15}$$

R214 给 $(bc)_D\mid36$，所以 $a_D^2\le1296$；R213 的逐素数
有限积估计上界为 (249.14) 的一半，多出的因子二把非严格
(249.15) 转成严格 (249.4)。从 $a=c$ 到 $bc$ 的类数比单调性
保留单位指数 $[\mathcal O_K^\times:\mathcal O_a^\times]$，见
R213/R238；不把 $a=1$ 时的单位数错误地固定成统一常数。
同一个常数也覆盖旧 Steinberg 输入。

上述结论的指数范围与 R238 相同，但其算术前提已覆盖全部
CM 因子。仍没有共同导子 $bc$ 的上界，没有排除所有整 $j$ 的
异常曲线，也没有完成 Serre 一致性。

## 8. 已刊输入与准确来源

1. Jan Nekovář，*Level raising and anticyclotomic Selmer groups for Hilbert
   modular forms of weight two*，*Canadian Journal of Mathematics*
   **64** (2012), 588–668，DOI
   [10.4153/CJM-2011-077-6](https://doi.org/10.4153/CJM-2011-077-6)。
   [出版社全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A11114CBB9FC75C2DBF56F766BFE7BF/S0008414X00009196a.pdf/level_raising_and_anticyclotomic_selmer_groups_for_hilbert_modular_forms_of_weight_two.pdf)。
   本文直接使用 p.593 的 Theorem B(c)；(A1)、(A2) 的完整 CM
   条件见 p.592 Theorem A。原文 p.641 §2.10.5(c) 明确通过
   新选辅助 CM 扩张证明 B(c)，p.664–665 Proposition B.6.5
   对 CM 的无限阶条件另有完整刻画。这里只用有理 Selmer 结论。
2. Haruzo Hida，*On abelian varieties with complex multiplication as factors
   of the abelian variety attached to Hilbert modular forms*，
   *Japanese Journal of Mathematics, New Series* **5** (1979), 157–208，
   DOI [10.4099/math1924.5.157](https://doi.org/10.4099/math1924.5.157)。
   [原刊 PDF](https://www.jstage.jst.go.jp/article/math1924/5/1/5_1_157/_pdf/-char/en)。
   p.197 §5.1–5.3（特别 Proposition 5.2），p.198 §5.4 给所用
   CM Hilbert theta 构造、准确导子与 Hecke Euler 因子。本文不
   使用该文有关 Hilbert 形式的阿贝尔簇存在性结论。
3. 同一 theta/Galois 诱导对应的已刊明述可核 B. Balasubramanyam,
   E. Ghate, V. Vatsal，*On local Galois representations associated to
   ordinary Hilbert modular forms*，*Manuscripta Mathematica* **142**
   (2013), 513–524，DOI
   [10.1007/s00229-013-0614-1](https://doi.org/10.1007/s00229-013-0614-1)，
   [作者稿](https://mathweb.tifr.res.in/~eghate/hilbertCM.pdf)，§1 p.2。
   此处不调用该文含额外残余像前提的主要非 CM 定理。

本篇为纯证明交付，无数值数据或运行脚本。下载的两篇 primary PDF
仅为核读来源，不是结论所需的数据附件。
