# 两真实根状态配平的右矩阵和完整负侧试探替换

保留原 $n=4|j|\ge388$，原自由两行 $F_n$、正侧选定根矩阵 $C_n=\left(\begin{smallmatrix}1&0\\\beta_n&1\end{smallmatrix}\right)$ 和真实参考 $\Psi_n(0)=F_n(0)C_n$。下文 $0$ 作为 $F,\Psi$ 的参数表示 $T=0$。在 $\mathcal E_h$、腰读取中仍用物理半径 $r$。给出含真实端点和完整均值的同一物理误差替换，并对全频输入右矩阵付统一的实际常数。

## 真根的显式秩一逆

记 $B=\mathcal B_j$，$D(T)=\left(\begin{smallmatrix}1&-B/n^2\\-TB&1-B'/n^2\end{smallmatrix}\right)$ 为原 Darboux 矩阵。在根置
\[
 u=F_n(0)^{-1}(B(0)e_1+B'(0)e_2),\quad v^t=e_2^t F_n(0),\quad
 N=F_n(0)^{-1}D(0)F_n(0)=1-uv^t/n^2 .
\]
$ v^t u=B'(0)$ 精确成立，故逐真实自然标签可取
\[
 L_n=N^{-1}C_n=\left(1+\frac{uv^t}{n^2-B'(0)}\right)C_n,\qquad
 D(0)F_n(0)L_n=\Psi_n(0).                                     \tag{GDM.1}
\]
这是两列两个状态行的矩阵等式，实际 $\beta_n$ 在右边同一位置。[IN.2–10](R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md)

原 A 最小已证径向盘给 $|B(0)|=|V(0)|<245,\ |B'(0)|=|V'(0)|/3<7325$，故分母严格正。[原四组全频势预算](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md) 由 Wronskian 和零点值，$\|F_n(0)^{-1}e_1\|\|v\|=\pi n^{2/3}m_1(0)$，$\|F_n(0)^{-1}e_2\|\|v\|=2/\sqrt3$，其中 $m_1(0)=4/(3^{2/3}\Gamma(1/3)^2)$。在 $[0,1]$ 对 $e^{-t}$ 积分五次交错下截，在 $[1,\infty)$ 对条件指数分布均值 $2$ 用 Jensen，得
\[
 \Gamma(1/3)>
 3-\tfrac34+\tfrac3{14}-\tfrac1{20}+\tfrac1{104}-\tfrac1{640}
 +e^{-1}2^{-2/3}>53/20.
\]
末式可用 $e<68/25$、$2^{-2/3}> 629/1000$。因 $3^{2/3}>207/100$，有 $m_1(0)<69/250$。取 $388^{1/3}>29/4,\ \pi<22/7,\ 2/\sqrt3<7/6$，得
\[
 \|N^{-1}-1\|
 \le\frac{\pi m_1(0)|B(0)|n^{-4/3}+(2/\sqrt3)|B'(0)|n^{-2}}
              {1-|B'(0)|n^{-2}}
 <\min(7/50,\ 396\,n^{-4/3}).
\]
原 $|\beta_n|<100n^{-4/3}$ 与 (GDM.1) 给
\[
            \|L_n\|<6/5,\qquad \|L_n-1\|<511\,n^{-4/3}.       \tag{GDM.2}
\]
$L_n$ 是两原输入上的频率对角矩阵，左边的物理投影、非线性角映射、正常化及均值均无交换。上述不等式同时包括全部 $j$ 和共轭号。

## 原两状态的根差

在整个负域写 $Z(T)=\Psi_n(T)-D(T)F_n(T)L_n$，$H=B''+VB$。GDM.1、IN.6 和 Darboux 第一状态及其导数的定义给
\[
 Z(0)=0,\qquad Z'(0)= e_2\,\frac{H(0)}{n^2}\,[F_n(0)]_{2,:}L_n,\qquad
 H(0)=V''(0)/5+V(0)^2 .                                      \tag{GDM.3}
\]
附带 $|H(0)|<2929766/5+245^2<647000$。虽然两根状态配平，零锚两行矩阵的二阶高度导数仍有 (GDM.3) 的非零源。

记 $S=\operatorname{diag}(1,n^{-1})$，$w^V=w_0+n^{-1}w_1^V$，$w_F=w_0+n^{-1}w_1$，$R=n^{-2}R_2+n^{-3}R_3$，其中
\[
 R_2=B\mathcal K w_1^V+B'E_{22}w_0,\qquad R_3=B'E_{22}w_1^V .
\]
取 $f_F=P n^{7/6}e^{4ijX}w_F^tSF_n(T)L_n$，定义具同样物理意义的
$\delta f_R=-P n^{7/6}e^{4ijX}R^t S F_n(T)L_n$。原 IN.7–8 的有序矩阵乘法给实际两原列的恒等式
\[
        f_G-f_F=\delta f_R+P n^{7/6}e^{4ijX}(w^V)^t S Z(T).
                                                                  \tag{GDM.4}
\]
对 $f_G,f_F$ 分别按原 WUA.40–41 用相同 $J,D_0,B_{\rm op}$ 重建实际两状态 $\mathscr U_G,\mathscr U_F$ 及独立物理均值 $z_G,z_F$，均取其原零根初值。记 $D_r=\partial_r-d\partial_\phi$。在根 $T=0$ 同整圆，故 GDM.4 最后一项及其角导全零。$D_rT=QX_\phi$，两原状态的精确根差 $\delta h_*=(\mathscr U_G-\mathscr U_F)(r_*)$ 为
\[
 \begin{split}
 (\delta h_*)_2&=\delta f_R\big|_*,\\
 (\delta h_*)_1&=J_*(D_0-B_{\rm op})\delta f_R\big|_*+
 J_*P n^{7/6}e^{4ijX_*}
       (D_rT)_*\frac{w^V_{*,2}}n
       \frac{H(0)}{n^2}[F_n(0)]_{2,:}L_n .
 \end{split}                                                     \tag{GDM.5}
\]
第二行第一项先按完整原定义求根侧导，再取根值；只对 $\delta f_R|_*$ 这一个固定圈作导会漏去 $R,F_n,X$ 的径向导。$B_{\rm op}$ 为原非均值状态算子。GDM.5 中的 $P$ 作用于右侧整个物理角波。此式不删除真实有限头及任何频率的两状态。

原 SE.9–10 在这条完整物理根圆给 $T=0,X=\phi,D_rX=0,D_rT=c_*>0$，$a_0=1,b_0=D_rb_0=a_1^V=0$。置 $\gamma=b_1^V|_*$、$a'=D_ra_1^V|_*$、$\gamma'=D_r b_1^V|_*$、$A_i=[F_n(0)]_{i+1,:}$、$B_i=\partial_T^iB(0)$。于是 $R_2|_*=0$，$R_3|_*=(0,B_1\gamma)^t$，并且
\[
 D_rR_2|_*=(c_*B_0\gamma,\ B_0a')^t,\qquad
 D_r R_3|_*=(0,\ c_*B_2\gamma+B_1\gamma')^t .
\]
在这一圆，$D_0 P=P D_r$，自由矩阵第二行的 $T$ 导数为零。将 GDM.3–5 在取模以前合成，$H(0)-B_2=B_0^2$ 精确消去 $B_2$。若 $\mathcal P_n(g)=P n^{7/6}e^{4ij\phi}gL_n$，两个实际根行可写为
\[
\begin{split}
 d_2&=-\mathcal P_n\big(n^{-4}B_1\gamma A_1\big),\\
 d_1&=J_*\big\{-\mathcal P_n\big(
 n^{-2}c_*B_0\gamma A_0+n^{-3}B_0a' A_1+
 n^{-4}(B_1\gamma'-c_*B_0^2\gamma)A_1\big)-B_{{\rm op},*}d_2\big\}.
\end{split}                                                     \tag{GDM.7}
\]
只在此行使用了 $w^V_{*,2}=\gamma/n$。尤其原整件已给 $\|\gamma\|_{A_0}<0.938$、$\|\gamma_\phi\|_{A_0}<4.249$、$\|\gamma_{\phi\phi}\|_{A_0}<21.575$，并含真正角均值。$a'$、$\gamma'$ 是完整一般原频率根导数；$J_*$ 外的有限头及独立正端仍在 GDM.6。[原根归一](R133-supplement-natural-stable-port-Fredholm-and-exact-reference-elimination.md)；[真实首修正的已算全角界](R133-supplement-actual-saved-genuine-first-column-density-one-SV-sources.md)

## 同一物理输出的整件有向抵消

在每个原物理片用 WUA.42–43 从 $f_F,z_F$ 算 $g_F$ 和 WUA.46–47 的跃迁 $j_F$。保留同一个正侧真正改正 $e^+$ 和有限投影 $P_F$。WUA.50–53 对真实两行物理演化直接给
\[
 \begin{split}
 {\cal R}_{\rm waist}(\Psi_A-V_{\rm old})
 ={\cal R}_{\rm waist}\{&
 {\cal E}_h(0,r_*)[\,e^+(r_*)-P_F h^G(r_*)+\delta h_*\,]\\
 &+\int_0^{r_*}{\cal E}_h(0,r)g_F(r)\,dr
  +\sum_{0<r_\lambda<r_*}{\cal E}_h(0,r_\lambda)j_F(r_\lambda)
  +\mathscr U_F(0)-V_{\rm old}(0)\}.
 \end{split}                                                     \tag{GDM.6}
\]
连写的 $\mathcal E_h$ 指依原合格窗口在实际截面拼接，并含独立物理均值和有限头。若旧腰态以密度坐标给出，同 WUA.53 先用原 $\mathfrak D_0^{-1}$。证明是对 $\Psi_A-\mathscr U_F$ 在每个实原片应用变常数式，相邻片以真有向状态迹相接。等价地，把 $\mathscr U_G-\mathscr U_F$ 的同一 Duhamel 恒等式加入 WUA.52，整段势体源、其相伴接缝与原端点差逐项抵消。此合成从未将一个已取模的上界从另一个上界扣除。[原负侧真实两行、正端口与腰](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md)

因此在选定的一组真实负侧输入上，可用 (GDM.5)、完整自由包的物理源和 $\mathscr U_F(0)-V_{\rm old}(0)$ 合成一次。GDM.6 的 $\mathscr U_F$ 仍带实际 (GDM.1) 右矩阵。其余输入可沿原真势传播估计。若再改用直接数值试探 $U'$，同式的 $\delta h_*$ 必须改为 $h^G-U'(r_*)$，并使用 $U'$ 自身的所有状态源、跃迁、腰端与均值。原巨大 $N_{\rm raw,b}$ 的零阶角均值在自由源中仍有实际贡献，须靠这些有向端口或实际物理传播接收；GDM.2 自身只付输入矩阵。

GDM.1–5 和 GDM.7 对负侧两独立真参考列成立。GDM.6 中的正侧 e+ 只在原 PC 的自然终端 Ai 注入或另已资格的实际 positive Poisson 输入上使用；这里不为任意独立 Bi 输入授予已完成的正侧解。所有未资格的正端仍需单独证明。

附属 whole-receipt reader `fourfold_codazzi_genuine_root_matching_saved_bounds.py` 只验证下列新有理推论，原 V/SV 数值与其全部均值不重算；首次结果见 `../notes/2026-11-28-GDM-new-root-right-matrix-comparisons.json`。
