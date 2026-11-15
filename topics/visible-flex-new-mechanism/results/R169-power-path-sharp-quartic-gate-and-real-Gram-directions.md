# R169：真实幂路径的 sharp 四次门与可实现的 Gram 方向

日期：2026-11-15。**已证明。** 本稿仅作纸面推导，不新增原式编译、profile 评价、路径积分或对任何既有外候选的求解。

依据 [R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R148](R148-sharp-one-dimensional-highest-action-positivity.md)、[R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)、[R165](R165-prescribed-h-quadratic-highest-action-and-loglinear-frequency-gate.md) 和 [R167](R167-four-monomial-Gram-certificate-for-complete-highest-action.md)。

本稿把 R167 的有限充分证书与一族真正可实现的必要测试联系起来。沿真实幂曲线 $k=K h^p$，完整最高 action 对振幅 K 的二次部分有一个准确 sharp 判据。它给出关于任意实 p 的四次多项式 $\Omega(p)\ge0$，保留在 R165 长 log-linear 测试中成为端势的 H2 系数。该四次式也恰是 R167 Gram 矩阵沿一条明确向量曲线的取值；这条曲线通过真实有限平端路径的 sharp 极限实现。

本稿不把任意 Gram 负向量当作真实路径，也不将本路径子类的充要判据提升为全部最高 action 或完整成本的充要判据。

## 1. 沿用完整十个最高层标量

令 $\lambda$ 为真实权 −2 仿射字符，杀完整响应空间 R。沿用 R165/R167 的十个标量

$$
a,b,c,d,e,f,g,j,\ell,m.
$$

其中 a、b 来自 $\bar A_{hh}$，c 来自 $\bar A_{hk}$，d 来自 $\bar A_{kk}$，e、f 是两个面积系数，g、j、$\ell,m$ 是完整正规速度四次系数。它们都来自同一真实字符，而不是独立几何控制。

置

$$
r=\log h,\quad v=r',\quad z=r''+(r')^2,\quad \rho=e^{-2r}.
$$

完整已取字符的最高层为

$$
\begin{aligned}
L_4^\lambda=\rho\{&
a z^2+\ell v^4+(bk^2)z^2+c k z k''+d(k'')^2\\
&+(e k v+f k')[v k''-k'z]
+g v^2(k')^2+j k v^3k'+m k^2v^4\}.
\end{aligned}
\tag{1}
$$

式 (1) 保留全部 H 项和已经含真实 $N^{[2]}$ 收缩、边界势微分的 Q4。符号 p 在本稿中仅表示**固定实幂指数**，不表示 profile，也不表示另一稿可能使用的倒数变量 $1/h$。

## 2. 全部幂指数都给真实平端路径

固定任意实 $p,K$，取任意有限时间的正光滑平端 h，并设置

$$
k(s)=K h(s)^p.
\tag{2}
$$

因 h 严格正，即使 p 为负数或非整数，k 仍光滑并平端。真实水平变量由

$$
\omega_s=\frac{k_s}{2h}
=\frac{Kp}{2}h^{p-2}h_s
\tag{3}
$$

确定。更明确地，若 $p\ne1$，

$$
\omega(s)-\omega(s_*)
=\frac{Kp}{2(p-1)}
\left[h(s)^{p-1}-h(s_*)^{p-1}\right];
\tag{4}
$$

若 $p=1$，则

$$
\omega(s)-\omega(s_*)=\frac K2\log\frac{h(s)}{h(s_*)}.
\tag{5}
$$

这也包含 p=0 时 $\omega$ 常值的情形。端部 h、k、$\omega$ 都是实际常值 germs；左右可以不同。每次只使用已选定的有限 p、K 和有限 h 路径，再为这个紧族与补偿统一选择物理支和右锚区间。

由 (2)，

$$
k'=pkv,\qquad k''=pk(v'+pv^2),
\tag{6}
$$

而完整面积因子准确为

$$
v k''-k'z=p(p-1)k v^3.
\tag{7}
$$

它一般不为零；因此 f 在本路径族中必须保留。

