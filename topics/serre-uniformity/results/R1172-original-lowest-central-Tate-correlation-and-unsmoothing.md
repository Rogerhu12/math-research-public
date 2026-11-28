# R1172：原最低中央槽的完整 Tate 修正、同源群图与算术未平滑

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126。

**已证明下述原群、整上链及同源功能式；最低相关项的独立局部数值读取仍开放。** 本篇始终保留原 $\lambda_\infty$、圆单位 $\gamma_5$ 与全部根相位。没有把已构造的原 torsor 再命名为一个已知数值。

## 1. 同一个最低 quotient 与两种整尺度

沿 [R1147 §§10–11、18](R1147-original-canonical-moment-Heisenberg-lift.md)，令
$$
A=\operatorname{Sym}^4\mathcal H(1),\quad
B=\operatorname{Sym}^8\mathcal H(1),\quad
T=\mathbb Z_p(5),\quad Z=\operatorname{Sym}^4\mathcal H(6).
$$
原最低中央 quotient 的有序群律是
$$
\mathfrak b_4((x,y,t),(x',y',t'))
 =\Pi_4(x,y')+\lambda_\infty x\,t',
\quad
\lambda_\infty=\frac{21}{11}(1+p^4),
\quad
\Pi_4(v^4,w^8)=\langle v,w\rangle^4w^4.
\tag{1172.1}
$$
原 quotient cocycle 为 $(a,b,c)=(a_4,a_8,\gamma_5)$，且
$$
\Omega_4=\Pi_4(a\cup b)+\lambda_\infty a\cup c
\tag{1172.2}
$$
在完整算术 $\mathcal M=\mathcal M_{1,1,\mathbb Q}$ 的 $H^2$ 中为零。原 compatible tower 及其唯一 Hodge 点均沿 R1147、R1163 保留。

为避免将第一层的等式误用到高层，另记
$$
u_4=1-p^4,\quad u_8=1-p^8,\quad
\widetilde c=u_4^{-1}c,\quad \lambda_0=\frac{21}{11}.
$$
全部非零点的原矩用 $\widetilde a,\widetilde b$；原 primitive 矩用 $a,b$。真实群同构为
$$
(x,y,t;z)\longmapsto
(u_4x,u_8y,u_4t;\ u_4u_8z),
\qquad
u_4^2\lambda_\infty=u_4u_8\lambda_0.
\tag{1172.3}
$$
同根的零次 gauge 仍按 R1147 (1147.64)–(1147.65) 作用；它在最低中心包含 $\lambda_\infty$ 项。以下先在 primitive 规范证明，§5 再列原未缩放 theta 规范。

## 2. 实际同源运输连常 Tate 槽一起保留

取已有实际来源的辅助数 $n=2$ 或 $3<n<p$。在需除 $k_4(n)$ 时假设它是 $\mathbb Z_p$ 单位；本篇可始终取 $n=2$，所以不引入新的大素数例外。所有 theta 根、Norm 及 cochains 均消费 R1157–R1159 已建立的实际来源，不向 $n\ge p$ 外推。

设 $\phi_C:E\to E/C$ 为原 cyclic-$n$ quotient，令
$$
f_C=\psi_C^{-1}=n^{-1}\phi_C^*.
$$
原 Weil 配对满足
$$
\langle f_Cv,f_Cw\rangle=n^{-1}\langle v,w\rangle.
$$
因此把整个最低 quotient 从 $E/C$ 运输到 $E$ 的群态射，必须同时用
$$
x_C=\operatorname{Sym}^4 f_C(x),\quad
y_C=\operatorname{Sym}^8 f_C(y),\quad
t_C=n^{-4}t,\quad
z_C=n^{-4}\operatorname{Sym}^4 f_C(z).
\tag{1172.4}
$$
四次 Weil 收缩给 $n^{-4}$；$\lambda_\infty x\,t'$ 的两个输入也给同一 $n^{-4}$。所以 (1172.4) 保持完整 ordered 群律。只运输 $A,B$ 而让 Tate-five 槽不变会破坏这一等式。

$t_C=n^{-4}t$ 是原 $T$-torsor 的指定单位倍，不是改选圆单位。商曲线上的 $c$ 原本是同一个从基域拉回的 $\gamma_5$；同一兼容根在 (1172.4) 下给 $n^{-4}c$，于是各槽与基槽之间的差有一个指定的零 trivialization。

## 3. 保完整中心的 product 与真实 Norm reduction

作原最低 torsors 的真实 product/Weil restriction，中心暂保为
$$
Z_{\rm big}=Z\oplus\operatorname{Res}_{C}Z.
$$
其交换商坐标为 $(x_0,y_0,t_0;(x_C,y_C,t_C)_C)$。用原 theta Norm 点及上一节 Tate 的指定标识，约束
$$
\sum_Cx_C=(n+n^{-4})x_0,\qquad
\sum_Cy_C=(n+n^{-8})y_0,\qquad
t_C=n^{-4}t_0\quad\text{对每个 }C.
\tag{1172.5}
$$
取这些线性方程的 kernel 在 product 群中的逆像 $G_H$，沿已给的 quotient 点拉回原 product torsor。中心仍是全部 $Z_{\rm big}$。该 reduction 不反除 $n+1$，也不先删任何中央槽。

置
$$
k_d=n^2-n^{-d},\qquad s_n=n^4+n^{-11}.
$$
到 correlation 交换商的 map 为
$$
X=k_4x_0,\quad Y=k_8y_0,\quad
X_C'=nx_C-n^{-4}x_0,\quad
Y_C'=ny_C-n^{-8}y_0,\quad T_0=t_0.
\tag{1172.6}
$$
中心 map 仍取
$$
\mu(z_0;(z_C))=s_nz_0-n^2\sum_Cz_C.
\tag{1172.7}
$$

定义准确标量
$$
\begin{aligned}
v_{n,4}
 &=s_n-n^{-2}(n+n^{-4})\\
 &=n^4+n^{-11}-n^{-1}-n^{-6}
 =n^{-11}(n^5-1)(n^{10}-1),\\
\kappa_n&=\lambda_\infty\,\frac{v_{n,4}}{k_4}.
\end{aligned}
\tag{1172.8}
$$
新的 correlation 群使用完整有序 bilinear law
$$
\mathfrak b^{\rm corr}_{n,4}(v,w)
 =\Pi_4(X(v),Y(w))
  -\sum_C\Pi_4(X_C'(v),Y_C'(w))
  +\kappa_n X(v)\,T_0(w).
\tag{1172.9}
$$
各 map 均为 (1172.6) 的实际槽，两个输入分别为 $v,w$。未分裂时中间项是同一子群内先相乘再 trace。

对两个独立 $v,v'\in H$，前两项按 R1159 (1159.25) 的完整展开恰为 $\mu$ 作用于 product 的 $\Pi_4$ 部分，因为该展开只使用双线性及 (1172.5)。Tate 部分则逐项为
$$
\begin{aligned}
\mu\!\left(\lambda_\infty x_0t_0';
              (\lambda_\infty x_Ct_C')_C\right)
 &=\lambda_\infty
   \left(s_nx_0-n^{-2}\sum_Cx_C\right)t_0'\\
 &=\lambda_\infty v_{n,4}x_0t_0'
 =\kappa_n X\,T_0'.
\end{aligned}
\tag{1172.10}
$$
故
$$
\boxed{\quad
\mathfrak b^{\rm corr}_{n,4}(\lambda v,\lambda v')
 =\mu\bigl(\mathfrak b_{\rm big}(v,v')\bigr).
\quad}
\tag{1172.11}
$$
因此 $(v,z)\mapsto(\lambda v,\mu z)$ 是真实群态射。没有额外的中央二次 map，也没有只核反对称 bracket 后就宣群同态。

这已经给出一个真实 correlation torsor。下一节给不以未知原中央 cochain 为输入的指定算术构造，并将所有 Norm/crossed 修正列出。

## 4. 原 Tate 修正的完整 crossed 上链

使用 [R1159 §§1–3](R1159-original-correlation-to-Hecke-cochain-comparison.md) 的同一右陪集、原根及
$$
T_na=(n+n^{-4})a+d\eta_4,\qquad
T_nb=(n+n^{-8})b+d\eta_8.
\tag{1172.12}
$$
先以实际 $\rho_4,\rho_8,\rho'_4,\rho'_8$ 将 raw quotient 完整 gauge 到
$$
(k_4a,k_8b;\ na^C-n^{-4}\operatorname{res}a,\
nb^C-n^{-8}\operatorname{res}b;\ c).
\tag{1172.13}
$$
中央 gauge 按 (1172.9) 一并执行；特别不能省掉由 $\rho_4$ 与 $c$ 产生的项。

令 $J_n^{\Pi_4}$ 是原 R1159 (1159.14) 的同一三行公式，将 coefficient map $\Pi_0$ 换为已校准的 $\Pi_4$：
$$
\begin{aligned}
J_n^{\Pi_4}
={}&n^{-7}\Pi_4\{\eta_4\cup b+R_{a^C,b}\}\\
 &+n^{-3}\Pi_4\{-a\cup\eta_8+L_{a,b^C}\}
       -n^{-12}\Pi_4K_{a,b}.
\end{aligned}
\tag{1172.14}
$$
这里所有 $R,L,K$ 都是原实际陪集的有限和，并非新的选择。

还需要一条原 projection formula。对全局 $c$，置
$$
w_t=t^{-1}c(t),\qquad
R_{a^C,c}(g)=\sum_t t^{-1}a^C(h_{t,g})\otimes g w_{t_g}.
$$
同一个 (1159.4) 给
$$
\operatorname{Cor}(a^C\cup\operatorname{res}c)
 =(T_na)\cup c+dR_{a^C,c}.
\tag{1172.15}
$$
这是 $A\otimes T\to Z$ 的原乘法；未假设任意陪集都在几何群中，也没有先令 $R_{a^C,c}=0$。

记中心 correspondence 的整链 map 为
$$
T_n^{Z}=\operatorname{Cor}\left(n^{-4}
                       \operatorname{Sym}^4f_C\right),
\qquad
\mathcal V_{n,4}=s_n-n^2T_n^{Z}.
\tag{1172.16}
$$
它在 Frobenius coefficient 函数上是 $s_n-n^{-2}T_n^{(4)}$。由 (1172.12)、(1172.15)，准确有
$$
\mathcal V_{n,4}(a\cup c)
 =v_{n,4}a\cup c
   -n^{-2}d\{\eta_4\cup c+R_{a^C,c}\}.
\tag{1172.17}
$$
所有系数都保留真实的 $n^{-4}$ Tate 运输。

(1172.13) 的实际 corrected cup 是
$$
\begin{aligned}
\Omega_{{\rm corr},4}
={}&\Pi_4(k_4a\cup k_8b)\\
&-\operatorname{Cor}\Pi_4\{(na^C-n^{-4}\operatorname{res}a)
             \cup(nb^C-n^{-8}\operatorname{res}b)\}\\
&+\kappa_n k_4\,a\cup c.
\end{aligned}
\tag{1172.18}
$$
将原 $\Pi_4$ 展开与 (1172.17) 合并，得到完整一次修正
$$
\boxed{\begin{aligned}
J_{n,4}
 &=J_n^{\Pi_4}
      +\lambda_\infty n^{-2}
                 \{\eta_4\cup c+R_{a^C,c}\},\\
\Omega_{{\rm corr},4}
 &=\mathcal V_{n,4}\Omega_4+dJ_{n,4}.
\end{aligned}}
\tag{1172.19}
$$
附加项的号是正：$\mathcal V_{n,4}(a\cup c)$ 在 (1172.17) 中带负的 exact 项，而 correlation 使用 $\lambda_\infty v_{n,4}a\cup c$。

由原 $[\Omega_4]=0$，(1172.19) 给 $[\Omega_{{\rm corr},4}]=0$。于是可直接用 [R1160 §8](R1160-original-explicit-arithmetic-descent-and-unsmoothing.md) 的实际连续算术构造，定义
$$
h_{{\rm corr},4}=-\mathcal B_{4,6}(\Omega_{{\rm corr},4}),
\qquad
h_{\mathcal V,4}=h_{{\rm corr},4}+J_{n,4}.
\tag{1172.20}
$$
$\mathcal B_{4,6}$ 的输入仅是显示的原 abelian/root/cyclotomic cochains；不含一个待定 $Z_4(E)$。它给 $dh_{\mathcal V,4}=-\mathcal V_{n,4}\Omega_4$。原全 $\mathcal M$ 上 $H^0(Z)=H^1(Z)=0$ 只在两个真实 lifts 已构造且 quotient 已固定之后使用，识别 (1172.20) 与 §3 的 product pushout。

## 5. 辅助数二的全部整常数

对 $n=2$，
$$
k_4(2)=\frac{63}{16},\qquad
v_{2,4}=\frac{3\cdot11\cdot31^2}{2^{11}},\qquad
\boxed{\ \kappa_2=\frac{31^2}{128}(1+p^4).\ }
\tag{1172.21}
$$
这三个数在所有 $p>37$ 都是单位。这里 $\kappa_2$ 用的是 primitive-normalized raw 四次、八次矩以及原 $c=\gamma_5$。

若直接使用原全部非零点的 theta 矩，不先乘 $u_4,u_8$，则必须同步保留：
$$
\boxed{\begin{array}{c|c}
\text{实际 Tate 槽}&\text{对应原 raw bilinear 系数}\\ \hline
\widetilde c=u_4^{-1}c & \widetilde\kappa_2=31^2/128\\
c=\gamma_5 & \widehat\kappa_2=31^2/(128u_4).
\end{array}}
\tag{1172.22}
$$
由 (1172.3)，$u_4^2\kappa_2=u_4u_8\widetilde\kappa_2$；把 $\widetilde c$ 换成 $c/u_4$ 则得到第二行。这两种等式都是整塔等式，约模 $p$ 后才共同成为 $31^2/128$。不能先省掉 $1+p^4$ 后仍宣原高层兼容。

## 6. 原未平滑 primitive 与真正的功能方程

R1160 §8 的原 residue 截面在 $(d,t)=(4,6)$ 给 $T_n^{(4)}$ 的几何 $H^1$ 标量 $n+n^{-4}$，Tate 额外 $n^{-4}$ 与 (1172.16) 一致；绝对 Hochschild–Serre 运输给同一个 $v_{n,4}$。定义
$$
B_{n,4}=\mathcal B_{4,6}
          \bigl((\mathcal V_{n,4}-v_{n,4})\Omega_4\bigr).
$$
便有
$$
\boxed{\quad
h_4=\frac{h_{{\rm corr},4}+J_{n,4}+B_{n,4}}{v_{n,4}},
\qquad dh_4=-\Omega_4 .
\quad}
\tag{1172.23}
$$
可始终取 $n=2$。每个 map、单位逆和原 $\mathcal B$ 都与约化相容，因此 (1172.23) 给同一个原 compatible tower，随后用完整 $\mathcal M$ 上的唯一性识别原最低 quotient。未在局部场上使用该唯一性。

另一方面，§3 的实际 product/Norm/reduction 群态射在同一 filtered realization 中保持唯一 Hodge 点。因此直接读取 Frobenius 得
$$
\boxed{\quad
Z_{{\rm corr},4}(E)
 =(n^4+n^{-11})Z_4(E)
  -n^{-2}\sum_C\operatorname{Sym}^4(\psi_C^{-1})Z_4(E/C).
\quad}
\tag{1172.24}
$$
由于 (1172.11) 是两个独立输入的 ordered 身份，把两边全部改成 BCH 中央坐标时仍是同一式，无需删除或猜测任何二次项。

(1172.23) 与 (1172.24) 分别是原连续算术 primitive 和真正跨同源的值式。前者的 $v_{n,4}$ 不能代替后者作用于全部实际曲线的算子。

## 7. 为什么不能照搬前两个槽的 S/U filling

在原 Manin 系数中，$\Pi_4(v^4,w^8)$ 的不变配对因子为 $\langle v,w\rangle^4$，剩余 degree-four 多项式为 $f(X,Y)=Y^4$。对任意 degree-four $P$，置
$$
\ell_\infty(P)=P(1,0)-P(0,1).
$$
沿原 $S(X,Y)=(-Y,X)$、$U(X,Y)=(-Y,X-Y)$，直接逐点代入得
$$
\ell_\infty((1+S)P)=0,\qquad
\ell_\infty((1+U+U^2)P)=0.
$$
但 $\ell_\infty(Y^4)=-1$。所以不存在与 R1158、R1169 相同形式的 degree-four $A,B$ 使
$$
Y^4=(1+S)A+(1+U+U^2)B.
\tag{1172.25}
$$
乘原 $S,U$ 不变的四次 Weil 因子并不会消除此端点障碍。这只是排除该未修正 filling，绝非否定已构造的 corrected torsor；所需额外 Tate 来源在 (1172.9)、(1172.19) 中已经准确保留。

本篇完成了最低槽的真实同源方向、全部 Tate 标量、指定 continuous cochain 和整未平滑接口。它尚未给 (1172.20) 的一般 Frobenius 共轭路径数值，也未给一个独立于该未知路径的四线加 cyclotomic endpoint 局部读取。不得把 $\kappa_2$ 或 $v_{2,4}$ 的单位性冒作 $Z_4$ 的非零，更不据此完成原全局中央减法或主目标。

## 来源与验证

- R1147 (1147.38)–(1147.40)、(1147.61)–(1147.65)：原 corrected cup、兼容整塔、primitive/all-vector 实际群尺度及全部根 gauge。
- R1157–R1159：真实辅助数二 theta/Norm、同一 cyclic subgroup 内的相关、原 $R,L,K,\eta_d$ 及 kernel 逆像群图。
- R1160 §§4、8：原 $\mathcal B_{4,6}$ 的完整算术共轭、两幺幂反差分、约化相容及 residue 截面。
- R1163 §§8–10：实际 $\Pi_4$ 与 constant Tate-five 乘法的整比较、原有序 primitive groupoid。
- R1169：同一前三槽/最低槽之间需要保留的 coefficient 与 Tate 区别。

本篇全部是原数据上的纸面群律、连续上链和有限标量计算，没有执行数学程序。global_route 独立纸核 (1172.17)–(1172.23) 的全部 Tate 运输、crossed 正号、未平滑微分及二同源标量；root 同时核了完整群图、两种整尺度和端点 functional。
