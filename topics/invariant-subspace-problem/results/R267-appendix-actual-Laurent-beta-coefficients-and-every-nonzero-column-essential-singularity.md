# R267 附录：实际根曲线的同源 Beta 系数与每个非零列的本性奇点

日期：2026-11-29（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的原曲线系数定理。** 对[同参数实际构造](R267-appendix-all-factor-complex-parameter-odd-target-and-norm-square-source.md)的每一个已经合法选定的因子族，本文证明其实际向量值函数 $X(s)p$ 对每个 $p\ne0$ 都在 $s=0$ 有本性奇点。证明使用完整原尾积的有界算子参数代入及同一 Beta 系数，处理有限个可能整块恒零的因子；不假设原交换子无零因子。

这个结论只关闭该实际曲线的可去及有限极点分支，不排除本性奇点中的稀疏强收敛子列。系数非零也不提供其经过 $CV^r$ 后的统一费用下界。

## 1. 固定原参数及合法算子代入

固定原 Haar 尾 $C=A^{(m_0)}$，$m_0\ge0$，以及前稿的同一组 $F_\nu,\zeta_\nu,d_\nu$。记
$$
A_0=(1-\zeta_0)F_0,\qquad
a=\zeta_0/\|C\|,\qquad
W=A_0/C,\qquad V=W/a.
\tag{1}
$$
$W=A_0/C$ 是有限多项式的精确除法。$W,V$ 都是原 $C$ 的非零奇多项式，零点最低次数至少一。因此它们有界、拟幂零，并且单射；最后一点来自 $V=C^kG(C)$，$k\ge1$、$G(0)\ne0$，以及原 $C$ 单射。

沿用
$$
Z_\nu(z)=(1-\zeta_\nu)F_\nu+z\zeta_\nu C/\|C\|,
\qquad e_\nu=d_\nu/2\in\mathbb N\quad(\nu\ge1),
$$
$$
T(z)=\operatorname*{SOT^*\!-\!lim}_{L\to\infty}
\prod_{\nu=1}^{L-1}Z_\nu(z)^{e_\nu},
\qquad
\kappa=\sum_{\nu\ge1}e_\nu\zeta_\nu<\infty.
\tag{2}
$$
前稿证明 $T$ 整个范数全纯；其 Cauchy 系数满足
$$
T(z)=\sum_{\ell\ge0}T_\ell z^\ell,\qquad
\|T_\ell\|\le\kappa^\ell/\ell!.
\tag{3}
$$
所有 $T_\ell$ 均与 $V$ 交换。

因此对任意 $t\in[0,1]$ 可以在原有界代数中定义
$$
T(-tV):=\sum_{\ell\ge0}(-t)^\ell T_\ell V^\ell.
\tag{4}
$$
该级数在算子范数绝对收敛，对 $t\in[0,1]$ 一致收敛。这是同一算子值 entire 函数的交换参数代入，不是将任意不交换算子塞入标量函数。

(4) 还等于原有限乘积逐因子代入后的真实强*极限：
$$
\boxed{
T(-tV)=\operatorname*{SOT^*\!-\!lim}_{L\to\infty}
\prod_{\nu=1}^{L-1}
\left((1-\zeta_\nu)F_\nu
-t\frac{\zeta_\nu}{\zeta_0}A_0\right)^{e_\nu}.
}
\tag{5}
$$
证明可先对有限乘积展开。其各系数强*收敛到 (3) 的系数；全部系数统一服从 $\kappa^\ell/\ell!$，所以代入后的幂级数尾由
$\sum_{\ell\ge L}\kappa^\ell\|V\|^\ell/\ell!$ 统一控制，得 (5)。伴随同理，因全部因子交换，其伴随也交换。

更直接的尾控制也保留：每个代入因子与 $I$ 的固定测试误差由原 $F_\nu-I$ 误差加
$\zeta_\nu(1+\|V\|)$ 控制；带重数 $e_\nu$ 后可和。任一切口以后的乘积范数至多
$$
\exp\!\left(\|V\|\sum_{\nu\ge L}e_\nu\zeta_\nu\right).
\tag{6}
$$
所以代入尾强*趋于 $I$。没有用这些带符号因子保持函数正锥。

## 2. 精确找出并提出全部恒零块

在 $t=1$ 记
$$
D_\nu=(1-\zeta_\nu)F_\nu-\frac{\zeta_\nu}{\zeta_0}A_0.
\tag{7}
$$
因为 $C$ 单射且拟幂零，非零标量多项式不可能在 $C$ 上为零：提出最低 $C$ 幂后余下是有界单位。因此 $D_\nu=0$ 等价于相应标量多项式恒等。

