# R621 — 原 norm8 极点行的有限六度补偿与同中央边界

日期：2026-11-14。**状态：已证明。**

继续 R617 的两个实际极点总行 $P_1,P_2$。
本篇在同一个原 $B_C\otimes\sigma$ 输入上使用 R533 的完整
六度核，并作有限有理除法。其余真实来源的低矩使全部主部只留下
原固定 $I_1$，没有增加一个未知负矩池：
$$
P_1=-36b_K\Omega^5I_1+\mathcal B_1,\qquad
P_2=-12\alpha\Omega^5I_1+\mathcal B_2 .
$$
两个余项均分成同样三类明确真域，源和权各自保留。
因此 $\alpha P_1-3b_KP_2$ 完整消去 $I_1$。
R617 的同两个 native 环带分别提取 $P_1,P_2$，遂给原中央和这些
有限补偿之间的真实关系。

原四单位条件、原 $q$ 的精确坐标以及全部单位切集均显示。
本篇没有证明 $\mathcal B_1,\mathcal B_2$ 或任何混合补域为零，
也不把 R562 的另一条单位测试替换成本篇极点测试。

## 1. 同一来源及 R617 两个条件矩

保持 R617 的全部规范和固定坏集：
$$
b=17,\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1 .
$$
记
$$
\alpha=1+3\omega,\quad \gamma_d=2+3\omega,\quad
R=\alpha c+d,\quad K_0=c+\gamma_dd,
$$
$$
a_Z=(-2+\omega)/2,\quad a_Q=(4+3\omega)/2,\quad
b_K=-(1+6\omega)/8,\quad a=-3\omega/8,
$$
$$
V_0=a_ZZ+a_QQ+b_KK_0,\quad
V=V_0+2\delta r,\quad Y=V+aR,\quad W=V+(a+2)R .
\tag{1}
$$
原完整来源 $\mu_0$ 仍含独立 $B_C(C)$，不是在混合条件下
重新插入一个已忘去的变量。

R617 付清的第一及第二 $R$ 矩分别是
$$
\begin{aligned}
\nu_1&=\frac{\Omega}{7}\,
 \nu_{B_C}(C)\otimes
 (\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
     -\nu_{f_3}(Z)\otimes\nu_\Theta(Q))
 \otimes\nu_\sigma(r)\otimes\nu_{g_8}(K_0),\\
\nu_2&=\frac{\Omega^2}{42}\,
 \nu_{B_C}(C)\otimes
 (\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
     -\nu_{f_3}(Z)\otimes\nu_\Theta(Q))
 \otimes\nu_\sigma(r)\otimes\nu_{h_8}(K_0),
\end{aligned}
\tag{2}
$$
其中
$$
g_8=x^2y_\wp\sigma^8=-\Theta f_1,\qquad
h_8=\sigma^8\{(2+6\omega)x^4-(40+24\omega)b\,x\}.
\tag{3}
$$
$\nu_k(\varphi)=\int R^k\varphi\,d\mu_0$ 是完整五变量身份。
故本篇的总行准确为
$$
\boxed{
P_k=\nu_k(1_{V\ {\rm unit}}V^{-k})
=\mu_0(1_{V\ {\rm unit}}R^k/V^k),\qquad k=1,2 .
}
\tag{4}
$$
它们就是原 norm8 环带的实际第一、第二修正项。

## 2. 原 B 与原 sigma 的完整六度核

不动 $(Z,Q,K_0)$，只在原 $(C,r)$ 上取
$$
\boxed{
H=\delta(C-r),\qquad K_b=\delta(C+r),\qquad
C=(H+K_b)/(2\delta),\quad r=(K_b-H)/(2\delta).
}
\tag{5}
$$
行列式 $2\delta^2=-6$ 是当前单位。
$B_C(z)=B(z/\delta)$，所以整个两变量生成函数准确成为
$$
B(h+k)\sigma(\delta(k-h))
=-\omega^2 B(h+k)\sigma(a_3(k-h)),
\qquad a_3=2+\omega,\quad \delta=-\omega^2a_3.
$$
也就是
$$
\boxed{(H,K_b)_*(\nu_{B_C}\otimes\nu_\sigma)
       =-\omega^2\nu_{F_B},}
