# 一阶模数、真实向量扩张与临界 GM 投影

日期：2026-11-12。状态：本文的模数识别、实际加法截面、Frobenius
与 Hodge 格的区别、第一垂直 $p$ 阶 defect 及指定 GM 投影均已证明。
没有由此得到无穷多个 $p$ 的非零性。

## 1. 固定的一阶模数真正保留了哪一个坐标

沿用[实际除法单位模型](2026-11-12-weight-one-division-unit-relative-model.md)：
$E_\lambda:y^2=x(x-1)(x-\lambda)$，$\omega=dx/(2y)$，
$t=\lambda-1/2$，$Z=-x/y$ 是零截面的纤维参数。
在同一个固定满 $68$ 层覆盖上，全部
$r_P$ 都是去掉非零 $68$ 挠点后的整单位，并且
$$
r_P(t,0)=1,\qquad
c_P(t):=\partial_Z\log r_P(t,0)=-68^2U_P(t).
\tag{1}
$$
坏位仍只有 $\{2,3,5,17\}$。

令 $\mathcal J_2=\operatorname{Pic}^0(E_\lambda,2O)$，即带 $2O$
刚性化的 Picard 群。忘掉刚性化给出
$$
0\longrightarrow
\mathcal O_{2O}^{\times}/\mathcal O^\times
\longrightarrow\mathcal J_2
\longrightarrow\operatorname{Pic}^0(E_\lambda)
\longrightarrow0.
\tag{2}
$$
在所选参数中，其核由 $1+cZ\bmod Z^2$ 描述，乘法对应 $c$ 相加。
不选参数时，它是加法线丛 $I_O/I_O^2\simeq\omega|_O$ 的向量群。

固定以下符号约定：$\mathcal O(D)$ 的典范有理截面是 $1$，
沿 $2O$ 取这个截面的刚性化。若 $D=\operatorname{div}r$ 且
$r(O)=1$，乘以 $r$ 将 $\mathcal O(D)$ 平凡化，刚性化变成
$r|_{2O}$。所以
$$
[\operatorname{div}r_P]_{\mathcal J_2}
\quad\hbox{在 (2) 的核中准确对应}\quad c_P.
\tag{3}
$$
这是主除子在普通 Jacobian 中为零后，仍然保留的真实一阶信息。

### 普遍向量扩张的识别

Coleman，*Vectorial extensions of Jacobians*，1990，
Prop. 1.2（p. 771）给出：若 $D-|D|$ 是非特殊的 $g$ 次除子，
且局部重数小于特征，则广义向量 Jacobian 是普遍向量扩张。
这里 $g=1$，$D=2O$，$D-|D|=O$，
$H^0(E,\omega(-O))=0$，假设全部满足。

需要整个家族时，用同文 Thm. 3.1（p. 778）：评价映射
$\pi_*\omega\to\omega|_O$ 是同构，故得到家族中的同构
$$
\boxed{\mathcal J_2\simeq
 \operatorname{Pic}^{\natural,0}(E_\lambda).}
\tag{4}
$$
右边表示相对次数零线丛及相对连接。我们在这里用 **Picard
的逆变约定**，而不是不说明对偶后就把矩阵转置。

若 $\omega=dz$，$z=Z+O(Z^2)$，平凡线丛上的连接 $d-c\omega$
有一阶水平截面 $1+cZ$。因此 (4) 把 (3) 对应到
$$
(\mathcal O_E,d-c_P\omega).
\tag{5}
$$
这个负号也可直接由 Coleman's Theorem 1.1 的
$E-\operatorname{div}f$ 约定核对。

## 2. 本题实际权一因子是加法核中的一个明确截面

