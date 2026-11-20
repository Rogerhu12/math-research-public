# R928 — 原固定 P 的实际长行右端、二次逆 Taylor 与全局兼容类

日期：2026-11-20。**状态：以下符号命题已证明，root全文核且theta独立审阅通过。**未作数学数值执行，未证明显示的固定类非零，未声称主目标完成。

本注接 R920 附 A，固定同一个原整矩阵和原源格。**三条长行延到 s 的精度原理不是新定理**：它是 R808 的 m13 精度引理在 R821 四块上的同一逐行读取，R828 的三 carry 注已经支付其整公式。这里新增的内容是把该输入写成固定原 P 的统一实际右端，再把负 fringe 中不能删除的二次逆 Taylor 项带入原全局兼容类；另外给出这些选定行的同来源充要判据。没有把只知道差在 K′ 中，误当成已知道仿射偏移。

## 1. 固定原对象及记号

令 p=6s−1>211，仍删除 R821 已列的有限坏集，固定同一原

$$
M=M_{\rm act}:\mathscr L_D\longrightarrow
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3),
\qquad 1\le\ell<s-13.
\tag{1}
$$

源端保完整 P134、c_*U0、公共 charge 四十及十九角。固定一个实际整源向量 $P_{\rm src}$，以后简称 P；修正 R、S 仍在原格中。曲线上指定光滑点另记 $P_C=(0,1)$，不与源向量 P 混淆。

使用 R828 一标量注的同一个参考 $g_{\Theta,\circ}$、实际

$$
h_\Theta=H_p w^{s-4}B(w),\qquad
g=g_{\Theta,\circ}e^{h_\Theta}.
\tag{2}
$$

这里 H_p、B、Gaussian 单位 a 都是实际整量，不另选高轴或 Teichmüller 数字。对原列 $\Phi$，令 $Q_\Phi$ 为包含公共四十的全部 charge，参考系数为 $A_\Phi^\circ$。定义

$$
W_i^\circ(Y)=\sum_\Phi Y_\Phi Q_\Phi^i A_\Phi^\circ,
\qquad
W_i^{\rm act}(Y)=
\sum_\Phi Y_\Phi Q_\Phi^i A_\Phi^\circ e^{Q_\Phi h_\Theta}.
\tag{3}
$$

所有除 p 的地方只用原有限窗口内已经支付的整性。特别不是把未正规化的全 sigma Taylor 级数约化到 k[[w]]。以下 $k=\mathcal O/p$，$\mathscr S$ 表示真实系数移位

$$
(\mathscr S A)(w)=\sum_{n\ge0}[w^{s+n}]A\,w^n.
\tag{4}
$$

## 2. H·B 低项恰好恢复实际高轴，不能提前删除

R828 三 carry 注的原整向量为

$$
\mathcal K_{j,d}(Y)_v=
\frac{a^{j-d}}{(j-d)!}
\sum_{m=0}^d\frac{H_p^m}{m!}
[w^{(d-m)s+v+4m-13}]B^mW_{j-d+m}^\circ(Y),
\quad 1\le d\le j\le3,\quad0\le v\le12.
\tag{5}
$$

在相同整窗口中，直接合并 (2)–(3) 得

$$
\boxed{
\mathcal K_{j,d}(Y)_v
=\frac{a^{j-d}}{(j-d)!}
[w^{ds-13+v}]W_{j-d}^{\rm act}(Y).
}
\tag{6}
$$

证明：指数展开的第 m 项恰为 (5) 的第 m 项。m>d 时，其首阶至少 $(d+1)(s-4)>ds-1$，因为 s>35、d≤3；所有原相对列在 w=0 整，因而没有负次数把该项拉回。显示的分母只涉及 m≤3。故 (6) 是原窗口中的整恒等式。

尤其 d=1 时

$$
\boxed{
\frac{a^{j-1}}{(j-1)!}
\left([w^{s-13+v}]W_{j-1}^\circ(Y)
+H_p[w^{v-9}]BW_j^\circ(Y)\right)
=\frac{a^{j-1}}{(j-1)!}
[w^{s-13+v}]W_{j-1}^{\rm act}(Y).
}
\tag{7}
$$

这对任意原 Y 成立，不先要求 Y 属于首核或 K′。在 R920 的零差空间中，H·B 低项因已付消失而为零；对一般固定仿射右端，正确操作是按 (7) 合并，不是令它为零。

## 3. 固定 P 的四个实际右端

先检验原必要整性门

