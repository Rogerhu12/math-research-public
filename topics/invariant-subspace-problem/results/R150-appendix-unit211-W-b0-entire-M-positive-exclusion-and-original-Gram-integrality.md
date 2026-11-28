# R150 后续：W/b0 整个大 M 正阶排除与原 Gram 整性

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

**已证明。** 在当前正确 W、完整 $b_0=0$ 物理图的任意 1009 位置，
$$
\boxed{v(M)=0,\qquad M=\delta\ell^2-m^2=4bc\delta.}
$$
这里的大写 $M$ 与 $m=u-\ell$ 不同。证明先在假设 $v(M)>0$ 下支付全部原变量及 Gram 坐标整性，再把真实均值式取剩余，得到一个直接矛盾。无需新消元执行、选剩余点、倒未付头或引用特征零零权空性。

## 1. 当前原范围及正确乘法

先行结果已给
$$
v(e)=v(k)=v(u)=v(Q)=v(\delta)=v(V_{\rm bar})=v(\ell)=0,
$$
$$
e=u-1,\quad Q=ek,\quad\delta=1-Q,\quad V_{\rm bar}=uk+2,
\quad m=u-\ell,\quad M=\delta\ell^2-m^2,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{kV_{\rm bar}}.
\tag{1}
$$
来源为[全 e/k/u](R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)、
[全 delta](R150-appendix-unit211-W-b0-entire-delta-positive-exclusion-and-1009-integral-unit.md)、
[全 Vbar](R150-appendix-unit211-W-b0-entire-Vbar-positive-exclusion-and-1009-integral-unit.md)、
[全 ell](R150-appendix-unit211-W-b0-entire-ell-positive-exclusion-and-1009-integral-unit.md)。
$m$、$M$ 因而整，但本稿不先付 $m$ 或 $M$ 的单位性。原物理图的 $b,c,\delta$ 非零，故 $M\ne0$；若有正阶，记 $d=v(M)>0$。任意有限扩张赋值均可，未假定整数阶。

令 $\rho^2=\delta$，
$$
p=1+\rho,\quad q=1-\rho,\quad
b=\frac{\ell+m/\rho}{2},\quad
c=\frac{\ell-m/\rho}{2},\quad a=1-\ell.
$$
于是 $bp+cq=u$，$bc=M/(4\delta)$。真正 dual 乘法和迹是
$$
(vz)_0=v_0z_0,\quad(vz)_1=v_0z_1+v_1z_0,\quad
(vz)_B=v_Bz_B,\quad(vz)_C=v_Cz_C,
$$
$$
\tau(v)=av_0+v_1+bv_B+cv_C,\qquad\mathbf1=(1,0,1,1).
\tag{2}
$$
使用原 Gram 行
$$
R_0=(0,0,p,q),\quad R_1=(0,A_1,r,s),\quad
R_B=(p,r,0,t),\quad R_C=(q,s,t,0),
$$
$$
(\mathcal Kv)_j=\tau(R_jv),\quad
d_{\rm vec}=\mathcal K\mathbf1,\quad F_2=\tau(d_{\rm vec})=2f.
$$
下文 $d_j$ 是此向量坐标；$d=v(M)$ 只在赋值式中使用。

原均值为
$$
E_j=\tau(R_j^2)-2(\mathcal Kd_{\rm vec})_j-2(d_{\rm vec}^2)_j+2F_2d_j,
$$
其中 $j=1$ 的第一项必须是 $2\tau(R_0R_1)$，且
$(d_{\rm vec}^2)_1=2d_0d_1$。不使用旧错误的 $(d_1)^2$。

## 2. 在 M 深图上先支付三个真正权单位

假设 $d=v(M)>0$。因 $\delta,\ell$ 为单位，$m$ 自动为单位。
本节在剩余域中省略横线，所有等式均来自 (1)，而
$$
\delta\ell^2=m^2.
\tag{3}
$$

### 2.1 不能有 ell=1/2

若 $\ell=1/2$，则
$$
\delta=(2u-1)^2,\quad Q=4u(1-u),\quad k=-4u,\quad
V_{\rm bar}=2(1-2u^2).
$$
这些原分母已为单位。代入 (1)，
$$
\frac12=-\frac{6u^2-6u+1}{2(1-2u^2)}
$$
迫 $2(2u-1)(u-1)=0$。$e=u-1$ 为单位，所以 $u=1/2$，继而 $\delta=0$，矛盾。因此
$$
2\ell-1\text{ 在整个 M 深图为赋值单位。}
\tag{4}
$$

