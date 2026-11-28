# 正确 h=k、Delta=0 图的完整原 Loww 纤维与8664个规范点界

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：完整证明。** 在原
$$
h=k,\qquad \Delta=0,\qquad ABQ(1-Q)P_f\,bcP_{02}\ne0
\tag{1}
$$
的正确物理图内，每个固定 $(\lambda,u,Q)$ 上至多有三个原 $z$。结合[全部 Q 纤维及1444三参数点界](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Q-fibers-1444-cover.md)，完整有序规范的不同原 Gram 与原值点至多 **8664**。

这里包括全部 $z$ 首项退化和两个 $\rho$ 嵌入；不把不同点数界当作非约化 scheme 长度。$P_f=0$ 补图和当前有限点的逐点排除仍须继续。本稿不恢复旧错误848/578或旧整 Delta 排空。

## 1. 整个原 h=k 图上的一个非零值

沿用正确碰撞矩关系
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\ell=A^3/B^2,\quad T=A^2/B,\quad
\xi=B/A,\quad h=k=1+\xi,\quad
w=\lambda-1-T.
\tag{2}
$$
直接展开有完整多项式身份
$$
(\lambda-1)B-A^2=-\lambda^2(2\lambda-1).
$$
所以
$$
\boxed{w=-\frac{\lambda^2(2\lambda-1)}B.}
\tag{3}
$$

原非零孤立 mean 图已付 $\lambda\ne0$；整个 $\lambda=1/2$ 的真实原五列排除见[正确对称 u=1 原证明中的准确引用](R150-appendix-unit211-h-equals-k-entire-symmetric-u-one-original-exclusion.md)及[三份原源静核](../notes/2026-11-28-hk-Szero-true-original-static-source-audit-8542.md)。
这些来源使用真实双点乘法，而非已撤回的紧凑 $R_{\rm bad}$。
因此 (1) 内的 $w$ 和 $2\lambda-1$ 都非零。

## 2. 同一个 z 上的完整仿射原恢复

固定 (1) 内的 $(\lambda,u,Q)$，取全部
$$
\rho^2=1-Q,\quad p=1+\rho,\quad q=1-\rho,\quad
m=u-\ell,\quad
b=\frac{\ell+m/\rho}2,\quad c=\frac{\ell-m/\rho}2.
$$
置
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,
$$
$$
\Phi=T_0+4u-4+Q,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,
$$
$$
P_f=T_0(J-Q),\quad
G=\lambda P_{02}+(u-1)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0.
$$
正确原恢复为
$$
z=Qt,\qquad
f=-\frac{P_c+bc\Phi z}{P_f},\qquad
v_n=Jf-G+bc z,\qquad V=v_n/Q.
\tag{4}
$$
再令
$$
W_1=(T_0+4uf)/2,\qquad
M=4bc(1-Q)=\ell(2u-\ell Q)-u^2,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y_0=\frac{\ell W_1-uV}{M},
$$
$$
X=x+\rho y_0,\quad Y=x-\rho y_0,\quad
A_1=2f-2V+2bc t,
$$
$$
r=X-(1-\ell)p-ct,\qquad s_{\rm G}=Y-(1-\ell)q-bt.
\tag{5}
$$

在固定三参数和任一 $\rho$ 根上，(4)–(5) 的每个原 Gram 坐标都对 $z$ 仿射。
全部分母在 (1) 非零，与 $z$ 无关；没有 $\Delta$ 逆，也没有新的 $z$ 首项逆。

$X,Y$ 是原两个 simple 位置的 $d$ 坐标，完整原 Gram 四行是
$$
(0,0,p,q),\quad(0,A_1,r,s_{\rm G}),\quad
(p,r,0,t),\quad(q,s_{\rm G},t,0).
$$
所有恢复都是同一点的原公式，不是分别投影后再拼接根。

## 3. 完整原 Loww 给一个常数项非零的三次

