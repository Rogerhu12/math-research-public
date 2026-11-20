# R138 补篇：更紧的完整外端提升与截顶曲率能量

2026-11-20，visible-exact-astra-ac637-20261120。

本篇给新的解析界，没有执行数值目标或重算 X/Y 的已成量。仍取同一
Qrepair、真实物理角、固定 `p=e_z/2`、同一个周期方向提升；全部 mean、
原全频 exterior graph 与真实径向区间不变。能量、`H,ω` 和
`C_E,C_H,A_Θ,Γ` 沿用 [V 补篇](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)。
圆周积分与范数同 V 使用非归一化 measure，除非明确标 normalized。

## 1. 从旧曲率证书得到更强的全域下界

令 `x=r−r_*`、`L=25/8−r_*`、`δ=1/1840`。旧 scalar 曲率证书已给
`K'>46` 于 `[.238,.239]`，`K>1/40` 于 `[.239,25/8]`，全部接口连续且
`K(r_*)=0`。原完整真根区间直接给

\[
r_{*,+}+1/1840<239/1000,\qquad 14/5<L<29/10.
\tag{Z.1}
\]

在 `0≤x≤δ`，积分同一真实 `K'` 得 `K≥46x`。在
`r_*+δ≤r≤.239`，仍有 `K≥46δ=1/40`；后续使用原已成正下界。因此

\[
\boxed{K(r)\ge k_{\rm cap}(x):=\min\{46x,1/40\}}
\quad(0\le x\le L).
\tag{Z.2}
\]

没有把真根替换为区间端点，也未假定证书区间以外的 `K` 单调。
这是既有结论的解析消费，不产生新的 curvature target。

## 2. 合并完整两列后再取外端旋转范数

采用 [O 补篇](R138-supplement-actual-outer-rotation-energy-and-mean-defect.md)
的同一个圆锚

\[
X=t e_r+z e_z,\quad Y=e_\theta,\quad t^2+z^2=1,\quad
b=\sum_{n\in4\mathbb N}b_n\sin n\theta,\quad
c=c_0+\sum_{n\in4\mathbb N}c_n\cos n\theta .
\]

写 `N=||c_perp||_(H^(-1/2),normalized)`。同一真实 exterior graph 已付

\[
\|b\|_{H^{-1/2}}\le(4001/4000)N,\qquad |c_0|\le N/32000.
\tag{Z.3}
\]

对每个非 mean 模先合并 `V_n=b_n sin(nθ)Y−c_n cos(nθ)X`。
由同一 frame 的 `X⊥Y`，

\[
\|V_n\|_{L^2_{\rm normalized}}^2=(b_n^2+c_n^2)/2.
\tag{Z.4}
\]

该环境向量的 Fourier 频率仅为 `n−1,n,n+1`，故完整向量 primitive
`I_(2π)` 对这一模的 `L²` 范数至多 `1/(n−1)`。不同 `n∈4N` 的频率集合
不交，mean 提升的非零环境频率1也与之不交；经过 primitive 后各组仍正交。
这没有将同模未知 `b,c` 的输出列分别视为正交，也没有把环境 primitive
的全局 norm 改成 `1/4`。

`sqrt(1+n²)/(n−1)²` 在 `n>1` 单调递减，其 `n≥4` 最大值是
`sqrt(17)/9<11/24`。独立 mean 的旋转为 `a t c_0Y`。所以

\[
\begin{split}
\|\omega_R\|_{L^2_{\rm normalized}}^2
&\le a^2\left\{\frac{\sqrt{17}}9
      \big(\|b\|_{H^{-1/2}}^2+N^2\big)+c_0^2\right\}\\
&\le a^2\left\{\frac{11}{24}
      \left(1+\left(\frac{4001}{4000}\right)^2\right)
      +\frac1{32000^2}\right\}N^2
<\frac{15}{16}a^2N^2 .
\end{split}
\tag{Z.5}
\]

[T.3](R138-supplement-exact-residual-transport-and-fixed-interior-point.md)
已对同一个固定 `p` 给 `B=−Btilde_R≥2πa²s_RN²`、`s_R>2/5`。
把 normalized 范数乘回 `2π`，

\[
\boxed{\|\omega_R\|_2^2<\frac{75}{32}\mathcal B
             <\frac{64}{25}\mathcal B,\qquad
       \|\omega_R\|_2\le\frac85\sqrt{\mathcal B}.}
\tag{Z.6}
\]

零方向使用非严格式。物理 mean 在 (Z.3)–(Z.5) 中保留；
原 `||H_R||₂≤sqrt(B)/20000` 与 `P_R=0` 不变，
真实外图的输入空间没有缩小。

