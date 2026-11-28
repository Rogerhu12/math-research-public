# R1214：原正 PS 返回的完整中心、纯尖点整基与 CM 轮廓核

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明，原 $p\equiv11\pmod{12}$ 行。** R1213 尚存的正 deck 返回中的 $A(b)$ 系数，现由同一个原 CM 尾的实际第二个 normal 层确定。结果是完整的
$$
S_{\rm ret}=-3\gamma^2\mathscr DT,
$$
不再只是模 $kA$ 的式子。原正纯尖点最高角色格的首中心读取因此是整约化同构；全部原 CM Abel 系数的共同核有一个实际纯尖点向量，其同一原点差的完整首对数为单位。

这里不把该共同核认作 non-CM 算术线，也不把一个非零原点对数等同于消去全部 MW 的本原泛函。后继仍须保持真正的 Hecke、极化、Lie 格和 CM 部分。

## 1. 原对象与真正的高 PS 输入

保持 R1204、R1209、R1211–1213 的
$$
p=12g-1=6n+5>37,\quad m=3n+2,\quad
a=m^2,\quad b_{\rm wt}=(m+1)^2=a+p,
$$
$$
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad
E=E_m,\quad U=p e_{V_m}e_N,\quad q=U/p.
\tag{1214.1}
$$
多项式变量仍为原 Igusa 坐标 $b$；置
$$
r=1-b^3,\quad B=b^3,\quad
A(b)=bQ(B),\quad u^m=r^{n+1}A(b),\quad
A_1=A(1)=-\binom mn.
$$
不要将 $b_{\rm wt}$ 与坐标 $b$ 混同。

给定任一
$$
T\in k[B]_{\le n},
$$
原高 PS 中心微分为
$$
\bar\Psi|_I=\frac{uT(b)}{rA(b)}\,db.
\tag{1214.2}
$$
它在 SS 点正则，在 CM 点的阶为 $n$，无穷远的阶为
$m-2-\deg_bT\ge0$。自然 $\delta^*$ 角色为 $\zeta$，完整惯性权为 $b_{\rm wt}$。反向的极点和次数论证正给整个 $k[B]_{\le n}$。

R1204 的全中心主系列来源论证并不依赖负 deck：其中唯一的 $N$ 可见共同因子是原 $W_{m-1}$，$E$ 在这个高 PS 空间上恒等。故原 Hodge base change、tame/deck 单位平均和 $E$ 给实际提升 $\Psi\in E\Lambda$，具有上述两个角色与中心约化。

由 R1211 在整个最高角色格上的整性，
$$
\boxed{\quad
\Omega_T=q(\pi_0^{e_0-p}\Psi)=\pi_0^{-p}U\Psi\in\Lambda.
\quad}
\tag{1214.3}
$$
其实际首中心记为
$$
\overline{\pi_0^{-1}\Omega_T}|_I
=\frac{S_T(b)}{uA(b)}\,db,\qquad
S_T\in b\,k[B]_{\le n}.
\tag{1214.4}
$$
R1204 §§2–5 的原 generic 第 $p$ 层证明同样不使用负 deck，因此已经给
$$
S_T(s)=-3\gamma^2\mathscr DT(s)\quad(A(s)=0),
\qquad
\mathscr D=r\partial_b^2-4b^2\partial_b-\frac94b.
\tag{1214.5}
$$
由于两个多项式都在 $b\,k[B]_{\le n}$，只差一个 $kA$。以下在原标记 $b=1$ 支再读一个实际值，确定此差。

## 2. 必须读取的原 CM 层及完整 polynomial 模

原 CM 尾保持 R1197 的
$$
U_{\rm tail}^2=V^{p+1}+A_{\rm tail},\quad
x=V^6,\quad y=U_{\rm tail}V^3,\quad z_D=V^{-3}.
$$
实际 centre 参数为 $W=\pi_0V$，故 $z_DW^3=\pi_0^3$；与原厚度三节点单位的关系仍由 R1208 保留。

