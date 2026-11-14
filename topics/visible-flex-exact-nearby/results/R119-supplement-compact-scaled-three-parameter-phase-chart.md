# R119 续篇：紧缩放全区间的三维实际相位图与共同两态控制

2026-11-14，visible-exact / tail_connector。

**状态：已证明的径向实际有限盒结论。** 本篇在同一个三维形状参数盒内，
对任意 $1/4\le\kappa\le K_*$ 构造完整两态正方向；该方向在一个
明确的 $\kappa$ 邻域内共同有效。参数半径、相位补偿和局部两态
可观测性均没有 $B$ 或 $\delta^{-1}$ 损失。
取 $K_*=2^{4000}J^{40}$ 后，恰接
[真实高振荡两态型](R119-supplement-exact-two-phase-curve-complete-oscillatory-generator.md)
的高缩放范围。

三个方向对所有频率共用，两个相位在整个有限盒内准确保持。
这里不把不同小频率包的不同方向称为整个非径向近核的共同方向；
后者仍需实际频率定位和外响应估计。原普通/weak 源及两个 mean
在末节保留。

## 1. 同一 actual quartic 和自然的完整两个状态

沿用第67/68束的真实 $Q=7+Bf$、$f=30x^2(1-x)^2$、
$dt_{\rm ph}=(\Delta/B)\,dx$，以及
$$
 e=B^{-1}<2^{-190},\quad \tau=\Delta^{-1}<1/80,\quad
 F=f+7e,\quad H=F+e,\quad \kappa=M^2/B,\quad J=j+5 .
 \tag{N.1}
$$
本篇 $M=4|m_{\rm std}|\ge4$，不使用不属于真实四重模的小频率。
选一个尚未使用的中心 $c_m$。可以在原区间
$I\subset[7/16,15/32]$ 中取 $c_m=c+\ell/4$；
它和高缩放曲线在 $c$ 附近的三个支集不交。
原 $\ell>2^{-31}J^{-2}$ 留有足够余量。

固定
$$
 K_*\ge1,\quad L_*=1+K_*,\qquad
 \varrho=2^{-2240}J^{-2}\Delta^{-11}L_*^{-10}.
 \tag{N.2}
$$
$[c_m-6\varrho,c_m+6\varrho]\subset I$，且与全部其它本地控制
支集不交。所有后续同支集参数同时使用这一条实际材料坐标。

令
$$
 Y=(u,u_{t_{\rm ph}}/B),\qquad u=\sqrt\mu\,h .
$$
准确径向系统和 profile kernel 为
$$
 Y_x=\Delta A_\kappa Y,\quad
 A_\kappa=\begin{pmatrix}0&1\\
 H^2/4-\kappa F-\tau F'/2&0\end{pmatrix},
 \tag{N.3}
$$
$$
 \mathcal K_{\rm rad}=B^2Y^T K_\kappa Y,\qquad
 K_\kappa=\begin{pmatrix}
 H^2/4-\kappa F&(H-2\kappa)/2\\
 (H-2\kappa)/2&1
 \end{pmatrix}.
 \tag{N.4}
$$
两行都保留，$Y$ 不被假称为行列式1的 physical canonical frame。

## 2. 全部 Sym2 的无 B 可观测性

记 $U_\kappa(x,c_m)$ 为 (N.3) 的基本阵，$U_\kappa(c_m,c_m)=I$。
对任意实对称 $C$ 定义
$$
 \mathcal K_C(x)=\operatorname{tr}
 [C\,U_\kappa(x,c_m)^T K_\kappa(x)U_\kappa(x,c_m)] .
$$
不限制 $C$ 为半正定或 rank-one。把相应三态写成 $X,P,Z$，
在中心准确有 $(X,P,Z)=(C_{11},C_{12},C_{22})$，且
$$
 \mathcal K=Z+(H-2\kappa)P+(H^2/4-\kappa F)X,\quad
 \tau X'=2P,\quad
 \tau P'=Z+(H^2/4-\kappa F-\tau F'/2)X .