### 2.2 Phi 也为单位

置
$$
J=2u(1-u)+\ell Q,\quad
T_0=2u-\ell Q-2u^2,\quad \Phi=T_0+4u-4+Q.
$$
原 W 身份给
$$
\Phi=-2e^2(k+4)/V_{\rm bar}.
$$
若 $\bar\Phi=0$，则 $\bar k=-4$。在该剩余线上，(1) 给
$$
\ell=u/2,\quad m=u/2,\quad M=u^2e,
$$
与 $u,e$ 为单位和 $\bar M=0$ 冲突。故
$$
v(\Phi)=0.
\tag{5}
$$

### 2.3 J-uQ 为单位

令 $\zeta=m/\ell$。在 (3)，
$$
\delta=\zeta^2,\quad u=\ell(1+\zeta),\quad Q=1-\zeta^2.
$$
$\zeta,\zeta-1,\zeta+1$ 都为单位，后两者由 $u,Q,\ell$ 的单位性支付。
若 $J-uQ=0$，则
$$
u=(\zeta^2-\zeta+2)/2,\quad
e=\zeta(\zeta-1)/2,\quad
k=-2(\zeta+1)/\zeta.
$$
此时
$$
(k+2)^2-2ek=\frac{2(\zeta^4-\zeta^2+2)}{\zeta^2},
\quad
kV_{\rm bar}=\frac{2(\zeta+1)(\zeta^3-\zeta+2)}{\zeta^2}.
$$
再用 $\ell=u/(1+\zeta)$ 及 (1)，准确得到
$$
\zeta^4-\zeta^2+2=\zeta^3-\zeta+2,
\qquad \zeta(\zeta-1)^2(\zeta+1)=0,
$$
与上述单位冲突。因此
$$
v(J-uQ)=0.
\tag{6}
$$
这三个单位只在假设的 M 深图中使用，未外推至其他边界。

## 3. 原 q/R 付 mu、T 及完整谱变量整性

记
$$
\mu=2\lambda-3,\quad
A=\frac{\mu^2+4\mu+5}{2},\quad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2},
$$
$$
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2
                 =4uQ\delta\ell^2-MA_*,
$$
$$
D=\ell A-T^2,\quad K=\ell^2B_3-3\ell AT+2T^3.
$$
$A_*$ 整，且 $C_*$ 在 M 深图为单位。完整原式
$$
q_2=2C_*A+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0
$$
等价于
$$
D=MS,\qquad
S=\frac{A_*A-\ell Q(3-4\lambda)}{4uQ\delta\ell}.
\tag{7}
$$
(7) 右边只有既有赋值单位分母，不倒 $A_*$ 或 $M$。
同时保留原
$$
R_6=MK^2-4m^2D^3=0.
\tag{8}
$$

若 $s_\mu=v(\mu)<0$，$q_2$ 的 $A$ 与 $T^2$ 系数为单位，中间线性 mu 项阶高于 $2s_\mu$，所以必有 $v(T)=s_\mu$。
(7) 给 $v(S)\ge2s_\mu$，(8) 给
$$
v(K)=d+\tfrac32v(S)\ge d+3s_\mu.
$$
设 $\alpha=\overline{T/\mu}$。由 $D=MS$ 及 $d>0$，
$$
\alpha^2=\bar\ell/2.
$$
由 $K/\mu^3$ 的剩余为零，
$$
\bar\ell^2/2-3\bar\ell\alpha/2+2\alpha^3=0,
$$
故 $\alpha=\bar\ell$，再迫 $\bar\ell=1/2$，与 (4) 冲突。
因此 $\mu$ 整。$q_2$ 的单位 $T^2$ 头随即付 $T$ 整；(7) 也使 $S$ 整。
这里没有假定 $A_*\ne0$，更没有用 $T=uQ\ell\mu/A_*$ 排除其精确零支。