原 $F_\nu$ 是一段连续二进幂的正系数和。两个此类多项式成比例时，其非零幂支撑相同，故块起点和长度均相同，再由规范系数得到 $F_\nu=F_0$。把它代入 (7)，有
$$
\boxed{
D_\nu=0\quad\Longleftrightarrow\quad
F_\nu=F_0\ \text{且}\ \zeta_\nu=\zeta_0.
}
\tag{8}
$$
由于 $\zeta_\nu\to0$ 而 $\zeta_0>0$，集合
$$
E=\{\nu\ge1:F_\nu=F_0,\ \zeta_\nu=\zeta_0\}
$$
有限。置
$$
h=\sum_{\nu\in E}e_\nu\in\mathbb N_0,\qquad
\widehat T(z)=
\operatorname*{SOT^*\!-\!lim}_{L\to\infty}
\prod_{\substack{1\le\nu<L\\\nu\notin E}}Z_\nu(z)^{e_\nu},
\qquad
\widehat\kappa=\sum_{\substack{\nu\ge1\\\nu\notin E}}e_\nu\zeta_\nu.
\tag{9}
$$
删除的是已明确识别的有限个整块；所有其他原因子完整保留。对 $\nu\in E$，
$$
Z_\nu(z)=A_0+azC=aC(zI+V).
$$
因而有全域有界恒等式
$$
\boxed{
T(z)=(aC)^h(zI+V)^h\widehat T(z).
}
\tag{10}
$$
$\widehat T$ 同样范数全纯，系数 $\widehat T_\ell$ 满足
$\|\widehat T_\ell\|\le\widehat\kappa^\ell/\ell!$。

## 3. 余尾在 $-V$ 的实际全旗单射稠像

令
$$
T_*=\widehat T(-V).
\tag{11}
$$
每个未删除的 $D_\nu$ 都是非零偶多项式在 $C$ 上的值，其零点常数为零。故每个有限前缀可以准确写成
$$
A_L=\prod_{\substack{1\le\nu<L\\\nu\notin E}}D_\nu^{e_\nu}
=C^{b_L}G_L(C),
\tag{12}
$$
其中 $b_L\ge0$，$G_L(0)\ne0$，且 $G_L(C)$ 及其逆属于原范数闭多项式代数。若前缀为空，就取 $b_L=0$、$G_L=I$。

用 (5)–(6) 的实际代入尾记 $R_L$，于是
$$
T_*=A_LR_L,\qquad R_L\to I\quad\text{强*},\qquad
\|R_L\|\le e^{\,\|V\|\widehat\kappa_L}\to1.
\tag{13}
$$
这里 $\widehat\kappa_L=\sum_{\nu\ge L,\nu\notin E}e_\nu\zeta_\nu$。

选择原 R23 的多项式收缩强*单位 $E_{\ell(L)}(C)$，使 $\ell(L)\to\infty$ 且最低次数至少 $b_L$。写
$E_{\ell(L)}=C^{b_L}B_L(C)$，定义实际有界
$$
U_L=G_L(C)^{-1}B_L(C).
$$
则同一来源满足
$$
\boxed{
T_*U_L=U_LT_*=R_LE_{\ell(L)}
\longrightarrow I\quad\text{强*},
\qquad
\|T_*U_L\|\le e^{\,\|V\|\widehat\kappa_L}\to1.
}
\tag{14}
$$
若要求收缩强单位，可以再乘标量 $e^{-\|V\|\widehat\kappa_L}$。

所有因子保持原闭 $C$ 不变旗及其固定有限放大。对每个固定 Hilbert 旗子商，(14) 与其伴随正是环境强*极限的压缩。因此诱导 $T_*$ 单射且像稠密：交换 (14) 消核，右侧像逼近恒等给实际像稠密。尤其
$$
\boxed{T_*p\ne0\quad\text{对每个 }p\ne0.}
\tag{15}
$$
这个结论由真实强单位支付，不从完整交换子无零因子、范数近似或环境单射性自动下传。

## 4. 全部足够负的 Laurent 系数及同源 Beta 表示

