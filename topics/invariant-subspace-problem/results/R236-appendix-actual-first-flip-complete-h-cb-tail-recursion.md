# R236 附录：真实first-flip双行的完整全层尾递推与同一正常态cb费用

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的来源保留扩展。** 本稿将 h 基准的完整全层递推接到已经发表的真实 first-flip N 双行。
保留第二行全部移位 carry、原四个来源因子和产生它们的同一个正常态。
初始尾交由四次真实物理余式建立，不把指定迟首纯系数族的 U 坐标常数直接代入这对不同的原行。
完成后，完整正常 cb 余式及其原双源的统一上型仍为 $140/9$，
完整尾生成元及原源为 $175/6$；未取得统一有界锚，也未证明 first-flip 条件总成立。

## 1. 原真实来源和明确适用条件

固定[真实 first-flip 稿](R236-appendix-carry-corrected-first-flip-n-pair-and-next-k-lift.md)
§1 的同一个核配对、同一个 first-flip 参数以及从中得到的同一个正正常 $\rho$。
这里沿用该稿的条件假设，不另行选择 gauge 或态。

记 $n\ge1$、$x=n+1\ge2$、$m=n+1$、$l=n+2$、
$k_0=n+3$、$j_0=n+4$、$s=16^n$。
准确原双行为
$$
S=\sum_{i\ge n}a_iN_i,\qquad
Z=a_n^2N_n+\sum_{i>n}(a_i^2-a_{i-1}^2\eta_{i-1})N_i,
\qquad a_i=(i+1)^{-2}.
\tag{1.1}
$$
置 $r_n=a_n$，
$$
r_i=a_i-\frac{a_{i-1}^2}{a_i}\eta_{i-1}\quad(i>n),\qquad
d=r_n-r_m,\quad b_i=a_i(r_n-r_i).
$$
已付的准确正差分界为
$$
.99g_i\le r_i-r_{i+1}\le1.01g_i\quad(i>n),\qquad
g_n\le d\le1.01g_n,\quad g_i=a_i-a_{i+1}.
\tag{1.2}
$$

原实际行
$$
P_m=(r_nS-Z)/b_m=N_m+V,\qquad
U=\sum_{i\ge l}\frac{a_i(r_m-r_i)}dN_i
$$
满足 $F:=\sum_{i\ge m}a_iN_i=a_mP_m-U$。记
$$
\varepsilon=\eta_n/x^4,\quad\delta=\eta_m,\qquad
H=V^2-\delta N_l,\quad K=U^2+\varepsilon V.
$$
全部四个原来源继续使用
$$
H_S=r_n(V-N_m)/b_m,\quad H_Z=-(V-N_m)/b_m,
$$
$$
K_S=F-a_nN_n-r_nE/b_m,\quad K_Z=E/b_m,\qquad
E=a_m^2P_m-2a_mU-\varepsilon I.
\tag{1.3}
$$
其中
$$
\|U\|\le.505<1,\quad \|V\|\le5x^2,\quad b_m^{-1}\le8x^5,
$$
$$
\|H_S\|\le48x^5,\quad\|H_Z\|\le48x^7,\quad
\|K_S\|\le74x,\quad\|K_Z\|\le72x^3.
\tag{1.4}
$$
$U$ 的正号及 E 中的负号保持原定义，没有回换到另一对纯系数行。

## 2. 当前正 k 枢轴的全部逆和原来源

写
$$
U=\alpha N_l+u,\qquad V=\beta N_l+v.
$$
由 (1.2)，
$$
\alpha\ge\frac{.99}{1.01}
\frac{x^2(2x+3)}{(x+2)^4(2x+1)}
\ge\frac1{24x^2},\qquad \alpha\le1.
$$
又 $r_n-r_l>d$，故
$$
\boxed{\frac12\le\beta\le3,\qquad
\|u\|\le1,\quad\|v\|\le5x^2.}
\tag{2.1}
$$
$\alpha$ 的下界可直接用 $x+2\le2x$、$2x+1\le(5/2)x$ 核算。

使用[正 k 枢轴稿](R236-appendix-positive-k-pivot-and-paid-original-two-row-normalization.md)
的准确公式，令
$$
t=\eta_lN_{l+1},\quad
c_0=\varepsilon\beta/(2\alpha),\quad
q_0=\frac{\varepsilon^2\beta^2}{4\alpha^2}+\frac{\varepsilon\delta}{2\beta},
\quad q=q_0I+\alpha^2t.
$$
由 $\delta\le\varepsilon$ 及 (2.1)，
$$
\frac{\varepsilon^2}{16}\le q_0\le1297x^4\varepsilon^2.
$$
完整实际小量为
$$
\boxed{
\frac{\alpha^2\eta_l}{q_0}
\le16x^8e^{-u_l+2u_n}
\le e^{-315269s}<1/2.
}
\tag{2.2}
$$
这里用原 $u_l\ge318080s$、$u_n\le1400s$、$\log x\le s$；
同样 $\delta/\varepsilon\le e^{-15956s}<1$。
因此
$$
\|q^{-1}\|\le32\varepsilon^{-2},\qquad
\|q\|\le2000x^4\varepsilon^2.
\tag{2.3}
$$

