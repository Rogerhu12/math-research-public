# $k,\omega$ 同反号：真实几何、左右锚与 $c^8$ 符号的范围

日期：2026-11-14。纸面核对，无新的研究计算。使用 [R45](../results/R45-reversal-four-block-third-period-cancellation.md)、[R56](../results/R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R83](../results/R83-true-fourth-transfer-and-zero-lower-history-variations.md) 与 [R100](../results/R100-pure-tail-c8-period-and-three-true-histories.md)。

**结论。** $h\mapsto h,k\mapsto-k,\omega\mapsto-\omega$ 是合法的真实 scalar 路径变换。它确使 R100 的短 action 反号，但其准确几何识别同时反转 ruling 坐标，$\xi$ 反射还交换左右 Volterra 锚。完整零矩阵不支付每条 ruling 的锚差。因此这项反号不产生同一正物理区间、同一 profile、同一 $M=T=0$ 类中的负第四成本。若各阶完整 range 已支付，则这是环境旋转加材料坐标反射下的等价问题。

## 1. 保持正向 $s$ 的真实 frame 变换

本模型的 ruling 方向是 $N$：

$$
F=(T,N,B),\qquad F_s=F\Omega(k),\qquad
\Omega(k)=\begin{pmatrix}0&-k&0\\k&0&1\\0&-1&0\end{pmatrix},
$$

$$
\alpha_s=h^2T,\qquad X(s,u)=\alpha(s)+uN(s),\qquad
\omega_s=\frac{k_s}{2h},\qquad \xi=h/u-\omega.
\tag{1}
$$

令

$$
\widetilde h=h,\quad \widetilde k=-k,\quad
\widetilde\omega=-\omega,\qquad
S=\operatorname{diag}(-1,1,1),\quad A=-S=\operatorname{diag}(1,-1,-1).
$$

有 $\Omega(-k)=S\Omega(k)S$，且新的 $\omega$ 仍满足 (1)。取初始 frame 为 $I$、初始位置为 $0$，则

$$
\widetilde F=SFS\in SO(3),\qquad
\widetilde T=AT,\quad \widetilde N=-AN,\quad
\widetilde B=-AB,\qquad \widetilde\alpha=A\alpha.
\tag{2}
$$

所以

$$
\boxed{\widetilde X(s,\widetilde u)=A X(s,-\widetilde u).}
\tag{3}
$$

$A$ 是准确的 proper 环境旋转，不是把负方向时间当正时间。若原路径 frame 闭合，变换后亦闭合；R45 的末 frame $D=\operatorname{diag}(-1,1,-1)$ 与 $S$ 对易，亦保持该端口。中心线闭合或 R45 四块的位移相消也由 (2) 保持。

scalar 端芽则按其实际数值变换。只有原端芽被这项变换固定时，才能无需连接直接拼回原端口；例如 $(k,\omega)=(0,0)$ 被固定。对其他端芽需要的真实连接及其高阶成本不能略去。

## 2. 正物理半线没有在这项识别中保持

为比较 (3) 中对应的材料点，必须取

$$
\widetilde\xi=-\xi,\quad \widetilde z=-z,\quad
\widetilde u=-u,\quad \widetilde e=-e,
\qquad z=\xi+\omega,\quad e=hz-k.
\tag{4}
$$

原来 $z>0$ 的活动区间由此对应新的 $\widetilde z<0$ 区间，不能同时称为 R83 的同一正物理支。R56 的局部公式仅需 $z\ne0$；负支本身仍正则，因为

$$
|X_s|^2=(h^2-ku)^2+u^2>0.
$$

但使用负支来识别同一几何，与另选一个新的正支是不同的比较。对有限路径当然可以另选远右的共同紧区间使两组 scalar 数据都满足 $z>0$，此时并未保持 (4) 所对应的同一材料带和 profile。

同时将 $\xi$ 平移、$\omega$ 反向平移不改变 $z$，因此不能在保持 (3)–(4) 的情况下把负支修成正支。单独改变 $\omega$ 或重新选择 profile 区间须作为新物理定义处理，不能只使用 $c^8$ 最高系数的平移性质替代完整周期的比较。

