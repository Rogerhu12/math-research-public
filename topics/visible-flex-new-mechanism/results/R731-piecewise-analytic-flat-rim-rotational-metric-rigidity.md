# R731　平端旋转度量的有限分段解析等距浸入必同轴

设 $0<r_0<r_1$，材料度量为 $g=m(r)^2\,dr^2+r^2\,d\varphi^2,\ m>0$，外圈以真实平环的一阶数据固定为 $F(r_1,\varphi)=C_1+r_1 e_r(\varphi),\ F_r=e_r,\ F_\varphi=r_1 e_\varphi$。假设 $F$ 是全带 $C^2$ 的准确等距浸入，外圈贴合真平环的两阶数据。允许有限个径向结；在每个闭径段，$F$ 在固定材料 $(r,\varphi)$ 有单侧实解析延拓至端点，内部实解析。$m$ 亦由 $|F_r|$ 获得相应单侧解析性。所求结论为
$$
       F(r,\varphi)=C(r)+r e_r(\varphi),\qquad C'(r)\parallel e_z .
$$
因此真实内圈平面不可能相对外圈倾转。证明无需嵌入性、反射对称、完整壳或任何小变形假设。

## 准确材料标架

取 $P=F_r/m,\ T=F_\varphi/r,\ n=P\times T,\ h=1/m,\ b=m/r$。设 $a=P_r\cdot n,\ \ell=P_\varphi\cdot n,\ k=T_\varphi\cdot n$。由正交单位标架和 $\partial_\varphi(mP)=\partial_r(rT)$ 得
$$
 P_r=an,\quad T_r=b\ell n,\quad
 P_\varphi=hT+\ell n,\quad T_\varphi=-hP+kn .
$$
确实，微分 $P\cdot P=1$ 和 $T\cdot T=1$，兼容式先给 $P_\varphi\cdot T=h,\ T_r\cdot P=0$，从而 $P_r\cdot T=0$。比较 $P_{r\varphi},P_{\varphi r}$ 的 $T,n$ 分量和 $T_{r\varphi},T_{\varphi r}$ 的 $n$ 分量，得到 [R687](R687-global-darboux-frames-with-quantitative-periodic-immersion-reconstruction.md) 在径向度量下的准确方程
$$
 h'=b\ell^2-ak,\qquad k_r=ha+b\ell_\varphi,\qquad
 \ell_r=a_\varphi-\ell/r .                                                     \tag{1}
$$
这里撇为材料 $r$ 导，所有 angular 导在真正的材料 $\varphi$。外平圈有 $h=1,k=\ell=0$。在 $C^2$ 的径结，标架的上述一阶数据连续。

## 零纬向法曲率时的单侧展开

设一侧从 $r=r_*$ 的 $k=\ell=0$ 出发。记 $z=r-r_*$，用 $f_j(\varphi)$ 表 $z^j$ 的系数。若 $a$ 的所有径系数恒零，单侧解析性令 $a=0$ 于邻域；(1) 给 $(r\ell)_r=0$, $k_r=0$，故 $\ell=k=0$、$h'=0$。若 $a_p$ 是首个非恒零系数（$p$ 可为零），由后两式逐阶积分得
$$
 k_{p+1}=h_0a_p/(p+1),\qquad \ell_{p+1}=\partial_\varphi a_p/(p+1),
$$
前面的系数各为零。Gauss 式的 $z^{2p+1}$ 项是 $-h_0a_p^2/(p+1)$，因 $h$ 径向，这一项在整圈恒定。$h_0>0$、圆连通、$a_p$ 连续实值且不恒零，故 $a_p$ 是同一个非零常数。

若存在角向非常数的系数，令 $j>p$ 为 $a_j$ 中的首个。由 (1)，$\ell$ 从 $z^{j+1}$ 才可能非零，$k$ 的系数至 $j$ 均为角常数，$k_{j+1}$ 的非恒部分为 $h_0(a_j)_{\rm nc}/(j+1)$。在 $z^{p+j+1}$ 的 Gauss 式中，$b\ell^2$ 没有贡献，$-ak$ 的非恒部分准确是
$$
  -h_0a_p\left(\frac1{p+1}+\frac1{j+1}\right)(a_j)_{\rm nc}.
$$
其中更高的 $a$ 或 $k$ 系数因对方的首项阶数不能进入，其余低项恒定。这与径向 $h'$ 矛盾。故整个单侧 $a,k$ 轴对称，$\ell=0$。该推导未除以零点的 $k$，同时包含首个真实法曲率发生在高阶和整段全平两种情况。

