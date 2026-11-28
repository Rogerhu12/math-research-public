# R699　真实宽截面肩两侧主曲率的全点界

[R688](R688-crown-to-primary-material-paths-and-window-projection-rows.md) 将 [R684](R684-directional-gauss-degree-and-two-solid-window-crowns.md) 两个老凸帽的截面肩各取物理宽 $.05$，以便给原平行帽和恒截面柱实际的过渡距离。对其真实有限退速，有
$$
                 -10.4<\kappa_i<8.55\qquad (i=1,2) .                 \tag{1}
$$
符号取凸球面外面为正。该界覆盖整张肩的所有截面和角度，对近帽固定及远帽纯平移的所有相位相同。本证只涉及此部件的形算子与近对角必要门。

## 1　真实截面和退速

用 [R681](R681-two-rigid-positive-crowns-and-one-reflected-window.md) 的坐标 $(x,w,z)$，令
$$
 F=H(\sigma)+(z/d)^2-1,\quad
 \sigma=(x/a)^2+((w-c)/b)^2,\quad
 H(s)=(\max(s-1,0)/.44)^4,
$$
其中 $a=.42,b=.07,c=.02,d=.08$。原凸体 $K_0=\{F\le0\}$ 外偏移 $r=.12$ 得 $K_r$。给定肩的物理纵坐标 $-.05\le y\le0$，固定取 $K_r$ 在 $w=\eta(y)$ 的整个真实截面，再以 $y$ 代替 $w$。因此肩的几何无需依赖某种极角样条的取样密度。沿 $g=-y$ 写
$$
 Q(g)=\int_0^g q(t)\,dt,\quad \eta(y)=-Q(-y),\quad
 \eta'=q(g),\quad \eta''=-q'(g)\ge0 .                               \tag{2}
$$
这与 R688 的[实际截面函数](../scripts/r688_true_caps_and_reference_sections.py)相同。

$g_0=.00001$ 以前 $q=1$；接着在长度 $L=.023$ 上置 $q=(1-S(s))^2$，$s=(g-g_0)/L$；其后 $q=0$。以 $d_s=.01$ 记两个端坡的相对宽度。在 $0\le s\le d_s$ 取
$$
 S(s)=\frac{d_s}{1-d_s}\left[(s/d_s)^3-\frac12(s/d_s)^4\right].
$$
在 $d_s\le s\le1-d_s$ 取 $S=(s-d_s/2)/(1-d_s)$，末端取 $S(s)=1-S(1-s)$。它在接合处至少 $C^2$，$0\le S'\le1/(1-d_s)$，且 $|S(s)-s|<.011$。最后一界在中央线段由式直接得，两端由 $0\le s\le .01$、$0\le S(s)\le .01/(2\cdot.99)$ 及对称性得。由 $|(1-S)^2-(1-s)^2|<.022$，
$$
       0\le Q(g)<.00001+.023(1/3+.022)<.0082.                      \tag{3}
$$
故在 $|x|\le.3825$ 的真平座，$(x/.42)^2+((c-\eta)/.07)^2<1$，原顶、底为真实平面，肩保留所需的开余量。R688 对同一水平座的材料重标不产生曲率。$q$ 初端在开带恒为一，肩与原平行帽匹配；末端在正长度开带恒为零，已是真柱。

## 2　原平行面的有向轴向下界