## 3. $C,D$ 与三个真实历史的准确变换

以下所有带反射的旧函数均在 $\xi=-\widetilde\xi$ 或 $c=-\widetilde c$ 处比较。固定 $s$ 正向不变，令

$$
K_0=kz^2-\frac{k^2+1}{h}z,\quad
\lambda=-\partial_s(z/h),\quad K=K_0+\lambda_s,
\quad C=\frac{K(1+e^2)}{8h},\quad D=\frac{Ke}{4}.
$$

直接由 (4) 得

$$
\widetilde K_0=-K_0,\quad \widetilde\lambda=-\lambda,
\quad\widetilde K=-K,\qquad
\widetilde C(c)=-C(-c),\quad \widetilde D(c)=D(-c).
\tag{5}
$$

采用同一零入历史，R100 的 $B_j'=C_j,J_j'=D_j$ 因而满足

$$
\widetilde B_j=(-1)^{j+1}B_j,\qquad
\widetilde J_j=(-1)^jJ_j.
\tag{6}
$$

在同 scalar 常端芽的周期系数类中，$\int C(c)ds=\int D(c)ds=0$ 连同真实 R20 迹身份等价于完整 $M=0$。为看清无遗漏，写已完成分部积分的 $\overline C=B_0+cB_1+c^2B_2$、$\overline D=B_1+2cB_2$。若两多项式恒零，R7/R20 的八参数表示先迫 $p_1,p_2,r_0,r_1,s_0,t_1=0$，再迫 $s_1=p_0/2,t_0=-p_0/4$；真实身份 $p_0/2+s_1-2t_0=0$ 迫剩余三数也为零。因此 (5) 保持完整零矩阵条件。这里的周期系数 $B_i$ 与 (6) 的 primitive 系数 $B_j$ 是不同对象。

用 R100 的记号

$$
p=B_4,\quad \eta=\omega-k/h,\quad
\ell=B_3-J_2/2-\eta p,\quad \zeta=B_3-4\eta p,
$$

则 (6) 给

$$
\widetilde p=-p,\qquad \widetilde\eta=-\eta,
\qquad\widetilde\ell=\ell,\qquad\widetilde\zeta=\zeta.
\tag{7}
$$

于是短式

$$
\mathcal R_8=\frac25p(\zeta+10\ell)\zeta_s
-\frac25\frac{k}{h}p^2-\frac1{20}p_s\zeta_s-\frac15p_s\ell_s
$$

严格满足 $\widetilde{\mathcal R}_8=-\mathcal R_8$。R100 的端势也反号。这是一个真实 $M=0$ 路径系数恒等式；它本身没有证明同锚完整第三算子 $T$ 被保持，也没有把一个完整第四成本函数取负。

## 4. profile、三矩与真正的右原函数

令 $I=[a,b]$、$\widetilde I=[-b,-a]$，用 $\mathscr Rf(x)=f(-x)$ 表示 profile 反射。对实或普通复双线性 profile，其三个真正矩