CM 仿射微分的惯性权是 $3m$ 的倍数。权 $b_{\rm wt}$ 的提升只有
$$
h_j=m+1+3mj,\qquad j\ge0
\tag{1214.6}
$$
这些可能 normal。所需第二个 normal 是
$$
h_c=4m+1=2p-1.
$$
除以 $\pi_0^p$ 后，它正好成为最高型的第一个 CM normal $2m=p-1$。

原中心第零层在这个节点正则。中心第 $h\ge0$ 层的 regular Laurent 项，在尾的 normal $h_c$ 处极阶至多
$$
(h_c-h)/3+1.
$$
所以最高极阶 $h_c/3+1$ 只来自 (1214.2)。较高中心层严格降低此界；既有 polar part 返回后在尾上正则，不提高当前最高极阶。所有 residue 按原 compact-type 树保留。此处没有删掉实际提升中的未知高中心系数。

原 full 分支到粗 CM 尾在无穷的分歧指数为六，且
$\operatorname{div}(\eta)=(p-2)\sum_\infty[\infty]$。令 $d=h_c/3$，则完整系数微分的 polynomial representative 次数至多
$$
6d+p-1=2h_c+p-1=5p-3.
$$
按 R1204.9a 的同一 full framing，
$$
D+1-p+(p+1)t\equiv-2(b_{\rm wt}-h_c)\pmod{p^2-1},
\quad D=5p-3,
$$
给 $t\equiv m-1\pmod{p-1}$。原齐次化及全部 Weil 分支运输遂将**整个**此层放入
$$
\mathcal M_c=\operatorname{Sym}^{5p-3}(k^2)\otimes\det^{m-1}.
\tag{1214.7}
$$
因原 $\Psi=E\Psi$ 且 full 换基在整个 $R/(p)$ 仿射图为常线性，其完整当前系数在 $E\mathcal M_c$ 中。$h_c<e_0$，没有超过真实模型的精度。

## 3. 原整角在该完整模上准确为二维

令 $\mathfrak c=X^pY-XY^p$，按它的幂过滤 (1214.7)。
记 $W_j=\operatorname{Sym}^{2j}(k^2)\det^{-j}$、
$\eta_{\rm det}=\det^m$。全部非终端和终端如下：

| $\mathfrak c$ 次数 | 准确组成因子 | $E_m$ 可见份数 |
|---|---|---|
| $0$ | $W_1\otimes\eta_{\rm det}$，$W_{m-1}$ | $1$ |
| $1$ | $\eta_{\rm det}$，$\operatorname{St}\otimes\eta_{\rm det}$ | $0$ |
| $2$ | $W_{m-1}$，$W_1\otimes\eta_{\rm det}$ | $1$ |
| $3$ | $W_{m-2}$，$W_2\otimes\eta_{\rm det}$ | $0$ |
| $4$，终端 | $W_{m-3}$ | $0$ |

这里终端次数是 $p-7$，不是一个还含第二因子的 evaluation quotient。各 $\eta_{\rm det}$ 扭曲因子无原 $N$ 固定线；$W_{m-2},W_{m-3}$ 属其它角。原幂等元取像 exact，所以
$$
\dim_kE\mathcal M_c=2.
\tag{1214.8}
$$
没有从这张维数表推定 $U$ 的作用；下一节从已付的原群环矩阵搬运它。

## 4. 等变 $\Theta^2$ 给准确的 CM 临界算子

保持原 Cartan 坐标
$$
\mathfrak c=A_0^{p+1}-B_0^{p+1},\quad
U_{\rm tail}=(A_0^{p+1}+B_0^{p+1})/2,\quad
V=A_0B_0,\quad A_{\rm tail}=\mathfrak c^2/4,
$$
以及真正等变的
$$
\Theta=X^p\partial_X+Y^p\partial_Y,\quad
\Theta V=2U_{\rm tail},\quad
\Theta U_{\rm tail}=V^p,\quad \Theta\mathfrak c=0.
$$
置 $h=V^{m-1}$、$F=U_{\rm tail}V^{m-2}$，所以 $dF=(\Theta F)\eta$。

