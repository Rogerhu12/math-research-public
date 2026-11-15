# R752 — 原同门的模 p 两来源闭包与准确点惯性抽取

日期：2026-11-15。**状态：下述来源级闭包、有限角色及规范 trace 结论已证明。**

R747 恢复了原 $e_0$ 与原 Y 轴。本篇进一步使用这些门的实际方向：
所有深度可达125的门都与 Y 正交；只有 Y/W/V 的一层单位或非单位门产生 Y 方向的 p 挠平移。
因此第一 Y 来源只需 **degree $34p$** 的共同覆盖。
高深度仍留在伙伴的实际代数系数中，不被删除。

固定 R742 的一个17角色 $\tau_k$，$k=2,4$ 后，每条真实来源恰能写成
原 $D_{k,17}$ 与第二 dyadic 来源 $P_{+,k,17}$ 各乘一个**模 p 的物理函数**。
这是实际 Mumford 平移给出的恒等式，不把一般 p-Weil 向量猜成一变量测试。
前者函数角型为0，后者为4。
primitive 支更强：去掉 Y-unit 后，整条来源就是一个代数常数乘 $D_{k,17}$。

最后，以完整 étale theta 平均读取一个明确系数，再接 R748/R751/R749 的点公式。
它与自然 Galois trace 不同，也不把已知中央零自动传给新测试。

## 1. 原来源、全部门与周期

使用 R747 的同一固定 p：
$$
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=\pi_0/\bar\pi_0=p\lambda^2,\qquad
\Omega=\Omega_p,\qquad b=17 .
\tag{1}
$$
所有正矩按原 $\Omega$ 和 b 齐次归一；$p$、$\lambda$、$\kappa$ 在本篇固定。

保原六输入、原 C 平均及三个 A 伙伴，记
$$
Y=A+c+2d,\quad W=A+3\delta c+4d,\quad
Z=W-b_YY,\quad V=36Y-\alpha W,
$$
$$
b_Y=(20+3\omega)/17,\quad \alpha=17-3\omega,\quad
E=(5+6\omega)A-29c-(58+87\omega)d .
\tag{2}
$$
实际权为 R742 的
$$
\Phi_\infty=\sum_{a=0}^{30}E^a\phi_{a,\infty}.
\tag{3}
$$
每个 $E^a\phi_{a,\infty}$ 的每个混次块都来自原六次中性权及其
$G^6,B_0^6$ 扩展；其总次数属于 $6\mathbf Z_{\ge0}$，不超过30。
线性换元、原完整两个 C 支和取 $u=0$ 均保这项齐次性。
所以这不是仅在 $\sum_a$ 后才成立的角型结论。

令
$$
B_i=b_iZ+e_iE,\quad
\Delta_\ell=1_{B_1\in p^\ell}-1_{B_3\in p^\ell},\qquad
\begin{array}{c|cc}
i&b_i&e_i\\ \hline
1&-(170+117\omega)/526&-(4+9\omega)/263\\
3&(170+291\omega)/526&(2-3\omega)/263 .
\end{array}
\tag{4}
$$
原四门为
$$
\begin{aligned}
m_P&=1_{\{Y,Z,E\ {\rm unit}\}}\Delta_\ell,\\
m_G&=m_P1_{\{W,V\ {\rm unit}\}},\\
m_W&=m_P1_{\{W\in p\}},\\
m_V&=m_P1_{\{V\in p\}}.
\end{aligned}
\tag{5}
$$
其逐点关系仍是 $m_P=m_G+m_W+m_V$。
本篇不在 (5) 上增删任何门。

令
$$
\mu_k=\mathcal P_{\tau_k}^Y e_0,\qquad
\tau_2(g_0)=-\omega^2,\quad\tau_4(g_0)=-\omega ,
$$
并定义四条实际第一 Y 测度
$$
\nu_{k,j,a,\ell}
=\Omega^{-1}Y_*
 \bigl(ZE^a\phi_{a,\infty}m_j\,\mu_k\bigr),