定义四个实际块
$$
C_H=v^2+\beta^2t,\quad D_H=2\beta v-\delta I,\qquad
C_K=u^2+\alpha^2t+\varepsilon v,\quad D_K=2\alpha u+\varepsilon\beta I.
$$
实际源和目标为
$$
A=-\frac{\varepsilon}{2\beta}q^{-1},\qquad
B=\left[N_l-\frac{u-c_0}{2\alpha}\right]q^{-1},
$$
$$
R_l=
\left[tD_K-\frac{u-c_0}{2\alpha}C_K-\frac{\varepsilon}{2\beta}C_H\right]q^{-1},
$$
$$
\boxed{P_l=N_l+R_l=HA+KB.}
\tag{2.4}
$$
$c_0\le36\eta_n/x^2<1$，从而
$$
\|A\|\le32\varepsilon^{-1},\qquad
\|B\|\le800x^2\varepsilon^{-2},\qquad
\|R_l\|\le1600x^2\varepsilon^{-2}.
$$
把 (1.3) 逐项代入，两个原源为
$$
\boxed{
\mathcal U_l=H_SA+K_SB,\qquad
\mathcal V_l=H_ZA+K_ZB,
}
$$
$$
\|\mathcal U_l\|,\|\mathcal V_l\|
\le61000x^7\varepsilon^{-2}.
\tag{2.5}
$$
因此可统一取
$$
\boxed{\|R_l\|,\|\mathcal U_l\|,\|\mathcal V_l\|\le e^{3000s}.}
\tag{2.6}
$$

反向也已付清：
$$
A^{-1}=-2\beta q/\varepsilon,\qquad
\|A^{-1}\|\le12000x^4\varepsilon=12000\eta_n,
$$
$$
H=-\frac{2\beta q}{\varepsilon}P_l
+\frac{2\beta}{\varepsilon}
\left[N_l-\frac{u-c_0}{2\alpha}\right]K,
$$
第二个系数范数至多 $150x^2\varepsilon^{-1}$。
故完整 $(H,K)=(P_l,K)$ 的代数及两种闭包身份都有真实来源和明确单位费。

## 3. 四次物理余式建立完整三生成元初尾

首先使用原 $S/a_n=N_n+F/a_n$ 的物理余式，其代表范数至多 x，
cb 范数至多 $1+x$。
再使用 $P_m=N_m+V$ 的物理余式，其 cb 范数至多 $1+5x^2$。
二者复合记为 $R_{\rm pre}:\mathcal C_n\to\mathcal C_l$，则
$$
\boxed{
\|R_{\rm pre}\|_{\rm cb}\le12x^3,\qquad
X-R_{\rm pre}X=S A_{\rm pre}(X)+ZB_{\rm pre}(X),
}
$$
$$
\boxed{\|A_{\rm pre}\|_{\rm cb},\|B_{\rm pre}\|_{\rm cb}\le20x^6.}
\tag{3.1}
$$
第二行的原源分别是 $r_n/b_m,-1/b_m$，其范数至多 $8x^5$；
再乘首余式 cb 范数 $1+x\le2x$，并加入第一步 $a_n^{-1}=x^2$，
得到 (3.1)。所有源都是正常线性映射。

原两次完整尾交已经是 $(H,K)$。现在用 (2.4) 的 $P_l$
作第三次物理余式，完整第 $k_0=l+1$ 位尾交为
$$
\boxed{
J_{k_0}=(R_l^2-\eta_lN_{k_0},\ C_K-R_lD_K).
}
\tag{3.2}
$$
其两个生成元、各自两个原源均可用 $e^{6100s}$ 控制。
例如新 h 原源为 $(R_l-N_l)(\mathcal U_l,\mathcal V_l)$，
另一个原源为 $(K_S,K_Z)-D_K(\mathcal U_l,\mathcal V_l)$。

