# O6 工作记录：原全局单位的中心整除与一辅助素数导数的实际下降

**状态：以下比较和构造已证明；尚未得到新的跨素数非零性。** 日期：2026-11-13。

本记录继续 R30–R36 的同一曲线、同一 $\pi$ 塔、同一直接字符和原椭圆单位。它不以新局部证书替代课题主目标，也不把单个行列式为零当作整个单位格上的原始行关系。

引用的算术输入限于仓库已核查的已出版 Bley、BKS 定理。Ohshita II 的 arXiv:1710.04568 页面本次只查到 v1、未列期刊出处；它的 §7.4 提供了寻找下述比较的线索，本记录不调用其 Theorem 7.19，而把需要的一辅助素数特例直接由 BKS 的 MRS 公式证明。

## 1. 固定原对象

取 R36 的素数范围，固定 $n\ge1$，写
$$
R=R_n=\mathbb Z_p[\Gamma_n],\qquad
\theta=T-p,\qquad
S=R/\theta R=\mathbb Z_p/p^n,
$$
$$
\omega_n(T)=(1+T)^{p^{n-1}}-1.
$$
使用 $\mathcal T=\{(67)\}$。取 R35 的辅助素位 $w\mid\mathfrak q$，满足
$$
\lambda_{p,n}(c_w)\in S^\times.
$$
所有单位群均已作 $\widetilde\chi$ 分量和 $p$-完备化，以下以加法模记号书写其群运算。记原全局单位格为 $U_0$，增加 $\mathfrak q$ 后的单位格为 $W=U_{\mathfrak q}$。R35 给
$$
0\longrightarrow U_0\longrightarrow W
 \xrightarrow{v_w}R\xrightarrow{x\mapsto xc_w}A_n.
\tag{1}
$$
令
$$
I=\operatorname{Ann}_R(c_w)=v_w(W).
$$
由 $\lambda_{p,n}(c_w)$ 为单位，$I\subset\theta R$。R36 的两条整泛函为
$$
f=p^{b_p}\mathcal L_n/\theta,\qquad
g=v_w/\theta,\qquad f,g\in W^*:=\operatorname{Hom}_R(W,R).
\tag{2}
$$
原椭圆单位记作 $z_n$，其局部 Coleman 系数仍为
$$
F_{p,n}=\theta^2G_{p,n}.
$$
选择 $h,z_w$ 如 R35，故 $v_w(z_w)=h$，$v_p(h)\ge n$。固定位置顺序 $[\infty,\mathfrak q]$ 后，
$$
\epsilon=\epsilon_{2,n,w}
 =\frac{u_n}{h}z_n\wedge z_w
 \in\bigcap_R^2W,\qquad u_n\in R^\times.
\tag{3}
$$
这里 $\bigcap_R^2W=\operatorname{Hom}_R(\bigwedge_R^2W^*,R)$ 是完整 Rubin 双对偶格。R35 的完整值理想等式为
$$
\left\langle(\phi\wedge\psi)(\epsilon):
 \phi,\psi\in W^*\right\rangle_R
 =\operatorname{Fitt}_{R,0}(A_n/Rc_w).
\tag{4}
$$
不能把 (4) 换成只由 $f,g$ 的一个值生成的理想。

## 2. 对称群环给出的实际同态提升

本节也适用于 $U_0$。这些格都是有限自由 $\mathbb Z_p$-模。令 $\operatorname{tr}:R\to\mathbb Z_p$ 取群环单位元的系数。则
$$
\operatorname{Hom}_R(W,R)
 \xrightarrow{\ \phi\mapsto\operatorname{tr}\phi\ }
 \operatorname{Hom}_{\mathbb Z_p}(W,\mathbb Z_p)
\tag{5}
$$
是同构，其逆为
$$
\ell\longmapsto
 \left(w\longmapsto\sum_{\gamma\in\Gamma_n}
       \ell(\gamma^{-1}w)\gamma\right).
\tag{6}
$$
直接换指标证明 (6) 为 $R$-线性；取单位元系数及利用 $R$-线性可验证两个复合都是恒等映射。

因此，对于每个 $N\ge1$，每个
$$
\bar\phi:W\longrightarrow R/p^NR
$$
都能提升为 $\phi\in W^*$：先提升其单位元系数对应的 $\mathbb Z_p$-线性泛函，再用 (6)。提升不典范，两种提升相差 $p^N\psi$，其中 $\psi\in W^*$。这一步使用的是整格的 $\mathbb Z_p$ 自由性，不能仅从有限环的自内射性推出整提升。