\tag{6}
$$
其中 $F_B$ 正是 R533 的整个核
$$
F_B=a_3\{\mathsf H\wedge f_1+6b\,f_3\wedge f_4\},\qquad
\mathsf H=(x^3-2b)\sigma^6,\quad \mathsf H(0)=1 .
\tag{7}
$$
两个轴的度数均为 $6$，交叉项为零；两个 odd 输入的半特征之积
正是 R533 的标准 even 半特征。固定 CM 单位 $-\omega^2$ 已在
(6) 中保留，没有未付的整体符号。

整个 $\mathcal S_6$ 的原核心为 $\beta$，故在本完整联合中，
保 $(Z,Q,K_0)$ 和其他全部条件，有
$$
\nu_{F_B}|_{\{H\in p^u,K_b\in p^v\}}
=\beta^{u+v}[\kappa^u,\kappa^v]_*\nu_{F_B}.
\tag{8}
$$
本篇在实际补域中使用 (8)，不由核直接赋中央零。

令
$$
T(Z,Q)=\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
          -\nu_{f_3}(Z)\otimes\nu_\Theta(Q),
$$
$$
\rho_1=T\otimes\nu_{g_8},\qquad
\rho_2=T\otimes\nu_{h_8},\qquad
\zeta_k=\nu_{F_B}(H,K_b)\otimes\rho_k(Z,Q,K_0),
$$
$$
s_1=-\omega^2\Omega/7,\qquad
s_2=-\omega^2\Omega^2/42 .
\tag{9}
$$
这里 $\rho_1,\rho_2$ 是不同的实际来源。
用
$$
U=V_0+K_b,\qquad V=U-H,
$$
(4) 准确写成
$$
\boxed{P_k=s_k\int 1_{V\ {\rm unit}}V^{-k}\,d\zeta_k.}
\tag{10}
$$

## 3. 同一个 q 与原四单位域的全坐标

置
$$
F_0=\delta Z/6+(1-2\omega)Q/2+K_0,\qquad
G_0=-\frac{32+31\omega}{6}Z+\frac{-14+\omega}{2}Q+(3-2\omega)K_0 .
$$
原正 carry 的行在 (5) 中准确为
$$
\boxed{
\begin{aligned}
D=F-C&=F_0+\{(-2-\omega)K_b+\omega H\}/(2\delta),\\
E=F+13C&=F_0+\{(12-\omega)K_b+(14+\omega)H\}/(2\delta),\\
G&=G_0+(21-3\omega)(K_b-H)/(2\delta).
\end{aligned}}
\tag{11}
$$
这里的 $H$ 专指 (5) 的六度轴。
R613 的旧轴记为 $H_{613}=J+11C$，
其中 $J=\omega(Z-Q)/2+\omega^2r+K_0$；
旧 $A=J-C$、$L=(Z+3Q)/2$ 都按 (5) 准确恢复。
所以原 $\mathscr X_n,\mathscr E_n$ 的条件也全部保留。
$\tau$ 固定本篇 $H,K_b,K_0$，负 carry 只把
$F_0,G_0$ 的 $(Z,Q)$ 行换成各自的 $\tau$ 行；
不与正支或旧 $H_{613}$ 相认。

因此原 $q_{+,n}$ 仍是
$$
\frac{1_{\Gamma_{+,n}}}{b\Omega^6}
\widehat P_p(D/\kappa^n,E,G),\qquad
\Gamma_{+,n}=\{H+K_b\ {\rm unit},\ D\in p^n\}.
\tag{12}
$$
$n\ge1$ 时，(12) 已自动给原 $F$ 单位。
$\widehat P_p$ 的全部 $\lambda,\kappa$ 系数均为原 R594 那一组。

若使用 (8) 的 $H$ 深核，则 (11)–(12) 全部把 $H$ 换成
$\kappa^uH$；$V$ 同时变成 $U-\kappa^uH$。
没有把 $q$、$V$ 或原 $Y/W$ 认成这个核心的不变量。

R562 的原四单位域，在当前实际 sigma 输入 $r$ 与
$B$ 输入 $v=\delta C$ 中，准确为
$$
\boxed{
\mathscr F_4=\{H,K_b,H+K_b,H-K_b\ {\rm unit}\}.
}
\tag{13}
$$
它就是 $\{r,v,H,K_b\ {\rm unit}\}$；
反射一个六度轴的负号不改变这个集合。
但 R562 的 $r^3(H^{-2}+K_b^{-2})/2$ 与 (10) 的 $V^{-k}$
是不同测试，不能只因同域就互相替换。