令 $p=(x_0,w_0,z_0)\in\partial K_0$、$N=\nabla F/|\nabla F|$，同一法向处的老平行面点为 $p+rN$，其 $w$ 坐标为 $\eta$。 写 $n=|N_w|$、$\Pi=I-NN^T$。若 $H'>0$，
$$
 N_w=k_0(w_0-c),\qquad
 k_0=\frac{2H'}{b^2|\nabla F|},\qquad
 \eta-c=(1+rk_0)(w_0-c) .
$$
于是 $w_0<c,N_w=-n$。若 $H'=0$，有 $n=0$。在 $n>0$ 情形，$0<c-w_0\le c-\eta<.0282$、$\sigma>1$，因此
$$
 |x_0|>.42\sqrt{1-(.0282/.07)^2}>.384 .
$$
同时 $|N_x|>0$，梯度分量之比给
$$
 c-w_0=(b/a)^2|x_0|\,n/|N_x|>.01066\,n,\qquad
           n\le(c-\eta)/.13066<.216 .                               \tag{4}
$$
平行面的轴向法向分量同时受椭圆横宽和偏移半径约束。接近平座 $n=0$ 时 (4) 也成立。

设原凸面外法算子为 $S_0$，在共同切平面 $E=N^\perp$ 上记 $v=\Pi e_w$。原隐式 Hessian 的三部分 $H''\nabla\sigma\otimes\nabla\sigma$、$H'\nabla^2\sigma$、$2e_z\otimes e_z/d^2$ 均半正定。保留第二部分的 $ww$ 项得
$$
                S_0\succeq k_0 vv^T .
$$
平行面 $S_r=S_0(I+rS_0)^{-1}$ 满足 $0\preceq S_r\preceq I/r$。映射 $A\mapsto A(I+rA)^{-1}=r^{-1}[I-(I+rA)^{-1}]$ 在半正定算子上单调，因为正定逆序。故
$$
 S_r\succeq\frac{k_0}{1+r k_0|v|^2}vv^T
    =\frac{n}{c-\eta-rn^3}vv^T
    \succeq\frac{n}{c-\eta}vv^T.                                    \tag{5}
$$
中项在 $n>0$ 用 $n=k_0(c-w_0)$ 和 $|v|^2=1-n^2$ 得。分母 $c-\eta-rn^3=(c-w_0)+rn(1-n^2)>0$。$n=0$ 时用半正定性即可。这一秩一有向下界保留了宽肩中实际抵消负曲率的一项。

## 3　拉回与全区间数值常数

取老平行面的局部外符号距离 $d_r$。肩由 $f(x,y,z)=d_r(x,\eta(y),z)=0$ 表示，材料平滑度足以用二阶隐微分。令 $T=\operatorname{diag}(1,\eta',1)$，$m=|T^T N|$. 由 (4)，
$$
              m^2=1-n^2(1-(\eta')^2)\ge1-.216^2>.976^2 .
$$
对于肩的任一单位切向 $\xi$，$T\xi$ 在老平行面的切平面中。其有向法曲率准确为
$$
 \kappa(\xi)=
   \frac{\langle S_rT\xi,T\xi\rangle - n\eta''\xi_y^2}{m}.           \tag{6}
$$
以 $q\le1$ 得正向 $\kappa\le 1/(.12\cdot.976)<8.55$。另一向由 (5) 的 $v\cdot T\xi=\eta'\xi_y$，再用 (4) 和 $|\xi_y|\le1$，有
$$
 (-\kappa)_+\le
 \frac{[(c+Q)\eta''-q^2]_+}{.13066\cdot.976}.                        \tag{7}
$$
首尾常速区 $\eta''=0$，不存在负曲率。

以下逐段界定 (7) 的分子。记 $z=1-S(s)$，$q=z^2$、$\eta''=2z S'(s)/L$。

* 首段 $s\le d_s$ 有 $Q\le g_0+Ld_s$、$z> .9949$。分子至多 $2(c+g_0+Ld_s)/(.99L)-.9949^4<.81$。
* 中段 $d_s\le s\le1-d_s$，用 $ds=-(1-d_s)dz$，有 $Q\le g_0+L[d_s+(.99/3)(1-z^3)]$。于是
$$
 (c+Q)\eta''-q^2\le
 2\left(\frac{c+g_0+Ld_s}{.99L}+\frac13\right)z-\frac53 z^4
 <2.45z-\frac53 z^4 .
$$
右多项式在 $0\le z\le1$ 的最大值是 $\tfrac34(2.45)(3\cdot2.45/20)^{1/3}$。由 $.718^3>3\cdot2.45/20$ 得它小于 $1.32$。
* 末段 $s\ge1-d_s$ 有 $z<.0051$，由 (3) 得分子至多 $2(.0282)(.0051)/(.99L)<.02$。

代回 (7)，$(-\kappa)_+<1.32/(.13066\cdot.976)<10.4$。任意主方向都是单位切方向，遂得 (1)，也覆盖已接的老帽侧和恒柱侧极限。两帽的刚姿和空间镜像不改变外向主曲率数值。

若实际全件直径 $D\le1/(.03\cdot10.4)$，此实际刚性肩在所有相位都严格通过 $|\kappa_i|<1/(.03D)$。例如 [R696](R696-two-pulse-ramp-support-and-whole-moving-window-diameter.md) 的提升并集直径 $<3.012$ 满足这个条件；设计窗改变后须换入最终的 $D$。两个不同材料点之间的双侧法球、未知窗其余部分、原帽真实数值误差及整个闭面的共同度量仍分别需要其自身的证明。