$$
\boxed{
[W_i^{\rm act}(P)]_{<s}\in p\mathcal O[w]\quad(i=0,1,2),
\qquad
[W_3^{\rm act}(P)]_{<\ell}\in p\mathcal O[w].
}
\tag{8}
$$

若存在任何 $M(P+pR)\in p^2\Gamma$，(8) 必成立。确实，模 p 的全部 normal 行先给前三个 <s−13 前缀和第四个 <ell 前缀；最前十三 carry 行给 $\mathcal K_{j,1}(P)\in p\mathcal O^{13}$，再由 (6) 恰补前三个末十三项。这也正是原 m13 的单位/一次 p 行权引理。

在 (8) 成立后，定义三个长 s、一个短 ell 的固定多项式

$$
\boxed{
\mathcal F_i^P
=-\overline{\left[
\frac{W_i^{\rm act}(P)}p+
\frac{i}{a}\mathscr S W_{i-1}^{\rm act}(P)
\right]_{<d_i}},
\qquad
d_0=d_1=d_2=s,\quad d_3=\ell.
}
\tag{9}
$$

i=0 时第二项定义为零。第一项只表示在 <d_i 的已经被 p 整除的有限前缀中取商，不声称整个 W_i 可被 p 除。第二项保同一个原 P 的完整实际移位系数；最高只用到本节已经支付的有限窗口。a 的全部整规范保持。

**命题 1（选定原行的精确仿射等价）。** 在 (8) 下，对任意原整 R、S，下列两项等价：

1. $M(P+pR)\in p^2\Gamma$，且 $M(P+pR+p^2S)$ 的三条最前十三行全部属于 $p^3\mathcal O$。
2. 同一个 $\bar R$ 满足

$$
\boxed{
[W_i^{\rm act}(R)]_{<d_i}\bmod p=\mathcal F_i^P,
\qquad i=0,1,2,3.
}
\tag{10}
$$

特别，完整 $M(P+pR+p^2S)\in p^3\Gamma$ 必给 (10)，而 (10) 的右端完全不含 S。

**证明。** 对 normal 行 $[\epsilon^iw^{13+n}]$，原实际四块的完整折回给

$$
[\epsilon^iw^{13+n}]M(Y)
=\sum_{d=0}^{i}p^d\frac{a^{i-d}}{(i-d)!}
[w^{ds+n}]W_{i-d}^{\rm act}(Y).
\tag{11}
$$

前三块取 $0\le n<s-13$，第四块取 $0\le n<\ell$。代入 Y=P+pR，先保所有项，再除以 p、模 p：d≥2 的项现在才消失。以 $i!a^{-i}$ 乘回，得到 (9)–(10) 在这些 normal 行上的部分。

前三条带的完整原式为

$$
[\epsilon^jw^v]M(Y)
=\sum_{d=1}^jp^d\mathcal K_{j,d}(Y)_v\pmod{p^4}.
\tag{12}
$$

由 (8)，$\mathcal K_{j,1}(P)$ 已可除 p。p³ 所需的下一位准确是

$$
\frac{\mathcal K_{j,1}(P)}p+
\mathcal K_{j,1}(R)+\mathcal K_{j,2}(P)=0\pmod p.
\tag{13}
$$

S 项前面是 p³，不进入 (13)。令 i=j−1，使用 (6)，并以 $i!a^{-i}$ 乘回，(13) 正是 (9)–(10) 的 $s-13\le n<s$ 部分；j=1 时 $\mathcal K_{1,2}=0$。反向按相同步骤恢复所有 normal 行与三条带。第零块最前十三行对全原源恒为零。没有漏掉原 p² 的其它行，也没有将尚需 p³ 的 normal 行认成已解决。证毕。

与 R828 三 carry 注的记账完全一致：

$$
U_{j,P}=\mathcal K_{j,1}(P)/p+\mathcal K_{j,2}(P)
$$

正是 (9) 的后三段右端。这里新增的是其整个 actual 前缀的统一形式，绝非把 U_{j,P} 或原除 p 商赋为零。

## 4. 返回原 r=2 的 H3 陪集，先检实际低行再作单位逆

现在加入 R920 的原几何及预算；C仍为同一原整Cartier曲线，允许既有奇点：

$$
C=(F=0),\quad P_C=(0,1),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad\kappa=C^2,
$$

$$
\mathcal E=Y\partial_Y,\quad e=\mathcal EF,\quad e(P_C)\ne0,
\quad r=2,\quad
\jmath(G)=q_{\rm src}t^rG\in\bar{\mathscr L}_D,\quad G\in\mathcal H_3.
\tag{14}
$$