原曲线是
$$
B(s)=\sqrt a\,s\sum_{k\ge0}\binom{1/2}{k}\frac{V^k}{s^{2k}},
\qquad X(s)=CB(s)T(s^2),
\qquad B(s)^2=a(s^2I+V).
$$
由 (10)，全部实际因子交换，故
$$
\boxed{
X(s)=C^{h+1}B(s)^{\,2h+1}\widehat T(s^2).
}
\tag{16}
$$
取 $\alpha=h+\tfrac12$。对每个 $s\ne0$，$V$ 拟幂零支付同一范数收敛级数
$$
B(s)^{2h+1}
=a^\alpha s^{2h+1}
\sum_{k\ge0}\binom{\alpha}{k}\frac{V^k}{s^{2k}}.
\tag{17}
$$
这不重新选取根支；它是原 $B(s)$ 的实际整数幂。

设 $\mathcal A_r$ 为 $X(s)$ 的 $s^{\,2h+1-2r}$ Laurent 系数。对每个整数 $r\ge h+1$，即全部负奇数指数，有
$$
\mathcal A_r
=a^\alpha C^{h+1}
\sum_{\ell\ge0}
\binom{\alpha}{r+\ell}V^{r+\ell}\widehat T_\ell.
\tag{18}
$$
级数绝对收敛。准确的二项式比值为
$$
\frac{\binom{\alpha}{r+\ell}}{\binom{\alpha}{r}}
=(-1)^\ell\frac{(r-\alpha)_\ell}{(r+1)_\ell}.
$$
对概率测度
$$
d\beta_r(t)=
\frac{t^{\,r-\alpha-1}(1-t)^\alpha}
{\mathrm B(r-\alpha,\alpha+1)}\,dt,\qquad 0<t<1,
\tag{19}
$$
有
$\int t^\ell\,d\beta_r=(r-\alpha)_\ell/(r+1)_\ell$。两参数都严格为正。代入 (18)，得到完整同源公式
$$
\boxed{
\mathcal A_r
=a^\alpha\binom{\alpha}{r}C^{h+1}V^r H_r,\qquad
H_r=\int_0^1\widehat T(-tV)\,d\beta_r(t).
}
\tag{20}
$$
积分是 $B(H)$ 范数 Bochner 积分；(3) 的剩余系数界支付逐项交换。这里没有把 Beta 平均先宣布为 quasiaffinity。

## 5. 定量锚与每个非零实际列的本性

令
$$
L_*=\widehat\kappa\|V\|e^{\widehat\kappa\|V\|}.
$$
由 $\widehat T$ 的同一系数界，直接逐项求和得
$$
\|\widehat T(-tV)-\widehat T(-V)\|
\le L_*(1-t),\qquad 0\le t\le1.
$$
而 (19) 的平均为
$\int(1-t)\,d\beta_r=(\alpha+1)/(r+1)$。所以
$$
\boxed{
\|H_r-T_*\|
\le \frac{\alpha+1}{r+1}L_*
=\frac{h+3/2}{r+1}L_*
\longrightarrow0.
}
\tag{21}
$$
固定任意 $p\ne0$。由 (15)、(21)，存在依赖于同一 $p$ 的 $r_p$，使
$$
\|H_rp\|\ge\tfrac12\|T_*p\|>0
\qquad(r\ge r_p).
\tag{22}
$$
$C^{h+1}V^r$ 单射，且 $\binom{\alpha}{r}\ne0$。因此 (20) 给
$$
\boxed{\mathcal A_rp\ne0\qquad(r\ge\max(h+1,r_p)).}
\tag{23}
$$
这说明实际向量值函数 $X(s)p$ 的范数 Laurent 展开含无穷多个非零负项；其零点是真正的本性奇点。特别 $p=\Omega$ 以及任意指定 $p=P_t\Omega$ 都在此范围，未将别的向量代入原列。

(22) 只发生在 $H_r$ 后、$C^{h+1}V^r$ 前。由于这个注入算子的像不闭，本文不从 (22) 推出
$\|\mathcal A_rp\|$ 的任何统一正下界，也没有反转其费用。这是 (20) 中必须保留的同源作用次序。

## 6. 实际后继

前稿的有限极点分支作为一般逻辑仍然正确，但对本构造的实际完整 $X$，§§2–5 已排掉该分支，不需假设没有超不变子空间。

本文没有排除某个稀疏 $s_j\to0$ 使 $X(s_j)\Omega$ 有强极限；向量值本性奇点本身不作这种推断。下一步仍需估计完整 (20) 或其重组后的同一列，或换一个真正不同的有界平方来源。固定分母 $Q_*$、原 $X(s)^2\to CQ_*^2$ 的范数预算和单真空列充分条件，均保持[固定原分母稿](R267-appendix-fixed-original-denominator-and-norm-square-vacuum-source.md)的准确范围。普通 ISP 仍未完成。
