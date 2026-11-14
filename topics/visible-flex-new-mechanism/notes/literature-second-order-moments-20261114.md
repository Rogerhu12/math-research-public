# 从等距对到固定度量路径：三矩与完整二阶相容性

**状态：已证明下述局部恒等式和线性化相容性引理；有限弯曲仅是待验证构造方案，课题未完成。** 本文只使用公开 Ghomi–Qiu–Raffaelli–Zhang, *Nonrigidity of smooth tight surfaces*（2026-11-12），<https://arxiv.org/html/2611.17269v1> §2 的带与无穷小弯曲公式，以及本会话的独立推导。以下引理不要求速度特殊取成 $v=V(\kappa)$；它对任意满足原文两个闭合条件的正光滑速度成立。

## 1. 约定及真正需要的二阶方程

$s\in\mathbb R/L_s\mathbb Z$ 是球面弧长，$B_s=N$, $T=-B\times N$，并有
$$T_s=\kappa N,\qquad N_s=-\kappa T-B,\qquad B_s=N.$$
令 $v=h^2>0$，$\alpha_s=vT$，$X(s,u)=\alpha(s)+uN(s)$，
$$w=v-\kappa u,\qquad E=w^2+u^2,\qquad
X_s=wT-uB,\quad X_u=N.$$
假设 $\alpha$ 周期，以及 $\oint\kappa_s/\sqrt v\,ds=0$。选周期原函数 $\omega_s=\kappa_s/(2h)$，取渐近坐标
$$\xi=\frac h u-\omega,\qquad u(s,\xi)=\frac h{\xi+\omega}.$$
本文只在正 $u$ 活动条带 $\xi\in[\ell,r]$ 工作，要求 $\ell+\omega(s)>0$。所有 profile 在 $[\ell,r]$ 光滑且两端的所有阶 jet 为零；也允许更强的 $C_c^\infty((\ell,r))$ 情形。按零延拓到稍大的几何工作区间后，profile 在这个更大区间的外侧 collar 恒零。

**理论与代码的支撑区别。** `kernel.profile` 使用 $\exp(1-1/(1-z^2))$（$|z|<1$，外为零），其支撑闭包恰为 $[\ell,r]$，严格说不属于 $C_c^\infty((\ell,r))$。它在活动条带内没有靠近端点的恒零开集，但端点所有 jet 都为零；在完整原 band 中的活动条带外仍有恒零开 collar。以下分部积分只用端点 jet 为零，线性化恢复也可按零延拓。因此数值固定活动边界 jet 与完整 band 固定外侧 collar 相容，不把二者写成同一句假设。

对 profile $\phi$，公开公式给
$$Y_\phi=P T+Q B,\qquad
P=-\frac u{2h}\phi'(\xi),\qquad
Q=u\phi(\xi)-\frac w{2h}\phi'(\xi).$$
记 $L_X Z=dX\cdot dZ+dZ\cdot dX$。固定目标度量
$$g_\varepsilon=g_X+\varepsilon^2dY_{\phi_0}\cdot dY_{\phi_0},$$
并尝试路径
$$F_{\varepsilon,t}=X+\varepsilon Y_{\phi_t}+\varepsilon^2Z_t+O(\varepsilon^3).$$
由于 $L_XY_{\phi_t}=0$，二阶必须且只需解
$$L_XZ_t=H_t:=dY_{\phi_0}\cdot dY_{\phi_0}-dY_{\phi_t}\cdot dY_{\phi_t}.$$
这允许 $Z_t$ 的一般三分量校正；不再要求 $F$ 留在 $X+$ 无穷小弯曲的仿射空间中。这里“二阶解”仍不等于对固定非零 $\varepsilon$ 的精确解。

## 2. 每条 ruling 的能量只依赖三个标量矩