该返回及全部十九角已付；不将 H3 扩成矩形多项式格。固定一个真实剩余源陪集

$$
\bar R_b+\jmath(\mathcal H_3).
\tag{15}
$$

R_b 是这个给定陪集的任一原整代表，不要求先找到一个 p³ 解。

原实际读取为

$$
W_i^{\rm act}(\jmath G)
=\mathcal U(w)t(w)^r
[(\mathcal E+40)^i(q_{\rm src}G)](t(w),g(w)),
\quad\mathcal U=c_*U_0^{\rm act}\in k[[w]]^\times.
\tag{16}
$$

先从 (9) 减去 R_b 的完整实际前缀，换到同一个 t 参数，并乘 $\mathcal U^{-1}$。**四个所得前缀都必须被真实 t^r 整除**；任一低行失败便排除该陪集，不得先除去公共 t^r。

通过后再除 t^r，记四个确定目标为 z_i。前三个长度

$$
J=s-r=T+13,\quad T=s-r-13;
$$

第四个长度为原 $L=\ell-r$。R920 范围有 L>0。令

$$
q_j(t)=[(\mathcal E+40)^jq_{\rm src}](t,g(t)),\quad q_0(0)\ne0.
$$

同一个原下三角单位逆给

$$
\begin{aligned}
f_0&=z_0/q_0,\\
f_1&=(z_1-q_1f_0)/q_0,\\
f_2&=(z_2-2q_1f_1-q_2f_0)/q_0,\\
f_3&=(z_3-3q_1f_2-3q_2f_1-q_3f_0)/q_0.
\end{aligned}
\tag{17}
$$

前三式模 t^J，末式模 t^L。于是 (10) 在 (15) 内准确等价于

$$
\boxed{
(\mathcal E^iG)(t,g)=f_i\pmod{t^J}\quad(i=0,1,2),
\qquad
(\mathcal E^3G)(t,g)=f_3\pmod{t^L}.
}
\tag{18}
$$

f_i 现在由原 P、给定陪集和原实际有限级数确定；没有新选择的 R/S。式 (16)–(17) 保 q 的全部 Euler 项及 P134/U0，不把原 charge 四十删掉。

## 5. 负 fringe 的二次逆 Taylor：仿射项不能按零差空间删掉

保持 R920 的

$$
g=\psi e^\eta,\quad\operatorname{ord}_t\eta=h,\quad
h<T\le2h,\quad T-h>\kappa,\quad T-h\le L\le h,
$$

$$
-13\le2h-J<0.
\tag{19}
$$

原 r=2、C.f0=3、b≥5 的已付界给 h>13，故

$$
2h<J\le2h+13<3h,\qquad
2h+L\ge h+T=J+h-13>J.
\tag{20}
$$

这里 η 只表示所需有限阶的 Euler Taylor 坐标；模 t^J 可用 $\log(1+u)=u-u^2/2$ 及其逆，不使用正特征中的无限对数。

置 $V_0=G|_C$、$V_1=(\mathcal EG)|_C$。完整有限逆 Taylor 给

$$
\boxed{
j_0^P=f_0-\eta f_1+\frac{\eta^2}{2}f_2\pmod{t^J},
\qquad
j_1^P=f_1-\eta f_2+\frac{\eta^2}{2}f_3\pmod{t^J}.
}
\tag{21}
$$

任何 (18) 的原 G 必满足 $[V_0]_{<J}=j_0^P$、$[V_1]_{<J}=j_1^P$。第二式的短 f3 足够，因为 2h+L>J；不需要把原第四短行延长。η³ 的所有余项由 3h>J 消失。

在 R920 的齐次差上 f0=f1=f2=0，且 η²f3 高于 J；所以 (21) 返回其两个 VJ 零前缀。但在当前固定仿射右端中，η²f2 和 η²f3 是实际已读项，不能从齐次情形借用消失。

始终使用实际 g 到 J。没有在 s−4 之后以 rho=(1+8t)Theta^17 替换它；R920 的 ODE 比较仍只到 min(J,s−4)。

## 6. 不必先选择一个解的固定全局兼容类

令

$$
V=H^0(C,N^3),\quad Z=(e|_C),\quad
\mathscr Z=H^0(Z,N^3|_Z),\quad
\mathscr J_J=N^3|_{JP_C}.
$$

使用 R836 已付的实际 k-线性算子

$$
D_3:V\longrightarrow\mathscr Z,\qquad
D_3(V_0)=(\mathcal EG_0)|_Z,\quad G_0|_C=V_0.
\tag{22}
$$