本篇 (10) 的总行可先合法删除完整 $q$，因为 (4) 是原
$\pi_4$ 测试，R594 已付
$$
\int_{\Gamma_{+,n}}q_{+,n}\,
 1_{V\ {\rm unit}}R^k/V^k\,d\mu_0=\beta^nP_k .
\tag{14}
$$
(14) 只能用于 cap/ex 完整相加后的总行。
对单个 cap、ex 或附加 (13) 的支，必须保 (11)–(12)；
下面的全来源变化和有理恒等式仍适用，但不得免费进行第 4 节的
无 cut 矩消去。

## 4. 两个 cofactor 的实际低矩

$T$ 的总阶至少为三。$g_8=-z+O(z^7)$，
$h_8(0)=2\alpha$，故
$$
\boxed{
\rho_1(V_0^j)=0\ (0\le j<4),\qquad
\rho_2(V_0^j)=0\ (0\le j<3).
}
\tag{15}
$$
这些是整个来源的正矩，不只模 $p$ 的近似。
原低阶矩直接给
$$
\begin{aligned}
\rho_1(V_0^4)
 &=24a_Zb_K(a_Z^2-a_Q^2)\Omega^4
   =(231/2+42\omega)\Omega^4,\\
\rho_2(V_0^3)
 &=12\alpha a_Z(a_Q^2-a_Z^2)\Omega^3
   =(210+42\omega)\Omega^3 .
\end{aligned}
\tag{16}
$$
例如第一式两项分别来自 $ZQ^2K_0$ 和 $Z^3K_0$，
其多项式系数为 $-24a_Za_Q^2b_K$、
$+24a_Z^3b_K$。第二式使用 $h_8$ 的真实质量 $2\alpha$。
没有省掉该非零质量。

由于 $U=V_0+K_b$，(15) 同时给
$\rho_1(U^4)=\rho_1(V_0^4)$、
$\rho_2(U^3)=\rho_2(V_0^3)$，且所有更低次矩全零；
右侧完全不含 $K_b$。
R533 的整个条件负五行为
$$
\boxed{
\int_{H\ {\rm unit}}H^{-5}\,d\nu_{F_B}(H,K_b)
=-a_3 I_1\,d\nu_{\mathsf H}(K_b),
\quad
I_1=\int_{\mathbf Z_p^\times}x^{-5}\,d\nu_{f_1}(x).
}
\tag{17}
$$
最后 $\nu_{\mathsf H}$ 的**完整**质量是 $1$。
这里没有提前附加 $K_b$ 单位条件。

## 5. 有限除法及三个完整补偿域

只在 $H$ 单位时定义下列有界函数：
$$
T_1(U,H)=-\sum_{j=0}^4 U^jH^{-j-1},\qquad
T_2(U,H)=\sum_{j=0}^3(j+1)U^jH^{-j-2}.
$$
在 $H,V$ 都为单位时定义
$$
R_1(U,H,V)=\frac{U^5}{H^5V},\qquad
R_2(U,H,V)=\frac{U^4(5H-4U)}{H^5V^2}.
\tag{18}
$$
下列是有限有理恒等式，不需要 $U/H$ 小：
$$
\boxed{V^{-1}=T_1+R_1,\qquad V^{-2}=T_2+R_2,\qquad V=U-H.}
\tag{19}
$$

定义三类实际补偿，$k=1,2$：
$$
\begin{aligned}
B_k^{(0)}
 &=s_k\int_{\{H\in p,\ V\ {\rm unit}\}}V^{-k}\,d\zeta_k,\\
B_k^{(c)}
 &=-s_k\int_{\{H\ {\rm unit},\ V\in p\}}T_k(U,H)\,d\zeta_k,\\
B_k^{(r)}
 &=s_k\int_{\{H,V\ {\rm unit}\}}R_k(U,H,V)\,d\zeta_k,
\qquad
\mathcal B_k=B_k^{(0)}+B_k^{(c)}+B_k^{(r)} .
\end{aligned}
\tag{20}
$$
三个被积函数都整有界。特别 $B_k^{(c)}$ 使用显示的有限多项式，
不在 $V\in p$ 上解释一个未经相消的 $1/V$。