R1203 的原临界模
$\mathcal M_{\rm crit}=\operatorname{Sym}^{3p-1}\det^{m-1}$
在其完整 $E$ 像中有原基
$$
F_1=V^{3m+1},\qquad
F_0=2F_1+\mathfrak c^2h,
$$
且
$$
\bar UF_1=\frac{\mathfrak c^2h}{8},\qquad
\bar U(\mathfrak c^2h)=0.
\tag{1214.9}
$$
两次 $\Theta$ 每次增次数 $p-1$，给同一个 $G$-等变映射
$\mathcal M_{\rm crit}\to\mathcal M_c$，并与 $E,U$ 交换。
直接在特征 $p$ 算得
$$
\Theta^2F_1
=2V^{5m+1}+3A_{\rm tail}V^{3m-1},
$$
$$
\Theta h=-3F,\qquad
\Theta^2(\mathfrak c^2h)=-3\mathfrak c^2\Theta F,
$$
$$
\Theta F=-4V^{3m-1}-5A_{\rm tail}V^{m-3}.
\tag{1214.10}
$$
第一向量的最高 $V$ 项为 $2V^{5m+1}$，第二向量的最高 $V$ 项严格较低，且非零。它们独立并由 (1214.8) 张成完整 $E\mathcal M_c$。

故若给定实际当前系数的 full polynomial 最高 $V^{5m+1}$ 系数为 $\ell$，由 (1214.9)–(1214.10) 准确有
$$
\boxed{\quad
\bar U(\text{整个当前系数})\,\eta
=-\frac{3\mathfrak c^2\ell}{16}\,dF
=-\frac{3A_{\rm tail}\ell}{4}\,dF.
\quad}
\tag{1214.11}
$$
这里“最高系数”在固定原非零 pairing 分支读取，determinant 运输仍在完整模中；不能把 $\mathfrak c$ 在评价点设为零。完整较低极部所在的一维线确被 $U$ 杀掉。所有高中心层及 holomorphic 提升差都包含在这条被杀线中，没有凭极阶删去原微分。

## 5. 同一个 good CM 来源给实际最高系数

在原 $b=1$ 支，沿 R1209 的 good CM 参数
$$
v^3=r,\quad t=vG/F_{\rm per},\quad
t=\vartheta W^m,\qquad
u=\tau W^{m+1}K(t),\quad
K=(v/t)F_{\rm per}^{-2}.
$$
这里 $F_{\rm per}$ 是 R1209 的周期 $F$，不同于上一节的尾函数 $F$；$\vartheta$ 是该文的同一个 $c_1$，没有新选单位。原
$$
\frac{db}{dt}=-v^2F_{\rm per}^2
$$
给
$$
\frac{uT}{rA}\,db
=-\tau W^{m+1}\frac{T}{tA}\,dt
=-m\tau W^mR(t)\,dW,\qquad
R(t)=\frac{T(b(t))}{A(b(t))}.
\tag{1214.12}
$$
对于本篇 $T\in k[B]$，$R$ 只含 $t^3$ 幂。写
$R=R_0+R_1t^3+\cdots$。原 normal $h_c=4m+1$ 的最高极部于是为
$$
-m\tau\vartheta^3R_1\,V^{4m}\,dV.
$$
用同一个 $\eta=dV/(2U_{\rm tail})$ 及原分支
$U_{\rm tail}\sim V^{m+1}$，它给
$$
\boxed{\quad \ell=-2m\tau\vartheta^3R_1.\quad}
\tag{1214.13}
$$
这只读取实际最高极部，不把 $U_{\rm tail}V^{4m}$ 猜作整个 $N$ 固定 polynomial 系数。整个系数的来源与较低项已在 §§2–4 支付。