## 3. 两个受控方向的直和先用 Minkowski

沿 V 记 `vartheta=Theta_phi=v/m`、`w=omega∘Theta`、
`D_w=∂r−d∂phi`、`κ=Kv²`、`δ_c=b−uc`。准确有

\[
\begin{split}
D_w w&=\{e[-\delta_cX+(u\delta_c-\kappa c)Y]
                      -\gamma uH\}\circ\Theta,\\
\sqrt K\,w_\phi&=\{\sqrt K\,\vartheta(W+H)\}\circ\Theta .
\end{split}
\tag{Z.7}
\]

将右侧的 `W,b,c` 部分放入一个 Hilbert 直和向量，`H` 部分放入另一个。
保真 Jacobian `dphi=dtheta/vartheta`，V.11 的同一两个已付系数给两向量
平方范数分别不超过 `C_E E` 和 `C_H||H||₂²`。在整个 `(r,phi)` 直和先用
Minkowski，准确得到

\[
\boxed{\left(\|D_w w\|_2^2+\|\sqrt K\,w_\phi\|_2^2\right)^{1/2}
 \le \sqrt{C_E}\sqrt{\mathcal E}+\sqrt{C_H}\|H\|_2.}
\tag{Z.8}
\]

不必先用 `(a+b)²≤2a²+2b²`。同一个 whole-circle drift flow
`psi_r=−d(r,psi), psi(R)=id`、`v_*=w∘psi` 的 Jacobian 与逆 Jacobian
由旧 `Γ` 控制。(Z.2)、(Z.8) 遂给

\[
\boxed{
\mathfrak G_{\rm cap}^{1/2}
:=\left[\int\big(|(v_*)_r|^2+k_{\rm cap}(x)|(v_*)_\xi|^2\big)\right]^{1/2}
\le\sqrt\Gamma\big(\sqrt{C_E}\sqrt{\mathcal E}+\sqrt{C_H}\|H\|_2\big).
}
\tag{Z.9}
\]

两项换元同时受 `Γ` 控制，没有再多加平方和因子。旧 `H` 的 Volterra 界
与 `Γ/A_Θ/C_E/C_H` 完整保存球均可只读，不重算其成功目标。

## 4. 后继 body H^(1/2) 不等式的准确消费

若另一完整证明对全部根端自由环境向量给

\[
\|z\|_{L^2_xH^{1/2}_\xi}
 \le A_G\,\mathfrak G_{\rm cap}(z)^{1/2}+B_G\|z(L)\|_2,
\tag{Z.10}
\]

且旧 whole saved 球给 `||H||₂≤h_E sqrt(E)+h_B sqrt(B)`，
则 V.15 的两次一阶 composition 与 (Z.6)、(Z.9) 给

\[
\|\omega\|_{L^2_rH^{1/2}_\theta}
\le w_E^{(1/2)}\sqrt{\mathcal E}+w_B^{(1/2)}\sqrt{\mathcal B},
\]
\[
\begin{split}
w_E^{(1/2)}&=A_G\Gamma\sqrt{A_\Theta}
                    (\sqrt{C_E}+\sqrt{C_H}h_E),\\
w_B^{(1/2)}&=A_G\Gamma\sqrt{A_\Theta C_H}\,h_B
                       +\tfrac85B_G A_\Theta\sqrt\Gamma .
\end{split}
\tag{Z.11}
\]

用已成 Y 的完整 `E_0,E_1,h_E` 和 X 不变量可另定义三个新 body 系数

\[
\begin{split}
a_{EE}^{\rm new}&=E_0(w_E^{(1/2)})^2+E_1w_E^{(1/2)}h_E,\\
a_{EB}^{\rm new}&=2E_0w_E^{(1/2)}w_B^{(1/2)}
                   +E_1(w_E^{(1/2)}h_B+w_B^{(1/2)}h_E),\\
a_{BB}^{\rm new}&=E_0(w_B^{(1/2)})^2+E_1w_B^{(1/2)}h_B .
\end{split}
\tag{Z.12}
\]

(Z.10) 常数及 (Z.11)–(Z.12) 的实际新球须另付；本文未计算这些量。
这只替 body `H^(1/2)` 费用，不免费获得 V 的 `H^(2/3)` 体界、
`H^(1/3)` 根迹或 `H^(-1/3)` 根缺陷新费用。真实根型仍保有限/high、
独立 mean 与非齐次 `H`；完整吸收门、全频逆和总课题未因此闭合。