## 径结传递与真实端姿

单侧实际解析性把上述全部系数结论提升到开邻域，解析恒等定理再使 $a_\varphi=k_\varphi=\ell=0$ 贯穿该径段。下一径结若 $k=0$，前侧已给 $\ell=0$，可直接重用零端证明；若 $k\ne0$，前侧给常数 $k_0$ 和 $\ell_0=0$，从新侧使用
$$
         a=(b\ell^2-h')/k .
$$
此式此时分母在邻域离零。已知 $k,\ell$ 至阶 $j$ 的系数，就由该式得到 $a$ 至阶 $j$；后两条 (1) 再给 $k,\ell$ 至阶 $j+1$。从常数 $k_0,\ell_0=0$ 出发，新侧每阶 $a,k$ 恒定、$\ell$ 为零；$h'$ 始终取新侧自己的径向函数。这样有限次传递到内圈。$T_r=b\ell n=0$，于是 $T=e_\varphi$，按角积分便有 $F=C(r)+r e_r$，再由 $g_{r\varphi}=0$ 得 $C'$ 垂直整个外平面。结论得证。

[R726](R726-closed-spinor-fourier-and-complete-common-metric-residuals.md) 在正立体分母及 $J>0$ 下具有分段有理的辅助角 Fourier 系数，材料角局部解析逆由 $\Phi_\psi=J>0$ 保证，因此每一个有限径分区的多项式参数场满足本定理的解析假设。对非零倾角，这些场均不能给出准确零残差。本结论没有给随阶数、结数或高导数统一的正误差下界。有限 $\eta$ 的真实数据、固定一条 $E$ 后的实际精化和极限族的 $C^2$ 资格仍须分别核；一列解析场的 $C^2$ 极限可以不解析。因此本定理不取消 R728 的实际数值输入。

## 附录：有限阶离开外平圈的光滑解也在外领同轴

此节仅断言一个外领。现令实际 $F,m$ 在外圈单侧 $C^\infty$，设 $a$ 有有限阶首个非零径 jet $p$。前述系数论证只用有限次数微分，所以仍给 $\ell$ 和 $k$ 的非轴对称部分在外圈无穷阶平；所有涉及的角导在紧圈上一致平。令 $x=r_1-r>0$。Gauss 首项给 $h'\asymp x^{2p+1}>0$。由 (1)，
$$
 (h^2+k^2)'=2hb\ell^2+2kb\ell_\varphi ,
$$
其右边无穷阶平，且外端 $h^2+k^2=1$。取 $k_0$ 为与实际首项同号的 $\pm\sqrt{1-h^2}$，可写成 $x^{p+1}$ 乘非零光滑函数；$k-k_0=(h^2+k^2-1)/(k+k_0)$ 及所需各阶角径导均无穷阶平。

写 $u=k-k_0,\ A=(h'-b\ell^2)/k^2,\ D=2b\ell/k$。足够靠外时 $A\asymp1/x>0$、$|A_r|/A=O(1/x)$，$A_\varphi,D_\varphi$ 无穷阶平。只在这个 $k\ne0$ 的开外领内用 Gauss 解 $a$，与 $k_0'=-hh'/k_0$ 相减，得
$$
 u_r=b\ell_\varphi+\frac{hh'}{kk_0}u+\frac{hb\ell}{k}\ell,\qquad
 \ell_r=A u_\varphi+D\ell_\varphi-\ell/r .
$$
对称化能量 $\mathcal E=\int(Au^2+b\ell^2)\,d\varphi$。输运矩阵乘 $\operatorname{diag}(A,b)$ 后是对称矩阵，其角导中的 $(Ab)_\varphi,(bD)_\varphi$ 都平；周期分部积分控制输运项。其余项中 $hh'/(kk_0)=O(1/x)$，$b$ 及 $b^{-1}$ 有界，$hb\ell/k$ 平，故 $|\mathcal E_r|\le C\mathcal E/x$。对 $0<x_0<x$，Gronwall 给 $\mathcal E(x)\le (x/x_0)^C\mathcal E(x_0)$。$\mathcal E(x_0)=O(x_0^N)$ 对所有 $N$ 成立，令 $x_0\downarrow0$ 得整外领 $\mathcal E=0$。该结论不跨越未知的内侧变型点，不适用于未经证明正则性的任意 $C^2$ 极限，也不处理 $a$ 本身在外端无穷阶平但内部不为零的情形。