把 (10) 先分成 $H$ 深／单位，再在单位支使用 (19)，得到
$$
P_k=s_k\int_{H\ {\rm unit}}T_k\,d\zeta_k+\mathcal B_k .
\tag{21}
$$
(15)–(17) 使第一项完全可算。
没有使用 $I_3=0$、$I_4=0$ 或任何新的负矩值：
$$
\boxed{
P_1=d_1\Omega^5I_1+\mathcal B_1,\qquad
P_2=d_2\Omega^5I_1+\mathcal B_2 ,
}
$$
$$
\boxed{
d_1=9/2+27\omega=-36b_K,\qquad
d_2=-12-36\omega=-12\alpha .
}
\tag{22}
$$
第一式主部只有 $-U^4H^{-5}$，第二式只有 $4U^3H^{-5}$；
其他主部在**完整 cofactor 积分**后由 (15) 严格为零。
将 $s_1,s_2$、$-\omega^2a_3=\delta$ 和 (16) 相乘，
即得 (22) 的绝对系数。

范数为
$$
N(d_1)=3^4\cdot31/4,\qquad N(d_2)=2^4\cdot3^2\cdot7 .
$$
$31\not\equiv7\bmod64$，故两者在整个当前射线都是单位。
本篇没有新增射线或坏素数。

## 6. 原四单位补域的完整有限分割

在 (20) 的两条 $H$ 单位域中，精确有不交分割
$$
\{H\ {\rm unit}\}=\mathscr F_4\sqcup\mathscr E_0
                      \sqcup\mathscr E_+\sqcup\mathscr E_- ,
$$
$$
\begin{aligned}
\mathscr E_0&=\{H\ {\rm unit},K_b\in p\},\\
\mathscr E_+&=\{H,K_b\ {\rm unit},H+K_b\in p\},\\
\mathscr E_-&=\{H,K_b\ {\rm unit},H-K_b\in p\}.
\end{aligned}
\tag{23}
$$
$p\ne2$ 使 $\mathscr E_+,\mathscr E_-$ 不交；
若 $K_b$ 深而 $H$ 单位，两个 $H\pm K_b$ 自动单位。
所以 $B_k^{(c)}$、$B_k^{(r)}$ 可按 (23) 分成四个真实积分，
并分别保 $V$ 深／单位指示。
这正保原 $r$、$C$ 单位失败的两支以及第二六度轴深支。
它们不是假想的独立纤维。

第一条深支还有完整已付核返回：
$$
\boxed{
B_k^{(0)}
=s_k\beta\int_{\{U\ {\rm unit}\}}
       (U-\kappa H)^{-k}\,d\zeta_k .
}
\tag{24}
$$
这是 (8) 直接作用于同一域的结果；$H$ 缩放后，
$U-\kappa H$ 为单位当且仅当 $U$ 为单位。
若附原 $q$ 或其他条件，须同时用 (11) 把 $H$ 替换为 $\kappa H$。
(24) 没有将任何条件质量或新的移权矩赋零。

## 7. 消去 I1 的实际有限关系

(22) 直接给
$$
\boxed{\alpha P_1-3b_KP_2
       =\alpha\mathcal B_1-3b_K\mathcal B_2.}
\tag{25}
$$
$I_1$ 在这条式子中完全消去，而两种真实来源
$\zeta_1,\zeta_2$ 和各自权仍分别保留。
(25) 不是将两个补偿错误地认成同一边际。

现用 R617 的原中央和原 norm8 环带：
$$
\mathcal T=J'_S-6\delta J'_T,\quad
A_m=\int_{\{R\notin p^{2m}\}}\ell\,d\mu_0,\quad
S_m=\lambda^{-2m}\kappa^{-2m}(\mathcal T-A_m).
$$
该篇已证明
$$
S_m=-2d_pP_1+d_p\ell_2\kappa^{2m}P_2+p^{4m}\mathcal O,
\qquad \ell_2=2-3\omega/4 .
\tag{26}
$$
$N(\ell_2)=97/16$，而 $97\not\equiv7\bmod64$，
所以仍不增加例外。
同两个实际环带分别提取两行：
$$
\boxed{
\begin{aligned}
\mathsf P_m
 &=-\frac{S_{m+1}-\kappa^2S_m}{2d_p(1-\kappa^2)}
   =P_1+p^{4m+2}\mathcal O,\\
\mathsf Q_m
 &=\frac{S_{m+1}-S_m}
       {d_p\ell_2\kappa^{2m}(\kappa^2-1)}
   =P_2+p^{2m}\mathcal O .
\end{aligned}}
\tag{27}
$$
所有负归一幂作用于已经付清的完整差；
没有分拆估值后删项。
于是原中央及同两个 native 环带满足
$$
\boxed{
\alpha\mathsf P_m-3b_K\mathsf Q_m
=\alpha\mathcal B_1-3b_K\mathcal B_2+p^{2m}\mathcal O .
}
\tag{28}
$$
每个 $A_m$ 仍可用 R617(23) 写成**同一个**
$q_{+,n}$ 的 cap/ex 环带之和，再准确乘 $\beta^{-n}$。
因此 (28) 连接的就是原总行及其完整真实补偿。

