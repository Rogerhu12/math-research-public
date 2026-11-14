# R236 附录：原正常正湮灭态的多项式柱尾下界与临界最高位置矩发散

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：以下定理及常数已逐项核验。对原有界慢行，任意秩的正常正湮灭态必须有明确的多项式柱尾；相应临界最高位置矩发散。这仍允许更慢的正常尾，未排除一般正常见证。

[已有 R213](R213-walsh-block-deletion-and-coefficient-tail-kernel-obstruction.md) §6.13–6.17 对指定危险闭分支的核向量给过系数平方尾量级及位置矩发散。本稿的新增对象是任意秩正常正湮灭态和有限放大零商，使用原解析代数中的收缩测试及密度正性；不把核向量结论直接移用。实际截断及混合 N/Y 关系沿[原 carry 常数](R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)，正常旗沿[完整原右源](R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)。

## 1. 原对象与定理

在原 Haar 空间逐位取 $X_i\in\{N_i,Y_i\}$，其中
$Y_i=N_i(I+N_i)^{-1}$，原 $N_i$ 是交换的拟幂零收缩。令 $\mathcal A$ 为其原范数闭含单位解析代数。两种选择生成同一代数，因为
$$Y_i=N_i(I+N_i)^{-1},\qquad N_i=Y_i(I-Y_i)^{-1},$$
两逆均由拟幂零的实际幂级数给出。使用
$$\|X_i\|\le3,\quad\|X_i-E_i\|\le4\eta_i,\quad
\eta_i\le \exp(-770\,16^i),$$
及在第 P 位保真截断时
$$\|X_i-X_i^{[P]}\|\le9\eta_{P-1}\quad(i<P),$$
其中 $X_i^{[P]}$ 只作用于前 P 位。

设
$$X=\sum_{i\ge0}a_iX_i,\qquad |a_i|\le A(i+1)^{-2},$$
且 $i\ge J$ 时 $|a_i|\ge a_-(i+1)^{-2}$，其中 $A,a_->0$。允许任意复相位和有限首位例外。固定同一正常正迹类 $\rho$，$\tau=\operatorname{Tr}\rho>0$，并假设原零式
$$\operatorname{Tr}(\rho XG)=0\qquad(G\in\mathcal A). \tag{1.1}$$
若原见证给全部 $\mathcal A'$ 右零式，则包含 (1.1)；若来自原旗上的 $\pi(X)=0$，也由原解析同态直接得到 (1.1)。

记 $\Omega_+$ 为尾的 Haar 真空，$\Pi_P$ 为前 P 位任意、其余位固定为 $\Omega_+$ 的物理柱投影。令
$$q_P=\operatorname{Tr}\rho(I-\Pi_P).$$

**定理。** 存在仅依 $A,a_-,J$ 及原 carry 的 $P_0$，使所有 $P\ge P_0$ 都有
$$\boxed{\frac{q_P}{\tau}\ge
\frac{(a_-/A)^2}{9\cdot2^{30}P^3}.}\tag{1.2}$$
阈值不依 $\rho$、其秩或有限放大维数。特别也可把右侧常数改为较小的 $(a_-/A)^2 2^{-34}$。

## 2. 从原复系数选择一组实际正 Cayley 因子

把 $I_P=\{P,\ldots,2P-1\}$ 中的 $a_i$ 相位分为四个闭扇区，边界一致分配。选择平方质量最大的组 F，设其中心角为 $\vartheta$，并置
$$c_i=|a_i|\quad(i\in F),\qquad B=(\sum_{i\in F}c_i^2)^{1/2}.$$
于是
$$\operatorname{Re}(e^{-i\vartheta}a_i)\ge c_i/\sqrt2\ge 2c_i/3,$$
$$\boxed{B^2\ge\tfrac14\sum_{i=P}^{2P-1}|a_i|^2
\ge \frac{a_-^2}{64P^3},\qquad \sum_Fc_i\le\sqrt P\,B.}\tag{2.1}$$