完整原谱可写为
$$
h_B=1+\frac{T-m\sigma}{\ell}+\rho\sigma,\qquad
h_C=1+\frac{T-m\sigma}{\ell}-\rho\sigma,\qquad
w=\lambda-1-T.
$$
原第二矩准确给
$$
D=M\sigma^2.
\tag{9}
$$
由 (7)、(9) 和物理 $M\ne0$ 得 $\sigma^2=S$，故 $\sigma,h_B,h_C,w$ 全整。这里使用的是正则右式 $S$；没有把 $M$ 当赋值单位，也未倒 $D$ 或选某个谱根。

## 4. 真 E1 在乘 M 后的单位 f² 头

由 (3) 可在有限赋值扩张中取 $\rho$，交换原 B/C 标签使
$$
\bar m=\bar\ell\bar\rho,\qquad
v(b)=0,\quad v(c)=d>0,\quad \bar b=\bar\ell,\quad\bar c=0.
\tag{10}
$$
$p,q,p-q$ 都为单位，因为 $\rho$ 为单位且 $pq=Q$ 为单位。
交换标签同时保留全部原均值和原值式，未挑一个几何值根。

置
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\quad
G=\lambda P_{02}+(u-1)T_0,
$$
$$
P_f=T_0(J-Q),\quad P_c=QP_{02}(\ell+T)-GT_0.
$$
这些系数都已整。完整原仿射恢复是
$$
t=-\frac{P_ff+P_c}{bcQ\Phi},\quad
V=\frac{Jf+bcQt-G}{Q},\quad W_1=2uf+T_0/2,
$$
$$
X=\frac{W_1-qV}{b(p-q)},\quad
Y=\frac{pV-W_1}{c(p-q)},\quad
A_1=2f-2V+2bct,
$$
$$
r=X-ap-ct,\quad s=Y-aq-bt.
\tag{11}
$$
这些是以未知 f 为变量的普通仿射式，目前尚未假设 f 整。

说明完整 W 身份如何付其系数，而不把必要关系当额外输入。由 (1)，
$$
F_W=\ell Q(uQ+2e)-u[(Q+2e)^2-2Qe^2]=0.
$$
直接展开得
$$
(J-2uQ)\Phi-T_0(J-Q)=2F_W=0.
$$
所以
$$
V_f=2u,\quad X_f=u/b,\quad Y_f=u/c,\quad
(d_1)_f=2-2u.
\tag{12}
$$
这里下标 f 是完整普通系数，绝不是取物理 $f=0$。

由 (5)、(10)–(11)，$X,r,A_1,d_1$ 的全部仿射系数整；
$t,Y,s$ 的各系数阶至少 $-d$。其中
$$
d_0=u,\quad d_B=X,\quad d_C=Y,\quad d_1=2f-V-au.
$$
又
$$
(\mathcal Kd_{\rm vec})_1=uA_1+brX+csY.
$$
故 $ME_1$ 是系数整、次数至多二的 f 多项式。

令 $\vartheta=t_f=-P_f/(bcQ\Phi)$。由真乘法，
$$
[f^2]E_1=-2\{u^2(1/b+1/c)-u(b+c)\vartheta\}+8(1-u).
$$
用 $b+c=\ell$、$bc=M/(4\delta)$ 及
$P_f/(Q\Phi)=J/Q-2u$，得到完整精确头
$$
\boxed{
M[f^2]E_1=8(1-u)M-8u\ell\delta(J/Q-u).
}
\tag{13}
$$
(6) 使 (13) 的剩余非零。因此 $ME_1=0$ 是一个真单位二次头方程，迫
$$
v(f)\ge0.
\tag{14}
$$
这是独立真 E1，不是加权均值代替式，且没有将 $m,M,P_{02}$ 或 $f-u$ 作为新分母。

由 (11)–(14)，$X,r,A_1,d_1$ 已整；$ct,cY$ 整。还需排除 t、Y 自身的极点，才能取全原 Gram 剩余，下一节完成该步。

## 5. 完整 EC/PC 排除 t 与 Y 的所有极点

