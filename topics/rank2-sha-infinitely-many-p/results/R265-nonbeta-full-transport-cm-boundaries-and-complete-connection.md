# R265 — 非 beta 载体的全十七维整运输、真实 CM 极补偿与完整连接

日期：2026-11-13。**状态：两个实际非拉回十七维运输、所有惰性 $p>19$ 的整逆、协变二阶导数的全部边界极、两条真实 CM 补偿，以及运输前后的完整 Mellin 连接式均已证明。有限来源的整逆没有被当作原三曲线中央泛函的闭合。**

本文接续 [R262](R262-nonbeta-normtwo-constants-and-original-octic-basis.md) 的
$G_h=F(\beta z)/(x(z)(x(z)^2-1)^h)$，将九条来源扩到正权和相邻权的
两个完整十七维空间。与 R259 的纯拉回算子不同，实际乘子保留原 $z$ 中的
有理函数。全文使用 R248/R259 已支付的同一 CM 线丛同构、正有限平坦迹和 Gaussian 规范。

## 1. 两个真正全纯的非拉回来源空间

固定
$$
E_0:y^2=x^3-x,\qquad dz=\frac{dx}{2y},\qquad U=x^2,
\qquad \beta=4-i,\quad\bar\beta=4+i,
$$
$$
S=-y\vartheta\sigma^3,\qquad F=S^{17},\qquad
W=-y\vartheta\sigma^{67},\qquad D=U^8(U-1)^8,\qquad F=WD.
\tag{1}
$$
原 degree-$68$ 的两个空间是
$$
\mathcal H_+=W\mathbb Q(i)[U]_{\le16},\qquad
\mathcal H_-=\frac Wx\mathbb Q(i)[U]_{\le16}.
\tag{2}
$$
定义乘子及实际运输
$$
\mu(z)=\frac{F(\beta z)}{F(z)},\qquad
\boxed{\mathcal T_\pm C=[\bar\beta]_*(\mu C),\quad C\in\mathcal H_\pm.}
\tag{3}
$$
这里的乘法先在原 theta 截面上进行；没有对 Mellin 变换使用乘法性。
更具体地，两个输入分别为
$$
F(\beta z)\frac{P(U)}{D(U)},\qquad
F(\beta z)\frac{P(U)}{xD(U)}.
\tag{4}
$$
它们的真实全纯性可逐点检查。$F(\beta z)$ 在 $T_0=(0,0)$ 有三十四阶零，
在 $T_\pm=(\pm1,0)$ 有十七阶零。$D$ 在这些点的零阶分别为三十二、十六。
所以 (4) 在 $T_0$ 的最低余下零阶分别为二、零，在 $T_\pm$ 均至少为一。
原点处 $P/D$ 无极，$1/x$ 从 $z^2$ 起；其他点不出现新极。
因此 (4) 是实际 degree-$1156$ 全纯来源，保留原 $T_0$ twist。

正有限平坦迹降回 degree $68$，并与全局 $i$ 作用相容。
两个目标准确为 (2)，故存在唯一的 $17\times17$ Gaussian 有理矩阵 $T_\pm$ 使
$$
\mathcal T_+(WP)=W(T_+P),\qquad
\mathcal T_-\left(\frac WxP\right)=\frac Wx(T_-P).
\tag{5}
$$
此处矩阵作用于升幂系数列。源的全纯性和目标维数先于任何插值计算，
因而 (5) 不是截断无限空间后得到的拟合。

## 2. 全纤维计算及所有惰性素数上的整逆