用原真正 Cayley 元及其纯位模型
$$V_i=(I-N_i)(I+N_i)^{-1}=I-2Y_i,\qquad D_i=I-2E_i.$$
原收缩性给
$$\operatorname{Re}V_i=(I+N_i^*)^{-1}(I-N_i^*N_i)(I+N_i)^{-1}\succeq0.$$
又 $\operatorname{Re}D_i=I-E_i-E_i^*\succeq0$，且安全界
$\|V_i-D_i\|\le18\eta_i$ 成立。置
$$L=\sum_Fc_iV_i,\quad L_0=\sum_Fc_iD_i,\quad t=12B,$$
$$H=t(t+L)^{-1},\qquad H_0=t(t+L_0)^{-1}. \tag{2.2}$$
两个 L 都增生，故
$$\|H\|,\|H_0\|\le1. \tag{2.3}$$
同时 H 是原 $\mathcal A$ 中的真正元素：写 $L=sI-2Z$，其中
$s=\sum_Fc_i>0,\ Z=\sum_Fc_iY_i$。有限交换拟幂零和 Z 的谱半径为零，故
$((t+s)I-2Z)^{-1}$ 的实际幂级数范数收敛。这里的代数成员身份和收缩范数分别有独立依据。

## 3. 纯尾的明确非零锚

以 $\chi_i$ 表示第 i 位 Walsh minus 向量，令 $w=\sum_Fc_i\chi_i$。
有
$$L_0\Omega_+=w,\qquad\|w\|=B,$$
$$L_0^2\Omega_+=-B^2\Omega_+
+2\sum_Fc_i^2\chi_i
+2\sum_{i<j,\ i,j\in F}c_ic_j\chi_i\chi_j.$$
各项正交，故
$$\|L_0^2\Omega_+\|^2=3B^4+2\sum_Fc_i^4\le5B^4\le9B^4.$$
准确预解身份
$$H_0=I-L_0/t+H_0L_0^2/t^2$$
于是给
$$H_0\Omega_+=\Omega_+-w/t+r,\qquad\|r\|\le1/48. \tag{3.1}$$
若 $g_i$ 为 $H_0\Omega_+$ 的一次 Walsh 系数，则 Cauchy–Schwarz 与 (2.1) 给
$$\begin{aligned}
\operatorname{Re}\!\left(e^{-i\vartheta}\sum_Fa_ig_i\right)
&\le-\frac{2B^2}{3t}+\frac B{48}\\
&=-\frac{5B}{144}\le-\frac B{32}.
\end{aligned}\tag{3.2}$$

记尾真空态 $\omega(U)=\langle\Omega_+,U\Omega_+\rangle$，并取
$$G=H-\omega(H)I,\qquad G_0=H_0-\omega(H_0)I.$$
它们范数不超过 2，真空均值准确为零；G 属原 $\ge P$ 尾解析代数。对
$X_{\rm tail}^0=\sum_{i\ge P}a_iE_i$，
$$\kappa_0:=\omega(X_{\rm tail}^0G_0)=\frac12\sum_Fa_ig_i.$$
因为 $G_0$ 只作用于 F 且均值零，未选位贡献准确消失。因此
$$|\kappa_0|\ge B/64. \tag{3.3}$$

## 4. 全部真实尾误差及原头 carry

由预解差及 (2.1)，
$$\|H-H_0\|\le\|L-L_0\|/t\le\tfrac32\sqrt P\,\eta_P,$$
$$\|G-G_0\|\le3\sqrt P\,\eta_P.$$
令 $s_P=\sum_{i\ge P}|a_i|\le A/P$。原尾
$X_{\rm tail}=\sum_{i\ge P}a_iX_i$ 满足
$$\|X_{\rm tail}-X_{\rm tail}^0\|\le4s_P\eta_P,\qquad
\|X_{\rm tail}^0\|\le s_P.$$
所以 $\kappa=\omega(X_{\rm tail}G)$ 满足
$$|\kappa-\kappa_0|
\le8s_P\eta_P+3s_P\sqrt P\,\eta_P
\le11A P^{-1/2}\eta_P. \tag{4.1}$$
取 P 足够高使这不超过 $B/128$，得到 $|\kappa|\ge B/128$。
这个阈值由 (2.1) 可选为 $\rho$ 无关。

另有准确分解
$$X=X_{<P}^{[P]}+X_{\rm tail}+R_P,\qquad
\|R_P\|\le18A\eta_{P-1}.$$
因为 G 是纯 $\ge P$ 尾算子且 $\omega(G)=0$，原头项的柱压缩准确为零，故
$$\boxed{\Pi_PXG\Pi_P=\kappa\Pi_P+\Pi_PR_PG\Pi_P.}\tag{4.2}$$
误差范数不超过 $36A\eta_{P-1}$。再取 P 高到
$36A\eta_{P-1}\le B/256$；由 (2.1)，阈值仍只依原系数与 carry。
没有把低位 carry 写成 $\eta_P$，也没有删除实际头误差。

## 5. 用同一正密度支付原来源