\qquad j=P,G,W,V .
\tag{6}
$$
(6) 是 R747 已付的原来源，不是另行指定的边际。
准确有
$$
\Omega I_{-1}(\nu_{k,P,a,\ell})=p_{\tau_k,a}(\ell),\quad
\Omega I_{-1}(\nu_{k,G,a,\ell})=g_{\tau_k,a}(\ell),
$$
$$
\Omega I_{-1}(\nu_{k,W,a,\ell})=\lambda h_{\tau_k,a}^W(\ell),\qquad
\Omega I_{-1}(\nu_{k,V,a,\ell})=\gamma\lambda h_{\tau_k,a}^V(\ell).
\tag{7}
$$
两个外部 core 标量均保留。

## 2. 深伙伴门不产生第一 Y torsion

原生成嵌入为
$$
\iota_Y(z)=y^t z,\qquad
y=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2),\qquad N(y)=34 .
\tag{8}
$$
对物理行 L，Fourier 角色产生的生成平移沿 $L^t$，其 Y 坐标准确为
$$
\boxed{\frac{\langle L,y\rangle}{34}\,t.}
\tag{9}
$$
这是生成变量的双线性转置与 Hermitian 正交分解的合成；
不是把生成列换成 $\bar L^t$。

取 R745 的 Y 与五伙伴加法 isogeny。
其度数与本篇 p 互素，故在每个 $\mathfrak p^\ell$-torsion 上为同构。
因此 (9) 中的零系数表示**唯一 p-primary 提升的 Y 坐标严格为零**。
不存在一个需要再补上的 prime-to-p gluing 点。

原 $Z,E,B_1,B_3$ 及 $C^\perp$、其余三个权伙伴均与 Y 正交。
所以：

1. $\Delta_\ell$、Z/E-unit 和原 C 门的任意深度 Fourier 展开只平移伙伴；
2. Y-unit 只产生 $E[\mathfrak p]$ 的 Y 平移；
3. W/V 的浅门也只产生 $E[\mathfrak p]$ 的 Y 平移，其系数为
   $b_Y$ 与 $263/17$，因为
   $W=b_YY+Z$、$V=(263/17)Y-\alpha Z$。

所有固定分母在 p 处均可唯一求逆。
相加、取交或取差不增加这些 Y 平移的阶数。

于是 R747 的第一因子池可准确收紧为
$$
\boxed{
\mathscr T_{34,1}
=\sum_{t\in E_{17}[\mathfrak p]}
 H^0(E_{17},t_t^*\mathcal L_{34}),
\qquad \mathcal L_{34}=\mathcal O(34[0]).
}
\tag{10}
$$
而不是在第一 Y 因子上用 $\mathfrak p^{125}$。
伙伴仍保其全部 $\mathfrak p^\ell$-torsion 和全 Mumford 配对；
这些项进入实际代数系数，不能换成质量。

R747 的共同覆盖因此只需
$$
[\bar\pi_0]^*\mathscr T_{34,1}
\subset H^0(E_{17},\mathcal O(34p[0])).
\tag{11}
$$
若用 (11) 计算原负一值，真实倍率为
$$
I_{-1}([\bar\pi_0]_*\nu)=\bar\pi_0^{-1}I_{-1}(\nu).
\tag{12}
$$
$\bar\pi_0$ 是所选 p 处的单位。(12) 不能省成一个未指定常数。

这里无需把实际来源扩大到任意径向 p-Weil 向量。
(6) 本来支撑 Y-unit；一层 Fourier 平移及 (12) 已给全部所需模型。
若另用更大的 Schrödinger 空间，须另付其与 (10) 的 intertwiner，
不能以一般径向分解替换本篇的实际来源。

## 3. 固定17角色下的完整二维坏处空间

本节给 (10) 的完整第一因子范围，不从“总 type5”直接丢掉另一个 dyadic 向量。