将 (1214.13) 代入 (1214.11)，再按 (1214.3) 除 $\pi_0^p$，原返回的第 $2m$ 个 CM normal 为
$$
\Omega_T^{[2m]}
=\frac{3m\tau\vartheta^3 A_{\rm tail}}2\,R_1\,dF.
\tag{1214.14}
$$

## 6. 原 canonical 相位锁定 $A$ 的系数

R1213/R1209 对给定首中心 $S_T$ 的同一 first CM 层，给
$$
\Omega_T^{[2m]}
=\frac{m\vartheta^3S_T(1)}{2\tau A_1}\,dF.
\tag{1214.15}
$$
为核这个尺度，$d_1=(2m-1)/3=-2/3$，
$e_0(S_T)=-S_T(1)/A_1$，代入
$m\vartheta^3e_0/(3\tau d_1)$ 即得 (1214.15)。
于是 (1214.14)–(1214.15) 迫
$$
S_T(1)=3\tau^2A_{\rm tail}A_1R_1.
\tag{1214.16}
$$

所需平方相位不是一个未知单位。R1208.26–27 在同一 good 模型已经给
$$
B_{\rm good}=-2A_1,\qquad
\tau=\frac{B_{\rm good}^{p+1}}{A_1},\qquad
A_{\rm tail}=-\frac{3\gamma^2}{B_{\rm good}^{2p}}.
$$
因此直接有
$$
\boxed{\quad
\tau^2A_{\rm tail}
=-\frac{3\gamma^2B_{\rm good}^2}{A_1^2}
=-12\gamma^2.
\quad}
\tag{1214.17}
$$
此式没有把普通 SS 的 $2rh'$ 公式代到退化的 $r=0$；它使用实际 good CM 的已付 Poincaré/Weil 规范。