改变 G0 的真实全局提升只加 F H2，故该式良定义。定义完整有限映射

$$
\mathcal T_J:V^2\longrightarrow\mathscr J_J^2\oplus\mathscr Z,
\quad
(V_0,V_1)\longmapsto
([V_0]_{<J},[V_1]_{<J},D_3V_0-V_1|_Z).
\tag{23}
$$

则由原 P 直接给出的类为

$$
\boxed{
\mathfrak c(P;\bar R_b+\jmath\mathcal H_3)
=[(j_0^P,j_1^P,0)]\in\operatorname{coker}\mathcal T_J.
}
\tag{24}
$$

它是原有限全局 k-线性兼容类；没有把含 Euler 导数的 (22) 冒称 O_C-线性映射。

**命题 2。** (24) 是任何同陪集完整 p³ 解的必要障碍；它为零，当且仅当存在同一真正全局兼容对

$$
[V_0]_{<J}=j_0^P,\quad[V_1]_{<J}=j_1^P,\quad
D_3V_0=V_1|_Z.
\tag{25}
$$

它与 (15) 内基点 R_b 的选择无关。因此 (24) 不是先选到一个解之后才能描述的差空间。

**证明。** 必要性由 (18)–(22)。等价是原完整映射 (23) 的实际像定义。若换基点 $\bar R_b\mapsto\bar R_b+\jmath G_b$，(17) 中 f_i 减去同一个 $(\mathcal E^iG_b)(t,g)$。由完整 (21)，j0、j1 相应减去 $G_b|_C$、$(\mathcal EG_b)|_C$ 的前缀。后二者本来兼容，故代表只减去 $\mathcal T_J(G_b|_C,(\mathcal EG_b)|_C)$，类不变。证毕。

还有同一整源的字面重记账检查：若只把 P 写为 P+pY，同时把 R_b 写为 R_b−Y，(9) 的目标减去 $W_i^{act}(Y)$，从 R_b 减去的项同步改变，相对目标不变。这是同一个实际 P+pR 的坐标重写，不授权改变 P134 或原来源。

任何 $(\lambda_0,\lambda_1,\nu)\in(\mathscr J_J^\vee)^2\oplus\mathscr Z^\vee$ 若满足

$$
\operatorname{ev}_J^\vee\lambda_0+D_3^\vee\nu=0,\qquad
\operatorname{ev}_J^\vee\lambda_1-\operatorname{res}_Z^\vee\nu=0,
\tag{26}
$$

就对 (24) 读取确定标量

$$
\lambda_0(j_0^P)+\lambda_1(j_1^P).
\tag{27}
$$

(24) 为零当且仅当全部真实 (26) 的 (27) 为零。这里没有把任意有限局部向量当作全局左行，也没有预先赋这个固定标量非零。

全部 V、Z 和配对均在原可能奇异的 Cartier 曲线及十九角上，保非约化结构、剩余域迹和 conductor；不换成去边界的仿射环境。

## 7. 固定类之后仍用同一 H1：选定行的完整充要判据

仅有 (24)=0 还不充分。以下给出 (18) 的完整判据，避免把两个全局值代替全部四行。

对任意一个 (25) 的兼容对，R836 给真实 $G_0\in\mathcal H_3$ 同时实现 $G_0|_C=V_0$、$(\mathcal EG_0)|_C=V_1$；所有实现恰为 $G_0+F^2\mathcal H_1$。定义原完整有限像

$$
\mathcal N_{J,L}:\mathcal H_1\longrightarrow
k[[t]]/(t^J)\oplus k[[t]]/(t^L),
$$

$$
L_1\longmapsto
\bigl((\mathcal E^2(F^2L_1))(t,g),
(\mathcal E^3(F^2L_1))(t,g)\bigr).
\tag{28}
$$

该映射单射：其第一分量截到旧 T 后就是 R836 的
$c_F\mathcal E_{3\eta,T}$，已在同一个原 H1 上证明单射。这里在新 J>T 中直接保完整 (28)，不把旧模 t^T 的镜轴公式免费延长到 t^J。

**命题 3。** (18) 可解，当且仅当存在同一个 (25) 的兼容对，使

$$
\boxed{
\bigl(f_2-(\mathcal E^2G_0)(t,g),
f_3-(\mathcal E^3G_0)(t,g)\bigr)
\in\operatorname{im}\mathcal N_{J,L}.
}
\tag{29}
$$

一旦兼容对固定，(29) 的 L1 唯一。判据与 G0 的选择无关。