## 8. 与 R617 极点外矩形的单位联立

R617 的记号保持：
$$
c_\tau=(-323-360\omega)/343,\qquad
\varepsilon_{\rm pole}=(-1255680-1105920\omega)/117649 ,
$$
$B_n^{\rm pole}$ 是该篇 (38) 中完整的新三深矩形外域，
包含两个各自的单位指示。
它已付
$$
-(1+c_\tau)P_1-B_n^{\rm pole}
=\beta^{3n}\varepsilon_{\rm pole}\Omega^5\kappa^{4n}I_1
+p^{8n}\mathcal O .
$$
用 (22) 的**完整有限式**消去 $I_1$，令
$$
t_n=\beta^{3n}(\varepsilon_{\rm pole}/d_1)\kappa^{4n},
\qquad u_n=1+c_\tau+t_n .
$$
$N(1+c_\tau)=400/343$，$t_n\in p^{4n}\mathcal O$，
故 $u_n$ 对所有当前素数、所有 $n\ge1$ 为单位。
严格得到
$$
\boxed{
u_n P_1=-B_n^{\rm pole}+t_n\mathcal B_1+p^{8n}\mathcal O,
}
\tag{29}
$$
以及只用原中央和同两个环带的
$$
\boxed{
u_n\mathsf P_{2n}
=-B_n^{\rm pole}+t_n\mathcal B_1+p^{8n}\mathcal O .
}
\tag{30}
$$
它保原固定 $I_1$ 的全部规范，但不再引入另一个未知负矩。
右侧两个补偿仍是完整实际积分，不能只因系数是单位就将它们删掉。

## 9. 范围与未付项

若原 $J'_S=J'_T=0$，只可令 (26)–(30) 中
$\mathcal T=0$。这确实强制显示的 native 环带与三类有限补偿
满足 (28)、(30)，但还没有使 $P_1$、$P_2$ 或 $\mathcal B_k$ 为零。

特别，原四单位证书控制的是它的特定测试；本篇的
$V=V_0-H+K_b$ 会移动该测试。
(23) 的四个 $H$ 单位分支和 (20) 的 $H$ 深支全都保留。
当前剩余问题已具体化为这些同来源、同单位 cut 的有限补偿，
而不是一个可自由赋零的“外域”。

本篇未把 R594 原 $\mathcal D_n$ 的局部赋值移给任何新域，
也未用固定系数范数去断言依赖 $p$ 的 $I_1$ 非零。
课题主目标仍待此实际补偿与原算术零的进一步比较。

## 精确文件与依赖

- [check-r621-original-six-degree-finite-pole-compensation.js](../scripts/check-r621-original-six-degree-finite-pole-compensation.js)
- [check-r621-original-six-degree-finite-pole-compensation.json](../scripts/check-r621-original-six-degree-finite-pole-compensation.json)
- [R533：完整六度外积及条件负五行](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)
- [R562：原四单位域与实际负二关系](R562-original-four-unit-domain-and-negative-two-unit-relation.md)
- [R594：同一完整 q](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)
- [R613：两个 carry 的完整 cap/ex](R613-original-reflected-carry-intersection-and-complete-two-state-return.md)
- [R617：原 norm8 环带及两条条件矩](R617-original-norm8-annulus-and-negative-five-pole.md)

BigInt 证书保存全五坐标变换、所有 D/E/G/V 行、CM 绝对系数、
两个完整 cofactor 矩及单位范数、两条有限有理恒等式。
无限环带、条件负矩、原 q 的量词和全部真域由正文证明。