真实 first-flip 稿 §5 已为同一 S,Z 支付
$$
P_{k_0}^{h}=N_{k_0}+R_{k_0}^{h}
=S\mathcal U_{k_0}^{h}+Z\mathcal V_{k_0}^{h},
$$
$$
\|R_{k_0}^{h}\|\le e^{210000s},\qquad
\|\mathcal U_{k_0}^{h}\|,\|\mathcal V_{k_0}^{h}\|\le e^{590000s}.
\tag{3.3}
$$
该行是完整 $J_{k_0}$ 的真实成员，把它冗余加入后作第四次物理余式。
这给完整 $J_{j_0}$ 的三个生成元：
$$
(R_{k_0}^{h})^2-\eta_{k_0}N_{j_0},\qquad
a_i-R_{k_0}^{h}b_i\quad(i=1,2),
\tag{3.4}
$$
其中 $a_i+N_{k_0}b_i$ 是 (3.2) 两个实际生成元。
所有 carry 都保留。它们和全部原双源满足
$$
\boxed{
\|G_{j_0,i}\|\le e^{421000s},\qquad
\|\mathbf G_{j_0,i}\|_{\max}\le e^{801000s}.
}
\tag{3.5}
$$

四次物理余式的完整正常复合记为
$\mathfrak R_{j_0}:\mathcal C_n\to\mathcal C_{j_0}$。
(3.1)、(2.6)、(3.3) 给
$$
\boxed{
\|\mathfrak R_{j_0}\|_{\rm cb}\le e^{214000s},\qquad
X-\mathfrak R_{j_0}X
=S\mathcal A_{j_0}(X)+Z\mathcal B_{j_0}(X),
}
$$
$$
\boxed{
\|\mathcal A_{j_0}\|_{\rm cb},\|\mathcal B_{j_0}\|_{\rm cb}
\le e^{594000s}.
}
\tag{3.6}
$$
例如最后一步来源费用至多
$e^{590000s}\cdot12x^3(1+e^{3000s})$，
其余前三步更小；所列常数有余量。
这些 cb 界来自实际物理块压缩，不随有限矩阵放大改变。

## 4. 全层 primitive、完整生成元与任意原右目标

从 (3.3) 继续原 carry-h 链，仍取
$$
L_{k_0}=210000s,\qquad L_{j+1}=4L_j+2u_j+\log8,\qquad
A_n=e^{380000s},\quad c=7/2.
$$
全部真实单位和原源按[h 基准稿](R236-appendix-complete-h-reference-retractions-and-small-primitive-type.md)
§1 支付：
$$
\|R_j^{h}\|\le e^{L_j},\qquad
\|\mathcal U_j^{h}\|,\|\mathcal V_j^{h}\|
\le A_nc^{j-k_0}e^{L_j}.
$$
后续每层把这一原成员冗余加入完整理想，并作物理余式
$r_j(a+N_jb)=a-R_j^{h}b$。

在本稿采用直接四位初值
$$
v_{j_0}=\mathfrak R_{j_0}(U),
$$
不把它另认作先前的固定点 $u_*$。由 (3.6) 和 $\|U\|\le1$，
其目标/原源分别受 $e^{214000s}$、$e^{594000s}$ 控制。
定义
$$
\mu_{j_0}=214000s,\qquad \mu_{j+1}=\mu_j+L_j+\log2,
$$
$$
\gamma_{j_0}=421000s,\qquad
\gamma_{j+1}=\max\{2L_j,\gamma_j+L_j\}+\log2.
\tag{4.1}
$$
于是完全相同的真实归纳给全部 $j\ge j_0$：
$$
\boxed{
\|\mathfrak R_j\|_{\rm cb}\le e^{\mu_j},\quad
\|\mathcal A_j\|_{\rm cb},\|\mathcal B_j\|_{\rm cb}
\le A_nc^{j-k_0}e^{\mu_j},
}
$$
$$
\boxed{
v_j=\mathfrak R_j(U)\in\mathcal B_j,\quad \chi(v_j)=0,\quad
\|v_j\|\le e^{\mu_j},\quad
\|{\rm source}(U-v_j)\|_{\max}\le A_nc^{j-k_0}e^{\mu_j}.
}
\tag{4.2}
$$
完整 $j-n-1$ 个尾生成元及其原双源满足
$$
\boxed{
\|G_{j,i}\|\le e^{\gamma_j},\qquad
\|\mathbf G_{j,i}\|_{\max}\le A_nc^{j-k_0}e^{\gamma_j}.
}
\tag{4.3}
$$
初始原源指数 $801000s$ 恰被 $380000s+421000s$ 覆盖；
$c^{j_0-k_0}>1$ 另留余量。

完整代数及闭包身份为
$$
\boxed{
(S,Z)_{\mathcal C_n}=\mathfrak R_j^{-1}(J_j),\qquad
(S,Z)_{\mathcal C_n}\cap\mathcal C_j=J_j,
}
$$
$$
\boxed{
\overline{(S,Z)_{\mathcal C_n}}^{\,\nu}
=\mathfrak R_j^{-1}(\overline{J_j}^{\,\nu}),
\qquad \nu=\|\cdot\|\text{ 或 }uw.
}
\tag{4.4}
$$
如果给定 $\mathfrak R_jX=\sum_iG_{j,i}b_i$ 的实际尾分解，
每个返回原源的范数至多
$$
\boxed{
A_nc^{j-k_0}\left(e^{\mu_j}\|X\|+
e^{\gamma_j}\sum_i\|b_i\|\right).
}
\tag{4.5}
$$
同一界对每个有限矩阵放大成立；没有假定生成元分解存在统一小范数。

