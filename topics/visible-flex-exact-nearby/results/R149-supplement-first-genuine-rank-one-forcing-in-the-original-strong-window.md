# 完整首个 genuine 秩一体源在原强 Sobolev 窗口的直接接收

在 [G.6–9、G.21](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md) 的完整 $L_{2,j}$ 中分出其原加数 $\mathfrak R_j(w_0)$。保留 $n=4|j|$、两参考输入、原选中实参数域、$P$ 和同一反射类中的物理 $J$。令 $D=x^2+Ty^2$, $\Delta=D-n^{-2}V_{\rm ext}y^2$，$y=T_\phi$, $x=X_\phi$, $s=\sqrt{-T}$，$\epsilon=\operatorname{sgn}j$。由 $\omega_\phi=-sy$ 和实际 $w_0=G(x^2+\omega_\phi^2,2i\epsilon x\omega_\phi/s)^t$，
$$
 (i\epsilon y,x)w_0=-i\epsilon GyD,\qquad
 R=\mathfrak R_j(w_0)=-\vartheta QG\,V_{\rm ext}\,y(D/\Delta)
                       (x,i\epsilon y)^t .                              \tag{GSF.1}
$$
此式用完整真实 $B_je_1$；零点按原连续延拓。归一共轭或非零流形外推均未用于这项抵消。

以下给出能由原有限物理系数直接审计的严界。对 $0\le\rho<1/5000$，取 $Y=(35/2)\rho^2$；其余部位该源为零。记 $\Theta_0(r),\Theta_1(r)$ 为原 $\vartheta,\partial_\phi\vartheta$ 的整圆模界。对任意 $S\subset\{4|j|\ge N\}$、$N\ge388$，真实标量体源
$$
 \mathcal F_R f=P\sum_{j\in S}n^{-5/6} e^{4ijX}
                          R^t \operatorname{diag}(1,n^{-1})\Psi_n(T) f_j
$$
从归一物理 $H^{-4/3}$ 到原 $H^{-5/3}$ 的整圆算子范数至多
$$
 N^{-1/2}(1+N^{-2})^{2/3}
             [1400000\,\Theta_0(r)+40000\,\Theta_1(r)]\,Y.              \tag{GSF.2}
$$
平方后作普通 $dr$ 积分，再开根，给全域体源费用。原 $J:H^{-5/3}\to H^{-2/3}$ 在此支持的整根窗内原界小于 $2$，故完整第一物理行的这一个加数至多同数乘 $2$。该次 $J$ 发生在原投影和反射组装后。此处未将普通 $L^2_\phi$ 的 8.22 传播费移到负 Sobolev 窗口。[实际根窗 J 界](R133-supplement-actual-piecewise-root-radius-one-over-fifty-and-full-seams.md)

## 系数与物理角导的共同分离

固定径向圆，以 $\mathscr M$ 记录形如 $\int a_h(\phi)c_h(j)\,dh$ 的符号，费用为 $\int\|a_h\|_\infty\sup_j|c_h(j)|dh$，可加有限和。对标量逐点积费用次乘；对矩阵用各项费用之和，对列用各分量费用之和。频率符号 $i\epsilon$ 的费用为一。此定义在剖面算子内依次产生输入对角与物理左乘，见 [GIB.2](R149-supplement-global-two-ray-inverse-powers-and-genuine-deformation-reception.md)，不会交换这两者。

用 $K=V_{\rm ext}$ 临时代指势，物理曲率在此节不参与该记号。BPF.4 对 $V,V_T$ 及原整域 $|V|<276,|V_T|<26431,|V_{TT}|<3830956$ 给
$$
 \|K\|_{\mathscr M}<290,\qquad \|K_\phi\|_{\mathscr M}<14000000\,Y.
$$
确实，实 cutoff 的 $|\chi_V'|<(2/L)\sqrt{129}<48000$：$p_{64}'$ 的峰值为 $129{128\choose64}/4^{64}\le\sqrt{129}$，其中 $[(2k-1)/(2k)]^2\le(2k-1)/(2k+1)$ 后乘积伸缩。$\chi_V'$、$y$ 都是公共左因子，$V_T$ 的水平集费至多 $26431+L\,3830956$；故导费用不超过 $Y[48000(276+L\,26431)+26431+L\,3830956]$。

