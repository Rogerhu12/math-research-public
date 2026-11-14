# R150 附录：正锚加权误差下全部合法全柱中心的排序分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。状态：完整证明；kernel_resume_1cf 已全文独立核查必要性、排序尾预算、全部量词与应用。

[原中心谱稿 §§5—6](R150-appendix-linear-slope-center-ratios-and-equal-weight-bell-cyclicity.md)已从正锚的小尾比子列构造合法实际全柱，并计算其中心。本稿证明反向：任何合法位集都必须落回同一个排序小尾比及同一个排序平均。因此允许任意物理重排，也不能额外制造中心。新增是这个必要性和完整中心集合分类；所引用的循环性应用不重计为独立主定理。

## 1. 固定原行与精确结论

取
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
c\in\ell^2(\mathbb C),\quad |c_j|\le C_0a_j,
$$
以及
$$
\zeta=a+d^0+e^0,\qquad
\nu=c+\gamma a+d^1+e^1,
$$
其中 $d^\ell_j=0$ 于 $a_j=0$，
$$
K_\ell^2=\sum_{a_j>0}|d^\ell_j|^2/a_j<\infty,
\qquad e^\ell\in\ell^1(\mathbb C),\quad \ell=0,1.
$$
原常数 $u_*,v_*,\gamma$ 任意复，原 first 为
$u=u_*+\sum\zeta_j\chi_j$、$v=v_*+\sum\nu_j\chi_j$。

固定按物理位打破并列的下降重排
$r_j=a_{\iota(j)}>0$，令
$$
I_n=\{\iota(1),\ldots,\iota(n)\},\quad
S_n=\sum_{j\le n}r_j,\quad
G_n^2=\sum_{j>n}r_j^2,
$$
$$
\eta_n=\frac{\sqrt n\,G_n}{S_n},\qquad
b_n=\frac{\sum_{j\le n}c_{\iota(j)}}{S_n}.
\tag{1.1}
$$
特别 $|b_n|\le C_0$。

称递增穷尽的有限物理位集 $E_m$ 为本稿的合法全柱，若记
$$
n_m=|E_m|,\quad
\sigma_m=u_*+\sum_{E_m}\zeta_j,\quad
\tau_m=v_*+\sum_{E_m}\nu_j,\quad
g_m=\|\zeta_{E_m^c}\|_2+\|\nu_{E_m^c}\|_2,
$$
则
$$
\boxed{
|\sigma_m|\to\infty,\qquad
\frac{\sum_{E_m}(|\zeta_j|+|\nu_j|)}{|\sigma_m|}\le C,\qquad
\frac{\sqrt{n_m}\,g_m}{|\sigma_m|}\to0.
}
\tag{1.2}
$$
允许只取满足这些条件的递增子列。

**定理 1。** 每一条合法全柱都满足
$$
\boxed{
\eta_{n_m}\to0,\qquad
\frac{\sum_{E_m}a_j}{S_{n_m}}\to1,\qquad
\frac{\tau_m}{\sigma_m}-\gamma-b_{n_m}\to0.
}
\tag{1.3}
$$

**定理 2。** 至少存在一条合法全柱，当且仅当
$$
\boxed{\liminf_{n\to\infty}\eta_n=0.}
\tag{1.4}
$$
全部合法全柱可达到的中心比极限，恰为
$$
\boxed{
\mathcal K
=\gamma+
\left\{
b:\ \exists n_k\uparrow\infty,\
\eta_{n_k}\to0,\ b_{n_k}\to b
\right\}.
}
\tag{1.5}
$$
合法全柱的任何聚点也属于这个集合，反之每个集合元素都能由一条合法全柱实现为极限。

这里固定正锚 $a$、受控行 $c$ 和 $\gamma$ 后，集合 $\mathcal K$ 不依赖原 weighted 误差、可和误差或两个常数。没有声称改变这些误差后每一条具体位集序列仍合法。

## 2. 原主行在一个可和误差外控制正锚

令
$$
B=\{j:|d_j^0|>a_j/2\}.
$$
加权条件给
$$
\sum_Ba_j\le4K_0^2<\infty.
$$
在 $B^c$ 上，$|a_j+d_j^0|\ge a_j/2$。因此逐项有
$$
\boxed{
a_j\le2|\zeta_j|+h_j,\qquad
h_j=a_j\mathbf1_B(j)+2|e_j^0|,\qquad h\in\ell^1,\ h\ge0.
}
\tag{2.1}
$$
这将可能被主误差抵消的坐标全部保留为真实可和行，没有删除原尾中的异常位置。

