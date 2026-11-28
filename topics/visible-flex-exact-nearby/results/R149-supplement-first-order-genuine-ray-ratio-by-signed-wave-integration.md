# 已证明：首强迫比的有符号边界项使体强迫只用一阶径向导数

在同一严格实负域，记 $L=\partial_\rho+d\partial_\phi$, $L_\sigma=L+\sigma b\partial_\phi$, $b=\eta\sqrt{-K}$。令 $p_\sigma=x-\sigma v$，$x=X_\phi, v=\omega_\phi$，$s=\sqrt{-T}$，$i_\epsilon=i\operatorname{sgn}j$。下式直接给出 [WUA.16](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md) 两方向、两频率符号的同一真实 $R_\sigma$。它保留真实 GCS 截面初值和整个有向体积分。

写 $W=L^2-b^2\partial_\phi^2$。由于 $[\partial_\phi,L]=d_\phi\partial_\phi$ 及 $b$ 径向，
$$
 W=L_\sigma L_{-\sigma}+\sigma(b_\rho-bd_\phi)\partial_\phi.
$$
设 $p_{-\sigma}=x+\sigma v$，$Q_f=b/s$，则 $\mu=(b/s)^2p_\sigma p_{-\sigma}$、$v_{0,\sigma}=G p_\sigma^2$。在真实入向方程
$$
 L_\sigma R_\sigma=-\frac{Q_f p_{-\sigma}}{G p_\sigma^2}
 \left(F_a/2-i_\epsilon\sigma F_b/(2s)\right)
$$
代入 $(F_b,F_a)^t=-\mu^{-1}(W+T_0L+V_0-\vartheta H^{-1}H_D)w_0$。所有方向和行次固定，系数正好化成行向量
$$
 c_\sigma=\frac{1}{2b G p_\sigma^3}(-i_\epsilon\sigma,s).
$$
因此令 $U_\sigma=R_\sigma-c_\sigma L_{-\sigma}w_0$，可得
$$
 L_\sigma U_\sigma=
 c_\sigma\left[\sigma(b_\rho-bd_\phi)\partial_\phi w_0+
 T_0 Lw_0+V_0 w_0-\vartheta H^{-1}H_Dw_0\right]
 -(L_\sigma c_\sigma)L_{-\sigma}w_0 .                  \tag{1}
$$
这是沿真实特征的一次分部积分，未另加任一未知端点。入端 $U_\sigma(c)=R_\sigma(c)-c_\sigma L_{-\sigma}w_0(c)$，在每个中间点与出端重新加回 $c_\sigma L_{-\sigma}w_0$。

## 完整消去径向幅因子

写 $g=w_0/G=(x^2+v^2,2i_\epsilon x v/s)^t$，$C=Gc_\sigma$，$\ell=\log G$。取真实正规化参数 $k=-K/\rho, B=b/\sqrt\rho,A=3\omega/(2\rho^{3/2})$，$k_1=k_\rho,A_1=LA$。由原 $G=(k_*/\eta_*)^{1/6}E_G A^{1/6} k^{-1/4}$ 得
$$
 L\ell=2\beta\Pi S+A_1/(6A)-k_1/(4k),\qquad
 \ell_\phi=A_\phi/(6A),\qquad S=u^2+Kv^2 .
$$
$G$ 的真实数值及 $E_G$ 积分整体不出现在本比值的接收、输运或还原中。使用以下三个向量：
$$
 D_0=Lg+(L\ell)g,\qquad D_\phi=g_\phi+\ell_\phi g,\qquad
 D_-=D_0-\sigma bD_\phi .
$$
由 $L_\sigma p_\sigma=-d_\phi p_\sigma$ 及 $s/b=A^{1/3}/B$，两带号槽的相对率为
$$
 t_0=3d_\phi-B_\rho/B-1/(2\rho),\qquad
 t_1=3d_\phi-B_\rho/B+(A_1+\sigma b A_\phi)/(3A).
$$
令 $M=(C_0(t_0-L_\sigma\ell),C_1(t_1-L_\sigma\ell))$。完整的 (1) 便是
$$
 \boxed{\quad
 L_\sigma U_\sigma=
 C\left[\sigma(b_\rho-bd_\phi)D_\phi+T_0D_0+V_0g+
 i_\epsilon\vartheta(b/s)(Tg_1,g_0)^t\right]-M D_-,
 \qquad R_\sigma=U_\sigma+C D_- .\quad}
$$
这里 $g=(g_0,g_1)^t$；最后的 $i_\epsilon\vartheta$ 项正是自由 $H^{-1}H_D=-i_\epsilon Q_fK_T$ 的完整贡献。它只应用于定义 $R_\sigma$ 的自由 WUA.13，后面的 genuine $B_j$ 仍保留。上式需要的导数由 $Lx=bv_\phi-d_\phi x$、$Lv=bx_\phi-d_\phi v$、$Ls=bx/(2s^2)$、$s_\phi=v/(2s^2)$ 给出。每个角阶都按同一物理点的带号 Leibniz 运算，具体核在 `fourfold_codazzi_true_first_ratio_first_order.py`。

## 所需的真实数据及接缝

首比值的六阶角体强迫只需 $A_1$ 到六角阶、$A_\phi$ 到六角阶、$x_\phi,v_\phi$ 各到六角阶。因 $\rho LA_1+(5/2)A_1=(3/2)L(Bx)$，其正权源 $(B_\rho)x+B(bv_\phi-d_\phi x)$ 同样只用到 $x$ 六阶、$v$ 七阶与 $d$ 七阶。因此 GPR 的两真实标签九阶和同点相关 $\omega$ 八阶已经足够；$A_2$、$k_2$、$\eta_{\rho\rho}$、$Z_{\rho\rho}$ 以及第十阶标签全部不在这个体强迫或端点中。原 $T_0,V_0,\vartheta$ 中的独立一次径向导仍由原真实片的一侧给出。紧支撑 $T_{\rm met}$ 和原高阶 scalar 模型容许 $k_1,B_\rho$ 的正规化计算。

$u,v$ 的实际 value repair 使其所有角导在真接缝连续，$d,d_\phi,b$ 连续；两真相位的角导、$Lx,Lv,Ls$ 由上述式连续。$G$ 的一阶径向与角导由平滑原 intrinsic $q$、连续 $\Pi S$ 和这些相位值导决定，故 $c_\sigma L_{-\sigma}w_0$ 及其任意已用角导连续。原 $R_\sigma$ 由分片有界强迫的特征积分定义，亦连续。于是各格中变换引入的边界项在共同物理接缝准确抵消。原 $U_\sigma$ 体强迫及 $R_{\sigma,r}$ 的有向跳仍须保留；此证明没有删除后续 genuine 残差的任何物理跳源。这里给出的是有符号等式，不从不同范数上界相减。
