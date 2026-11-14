# R287 — 原三条一阶原函数的真实 dyadic 像、完整交换差与未投影乘子

日期：2026-11-13。**状态：以下真实 $\mathcal V G_H$、$Q_{0,+}G_A^{\rm CM}$、$Q_{0,+}G_B^{\rm CM}$ 的全部系数、相位、两侧未投影项、联合独立性和保质量 Mellin 恒等式均已证明。这三个实际交换差并未闭回原三条中央行及两个 CM 参考，不能由此宣称原中央非零。**

本篇只使用 R229/R246 的实际 theta 群算子，以及 R283/R284 已付出的原一阶原函数。所有计算是固定有理或 Gaussian 计算；没有目标素数扫描。尤其不把一个投影后的连接代替完整连接。

## 1. 原归一、边界与共同次数

继续写
$$
U=x^2,\quad v=x^{-2},\quad
S_A=A_{17}(2z)/16,\quad S_B=A_{34}(z),\quad S_H=A_{136}(z),
$$
$$
L=\partial_z-\mathcal W,\qquad
\mathcal W=68\zeta+71y/x.
\tag{1}
$$
令 $\beta=4-i$，$C_\beta=\vartheta(2\beta z)$。R283 的两个唯一全纯 CM 补偿原函数和第三条原函数分别为
$$
K_A=\sigma^{68}yP_A^G(U),\qquad
K_B=\sigma^{68}yP_B^G(U),\qquad
K_H=-x\vartheta\sigma^{67}P_H^G(U),
\tag{2}
$$
其中前两式是 $G_A^{\rm CM},G_B^{\rm CM}$，不是带原点归一常数的有极 $G_A,G_B$。准确有
$$
LK_A=S_A-c_AC_\beta=:E_A,\quad
LK_B=S_B-c_BC_\beta=:E_B,\quad LK_H=S_H.
\tag{3}
$$
全部 $P_i^G,c_i$ 取 R283 证书的原值，未在运输时重新选择原函数常数。具体地
$$
c_A=-\frac{a_0}{2e_\beta},\quad c_B=-\frac{b_0}{2e_\beta},\quad
a_0=-\frac{1248227362551868}{22563055139625},\quad
b_0=\frac{727339049799116}{7521018379875},
$$
$$
e_\beta=
\frac{194313797443214851}{4512611027925}
-\frac{218295166992512}{31556720475}i.
\tag{4}
$$
在 untwisted 十七维块上，完整连接是
$$
L(\sigma^{68}yP)=\sigma^{68}\mathscr L P,\qquad
\boxed{\mathscr L P=4U(U-1)P'+(70-68U)P.}
\tag{5}
$$
记 $P_A,P_B,C_\beta(U)$ 为 $S_A,S_B,C_\beta$ 在 $\sigma^{68}$ frame 中的原多项式。不要把 $P_A^G$ 与 $P_A$ 混同。

$\mathcal U,\mathcal V$ 始终是 R246 的共同 $[2]$ 拉回后的 degree-$272$ 算子；$Q_{0,+}$ 是 R229 的实际八项算子，并沿同一个 $[2]$ 拉回。若令
$$
L_2=\partial_z-2\mathcal W(2z),
$$
则 $L_2K(2z)=2(LK)(2z)$。下文将输出重新写成 $F(2z)$，所以完整交换差使用 $\tfrac12L_2$。这一步的二因子、共同正 theta 权和 charge 均保留。

## 2. 旧奇块的准确四维坐标

设 $\Pi_0$ 为 R246 的旧块投影。untwisted 奇块中的像恰为
$$
\mathcal O_i=
\operatorname{span}\{g_1(2z),g_2(2z),g_3(2z),g_4(2z)\},
\qquad g_j(w)=\vartheta(w)^{17}y(w)v(w)^j.
\tag{6}
$$
在 native $\sigma^{68}y$ frame 中，这四列为
$$
\boxed{
R_j(U)=\frac{16^j}{8}U^{j-1}(U-1)^{2j-2}
(U+1)^{18-4j}(U^2-6U+1),\quad 1\le j\le4.
}
\tag{7}
$$
即 $g_j(2z)=\sigma^{68}yR_j(U)$。这是倍点公式
$$
x(2z)=\frac{(U+1)^2}{4x(U-1)},\quad
y(2z)=\frac{y(U+1)(U^2-6U+1)}{8U(U-1)^2},\quad
\vartheta(2z)=\sigma^4(U+1)
$$
的直接代入。四个 $R_j$ 的次数依次为 $16,15,14,13$，故独立。

两个实际投影矩阵也可完全有理地写出。对 $0\le j\le16$，
$$
\Pi_i(U^j)=\frac14\left[
U^j+U^{16-j}-2^{-16}D_{32,j}(U)\right],
\tag{8}
$$
其中 $D_{n,j}(x^2)=(x-1)^{n-2j}(x+1)^{2j}+(x+1)^{n-2j}(x-1)^{2j}$。
对正偶块 $0\le j\le17$ 则为
$$
\Pi_e(U^j)=\frac14\left[
U^j+U^{17-j}+2^{-17}D_{34,j}(U)\right].
\tag{9}
$$
它们是原二挠点 $0,(0,0),(1,0),(-1,0)$ 的真实归一迹，分别秩四和五；特别
$\Pi_eP_A=P_A,\ \Pi_eP_B=0,\ \Pi_eC_\beta=C_\beta$。

## 3. $\mathcal V K_H$ 的准确相位和全部四个系数

令 $M_i$ 为 R283 twisted 奇十七维块的原 $\pi_5=2+i$ 五次迹矩阵，$N_i=M_i/(2+i)$。在 (6) 未倍点的旧四维基中，同一真实五次迹准确为
$$
M_o=\frac1{64}
\begin{pmatrix}
51-52i&7-14i&-1-8i&43-26i\\
259-238i&75+80i&23+54i&-153-84i\\
-259-72i&-31+2i&-95-100i&-51+62i\\
157-94i&-19-12i&-7+14i&-31+72i
\end{pmatrix}.
\tag{10}
$$
置 $S=-iM_o/(2+i)$。精确矩阵乘法给
$$
\boxed{S^4=iI_4.}
\tag{11}
$$
这里的符号由实际矩阵确定。几何的 $G(iz)=iG(z)$ 在有限 Fourier 坐标中用逆向作用；不能把正偶块的相位直接搬到本奇块。准确投影是
$$
\boxed{\Pi_v=\frac14\sum_{a=0}^3(-iN_i^4)^a,}
\tag{12}
$$
即选取 $N_i^4=+i$ 的四维子空间。

给出 (10) 的精确来源。用 R248 原范数五多项式
$$
Q_\pi=U-(1-2i),\quad K_\pi=(2+i)U-i
$$
及其共轭，置
$$
P_\pi=\frac{Q_\pi^2}{\pi_5}
\{Q_\pi K_\pi+4U(Q_\pi'K_\pi-Q_\pi K_\pi')\}.
$$
在实际纤维 $f_a=UQ_\pi^4-aK_\pi^4$ 上令
$$
U_b=UQ_{\bar\pi}^4/K_{\bar\pi}^4,\qquad
\mathfrak m=
(Q_{\bar\pi}/Q_\pi)^{16}(P_{\bar\pi}/P_\pi)
(K_\pi/K_{\bar\pi})^3.
$$
第 $j$ 列的归一值就是 $\operatorname{Tr}_{f_a}(\mathfrak m U_b^{-j})$。
对首一 $f_a$，此迹等于 $[(U^4)]((\mathfrak m U_b^{-j})f_a'\bmod f_a)$。
四个固定纤维 $a=2,3,4,5$ 唯一确定 (10)，第五个 $a=6$ 逐列验证。所有分母在这些商环中均实际可逆。

完整 $17$ 因子保持不动，R246 的有限 dyadic 算子给
$$
M_i\mathcal U=-i\mathcal U M_o,
\qquad N_i\mathcal U=\mathcal U S.
\tag{13}
$$
这里 $g_{\pi_5}=-g_*^{-1}$，它在旧 dyadic 线和新 dyadic 线上的相对因子为 $-i$；未将原 raw $\pi_5$ 换成 primary $i\pi_5$。共同标量已由 R246 两个实际 CM17 参考定标。

还须固定 $\mathcal U$ 本身的标量。令 $r$ 读 twisted 多项式的 $U^{16}$ 系数。R246 同一个真实四分点展开给
$$
\boxed{r\mathcal U=\frac i{32}(-13,5,3,-11).}
\tag{14}
$$
具体地，在 $-T=-(1-i)\Omega_0/4$ 有 $x=i,y=-1+i$，归一 theta 的对数导数为 $(1+i)/2$。因此
$$
\left.\partial_w\{\widehat\vartheta(w-T)^{17}
y(w-T)x(w-T)^{-2j}\}\right|_{w=0}
=(-1)^j(8j-21).
$$
R246 的四移位和在原 $i$ 权上一阶系数为该值的 $i/16$ 倍，而 $K(2z)$ 的一阶系数为 $-2[U^{16}]P$，正给 (14)。这同时保留了尺度和四移位相位。

(13)、(14) 的四行观测矩阵 $((r\mathcal U)S^k)_{0\le k<4}$ 行列式非零。把它用于 $rN_i^k\Pi_vP_H^G$，唯一求得
$$
\boxed{\mathcal VK_H(2z)=F_H(2z),\qquad
F_H(z)=\sum_{j=1}^4 h_jg_j(2z),}
\tag{15}
$$
其中
$$
\boxed{
\frac1i(h_1,h_2,h_3,h_4)=
\left(
\frac{3611281457093}{68911032277401600},
\frac{2813582085593}{482377225941811200},
-\frac{1080089631219271}{482377225941811200},
\frac{158865506722691}{482377225941811200}
\right).
}
\tag{16}
$$
这是整条原函数的像，不只是投影连接或几个未付出的低阶 jets。

## 4. 原 $A/B$ 两条 $Q_{0,+}$ 像的准确构造

置 $\kappa_4=2^{-1/4}$，使用 R229 的 degree-four 原坐标
$$
T=\sigma^4(U+1),\quad F=\sigma^4(U-1),\quad
G=2x\sigma^4,\quad H_4=2y\sigma^4,
$$
满足 $T^2=F^2+G^2,H_4^2=2FG$。原归一 $M,N$ 分别将这些坐标送到
$$
M:(\kappa_4(F+G),\ \kappa_4^3(T+H_4),\
\kappa_4^3(T-H_4),\ -\kappa_4(F-G)),
$$
$$
N:(\kappa_4(F-G),\ \kappa_4^3(T-iH_4),\
-\kappa_4^3(T+iH_4),\ -i\kappa_4(F+G)).
\tag{17}
$$
本篇准确使用
$$
Q_{0,+}=-\frac18\{(1+M^2)(N+N^3)+(M+M^3)(1-N^2)\}.
\tag{18}
$$
作用于多项式时，$M^kN^j$ 对应的坐标代换矩阵是 $N^jM^k$；次序没有省略。

若 $K=\sigma^{68}y\sum_{j=0}^{16}p_jU^j$，其完整齐次表示为
$$
\boxed{K=\frac{H_4}{2^{17}}
\sum_{j=0}^{16}p_j(T+F)^j(T-F)^{16-j}.}
\tag{19}
$$
将 R283 的 $P_A^G,P_B^G$ 逐项代入 (17)–(19)，得
$$
\boxed{\kappa_4Q_{0,+}K_A=F_A,\qquad
\kappa_4Q_{0,+}K_B=F_B,\qquad
F_i=\sum_{j=1}^4q_{ji}g_j(2z).}
\tag{20}
$$
全部 $q_{ji}\in\mathbb Q(i)$ 由本篇 JSON 的
`Q_A_B.results.*.kappa_times_Q0plus_old_coefficients` 给出；(17)–(19) 是它们不依赖拟合的固定生成式。

证书在精确环 $\mathbb Q[\kappa_4,i,y]/(\kappa_4^4-1/2,i^2+1,y^2-x^3+x)$ 中计算全部八项。取固定 $x=2,4,5,6$ 确定四列系数，在另一固定纤维 $x=7$ 核验；输出的偶 $y$ 部分全部为零，唯一剩下的 $\kappa_4$ 因子准确为 $\kappa_4^{-1}$。由于 (18) 的像是 (6)，且四个求值点的 (7) 矩阵可逆，这证明完整恒等式 (20)。

三个四维向量 $(q_A,q_B,h)$ 独立。其前三行的 $3\times3$ 子式准确为
$$
-\frac{247672964913094482304598144434228758223624567}
{6206678152570006457519580841711747431435384284774400000}
\;-
\frac{2030434832239479440168103003949640251257746224049}
{31778192141158433062500253909564146848949167538044928000000}i,
\tag{21}
$$
显然非零。

## 5. 完整未投影项恰为一个线性乘子

**定理 1。** 对每个 $F=\sigma^{68}yP\in\mathcal O_i$，有
$$
\boxed{(1-\Pi_0)LF=-\sigma^{68}(20U-54)P.}
\tag{22}
$$
更具体地
$$
\Pi_0L\Pi_0=\partial_z-34\zeta(2z),\qquad
\mathcal W-34\zeta(2z)=\frac{20U-54}{y}.
\tag{23}
$$

**证明。** 在真实四个二挠平移的 frame 中，导数同时微分自动因子的线性指数。计入这些项后，连接的平均在每个二挠点具有留数 $17$，其准周期是 $68\zeta$ 的准周期。故它与 $34\zeta(2z)$ 之差是常数；$i$ 协变使该常数为零。也可直接用 (8)、(9)、(5) 逐列核验第一式，不需要省去任何指数。

准确的 zeta 倍点式为
$$
\zeta(2z)=2\zeta(z)+\frac{3U-1}{2y}.
$$
由 $y^2/x=U-1$，
$$
\mathcal W-34\zeta(2z)
=\frac{71(U-1)-17(3U-1)}y
=\frac{20U-54}y.
$$
乘回 $F$ 即得 (22)。证书还独立验证四个 $R_j$ 上的完整矩阵等式
$(1-\Pi_e)\mathscr L R_j=-(20U-54)R_j$。$\square$

因此两侧未投影项有确切的非零来源，不是一个可以通过选择平均连接消去的常数。

R231/R246 的原源身份分别给
$$
\kappa_4Q_{0,+}E_A=0,\quad
\kappa_4Q_{0,+}E_B=-R_{289}/320,\quad
\mathcal VS_H(2z)=\frac{8i}{11}S_A(2z),
\tag{24}
$$
其中
$$
R_{289}=\vartheta(2z)^{17}P_2(v(2z)),\qquad
P_2(s)=1-18s^2+16s^3+s^4.
$$
前两式包括 $Q_{0,+}C_\beta=0$，但 (20) 中的 CM 补偿并未随之删除。

定义三条完整交换差
$$
\boxed{
D_A=-LF_A,\qquad
D_B=-R_{289}/320-LF_B,\qquad
D_H=\frac{8i}{11}S_A-LF_H.
}
\tag{25}
$$
在共同 degree-$272$ 尺度，这些式子准确是原算子作用于 (3)，减去 $\tfrac12L_2$ 作用于完整输出。由 (22)，三列都满足
$$
(1-\Pi_0)D_i=\sigma^{68}(20U-54)P_{F_i}.
\tag{26}
$$
这里连 $D_H$ 的 off-block 也保留了；只计算 $\Pi_0L\Pi_0$ 不会得到 (25)。

## 6. 实际三列不能联合闭回原源及 CM

**定理 2。** 在原固定函数空间中
$$
\dim\operatorname{span}\{S_A,S_B,C_\beta,C_{\bar\beta},D_A,D_B,D_H\}=7.
\tag{27}
$$
特别地，$D_H$ 单独加入前四列就使秩由四升到五。

**证明。** 前四列独立，后三列的 off-block 由 (21)、(26) 独立。原 $S_A,C_\beta,C_{\bar\beta}$ 在 $\Pi_0$ 的像中，$S_B$ 在其核中。若存在 (27) 的关系，则应用 $1-\Pi_0$ 后为
$$
(20U-54)(aP_{F_A}+bP_{F_B}+cP_{F_H})=dP_B(U).
$$
原 $P_B$ 的直接代入准确给
$$
\boxed{P_B(27/10)=
\frac{893895064914654570906099}{10000000000000000}\ne0.}
\tag{28}
$$
故 $d=0$，再由 (21) 得 $a=b=c=0$。剩余原四列的独立性完成证明。$\square$

这个证明还说明：整个旧 odd 四维块的 off-block 像与原 $S_B$ 方向无非零交，而不仅是本次三条选定向量偶然独立。

对于单条 $D_H$，列序取 $(P_A,P_B,C_\beta,C_{\bar\beta},D_H/\sigma^{68})$，行序取 $U^1,U^2,U^0,U^3,U^4$，子式准确为
$$
-\frac{4887764700845806333422577}{122674872320000}\ne0.
\tag{28a}
$$

对真正的两个奇 CM 参考
$$
G_u(z)=\sigma(z)^4y(z),\qquad G_{u,\beta}=G_u(\beta z),\quad
G_{u,\bar\beta}=G_u(\bar\beta z),
$$
准确还得到
$$
\boxed{
\dim\operatorname{span}
\{K_A,K_B,G_{u,\beta},G_{u,\bar\beta},F_A,F_B,F_H\}=7.
}
\tag{29}
$$
这次比较也使用真正的两个 CM 多项式，没有用一个任意水平原函数替代 CM 参考。证书给出 (29) 在 $U^0,\ldots,U^6$ 七行上的非零 Gaussian 行列式。它另外给出 $F_H$ 单独加入前四列的 $5\times5$ 非零子式，所以原 $\mathcal VK_H$ 的两个“秩五”结论各有独立的精确证书。

具体地，后一子式使用 $U^0,\ldots,U^4$ 行、列序 $(P_A^G,P_B^G,P_{G_{u,\beta}},P_{G_{u,\bar\beta}},P_{F_H})$，准确为
$$
-\frac{3529459705680705646725371446437026815966919075408607912343}
{5339636617491867534603434038861017833033603481600000}
-\frac{68589218273487735224516005492834357157436395410399801}
{3792355552195928646735393493509245620052275200000}i.
\tag{29a}
$$

## 7. 完整中央恒等式与质量

以下只在 R263/R283 的普通好素数、实际有界测度和同一 $\Omega_0$ 下取 Mellin；不将这些测度式自动搬到惰性规范。置
$$
\mathscr J_f(u)=\frac{M_f(u)}{J_\vartheta(u)},\qquad
\Lambda(F;u)=\frac{M_{F'}(u)-M_{\mathcal WF}(u)}{J_\vartheta(u)}.
\tag{30}
$$
所有 $F_i$ 为实际正 theta 奇来源，$F_i'$ 是 R284 已付出的 tame-one 观察；$\mathcal WF_i=F_i'-LF_i$ 因而使用同一个有界测度差，未把裸 $\zeta$ 单独当作有界测度。

(25) 的完整、全权转置准确是
$$
\boxed{
\begin{aligned}
\mathscr J_{D_A}(u)&=-\Lambda(F_A;u),\\
\mathscr J_{D_B}(u)&=-\mathscr J_{R_{289}}(u)/320-\Lambda(F_B;u),\\
\mathscr J_{D_H}(u)&=\frac{8i}{11}\mathscr J_{S_A}(u)-\Lambda(F_H;u).
\end{aligned}}
\tag{31}
$$
这是原来源的恒等式，不声称 $Q_{0,+}$ 或 $\mathcal V$ 保持某一条原单位 Mellin 行。

若 $m_f=M_f(0)$，(31) 的质量分别为
$$
m_{D_A}=-m_{F_A'}+m_{\mathcal WF_A},\quad
m_{D_B}=-m_{R_{289}}/320-m_{F_B'}+m_{\mathcal WF_B},\quad
m_{D_H}=-m_{F_H'}+m_{\mathcal WF_H}.
\tag{32}
$$
最后一式用了原 $m_{S_A}=0$。没有把奇原函数的 principal Mellin 恒零误当作其导数的质量零。原 CM 边界的质量仍是 $m_{C_\beta}=m_\vartheta\ne0$，并已通过 (4) 进入 (20)。

同一参考下，从 native 到共同 $[2]$ 的准确尺度式是
$$
\mathscr J_{f(2\cdot)}(u)=(2^d)^u\mathscr J_f(u),\qquad
\mathscr J_{f(2\cdot)}'(0)=\mathscr J_f'(0)+d\log_p2\,\mathscr J_f(0),
\quad d=p-1.
\tag{33}
$$
因此若在共同尺度求 (31) 的中央导数，(32) 必须一起转置。若连参考也换成 $J_{\vartheta(2\cdot)}$，两个已显示的相同尺度因子才会消去。

原三条完整中央零仍只给 R283 的原两条非齐次 $\Lambda(K_A),\Lambda(K_B)$ 及 $\Lambda(K_H)$ 观察。它们没有把 (27) 的三个新来源置零；原 $S_B$ 的中央零也没有使 $\mathscr J_{R_{289}}'$ 自动为零。(27)–(29) 精确定位了这一实际 norm-two 尝试留下的三条新观察，不能由“有限块同构”或“整个角带已归一”省去。

## 8. 可复算证书

- [check-original-dyadic-primitive-transfer.py](../scripts/check-original-dyadic-primitive-transfer.py)
- [check-original-dyadic-primitive-transfer.json](../scripts/check-original-dyadic-primitive-transfer.json)

脚本从已发表 R277/R283 原系数出发，重新计算 (10) 的五个固定纤维、(12) 的准确四维投影、(14) 的观测矩阵、全部 $\mathcal VK_H$ 和 $Q_{0,+}K_{A/B}$ 系数，并输出 (25) 的全部十八行。它验证完整未投影乘子 (22)，给出 (27)、(29) 及两个单条秩五结论的非零子式。没有在这些计算中把中央零转成算子轨道上逐列零，也没有删除原 CM 边界或移动 theta frame。