R735 的标准 degree34 Fourier 模型由周期68的序列 $a_n$ 给出，
准确半特征关系为
$$
(-1)^n a_{n+34}=-a_n .
\tag{13}
$$
以 $n\bmod4$ 和 $3n\bmod17$ 作 CRT 坐标。
对每个17坐标，(13) 迫二处的四个数为
$$
(A,B,-A,B).
\tag{14}
$$
因此整个34维空间准确是
$$
\operatorname{span}(f_A,f_B)\otimes\mathbf C^{17},\qquad
f_A=e_0-e_2,\quad f_B=e_1+e_3 .
\tag{15}
$$
这也是 R735 使用的真实半特征模型，不另换一个 flat twist。

R735 的17环面完整投影证明 $\tau_2,\tau_4$ 各单重，
由其非零奇向量 $f_k$ 张成。
故该17投影后的完整空间恰为
$$
\mathcal H_k=\operatorname{span}(f_A,f_B)\otimes f_k,
\qquad \dim\mathcal H_k=2 .
\tag{16}
$$
二处原矩阵为
$$
M_\omega^{\rm old}
=\frac{\omega^2}{\sqrt2}
 \begin{pmatrix}-\zeta_8&i\\ i&i\zeta_8\end{pmatrix}.
\tag{17}
$$
其两个特征向量及特征值为
$$
t_\pm=\frac{1\pm\sqrt3}{\sqrt2},\qquad
M_\omega^{\rm old}(1,t_-)^t=\omega(1,t_-)^t,\quad
M_\omega^{\rm old}(1,t_+)^t=(1,t_+)^t.
\tag{18}
$$
第二式也由 $\operatorname{tr}M_\omega^{\rm old}=-\omega^2$、
第一式及 $\omega+\omega^2=-1$ 直接给出。

几何 $\mu_3$ 的原标签是 $\omega^2$；
17因子有 $\tau_k(g_0^{12})=1$。
二处两向量均偶，17向量奇。因此两条整 theta 线分别为 type5、type3。
它们的完整来源记为
$$
D_{k,17},\qquad P_{+,k,17}.
\tag{19}
$$
第一条正是 R732/R735 首项 $z^5$ 系数1的原来源。
第二条采用 R751 的规范：
首非零项 $z^{r_k}$ 的系数为1，
$$
r_k\in\{3,9,15,21,27\}.
$$
不存在首阶已被默认等于3的断言。
其非零性来自 (14) 的非零 Fourier 序列；
其代数规范来自原 rigidified theta 空间的代数结构。

这给完整直和
$$
\boxed{\mathcal H_k
=\overline{\mathbf Q}D_{k,17}
 \oplus\overline{\mathbf Q}P_{+,k,17}.}
\tag{20}
$$
(20) 的有限向量、相位和整 line bundle 同时保留。
这里只用 R751 的来源规范；该篇的进一步算术角色在第8节使用。

## 4. 实际伙伴正矩没有增加 Y 的无穷权

原 Y 与 B 正交分裂为
$$
s^*\mathcal L=\mathcal L_{34}\boxtimes\mathcal L_B .
\tag{21}
$$
其 Hermitian Gaussian 的交叉项为零。
每条 Z、E 及另外三个权方向的正矩都沿 B 微分；
它们只作用第二因子的有限 jet。
所以在任何固定 torsion 项上，收缩后仍是
$H^0(t_t^*\mathcal L_{34})$ 中的截面，没有额外的 Y 导数。

原 finite p 门、C 平均和17投影全部保留后，仍可逐项如此处理。
R745 已付每个 jet 的代数性以及
$\Omega^{-d}$ 与 d 次物理矩的准确抵消。
因此本篇的展开系数均为代数数；没有把一个一般条件 p-adic 积分当作代数系数。

将 R742 的 $u=0$ 权临时换回 $u$ 邻域内同一个实际有理权时，
固定 p、$\ell$ 后所有门和 torsion 点均固定。
可以选同一个有限 theta 基；
每个展开系数都是某个固定数域中的 $u$ 有理函数，并在 $u=0$ 正则。
这是按有限坐标取极限的依据，不是给任意无限 logarithm 和赋代数性。

## 5. 从真实 Mumford 平移到模 p 物理函数

