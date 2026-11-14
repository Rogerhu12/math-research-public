# R239 附录：双 dyadic 块的原头近交织与增长头完整非primitive核观测

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：下列原有限头近交织、完整纯尾修正及原缺陷角度估计已证明。一般左费用、无权 $N=M$ 和普通 ISP 仍开。

本稿把[实际高孔观测笔记 §14](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)的单个 primitive 头推广为一个增长低头的整个 $A_r+D_m$ 核。它保留原 $A_r$ 的长跳跃及全部非primitive尾分量；没有用 Jordan 相似替换实际内积。

## 1. 原空间与嵌入

选定 $N$ 或 $Y$ 模型。令
$$
m\ge7,\quad d=2^m,\quad 1\le r\le m-6,\quad K=2^r\le d/64,
\quad n=m-2,\quad p=2^n=d/4.
$$
$A_m$、$A_r$ 是同一模型的原有限头，分别作用在 $H_m=\operatorname{span}\{e_0,\ldots,e_{d-1}\}$ 与 $H_r=\operatorname{span}\{e_0,\ldots,e_{K-1}\}$。原系数为 $b_j=(j+1)^{-2}$，且
$$
D=D_m=\sum_{j\ge m}b_jE_j,\qquad L_m=A_m+D.
$$
给定原窗口 $4d\le q\le q_m=\lfloor e^{d^3/4}\rfloor$，定义闭空间
$$
\boxed{
\mathscr Z_{r,m,q}
=\ker(A_r\otimes I+I\otimes D_m)
\cap(H_r\otimes\mathcal H_{\le q}^{(m)}).
}
\tag{1.1}
$$
每个 $z$ 都满足
$$
D_m^Kz=(-A_r)^Kz=0.
\tag{1.2}
$$
没有预先令其尾分量 primitive。

对 $a=0,p,2p$，令 $U_a:H_r\to H_m$ 为原物理平移嵌入 $U_ae_\ell=e_{a+\ell}$。两高块互不相交且不越出 $H_m$。定义
$$
\boxed{
H_{m,r}=\frac{b_{n+1}U_p-b_nU_{2p}}{\sqrt{b_n^2+b_{n+1}^2}}.
}
\tag{1.3}
$$
于是 $H_{m,r}^*H_{m,r}=I_{H_r}$。其第零列就是原高孔笔记的 $h_m$，第一个非零列是将该列最低位创建一次。

令
$$
\mathscr G_{r,m,q}
=(H_{m,r}\otimes I)\mathscr Z_{r,m,q}.
\tag{1.4}
$$
这是原空间中的闭子空间。

**定理。** 对任意原缺陷 $w\in W=M\ominus N$，
$$
\boxed{
\|P_{\mathscr G_{r,m,q}}w\|
\le2e^{-d^4/20}\|w\|.
}
\tag{1.5}
$$
对任意原完整源 $r_0\in\mathscr R_q$，沿用真正的左最小者 $v=E_q^\dagger r_0$ 和 $r_0^\flat=G_qJ_q^{-1}r_0$，有
$$
\boxed{
\|P_{\mathscr G_{r,m,q}}v\|^2
\le e^{-d^4/10}
\left(\mu_q(r_0)^2+\lambda_q(r_0^\flat)^2\right).
}
\tag{1.6}
$$
这里 $r_0$ 的下标只为避免与低头位数 $r$ 混淆。

## 2. 原 dyadic 块的准确权积

先取任意 $a=2^s$，其中 $s\ge r$ 且 $a+K\le d$。对 $i<s$，比较原归一化加权后移在 $U_aH_r$ 上与低头上的作用。

当 $i<r$ 且 $\ell\ge2^i$ 时，长度 $2^i$ 的区间不跨越块底 $a$，所有权的二进阶与对应低头区间相同，所以
$$
N_i^{[m]}U_ae_\ell=U_aN_i^{[r]}e_\ell.
$$
当 $i<r$ 且 $\ell<2^i$ 时，区间跨越 $a=2^s$，它只把标准长 $2^i$ 区间中的一个 $\alpha_i$ 换成 $\alpha_s$，其余权的计数不变。因此
$$
\left(N_i^{[m]}U_a-U_aN_i^{[r]}\right)e_\ell
=\frac{\alpha_s}{\alpha_i}e_{a+\ell-2^i}.
$$
不同 $\ell$ 的输出正交。故
$$
\boxed{
\|N_i^{[m]}U_a-U_aN_i^{[r]}\|
\le\frac{\alpha_s}{\alpha_i}
\quad(i<r).
}
\tag{2.1}
$$
对 $r\le i<s$，整个块都跨底，准确有
$$
N_i^{[m]}U_a=\frac{\alpha_s}{\alpha_i}U_{a-2^i}.
\tag{2.2}
$$
对 $i=s$，完整区间内恰有标准各阶权的计数，因此
$$
N_s^{[m]}U_a=U_0,\qquad (N_s^{[m]})^2U_a=0.
\tag{2.3}
$$
对 $i>s$，头索引不足 $2^i$，作用为零。