M.8 原整窗的解析角宽为 $1/32$，其正积分在同一复角条上留 $\rho^2$，故 $|y|\le Y,\ |y'|\le32Y$，以及 $|x|\le81/80,\ |x'|\le 32/80$。直至根点的真实 $Q=\eta\sqrt k A^{-1/3}$、$G$ 有 $QG<35$，因为原 $a_+<23,A_->4,G<23/10$。$Q\propto(-T)^{-1/2}$、$G\propto A^{1/6}\propto(-T)^{1/4}$ 中被略去的因子仅依赖 $r$，所以 $|(QG)'|\le35Y/(4(-T))<1$；用 $-T\ge5\rho/2$。这些式子对 $\rho=0$ 按极限取值。整圆 $-T<1/1900$、$D>977/1000$，并由 $D'=2xx'+y^3+2T yy'$ 知 $|D'|<1$。

令 $F=D/\Delta=(1-a)^{-1}$，$a=n^{-2}K y^2/D$。几何级数给 $\|F\|_{\mathscr M}<1001/1000$，$\|F'\|_{\mathscr M}<Y^2$（$\rho>0$）。直接将 $a'$ 的三项用 $n\ge388,\ Y\le7/10^7,\ |(1/D)'|<(1000/977)^2$ 计入 $\|F\|^2\|a'\|$ 即得。由 GDG.17 的原分子、$F/D$ 及它们的导数得到
$$
 \|B_j\|_{\mathscr M}<21/10,\qquad \|B_j'\|_{\mathscr M}<33/10 .
$$
具体地，分子条目总费至多 $2(81/80)+(1+1/1900+290/388^2)Y<2.026$；导数总费小于 $1$，因为对角不超过 $2(32/80)$，其余为 $(Y+14000000Y/388^2)Y+(1+1/1900+290/388^2)32Y$。分母倒数 $(F/D)$ 与其导数分别小于 $1.025$、$1.06$。

于是按 (GSF.1) 逐因子得
$$
 \|R\|_{\mathscr M}\le10400Y\Theta_0,\qquad
 \|R'\|_{\mathscr M}\le Y(340000\Theta_0+10400\Theta_1).
$$
导 $y$ 的费用为 $32\cdot10400Y\Theta_0$，导 $QG$、势 $K$、$F$、末列的其余费用分别小于 $300,350,1,4100$ 倍 $Y\Theta_0$。取 $C=B_jR$ 并接 [GIB 实际近支撑剖面](R149-supplement-global-two-ray-inverse-powers-and-genuine-deformation-reception.md) 两行各 $9/5$，得
$$
 {9\over5}(\|C\|_{\mathscr M}+\|C'\|_{\mathscr M})
 \le Y(1400000\Theta_0+40000\Theta_1).
$$
原物理微分恒等式给 $\mathcal U(R)=n^{-1}[\partial_\phi\mathcal U(C)-\mathcal U(C')]$。两个输出乘子 $\Lambda^{-5/3}\partial_\phi$ 与 $\Lambda^{-5/3}$ 范数至多一，后者保均值。$n^{-5/6-1}(1+n^2)^{2/3}\le N^{-1/2}(1+N^{-2})^{2/3}$，证毕。

## 对整个支持逐原格结账

根到真实 $c$ 的片使用 [原完整复角系数张量](R133-supplement-actual-complex-inner-root-first-Airy-forcing.md) 的 $\|\vartheta\|<23$、角宽 $>1/128$，所以可取 $\Theta_1=128\cdot23$。其余所有与 $\rho<1/5000$ 相交的原闭格使用原 176 整件与真实一阶带号 $\vartheta$ 的完整 Laurent 系数，为零和非零模分别按其原频率付费，得到各格 $\Theta_0,\Theta_1$。根的不确定性在选格时取全上、下界。在外向原格 $[l,r]$，$\int_l^r\rho^4dr$ 按 $[(r_+-l)^5-(r_+-r)^5]/5$ 向上收，不用该格长度乘一律最大 $\rho^4$。原 $\mathcal U(\mathfrak R(w_0))$ 由真实 $c,\Phi_\pm,T,\Psi_n$ 定义，只在估计中用上述实包。新 owner 将报告 $N=388$ 和 $N=4(2^{20}+1)$ 的实际全域普通体源费以及各自乘 $J$ 后的第一行费；其它局部项、原非局部项和端点仍须参加完整物理响应。