固定原 formal CM 参数和一个原始 p 次根 $\zeta_p$。
按原 ordinary 型将
$$
t_s\in E[\mathfrak p],\quad s\in\mathbf F_p
$$
与 formal 乘法平移 $\zeta_p^s$ 对应。
设 $\mathsf T_s$ 为带完整 BK 配对的 canonical Mumford 平移。
R745 的原形式恒等式给
$$
\boxed{
\nu_{\mathsf T_sF}(x)=\zeta_p^{sx}\nu_F(x).
}
\tag{22}
$$
若某个代数 theta 基使用不同的 torsion 代表，
其原 root-of-unity 因子必须同时放进展开系数；
(22) 指已经完成该规范比较的算子。
这里没有使用 $\log\zeta_p=0$。

由 R742 的真实17交换及 (10)、(20)，每个 (6) 都有代数展开
$$
\nu_{k,j,a,\ell}
=\sum_{s\in\mathbf F_p} c_{j,-,s}\,\zeta_p^{sx}\nu_{D_k}
 +\sum_{s\in\mathbf F_p} c_{j,+,s}\,\zeta_p^{sx}\nu_{P_{+,k}} .
\tag{23}
$$
省略的下标 $k,a,\ell$ 在系数中全部保留。
等价地，定义实际模 p 函数
$$
\Phi_{j,\pm}(x)=\sum_{s\in\mathbf F_p}c_{j,\pm,s}\zeta_p^{sx},
$$
得到来源级主式
$$
\boxed{
\nu_{k,j,a,\ell}
=\Phi_{j,-}(x)\nu_{D_{k,17}}(x)
 +\Phi_{j,+}(x)\nu_{P_{+,k,17}}(x).
}
\tag{24}
$$
高深度伙伴与原 q 的所有系数都在 $c_{j,\pm,s}$ 中；
(24) 没有将它们替换为一个边际质量。

### 5.1 唯一性及全 unit 支撑

(23) 的 $2p$ 个原向量线性独立。
证明可在 (11) 的共同覆盖上直接给出。

令 $\mathcal L'=[\bar\pi_0]^*\mathcal L_{34}$，度数为 $34p$。
原 $[\bar\pi_0]^*\mathcal H_k$ 在
$\ker[\bar\pi_0]=E[\bar{\mathfrak p}]$ 的自然下降 lift 下逐点固定。
各 $\mathsf T_s$ 在覆盖上变成相应
$E[\mathfrak p]$ 平移。两个 p 阶子群之间的 theta 交换配对完美：
其限制是原 $e_p$ 的一个 $34$ 次单位幂。

所以不同 s 的向量属于不同的 $E[\bar{\mathfrak p}]$ 特征空间。
同一个 s 内两向量由 (20) 独立。
这证明全部 $2p$ 个向量独立，也证明 (23) 的系数唯一。
整个论证使用奇数阶子群的原对称 lift；
R747 的唯一 splitting 说明其没有遗漏中心标量。

由于 (6) 支撑 Y-unit，乘 $1_{x\in p}$ 后为零。
但模 p 函数在该陪集上为常数，故
$$
0=\Phi_{j,-}(0)\,1_{x\in p}\nu_{D_k}
  +\Phi_{j,+}(0)\,1_{x\in p}\nu_{P_{+,k}} .
$$
用
$1_{x\in p}\nu_F=p^{-1}\sum_s\zeta_p^{sx}\nu_F$
和刚证明的独立性，得到
$$
\boxed{\Phi_{j,-}(0)=\Phi_{j,+}(0)=0.}
\tag{25}
$$
这里未使用一个尚未证明的 $P_+$ whole p-core。

### 5.2 每条原来源的完整角型

原六 sigma 的共同 $\mu_6$ 型为0；
C 平均、所有齐次零陪集门及17投影都与该共同作用相容。
第1节的逐 a 齐次性与分子 Z 给
$$
[\zeta]_*\nu_{k,j,a,\ell}=\zeta^5\nu_{k,j,a,\ell},
\qquad \zeta\in\mu_6 .
\tag{26}
$$
由 (20)、(22) 及唯一性，
$$
\boxed{
\Phi_{j,-}(\zeta x)=\Phi_{j,-}(x),\qquad
\Phi_{j,+}(\zeta x)=\zeta^4\Phi_{j,+}(x).
}
\tag{27}
$$
也可把 (23) 先按 (26) 平均得到同式。
因此 type3 基线并未消失；它乘角4的真实有限函数后恰成为总 type5。
不能仅凭 (26) 删除第二项。

