# R71. 实际 Kummer Frobenius 与补偿后的临界 jet

日期：2026-11-12。**状态：实际有限 Kummer 系统、奇偶半线及完整补偿公式已证明；指定移动 jet 的无穷非零仍开。**

R66 的 68 阶除法单位 $r_P$ 满足 $r_P(O)=1$。
同一中央 Borel 函数的奇部给另一固定代数模函数
$M_o=t+t^3/2+\cdots$；偶部为 $M_e=M_1=t^4+7t^6/2+\cdots$。
它们均在 $p\notin\{2,3,5,17\}$ 整。

令 $S$ 为原 256 标签和、$S_R$ 为其旋转，准确规范为
$$
M_e=c_e(S-iS_R)/2,\quad M_o=c_o(S+iS_R)/2,
$$
$$
c_e=\frac{\sqrt2\,17^{17/4}}{4800f},\qquad
c_o=\frac{i\sqrt2\,17^{7/4}}{32f}.
$$
在单位对数 $H_S,H_R$ 中取
$h_e=-c_e(H_S-iH_R)/(2\cdot68^2)$ 和相同的奇组合 $h_o$，
则其 $O$ 点一阶切向分别准确等于 $M_e,M_o$。

## 1. 真正整 Frobenius 修正

使用模参数 $t$ 与纤维坐标 $Z=-x/y$，选任何固定零截面的形式 Frobenius lift
$$
\phi(t)=t^p,\qquad
\phi(Z)=Z^p+pa_1(t)Z+pO(Z^2).
$$
对每个实际单位令
$$
Q_r=\frac{r^\sigma(t^p,\phi(Z))}{r(t,Z)^p},\qquad
B_r=\frac1p\log Q_r.
$$
有 $Q_r\equiv1\pmod p$、$B_r\in\mathcal O[[t,Z]]$、$B_r(t,0)=0$。
故 $H_r=\log r$ 的 Kummer 系统确有整 Frobenius 矩阵
$$
\begin{pmatrix}1&0\\pB_r&p\end{pmatrix}.
$$
两个单位共享常数方向，得到实际秩三系统，且连接是完整的 $d\log r$。

令 $B_e$ 为与 $h_e$ 相同规范的修正，$b_e=\partial_ZB_e(t,0)$。
惰性时系数 Frobenius 交换奇偶半线，微分给
$$
b_e=\eta a_1(t)M_o(t^p)-M_e(t),\qquad \eta=c_e/c_o^\sigma\in\mathcal O^\times.
\tag{1}
$$
普通时为
$b_e=\eta a_1(t)M_e(t^p)-M_e(t)$，$\eta=c_e/c_e^\sigma$。
因此裸惰性 $[t^{p+1}]b_e$ 依赖 lift：改变 $a_1$ 的一次项就改变该值。

## 2. 实际 GM 配对消去 lift 依赖

使用 R68 的同一整 $U,V$，令 $s=1-4t^2$、$H=V/t$，以及
$$
F_i=\frac{U^{p+1}}{sH^{p+2}},\qquad
F_o=\frac{U^{p-1}}{sH^p}.
$$
二者为常数项 1 的偶整级数。准确有特征零等式
$$
\boxed{C_{p+1}=\eta[t]a_1-[t^{p+1}](b_eF_i),}
\tag{2}
$$
$$
\boxed{C_{p-1}=-[t^{p-1}](b_eF_o).}
\tag{3}
$$
惰性补偿来自 $M_o(t^p)=t^p+O(t^{3p})$；普通修正从 $4p$ 次起，故不贡献临界项。
式 (2) 的两个 lift 变化准确相消。必须先取完整差再除 $p$，不能假定各项分别被 $p$ 除。
普通整和需除 $p^2$。取 $a_1=0$ 是合法形式坐标选择，但不证明所得值非零。

本结果把固定 Kummer 代表的 exact 修正和真实 GM 因子准确接合。
尚未将移动的 $p\pm1$ 阶 jet 识别为固定秩线性 cohomology 的已知非零条目。
全文见 [Kummer 垂直 jet 与 GM 配对](../notes/2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)。