全部有限头的 $\|N_i^{[t]}\|\le1$。又 $(N_i^{[t]})^2=\eta_iN_{i+1}^{[t]}$（顶位则为零），故
$$
\|(I+N_i^{[t]})^{-1}\|
\le\frac2{1-\eta_i}<3.
\tag{2.4}
$$
对任意两个算子 $M,B$ 和中间映射 $U$，当上述逆存在时，直接乘回两侧可核验
$$
M(I+M)^{-1}U-UB(I+B)^{-1}
=(I+M)^{-1}(MU-UB)(I+B)^{-1}.
\tag{2.5}
$$
因此 (2.1) 的 Cayley 版本至多多付因子 $9$，(2.2) 至多多付因子 $3$；(2.3) 仍准确给 $Y_s^{[m]}U_a=U_0$，其后项仍为零。

由于 $\alpha_s/\alpha_i\le\eta_{s-1}$ 对所有 $i<s$ 成立，且 $\sum_{i\ge0}b_i<2$，两个模型统一得到
$$
\boxed{
\|A_mU_{2^s}-U_{2^s}A_r-b_sU_0\|
\le18\eta_{s-1}.
}
\tag{2.6}
$$
这是一条整块算子范数界，不是逐列界直接乘到未知叠加上。

## 3. 两块主项相消，低头完全保留

将 (2.6) 分别用于 $s=n,n+1$。在 (1.3) 的线性组合中，两个 $U_0$ 主项准确相消。由 Cauchy--Schwarz 和 $\eta_n\le\eta_{n-1}$，
$$
\begin{aligned}
\|A_mH_{m,r}-H_{m,r}A_r\|
&\le18\frac{b_{n+1}\eta_{n-1}+b_n\eta_n}{\sqrt{b_n^2+b_{n+1}^2}}\\
&\le18\sqrt2\,\eta_{m-3}<32\eta_{m-3}.
\end{aligned}
$$
记
$$
\boxed{E=A_mH_{m,r}-H_{m,r}A_r,\qquad \|E\|\le32\eta_{m-3}.}
\tag{3.1}
$$
置 $T=d/2+K-1$。$H_{m,r}$ 的输出头指标至多为 $T$，而 $A_m$ 与 $A_r$ 都严格下降头指标，因此 $E$ 的输出头指标至多为 $T-1$。特别
$$
\boxed{A_m^TE=0.}
\tag{3.2}
$$
对 $z\in\mathscr Z_{r,m,q}$，有准确式
$$
L_m(H_{m,r}\otimes I)z=(E\otimes I)z,
\qquad D^K(E\otimes I)z=0.
\tag{3.3}
$$
实际低头 $A_r$ 的全部长跳跃和所有非primitive层耦合都仍在 (1.1) 中，没有用纯等权头代替。

## 4. 同一辅助头上的有限同伦修正

使用[R254相容多次原像 §§1–3](R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)，把该稿 $(j+2)^{-2}$ 重编号成当前 $(j+1)^{-2}$。输入孔数上界取 $q$、最大阶取 $T$，得到同一辅助头上的 $R_0=I,R_1,\ldots,R_T$，满足
$$
DR_j=R_{j-1},\qquad
R_j(\ker D^K\cap\mathcal H_{\le q})\subset\ker D^{K+j},
$$
并严格增加 $j$ 个孔。
为统一粗界，取
$$
\mathcal L=512\sqrt{q+2T+1}(m+q+2T+1)^{3/2}.
$$
该稿完整层范数界给
$$
\boxed{
\|R_jf\|\le\binom{K+j-1}{K-1}\mathcal L^{K+j-1}\|f\|,
\quad f\in\ker D^K\cap\mathcal H_{\le q}.
}
\tag{4.1}
$$
输入核阶 $K$ 只支付一次，未把费用改成 $\mathcal L^{Kj}$。所有头矩阵与尾 $R_j$ 交换。

定义
$$
\mathcal C z
=\sum_{j=1}^T(-1)^{j-1}A_m^{j-1}\otimes R_j\,(E\otimes I)z,
\qquad
\mathcal Z z=(H_{m,r}\otimes I)z-\mathcal C z.
\tag{4.2}
$$
(3.2) 与相容关系使有限和严格望远镜：
$$
L_m\mathcal C z=(E\otimes I)z,
\qquad
\boxed{L_m\mathcal Zz=0.}
\tag{4.3}
$$
全部输出孔数不超过 $q+T$，位置支撑可以无限远。没有在闭像未付的空间上使用无界逆。