## 6. primitive 支整条回到原 Dk

定义去掉 Y-unit 的真实来源
$$
\widetilde\nu_{k,P,a,\ell}
=\Omega^{-1}Y_*
 \left(ZE^a\phi_{a,\infty}
 1_{\{Z,E\ {\rm unit}\}}\Delta_\ell\,\mu_k\right).
\tag{28}
$$
其全部门与权都在 Y 的正交伙伴上。
第2节因而给：第一 Y 因子没有 p 挠平移，整条来源属于裸 $\mathcal H_k$。
同一齐次性又使它为 type5。
由 (20) 准确有
$$
\boxed{
\widetilde\nu_{k,P,a,\ell}
=C_{k,a,\ell}\,\nu_{D_{k,17}},
\qquad
\nu_{k,P,a,\ell}
=C_{k,a,\ell}\,1_{x\ {\rm unit}}\nu_{D_{k,17}},
}
\tag{29}
$$
其中 $C_{k,a,\ell}\in\overline{\mathbf Q}$。

因为 $[z^5]D_{k,17}=1$，这个实际系数由原完整正矩直接读取：
$$
\boxed{
C_{k,a,\ell}
=\frac1{120\Omega^6}
 \int Y^5Z E^a\phi_{a,\infty}
 1_{\{Z,E\ {\rm unit}\}}\Delta_\ell\,d\mu_k .
}
\tag{30}
$$
(30) **不附 Y-unit**。所有原深门、C 支及伙伴都在积分内。
最高原总正矩次数为36；(30) 中的 $\Omega^6$
准确对应新增的五次 Y 矩与一次 Z 矩，其余混次沿用 (3)。

于是
$$
\boxed{p_{\tau_k,a}(\ell)=C_{k,a,\ell}\,\Omega I_{k,1}.}
\tag{31}
$$
这是原负一支到原已识别线的完整返回，
不是从一个非零质量推一个新算术来源。

将 (31) 代入 R742 的过滤式，并用 $I_{k,1}\ne0$ 约去共同因子，
得到实际代数系数恒等式
$$
\begin{aligned}
\mathscr P\sum_{a=0}^{30}\mathscr Q_{\ne a}
 \{\lambda^{r+2}C_{k,a,r+2}
              +c_a\lambda^{r+1}C_{k,a,r+1}\}
= (-1)^r\lambda^{2r+248}U_{31}V_{31}\,d_k ,
\end{aligned}
\tag{32}
$$
其中所有过滤器均为 R742 的原过滤器，
$$
c_a=-\chi_A\lambda^3\kappa^{a+1},\qquad
d_2=c_\infty/a_\infty,\qquad d_4=1/a_\infty .
$$
右边为非零代数数。
因此，对每个固定合格 p、每个 $k=2,4$ 及每个 $r\ge1$，
(32) 实际使用的有限集合中至少有一个 $C_{k,a,\ell}\ne0$；
这些指标均在 $0\le a\le30$、$r\le\ell\le r+124$ 内。
尤其 $r=1$ 时，至少一条 (30) 的真实正矩非零。
这不是逐个 a、逐个 $\ell$ 的非零断言，也未给所有 p 共用的一个非零指标。

(30) 所新增的正矩恰为 $Y^5Z$，总次数6；
原 $E^a\phi_a$ 的各6h次权仍逐项相乘，所以完整最高次数为36。
不能只取这个6次因子而删原权和伙伴门。

(32) 仍是原完整来源恒等式；它没有给 $J'_S,J'_T,J'_U$ 新增一个零。

## 7. 完整有限角色：只有 tame p 行

把 (27) 限制在 $\mathbf F_p^\times$。
其完整乘法 Fourier 展开为
$$
\Phi_{j,\pm}(x)
=\sum_{\chi\bmod p}\widehat\Phi_{j,\pm}(\chi)\chi(x),\qquad
\widehat\Phi_{j,\pm}(\chi)
=\frac1{p-1}\sum_{x\in\mathbf F_p^\times}
      \Phi_{j,\pm}(x)\chi(x)^{-1}.