对任意有限位集 $E$，置 $s=\sum_Ea_j$。加权 Cauchy–Schwarz 给
$$
\left|\sum_Ed_j^0\right|\le K_0\sqrt s,\qquad
\sum_E|\zeta_j|\le s+K_0\sqrt s+\|e^0\|_1.
\tag{2.2}
$$
沿合法序列，$|\sigma|\to\infty$ 迫 $s\to\infty$；否则 (2.2) 使 $\sigma$ 有界。于是
$$
\boxed{
\sigma=s+O(\sqrt s)+O(1),\qquad \sigma/s\to1,\qquad
\sum_E|\zeta_j|\le C_1s.
}
\tag{2.3}
$$
因此 (1.2) 特别给
$$
\frac{\sqrt n\,\|\zeta_{E^c}\|_2}{s}\to0,
\qquad n=|E|\to\infty.
\tag{2.4}
$$

## 3. 任意合法头与同位数最大头具有同一质量和中心

取 $I_n$ 为 (1.1) 中的最大 $n$ 个正锚位。记漏掉和额外选入的质量
$$
m_E=\sum_{I_n\setminus E}a_j,\qquad
r_E=\sum_{E\setminus I_n}a_j.
$$
两集合的位数相同，最大头的定义给 $r_E\le m_E$。由 (2.1)，
$$
m_E
\le2\sqrt n\,\|\zeta_{E^c}\|_2+\|h\|_1=o(s).
\tag{3.1}
$$
这里固定的可和总量除以 $s\to\infty$ 后消失；不需要预先假定异常位在 $E$ 中的具体速度。

所以
$$
0\le S_n-s=m_E-r_E=o(s),\qquad
m_E+r_E=o(s).
\tag{3.2}
$$
即 $S_n/s\to1$。由 $|c_j|\le C_0a_j$，
$$
\left|\sum_Ec_j-\sum_{I_n}c_j\right|
\le C_0(m_E+r_E)=o(s).
\tag{3.3}
$$
原第二行的 weighted 头仍为 $O(\sqrt s)$，可和头及原常数为 $O(1)$，故
$$
\tau=\gamma s+\sum_Ec_j+O(\sqrt s)+O(1).
$$
与 (2.3)、(3.2)、(3.3) 合并，得到
$$
\boxed{\tau/\sigma=\gamma+b_n+o(1).}
\tag{3.4}
$$
至此中心必要性已经证明；下一节另行支付排序尾比，不能把头质量相同直接当作尾平方和结论。

## 4. 删除最小主系数并补最大异常位：反推完整排序尾比

仍记 $n=|E|$、$s=\sum_Ea_j$，取
$$
k=\lceil n/s\rceil.
$$
充分大时 $s>2$，且
$$
k/n\le1/s+1/n\to0.
$$
又 $s\le\sqrt n\,\|a\|_2$，所以 $k\ge n/s\to\infty$。因而最终 $1\le k<n/2$。

从 $E$ 中删去 $k$ 个 $|\zeta_j|$ 最小的位，记该集为 $R$。由 (2.3)，每个被删幅度最多为
$$
\frac{\sum_E|\zeta_j|}{n-k+1}
\le\frac{2C_1s}{n}.
$$
所以
$$
\boxed{\|\zeta_R\|_2\le\frac{2C_1s\sqrt k}{n}.}
\tag{4.1}
$$

令 $J_k$ 为 $h$ 的至多 $k$ 个最大非零幅度位；若支撑有限，超过支撑后取全部。非负可和行的最佳 $k$ 项尾满足
$$
\boxed{\|h_{J_k^c}\|_2\le\|h\|_1/\sqrt k.}
\tag{4.2}
$$
例如下降重排 $h_j^*$ 有
$(h_{k+1}^*)\sum_{j>k}h_j^*\le\|h\|_1^2/k$，便得该式。

构造辅助集合
$$
E'=(E\setminus R)\cup J_k,\qquad |E'|\le n.
$$
这是证明中用于比较最佳截断的有限集合，不要求把它本身作为新的合法穷尽序列。