记两固定单位为 $R_S=\prod_{\mathcal S}r_P$ 与
$R_R=\prod_{\mathcal S_{\rm rot}}r_P$，并置
$c_S=\partial_Z\log R_S|_O$、$c_R=\partial_Z\log R_R|_O$。
[真实 Kummer 配对](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)
已经固定
$$
\begin{aligned}
h_e&=-\frac{c_e}{2N^2}(\log R_S-i\log R_R),&
M_e&=-\frac{c_e}{2N^2}(c_S-i c_R),\\
h_o&=-\frac{c_o}{2N^2}(\log R_S+i\log R_R),&
M_o&=-\frac{c_o}{2N^2}(c_S+i c_R),
\end{aligned}
\tag{6}
$$
其中 $N=68$，
$$
c_e=\frac{\sqrt2\,17^{17/4}}{4800f},\qquad
c_o=\frac{i\sqrt2\,17^{7/4}}{32f},\qquad f=34(1+i).
$$
$M_e=M_1=t^4+\frac72t^6+\cdots$，$M_o=t+\frac12t^3+\cdots$，
两者都是有理代数 germ，且在所有上述好位整。

由于 (3) 已落在加法核中，允许在那里作 (6) 的线性组合。
故 $M_e$ 是固定二维群 $\mathcal J_2$ 中的实际截面，
而其 Picard-连接解释准确为
$$
(\mathcal O_E,d-M_e(t)\omega).
\tag{7}
$$
这不是把含 $i$ 的系数直接当成原单位的整数幂。
在更高模数中若要作同样的线性组合，本文只对 **对数 cochain**
作线性组合，不宣称 $R_S^aR_R^b$ 在任意代数整系数 $a,b$ 下
仍是整单位。

普通相对 de Rham 上同调并不提供额外的一阶坐标。
特征零下 $\operatorname{Spec}k[Z]/Z^2$ 的 de Rham 复形与一点
准同构：$dZ$ 正是 $d(Z)$。因而把 $O$ 换成这个非约化点，
却仍使用普通相对 de Rham，不会保留 (3)。这里起作用的是
刚性化/模数。

## 3. Frobenius 拉回的模数是 $2pO$