(3.1)、(4.1) 及 $\|A_m\|<6$ 给
$$
\boxed{
\|\mathcal C\|
\le\varepsilon_{m,r,q}
:=32T6^{T-1}\binom{K+T-1}{K-1}
\mathcal L^{K+T-1}\eta_{m-3}.
}
\tag{4.4}
$$
同一输入空间的所有孔层按算子范数一起估计，没有额外 $q$ 次三角求和。

## 5. 原最大窗口仍支付增长 K 的全部费用

$q\ge4d$、$K\le d/64$ 及 $T=d/2+K-1$ 给
$\mathcal L\le2048q^2$。记 $R=K+T-1$，则
$$
R\le17d/32,\qquad T\le33d/64,\qquad
\binom R{K-1}\le2^R.
$$
利用 $\log q\le d^3/4$ 与原准确的
$$
\log\eta_{m-3}
=-\frac{175}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d,
$$
(4.4) 给
$$
\begin{aligned}
\log\varepsilon_{m,r,q}
\le{}&-\frac{39}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d\\
&+R\log4096+(T-1)\log6+\log(32T).
\end{aligned}
\tag{5.1}
$$
后面两项和对数项之和小于 $7d$：例如使用 $\log4096<9$、$\log6<2$、$T\le33d/64$、$R\le17d/32$ 和 $\log(32T)<d$ 即可。因此整行线性余量严格为负。

当 $m\ge7$ 时 $d\ge128$，
$$
\frac{39}{512}-\frac{315}{256d}
\ge\frac{2181}{32768}>\frac1{20}.
$$
于是
$$
\boxed{\varepsilon_{m,r,q}\le e^{-d^4/20}.}
\tag{5.2}
$$
这里允许 $K$ 随 $m$ 增长到 $d/64$，也允许整个原合法 $q$ 窗。

## 6. 原缺陷的角度估计

$T<d$，所以 $q+T\le q_m+d<e^{d^3/3}$。原线性逐头提升在整个有限孔核上给
$$
\Lambda\mathcal Zz\in N,\qquad
\|(\Lambda-I)\mathcal Zz\|\le e^{-75d^4}\|\mathcal Zz\|.
$$
(1.3) 为等距嵌入且 $\|\mathcal Z\|\le1+\varepsilon_{m,r,q}$，故
$$
\|\Lambda\mathcal Z-(H_{m,r}\otimes I)|_{\mathscr Z_{r,m,q}}\|
\le\varepsilon_{m,r,q}+e^{-75d^4}(1+\varepsilon_{m,r,q})
\le2e^{-d^4/20}.
\tag{6.1}
$$
对原 $w\in W$ 取伴随，使用等距嵌入的真实值域投影，即得 (1.5)。
本证明没有把 $P_{\mathscr G}w$ 认成新的 $M$ 向量或来源。

## 7. 任意原源的完整旗和三 Gram 版本

把 $\mathcal Zz$ 在原 $q$ 边界切为 $z^-+z^+$。左块在 $\mathscr V_q$ 中。
右块只来自 (4.2) 的修正。对输入第 $\ell\le q$ 孔层，第 $j$ 项位于 $\ell+j=q+k$，所以 $j\ge k\ge1$。由 (3.2) 的支撑及逐次下降，其头指标至多为 $T-j$；由 (4.1) 其尾核阶至多为 $K+j$。而
$$
d-(T-j)\ge K+j
\quad\Longleftrightarrow\quad d-T\ge K,
$$
后者由 $K\le d/64$ 明确成立。头范围 $T-j\le d-k$ 也成立。于是每个右分量都在原联合输入旗中，内部零输出继承 (4.3)，有
$$
z^+\in\ker S,\qquad E_qz^-+F_{\rm flag}z^+=0.
\tag{7.1}
$$

对 (1.6) 的源 $r_0$ 置 $y=J_q^{-1}r_0$、$v=E_q^*y$、$c^\flat=F_{\rm flag}^*y$，并按左右物理孔层记 $x=v+c^\flat$。则
$$
x\perp\operatorname{Ran}\mathcal Z,
\qquad \|x\|^2=\mu_q(r_0)^2+\lambda_q(r_0^\flat)^2.
$$
由于 $(H_{m,r}\otimes I)\mathscr Z_{r,m,q}$ 全在 $q$ 以下，(4.2) 给
$$
\left((H_{m,r}\otimes I)|_{\mathscr Z_{r,m,q}}\right)^*v
=\mathcal C^*x.
$$
左侧范数恰等于 $\|P_{\mathscr G_{r,m,q}}v\|$。由 (5.2) 得 (1.6)。完整源 Gram、低层左配对和所有非primitive尾项均被保留。

## 8. 二阶图是完整特例；未付的范围

