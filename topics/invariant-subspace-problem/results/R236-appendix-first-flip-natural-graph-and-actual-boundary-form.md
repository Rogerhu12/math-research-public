# R236 附录：指定first-flip的真核图、自然闭商和实际边界型

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的原见证条件等价归约。** 本稿只使用指定 N 型二次式、同一个真实核和实际首位 gauge。
将首位非零配对条件准确写成一个最大自然商在真实核图上的边界双线性型。
同时保留全部闭域、实际进位、完整右交换子作用和原正常见证的图范数。
尚未证明这个特定边界型必非零，也未将任意正常态的慢尾例子当作实际见证。

## 1. 原二次式的准确首位物理矩阵

固定[真实 first-flip 稿](R236-appendix-carry-corrected-first-flip-n-pair-and-next-k-lift.md)
§1 的原 N 型二次式。把其首支撑记为 k，设
$$
a=a_k>0,\qquad
S=\sum_{i>k}a_iN_i,\qquad
Z=\sum_{i>k}a_i^2N_i-\sum_{i>k}a_i^2N_i^2.
$$
注意 Z 包含全部原 carry 项。
令
$$
R=S^2+Z,\qquad
t=N_k^2=\eta_kN_{k+1}.
$$
原准确二次式就是
$$
\boxed{T_N=2aN_kS+R.}
\tag{1.1}
$$
在第 k 位物理分块、并压去它之前不参与算子的有限头后，
$$
N_k=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
T_N=\begin{pmatrix}R&2atS\\2aS&R\end{pmatrix}.
\tag{1.2}
$$
S,R,t 都作用在真实下一尾 $\mathcal H_{\rm tail}$，两两交换且对原尾反射共轭
$C_{\rm tail}$ 对称。S 在这个完整尾空间上单射且像稠密；
只使用已证的全空间性质，不假设任何未知限制上的密度。

设尾配对为
$$
B_{\rm tail}(f,g)=\langle f,C_{\rm tail}g\rangle.
$$
第 k 位和尾的原双线性配对准确是
$$
B_2((f_0,f_1),(g_0,g_1))
=B_{\rm tail}(f_0,g_1)+B_{\rm tail}(f_1,g_0).
\tag{1.3}
$$
指定 first-flip 在这一位为 $J=\operatorname{diag}(1,-1)$。

若 $k>0$，原 H 还含有限前头 $\mathbb C^{2^k}$。
$T_N$ 在该前头为恒等张量，原 first-flip 是一个可逆对角前头因子张量 J。
相应前头配对非退化，因此原 $B(M,U_\zeta M)\ne0$
与本稿尾矩阵核上的 $B_2(M_{\rm tail},J M_{\rm tail})\ne0$ 等价。
这里仅分离了真实不参与的有限头，没有换核、换 gauge 或换正常态。

## 2. 最大自然商与最小闭商的准确域

定义
$$
\boxed{
Q_{\max}=\frac1{2a}S^{-1}R,\qquad
\operatorname{Dom}Q_{\max}
=\{f:Rf\in\operatorname{Ran}S\}.
}
\tag{2.1}
$$
$S^{-1}$ 是作用在真实 $\operatorname{Ran}S$ 上的闭算子。
所以 (2.1) 是稠密定义的闭算子：
其域包含稠密的 $\operatorname{Ran}S$；
若 $f_n\to f$、$Q_{\max}f_n\to g$，则
$Rf_n\to Rf$，闭性给 $Rf=2aSg$。

另定义
$$
Q_0=\frac1{2a}R S^{-1},\qquad
\operatorname{Dom}Q_0=\operatorname{Ran}S.
$$
由于 R 与 S 交换，$Q_0\subset Q_{\max}$。
用原 C 转置记号
$$
Q^t=C_{\rm tail}Q^*C_{\rm tail}
$$
（只在环境尾空间使用，不把 C 下传到未知核），
有准确域身份
$$
\boxed{
Q_0^t=Q_{\max},\qquad
Q_{\min}:=\overline{Q_0},\qquad
Q_{\min}^t=Q_{\max},\quad Q_{\max}^t=Q_{\min}.
}
\tag{2.2}
$$
证明：$R$ 有界且 C 对称，$S^{-1}$ 的 C 转置是其自身，
故 $(R S^{-1})^t=S^{-1}R$，右侧自然域正是 (2.1)。
其域稠密，保证 $Q_0$ 可闭；再取两次转置得到 (2.2)。
特别
$$
Q_{\min}\subset Q_{\max}.
$$
这是最小闭域与最大自然域的实际区别，不能用形式交换相除删掉。