同一个对称群环同构还给
$$
W\xrightarrow{\sim}W^{**}.
\tag{7}
$$
这是自然的评价映射；在 (5) 下它成为有限自由 $\mathbb Z_p$-模的双对偶映射。因此对任意 $\phi\in W^*$，收缩
$$
i_\phi\epsilon\in\bigcap_R^1W=W
\tag{8}
$$
确实是原整 $S$-单位格中的元素。

中心约化的同态也可提升。对称性给
$$
\operatorname{Ext}^1_R(W,R)
 =\operatorname{Ext}^1_{\mathbb Z_p}(W,\mathbb Z_p)=0.
$$
例如以一个 $R$-自由分解计算两边，(5) 是整个 Hom 复形的同构；该分解也是 $\mathbb Z_p$-自由分解。将 $\operatorname{Hom}_R(W,-)$ 作用于
$0\to R\xrightarrow{\theta}R\to S\to0$，得到
$$
W^*/\theta W^*\xrightarrow{\sim}
 \operatorname{Hom}_S(W/\theta W,S).
\tag{9}
$$
这没有声称 $W/\theta W$ 为自由 $S$-模。其可能的非自由性必须保留。

## 3. 原椭圆单位的一次全局中心除法

在 (8) 取 $\phi=g$。按 BKS 的收缩约定，
$$
i_g(z_n\wedge z_w)=g(z_n)z_w-g(z_w)z_n.
$$
由于 $g(z_n)=0$、$g(z_w)=h/\theta$，在
$\mathbb Q_p\otimes R$ 中计算得
$$
i_g\epsilon=-u_n\,\frac{z_n}{\theta}.
\tag{10}
$$
左端已由 (8) 证明属于 $W$，而 $u_n$ 是单位，故 $z_n/\theta\in W$。其 $v_w$ 为零，由 (1) 得到更准确的结论
$$
\boxed{\quad z_n/\theta\in U_0.\quad}
\tag{11}
$$
这里的除法在 $\mathbb Q_p\otimes R$ 中唯一，且最终回到整格；没有在 $S$ 中除零。

对每个 $n$ 都可选满足 R35 条件的辅助素数。所得 (11) 与这些选择无关，因为 $\theta$ 在 $\mathbb Q_p\otimes U_0$ 中可逆。范数与 $\theta$ 相容，而原 $z_n$ 范数相容；故这些商也范数相容，给出
$$
z_\infty/\theta\in E_\infty^{\widetilde\chi}.
\tag{12}
$$
这是原全局单位塔中的整除。它不是把局部商自由地宣称为全局单位。

其实际局部坐标及 R36 观测为
$$
\mathcal L_n(z_n/\theta)=\theta G_{p,n},
\qquad
f(z_n/\theta)=p^{b_p}G_{p,n},
\qquad g(z_n/\theta)=0.
\tag{13}
$$
因此该实际元素给出的非零门仍是 R36 已有的 $p^{b_p}G_p(p)\ne0$，本身没有降低这一门。

### 3.1 完整 Fitting 整除可继续作用于同一元素

如果对于某个 $d\ge0$，
$$
\operatorname{Fitt}_{R,0}(A_n/Rc_w)\subset\theta^dR,
\tag{14}
$$
则 (4) 和 Rubin 格的定义直接给
$$
\epsilon/\theta^d\in\bigcap_R^2W.
$$
再收缩 $g$，与 (10) 完全相同的演算给
$$
\boxed{\quad z_n/\theta^{d+1}\in U_0.\quad}
\tag{15}
$$
条件 (14) 要求所有整泛函外积的值整除，不能由
$(f\wedge g)(\epsilon)$ 的整除代替。

特别地，令 $q_p=\operatorname{rank}_{\mathbb Z_p}D_p$。对给定 $c_w$，取其在 $\mathcal A_p$ 中的提升 $c$。因 $\lambda_{p,n}(c_w)$ 是单位，$\lambda_p(c)$ 也是单位。置
$$
Q=\mathcal A_p/\Lambda c.
$$
则
$$
(Q/\theta Q)\otimes\mathbb Q_p
 \simeq N_p\otimes\mathbb Q_p,