$$
直接一次和两次微分给以下三个完整恢复式：
$$
 P=\frac{(H-2\kappa)\mathcal K-\tau\mathcal K'}
                         {4\kappa(\kappa-e)},
 \tag{N.5}
$$
$$
 X=\frac{\tau^2\mathcal K''+
                  (4\kappa F-H^2-\tau F')\mathcal K}
                         {2\kappa(\kappa-e)\tau F'},
 \tag{N.6}
$$
$$
 Z=\mathcal K-(H-2\kappa)P-(H^2/4-\kappa F)X .
 \tag{N.7}
$$
这些恒等式由同一实际有限 $e>0$ 系统导出，没有先令 $e=0$。
例如
$\tau\mathcal K'=(H-2\kappa)\mathcal K-4\kappa(\kappa-e)P$；
再微分并消 $P$，恰给 (N.6)。

对 $\kappa\ge1/4$，$\kappa-e>\kappa/2$、
$3/4<F'<2$、$H<3$。置
$W_C=\max_{0\le r\le2}|\mathcal K_C^{(r)}(c_m)|$、$L=1+\kappa$。
由 (N.5)--(N.7)，
$$
 |X|<16\Delta L\kappa^{-2}W_C,\quad
 |P|<2L\kappa^{-2}W_C,\quad
 |Z|<(1+6L^2\kappa^{-2}+48\Delta L^2\kappa^{-2})W_C .
 \tag{N.8}
$$
$L/\kappa\le5$ 和 $\Delta>80$ 于是给
$$
 \|C\|_F<2^{12}\Delta W_C .
 \tag{N.9}
$$
关键是此式对整个 $\kappa\ge1/4$ 统一，且没有 $B$。

仍令 $p=F^3F'$、$q$ 为第67束第二 phase 列除以 $\Delta^2$，
$W_p=pq'-p'q$，并使用同一
$$
 \mathcal A=\partial_x^2+b_1\partial_x+b_0,\qquad
 \mathcal A p=\mathcal A q=0 .
$$
原第68束 (B.2)--(B.3) 的完整三态逆准确给
$$
 \max_{r\le2}|g^{(r)}|
  \le2^{1365}\Delta^4(1+\kappa)^4
                        \max_{r\le2}|(\mathcal A g)^{(r)}|,
 \quad g=F^{9/2}\mathcal K_C .
 \tag{N.10}
$$
这是已经证明的有限 $e$ 五函数 Wronskian，不重做其科学源。
$F^{-9/2}$ 的两个 jets 费用小于 $2^9$。
对 $\|C\|_F=1$，(N.9)--(N.10) 因而保证某个 $r=0,1,2$ 满足
$$
 |(\mathcal A g)^{(r)}(c_m)|>
          \epsilon:=2^{-1400}\Delta^{-5}L_*^{-4}.
 \tag{N.11}
$$
从 $1386$ bits 放宽至 $1400$ 已包含前述完整单位换算。

## 3. 同一个真实短片和三个固定方向

以下短片估计也不乘整负窗条件数。
在 $|x-c_m|\le6\varrho$，原 quartic 到五阶的有限多项式界给
$$
 \max_{l\le5}\|K_\kappa^{(l)}\|_F<2^{32}L_*,
 \qquad
 \max_{l\le4}\|(\Delta A_\kappa)^{(l)}\|
                                      <2^{30}\Delta L_* .
$$
由 $12\varrho\,2^{30}\Delta L_*<1/4$，完整双向 flow norm 小于2。
令 $C_*=2^{36}\Delta L_*$；反复微分实积分方程给
$$
 \|U_\kappa^{(r)}\|\le2r!C_*^r,\qquad 0\le r\le5 .
 \tag{N.12}
$$
原 $F^{9/2}$ 的前五阶 jets 小于 $2^{80}$ 已足够。
四因子 Leibniz 和至多 $4^5$ 项，两个 flow 导数的 factorial
乘积至多 $5!$；所以
$$
 \max_{r\le5}|g^{(r)}|<2^{320}\Delta^5L_*^6.
$$
再用 $|b_\nu^{(l)}|\le l!2^{82l+97}$，$l\le3$，得到安全的
$$
 \max_{r\le3}|(\mathcal A g)^{(r)}|
                              <G:=2^{800}\Delta^6L_*^6 .
 \tag{N.13}
$$
$\varrho G<\epsilon/16$ 由 (N.2) 立即成立。
因此 (N.11) 中选中的导数在整个支集上保持其符号，模大于
$\epsilon/2$。

令 $P(y)=(1-y^2)_+^{14}$，同时固定三个实际形状
$$
 \psi_r=2^{-700}F^{9/2}\mathcal A^*
       \left[\partial_x^r\{\varrho^{r+6}
                  P((x-c_m)/\varrho)\}\right],
                    \qquad r=0,1,2 .
 \tag{N.14}
$$
三者不依赖 $\kappa$。它们是真 $C_c^9$ 函数，准确消去
两个实际 phase；原已付有限 jets 保留每个 $\varrho$ 幂后给
$$
 \|\psi_r^{(l)}\|_\infty\le\varrho^{4-l},\qquad
 \|\psi_r^{(l)}\|_{L^1}\le2\varrho^{5-l},
                 \quad 0\le l\le4,\qquad \|\psi_r\|_{C^4}\le1 .
 \tag{N.15}
$$
对 (N.11) 选中的 $r$，完整分部积分给
$$
 \left|\int\psi_r\mathcal K_C\,dx\right|
 >2^{-704}\epsilon\varrho^{r+7}
 \ge2^{-2104}\Delta^{-5}L_*^{-4}\varrho^9 .
 \tag{N.16}
$$
此处是无量纲 $dx$ 积分；物理 $B\Delta$ 因子将在第6节保留。

定义
$$
 \sigma_*=2^{-2110}\Delta^{-5}L_*^{-4}\varrho^9,
$$
以及
$$
 \mathcal L_\kappa:\mathbb R^3\longrightarrow\operatorname{Sym}(2),
 \quad
 \mathcal L_\kappa v
 =\int\Big(\sum_{r=0}^2v_r\psi_r\Big)
                     U_\kappa^T K_\kappa U_\kappa\,dx .
 \tag{N.17}
$$
(N.16) 对全部 Frobenius 单位 $C$ 表明
$\|\mathcal L_\kappa^*C\|_\infty>64\sigma_*$。
两边都是三维，故 $\mathcal L_\kappa$ 可逆，且
$$
 \|\mathcal L_\kappa^{-1}\|_{F\to\ell^1}
                                  <(64\sigma_*)^{-1}.
$$
因此存在唯一的真实系数
$$
 v(\kappa)=\mathcal L_\kappa^{-1}(\sigma_*I),\qquad
 |v(\kappa)|_1<\sqrt2/64<1/16 .
 \tag{N.18}
$$
这是一组三个固定控制的完整线性代数，不是为每个模式新开
一个独立极小参数，也没有只检验 rank-one 输入。

## 4. 同支集相位补偿和完整三维有限盒

在 $c_m\pm4\varrho$ 取原第三相位篇同一类补偿：
$$
 \eta_\pm=2^{-80}\varrho^4
                 P((x-c_m\mp4\varrho)/\varrho).
$$
它们与 $\psi_0,\psi_1,\psi_2$ 的中央支集不交。
两个当前 phase 密度之比的导数仍是 $W_p/(128p^2)>2^{-15}$，
故其完整 $2\times2$ Jacobian 的真实逆满足
$$
 \|M^{-1}\|_{\infty\to\infty}<H_*=2^{128}\varrho^{-6}.
 \tag{N.19}
$$
这包含两个补偿列积分的 $\varrho^{11}$ 行列式费用；
没有借用原远端 bump 的逆。

置
$$
 R_*=2^{-2300}\Delta^{-5}L_*^{-5}\varrho^{10},\qquad
 q_r=(R_*/3)\theta_r,\quad |\theta_r|\le1 .
 \tag{N.20}
$$
在同一原 phase map 上解
$$
 \Xi(q)=\sum_{r=0}^2q_r\psi_r
                     +z_-(q)\eta_-+z_+(q)\eta_+,\qquad
                              \mathsf C(\Xi(q))=0 .
 \tag{N.21}
$$
原 $\|D^2\mathsf C\|<2^{-10}$、$D\mathsf C(0)\psi_r=0$
和 (N.19) 给与第三相位篇完全相同的 contraction。
它在复 $|q|_1<2R_*$ 中成立；在实际 $|q|_1\le R_*$ 上，
$$
 |z(q)|_\infty\le H_*|q|_1^2,\quad
 |Dz(q)[a]|_\infty\le H_*|q|_1|a|_1,\quad
 \|\Xi(q)\|_{C^4}\le2|q|_1 .
 \tag{N.22}
$$
例如 Jacobian 逆小于 $2H_*$，
$D_q\mathsf C$ 在原 annihilator 方向上小于
$2^{-9}|q|_1$，足以给第二式。
$H_*R_*<2^{-2000}$，所有 self-map 和复球余量均严格满足。

整个实际盒的原两个径向 $\bar\Gamma$ 保持原值，因为
$\mathsf C(\Xi(q))$ 准确为零，且原 phase map 支集相加。
这没有把真实非径向 $D\Gamma^*$ 设零。
对任一向量 $a\in\mathbb R^3$，当前完整方向是
$$
 \Psi_{q,a}=\sum a_r\psi_r+Dz_-(q)[a]\eta_-
                                     +Dz_+(q)[a]\eta_+ .
 \tag{N.23}
$$
后两个当前补偿列在下面的有限盒估计中真实付费。

## 5. 当前盒的全矩阵稳定性和共同频率包

现在 $F_q=F-\tau\Xi(q)'$，
$U_{\kappa,q}$ 是当前 (N.3) 在 $c_m$ 的完整基本阵。
记
$$
 \mathcal M_{\kappa,q}(x)=U_{\kappa,q}^T K_\kappa(F_q)U_{\kappa,q},
 \qquad
 \mathcal L_{\kappa,q}a=\int\Psi_{q,a}\mathcal M_{\kappa,q}\,dx .
 \tag{N.24}
$$
这里每个点的物理 density 都使用其当前值，不把背景换回原点。

(N.15)、(N.22) 给
$|\Xi^{(l)}|\le2R_*\varrho^{4-l}$，$l\le4$。
于是
$$
 \|\Delta(A_{\kappa,q}-A_{\kappa,0})\|
                     <8L_*R_*\varrho^2,\qquad
 \|U_{\kappa,q}-U_{\kappa,0}\|
                     <2^9L_*R_*\varrho^3 .
 \tag{N.25}
$$
第二式是同一短片上的完整一次有序 Duhamel；
两个 flow norm 都小于2。由
$\|K_\kappa(F_q)\|_F<8L_*$，进一步
$$
 \|\mathcal M_{\kappa,q}-\mathcal M_{\kappa,0}\|_F
                                  <2^{16}L_*^2R_*\varrho^3 .
 \tag{N.26}
$$
中央三个方向的 $L^1$ 范数给相应积分误差
$2^{17}L_*^2R_*\varrho^8|a|_1$。

两个补偿 bump 各自 $L^1$ 范数至多 $2^{-79}\varrho^5$，
而 $\|\mathcal M_{\kappa,q}\|_F<32L_*$。
故它们的完整附加误差至多
$$
 2^{-73}L_*H_*R_*\varrho^5|a|_1
       =2^{55}L_*R_*\varrho^{-1}|a|_1 .
$$
由于 $L_*\varrho^9<1$，两种误差一起给
$$
 \boxed{\quad
 \|\mathcal L_{\kappa,q}-\mathcal L_{\kappa,0}\|_{\ell^1\to F}
   <2^{57}L_*R_*\varrho^{-1}
   =2^{-133}\sigma_* .
 \quad}
 \tag{N.27}
$$
这一步用的是局部完整状态和当前两条补偿，没有把旧
$K_j^6(U+B)^2$ 半径公式的 $B$ 费用直接删掉；
而是重新证明了实际有限盒稳定性。

由 (N.18)、(N.27)，全盒在方向 $v(\kappa)$ 上满足
$\mathcal L_{\kappa,q}v(\kappa)>\sigma_*I/2$。
还可把同一个方向用于一整个频率包。
因为 $q$、其相位补偿和三个基函数都不依赖 $\kappa$，
$$
 \|\partial_\kappa U_{\kappa,q}\|
                       <2^7\Delta\varrho,\qquad
 \|\partial_\kappa\mathcal M_{\kappa,q}\|_F<32 .
$$
第一式使用
$\partial_\kappa(\Delta A)=\Delta\left(\begin{smallmatrix}0&0\\-F_q&0\end{smallmatrix}\right)$；
第二式的完整乘积余项小于
$2^{12}L_*\Delta\varrho<1$，其直接项小于16。
由 $\|\Psi_{q,a}\|_{L^1}<3\varrho^5|a|_1$，
$$
 \|\partial_\kappa\mathcal L_{\kappa,q}\|_{\ell^1\to F}
                                          <2^8\varrho^5 .
 \tag{N.28}
$$
取
$$
 \eta_* =2^{-16}\sigma_*\varrho^{-5}.
 \tag{N.29}
$$
对任意 $\kappa_0\in[1/4,K_*]$ 和
$|\kappa-\kappa_0|\le\eta_*$、$\kappa\in[1/4,K_*]$，
使用同一个 $v(\kappa_0)$，由 (N.27)--(N.29) 得
$$
 \boxed{\quad
           \mathcal L_{\kappa,q}v(\kappa_0)
                             >\frac{\sigma_*}{2}I_2
          \quad\text{于整个 }|q|_1\le R_* .
 \quad}
 \tag{N.30}
$$
一个有限网格覆盖全部紧区间即可，但网格不增加实际参数：
所有方向都在同一个固定三维盒中。$\eta_*$ 和 $R_*$
只含 $\Delta,J,L_*$，没有 $B$ 或 $\delta$。

## 6. 原有限坐标、物理 measure 和完整两端 scattering

取实际 $\theta$ 点和方向 $v(\kappa_0)$。
$D_\theta q=(R_*/3)v(\kappa_0)$，
所以当前物理 crossing 对任意 $Y(c_m)$ 精确多一个
$B^2dt_{\rm ph}=B\Delta\,dx$ 因子。由 (N.30)，
$$
 \mathfrak L_{\theta,v,M}>
             \frac{B\Delta R_*\sigma_*}{8}|Y(c_m)|^2 .
 \tag{N.31}
$$
若 $\theta\in[-1/2,1/2]^3$，整段
$\theta+s\,v(\kappa_0)$、$|s|\le1$ 都留在原实际盒内；
不是只给原点一个无限小方向。

在原中心 wave
$Z=(\sqrt{k_c}u,u_{t_{\rm ph}}/\sqrt{k_c})$、
$k_c=\sqrt{7M^2-16}$ 下，
$$
 |Y|^2=|Z_1|^2/k_c+(k_c/B^2)|Z_2|^2
                    \ge\frac{M}{3B^2L_*}|Z|^2 .
 \tag{N.32}
$$
第一槽只用了
$M^2/B=\kappa\le L_*$ 和 $B>1$；
未偷偷假设 $M<B$。第二槽用 $k_c>2M$。
又 $\kappa\ge1/4$ 给 $M\ge\sqrt B/2$，所以
$$
 \mathfrak L_{\theta,v,M}
               >\frac{\Delta R_*\sigma_*}
                          {48L_*\sqrt B}|Z(c_m)|^2 .
 \tag{N.33}
$$
最后使用原已重付的全实 Cauchy
$K_j=2^{6000}J^8\delta_j^{-16}$ 与完整两端 Green/Cayley
比较，得到整个径向负窗
$$
 \boxed{\quad
 -iS_M^*D_{\theta,v(\kappa_0)}S_M
       >\frac{\Delta R_*\sigma_*}
                    {2^9L_*\sqrt B\,K_j^2}\,I_2 ,
 \quad |\kappa-\kappa_0|\le\eta_* .
 \quad}
 \tag{N.34}
$$
同一个方向对包内所有真实 Fourier 模、两个角锥及两个端口
同时成立。径向 Parseval 把 (N.34) 原样相加，保留完整两态
交叉项，没有除以模数。

取 $K_*=2^{4000}J^{40}$ 后，所有参数费用都是固定常数和
$J,\Delta$ 的幂；真正物理换算仅留下 (N.34) 中显示的
$B^{-1/2}K_j^{-2}$。没有把一个原 $C^4$ 以外的归一当成
免费参数，也没有预先使用尚缺的全网谱隙。

## 7. 与高缩放曲线共存、原 joint 图及完整源

高缩放曲线和本三维图的五个支集安排在同一原 $I$ 内的
两个不交子区间。其中央、左右补偿都不交，因此原局部 phase
泛函相加；两个子图各自 $\mathsf C=0$，合在一起仍准确为零。
高缩放片的 quartic germ 未被本三维图改变，反之亦然。
总 $C^4$ 小于 $2r_0+2R_*<2^{-79}$。

允许族的入口需要重新消费：第53束覆盖完整 $C_0^4$ 球，
没有要求形状处处留在线性 annihilator；本图在其原实、复球内。
第54束的真实 phase map 支集相加，故原 radial $\bar\Gamma$
准确固定。第55束的状态估计与两相位联立收缩只使用相同
$C^4$ 输入和当前 radial 基点，本图按第三相位与局部曲线第8节同样
逐项满足。没有新增端 jets 或 $Q_{ttt}$ 接缝原子。
这重新接入原 $\Gamma^*(a,\Omega)$，但不将其两条
实际非径向导数判为零。

ordinary/weak 源完整保留。若物理总通量状态
$Y_{\rm ph}=(h,\pi)$ 满足
$Y_{{\rm ph},t_{\rm ph}}=A_{\rm ph}Y_{\rm ph}+\mathbf s$，
定义自然两行
$$
 T_{\rm nat}Y_{\rm ph}
  =\binom{\sqrt\mu h}
    {B^{-1}\{\pi/\sqrt\mu-(1+Q)\sqrt\mu h/2\}} .
 \tag{N.35}
$$
它的 determinant 是 $B^{-1}$，所以不误称为 unitary 或
physical symplectic 归一。准确源方程为
$$
 (T_{\rm nat}Y_{\rm ph})_x
   =\Delta A_\kappa(T_{\rm nat}Y_{\rm ph})
                         +(\Delta/B)T_{\rm nat}\mathbf s .
 \tag{N.36}
$$
两个原源分量同时进入；第一 weak 源不会因为主方程写成
二阶形式而消失。其参数列仍按原材料坐标的
$\widehat{\mathbf s}=\dot{\mathbf s}-\Psi\mathsf B\mathbf s$
及完整有序 Duhamel 传播，不索取未经给定的 $F^t_t$。
物理 bare flux 另外的 $F^t$ 端迹不被 (N.36) 赋予新权限。

$M=0$ 的高度/flux mean 不属于本 $\kappa\ge1/4$ 结论；
其完整两行与全局唯一高度常数继续由原合同保留。
本篇没有删去 mean 来制造有限维可逆性。

## 8. 下一项必须真正完成的全网门

与高缩放共同曲线合并后，全部 $\kappa\ge1/4$ 已有一个实际
无 $B$ 半径损失的径向有限参数机制，且每个紧缩放小包有共同
两态 PSD。低缩放仍由已付低锥方向处理，不能拿它跨过
$[3/4,1]$ 的严格反例。

尚未完成的是：在当前完整非径向酉网络的 near-kernel 中，
证明足够的频率定位，使一个真实小包使用 (N.30) 的同一方向；
或者给覆盖多个包的真实共同参数组合。相邻负窗、正片、
端角共轭和 $\Gamma^*$ 两列的参数响应也须按实际完整算子
支付，并保留原层权和 source-to-label 两向映射。
本篇未用径向 Parseval 隐去这些交叉项。

所有推导是显式解析恒等式与有限范数估计，复用了已经完成的
五函数 Wronskian 证明；没有新数值实验或未执行的通过门。