## 3. 真核恰为受限最大商的图

令真实有界下一尾算子
$$
F=R^2-4a^2tS^2
$$
并定义
$$
\boxed{
\mathscr D=\operatorname{Dom}Q_{\max}\cap\ker F.
}
\tag{3.1}
$$
给 $\mathscr D$ 以图范数
$$
\|f\|_Q^2=\|f\|^2+\|Q_{\max}f\|^2.
$$
它是闭的图 Hilbert 空间。
原矩阵核准确参数化为
$$
\boxed{
\mathcal U:\mathscr D\longrightarrow\ker T_N,\qquad
\mathcal U f=(-Q_{\max}f,f),
}
\tag{3.2}
$$
且 $\mathcal U$ 对图范数等距满射。

确切证明如下。若 $(f_0,f_1)\in\ker T_N$，
第二行给 $Rf_1=-2aSf_0$，故 $f_1\in\operatorname{Dom}Q_{\max}$，
$f_0=-Q_{\max}f_1$。将第一行乘 S 并使用全部交换关系，得
$Ff_1=0$。反过来，若 $f\in\mathscr D$，
第二行由定义为零；第一行乘 S 后为零，S 的环境单射性迫第一行本身为零。
这里只用了环境单射性，没有取消一个未知限制的稠密像。

还有一个由真实核额外给出的准确关系：
$$
\boxed{
Q_{\max}\mathscr D\subset\mathscr D,\qquad
Q_{\max}^2f=tf\quad(f\in\mathscr D).
}
\tag{3.3}
$$
确实 $R^2f=4a^2tS^2f$ 给
$R Q_{\max}f=2atSf\in\operatorname{Ran}S$，
所以 $Q_{\max}f$ 再属于最大商域，且二次作用为 tf。
F 与最大商在自然域上交换，故 $FQ_{\max}f=0$。
由 $\|t\|=\eta_k<1$，
$$
\|Q_{\max}f\|_Q^2=\|Q_{\max}f\|^2+\|tf\|^2\le\|f\|_Q^2.
\tag{3.4}
$$
因此 Q 在这个**实际图度量**中是收缩，尽管不能据此说它在环境尾范数中有界。
在 (3.2) 下，原 $N_k$ 的作用正是 $-Q_{\max}$。

## 4. 首位翻转配对恰为实际边界型

定义 $\operatorname{Dom}Q_{\max}$ 上的边界双线性型
$$
\boxed{
\mathfrak b(f,g)
=B_{\rm tail}(Q_{\max}f,g)
-B_{\rm tail}(f,Q_{\max}g).
}
\tag{4.1}
$$
它是交错的，且
$|\mathfrak b(f,g)|\le\|f\|_Q\|g\|_Q$。
由 (1.3)、(3.2)，准确有
$$
\boxed{
B_2(\mathcal U f,J\mathcal U g)=\mathfrak b(f,g)
\qquad(f,g\in\mathscr D).
}
\tag{4.2}
$$
所以
$$
\boxed{
B(M,U_\zeta M)\ne0
\quad\Longleftrightarrow\quad
\mathfrak b|_{\mathscr D\times\mathscr D}\not\equiv0.
}
\tag{4.3}
$$
这是所研究的**同一个指定** first-flip 条件，不是别的 dyadic 相位存在性。