由原精确 carry，
$$
\boxed{
\lim_{j\to\infty}\mu_j/16^j=140/9,\qquad
\lim_{j\to\infty}\gamma_j/16^j=175/6.
}
\tag{4.6}
$$
因此这两个上型现在适用于**有真实 first-flip 来源的同一个固定原理想和正常态**。

## 5. 正多项式结构及来源边界

该真实 pair 的系数
$$
\alpha_i=\frac{a_i(r_m-r_i)}d,\qquad
\beta_i=\frac{a_i(r_n-r_i)}{a_md}
$$
还满足
$$
\lambda_i=\alpha_i/\beta_i
=a_m\frac{r_m-r_i}{r_n-r_i},
$$
它随 i 严格增加，且趋于有限正数
$\lambda_\infty=a_mr_m/r_n$。
故固定起点正多项式递推可保留一般正更新
$f_{j+1}=f_j+(\lambda_j-\lambda_{j-1})g_j$；
其系数和真实线性尾须使用这里的 $\alpha_i,\beta_i$，
不能用未修正纯系数 pair 的显式 $h_j=(2j+1)/(n+2)^4$ 代替。
本稿的 h/正常 cb 证明不依赖那条不同 pair 的显式公式。

每个 $P_j^{h}$ 仍有准确条件锚
$e_j^*[2P_j^{h}(I+N_j)^{-2}]e_j=I$，
并由 (1.3)、(3.3) 及后续实际源保持同一个原 $\rho$ 的全部右湮灭。
费用上型有限没有给出一致有界目标或不消失的统一归一锚。

本稿始终保留首段假设：那个指定 first-flip 必须已经给出非零原核配对。
没有证明这种 flip 总能选到，没有把另一个 gauge 的见证移过来，
也没有外推一般 Cayley Q/H 双行。


## 6. 改进上型对真实尾残量到底给出什么

这一节保留同一个原正常态，不以一般正常性的极限替代速率。
令 $\tau=\operatorname{Tr}\rho>0$，
$\rho_j=\operatorname{Tr}_{<j}\rho$ 是实际尾部分迹，
$\Omega_j$ 是原 Haar 无限张量的尾真空，并记
$$
\delta_j=\|\rho_j-\tau|\Omega_j\rangle\langle\Omega_j|\|_1.
$$
正常性只给 $\delta_j\to0$。
一个直接证明是先在迹范数中用只占有限头的有限秩算子逼近 $\rho$；
对所有更远尾，其部分迹准确为该近似算子迹乘尾真空投影，
再用部分迹在迹类上的收缩性。

对每个实际 $T_j\in J_j$，同一原来源给
$\operatorname{Tr}(\rho_jT_j)=0$，故
$$
\boxed{
\tau|\omega_j(T_j)|\le\delta_j\|T_j\|.
}
\tag{6.1}
$$
因此本稿新费用只给以下准确条件界：
若 $X\in(S,Z)_{\mathcal C_n}$，则
$$
\boxed{
|\omega_j(\mathfrak R_jX)|
\le(\delta_j/\tau)e^{\mu_j}\|X\|.
}
\tag{6.2}
$$
若给定 $T_j=\sum_iG_{j,i}b_i$，则
$$
\boxed{
|\omega_j(T_j)|
\le(\delta_j/\tau)e^{\gamma_j}\sum_i\|b_i\|.
}
\tag{6.3}
$$
没有额外的 $\delta_je^{\mu_j}\to0$ 或 $\delta_je^{\gamma_j}\to0$ 时，
$140/9$ 和 $175/6$ 这两个上型本身不足以得到新的非消失归一锚。

反过来，若在这些同一实际理想中构造出统一有界的远尾 $T_j$，
且 $|\omega_j(T_j)|$ 有统一正下界，(6.1) 就会排除该原正常态。
这是真正仍需支付的锚条件。
$\mathfrak R_j(I)=I$ 不提供这样的理想目标：
其原缺陷为零，I 从未被证明属于原理想。
而初始物理消元准确杀掉 S 和 Z，
故 $\mathfrak R_j(S)=\mathfrak R_j(Z)=0$ 也不能自动提供锚。

现有 h 条件锚只给
$$
\delta_j\ge
\frac{\tau}{9(1+e^{L_j})},
$$
与任意慢的 $\delta_j\downarrow0$ 相容。
这条必要下界不被当成衰减上界，也没有把一个非湮灭正常态的尾例外
当作实际见证的反例。