置 $\rho_P=\Pi_P\rho\Pi_P,\ \tau_P=\tau-q_P$。正性和 Hilbert–Schmidt 乘积界直接给
$$\begin{aligned}
\|\rho-\rho_P\|_1
&\le\|(I-\Pi_P)\rho^{1/2}\|_2\|\rho^{1/2}\|_2\\
&\quad+\|\Pi_P\rho^{1/2}\|_2\|\rho^{1/2}(I-\Pi_P)\|_2\\
&\le2\sqrt{\tau q_P}.
\end{aligned}\tag{5.1}$$
由 (4.2) 及 $\rho_P\ge0$，
$$\frac B{256}\tau_P\le|\operatorname{Tr}\rho_PXG|.$$
原 (1.1)、$\|X\|\le6A$ 和 $\|G\|\le2$ 因而给
$$\frac B{256}\tau_P
\le\|\rho-\rho_P\|_1\|XG\|
\le24A\sqrt{\tau q_P}. \tag{5.2}$$
若 $q_P\le\tau/2$，则
$$\frac{q_P}{\tau}\ge\frac{B^2}{(12288A)^2}
\ge\frac{(a_-/A)^2}{9\cdot2^{30}P^3}.$$
若 $q_P>\tau/2$，该更弱下界自动成立，因为 $a_-\le A$。定理得证，无需先选依赖 $\rho$ 的正常尾阈值。所有投影与算子张量恒等到有限放大后，常数不变。

## 6. 最高位置的临界三阶正矩必须发散

在 Walsh 基定义正的最高位置算子
$$\mathsf M\chi_F=(1+\max F)\chi_F\quad(F\ne\varnothing),\qquad
\mathsf M\chi_\varnothing=0.$$
原 $\Pi_P$ 恰为 $\mathsf M\le P$ 的谱投影。因此对任意正幂 b，Tonelli 或离散分部求和给
$$\operatorname{Tr}\rho\mathsf M^b
=\sum_{P\ge0}\bigl((P+1)^b-P^b\bigr)q_P.$$
取 $b=3$，由 (1.2) 右侧支配调和级数，得到
$$\boxed{\operatorname{Tr}\rho\mathsf M^3=\infty.}\tag{6.1}$$
所以有限第三最高位置矩的正正常密度不可能满足原 (1.1)。这是同一正 $\rho$ 的可相加能量，不是非正输运 $K_\rho$ 的矩，也不等同于 Walsh 次数的指数矩。

## 7. 一般幂尾的明确推论

同一证明适用于 $p>1$ 及
$$|a_i|\le A(i+1)^{-p},\qquad
|a_i|\ge a_-(i+1)^{-p}\quad(i\ge J).$$
仍选择同一大小 P 的四扇区块，得到
$$B^2\ge a_-^2\,2^{-2p-2}P^{1-2p},\qquad
\|X\|\le3A\zeta(p).$$
尾的 $\ell^1$ 界及超小 carry 仍付 (4.1)–(4.2) 的相应阈值。式 (5.2) 一般写为
$(B/256)\tau_P\le4\|X\|\sqrt{\tau q_P}$，于是
$$\boxed{\frac{q_P}{\tau}\ge
\frac{(a_-/A)^2}{9\zeta(p)^2\,2^{2p+24}}P^{1-2p},\qquad
\operatorname{Tr}\rho\mathsf M^{2p-1}=\infty.}\tag{7.1}$$
当 $p=2$ 时用 $\zeta(2)\le2$ 恰回 (1.2) 的常数。此节只改变明确系数尺度，原正常源与有限放大均保持。

## 8. 方法的实际费用及剩余范围

$XG/\kappa$ 是原主理想中的柱压缩单位；其完整全域源范数仅为 $O(P^{3/2})$，柱误差是多项式乘真实 carry。全域输出范数没有因此一致有界，不由此宣布强主理想闭包含单位。

这类有界、均值零的纯尾测试，其锚量级有明确上限。任意这样的 U 满足
$$|\omega(X_{\rm tail}^0U)|
\le\tfrac12\left(\sum_{i\ge P}|a_i|^2\right)^{1/2}\|U\|.$$
证明是 $(X_{\rm tail}^0)^*\Omega_+$ 只有真空与一次 Walsh 部分，零均值删除真空后应用 Cauchy–Schwarz；实际尾仅另加 $4s_P\eta_P\|U\|$。因此不能把本方法的锚免费提升成固定常数。

本稿排除 $q_P=o(P^{-3})$ 及有限第三最高位置矩的所有原正正常见证，并保任意复相位、逐位 N/Y 和任意秩。一般更慢的正常尾及两行共同零式仍须继续处理；普通 ISP 保持开放。