固定 $s$，记 $z=\xi+\omega=h/u$，以及
$$A_\phi=\phi'-z\phi'',\qquad
B_\phi=\phi-z\phi'+\frac{z^2}{2}\phi''.$$
直接对 $u$ 求导得到
$$\partial_uY_\phi=-\frac{A_\phi}{2h}T+
\left(B_\phi+\frac\kappa{2h}A_\phi\right)B.$$
定义
$$J_0(\phi)=\int_\ell^r(\phi'')^2d\xi,\qquad
J_1(\phi)=\int_\ell^r\xi(\phi'')^2d\xi,$$
$$J_2^*(\phi)=\int_\ell^r\xi^2(\phi'')^2d\xi+
2\int_\ell^r(\phi')^2d\xi.$$

**引理 1（已证明）。** 沿整条活动 ruling，
$$\mathcal E_s(\phi):=
\int_{h/(r+\omega)}^{h/(\ell+\omega)}|\partial_uY_\phi|^2\,du$$
满足
$$\boxed{\mathcal E_s(\phi)=\frac h4J_2^*
 +\frac{h\omega-\kappa}{2}J_1
 +\left(\frac{h\omega^2}{4}-\frac{\kappa\omega}{2}
 +\frac{\kappa^2+1}{4h}\right)J_0.}$$

**完整的分部积分。** 因 $\phi$ 的所有端点 jet 为零，所有下列端项都为零。由 $du=-h z^{-2}d\xi$，需要三个积分。

首先，
$$\int\frac{A_\phi^2}{z^2}
=\int\left((\phi'')^2-\frac{2\phi'\phi''}{z}
 +\frac{(\phi')^2}{z^2}\right)=J_0,$$
其中 $-\int((\phi')^2)'/z=-\int(\phi')^2/z^2$，消去最后一项。

其次，展开 $A_\phi B_\phi/z^2$ 得
$$\frac{\phi\phi'}{z^2}-\frac{(\phi')^2}{z}
+\frac32\phi'\phi''-\frac{\phi\phi''}{z}
-\frac z2(\phi'')^2.$$
这里 $\int\phi'\phi''=0$，且
$$-\int\frac{\phi\phi''}{z}
=\int\frac{(\phi')^2}{z}-\int\frac{\phi\phi'}{z^2}.$$
故
$$\int\frac{A_\phi B_\phi}{z^2}
=-\frac12\int z(\phi'')^2=-\frac12(J_1+\omega J_0).$$

最后，
$$\frac{B_\phi^2}{z^2}=
\frac{\phi^2}{z^2}+(\phi')^2+\frac{z^2}4(\phi'')^2
-\frac{2\phi\phi'}z+\phi\phi''-z\phi'\phi''.$$
前后配对给
$\int(\phi^2/z^2-2\phi\phi'/z)=0$，
$\int((\phi')^2+\phi\phi'')=0$，以及
$-\int z\phi'\phi''=\frac12\int(\phi')^2$。于是
$$\int\frac{B_\phi^2}{z^2}
=\frac14\int z^2(\phi'')^2+\frac12\int(\phi')^2.$$
将这三个式子代回
$$\mathcal E_s=h\int\frac{B_\phi^2}{z^2}
 +\kappa\int\frac{A_\phi B_\phi}{z^2}
 +\frac{\kappa^2+1}{4h}\int\frac{A_\phi^2}{z^2}$$
即得引理。极化后，同一公式也适用于两个 profile 的双线性能量。

**含义。** 保持 $J_0,J_1,J_2^*$，就同时保持所有 $s$ 的 ruling 能量。这是二阶固定边界的一个可满足条件；并非完整的二阶充分条件。

## 3. 可以显式构造保持三矩的连续圆路径

取同一中心 $c=(\ell+r)/2$ 的四个线性无关偶 profile，均在两端平坦。记其有限维空间为 $V$，并定义双线性型
$$\mathsf A(f,g)=\int f''g'',\qquad
\mathsf B(f,g)=\int\xi^2f''g''+2\int f'g'.$$
$\mathsf A$ 正定；偶性使 $\int\xi f''g''=c\mathsf A(f,g)$。

取 $\mathsf A$ 正交归一的 $\mathsf B$ 广义特征基 $e_0,e_1,e_2,e_3$，特征值递增为 $\lambda_0\le\lambda_1\le\lambda_2\le\lambda_3$。在严格不等式的情形取 $\mu\in(\lambda_1,\lambda_2)$，令
$$f=\sqrt{\frac{\lambda_3-\mu}{\lambda_3-\lambda_0}}e_0
 +\sqrt{\frac{\mu-\lambda_0}{\lambda_3-\lambda_0}}e_3,$$
$$g=\sqrt{\frac{\lambda_2-\mu}{\lambda_2-\lambda_1}}e_1
 +\sqrt{\frac{\mu-\lambda_1}{\lambda_2-\lambda_1}}e_2.$$
则 $\mathsf A(f,f)=\mathsf A(g,g)=1$，$\mathsf B(f,f)=\mathsf B(g,g)=\mu$，两个型的交叉项都为零。因此
$$\phi_t=\cos t\,f+\sin t\,g,\qquad0\le t\le\pi$$
保持全部三个矩，并从 $f$ 连到 $-f$。退化特征值情形可在等值子空间直接取正交向量；数值脚本会显式报告特征值，而不隐藏分母退化。

这是一条**满足 ruling 二阶相容性的 profile 路径**，不是已构造的等距曲面路径。尤其初始 profile 已从旧核谱中的单个 bump 改成 $f$，这是另一次设计，不能和旧 $g_\varepsilon$ 混为同一个固定度量问题。

## 4. 完整线性化方程的必要充分周期条件

以下将一个给定光滑对称张量写成
$$H=H_E\,ds^2+2H_F\,ds\,du+H_G\,du^2,$$
并假设 $H$ 在活动条带两端所有 jet 为零，外延为零。求周期的 $Z=pT+\rho N+qB$，也要求其两端所有 jet 为零；将它在更大几何工作区间外延为零后，即固定完整 band 的外侧 collar。若采用更强的活动边界内侧开 collar 恒零假设，下面构造也保持这一更强性质。所有下标 $s$ 在未注明时表示固定 $u$ 的偏导数。

由标架方程，
$$Z_s=(p_s-\kappa\rho)T+(\kappa p+\rho_s+q)N+(q_s-\rho)B,
\qquad Z_u=p_uT+\rho_uN+q_uB.$$
$L_XZ=H$ 等价于
$$2\rho_u=H_G,$$
$$wp_u-uq_u+\kappa p+q=H_F-\rho_s=:\mathcal A,$$
$$wp_s-uq_s=\frac{H_E}{2}+(w\kappa-u)\rho=: \mathcal B.$$

第一式与下侧端点的 $\rho=0$ 唯一确定 $\rho$。它在上侧端点也为零，当且仅当
$$\boxed{\int_{h/(r+\omega)}^{h/(\ell+\omega)}H_G(s,u)\,du=0
\quad\text{对每个 }s.}\tag{C1}$$
对 §1 的二阶 $H$，引理 1 和三矩路径正好保证 (C1)。

令
$$\zeta=wp-uq=v p-u(\kappa p+q),\qquad
\eta=\kappa p+q.$$
第二式变成 $\zeta_u+2\eta=\mathcal A$，故
$$\eta=\frac{\mathcal A-\zeta_u}{2},\qquad
p=\frac{\zeta+u\eta}{v},\qquad q=\eta-\kappa p.$$
将其代入第三式，设
$$d=v_s-\kappa_su,\qquad
c_*=\frac{ud}{2v},\qquad D=\partial_s+c_*\partial_u,$$
便得
$$D\zeta-\frac d v\zeta=\mathcal B+c_*\mathcal A.$$
直接微分 $\xi=h/u-\omega$ 可知 $D\xi=0$；同时 $Du=c_*$，所以 $D(u^2)/u^2=d/v$。于是
$$\boxed{\left.\partial_s\right|_\xi W=\mathcal S(s,\xi),\qquad
W=\frac\zeta{u^2},\quad
\mathcal S=\frac{\mathcal B+c_*\mathcal A}{u^2}.}$$

**引理 2（已证明）。** 在以上正条带及端点平坦假设下，周期、两端平坦且可零延拓的 $L_XZ=H$ 有光滑解，当且仅当 (C1) 成立并且
$$\boxed{\mathcal P_H(\xi):=\oint\mathcal S(s,\xi)\,ds=0
\quad\text{对每个 }\xi\in[\ell,r].}\tag{C2}$$

必要性已经由逐步等价变换得到。反过来，(C1) 给两端平坦的光滑周期 $\rho$；于是 $\mathcal A,\mathcal B,\mathcal S$ 也在两端平坦。(C2) 允许对每条闭 $\xi$ 叶取 $\mathcal S$ 的周期原函数 $W$；例如规定它的 $s$ 平均值为零。这样 $W$ 在两端的各阶 $\xi$ 导数为零，且对 $\xi$ 光滑。用上面的公式恢复 $\zeta,\eta,p,q$，得到周期光滑且两端平坦的 $Z$，它可在活动条带外零延拓。不存在漏掉的空间位置单值差：$Z$ 已在周期标架中显式给成一个向量场。

因此“保持三个矩”仅处理 (C1)；(C2) 是剩下的一个函数值周期障碍，必须实际求零。不能因为 (C1) 已简化为三条等式就把整个二阶问题当成三条等式。

## 5. 圆路径只需检验两个二阶 forcing 通道

设 $Y_f,Y_g$ 对应 §3 的两个 profile。因为
$$dY_f^2-dY_{\phi_t}^2
 =\sin^2t\,H^{(d)}+\sin t\cos t\,H^{(c)},$$
其中
$$H^{(d)}=dY_f^2-dY_g^2,\qquad
H^{(c)}=-(dY_f\cdot dY_g+dY_g\cdot dY_f),$$
只需检查 $H^{(d)},H^{(c)}$ 两个通道的 (C2)。两者的 (C1) 由三矩及交叉正交同时保证。若两通道均通过，可求 $Z_d,Z_c$，并取
$$Z_t=\sin^2t\,Z_d+\sin t\cos t\,Z_c.$$
这时 $Z_0=Z_\pi=0$，与已知 $F_\pm=X\pm\varepsilon Y_f$ 端点一致。

对固定非零 $\varepsilon$，当前截断路径的误差仍含
$$\varepsilon^3(dY_{\phi_t}\cdot dZ_t+dZ_t\cdot dY_{\phi_t})
+\varepsilon^4dZ_t^2.$$
所以第三阶需解
$$L_XZ_{3,t}=-(dY_{\phi_t}\cdot dZ_t+dZ_t\cdot dY_{\phi_t}),$$
第四阶需解
$$L_XZ_{4,t}=-(dZ_t^2+dY_{\phi_t}\cdot dZ_{3,t}
+dZ_{3,t}\cdot dY_{\phi_t}).$$
各阶仍要满足 (C1),(C2)。低阶校正可加入任意原核场 $Y_\chi$，这些自由函数会进入下一阶相容性，应作为可调未知量，而不能把某个零均值选取下的高阶失败当成一般不存在。

## 6. 实际数值计划及完成边界

先在本公开仓库 Actions 中用固定的参考求积定义 profile 基、广义特征向量、归一化、$\ell,r$ 和 $\varepsilon$；之后独立加密 $s,\xi$ 节点。记录两个通道的 ruling 总积分、函数 $\mathcal P_H(\xi)$、恢复 $Z$ 后的完整 $L_XZ-H$、collar jet 残差。若 (C2) 非零，要优化更多 profile 系数使两个函数通道为零，不能用减去周期均值冒充解；若为了诊断减去均值，必须同时保留原非零均值。

只有二阶稳定通过以后，才沿这些校正预测值对**同一个固定 $g_\varepsilon$**做完整度量 Newton 校正，并逐步沿 $t$ 延拓。缩小 $\varepsilon$ 所获得的高阶误差变小不算完成标准的固定参数加密收敛。即使得到精确有限带族，还需要嵌入到闭曲面、握持区、大位移和全程 reach；这里一项都没有先行宣称完成。