在特征 $p$ 的特殊纤维上，令
$F:E\to E^{(p)}$ 为相对 Frobenius。在兼容参数中
$F^*Z'=Z^p$，所以
$$
F^{-1}(2O')=2pO.
$$
线丛及刚性化的真正拉回依次为
$$
\operatorname{Pic}^0(E^{(p)},2O')
 \longrightarrow \operatorname{Pic}^0(E,2pO)
 \longrightarrow \operatorname{Pic}^0(E,2O).
\tag{8}
$$
最后一步是限制刚性化。对加法核，
$$
1+cZ'\longmapsto1+cZ^p\bmod Z^{2p}
                    \longmapsto1\bmod Z^2.
\tag{9}
$$
所以它在 $2O$ 的加法核上为零，却并非在较高模数中已经消失。

较高模数的主单位群
$$
(1+Zk[Z])/(1+Z^{2p}k[Z])
$$
不是一个向量群：$(1+Z)^p=1+Z^p\ne1$，而特征 $p$ 的任意
加法向量群都被 $p$ 杀掉。特征零中的对数也不能免费给出整同构，
因为 $[Z^p]\log(1+Z)=1/p$。这准确解释了为什么不能把
Coleman 的一阶模数同构原样应用于 $2pO$，再忽略一次除 $p$。

若在特征零正式邻域选择
$\phi Z=Z^p+p a_1(t)Z+pO(Z^2)$，它对一阶刚性化的作用才是
乘以 $p a_1(t)$。除以 $p$ 后留下的 $a_1$ 依赖 lift。
前述 Kummer 稿 (14)–(20) 已经给出它与实际 GM 配对的精确补偿，
这里没有再把 $a_1$ 当成一个自动规范的标量。

## 4. 群同态与 crystalline Frobenius 的 Hodge 约定

为消除对偶歧义，直接对 Picard-连接函子取一阶变形。
线丛的过渡函数 $1+\epsilon f_{\alpha\beta}$ 与连接形式
$\epsilon\omega_\alpha$ 满足
$\omega_\beta-\omega_\alpha=df_{\alpha\beta}$。
因此
$$
\operatorname{Lie}\operatorname{Pic}^{\natural,0}(E)
 =\mathbb H^1(E,\mathcal O_E\to\Omega_E^1)
 =H^1_{\rm dR}(E),
\tag{10}
$$
而加法核的 Lie 线正是 $\operatorname{Fil}^1=H^0(E,\Omega^1)$。
曲线映射的拉回在 (10) 上就是通常的逆变 de Rham 拉回。

任意特征零代数群同态
$\mathcal J_2(E')\to\mathcal J_2(E)$ 都把加法核送入加法核：
把这个限制再映到椭圆商，得到的 $\mathbb G_a\to E$ 同态为零。
故其微分必须保持 (10) 的 Hodge 线。

但本题实际 crystalline Frobenius 的行约定是
$$
\Phi(\omega^\sigma,\eta^\sigma)^t
 =F(\omega,\eta)^t,\qquad\eta=\nabla_t\omega.
$$
[整 GM Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)
在惰性 CM 点给出
$$
F(0)=\begin{pmatrix}0&pa\\ b&0\end{pmatrix},
\qquad a,b\in\mathbb Z_p^\times,\quad ab=-1.
\tag{11}
$$
于是 $\Phi(\omega^\sigma)=pa\eta$，在特征零中不在
$\operatorname{Fil}^1$。所以 (11) **不是**某个特征零
$\mathcal J_2$ 群同态的微分。它模 $p$ 杀掉 Hodge 线，与 (9)
完全相容；不能从这个模 $p$ 相容性反推一个保持加法核的整 lift。

同时，若 $H=\mathcal O\omega\oplus\mathcal O\eta$，则
$$
\Phi(H^\sigma)=\mathcal O\omega\oplus p\mathcal O\eta,\qquad
\operatorname{length}_{\mathcal O}(H/\Phi(H^\sigma))=1.
\tag{12}
$$
要把 Hodge 源向量的像除以 $p$，实际使用的是扩大的源格
$H'=\mathcal O(\omega/p)\oplus\mathcal O\eta$，
$H'/H$ 长度一。它不是原格的整基变换。
这里的行列式理想为 $(p)$，是一层 $p$；若剩余域为 $k$，
有限群的集合指数是 $\#k$。真正截面/jet 格中的代价须保留其诱导格，
不由 (12) 猜测所有评价映射的范数。

## 5. $2pO$ 的第一余项可以写成实际固定单位的一个系数

令 $\mathcal O$ 是容纳固定层系数的未分歧整环，$\sigma$ 为其
Frobenius。写
$$
z(t,Z)=\int_0^Z\omega,\qquad
b_p(t)=p[Z^p]z=[Z^{p-1}]\frac{\omega}{dZ}.
\tag{13}
$$
$b_p$ 是整函数。对归一整单位 $r=1+cZ+\cdots$，
$$
\Lambda_{r,p}:=p[Z^p]\log r\in\mathcal O[[t]],\qquad
\Lambda_{r,p}\equiv c(t)^p\pmod p.
\tag{14}
$$
证明只需展开 $\log r$ 到 $Z^p$：只有第 $p$ 个幂的分母含 $p$，
其贡献为 $c^p/p$。

令 $\mathcal H_p(t)$ 为纤维不变向量场的 Hasse 系数，
$\delta^p=\mathcal H_p\delta$ 模 $p$。则
$$
b_p\equiv\mathcal H_p\pmod p.
\tag{15}
$$
一个不依赖符号猜测的证明是把 $z$ 截到次数 $p-1$。
这些系数都整，且 $\delta z=1$。在 $O$ 对截断式应用 $\delta^p$，
漏掉的唯一可能贡献是
$(b_p/p)\delta^p(Z^p)|_O=b_p(p-1)!$。
模 $p$ 用 Wilson 定理，得到 $\mathcal H_p-b_p=0$。

因此，单位的高模数刚性化与其由一阶连接给出的水平刚性化之间，
第一个可能不整的对数系数满足
$$
\boxed{\quad
p[Z^p](\log r-cz)\equiv c^p-\mathcal H_p c\pmod p.
\quad}
\tag{16}
$$
右边也正是连接 $d-c\omega$ 的 $p$-curvature 的相反数：
$(\delta-c)^p-\nabla_{\delta^p}=\mathcal H_pc-c^p$。
这给出了较高模数余项的实际几何含义。

对 (6) 取相同线性组合，定义
$$
\Lambda_{e,p}=p[Z^p]h_e,\qquad
W_{e,p}=p[Z^p](h_e-M_ez)
       =\Lambda_{e,p}-b_pM_e.
\tag{17}
$$
两者完整地在 $\mathcal O[[t]]$ 中。由 $\sigma(i)=-i$ 或 $i$，
以及 $M_e,M_o$ 的有理系数，得到准确的两型同余
$$
\boxed{
\begin{array}{ll}
p\equiv3\pmod4:&
W_{e,p}\equiv
 \eta_pM_o(t^p)-\mathcal H_p(t)M_e(t)\pmod p,
 \quad\eta_p=c_e/c_o^\sigma,\\[1mm]
p\equiv1\pmod4:&
W_{e,p}\equiv
 \eta_pM_e(t^p)-\mathcal H_p(t)M_e(t)\pmod p,
 \quad\eta_p=c_e/c_e^\sigma.
\end{array}}
\tag{18}
$$
例如惰性时
$(-c_e/(2N^2))(c_S^p-i c_R^p)
 =\eta_p M_o(t)^p\bmod p$。
这样系数 Frobenius 的半线交换仍然保留在高模数 defect 中。

## 6. 惰性处真实 GM 投影究竟消掉多少

以下限定 $p\equiv3\pmod4$、$p\ge7$。
取实际整 GM 的 $U,V$，令
$$
s=1-4t^2,\quad J^F=V/t,\quad
F_i=\frac{U^{p+1}}{s(J^F)^{p+2}},\qquad
\mathcal P_p(F)=[t^{p+1}]\frac{F(t)F_i(t)}{V(t)}.
\tag{19}
$$
$\mathcal P_p$ 允许 $F/V$ 有简单的 Laurent 极点；
它对整 $F$ 的值仍然整。
实际中央系数为 $C_{p+1}=[t^{p+1}]M_eF_i\in p\mathbb Z_p$。

令 $n=(p-1)/2$，并取二进分母的整 Hasse lift
$$
H_p(t)=P_n(2t),\qquad h_p=H_p'(0)\in\mathbb Z_p^\times.
\tag{20}
$$
标准系数公式也直接证明 $H_p\bmod p=\mathcal H_p$：
$[x^{p-1}](x(x-1)(x-\lambda))^n
 =(-1)^n\sum_j\binom nj^2\lambda^j$，
后者在 $\lambda=1/2+t$ 等于 $P_n(2t)$ 模 $p$。
$n$ 为奇数，$P_n$ 的线性项的阶乘均小于 $p$，
所以 $h_p$ 是单位。

Legendre 方程给
$$
sH_p''-8tH_p'-H_p=-p^2H_p.
$$
在所有次数 $\le p-2$，奇系数递推的分母不含 $p$，故
$H_p\equiv h_pL\bmod p^2$ 到这些次数。
而 $V-L$ 从 $t^p$ 开始。因此
$$
\mathcal P_p(H_pM_e)\equiv h_pC_{p+1}\pmod{p^2},
\tag{21}
$$
因为 $M_e$ 从 $t^4$ 开始，所需 $H_p-h_pV$ 的最高次数正是
$p-2$。这里没有越过一次递推分母 $p$。

另一项可以完整精度计算。$M_o(t^p)=t^p+O(t^{3p})$，
而 $U=1+t^2/2+\cdots$、$J^F=1+3t^2/2+\cdots$，所以
$$
\begin{aligned}
\mathcal P_p(M_o(t^p))
 &= [t^2]\frac{U^{p+1}}{s(J^F)^{p+3}}\\
 &=\frac{p+1}{2}+4-\frac{3(p+3)}2\\
 &=\boxed{-p}.
\end{aligned}
\tag{22}
$$
故第一 Frobenius 项在临界投影中模 $p$ 确实消掉，
但除 $p$ 后留下的是已知单位 $-1$，不能把它当成完全为零。

为把剩余项也保留，令
$$
E_{e,p}=
 \frac{\Lambda_{e,p}-(b_p-H_p)M_e-\eta_pM_o(t^p)}p
 \in\mathcal O[[t]].
\tag{23}
$$
整性由 (14)、(15)、(18) 得到。这个定义相当于设置新坐标
$Z_{\rm new}=Z+((b_p-H_p)/p)Z^p$，把旧级数通过逆换元改写为
$Z_{\rm new}$ 的级数，再取归一化的第 $p$ 个对数系数。
因此它变为 $\Lambda_{e,p}-(b_p-H_p)M_e$，不是直接正向代入
新表达式所产生的相反号；这没有假定额外的 Frobenius 恒等式。
由定义，特征零中准确有
$$
W_{e,p}+H_pM_e=\eta_pM_o(t^p)+pE_{e,p}.
\tag{24}
$$
应用 (19)，再用 (21)、(22)，得到
$$
\mathcal P_p(W_{e,p})+h_pC_{p+1}
 \equiv-\eta_pp+p\mathcal P_p(E_{e,p})\pmod{p^2}.
\tag{25}
$$
特别 $\mathcal P_p(W_{e,p})\in p\mathcal O$，且
$$
\boxed{\quad
h_p\,\frac{C_{p+1}}p\equiv
-\eta_p-\frac{\mathcal P_p(W_{e,p})}p
 +\mathcal P_p(E_{e,p})\pmod p.
\quad}
\tag{26}
$$

这是同一实际单位、同一刚性化和同一 GM 临界行的比较。
它证明第一 Hasse/Frobenius 项的投影有准确的 $-p$ 因子；
同时把仍需控制的高模数项全部显式保留。
目前没有证明 (26) 的最后两项消失，或不能恰好抵消 $-\eta_p$。
它们仍取增长到 $p$ 的纤维 jet 与增长到 $p+1$ 的基底 jet。
因此 (4) 的二维几何接收器与 (26) 的高模数计算都是实际正面
接口，但尚未把所需非零性降成固定维 Frobenius 的已知非零条目。

## 来源与范围

- Robert F. Coleman，*Vectorial extensions of Jacobians*，
  Ann. Inst. Fourier **40** (1990), 769–783：
  Prop. 1.2 / Theorem 1.1，p. 771；相对 Picard-连接函子，
  pp. 772–773；Theorem 3.1，p. 778。
  [原文](https://www.numdam.org/article/AIF_1990__40_4_769_0.pdf)。
  已读原文并逐项核对本题假设。
- 实际单位与完整好整模型：
  [除法单位 relative 模型](2026-11-12-weight-one-division-unit-relative-model.md)。
- 两条半线、常数、局部 lift 及原 GM 补偿：
  [Kummer 垂直 jet](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)。
- 实际 $U,V$、行基约定及临界系数替换：
  [整 GM Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)。
- 本文 (13)–(26) 是直接的有限系数与不变向量场计算，
  不把一般 $p$-curvature 猜想、regulator 非退化或待证的
  跨 $p$ 传播作为输入。