取以下十七个实际有理载体：
$$
r_j=U^{-j}\quad(0\le j\le8),\qquad
r_{8+h}=(U-1)^{-h}\quad(1\le h\le8).
\tag{6}
$$
$Dr_j$ 组成 $\mathbb Z[U]_{\le16}$ 的一个整基，基变换行列式为 $\pm1$。
令 $P_\beta,P_{\bar\beta},Q_{\bar\beta},K_{\bar\beta}$ 是 R248 的原 CM 多项式，
其中 $S(\beta z)=WP_\beta(U)$，另一个方向同理。
对目标坐标 $t$，令
$$
f_t(U)=UQ_{\bar\beta}(U)^4-tK_{\bar\beta}(U)^4.
$$
它是首一的十七次完整纤维多项式。由同一原 frame 得
$$
\boxed{\begin{aligned}
(T_+(Dr))(t)
 &=D(t)\operatorname{Tr}_{f_t=0}
 \left[\left(\frac{P_\beta}{P_{\bar\beta}}\right)^{17}r(U)\right],\\
(T_-(Dr))(t)
 &=D(t)\operatorname{Tr}_{f_t=0}
 \left[\left(\frac{P_\beta}{P_{\bar\beta}}\right)^{17}
       \frac{Q_{\bar\beta}^2}{K_{\bar\beta}^2}r(U)\right].
\end{aligned}}
\tag{7}
$$
第二行的额外因子准确为 $x(\bar\beta z)/x(z)$；不多出 $U$。
式 (7) 对 (6) 给出全部三十四条完整来源。
证书在 $t=2,\ldots,18$ 的十七个精确纤维恢复目标多项式，并在 $t=19$
逐列核对另一个完整纤维。纤维内 trace 用首一多项式恒等式
$$
\operatorname{Tr}_{f_t=0}a(U)
=[U^{16}]\bigl(a(U)f_t'(U)\bmod f_t(U)\bigr)
$$
计算，所有除法均在 $\mathbb Q(i)[U]/(f_t)$ 中准确完成。

全部 $578$ 个矩阵系数和两个准确行列式保存在随文 JSON。关键整性数据是

| 实际运输 | 秩 | 矩阵全部系数分母的最小公倍数 | 行列式实、虚部的整数 gcd |
|---|---:|---:|---:|
| $T_+$ | 17 | $2^{29}$ | $2^7$ |
| $T_-$ | 17 | $2^{30}$ | $2^4$ |

两个行列式本身都是非零 Gaussian 整数。
若 $p\equiv3\pmod4$，Gaussian 整数被 $p$ 整除当且仅当其实部、虚部都被 $p$ 整除。
因此表中准确 gcd 直接证明
$$
\boxed{T_\pm\in\operatorname{GL}_{17}(\mathcal O_p)
\quad\text{对每个奇惰性素数 }p,}
\tag{8}
$$
其中 $\mathcal O_p=\mathbb Z_p[i]$。
后续原 Mellin 论证仍按既有规范使用 $p>19$。

这一步区别于 $[\bar\beta]_*[\beta]^*$：后者在每个固定 $i$ 型中的像至多一维，
而 (3) 的两个实际原坐标矩阵均为十七维整同构。

R262 的原八次子矩阵也可加强到相同的整范围。其 $4\times9$ 矩阵全部系数
仅有分母 $2^{33}$；前四列行列式写成公分母 $2^{94}$ 后，Gaussian 分子的
实、虚部 gcd 准确为 $17$。由于 $17$ 分裂，R262 的前四个原 $G_h$
对所有惰性 $p>19$ 都给出原四八次伴随的整基。
这没有把原四个对数常数 $C_k$ 误当作 $p$ 进单位。

## 3. 协变二阶导数的两个真实边界极

置
$$
\nabla_F=\partial_z-F'/F,\qquad C_P=\frac WxP(U).
$$
因为 $C_P=F\cdot P/(xD)$，准确有 $\nabla_F^2C_P=F(P/(xD))''$。
使用 $\partial_z x=2y$、$y^2=x^3-x$，完全约分得
$$
\boxed{\nabla_F^2C_P=W\mathcal D(P),}
\tag{9}
$$
$$
\mathcal D(P)=16U(U-1)P''-(508U-260)P'
 +\left(4290-\frac{1190}{U}+\frac{1088}{U-1}\right)P.
\tag{10}
$$
式 (10) 中的撇号表示 $U$ 导数。定义真正的多项式部分
$$
\begin{aligned}
K_2(P)={}&16U(U-1)P''-(508U-260)P'+4290P\\
&-1190\frac{P-P(0)}U+1088\frac{P-P(1)}{U-1}.
\end{aligned}
\tag{11}
$$
于是完整式为
$$
\boxed{\nabla_F^2C_P
=WK_2(P)-1190P(0)\frac WU+1088P(1)\frac W{U-1}.}
\tag{12}
$$
$W/U$ 在 $T_0$ 确有二阶极；$W/(U-1)$ 在 $T_\pm$ 确有一阶极。
两者支撑不同，所以不能互相抵消。由此得到准确的全纯定义域
$$
\boxed{\nabla_F^2C_P\text{ 全局全纯}
\iff P(0)=P(1)=0
\iff P=U(U-1)R,\quad\deg R\le14.}
\tag{13}
$$
这正是 R245 的原十五维 companion 空间。
代入 (10) 后得到原 $\mathscr L R$，不是一个新的截断代替。

最高载体的极也可直接从完整导数梯级检查。令
$u_h=1/(x(U-1)^h)$、$v_h=(U-1)^{-h}$，则
$$
u_h''=\left(2(4h+1)(2h+1)-\frac6U\right)v_h
       +8h(2h+1)v_{h+1},
\tag{14}
$$
$$
v_h''=4h\bigl((4h-1)u_{h-1}+(8h+1)u_h+(4h+2)u_{h+1}\bigr),
\quad h\ge1,
\tag{15}
$$
$$
(x^{-m})''=2m\bigl((2m-1)x^{1-m}-(2m+1)x^{-m-1}\bigr).
\tag{16}
$$
特别 $h=8$ 的下一极层确实存在；它不能因为原载体列表止于八就被删除。

作为 (11) 的独立有限核对，其在 $U^j$ 上的对角元是
$(4j-65)(4j-66)$，$0\le j\le16$。该多项式部分若要单独求逆，
大于十九的惰性坏素数恰为 $23,31$。
这与 (8) 的整逆条件是不同陈述；本文不靠删除 (12) 的极项来调用这个逆。

## 4. 两条真实 CM 来源准确补足全部边界

取实际相邻 CM 截面
$$
\Gamma_\beta(z)=\frac{S(\beta z)}{x(\beta z)}=\frac WxG_\beta(U),\qquad
\Gamma_{\bar\beta}(z)=\frac{S(\bar\beta z)}{x(\bar\beta z)}=\frac WxG_{\bar\beta}(U).
\tag{17}
$$
其原多项式是 $G_\beta=-U^{16}P_\beta(1/U)$，共轭方向同理。
这与 R259/R264 的 $D_\beta K_\beta^2$ 规范完全一致。
两个真实边界值为
$$
\boxed{
\begin{pmatrix}G_\beta(0)&G_{\bar\beta}(0)\\G_\beta(1)&G_{\bar\beta}(1)\end{pmatrix}
=\begin{pmatrix}-1&-1\\-65536-262144i&-65536+262144i\end{pmatrix},
\qquad\det=-2^{19}i.}
\tag{18}
$$
所以对任意 $P$，唯一的两个固定代数系数 $c_\beta(P),c_{\bar\beta}(P)$ 满足
$$
c_\beta+c_{\bar\beta}=-P(0),\qquad
c_{\bar\beta}-c_\beta=\frac{P(1)-65536P(0)}{262144i}.
\tag{19}
$$
定义
$$
\mathcal R P=P-c_\beta(P)G_\beta-c_{\bar\beta}(P)G_{\bar\beta}.
$$
则 $\mathcal R^2=\mathcal R$，像为 (13) 的十五维空间，并有整的完整源分解
$$
\boxed{C_P=C_{\mathcal RP}+c_\beta(P)\Gamma_\beta
 +c_{\bar\beta}(P)\Gamma_{\bar\beta}.}
\tag{20}
$$
这里对每个奇惰性 $p$ 都不添新分母。

求导后必须保留 (20) 的全部三项：
$$
\boxed{\nabla_F^2C_P=WK_2(\mathcal RP)
 +c_\beta(P)\nabla_F^2\Gamma_\beta
 +c_{\bar\beta}(P)\nabla_F^2\Gamma_{\bar\beta}.}
\tag{21}
$$
后两项包含 (12) 的实际极，分别在原点仍为正则 germ。
它们的原质量是 $2\beta^2$、$2\bar\beta^2$，因为
$\Gamma_\beta=\beta^2z^2+O(z^6)$。
这些项不能在中央导数中凭“CM 参考”四字删除，也不能把它们的
协变导数与已知尺度对数混为一条泛函。

## 5. 真实运输后的完整有限连接差

令 $E$ 是将 $R\in\mathbb Q(i)[U]_{\le14}$ 送到 $P=U(U-1)R$ 的
$17\times15$ 矩阵，令 $L=K_2E$。
两条 CM 边界行记为 $C=(c_\beta,c_{\bar\beta})^t$，并置 $r=1/\bar\beta$。
定义准确的有限矩阵
$$
\boxed{\Delta=K_2\mathcal R T_-E-r^2T_+L,\qquad
 B_{\rm CM}=CT_-E.}
\tag{22}
$$
全部系数由 (7)、(11)、(18) 唯一确定，随文证书逐项给出。
对任意原正则 companion $C_{ER}$，记 $P'=T_-ER$，则
$$
\boxed{\begin{aligned}
\nabla_F^2\mathcal T_-C_{ER}
 -r^2\mathcal T_+(\nabla_F^2C_{ER})
={}&W\Delta R\\
 &+(B_{\rm CM}R)_\beta\nabla_F^2\Gamma_\beta
 +(B_{\rm CM}R)_{\bar\beta}\nabla_F^2\Gamma_{\bar\beta}.
\end{aligned}}
\tag{23}
$$
这已将全部边界极保留为两个实际 CM 项，其余差为真正全纯的原正权来源。
证书还在十九维“十七个多项式坐标 + 两个实际极坐标”内核对 (23)，
没有只比较全纯投影。

式 (23) 的全十九坐标交换差秩为十五；补偿后 $\Delta$ 的秩也为十五。
因而在原十五维正则输入中，没有非零输入能使这个完整交换差消失。
它的解析含义可按全部实际分支直接给出。
把 $[\bar\beta]_*$ 写成原十七分支之和 $\sum_\nu T_\nu$，每条分支覆盖
$z\mapsto rz+t_\nu$，并含原 Mumford/Gaussian 乘子。取
$$
f(z)=F(\beta z),\qquad Q=\mu C_{ER},\qquad
a_\nu=\partial_z\log\frac{T_\nu f}{F}.
$$
乘法本身有精确的 frame 相容性
$\nabla_f^j(\mu C)=\mu\nabla_F^jC$，但 trace 的连接必须另外保留。
链式法则给
$$
\boxed{\nabla_F^2T_\nu Q
=r^2T_\nu\nabla_f^2Q
 +2r a_\nu T_\nu\nabla_fQ
 +(a_\nu^2+a_\nu')T_\nu Q.}
\tag{24}
$$
因此 (23) 的整个右端准确等于
$$
\boxed{\sum_\nu\left(2r a_\nu T_\nu\nabla_fQ
 +(a_\nu^2+a_\nu')T_\nu Q\right).}
\tag{25}
$$
(22) 给出 (25) 在实际有限来源中的全部坐标，(24) 则保留其原几何来源。
它们是同一连接差的两种精确表达。

## 6. 与 R264 原 norm-two 连接的整拼合

R264 的实际算子是
$$
\mathscr K h=h''+\frac{68yx}{U-1}h'+\frac{1088x}{U-1}h,
$$
$$
F\mathscr K(P/D)=4\frac WxM(P),\qquad
M(P)=4U^2(U-1)P''+U(61-55U)P'-(80U+264)P.
\tag{26}
$$
令 $\ell$ 为该原矩阵的准确余核，
$$
\gamma=\ell(G_\beta)=5479905460224-3786459611136i.
$$
R264 已证 $\gamma$ 对所有惰性 $p>19$ 为单位。
因而对每个 $P\in\mathcal O_p[U]_{\le16}$，有唯一
$A_P\in\mathcal O_p[U]_{\le15}$ 使
$$
\boxed{T_-P=M(A_P)+\frac{\ell(T_-P)}\gamma G_\beta.}
\tag{27}
$$
本篇保存完整的 $17\times17$ 反解矩阵：前十六行给 $A_P$，最后一行给
$\ell(T_-P)/\gamma$；准确回乘核对全部 $289$ 个系数。
换回原来源，得到
$$
\boxed{\mathcal T_-C_P
=\frac14F\mathscr K(A_P/D)
 +\frac{\ell(T_-P)}\gamma\Gamma_\beta.}
\tag{28}
$$
$WA_P$ 的原质量准确为零，外面的 $1/4$ 来自原算子规范。
(28) 把整个非拉回十七维像接到真实 norm-two 连接和一条已知 CM 来源，
而 (23)–(25) 明确保留与其并行的二阶交换差。

一个有用的有限范围核对是：R248 的五条正权来源
$P_\beta,P_{\bar\beta},P_H,P_2,P_3$ 经 $M$ 的像仍维五；它与
“R254 四条相邻八次来源加 $G_\beta$”的五维空间交集为零。
准确的 $17\times10$ 拼接矩阵在 $\mathbb Q(\zeta_8)$ 上秩为十。
所以 (28) 中的整原像不能未经计算就缩回这五条已知正权来源。
这只是这两个明确有限池的事实，不排除更大的实际连接图。

## 7. 全部移权、质量、尺度和完整 Mellin 转置

固定惰性 $p>19$，置 $d=p+1,c=68c_0$。
对任一上述相邻 companion $C$，定义
$$
W_F=zF'/F,\qquad W_0=W_F-dcz^d,\qquad \mathcal E=z\partial_z,
$$
$$
f_C(u)=\mathcal J_c(C/z^2;u),\qquad
g_C(u)=\mathcal J_c(W_0C/z^2;u),
$$
$$
h_C(u)=\mathcal J_c((W_0^2+\mathcal EW_0-W_0)C/z^2;u).
$$
沿用原完整 Newton 变换，记
$$
\boxed{\begin{aligned}
\mathfrak D_c(C;u)={}&(du+1)(du+2)f_C(u)
 +du(d-3-2du)f_C(u-1)\\
&+d^2u(u-1)f_C(u-2)-2(du+1)g_C(u)
 +2dug_C(u-1)+h_C(u).
\end{aligned}}
\tag{29}
$$
R245/R251 的完整 Euler 转置给
$\mathfrak D_c(C;u)=\mathcal J_c(\nabla_F^2C;u)$。
因此 (23) 的全体 $u$ 形式是
$$
\boxed{\begin{aligned}
\mathfrak D_c(C_{T_-ER};u)
 -r^2\mathcal J_c(WT_+LR;u)
={}&\mathcal J_c(W\Delta R;u)\\
&+(B_{\rm CM}R)_\beta\mathfrak D_c(\Gamma_\beta;u)\\
&+(B_{\rm CM}R)_{\bar\beta}\mathfrak D_c(\Gamma_{\bar\beta};u).
\end{aligned}}
\tag{30}
$$
右端也准确等于把 (25) 的全部两种连接项送入 $\mathcal J_c$ 的结果。
这保留了 $W_0$、$\mathcal EW_0$、$u-1$、$u-2$ 及完整尾。
特别中央导数不是只取 $f_C'(0)$；准确有
$$
\begin{aligned}
\mathfrak D_c'(C;0)={}&2f_C'(0)+3df_C(0)
 +d(d-3)f_C(-1)-d^2f_C(-2)\\
&-2g_C'(0)-2dg_C(0)+2dg_C(-1)+h_C'(0).
\end{aligned}
\tag{31}
$$
其中 $f_{\Gamma_\beta}(0)=\beta^2$，共轭方向同理。

(28) 也可直接作用于全变换：
$$
\boxed{\mathcal J_c(C_{T_-P};u)
=\frac14\mathcal J_c(F\mathscr K(A_P/D);u)
 +\frac{\ell(T_-P)}\gamma\mathcal J_c(\Gamma_\beta;u).}
\tag{32}
$$
本式的 $\mathscr K$ 仍是 (26) 的整个三项算子；它没有与 Mellin 泛函交换。

若将 (24) 的分支缩放移到输入端，原 degree-$1156$ gauge 是 $17c$。
写 $T_\nu Q(z)=e_\nu(z)Q(rz+t_\nu)$，则准确的尺度单位为
$$
\boxed{\mathcal J_c(T_\nu Q;u)
=U_{\bar\beta,p}^{-u}\,
\mathcal J_{17c}\bigl(e_\nu(\bar\beta z)Q(z+t_\nu);u\bigr),
\qquad U_{\bar\beta,p}=\frac{\bar\beta^{p+1}}{17}.}
\tag{33}
$$
所有 Gaussian 和平移项仍在括号内。
求中央导数时保留 $-\log_pU_{\bar\beta,p}$ 乘对应质量。
共同 $[2]$ 后，gauge 变为 $4c$，全函数另外乘 $q_2^u$，
$q_2=2^{p-1}$；并且
$\nabla_{F(2z)}^2C(2z)=4(\nabla_F^2C)(2z)$。
所以两条 CM 导数的质量和所有 $\log_pq_2$ 项仍然按 (21)、(31) 保留。

全部这些输入在原正式盘内正则。固定二挠和十七挠极支撑在该盘之外，
固定次有理乘子、导数以及原 Mumford 平移的 Gauss 成本按 R245/R254 保持；
从而 (29)–(33) 使用完整收敛的 Newton 尾，没有用有限截断替换中央值。

## 8. 已支付的有限图与尚未推出的中央闭合

本篇完成了三个具体环节：(3) 的真正非拉回来源给出两个全十七维整运输；
(18)–(25) 把最高载体的实际极和非零连接差完整支付；(27)–(33) 将其接到
原 norm-two 算子、真实 CM 参考及全体 Mellin 移权。

这提供的是一张有明确整矩阵和完整解析转置的原来源图。
原三条 rank-$2$ 曲线的中央零目前没有被证明在这整张图下封闭。
尤其不能由 (8) 或 (28) 反推所有十七个输入中央行为零，
也不能删除 (30) 的 CM 导数、(25) 的连接差或 (31) 的移权值。
R268 的 de Rham/Cartier 检测可以作用于这里实际的 $M$ 余核，
其与原 theta frame 及中央 Mellin 行的相容性仍须在同一图内另行支付。

## 精确证书

- [脚本](../scripts/check-nonbeta-full-transport-and-cm-boundary.py) 和
  [完整输出](../scripts/check-nonbeta-full-transport-and-cm-boundary.json)
  的 $202$ 项精确检查全部通过。输出保存两个完整矩阵、原极坐标、CM 正则化、
  全部有限连接差，以及 R264 的整反解。
- 原全纤维公式和相位来自 R248/R259；R262 给原八次接口；
  R245/R251 给原协变来源与完整 Mellin；R264 给原 norm-two 连接及余核补偿。
- 所有矩阵计算在固定精确数域中完成；无目标素数数值筛选。