引用[全自由 f、t 的原低加权 N/P 恒等式](R150-appendix-unit211-unrestricted-f-and-t-original-low-weighted-NP-identities.md)。
在此对称规范 $\sigma=p+q=2$，写
$$
S_x=X+Y,\qquad P_x=pX+qY,\qquad \eta=f-u,
$$
$$
K_w=2\bigl[t^2+(5u-2S_x-2)t
+2XY+2P_x-2uS_x+2u^2-6u+Q\bigr],
$$
$$
\widehat K_w=K_w+4\eta(t-2).
\tag{6}
$$
完整原条件的一个必要组合为
$$
\boxed{
L_w(z):=2P_{02}(2\lambda-1)w-bc\,t\,\widehat K_w=0.
}
\tag{7}
$$
它的真实来源是
$$
L_w=NS-PS-\frac13p_j+(1-\ell)n_0
-\bigl(d_1-2\ell u-2\eta\bigr)E_0+E_{W,2},
\tag{8}
$$
采用该已刊原恒等式的准确记号。所有右端原方程在原解都为零。
在已经恢复 $E_0,n_0,p_j$ 的图上，(7) 也可写成 $NS-PS+E_{W,2}$。
本稿使用的是 (6)–(8) 的完整自由 $\eta$ 修正，不提前令 $f=u$。

由 (4)–(5)，$t,X,Y,\eta$ 对 $z$ 至多一次；
故 $K_w,\widehat K_w$ 对 $z$ 至多二次。因此
$$
\deg_z L_w\le3.
\tag{9}
$$
同时 $t=z/Q$，所以在 $z=0$ 直接有
$$
\boxed{
L_w(0)=2P_{02}(2\lambda-1)w
=-\frac{2P_{02}\lambda^2(2\lambda-1)^2}{B}\ne0.
}
\tag{10}
$$
(10) 不声称 $z=0$ 是物理原点；它只是当前多项式的一个准确系数值。
没有借该点的 Gram 非退化性，也不需要构造原 $t=0$ 的解。

(9)–(10) 证明 $L_w$ 在每个完整固定三参数纤维都是一个非零三次以下多项式。
故所有原 $z$ 至多有三个。降成二次、一次或非零常数时只会减少点数。
这里无需付它的最高次系数，所以不存在遗漏的首项零面。

$\rho$ 的两个选择给相同 $L_w$：$S_x,XY,P_x$ 都对 $\rho$ 反号不变。
即使不使用此不变性，分别计两个嵌入仍给下节相同的安全上界。

## 4. 计数与一个可继续使用的首一环境

已刊完整三参数界为1444。每个三参数点由 (9)–(10) 至多有三个 $z$，
故不同 $(\lambda,u,Q,z)$ 至多
$$
1444\cdot3=4332.
$$
$\rho^2=1-Q$ 保留两种复根；每个根通过 (4)–(5) 唯一确定
$b,c,f,t,A_1,r,s_{\rm G}$ 等完整有序 Gram 参数。
原值 $w,h,k$ 则由 (2) 唯一决定；因为 $h=k$，没有额外的两个 simple 值选择。
因此完整有序规范的不同原点数至多
$$
\boxed{2\cdot4332=8664.}
\tag{11}
$$

还可保留不除首项的后续必要环境。
整个原 $h=k,t=0$ 已由[完整原低式排除](R150-appendix-unit211-entire-tzero-half-total-weight-and-hk-exclusion.md)处理，
故当前图已有 $z\ne0$。令 $\zeta=1/z$，
把 (7) 写为 $L_w=c_0+c_1z+c_2z^2+c_3z^3$，
其中 (10) 的 $c_0$ 是准确原单位。于是所有原点满足首一
$$
\boxed{
\zeta^3+\frac{c_1}{c_0}\zeta^2+
\frac{c_2}{c_0}\zeta+\frac{c_3}{c_0}=0.
}
\tag{12}
$$
这里的 $\zeta$ 仅是原 $z$ 的倒数，不是新的原几何自由度；
$\zeta=0$ 的环境点仍不能认作物理原点。
(12) 给后继完整有限代数一个新的首一必要输入，但本稿没有执行这种代数或宣布其长度。

## 5. 来源、检查及保留范围

本稿是已刊正确原定义和全自由 Loww 恒等式的直接纸面合成。
root 与 r150_open_geometry 独立核了 (3)、仿射恢复、次数、非零常数项以及完整点数。
没有新数学执行，也没有重新展开原 Loww 大系数。

特别，本稿没有重启 dc888 的两个冻结 z 结果式，没有调整其顺序或预算，
也没有再算已成722/Q纤维投影。证明 (9) 只用准确的代数次数，
证明 (10) 只用原显式常数项；二者均覆盖全部权和首项退化。

(11) 只适用于 (1)。$P_f=0$、其它一般 LS 图、原有限点的排空、
全 Bell 幂与算子桥继续保留；普通复可分无限维 Hilbert ISP 未完成。