由 (2) 和 $R_C=(q,s,t,0)$，准确有
$$
\tau(R_C^2)=aq^2+2qs+bt^2,\qquad
\tau(R_C^3)=aq^3+3q^2s+bt^3,
$$
$$
(\mathcal Kd_{\rm vec})_C=aqu+qd_1+su+btX.
$$
因此
$$
E_C=bt^2-2Y^2+\mathcal L(t,Y)=0,
\tag{15}
$$
其中 $\mathcal L$ 对 t、Y 至多一次、各系数整；使用 $s=Y-aq-bt$ 即得。
完整原三次式为
$$
P_C=\tau(R_C^3)-3Y\tau(R_C^2)+2Y^3-P_{02}h_C^3=0.
$$
因 $h_C$ 已整，写成
$$
P_C=bt^3-3bYt^2+2Y^3+\mathcal Q(t,Y)=0,
\tag{16}
$$
其中 $\mathcal Q$ 总次数至多二且系数整。

若 t、Y 中至少一个有极点，(15) 先迫两者具有同一负阶 $\nu$；
否则仅一个平方项唯一最低。令 $z=\overline{t/Y}$，则最低项给
$$
\bar b z^2=2,\qquad
\bar b z^3-3\bar b z^2+2=0.
$$
由此 $z=2$、$\bar b=1/2$，与 (4)、(10) 冲突。因此
$$
v(t)\ge0,\qquad v(Y)\ge0.
\tag{17}
$$
现在全部原 Gram 坐标、全部原谱值都整。过程中未假定 $P_{02},\lambda,D$ 的剩余非零，故这些内部零层也全保。

## 6. 原三维剩余均值的直接矛盾

合法取全原式剩余，(10) 使 $c=0,b=\ell$。本节省略横线：
$a=1-b$、$u=bp$，且 $p,b,1-2b$ 为单位。迹只保留原 dual 两坐标和 B 坐标：
$$
\tau(x_0,x_1,x_B)=ax_0+x_1+bx_B.
$$
这不是套用一个特征零零权分类，而是直接使用真实剩余行
$$
R_0=(0,0,p),\quad R_1=(0,A_1,r),\quad R_B=(p,r,0).
$$

原 $E_0=0$ 是
$$
bp^2-2bpX-2u^2+4fu=0,
$$
所以
$$
X=2f+p/2-u.
\tag{18}
$$
由 $F_2=2f$ 和行定义，
$$
d_1=2f-au-bX,\quad r=X-ap,\quad A_1=d_1-br.
$$
再直接计算
$$
(\mathcal Kd_{\rm vec})_B=2pf-apu.
$$
把这些代入完整 $E_B$，逐项化简得到
$$
\boxed{E_B=-2p(1-2b)\{f+p(1-4b)/4\}.}
\tag{19}
$$
因此
$$
f=p(4b-1)/4,\quad X=u,\quad
d_1=p(b-1/2),\quad r=p(2b-1).
\tag{20}
$$
由于 $X=u$，
$$
(\mathcal Kd_{\rm vec})_1
=uA_1+brX=u(A_1+br)=ud_1.
$$
完整真 E1 此时准确为
$$
\begin{aligned}
E_1
 &=2bpr-2ud_1-4ud_1+4fd_1\\
 &=2ur+(4f-6u)d_1
 =\boxed{\frac{p^2}{2}(2b-1)^2}.
\end{aligned}
\tag{21}
$$
右侧在特征 1009 非零，矛盾。

## 7. 整个 M 深图关闭及准确范围

假设 $v(M)>0$ 后，§2 从原 W 权关系付清 Phi、$J-uQ$、$2\ell-1$ 的单位；
§3 不倒 Astar 地付清全部谱整性；§4 以真 $ME_1$ 二次头付 f 整；
§5 以完整 EC/PC 排除所有剩余 Gram 极点；§6 才合法取零权剩余并用 E0/EB/E1 得矛盾。
所以没有遗漏因坐标极点而无法取剩余的原解。

原 M 已整，正阶全图不可能，故 $v(M)=0$。这是每个原点和每个 1009 位置的单位结论，非任意有限域好点向 QQ 的推断。所有恒等式在正文展开，没有新计算目标、资源预算或复算旧门。

本稿不直接支付全图的 $m,A_*,\Phi,J-uQ$；§2 的三个辅助单位仅在被排除的 M 深图中成立。全局新结论只有大写 M 单位，以及所证明的该边界不存在。其他边界、完整 W 空性及普通 Hilbert 不变子空间问题继续按各自原范围研究。