$$
\mathsf M_0(q)=\int q''{}^2,\quad
\mathsf M_1(q)=\int \xi q''{}^2,\quad
\mathsf M_2(q)=\int(\xi^2q''{}^2+2q'{}^2)
$$

变为 $(\mathsf M_0,-\mathsf M_1,\mathsf M_2)$。因此复三矩零，以及相应实 $f,g$ 的三矩等长、正交圆条件，均被保持。

第一场也没有未明符号。其 frame 分子是

$$
V_\phi=(-\phi'/2,0,h\phi-e\phi'/2),\qquad Y_\phi=FV_\phi/z.
$$

对 $\widetilde\phi=\mathscr R\phi$，有 $\widetilde V=S\mathscr RV$，所以

$$
\widetilde Y_{\mathscr R\phi}=A\mathscr RY_\phi.
\tag{8}
$$

不过，带符号右原函数 $I_bf(\xi)=\int_b^\xi f$ 的准确反射为

$$
\boxed{I_{-a}(\mathscr Rf)
=-\mathscr R(I_af)
=-\mathscr R(I_bf)-\int_a^b f.}
\tag{9}
$$

最后一项是真正的全带积分。不能因几何 period 矩阵为零就将它逐 $s$ 删除。幂尾 $q=(c-\xi)^8$ 的右端邻域在反射后是旧左端邻域；新右尾与旧右尾之间没有由 (8) 给出的同锚等同。

## 5. 每一阶 range 的完整锚差

考虑一个确由已知向量场共同反射产生的二次 forcing $H$。R56 的分子配对满足

$$
\widetilde T_\xi=\mathscr RT_\xi,\quad
\widetilde T_s=\mathscr RT_s,\quad
\widetilde T_{s\xi}=-\mathscr RT_{s\xi},\quad
\widetilde J=\mathscr RJ.
$$

定义本阶 ruling 缺陷

$$
\mathfrak h_H(s)=\frac1{2h(s)}\int_a^bT_\xi(s,\xi)\,d\xi.
$$

R56 中 $P=-I_bT_\xi/(2h)$、$B=J/(2h)$、$\rho=P+B/z$。由 (9) 得

$$
\widetilde P=-\mathscr RP+\mathfrak h_H,
\qquad\boxed{\widetilde\rho=-\mathscr R\rho+\mathfrak h_H.}
\tag{10}
$$

因此完整 characteristic 密度准确变为

$$
\boxed{\widetilde{\mathcal R}_H
=\mathscr R\mathcal R_H-(\mathscr RK_0)\mathfrak h_H
+(\mathscr R\lambda)(\mathfrak h_H)_s.}
\tag{11}
$$

常 scalar 端芽给 $\lambda(0,\xi)=\lambda(L,\xi)=0$，积分得到

$$
\boxed{\widetilde\Pi_H
=\mathscr R\Pi_H-\mathscr R\int_0^L K(s,\xi)\mathfrak h_H(s)\,ds.}
\tag{12}
$$

若不作常芽假设，还须保留边界项 $[\mathscr R\lambda\,\mathfrak h_H]_0^L$。式 (10) 的附加项不是一般的齐次 $Y_\psi$：它首先改变 normal ruling 恢复。

当**本阶完整 ruling 已付**时，$\mathfrak h_H=0$，才由 (11)–(12) 直接得到相同符号的拉回

$$
\widetilde\Pi_H=\mathscr R\Pi_H.
\tag{13}
$$

以同一个零 $s$ 锚积分还给 $\widetilde W=\mathscr RW$、$\widetilde\eta_0=-\mathscr R\eta_0$。代入 R56 完整恢复分子 (7)，恢复场就是 $A\mathscr RZ$，故可逐阶继续。

这特别说明第四层的条件边界：先付第二、第三完整 range，能够保证第四向量 forcing 确实按 (8) 反射；它仍不自动支付第四 ruling。第四 canonical period 此时一般仍应使用 (12)。若第四 ruling 已为零，或已通过一个合法全局第三 gauge 支付后再比较，才可直接使用 (13)。不能提前抹去这一项。

## 6. 对真实第四成本问题的结论

完整几何问题在 (3) 的环境旋转和材料反射下等价。准确可解的二阶、三阶以及第四阶场均可这样传送；这不改变“存在满足两 collar 的完整第四解”这一事实。相反，只有 universal $M=0$ 或甚至原同锚 $M=T=0$ 时，未付的逐 $s$ ruling 锚差仍须逐阶处理，不能单从 scalar 符号替换推导新右锚第四成本。

R100 的 $c^8$ 系数反号同时改变了 profile 端点的左右角色；它不与 (13) 矛盾。它提供真实 $M=0$ 系数的对称核对，尚未给同一正物理支、同一 profile 圆的 $V\mapsto-V$，也没有产生 R83 第四成本半群的逆元。

下一步如需利用反射构造负成本，必须另外给出：相同实际端口的有限连接、保持共同 profile/物理域的操作、逐阶左右锚缺陷的真实支付，以及完整第四成本的比较。这些成本不能被短 action 的一个系数反号代替。
