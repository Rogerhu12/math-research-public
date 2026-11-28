# 整个原根到截面的 genuine 三项有符号局部源与两列 Green 矩阵

取原真实 $r_*$、$c=76285779072683/320000000000000$ 和选定的 repaired 背景。两者在单一原物理片 2549 内。下述有限计算合成 [G.6–9](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md) 的完整局部普通源，先合并旧自由余项、频率相关势和真实首幅，再应用同一 genuine 两列。完整原 $J$、物理腰读和公共输入只施于这个缓变源一次。[GFW.4](R149-supplement-signed-free-first-wave-and-correlated-genuine-potential.md)；[原 GCS 截面](R149-supplement-actual-whole-signed-cut-seed.md)。

令 $s=1/512$，$R=2^{-15},L=1/2000,t=T/R$。原共同势 $V_j$ 在 $|T|\le L$ 的完整界为 $276,26431,3830956$，分别对应零至二阶。两真实参考的根矩阵是 $F_n(0)C_n$，其中 $|\beta_n|<100n^{-4/3}$。实际截面和沿固定 $X$ 的 $T$ 单调性给整个实根窗 $|t|<3/5$。程序还逐闭格检验复轮廓 $|\Im\phi|=s$ 上同一不等式，周期条带内部由最大模原理覆盖。实域上 $|T|<L/2$，截断势恒等于原势，故可在此处使用该真实系数的唯一局部解析延拓。原完整物理根片上两支逆矩阵在 $1/64$ 角条内已有正行列式模隙。[原共同势](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md)；[原两列和旧圆逆](R133-supplement-actual-genuine-common-radial-columns-and-old-circle-inverse.md)。

## 同一初值下的两行有向解

对每个 $97\le |j|\le2^{20}$，采用同一右根坐标 $U_0=(Y(0),RY_T(0))^t$。自由矩阵 $F^c$ 和 genuine 矩阵 $G^c$ 均在 $t=0$ 归一为恒等阵。写 $q=n^2R^3$，$v_k=[t^k]V_j(Rt)$，$b_k=v_k/(2k+1)$。原背景的十五阶系数前缀（次数零至十四）按其原 whole stage 准入。对本频带真实 $z=j^{-2}$ 先做原 96 个非零中间分母的带号有理运算，按原径向 $r$ 导为 $-\partial_\rho$ 取 $W/\kappa^2$，再以 $\bar T(\rho)/R$ 的同一非零线性系数三角反演得 $v_0,\dots,v_{12}$。其余阶有 $|v_k|\le276(R/L)^k$。$B=\int_0^1 V_j(\tau^2T)d\tau$、$V_T,B_T,B_{TT}$ 皆在相同 $t$ 上以这些系数和全部收敛尾恢复。

对自由高度 $f$、共初值 genuine-minus-free 高度 $d$ 和 WUA.54 的零初值有向 Darboux 高度 $j_H$，精确方程为
\[
 f''=qt f,\quad d''=qt d-R^2V(f+d),\quad
 j_H''=(qt-R^2V)j_H+(R/n^2)(B_{TT}+VB) f'.                 \tag{GLC.1}
\]
此式导数均在 $t$。$d,j_H$ 的两行根初值皆零，无需从两已经取模的解相减。完整根端差 $\Psi D_n^{\rm root}$ 仍按 WUA.54 接入。$|t|\le1$ 上 $q+276R^2<1$，故两齐次状态矩阵的复直径向传播从原点或其到该点的子段的范数小于 $e$。Duhamel 给 $f,d,j_H$ 的圆盘模上界分别为 $3,9R^2\cdot276,9R(3830956/5+276^2)n^{-2}$。按 (GLC.1) 各计算到次数 64；若首遗漏为 $m$，在 $u=|t|$ 处高度尾至多 $M u^m/(1-u)$，第二状态行尾至多 $M u^{m-1}(m/(1-u)+u/(1-u)^2)$。同一 $\mathrm{diag}(1,R)F_n(0)C_n$ 在完整局部源两行做完以后右乘，其中真正第二参考列既是独立原输入，也是原第一列剪切的同一列。原 $Y_T/n$ 乘 $1/(nR)$ 一次。[WUA.17–24,54](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md)。

## 原物理格上的全部局部源