R1206/R1209 的有理微分恒等式对任意 $T$ 线性成立，给
$$
\mathcal E_{\mathscr DT}=-(tR)''
=-12R_1t^2+\cdots.
$$
另一方面它的 $t^2$ 系数是 $-\mathscr DT(1)/A_1$，故
$$
\mathscr DT(1)=12A_1R_1.
\tag{1214.18}
$$
(1214.16)–(1214.18) 遂给
$S_T(1)=-3\gamma^2\mathscr DT(1)$。
结合 (1214.5) 以及 $A_1\ne0$，得到所求完整等式
$$
\boxed{\quad
S_T(b)=-3\gamma^2
\left((1-b^3)T''-4b^2T'-\frac94bT\right).
\quad}
\tag{1214.19}
$$
原返回的额外全纯 $A$ 系数已真实确定；没有通过任选中心延伸将它设为零。结果只依赖实际中心约化 $T$，所有允许的提升差均在 (1214.11) 的被杀低极线中。

## 7. 正纯尖点最高格的首中心同构和实际整基

令 $\Gamma_+$ 为 R1211 的最高惯性权、自然正 deck 的 $W$ 格。该文保证 $q$ 是其整幂等元，R1205.11、1205.14 给
$$
\operatorname{rank}_W(q\Gamma_+)=n+1.
$$
而原多项式算子有明确三角式
$$
\mathscr D(B^j)
=b\left(3j(3j-1)B^{j-1}
-\frac94(2j+1)^2B^j\right),\quad0\le j\le n.
\tag{1214.20}
$$
所有对角系数为单位；所以
$-3\gamma^2\mathscr D:k[B]_{\le n}\to b\,k[B]_{\le n}$
是同构。

取 $1,B,\ldots,B^n$ 的任一实际高 PS 提升 $\Psi_j$，则
$$
\boxed{\quad
\pi_0^{-p}U\Psi_0,\ldots,\pi_0^{-p}U\Psi_n
\text{ 是 }q\Gamma_+\text{ 的一个 }W\text{-基}.
\quad}
\tag{1214.21}
$$
证明是其真实首中心由 (1214.19)–(1214.20) 线性独立；任何模 $p$ 的关系在首中心读取后使全部系数为零。再用实际秩及 Nakayama。
因此完整首中心映射给
$$
\boxed{\quad
q\Gamma_+/pq\Gamma_+
\xrightarrow{\ \sim\ }b\,k[B]_{\le n}.
\quad}
\tag{1214.22}
$$
这是首中心同构。原 generic 底仍只有 $n$ 维，其核正由 $kA$ 表示；没有将它改称 generic 底单射，也没有将此角色格结论外推为整个 BT 的整分裂。

## 8. 实际纯尖点的完整 CM 轮廓核与首对数单位

保持原有理盘 $w=(a_{\rm coarse}-1)/p^3$、
$z_{\rm CM}=\varepsilon^3w$、$\varepsilon=\pi_0^m$。
R1193 §7 的全尾证明只用最高惯性权，故对 (1214.22) 的实际正微分同样给
$$
H_\Omega(w)=\varepsilon^{-m}\int_{c_1}^{x(w)}\Omega
\in W\langle w\rangle,\qquad
\deg\bar H_\Omega\le n,\quad H_\Omega(0)=0.
$$
所有 $p$ 倍积分次数仍至少再含一个 $p$，并未仅比较有限 Taylor 窗。

R1213 的全部 CM normal 及 R1197 的相同一维角像，给从高到低的旗标
$$
S(1),S'(1),\ldots,S^{(n-1)}(1)
$$
乘原单位三角矩阵。$S=bP(B)$、$b(1)=1$ 及
$dB/db(1)=3$ 为单位，所以此旗标满秩 $n$，共同核为
$$
kS_+,\qquad S_+=b(B-1)^n=-b\,r^n.
\tag{1214.23}
$$
由 (1214.22)，它确有实际纯尖点提升；可以明确取
$T_+=(-3\gamma^2\mathscr D)^{-1}S_+$ 后应用 (1214.3)，反解只除 (1214.20) 的显示单位。

在 R1213 的同一周期中，
$$
\mathcal E_{S_+}
=\frac{v^{3n+2}bF_{\rm per}^3}{A_1},
\qquad [t^m]\mathcal E_{S_+}=\frac1{A_1}.
$$
因此它的完整首对数不是只有 SS 部分，而是
$$
\boxed{\quad
\bar H_{\Omega_{T_+}}=0,\qquad
\mathcal V_m^+(S_+)
=-\frac{8\,2^m\nu}{A_1^2}\in k^\times.
\quad}
\tag{1214.24}
$$
全部三个 CM 支、analytic、static 和 node 接口已由 R1213 支付。

## 9. 后续真实算术比较仍保留

(1214.24) 是同一个原 $P=(p-1)D_0$、实际纯尖点格和完整盘轮廓的结论。它不证明 $S_+$ 是或不是原 CM 算术线，也不证明其 non-CM 投影为单位。原最高正部分的 CM 系统须按 R1212 的实际算术 twist 及原 Hecke 去识别。

同样，首中心同构不代替从真实纯尖点 Lie 格到 R1212 ambient Gram 的整运输。要消去全部 MW，仍须保 R1036/R1063 的完整原 log、split-Hecke 平衡、CM 消去和饱和格；不能因某一向量的 $V$ 为单位便宣布存在所需本原 whole-MW 法向。现在可继续的正额外方向已由具体 (1214.19)–(1214.22) 给出，不再留一个未知 $A$ 系数。

来源：R1203 的原 $U$ 群环矩阵；R1204 §§2–5 的实际高 PS 输入/普通节点；R1197 的 full CM 极界与齐次化；R1208 §9 的 canonical good CM 相位；R1209 的同一有限周期；R1211 的整个最高角色整性、R1205 的实际正重数，以及 R1213 的全正首对数。root 原推，global_route 独立核完整模/群作用/节点系数/相位及返回链。全文为纸面证明；没有数学程序执行或新素数窗口。主目标仍 OPEN。

独立末审：global_route 全文复核 §§7–8 的真实首中心降模、三角单位、秩/Nakayama、全尾界及正 deck 旗标；共同核和 e_n、V 的符号尺度均 PASS。根复核完整原群模和源系数。