\tag{33}
$$
因而准确有
$$
\boxed{
\begin{aligned}
\Omega I_{-1}(\nu_{k,j,a,\ell})
={}&
 \sum_{\chi|_{\mu_6}=1}
 \widehat\Phi_{j,-}(\chi)\,\Omega I_{k,\chi}\\
&+\sum_{\chi(\zeta)=\zeta^4}
 \widehat\Phi_{j,+}(\chi)\,\Omega I_{+,k,\chi}.
\end{aligned}}
\tag{34}
$$
这里每个 $\chi$ 都是模 p 的角色，所有系数均为代数数。
伙伴的 $p^{125}$ 深度不产生第一 Y 的 wild 角色；
它仍在这些系数中。

第一行正是 R746/R748 的原 $D_k$ 物理单位负一行，
第二行正是 R751 的 $P_{+,k}$ 物理单位负一行。
(22)–(24) 是将实际来源接到这两种一变量公式的证明。
没有省略任何合法 tame 角色，零值也照式保留。

对固定 p，(34) 的点来源族有限且与 $\ell$ 无关。
改变 $\ell$ 可以改变伙伴系数和其数域，不能把这些系数先固定再作自然 Galois 平均。
取 R742 的实际 $u\to0$ 时，第4节给同一有限族中
每个系数的明确代数极限，故可按坐标取极限。
本篇不使用一个关于一般 $\mathbf C_p$ 极限的点投影连续性断言。

## 8. 规范 étale theta 平均读取平凡点系数

本节给一个可以直接用于各实际 cut 的完整算子。
对第5节共同覆盖后的截面，定义
$$
\mathsf E_{\bar{\mathfrak p}}
=\frac1p\sum_{b\in E[\bar{\mathfrak p}]}
          \widetilde{\mathsf T}_b ,
\tag{35}
$$
使用其自然 descent 对称 lift。
由第5.1节的完美配对，
$$
\mathsf E_{\bar{\mathfrak p}}
   [\bar\pi_0]^*F_{j}
=[\bar\pi_0]^*
 \{c_{j,-,0}D_{k,17}+c_{j,+,0}P_{+,k,17}\}.
\tag{36}
$$
(35) 精确杀掉全部非零 s，只取原加性 Fourier 的零项。
这是几何 theta-group 平均，不是 Galois trace。

由于 (26) 且 (35) 与 $\mu_6$ 相容，(36) 的 type3 系数必为零：
$$
c_{j,+,0}=0.
\tag{37}
$$
同式也直接由 (27) 对全部 $x\bmod p$ 求和得到。

另一方面，完整 Ramanujan 和给
$$
\widehat\Phi_{j,-}(1)
=c_{j,-,0}-\frac1{p-1}\sum_{s\ne0}c_{j,-,s}
=\frac{p\,c_{j,-,0}-\Phi_{j,-}(0)}{p-1}.
$$
用 (25)，准确简化为
$$
\boxed{\widehat\Phi_{j,-}(1)=\frac p{p-1}c_{j,-,0}.}
\tag{38}
$$
$p/(p-1)$ 不是可删的单位；它的 p 进赋值为1。
$c_{j,-,0}$ 可以含 $1/p$，如原 unit depletion 的实际例子所示。

R748 已付第一行的全部点公式；R751 已付第二行的完整坏处、周期及点角色。
原 D 的 $\chi=1$ 项在 p 惯性下平凡，
其余合法 $\chi$ 的实际点角色在 p 单位上为 $\chi^{-1}$。
第二行的 $\chi|_{\mu_6}=\zeta^4$ 本来非平凡；
其点角色也被 p 惯性平凡投影消掉。
所用椭圆曲线到 $E_1$ 的固定缩放域在 p 不分歧。