由 (2.2)，环境最大域上 $\mathfrak b$ 的双侧根恰为
$\operatorname{Dom}Q_{\min}$。
例如若 $f\in\operatorname{Dom}Q_{\max}$ 且
$\mathfrak b(f,g)=0$ 对每个 $g\in\operatorname{Dom}Q_{\max}$ 成立，
转置域的定义给
$f\in\operatorname{Dom}Q_{\max}^t=\operatorname{Dom}Q_{\min}$。
故 $\mathfrak b$ 在实际边界商
$$
\operatorname{Dom}Q_{\max}/\operatorname{Dom}Q_{\min}
$$
上非退化。这里只指双线性根为零，没有假设一个有界正度量逆或统一条件数。
其在受限 $\mathscr D$ 的像上仍可能全等向，不能由环境非退化自动排除。

## 5. 原闭像缺陷和同一个正常见证的图表示

S 在 $\mathscr D$ 上保图域并与 Q 交换。
由 (3.2)，
$$
S\mathcal U f=\mathcal U(Sf).
$$
因此原实际旗的闭像准确为
$$
\boxed{
\overline{S\,\ker T_N}
=\mathcal U(\mathscr D_0),\qquad
\mathscr D_0:=\overline{S\mathscr D}^{\,\|\cdot\|_Q}.
}
\tag{5.1}
$$
闭包使用实际图范数；环境 $\operatorname{Ran}S$ 稠密没有代替这一步。

由于 $S\mathscr D\subset\operatorname{Ran}S=\operatorname{Dom}Q_0$，
(2.2) 给
$$
\mathfrak b(S\mathscr D,\mathscr D)=0.
$$
连续性使 $\mathfrak b$ 下降到实际图缺陷
$$
\mathscr D/\mathscr D_0.
\tag{5.2}
$$
原 $M\ominus\overline{SM}$ 中的向量与
$\mathscr D\ominus_Q\mathscr D_0$ 通过 (3.2) 等距对应。
因此原正向量态使用的是这个同一个图缺陷，未另换密度。

全部实际右交换子都被保留：
若 $V$ 属于真实尾完整交换子，则
$V\operatorname{Dom}Q_{\max}\subset\operatorname{Dom}Q_{\max}$ 且
$Q_{\max}V=VQ_{\max}$，其图算子范数不超过 $\|V\|$。
它同时保持 $\mathscr D$ 和 $\mathscr D_0$。
前一位的完整右算子 $a+N_kb$ 在图上准确作用为 $a-Q_{\max}b$；其范数由 (3.2) 的等距实现控制为 $\|a+N_kb\|$。加回前面不参与的有限头后，任意原完整 $A' $ 右算子直接通过原核 M 的限制作用到这个等距图上，同样正常且契约。这里没有将图范数换成未付的环境尾范数。因此整个原右测试族都保留，不只是多项式右因子。

原第二行还满足真正的核图身份
$$
\boxed{
Zf=S(2aQ_{\max}-S)f\qquad(f\in\mathscr D).
}
\tag{5.3}
$$
(3.3) 确保 $(2aQ_{\max}-S)f$ 仍在 $\mathscr D$。
故 $Z\mathscr D\subset S\mathscr D$。
这精确解释了从真核图闭像缺陷得到的同一正常态为何同时湮灭 S、Z 的全部右倍数：
第二行不是可以任意增添的另一独立正常态条件，也没有在域外形式除 S。

## 6. 现在必须处理的两个实际部分

(4.3) 把所需非零首flip配对完整定位。
图缺陷非零本身只给
$\mathscr D/\mathscr D_0\ne0$；
要由此推出 (4.3)，仍须用这里的实际 S、R、F 处理两部分：

1. 从图缺陷送入环境边界商的核为
   $$(\mathscr D\cap\operatorname{Dom}Q_{\min})/\mathscr D_0.$$
   它需要真正的核内图核心结论，不能用环境 $\operatorname{Ran}S$ 稠密代替。
2. 即使该核已清除，$\mathscr D$ 在环境边界商中的像仍须证明不是全等向。
   环境边界型非退化及图商的正常契约表示不单独证明这一点。

本稿没有构造这两个部分在当前真实算子中非零的反例，
也没有证明它们必消失。它给出的是同一个原核、完整来源和真实图度量下的等价接口。
特别原 $Q_{\max}^2=t$、全部右交换子作用和 (5.3) 已纳入；
这些额外真核方程仍未产生有限恒等式矛盾。