\qquad
\dim_{\mathbb Q_p}(Q/\theta Q)\otimes\mathbb Q_p=q_p-1.
$$
在 DVR $\Lambda_{(\theta)}$ 上，$Q$ 的每个非零初等因子至少含一次 $\theta$；所以其零阶 Fitting 理想包含于 $\theta^{q_p-1}$。由于 $\theta$ 是 $\Lambda$ 的素元，这个包含对全体 Fitting 生成元已在 $\Lambda$ 中成立。基变换到 $R$ 给 (14)，其中 $d=q_p-1$。于是
$$
z_n/\theta^{q_p}\in U_0,\qquad
z_\infty/\theta^{q_p}\in E_\infty^{\widetilde\chi}.
\tag{16}
$$
这也可直接由 R32 的秩一完整 Fitting 表达式得到：它表达原椭圆单位在完整全局单位格中的整除。式 (16) 没有给 $q_p$ 的上界。所得商依赖 $p$ 及原塔，不能当成一个与 $p$ 无关的固定代数函数，再免费套用固定源的高度或 Padé 估计。

## 4. 辅助主化元素的确切中心值

令
$$
A_n(T)=\frac{\omega_n(T)-\omega_n(p)}{T-p}\in\mathbb Z_p[T].
$$
在 $R$ 中有 $\theta A_n=-\omega_n(p)$。由于 $v_p(h)\ge n=v_p(\omega_n(p))$，
$$
\frac h\theta=-\frac{h}{\omega_n(p)}A_n(T)\in R.
$$
故
$$
\boxed{\quad
e_n\!\left(g(z_w)\right)
=e_n(h/\theta)
=-\frac{h\,\omega_n'(p)}{\omega_n(p)}
 \pmod{p^n}.
\quad}
\tag{17}
$$
右端在约化前的赋值恰为
$$
v_p(h)-1,
$$
因为 $v_p(\omega_n'(p))=n-1$。所以已知主化元素只在 $v_p(h)=n$ 时给一个深度 $n-1$ 的非零中心值；若 $v_p(h)\ge n+1$，该中心值为零。

这不是整个 $g(W)$ 的中心像：$I=\operatorname{Ann}_R(c_w)$ 可能有别的生成元，不能用单个整数 $h$ 代替 $I$。

## 5. 原中心核与不可删除的 Tor

置
$$
J=I/\theta=\{x\in R:\theta x\in I\}.
$$
由于 $I\subset\theta R$，$g(W)=J$，且
$$
0\to U_0\to W\xrightarrow{g}J\to0
$$
正合。$\theta$ 在 $U_0,W,J$ 上均为非零因子，故中心约化给
$$
0\to U_0/\theta U_0\to W/\theta W\to J/\theta J\to0.
$$
但 $J/\theta J\to S$ 未必单射。准确地，
$$
\boxed{
0\to U_0/\theta U_0
\to\ker(\bar g:W/\theta W\to S)
\to\frac{J\cap\theta R}{\theta J}\to0.
}
\tag{18}
$$
最后一项也可写为
$$
\frac{I\cap\theta^2R}{\theta I}
 \simeq\operatorname{Tor}_1^R(S,R/J)
 =(R/J)[\theta].
\tag{19}
$$
最后同构将 $x+J$ 送到 $\theta x+\theta J$。因此计算 $\bar f$ 在 $\ker\bar g$ 上的像时，必须支付 (19) 中元素的真实单位提升。只计算 $U_0$ 会遗漏这些方向。

作为计算记号，设
$$
\bar g(W)=p^\beta S,\qquad
\bar f(\ker\bar g)=p^\alpha S,
\qquad0\le\alpha,\beta\le n.
$$
若 $\beta<n$，选择实际 $w_0\in W$ 使 $\bar g(w_0)=p^\beta$，置 $x=\bar f(w_0)$。真实像由
$$
(p^\alpha,0),\qquad(x,p^\beta)
$$
生成，并必满足
$$
\boxed{\quad p^{n-\beta}x\in p^\alpha S.\quad}
\tag{20}
$$
这是因为 $p^{n-\beta}w_0$ 属于真实的 $\ker\bar g$，不能省略。

令 $\eta=\min\{\alpha,\beta,v_p(x)\}$，其中约化元素的赋值截于 $n$。两列矩阵的 Smith 指数为
$$
\eta,\qquad\min\{n,\alpha+\beta-\eta\}.
$$
所以存在原始关系 $a\bar f+b\bar g=0$ 的准确条件是
$$
\alpha+\beta-\eta\ge n.
\tag{21}
$$
条件成立时
$$
(a,b)=(-p^{\beta-\eta},x/p^\eta)
$$
给一条原始关系：若 $\eta=\alpha$ 严格小于另外两项，则 (21) 会迫使 $\beta\ge n$，矛盾；因此至少一个所写系数是单位。若 $\beta=n$，则 $\bar g=0$，关系 $(0,1)$ 已经原始。

这里的 Smith 计算只是原实际像的计算工具。式 (11)、(17) 并没有给出足够的新 $\alpha,\beta,\eta$ 界来无条件验证 (21)。

## 6. 一辅助素数 Kolyvagin 导数的整单位下降

固定 $N\ge1$。可把 R35 的辅助素数另加条件
$$
N\mathfrak q\equiv1\pmod{p^N}.
\tag{22}
$$
这种选择仍存在：要求 $\mathfrak q$ 完全分裂于 $K_n(\mu_{p^N})$，同时在 R35 的目标无分歧类域中取指定 Frobenius。$K_n/K$ 在 $\bar{\mathfrak p}$ 未分歧，而加 $\mu_{p^N}$ 后在 $\bar{\mathfrak p}$ 全分歧；故这部分与目标无分歧类域的交为 $K_n$。Chebotarev 因而可同时实现两项条件及原 $\lambda$ 单位条件。

令 $F_{\mathfrak q}/K$ 为模 $\mathfrak q$ 射线类域的最大 $p$ 子扩张。因 $K=\mathbb Q(i)$ 类数为一、$p\nmid4$，
$$
H=\operatorname{Gal}(F_{\mathfrak q}/K)\simeq C_{p^a},
\qquad a=v_p(N\mathfrak q-1)\ge N.
$$
它只在 $\mathfrak q$ 分歧且在该处全分歧，因而与 $K_n$ 线性无交。置
$$
L=K_nF_{\mathfrak q},\qquad m=|H|=p^a,
$$
固定 $H$ 的生成元 $\sigma$，并写
$$
D=\sum_{j=0}^{m-1}j\sigma^j,\qquad
\mathcal N_H=\sum_{j=0}^{m-1}\sigma^j.
$$
则
$$
(\sigma-1)D=m-\mathcal N_H.
\tag{23}
$$

取同一 $\mathcal T$、同一位置顺序及同一字符下的**真正秩一 Rubin–Stark 单位**
$$
\xi=\epsilon_{L/K,S\cup\{\mathfrak q\},\mathcal T}^{\{\infty\},\widetilde\chi}.
$$
Bley 对交换扩张 $L/K$ 的定理以及 BKS 保证其整性。这是以
$\epsilon_{1,n}=u_nz_n$ 为低层归一的实际 Rubin–Stark Euler 家族，不引入一个可自由扰动的参考单位。

由于 $\mathfrak q$ 完全分裂于 $K_n$，普通范数关系中的因子
$1-\operatorname{Fr}_{\mathfrak q}^{-1}$ 在 $R$ 中为零，故
$$
\mathcal N_H\xi=0.
\tag{24}
$$
也可从定义验证：低层增加完全分裂的 $\mathfrak q$ 后，$S$-截断的 $L$ 函数多一个零，秩一领先项为零；对数后的范数为零，而本字符中无根单位误差。

由 (23)–(24)，$D\xi\bmod p^N$ 为 $H$-不变量。下面精确证明它来自 $W/p^NW$，而不只来自一个可能含类群 Kummer 项的上同调群。

### 6.1 两个负号与实际下降元素

令 $t=\sigma-1$。在 $I(H)/I(H)^2$ 中，$t$ 的阶为 $m$。高阶范数的首项为
$$
\begin{aligned}
\mathcal N_H^{(1)}(\xi)
&=\sum_{j=0}^{m-1}\sigma^j\xi\otimes\sigma^{-j}\\
&=-D\xi\otimes t,
\end{aligned}
\tag{25}
$$
因为 $\sigma^{-j}\equiv1-jt\bmod I(H)^2$，而常数项由 (24) 消失。

原低层 reciprocity 泛函写为
$$
\operatorname{Rec}_{\mathfrak q}(w)=\bar\phi_{\mathfrak q}(w)\otimes t,
\qquad
\bar\phi_{\mathfrak q}:W\to R/mR.
$$
这里取真实局部 Artin 互反映射并按已固定 $\sigma$ 取坐标。BKS Theorem 5.16 的 $r=1,r'=2$ MRS 关系带符号
$(-1)^{r(r'-r)}=-1$，因而
$$
\mathcal N_H^{(1)}(\xi)
=-\nu\bigl(i_{\operatorname{Rec}_{\mathfrak q}}\epsilon\bigr).
\tag{26}
$$
式 (25) 与 (26) 的负号相消。

按第 2 节将 $\bar\phi_{\mathfrak q}$ 提升为实际
$\phi_{\mathfrak q}\in W^*$，并定义
$$
\boxed{\quad
w_{\mathfrak q}=i_{\phi_{\mathfrak q}}\epsilon
=\frac{u_n}{h}
 \left(\phi_{\mathfrak q}(z_n)z_w
       -\phi_{\mathfrak q}(z_w)z_n\right)\in W.
\quad}
\tag{27}
$$
虽然右侧可在 $\mathbb Q_p\otimes R$ 中计算，其整性来自 (7)–(8)，不要求逐项除以 $h$ 后仍整。

MRS 的自然注入 $\nu$ 在当前一个循环辅助群的情形，是单位包含映射与
$I(H)/I(H)^2=\mathbb Z/m\cdot t$ 的张量。故 (25)–(27) 给
$$
D\xi=\operatorname{res}_{L/K_n}(w_{\mathfrak q})
\quad\text{于 }L^\times\otimes\mathbb Z_p/p^N
\text{ 的目标字符分量}.
\tag{28}
$$
所需限制映射没有 Kummer 核：$K_n$ 不含 $\mu_p$，继续作 $p$ 幂扩张 $L/K_n$ 仍不含 $\mu_p$，故
$H^i(H,\mu_{p^N}(L))=0$。Inflation–restriction 因而给模 $p^N$ Kummer 类的唯一下降。$\mathcal T$ 修正在该字符上消失，已由 R32 §3 核查；在 $R[H]$ 中同一剩余特征的单位判据仍然成立。

于是通常由 $D\xi$ 定义的 Kolyvagin 类确实是
$$
\kappa_{\mathfrak q,N}
=w_{\mathfrak q}\bmod p^NW
\in W/p^NW.
\tag{29}
$$
这证明这一个实际 Euler 家族的导数落在整单位子群。一般 Kummer 类的单位–类群正合列仍含类群 $p^N$-挠；不能对任意类删去该项。

换一个 $\phi_{\mathfrak q}$ 的整提升会把 $w_{\mathfrak q}$ 改变一个 $mW\subset p^NW$ 中的元素，所以 (29) 与提升无关。若 $N\ge n$，中心类也与提升无关，因为
$p^nW\subset\theta W$。

### 6.2 与原 R36 两条泛函的准确比较

对任意 $\phi\in W^*$ 令 $w_\phi=i_\phi\epsilon$。则
$$
\boxed{
\begin{aligned}
g(w_\phi)&=\frac{u_n}{\theta}\phi(z_n),\\
f(w_\phi)&=\frac{u_n}{h}
 \left(\phi(z_n)f(z_w)-\phi(z_w)f(z_n)\right).
\end{aligned}}
\tag{30}
$$
这两项是整值；尤其第一项的整性不能靠先在 $S$ 中除 $\theta$ 来解释。对于 R36 的两条特定行，
$$
\begin{array}{c|cc}
 &f(\,\cdot\,)&g(\,\cdot\,)\\ \hline
w_f&0&p^{b_p}u_nG_{p,n}\\
w_g&-p^{b_p}u_nG_{p,n}&0.
\end{array}
\tag{31}
$$
所以用这些特定 reciprocity 行产生的单位值仍精确读出原 $G_p$，没有得到新的独立中心量。

## 7. 尚缺的实际原始性

令
$$
\mathscr C_\epsilon
=\{i_\phi\epsilon:\phi\in W^*\}\subset W.
$$
由 (9)，$S$ 上的全部对偶泛函均能从 $W^*$ 提升；又因 $S=\mathbb Z/p^n$ 的对偶分离有限 $S$-模的元素，得到准确等价
$$
\boxed{
\mathscr C_\epsilon\subset\theta W
\quad\Longleftrightarrow\quad
e_n\!\left(\operatorname{Fitt}_{R,0}(A_n/Rc_w)\right)=0.
}
\tag{32}
$$
证明：左边使所有 $(\phi\wedge\psi)(\epsilon)$ 的中心值为零；反过来这些值全为零，则每个 $i_\phi\epsilon$ 的中心类被所有 $S$-对偶消灭，由分离性该类为零。

R35 把右端理想准确识别为
$$
\operatorname{Fitt}_{S,0}(N_p/p^nN_p).
$$
因此 (29) 的单位下降并不保证其中存在中心原始元素。若 $N_p$ 有正秩，则 (32) 对所有 $n$ 成立，全部这些实际收缩单位的中心类都为零；它们仍有定义，且可继续作已付的整除。若 $N_p$ 有限，小精度也可能全零，直到精度超过真实 Fitting 长度。

本记录没有给出新的 $\alpha,\beta,\eta$ 的跨素数界，也没有证明某个实际 $w_{\mathfrak q}$ 在中心原始。所定位的下一项算术输入是：在原 reciprocity 家族或原全局单位格中，证明一个不被完整 $N_p$-Fitting 理想强制消灭的具体观测，或者给出足以验证 (21) 的额外单位/类群界。已知 Euler 因子消失、MRS 整性和同态提升本身均未提供这一输入。


## 8. 固定辅助 Euler 算子对原单位的实际作用

本节只讨论原全局单位的实际 Coleman 像，不将其任意扩张为饱和格。令
$$
\mathscr E_p=\operatorname{im}
 \left(E_\infty^{\widetilde\chi}\to U_\infty^{\widetilde\chi}\right)
 \subset\Lambda u_\infty,
\qquad B_p=\Lambda u_\infty/\mathscr E_p.
$$
R30 的类域论正合列把 $B_p$ 嵌入 R25 的 $M_p$。由 R25，$M_p$ 是有限自由 $\mathbb Z_p$-模，故 $B_p$ 也是有限自由 $\mathbb Z_p$-模；此外 $B_p$ 是 $\Lambda$-循环模。

这足以证明该实际像是主理想。设 $b=\operatorname{rank}_{\mathbb Z_p}B_p$，令 $h_p(T)$ 为 $T$ 在 $B_p$ 上作用的特征多项式。连续性使 $T$ 在 $B_p/pB_p$ 上幂零，故 $h_p$ 是次数 $b$ 的 distinguished polynomial。Cayley–Hamilton 给出满射
$$
\Lambda/(h_p)\twoheadrightarrow B_p.
$$
两边都是秩 $b$ 的自由 $\mathbb Z_p$-模；核既无挠又秩零，故为零。因此
$$
\boxed{\quad \mathscr E_p=h_p(T)\Lambda u_\infty.\quad}
\tag{33}
$$
此处没有断言有限层的全局单位全部是无穷塔范数，也没有删除 $\mathcal A_p$ 可能有的有限子模。

由原 $z_\infty$ 属于 $\mathscr E_p$，定义
$$
L_p(T)=F_p(T)/h_p(T)\in\Lambda.
$$
R30 的正合列和原特征理想等式给
$$
\operatorname{char}_\Lambda(\mathcal A_p)=(L_p).
\tag{34}
$$
写
$$
t_p=\operatorname{ord}_{\theta}L_p
 =\operatorname{length}_{\Lambda_{(\theta)}}
   (\mathcal A_p)_{(\theta)}\ge q_p.
$$
R34 的中心局部像单射又给 $\mathscr E_p\subset\theta U_\infty$，所以
$\operatorname{ord}_{\theta}h_p\ge1$。若以
$e_p=h_pu_\infty$ 作为 (33) 的基，原已构造单位满足
$$
\operatorname{loc}(z_\infty/\theta)
 =\frac{L_p}{\theta}e_p.
\tag{35}
$$
因此它在**实际全局单位局部像**中的中心重数准确为 $t_p-1$。特别地，在 $\Lambda_{(\theta)}$ 中它不是 $\theta$ 倍，当且仅当 $t_p=1$。这只给 $q_p=1$ 的一个更强充分条件；$q_p=1$ 仍允许较长的中心 Jordan 块，不能把两条件写成等价。

式 (35) 也区分了两种非零性：原 $G_p(p)\ne0$ 要求
$$
t_p=\operatorname{ord}_\theta h_p=1,
$$
而只要求 (35) 在单位像中非 $\theta$ 倍，仅要求 $t_p=1$。现有 Coleman 像并没有给出后一个条件。

现在固定一个非平凡理想 $\mathfrak a$，避开原导子和 $p$。原 CM Euler/Robert 平滑算子为
$$
s_{\mathfrak a}=N\mathfrak a\,\sigma_{\mathfrak a}^{-1}-1.
$$
在同一个中心，其准确取值是
$$
s_{\mathfrak a}(p)
 =\frac{N\mathfrak a}{\psi_E(\mathfrak a)}-1
 =\overline{\psi_E(\mathfrak a)}-1\ne0.
\tag{36}
$$
最后不等式由
$|\psi_E(\mathfrak a)|^2=N\mathfrak a>1$ 得到。对于固定 $\mathfrak a$，这是一个固定非零代数整数；除有限多个 $p$ 外它还是 $p$-进单位。普通 Euler 算子
$1-\sigma_{\mathfrak a}^{-1}$ 的中心值也非零。特别地，R35 固定 $(67)$ 的上述算子取值为 $-68$。

所以这些**具体原算子**都在 $\Lambda_{(\theta)}$ 中可逆。用它们乘，或在已经证明商整的前提下除，均保持 (35) 的 $\theta$ 重数。有限个这类操作及其 $\Lambda$-线性组合不能从一个 $\theta$ 倍产生非 $\theta$ 倍；线性组合至多增加消失阶。若改用一个在中心为零的组合再相除，那已是需要重新证明整性的中心除法，不能列为免费的 Euler 归一化。

若 $N_p$ 有正秩，R34–R35 给 $q_p\ge3$，故 $t_p\ge3$；(35) 此时至少含 $\theta^2$。因此上述固定辅助算子在该实际对象上不会提供新的原始性。反过来，尚不能从这些算子构造出 $t_p=1$ 的证明。

### 8.1 已出版 Iwasawa MRS 的中心范围

Bullach–Hofer 的已出版 Iwasawa MRS 定理给沿 $\gamma-1$ 的真实 Darmon 导数，其基准来自有限层完全分裂的素位。即使该整除可直接用于一个单位，$\gamma-1=T$ 在本题的 $\Lambda_{(T-p)}$ 中也是单位，所以它本身不降低 (35) 的中心阶。

形式换元 $\gamma\mapsto\gamma/(1+p)$ 会把其 augmentation 参数改成 $\theta/(1+p)$，但同时把原单位的 Galois 作用扭成 $\rho_E^{-1}$；所得对象不再是该定理的原 $\mathbb G_m$ 单位族。这个扭在特征零的有限群 $\Gamma_n$ 上也不下降，因为
$(1+p)^{p^{n-1}}\ne1$，只有模 $p^n$ 才下降。故未将这一换元当作原中心导数的额外原始性输入。

本节严格定位了固定算子路线的剩余量 $t_p$，没有给它上界，也没有用 $t_p$ 替换真正较弱的 $N_p$ 有限目标。


## 来源

- 本仓库 R30–R36，特别是 R32 的完整 Fitting 等式、R35 的固定辅助类和符号、R36 的两条整泛函。
- W. Bley，*On the Equivariant Tamagawa Number Conjecture for Abelian Extensions of a Quadratic Imaginary Field*，Documenta Mathematica 11 (2006)，Theorem 4.2、Corollary 4.3：[出版原文](https://ftp.gwdg.de/pub/EMIS/journals/DMJDMV/vol-11/04.pdf)。
- D. Burns、M. Kurihara、T. Sano，*On zeta elements for G_m*，Documenta Mathematica 21 (2016)，§5.3、Theorem 5.16 的 MRS 关系及 Theorem 1.5 的完整值理想：[出版原文](https://ems.press/content/serial-article-files/26320?nt=1)。
- T. Ohshita，*On higher Fitting ideals ... II*：[版本页面](https://arxiv.org/abs/1710.04568)。仅作为比较线索；本文所用特例已由 (23)–(29) 证明，不依赖该预印本的高阶理想定理。

- D. Bullach、M. Hofer，*The equivariant Tamagawa number conjecture for abelian extensions of imaginary quadratic fields*，Documenta Mathematica 28 (2023)，369–418，Theorem 6.1、Proposition 4.12：[出版 DOI](https://doi.org/10.4171/dm/907)，[公开稿](https://arxiv.org/abs/2102.01545)。这里只核其适用中心，没有调用它证明本题的非零性。