当 $r=1,K=2$ 时，两模型的低头都准确为 $A_1=E_0$。因此
$$
\mathscr Z_{1,m,q}
=\{e_0\otimes f-e_1\otimes D_mf:
 f\in\ker D_m^2\cap\mathcal H_{\le q}\}.
$$
(1.4) 恰为 $h_m\otimes f-(E_0^*h_m)\otimes D_mf$ 的整个闭图。这严格包含旧的 $h_m\otimes\ker D_m$ 方向；新增部分的输入满足 $D_m^2f=0$ 而 $D_mf\ne0$。

对更大的 $r$，(1.1) 保留整个原低头 $A_r$ 的核方程，没有选取单个 primitive 链或只保顶层。其尾短核阶最高可达 $K$，且 $K$ 可随 $d$ 线性增长。

(1.5) 只控制两个指定高 dyadic 块中的这个完整模型核，尚未覆盖其正交补或整个原左最小空间。它不分别控制相消的两个高块，也不允许丢掉 (1.1) 的 $A_r+D_m$ 核约束。常数很小不能消除这些范围限制；(1.6) 仍不是全源三 Gram 比较，更不是无权 $N=M$ 的证明。

## 9. 更大低头与窗口的明确交换：最高 K=d/4

前面的保守参数不是此构造的端点。以下保留相同定义、整块近交织和全部输入旗，只重新核算原像费用。

现在允许 $m\ge5$、$1\le r\le m-2$，即 $K\le d/4$，仍令
$$
T=d/2+K-1,\qquad R=K+T-1=d/2+2K-2.
$$
两高块仍不重叠、不越界，(2.1)–(4.4) 逐项不变；而完整右旗所需条件
$$
d-T\ge K
$$
在 $K\le d/4$ 时始终成立。对 $q\ge4d$ 仍有 $\mathcal L\le2048q^2$，因此统一准确的预算上界为
$$
\begin{aligned}
\log\varepsilon_{m,r,q}
\le{}&-\frac{175}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d
+2R\log q\\
&+R\log4096+(T-1)\log6+\log(32T).
\end{aligned}
\tag{9.1}
$$
对 $d\ge32$、$K\le d/4$，$R<d$、$T<3d/4$，最后一行小于 $12d$，所以与 $-75d/2$ 合并后严格为负。

### 9.1 整个原窗、K 达 d/16

若 $K\le d/16$ 且 $q\le e^{d^3/4}$，则
$$
R\le5d/8-2,\qquad
2R\log q\le\frac5{16}d^4-d^3.
$$
(9.1) 因而给
$$
\log\varepsilon_{m,r,q}
\le-\frac{15}{512}d^4+\frac{59}{256}d^3.
$$
对 $d\ge32$，
$$
\frac{15}{512}-\frac{59}{256d}
\ge\frac{181}{8192}>\frac1{50}.
$$
所以在整个原合法窗口内，$m\ge5$、$1\le r\le m-4$ 已有
$$
\boxed{
\varepsilon_{m,r,q}\le e^{-d^4/50},\qquad
\|P_{\mathscr G_{r,m,q}}w\|\le2e^{-d^4/50}\|w\|,
}
\tag{9.2}
$$
以及对任意原完整源
$$
\boxed{
\|P_{\mathscr G_{r,m,q}}v\|^2
\le e^{-d^4/25}
\left(\mu_q(r_0)^2+\lambda_q(r_0^\flat)^2\right).
}
\tag{9.3}
$$
原第1节较窄 $K\le d/64$ 的更强常数继续有效。

### 9.2 K 达 d/4，保原窗内的指数子窗

若只把窗口取为
$$
4d\le q\le\lfloor e^{d^3/8}\rfloor,
$$
则对全部 $K\le d/4$，有
$$
R\le d-2,\qquad 2R\log q\le\frac14d^4-\frac12d^3.
$$
于是
$$
\log\varepsilon_{m,r,q}
\le-\frac{47}{512}d^4+\frac{187}{256}d^3.
$$
对 $d\ge32$，
$$
\frac{47}{512}-\frac{187}{256d}
\ge\frac{565}{8192}>\frac1{20}.
$$
因此 $m\ge5$、$1\le r\le m-2$、上述指数子窗内，完整 (1.5)–(1.6) 原样成立：
$$
\boxed{
\|P_{\mathscr G_{r,m,q}}w\|\le2e^{-d^4/20}\|w\|,
\qquad
\|P_{\mathscr G_{r,m,q}}v\|^2
\le e^{-d^4/10}\left(\mu_q(r_0)^2+\lambda_q(r_0^\flat)^2\right).
}
\tag{9.4}
$$
最大低头维数 $K=d/4$ 不再是固定维模型，且保全部非primitive的 $A_r+D_m$ 核。它仍是指定两个高块中受该核方程约束的子空间，不覆盖整个 $W$ 或真实左空间。
