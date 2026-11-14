# R60. 秩零参考归一与无周期有限权证书

日期：2026-11-12。**状态：完整证明；未证明无穷多个素数命中证书。**

## 1. 实际参考是可逆的 Iwasawa 级数

固定普通目标素数 $p\ge13,p\ne17$。
令 $h_m=m![z^m]A_{17}$、$t_m=m![z^m]\theta_{17}$，两者均为固定整数。
用 $E_0:y^2=x^3-x$ 与 $E_{17}$ 的整 CM 同构选兼容周期
$\Omega_0=17^{1/4}\Omega_{17}$。
实际参考 principal Mellin 变换满足
$$
J_\theta(0)\in\mathcal O^\times,\qquad
\mathscr R_p(T)=J_p(T)/J_\theta(T)\in\mathbb Z_p[[T]],\quad
\mathscr R_p(0)=0.
\tag{1}
$$
其中 $\mathcal O=\widehat{\mathbb Z_p^{\rm ur}}$。

参考中心单位由实际平方公式、$L(E_0,1)/\Omega_{\rm real,0}=1/4$
和非异常 Euler 因子证明。全有理二挠点给
$a_p(E_0)\equiv2\pmod4$，Hasse界排除 $a_p(E_0)\equiv1\pmod p$。
这一步没有从正权矩中删除未知原点原子。

写 $T_m=(1+p)^m-1$，并分别使用两条曲线的真正 Hecke 值
$$
E_D(m)=1-\pi_D^m/\bar\pi_D^{m+1},\quad D=0,17.
$$
所有正权 $m\equiv0\pmod{p-1}$ 有
$$
\mathscr R_p(T_m)=\frac{E_{17}(m)}{E_0(m)}\frac{h_m}{t_m}\in\mathbb Q_p,
\qquad t_m\in\mathbb Z_p^\times.
\tag{2}
$$
周期在(2)中准确相消；$\mathscr R_p\in\mathcal O[[T]]$ 再由
$T_{(p-1)p^n}\to0$ 的逐Taylor系数极限降到 $\mathbb Z_p[[T]]$。
故
$$
\mathscr R_p'(0)=J_p'(0)/J_\theta(0),\qquad
v_p\mathscr R_p'(0)=v_pJ_p'(0).
\tag{3}
$$
这里是两个 Mellin 变换的商，不是函数商 $A_{17}/\theta_{17}$ 的 Mellin 变换。

## 2. 线性最高权的完整证书

令 $V_0=0$，$V_j$ 为(2)中 $m=j(p-1)$ 的值，置
$$
\Delta_r=\sum_{j=0}^r(-1)^{r-j}\binom rjV_j,\qquad
S_R=\sum_{r=1}^R\frac{(-1)^{r+1}}r\Delta_r,
\quad H_p(R)=\min_{r>R}(r-v_p(r)).
$$
由(1)的有界测度表示有 $\Delta_r\in p^r\mathbb Z_p$；
Newton展开在零求导给
$$
v_p\bigl(S_R-(p-1)\log_p(1+p)\mathscr R_p'(0)\bigr)\ge H_p(R).
\tag{4}
$$
结合 R40/R51 的实际斜率判据，
$$
\boxed{\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}
\iff\exists R\ge1:\ v_pS_R<H_p(R).}
\tag{5}
$$
最高权为 $R(p-1)$，不需 $\Omega_p$ 的有限精度输入。

## 3. 只用两个固定整数序列的版本

对每个 $R\ge1$ 选 $p\nmid s$ 且 $s(p-1)\ge R$，令
$$
\rho_0=0,\quad \rho_j=\frac{h_{sj(p-1)}}{t_{sj(p-1)}}\in\mathbb Q,
\quad
\widetilde S_{p,R}=\sum_{r=1}^R\frac{(-1)^{r+1}}r
\sum_{j=0}^r(-1)^{r-j}\binom rj\rho_j.
$$
设 $B_p(R)=R+1-\lfloor\log_p(R+1)\rfloor$。准确误差为
$$
v_p\bigl(\widetilde S_{p,R}-s(p-1)\log_p(1+p)\mathscr R_p'(0)\bigr)
\ge B_p(R).
\tag{6}
$$
证明中，Euler比值减一的估值至少为m，且
$v_p\rho_j\ge1+v_pj$；有限差分及除r后误差仍达到(6)。
$p\nmid s$ 使主项估值不随所选s改变，故同样有完整充要证书
$$
\boxed{\Sha[p^\infty]\text{有限}
\iff\exists R\ge1:\ v_p\widetilde S_{p,R}<B_p(R).}
\tag{7}
$$
若 $R\le p-2$，取 $s=1$ 且误差至少 $p^{R+1}$；
一般可使最高权不超过 $R^2+2R(p-1)$。
用 R57 的整数 $a_r$ 和 $T_r=\theta_0^{(4r)}(0)$，全部比值简化为
$h_{4r}/t_{4r}=a_r/(17T_r)$。

根端复跑[纯有理脚本](../scripts/check-ordinary-reference-newton.py)：
$p=13,R=2$ 只用权12、24得到 $\widetilde S=1248\bmod13^3$、
$\mathscr R_{13}'(0)=60\bmod13^2$。
单独参考规范给 $J_\theta(0)=133\bmod13^2$，乘回为
$J_{13}'(0)=37\bmod13^2$，与R56一致。
证明全文、原点原子和两条曲线的 Euler 规范见
[秩零参考与纯有理Newton证书](../notes/2026-11-12-ordinary-reference-normalized-rational-newton.md)。
逐p完备性不提供跨p非零；该条件仍列为open.md中的实际缺口。

## 4. 同一实际因子的四阶导数也给单位参考

更内在地，令 $B=A_{17}^{(4)}$。若 $\nu_A$ 为实际整 Amice 测度，
则 $d\nu_B=\Omega_{17}^{-4}x^4d\nu_A$，所以
$J_B(0)\equiv h_4=24\pmod{p^4\mathcal O}$。
这直接给单位参考，并且对正principal权m有
$$
\mathscr Q_p=J_p/J_B\in\mathbb Z_p[[T]],\quad
h_{m+4}\in\mathbb Z_p^\times,\quad
\mathscr Q_p(T_m)-h_m/h_{m+4}\in p^m\mathcal O.
\tag{8}
$$
证明下降时，近似值未必本来就是Qp值；但在 $m_n=(p-1)p^n$ 上
误差除以任意固定 $T_{m_n}^k$ 后仍趋于零，逐Taylor系数即可下降。
在(6)–(7)改用比值
$$
\frac{h_{4r}}{h_{4r+4}}=\frac{a_r}{17a_{r+1}},
\qquad p\nmid s,\quad s(p-1)\ge R+1,
$$
得到同样完备的纯有理证书。此处多要求的一阶准确补偿 $p^m$ 误差。
因此全局输入只需同一整数序列的相邻项；所有目标ordinary p及j≥1有
$p\nmid a_{j(p-1)/4+1}$。
根端独立核查p13、R2时部分和为325模2197，导数为79模169；
乘参考中心24后仍为37模169。完整证明见上述笔记§7。