从 [原 11 件完整 $N_{\rm raw}$](R133-supplement-actual-correlated-local-Airy-numerator-through-ten.md) 读出 $\mathfrak A_0 w_1$。原收据已经分开保存完整正尾；每项径向次数至少十一，所以新半径 $h\le h_0$ 时，该原正尾可乘 $(h/h_0)^{11}$。其余每个原幅、折叠和偏导均从自己的有符号 Taylor 及原整乘积 Cauchy 模取得。先由 $-\mu M_0(f_b,f_a)^t$ 恢复 $\mathfrak A_0 w_0$，$M_0$ 的两行是 $(a_0,Tb_0)$ 和 $(b_0,a_0)$。$A_T=D(Qx)+Q^2TT_{\phi\phi}-T_0Qx$，$\mathcal D_T=Q(xD+QTy\partial_\phi)$，其中 $D=-\partial_\rho-d\partial_\phi$。由 $\mathcal D_T T=\mu$，得
\[
 (\mathcal D_Tw_1^V)_2=(\mathcal D_Tw_1)_2+B(\mathcal D_Tw_0)_1+\mu B_T a_0.
\]
将 GFW.4、上述导数的整个 G.4 和真实 $B_je_1=(i\epsilon x,-y)^t/(-x^2-Ty^2+y^2V/n^2)$ 在同一点组成
\[
 U=L_{1,j}+n^{-1}L_{2,j}+n^{-2}L_{3,j},\quad
 a_j(\phi)=e^{i\epsilon n(X-\phi)}U^t\operatorname{diag}(1,n^{-1})\Psi_n(T).
                                                               \tag{GLC.2}
\]
两频率符号各保原代数分支。全部 $|j|\ge2^{20}+1$ 的原实频参数以闭区间 $0\le1/n\le[4(2^{20}+1)]^{-1}$ 和相容的 $z$ 另算整个 $U$；$z=0$ 是解析端点。该无穷输入行没有在复角域外推其真实振荡剖面。有限带的每个圆均保两原列、两个真实角轮廓和所有整数输出。四个同根径向闭格覆盖原 $c\le r\le r_*$，每个 $φ$ 轮廓按完整周期分 128 个中心闭格。旧有限 Fourier 多项式所有模精确折入原节点 DFT 后用四阶实角 Taylor 余项覆盖整个格；另加本场的全部解析尾。

## 有向整行 Fourier 接收和原公共输入

在 $\Im\phi=w=-\operatorname{sgn}(h)s$ 的格 $k$ 取 (GLC.2) 一输入列的矩形中点 $m_k$，该格整余差上界为 $e_k$，$N=128$。闭格积分给在每个 $j$ 的整输出移位 $h$ 上
\[
 |\widehat a_j(h)|\le e^{-4s|h|}\min\left\{\sup|a_j|,
 \left|\mathrm{sinc}(\pi h/N)(\mathrm{DFT}m)_{h\bmod N}/N\right|+N^{-1}\sum e_k\right\}.
                                                               \tag{GLC.3}
\]
$s$ 的正负均保；$h=0$ 可用任一条。两列的欧氏范数乘原 $\langle4(j+h)\rangle^{-5/3}$，每个 $h$ 取同输入带、两符号最大后对所有 $h$ 求和。每一移位是单位范数，故该和乘 $n_{\max}^{1/6}\langle n_{\max}\rangle^{4/3}$ 即为原 $H^{-4/3}\to H^{-5/3}$ 带费。显式计算 $|h|\le3072$；余部几何和在 $|h|<j_{\min}/2$ 仍用 $|4(j+h)|\ge2j_{\min}$，再保所有其余输出及两方向与零模。分离处理两输入符号的远尾要先相加。原 $P$ 压缩，反射限制也为压缩。

各 $j$ 带输入彼此正交，故各带费平方和乘对应径向格长度再相加开根，得到 $D$，即 (GLC.2) 含 $n^{1/6}$ 的完整有限输入局部残差到 $L^2(dr;H^{-5/3})$ 的上界。由 [原同域 $J$ 与 GSF](R149-supplement-first-genuine-rank-one-forcing-in-the-original-strong-window.md)、[GSW 原两行传播、物理 $1/2$ 读及右归一](R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md)，这个原加数的有限参考输入到归一物理腰费用至多
\[
 D_{\rm nat}=2\cdot2039\sqrt{r_+-c}\cdot0.719D,
 \qquad C_{97,\mathrm{local,finite}}<12.4D_{\rm nat}.           \tag{GLC.4}
\]
公共高行可用 $10.611\cdot1.061\sqrt{.097^2+.022^2}D_{\rm nat}/1.1$。参考输入投影在原 $N_i$ 左边，有限投影是该处的正交压缩。完整普通源在这个根窗已包含 GSF 的同一加数；后继相叠部分只计一次。原旧圆非局部源、独立均值源、正侧校正、原界面及真实试探到原腰行的端点差还要按原有向恒等式进入全响应。这里的阈值记录由首个公开科学运行给出。