故按 R749 **只作用点因子、固定全部系数**的惯性投影，(34) 给
$$
\boxed{
e_{I_p,1}^{\log}\{\Omega I_{-1}(\nu_{k,j,a,\ell})\}
=\frac p{p-1}c_{j,-,0}\,\Omega I_{k,1}.
}
\tag{39}
$$
这是整个实际 finite-gate 来源的结论。
不能只对某一个未识别的 $\mathbf C_p$ 条件质量施 (39)。

若定义 $\mathsf{CT}_Y$ 为 (36) 后的真实 $[\bar\pi_0]$ 下降，
则 (37)–(39) 可等价写为
$$
e_{I_p,1}^{\log}\{\Omega I_{-1}(\nu_j)\}
=\frac p{p-1}\Omega I_{-1}(\mathsf{CT}_Y\nu_j).
\tag{40}
$$
(35)–(40) 的全部 absolute phase 和变量倍率由同一个共同覆盖支付。
它们没有把 étale theta 平均误认成原某个物理 deep-core。

对 primitive，(29) 的模 p 函数为 $C_{k,a,\ell}1_{\mathbf F_p^\times}$，
其零 Fourier 系数为 $(p-1)C_{k,a,\ell}/p$。
于是 (39) 准确回到 (31)，各因子彼此吻合。

## 9. 三条真实补支的完整系数关系

原 (5) 的分区、(23) 的唯一性给逐函数恒等式
$$
\begin{aligned}
\Phi_{G,-}+\Phi_{W,-}+\Phi_{V,-}
 &=C_{k,a,\ell}1_{\mathbf F_p^\times},\\
\Phi_{G,+}+\Phi_{W,+}+\Phi_{V,+}&=0 .
\end{aligned}
\tag{41}
$$
所以各实际来源的平凡点系数准确满足
$$
\boxed{
C_{k,a,\ell}
=\frac p{p-1}
 \{c_{G,-,0}+c_{W,-,0}+c_{V,-,0}\}.
}
\tag{42}
$$
W/V 的系数是 R747 native 测度的系数，已经含 (7) 的
$\lambda,\gamma\lambda$。
若改写成返回态上的 $H_W,H_V$，须把这两个标量原样提出。

(41) 还保每个非平凡 tame 角色的相反补偿；
不是只比较一个平均值。
(39) 可以读取它们实际点空间中的每个已识别分量，
但不会改变它们源于同一完整分区的事实。

特别，R742 已知非零的 primitive 过滤项仍可由
G/W/V 三条支完整补足，原 paired-T 外部仍给其相反数。
本篇没有据 (42) 宣称其中某个支为零，
也没有将原无条件谱恒等式当作新的中央约束。

要接主目标，仍须将原 $J'_S,J'_T,J'_U$ 的已付条件，
传到某个**独立的完整同域**关系，或计算各原外部的实际值。
固定有限门的来源闭包不能将整条
$\log(1+\kappa\,\text{线性行}/\text{单位行})$
自动换成 (34) 的有限负一值。
若使用无穷极限，须像第4节那样逐系数支付真实极限；
R749/R753 的点因子操作不具有一般 $\mathbf C_p$ 连续性。

## 依赖

- [R747](R747-original-source-restoration-and-p-primary-gate-model.md)：
  原 e0 的四个实际来源、全部返回标量、p-primary 唯一提升与对称 lift。
- [R742](R742-fixed-seventeen-operators-and-same-gate-primitive-limit.md)：
  同一有限门、17投影交换、固定 p 的实际权极限及原过滤式。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)：
  正交 line bundle、全部代数 jets 与混次周期。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)、
  [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)：
  完整半特征、17单重向量、二处矩阵及原 Dk 规范。
- [R746](R746-original-type-five-all-finite-p-character-squares.md)、
  [R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md)：
  原 Dk 的物理有限角色与共同周期点公式。
- [R751](R751-second-dyadic-character-point-fields-and-inertia-extraction.md)：
  第二 dyadic 来源 P+ 的完整角型、坏处及 finite-character 点公式。
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md)：
  点张量单射、固定系数投影及其与自然 trace 的区别。

本篇不生成新的数值数据；所有新增身份是原实际来源、theta group 和有限角色上的精确证明。