## 3. 完整代入与唯一边界消去

定义

$$
q=2p-2
\tag{8}
$$

以及三个系数多项式

$$
A(p)=b+cp+dp^2,
\tag{9}
$$

$$
B(p)=2b+cp(p+1)+2dp^3,
\tag{10}
$$

$$
C(p)=b+cp^2+dp^4
+p(p-1)(e+fp)+gp^2+jp+m.
\tag{11}
$$

把 (6)–(7) 逐项代入 (1)，得到

$$
\int L_4^\lambda[h,K h^p]\,ds
=I_0[h]+K^2\mathscr J_p[h],
\tag{12}
$$

其中

$$
I_0[h]=\int e^{-2r}[a(r''+(r')^2)^2+\ell(r')^4]\,ds,
\tag{13}
$$

$$
\mathscr J_p[h]=
\int e^{qr}\left[
A(p)(r'')^2+B(p)r''(r')^2+C(p)(r')^4
\right]ds.
\tag{14}
$$

式 (11) 中的 $p(p-1)(e+fp)$ 正来自两个完整面积项，没有按正负作估计。$a,\ell$ 属于与 K 无关的 $I_0$，尚未删除。

因为 r 平端，

$$
[e^{qr}(r')^3]_{s_-}^{s_+}=0,
$$

所以

$$
\int e^{qr}r''(r')^2\,ds
=-\frac q3\int e^{qr}(r')^4\,ds.
\tag{15}
$$

定义

$$
D(p)=C(p)-\frac q3 B(p),
\tag{16}
$$

便有准确积分身份

$$
\boxed{\mathscr J_p[h]
=\int e^{qr}[A(p)(r'')^2+D(p)(r')^4]\,ds.}
\tag{17}
$$

## 4. 任意指数权 q 的准确 sharp 比值

对非恒定、有限、光滑平端 r，记

$$
X_q[r]=\int e^{qr}(r'')^2\,ds,\qquad
Y_q[r]=\int e^{qr}(r')^4\,ds>0.
$$

由 (15) 得

$$
\boxed{X_q-\frac{q^2}{9}Y_q
=\int e^{qr}\left(r''+\frac q3(r')^2\right)^2\,ds\ge0.}
\tag{18}
$$

不仅这个下界成立，而且对每个实 q，

$$
\boxed{\inf_r\frac{X_q[r]}{Y_q[r]}=\frac{q^2}{9},}
\tag{19}
$$

下确界在上述真实有限平端类中取。

当 $q=0$ 时，固定任意非恒定平端 $r_0$ 并取 $r=t r_0$。比值是
$t^{-2}X_0[r_0]/Y_0[r_0]$，随有限 t 趋于无穷而趋于 0。每条近似的 h=$e^r$ 仍严格正且有限。

当 $q\ne0$ 时，置 $R=-qr/2$。权重 $e^{qr}=e^{-2R}$，且

$$
\frac{X_q[r]}{Y_q[r]}
=\frac{q^2}{4}
\frac{\int e^{-2R}(R'')^2\,ds}
{\int e^{-2R}(R')^4\,ds}.
\tag{20}
$$

R148 已在真实正平端类证明

$$
\inf_R
\frac{\int e^{-2R}(R''+(R')^2)^2\,ds}
{\int e^{-2R}(R')^4\,ds}=\frac{25}{9}.
$$

而准确边界身份给

$$
\int e^{-2R}(R''+(R')^2)^2\,ds
=\int e^{-2R}(R'')^2\,ds+\frac73\int e^{-2R}(R')^4\,ds.
$$

故 (20) 右侧的第二个比值下确界为 $25/9-7/3=4/9$，得到 (19)。该换元是正函数之间的实际变化，R148 的每条有限正平端近似仍对应一条有限正平端 h；没有使用物理负 h。

对于非恒定有限平端路径，(18) 的严格等号一般不必被取到。本稿只使用准确下确界：若某个目标系数严格负，可先选一条有限近似使其积分已经负，不把无穷极限当作实际路径。

## 5. 固定幂指数的完整 sharp 判据

定义

$$
\Omega(p)=D(p)+\frac{(2p-2)^2}{9}A(p).
\tag{21}
$$

由 (17)–(18)，

$$
\boxed{\mathscr J_p[h]
=A(p)\left[X_q-\frac{q^2}{9}Y_q\right]+\Omega(p)Y_q.}
\tag{22}
$$

**定理 1。** 对固定实 p，$\mathscr J_p[h]\ge0$ 对全部真实正平端 h 成立，当且仅当

$$
\boxed{A(p)\ge0,\qquad \Omega(p)\ge0.}
\tag{23}
$$

充分性直接由 (18)、(22)。若 $A(p)<0$，取 $r=\varepsilon r_0$；$X_q$ 的非零首项为二阶 $\varepsilon^2$，$Y_q$ 为四阶，故足够小的有限 $\varepsilon$ 已使 (17) 负。若 $A(p)\ge0$ 而 $\Omega(p)<0$，当 A>0 时由 sharp 比值 (19) 取足够接近下界的有限平端 r，使

$$
A(p)\left(\frac{X_q}{Y_q}-\frac{q^2}{9}\right)+\Omega(p)<0;
$$

当 A=0 时任一非恒定 r 都给负值。因此必要性也成立。

将 (9)–(11) 代入 (21) 并合并，完整四次多项式为

$$
\boxed{\begin{aligned}
\Omega(p)={}&\frac19\Big[
b(5-2p)^2+c\,p(p+2)(5-2p)
+d\,p^2(p+2)^2\Big]\\
&+p(p-1)(e+fp)+gp^2+jp+m.
\end{aligned}}
\tag{24}
$$

特别地，所有真实正字符都必须满足 (23) 对每个实 p 成立。

在整个实轴上，$A(p)\ge0$ 等价于

$$
b\ge0,\qquad d\ge0,\qquad c^2\le4bd,
\tag{25}
$$

它们与已付加速度 PSD 门一致。新增的实际路径信息在完整 $\Omega$ 中，尤其保留了 f。

## 6. 幂路径子类的完整最高层等价与真实反例顺序

由 (12) 的任意有限实振幅 K，完整最高 action 对所有正平端 h、所有实 p、K 非负，当且仅当

$$
I_0[h]\ge0\quad\text{对所有 h},
\qquad A(p)\ge0,\ \Omega(p)\ge0\quad\text{对所有 p}.
\tag{26}
$$

R148 把第一个条件准确等价为

$$
a\ge0,\qquad \ell+\frac{25}{9}a\ge0.
\tag{27}
$$

所以 (25)、(27) 加全实轴的 (24) 非负，是**全部幂路径子类**上的完整最高 action 充要判据。它不是所有水平 h、k 路径的充要判据。

若某个 p 违反 (23)，按第 5 节先固定一条有限正平端 h，使 $\mathscr J_p[h]<0$。此时 $I_0[h]$ 是已确定的有限数。再选有限 K，满足

$$
K^2>\frac{\max(I_0[h],0)+1}{-\mathscr J_p[h]},
\tag{28}
$$

完整最高 action 便严格负。式 (4)–(5) 给真实平端 $\omega$；h、k、$\omega$ 的整个像仍有界，h 有严格正下界。

最后才对已固定的有限路径作正时间缩放。最高负 action 按 $\delta^{-3}$ 放大，R137 的真实矩阵/frame 补偿及同 k 真倒行，使完整低阶与桥成本被压过；R140 同一乘子也不改变最高层。顺序始终是

$$
\text{有限 p 与 h 形状}\ \longrightarrow\
\text{有限 K}\ \longrightarrow\
\text{共同物理支与补偿族}\ \longrightarrow\
\text{正时长缩放}.
$$

本稿没有将两个振幅或时长极限混为一条实际路径，也不把无穷大 h、k 或未平坦端口默认为合法。

## 7. 与 R167 Gram 证书的准确桥

令 $\alpha=p-1$，定义实向量

$$
\boxed{\zeta(p)=\left(\frac{\alpha^2}{3},\ \alpha,\ -\frac{2\alpha}{3},\ 1\right)^T.}
\tag{29}
$$

R167 使用

$$
Z=(y'',v y',v'y,v^2y)^T,\qquad k=e^r y,
$$

以及两个边界矩阵 $N_1,N_2$。直接代入其二次型，得到

$$
\zeta^TN_1\zeta=0,\qquad \zeta^TN_2\zeta=0.
\tag{30}
$$

确切地，前者是
$\alpha^2/3+\alpha^2-4\alpha^2/3=0$，后者是
$2\alpha+3(-2\alpha/3)=0$。

而 R167 完整矩阵满足

$$
\boxed{\zeta(p)^TG_0\zeta(p)=\Omega(p).}
\tag{31}
$$

可逐项核对：对该向量，

$$
\zeta_1+2\zeta_2+\zeta_3+\zeta_4=\frac{p(p+2)}3,\qquad
\zeta_3+\zeta_4=\frac{5-2p}{3}.
$$

它们给出 (24) 中 b、c、d 的三项；e 项为 $e p(p-1)$，f 项为 $f p^2(p-1)$，g、j、m 项依次为 $gp^2,jp,m$。这正是完整的 (24)。

因此对所有辅助边界参数，

$$
\boxed{\zeta(p)^TG_{\theta,\eta}\zeta(p)=\Omega(p).}
\tag{32}
$$

任何 R167 的半正定充分证书自动蕴含全部幂路径必要门。反过来，$\Omega$ 在全实轴非负只检查这一条向量曲线，不足以推出整个 Gram 矩阵半正定或存在相应辅助参数。

### 7.1 这条 Gram 测试曲线确有真实路径来源

在幂路径上，$y=h^{p-1}=e^{\alpha r}$（振幅可另乘 K）。记

$$
\varepsilon_r=v'+\frac{2\alpha}{3}v^2.
$$

有

$$
\boxed{Z-\zeta(p)Z_4=(\alpha\varepsilon_r y,\ 0,\ \varepsilon_r y,\ 0)^T.}
\tag{33}
$$

由于 $y^2=e^{2\alpha r}=e^{qr}$，

$$
\int|Z-\zeta(p)Z_4|^2\,ds
=(\alpha^2+1)\left[X_q-\frac{q^2}{9}Y_q\right],
\qquad
\int Z_4^2\,ds=Y_q.
\tag{34}
$$

第 4 节的真实 sharp 近似使 (34) 的两个积分之比趋于 0。因而 $\zeta(p)$ 并非对任意独立四单项作的形式赋值，而是由一列真实有限平端路径在准确加权积分意义下逼近的方向。严格负的 $\Omega(p)$ 可沿该列取得有限负成员，再执行第 6 节的完整实际反例构造。

本稿只为这条明确曲线支付可实现性；不能把 R167 任意负特征向量都类比为同样可实现。

## 8. 后继必要系统的最小新接口

在 p=0 时，

$$
\Omega(0)=m+\frac{25}{9}b,
$$

回到完整固定 k sharp 条件中二次于 k 的部分。在 p=1 时，

$$
\Omega(1)=d+g+b+m+c+j,
$$

正是 R165 的 $\gamma$。一般 p 保留 $f p^2(p-1)$，因此补充了长 log-linear 共轭门没有看见的 H2 信息。

对任意固定有理 p，(24) 是同一已发十个字符标量的准确有理线性必要行。若一个未排准确外候选的 $\Omega$ 在实轴有严格负值，连续性保证某个有理 p 也严格违反；可据该候选的四次多项式定向选择一行，而不盲扫 profile、几何或额外模板。

本稿不对任何当前候选代数值，也不更改已冻结 consumer。若该四次门通过，仍须检查 R165 一般固定 h 的二次型、完整低阶耦合和真实函数关系；若能找到 R167 的准确 Gram 证书，则可据其充分性把最高层作整体处理。必要与充分的界限不能交换。

所有来源均是完整真实算子与已发 head 数据。本稿没有新增独立成本维数、signed control、整个正字符不存在或 period/ruling 完成的断言。