最大 $n$ 项截断使正锚的 $\ell^2$ 尾最小，故由 (2.1) 得
$$
\begin{aligned}
G_n
&\le\|a_{(E')^c}\|_2\\
&\le2\|\zeta_{E^c}\|_2+2\|\zeta_R\|_2+\|h_{J_k^c}\|_2.
\end{aligned}
$$
因此
$$
\boxed{
\frac{\sqrt n\,G_n}{s}
\le
2\frac{\sqrt n\,\|\zeta_{E^c}\|_2}{s}
+4C_1\sqrt{\frac{k}{n}}
+\frac{\|h\|_1}{s}\sqrt{\frac nk}
\longrightarrow0.
}
\tag{4.3}
$$
第一项由 (2.4)，第二项由 $k/n\to0$；第三项因 $k\ge n/s$ 至多为
$\|h\|_1/\sqrt s\to0$。
结合 $S_n/s\to1$，得到 $\eta_n\to0$，定理1证毕。

这个辅助删除步骤很关键：仅由 $\ell^1$ 异常行的总量有限，并不能直接断言任意原位集都已有 $\sqrt n$ 加权的尾 $\ell^2$ 小量。

## 5. 反向构造及全部中心集合

若有 $n_k\uparrow\infty$ 满足 $\eta_{n_k}\to0$，取前中心谱稿已经支付的
$$
E_k=I_{n_k}\ \cup\
\{\text{最大 }n_k\text{ 个 }|e^0|\text{ 位}\}\ \cup\
\{\text{最大 }n_k\text{ 个 }|e^1|\text{ 位}\}\ \cup\
\{\text{前 }n_k\text{ 个物理位}\}.
\tag{5.1}
$$
全部排序使用固定并列规则，故这些位集递增穷尽，且 $|E_k|\le4n_k$。

为明确没有遗漏原误差，新增位的正锚质量至多
$\sqrt{3n_k}\,G_{n_k}=o(S_{n_k})$；原 weighted 两尾由
$$
n_k\|d^\ell_{E_k^c}\|_2^2/S_{n_k}^2
\le K_\ell^2/S_{n_k}\to0
$$
控制；每个可和行的排序尾满足
$n\sum_{j>n}(|e|_j^*)^2\to0$。
原 $a,c$ 尾则由 $\eta_{n_k}\to0$ 及 $|c|\le C_0a$ 控制。
所以 (5.1) 满足全部 (1.2)，且
$$
\tau_k/\sigma_k=\gamma+b_{n_k}+o(1).
\tag{5.2}
$$

若存在任意合法全柱，定理1以其位数 $n_m$ 给 (1.4)；反之上面的构造已经证明。若某个合法中心有极限，定理1给它属于 (1.5)；反之 (5.1)—(5.2) 实现 (1.5) 中每个点。对任意聚点先取子列即可。定理2证毕。

集合 (1.5) 也可写成有界闭集的交：
$$
\mathcal K-\gamma
=
\bigcap_{N\ge1}
\overline{\{b_n:n\ge N,\ \eta_n\le1/N\}}.
\tag{5.3}
$$
因此它是紧集，允许为空。公式 (5.3) 的反向由逐次选取
$n_N\ge N$、$\eta_{n_N}\le1/N$ 且 $b_{n_N}$ 逼近指定点，再抽严格递增子列得到。

若同一固定原 $\zeta,\nu,u_*,v_*$ 有两种允许的正骨架、weighted 与可和误差分解，则两种由 (1.5) 算出的集合完全相同：它们都等于左侧原实际合法全柱的中心极限全集。此处只改变同一原行的分解，不能与换成另一个实际主行或增加第二尺度混同。


## 6. 对原任意多项式判据的准确含义

原 $Z=X_u$ 在本系数类中空谱，完整有界可和扰动的预解公式已由前中心谱稿 §5.1 支付。因此[任意原二元多项式全柱定理](R150-appendix-cyclic-block-roots-arbitrary-bivariate-polynomials-and-unique-linear-center.md)适用于上述合法全柱。

- 若 $\mathcal K$ 至少含两个点，则每个非恒定标量 $F$ 的全部
  $[F(u,v)-\lambda]^r e^w$ 循环。可以交替选取两条排序好子列的更大指标，再用 (5.1) 构造一条中心比不收敛的合法穷尽列；无需把两条不可比较的原位集直接交织。
- 若 $\mathcal K=\{\beta\}$，则每条合法全柱的中心比都趋于 $\beta$。此时 $F_{\deg F}(1,\beta)\ne0$ 仍足以给全部循环性；最高符号在该点为零时，此单尺度方法保留候选。
- 若 $\mathcal K=\varnothing$，则本类原两行根本没有满足 (1.2) 的位集序列；不能单凭改物理排序声称恢复同一个全柱预算。

这只分类本稿明确的单尺度柱条件。重新去中心后为余行另付一个不同尺度、改变主锚、或使用幂好时间的证明均是其他接口，未被最后一项排除。原普通复 Hilbert ISP 仍未完成。