**证明。** 必要性是同源差恰为 F²H1。反向取唯一 L1，置 G=G0+F²L1。它保持 V0、V1，且第二、第三 Euler 行已由 (29) 达到 f2、f3。令 $d_i=(\mathcal E^iG)(t,g)-f_i$。实际 (21) 给

$$
d_0-\eta d_1+\eta^2d_2/2=0\pmod{t^J},
\qquad d_1-\eta d_2+\eta^2d_3/2=0\pmod{t^J}.
$$

已有 d2∈t^J、d3∈t^L，且 2h+L>J，故第二式先给 d1∈t^J，第一式再给 d0∈t^J。全部四行 (18) 成立。换 G0 只平移同一个 (28) 的实际像，不改变 (29)。证毕。

因此 (24) 与 (29) 完整判定命题1的**选定行**在原返回陪集中的成员性。它们使用固定 P 的真实非齐次数据，不从维数大小判断成员性。

## 8. 受限 S 与完整首 Bockstein 的剩余边界

对已经通过命题1的同一个实际整 R，完整二次商

$$
y_{P,R}=-\overline{M(P+pR)/p^2}\in\bar\Gamma
\tag{30}
$$

存在。若 S 的真正允许范围为一个已指定仿射格 $S_b+\mathscr S$，则完整 p³ 条件的准确最后一步仍是

$$
\boxed{y_{P,R}-\bar M\bar S_b\in\bar M(\overline{\mathscr S}).}
\tag{31}
$$

没有给出具体受限格时，不擅自添一个“normal 自由空间”。R 的整 lift 若改为 R+pY，则 (30) 同时改变 −\bar M\bar Y；受限 S 未必允许相应补偿。因此 (24) 或 (29) 通过均不推出 (31) 可解。

只有两组真正完整 p³ 解之差，R920 附 A 才给 $\Delta\bar R\in\ker\beta_1$；且仅在 $\Delta\bar R\in\jmath\mathcal H_3$ 时得到 $\jmath K'$。命题1选定行的齐次核一般更大，不能直接拿它代替 K′，也不能把 R920 的三／四来源短链结论套给一个尚未通过 (31) 的差。

若原指定 GRes 的 R842 联合延拓系统在长度 J 上实际可解，(21) 可直接代入其既有留数式，给

$$
\mathfrak G_F(\jmath G)
=-\operatorname{Res}_{P_C}
\frac{j_0^P\omega_0+j_1^P\omega_1}{e^2}.
\tag{32}
$$

这时右端确为同一固定 P 的 affine 值；原 R_b 的已知项另按线性加回。但本注没有解那个实际联合延拓系统，也没有由 (32) 删除其它边界留数。

待判的新具体量是 (24) 的实际值，继而是同一个兼容对的 (29) 以及同一个整 R 的 (31)。没有新增算术中央零，没有从四中央零构造首核，全部原 p4 native、末端四次 carry、固定导子与后续同 R/S 条件保持。

### 依赖

- R808 §1：原 m13 精度引理；本注不重复登记它。
- R821 §§4、8 及 R828 一标量注 §§1、3：同一个实际轴、完整 charge 和四块整窗口。
- R828 三 carry 注 §§1、2、5：原三条十三行及同 P/R/S 的全部整商。
- R836 §§2–6：真实 D3、两个全局值的 F²H1 挠集、旧 T 镜轴单射及四行返回。
- R840、R842：原 2Z/前缀兼容与有限全局对偶，所有十九角及 conductor。
- R920 §§1–3、附 A：负 fringe 的真实长度、二次逆 Taylor 和完整 p³ 差空间的精确范围。


### 原文件入口及审阅范围

- [R920](R920-original-first-bockstein-kernel-and-short-euler-chains.md)及附A保完整首Bockstein、真实差空间与相同P/R/S范围。
- [R828三carry原注](../notes/2026-11-16-r828-three-native-carry-recursions-and-last-block-tails.md)保(5)的所有真实H·B项及全部39条前带；(6)/(9)由这些整式逐项重写，不另造条件。
- [R836](R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)§2–6保D3、同源两值、F²H1及旧T镜轴；本篇新J窗直接使用(28)，不扩大旧镜轴适用范围。

root亲读本篇全部正文，另逐项回查原三carry注、R920和R836。normal与carry的i/a系数、二次逆Taylor、同陪集基点不变以及受限S的最后整像门均已复核。新增的是固定原P的准确非齐次输入与兼容类；这些量的实际非零值仍须研究，不能以本篇抽象判据宣布它们已非零。
